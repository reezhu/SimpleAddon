# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share.api.SyncApi import SyncApi

"""通用同步模块，接口见SyncApi"""


class SyncServerModule(BaseServerModule, SyncApi):
    @DefaultServerModule(name=StaticConfig.Module.Sync, version=-1)
    def __init__(self):
        super(SyncServerModule, self).__init__()
