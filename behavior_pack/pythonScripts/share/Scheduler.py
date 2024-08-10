# -*- coding: utf-8 -*-
import collections

import _thread
import time

"""调度器"""


class Scheduler(object):

    def __init__(self):
        self.__start = False
        self.__ticks = 0
        self.__task_id = 0
        self.__tasks = {}
        self.__balanceTasks = collections.deque([])
        self.__cancel_obj = []

    def startTick(self):
        """
        开始计时器，需要在系统加载完成后启动
        """
        self.__start = True

    def __sizeof__(self):
        return len(self.__tasks) + len(self.__balanceTasks)

    def tick(self):
        """
        tick主线程，需要挂在服务端或客户端事件上
        """
        if self.__start is True:
            # 移除取消的任务
            for cancel in self.__cancel_obj:
                if cancel in self.__tasks:
                    del self.__tasks[cancel]
            self.__ticks += 1

            # 普通任务
            self.__tickNormalTasks()

            # 弹性任务，如果运行时间超过0.01s将会推迟到下个tick
            self.__tickBalancedTasks()

    def __tickBalancedTasks(self):
        # count = 0
        timeout = time.time() + 0.02
        while len(self.__balanceTasks) > 0:
            ls = self.__balanceTasks[0]
            while len(ls) > 0:
                # count += 1
                # if count > 20:
                if time.time() >= timeout:
                    # print "scheduler timeout."
                    return
                # elif count > 800:
                # print "scheduler maximum."
                # return
                task = ls.popleft()
                task[0](*task[1])
            self.__balanceTasks.popleft()

    def __tickNormalTasks(self):
        for key, dicts in list(self.__tasks.items()):
            if dicts["func"].isCanceled() is True:
                del self.__tasks[key]
            elif dicts["later"] <= self.__ticks:
                try:
                    if dicts.get("asyc", False) is True:
                        _thread.start_new_thread(dicts["func"].run, ())
                    else:
                        dicts["func"].run()
                except Exception as e:
                    print("Error running task", dicts["func"].__dict__, e)
                if "interval" in dicts and dicts["func"].isCanceled() is False:
                    dicts["later"] = self.__ticks + dicts["interval"]
                elif key in self.__tasks:
                    del self.__tasks[key]

    def clearAll(self):
        """
        移除所有进程
        """
        del self.__tasks[:]

    def runFuncTaskLater(self, later, func, *args, **kwargs):
        # type: (int, callable, *object, **object) -> object
        '''
        添加稍后执行的任务
        :param later:
        :param func:
        :param args:
        :param kwargs:
        :return:
        '''
        if not func:
            return
        defaultRunable = DefaultRunnable(func, *args, **kwargs)
        return self.runTaskLater(later, defaultRunable)

    def runTaskLater(self, later, func):
        # type: (int, Runnable) -> int
        """
        添加稍后执行的任务
        :param later:
        :param func:
        :return:
        """
        later = self.__ticks + later + 1
        self.__task_id += 1
        func.setTaskId(self.__task_id)
        item = {"id": self.__task_id, "later": later, "func": func}
        self.__tasks[self.__task_id] = item
        # print "添加task", item
        return self.__task_id

    def runFuncBalancedTaskLater(self, later, func, *args):
        # type: (int, callable,*object) -> None
        """
        添加稍后执行的弹性操作,超时会推迟到下tick
        :param later:
        :param func:
        :return:
        """
        # later = self.__ticks + later + 1
        # self.__task_id += 1
        # func.setTaskId(self.__task_id)
        while len(self.__balanceTasks) < later:
            self.__balanceTasks.append(collections.deque([]))
        ls = self.__balanceTasks[later - 1]
        ls.append((func, args))
        # self.__balanceTasks[self.__task_id] = item
        # print "添加task", item
        # return self.__task_id

    def runFuncAsycTaskLater(self, later, func, *args, **kwargs):
        # type: (int,  callable, *object,**object) -> int
        '''
        添加稍后执行的异步操作
        :param later:
        :param func:
        :param args:
        :param kwargs:
        :return:
        '''
        defaultRunable = DefaultRunnable(func, *args, **kwargs)
        return self.runAsycTaskLater(later, defaultRunable)

    def runAsycTaskLater(self, later, func):
        # type: (int, Runnable) -> int
        """
        添加稍后执行的异步操作
        :param later:
        :param func:
        :return:
        """
        later = self.__ticks + later + 1
        self.__task_id += 1
        func.setTaskId(self.__task_id)
        item = {"id": self.__task_id, "later": later, "func": func, "asyc": True}
        self.__tasks[self.__task_id] = item
        # print "添加task", item
        return self.__task_id

    def runFuncTaskTimer(self, later, interval, func, *args, **kwargs):
        # type: (int, int, callable, *object, **object) -> int
        '''
        添加稍后执行的周期性循环操作
        :param later:
        :param interval:
        :param func:
        :param args:
        :param kwargs:
        :return:
        '''
        defaultRunable = DefaultRunnable(func, *args, **kwargs)
        return self.runTaskTimer(later, interval, defaultRunable)

    def runTaskTimer(self, later, interval, func):
        # type: (int, int, Runnable) -> int
        """
        添加稍后执行的周期性循环操作
        :param later:
        :param interval:
        :param func:
        :return:
        """
        later = self.__ticks + later + 1
        self.__task_id += 1
        func.setTaskId(self.__task_id)
        self.__tasks[self.__task_id] = {"id": self.__task_id, "later": later, "interval": interval, "func": func}
        return self.__task_id

    def cancelTaskById(self, task_id):
        # type: (int) -> None
        """
        按进程id移除进程,负载均衡进程无法取消
        :param task_id:
        """
        # print("Cancel task:", task_id)
        if task_id in self.__tasks or task_id in self.__balanceTasks:
            self.__cancel_obj.append(task_id)


class Runnable:
    task_id = -1
    __cancel = False

    def __init__(self):
        pass

    def run(self):
        pass

    def setTaskId(self, task_id):
        self.task_id = task_id

    def cancel(self):
        self.__cancel = True

    def isCanceled(self):
        return self.__cancel


class DefaultRunnable(Runnable):
    '''
    默认的runable
    '''

    def __init__(self, func, *args, **kwargs):
        # type: (callable, *object, **object) -> None
        Runnable.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            if not self.kwargs and not self.args:
                self.func()
            elif not self.kwargs:
                self.func(*self.args)
            else:
                self.func(*self.args, **self.kwargs)
        except:
            import traceback
            traceback.print_exc()
