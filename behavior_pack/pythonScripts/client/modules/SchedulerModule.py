# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.share.Scheduler import Scheduler

"""计时器，详细用法见Scheduler"""


class ClientSchedulerModule(Scheduler, BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.Scheduler, version=0)
    def __init__(self):
        super(ClientSchedulerModule, self).__init__()
        BaseClientModule.__init__(self)

    def onRegister(self):
        # print "onRegister", ClientSchedulerModule
        self.listenVanillaEvent(ClientEvent.OnScriptTickClient, self.tick)
        self.startTick()
