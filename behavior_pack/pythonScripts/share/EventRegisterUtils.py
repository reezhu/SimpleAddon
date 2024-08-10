# -*- coding: utf-8 -*-
# @Author  : Ree
utils = None
"""事件注解工具类"""


def Vanilla(event_name, module_name):
    # type: (str, str) -> classmethod
    """
    监听原版事件
    :param event_name: 事件str名
    :return:
    """

    def add_event(method):
        system = utils.getSystem()
        system._vanillaEvents.append((event_name, method, module_name))
        return method

    return add_event


def Server(event_name, module_name):
    # type: (str, str) -> classmethod
    """
    监听来自服务端的事件
    :param event_name: 事件的str名
    :return:
    """

    def add_event(method):
        system = utils.getSystem()
        system._serverEvents.append((event_name, method, module_name))
        return method

    return add_event


def Client(event_name, module_name):
    # type: (str) -> classmethod
    """
    监听来自客户端的事件
    :param event_name: 事件的str名
    :return:
    """

    def add_event(method):
        system = utils.getSystem()
        system._clientEvents.append((event_name, method, module_name))
        return method

    return add_event


def Wrapper(cls):
    # type: (callable(object)) -> classmethod
    """
    将事件包装为面向对象的object方便调用
    :param cls: 事件的类（注意不要括号！）
    客户端事件参考cloudpeakSkywarsScripts/share/api/ClientEvents.py
    服务端事件参考cloudpeakSkywarsScripts/share/api/ServerEvents.py
    :return:
    """

    def decorator_function(original_function):

        def wrapper_function(self, args):
            _args = cls()
            _args.__dict__.update(args)
            return original_function(self, _args)

        # hack：兼容网易的反射
        wrapper_function.__module__ = original_function.__module__
        wrapper_function.__name__ = original_function.__name__
        return wrapper_function

    return decorator_function
