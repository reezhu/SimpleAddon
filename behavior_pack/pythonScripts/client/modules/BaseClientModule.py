# -*- coding: utf-8 -*-
# @Author  : Ree
from functools import wraps

import mod.client.extraClientApi as clientApi
from mod.client.clientEvent import ClientEvent

import pythonScripts.share.ModConfig as config
import pythonScripts.share.api.ClientEvents as EventObj
from pythonScripts.client import ClientUtils as utils
from pythonScripts.share import EventRegisterUtils as Event
from pythonScripts.share import StaticConfig

"""
通用基类，勿动
"""


def DefaultClientModule(name, version=0):
    """
    由于python自身缺陷，此注解只能用在构造器上
    :param name:
    :param version:
    :return:
    """

    def registerSystem(func):
        tempName = name
        tempVersion = version

        @wraps(func)
        def onInvoke(self, *args, **kwargs):
            name = func.__name__ if tempName is None else tempName
            version = tempVersion
            module = func(self, *args, **kwargs)
            # print "default module...",
            utils.getSystem().registerModule(self, name=name, version=version)
            return module

        return onInvoke

    return registerSystem


class BaseClientModule(object):
    def __init__(self):
        from pythonScripts.client.MyClientSystem import MyClientSystem
        self._system = utils.getSystem()  # type: MyClientSystem
        self.config = config

        self._vanillaEvents = []
        self._clientEvents = []
        self._serverEvents = []
        if Event is not None:
            pass  # 用于格式化时保留引用
        if ClientEvent is not None:
            pass  # 用于格式化时保留引用
        if EventObj is not None:
            pass  # 用于格式化时保留引用

    def _onRegister(self, system):
        self._system = system
        self.onRegister()
        for event, method in self._vanillaEvents:
            self.listenVanillaEvent(event, method)
        for event, method in self._clientEvents:
            self.listenClientEvent(event, method)
        for event, method in self._serverEvents:
            self.listenServerEvent(event, method)

    def onRegister(self):
        pass

    def onUiInited(self):
        pass

    def listenVanillaEvent(self, event, method):
        self._system.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), event, self, method)

    def listenServerEvent(self, event, method):
        self._system.ListenForEvent(StaticConfig.ServiceDomain, StaticConfig.ServerSystemName, event, self, method)

    def listenClientEvent(self, event, method):
        self._system.ListenForEvent(StaticConfig.ServiceDomain, StaticConfig.ClientSystemName, event, self, method)

    def onDestroy(self):
        pass

    def getData(self, name):
        return self._system.getData(name)

    def NotifyToServer(self, event, eventData):
        eventData["playerId"] = clientApi.GetLocalPlayerId()
        self._system.NotifyToServer(event, eventData)

    def printEvent(self, args):
        print("onEvent: ", args if type(args) is dict else args.__dict__)
