# -*- coding: utf-8 -*-
# @Author  : Ree
import re

from pythonScripts.server.modules.BaseServerModule import *

"""placeholder模块"""


class PlaceHolderModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.PlaceHolder, version=-1)
    def __init__(self):
        super(PlaceHolderModule, self).__init__()

    def registerProcessor(self, key, processor, force=False):
        """
        使用代码注册处理器
        :param key:
        :param processor: 入参为playerId的静态方法或是模块与方法的dict
        """
        pass

    def compile(self, playerId, inputText):
        """
        替换文本
        @param playerId: 玩家
        @param inputText: 文本
        """
        pass

    def time(self, player, *args):
        print "time", args
        from datetime import datetime
        if len(args) > 0 and args[0] == "0":
            date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        elif len(args) > 0 and args[0] == "1":
            date = datetime.now().strftime('%Y-%m-%d')
        else:
            date = datetime.now().strftime('%H:%M:%S')
        return date

    def example(self, system):
        system.addData(StaticConfig.Data.PLACEHOLDER, {
            # 调用工具类
            "player": utils.getName,
            "pos": utils.getPos,
            # 调用模块方法
            "time": {
                "module": StaticConfig.Module.PlaceHolder,
                "function": "time"
            },
        }, version=0)

    # 这是一个打印玩家聊天记录的例子
    # @Event.Vanilla(ServerEvent.ServerChatEvent)
    def ServerChatEvent(self, args):
        print self.compile(args["playerId"], "[${time:0}]${name}说：" + args["message"])
