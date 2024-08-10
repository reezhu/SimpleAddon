# -*- coding: utf-8 -*-

from mod.common.mod import Mod

import pythonScripts.share.ModConfig as config
from pythonScripts.client.MyClientSystem import MyClientSystem
from pythonScripts.server.MyServerSystem import MyServerSystem
from pythonScripts.share import StaticConfig


@Mod.Binding(name=config.ModName, version=config.ModVersion)
class Boostrap(object):
    def registerServerModules(self, system):
        config.registerServerModules(system)

    def registerClientModules(self, system):
        config.registerClientModules(system)

    def registerData(self, system):
        config.registerData(system)

    def __init__(self):
        print("init mod", config.ModName, "@", config.ModVersion)

    @Mod.InitServer()
    def ServerInit(self):
        print("init server", config.ModName, "@", config.ModVersion)
        from pythonScripts.server import ServerUtils
        system = ServerUtils.getSystem()  # type: MyServerSystem
        if system is None:
            print("register server system @", config.ModName, config.ModVersion)
            system = ServerUtils.registerSystem(path="pythonScripts.server.MyServerSystem.MyServerSystem")
            print("register server finish:", StaticConfig.ServerSystemName)

        self.registerServerModules(system)
        self.registerData(system)

    @Mod.DestroyServer()
    def ServerDestroy(self):
        print("destroy server", config.ModName, "@", config.ModVersion)

    @Mod.InitClient()
    def ClientInit(self):
        print("init client", config.ModName, "@", config.ModVersion)
        from pythonScripts.client import ClientUtils
        system = ClientUtils.getSystem()  # type: MyClientSystem
        if system is None:
            print("register client system @", config.ModName, config.ModVersion)
            system = ClientUtils.registerSystem(path="pythonScripts.client.MyClientSystem.MyClientSystem")
            print("register client finish:", StaticConfig.ClientSystemName)

        self.registerClientModules(system)
        self.registerData(system)

    @Mod.DestroyClient()
    def ClientDestroy(self):
        print("destroy client", config.ModName, "@", config.ModVersion)
