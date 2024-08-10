# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
from mod.server.serverEvent import ServerEvent
from mod.server.system.serverSystem import ServerSystem
from pythonScripts.server.modules.BaseServerModule import BaseServerModule
from pythonScripts.share import EventRegisterUtils as Event


class MyServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.__modules = {}
        self.__loading = True
        self.__data = {}
        self.ListenForEvent(
            serverApi.GetEngineNamespace(),
            serverApi.GetEngineSystemName(),
            ServerEvent.LoadServerAddonScriptsAfter,
            self,
            self.LoadServerAddonScriptsAfter,
        )
        from pythonScripts.server import ServerUtils

        Event.utils = ServerUtils
        self._vanillaEvents = []
        self._clientEvents = []
        self._serverEvents = []

    def registerModule(self, module, name, version=0):
        # type: (BaseServerModule,str,int) -> None
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
            print("module", module, module._vanillaEvents)
            print(
                "registered server module:",
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

    def LoadServerAddonScriptsAfter(self, args):
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
            v[0]._onRegister(self)
            print("enabled server module:", k, ",version:", v[1], ",module:", v[0])

    def addData(self, name, data, version=0):
        if not self.__loading:
            raise Exception("必须在启动流程中注册数据！")
        dataByName = self.__data.get(name, [])
        dataByName.append((version, data))
        self.__data[name] = dataByName

    def getData(self, name):
        if self.__loading:
            raise Exception("数据还在加载中！")
        return self.__data.get(name, {})
