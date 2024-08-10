# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
from mod.client.clientEvent import ClientEvent
from mod.client.system.clientSystem import ClientSystem
from pythonScripts.client.modules.BaseClientModule import BaseClientModule
from pythonScripts.share import EventRegisterUtils as Event


class MyClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.__modules = {}
        self.__loading = True
        self.__data = {}
        self.ListenForEvent(
            clientApi.GetEngineNamespace(),
            clientApi.GetEngineSystemName(),
            ClientEvent.UiInitFinished,
            self,
            self.OnUIInitFinished,
        )
        self.ListenForEvent(
            clientApi.GetEngineNamespace(),
            clientApi.GetEngineSystemName(),
            ClientEvent.LoadClientAddonScriptsAfter,
            self,
            self.LoadClientAddonScriptsAfter,
        )

        from pythonScripts.client import ClientUtils

        Event.utils = ClientUtils
        self._vanillaEvents = []
        self._clientEvents = []
        self._serverEvents = []

    def registerModule(self, module, name, version=0):
        # type: (BaseClientModule,str,int) -> None
        if name not in self.__modules or version > self.__modules[name][1]:
            self.__modules[name] = (module, version)

            module._vanillaEvents = [
                (x[0], x[1]) for x in self._vanillaEvents if x[2] == name
            ]

            module._clientEvents = [
                (x[0], x[1]) for x in self._clientEvents if x[2] == name
            ]

            module._serverEvents = [
                (x[0], x[1]) for x in self._serverEvents if x[2] == name
            ]
            print(
                "registered client module:",
                name,
                ",version:",
                version,
                ",module:",
                module,
            )

    def getModule(self, name):
        if type(name) != str:
            name = name.__class__.__name__
        module = self.__modules.get(name)
        if module is None:
            return None
        else:
            return module[0]

    def Destroy(self):
        for module in list(self.__modules.values()):
            module[0].onDestroy()
        self.UnListenAllEvents()

    def OnUIInitFinished(self, args):
        # print "OnUIInitFinished ", args
        for k, v in list(self.__modules.items()):
            try:
                v[0].onUiInited()
            except Exception as e:
                print(
                    "[ERROR] on init ui! client module:",
                    k,
                    ",version:",
                    v[1],
                    ",module:",
                    v[0],
                )

    def LoadClientAddonScriptsAfter(self, args):
        # print "LoadClientAddonScriptsAfter", args
        sortedData = {}

        def st(param1, param2):
            return param1[0] - param2[0]

        for k, v in list(self.__data.items()):
            finalData = {}
            for version, data in sorted(v, cmp=st):
                finalData.update(data)
            sortedData[k] = finalData
        self.__loading = False
        self.__data = sortedData
        for k, v in list(self.__modules.items()):
            try:
                v[0]._onRegister(self)
                print("enabled client module:", k, ",version:", v[1], ",module:", v[0])
            except Exception as e:
                print(
                    "[ERROR] register client module:",
                    k,
                    ",version:",
                    v[1],
                    ",module:",
                    v[0],
                )
                print("error:", e)

    def addData(self, name, data, version=0):
        if not self.__loading:
            raise Exception("必须在启动流程种注册数据！")
        dataByName = self.__data.get(name, [])
        dataByName.append((version, data))
        self.__data[name] = dataByName

    def getData(self, name):
        if self.__loading:
            raise Exception("数据还在加载中！")
        return self.__data.get(name, {})
