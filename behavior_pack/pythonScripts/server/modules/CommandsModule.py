# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share.api.SyncApi import SyncApi

"""一个示例的指令模块，可以在这里写一些测试"""


class CommandsModule(BaseServerModule):
    def __init__(self):
        super(CommandsModule, self).__init__()
        self.__commands = {
            "effect": self.effect,
            "cool": self.cool,
            "health": self.health,
            "explosion": self.explosion,
            "sync": self.sync,
        }

    def onRegister(self):
        pass

    #     self.listenVanillaEvent(ServerEvent.ServerChatEvent, self.ServerChatEvent)
    @Event.Vanilla(ServerEvent.ServerChatEvent)
    def ServerChatEvent(self, args):
        # print "ServerChatEvent", args
        playerId = args["playerId"]
        message = str(args["message"])
        param = message.split(" ")
        if len(param) > 0:
            if param[0] in self.__commands:
                self.__commands[param[0]](playerId, param[1:])

    def effect(self, playerId, params):
        print "effect", playerId, params
        utils.addEffect(playerId, params[0], int(params[1]), int(params[2]))

    def cool(self, playerId, params):
        print "cool", playerId, params
        self.NotifyToClient(playerId, StaticConfig.Event.EquipmentCooldownReduceEvent, {"key": params[0], "time": int(params[1])})

    def health(self, playerId, params):
        print "cool", playerId, utils.getEntityAttr(playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH), utils.getEntityMaxAttr(playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH)

    def explosion(self, playerId, params):
        print "explosion", params
        radius = int(params[0])
        scheduler = utils.getModule(StaticConfig.Module.Scheduler)
        scheduler.runFuncTaskLater(30, utils.createOptimizeExplosion, playerId, utils.getDimension(playerId), utils.getFootPos(playerId), radius, 1, 3, True)
        # print utils.createOptimizeExplosion(playerId, utils.getDimension(playerId), utils.getFootPos(playerId), radius, 1, 3)

    def sync(self, playerId, params):
        module = utils.getModule(StaticConfig.Module.Sync)  # type:SyncApi
        print "before test", module.getAll(playerId)
        from random import random
        module.set(playerId, "test", random())
        print "after test", module.getAll(playerId)
