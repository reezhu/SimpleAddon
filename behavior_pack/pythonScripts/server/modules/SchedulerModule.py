# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share.Scheduler import Scheduler

"""计时器，详细用法见Scheduler"""


class ServerSchedulerModule(BaseServerModule, Scheduler):
    @DefaultServerModule(name=StaticConfig.Module.Scheduler, version=-1)
    def __init__(self):
        super(ServerSchedulerModule, self).__init__()
        Scheduler.__init__(self)

    def onRegister(self):
        self.listenVanillaEvent(ServerEvent.OnScriptTickServer, self.tick)
        self.startTick()
