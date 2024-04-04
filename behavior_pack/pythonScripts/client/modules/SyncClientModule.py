# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.share.api.SyncApi import SyncApi

ScreenNode = clientApi.GetScreenNodeCls()
ThisUi = "org.xjcraft.common.confirm"

"""通用同步模块，接口见SyncApi"""


class SyncClientModule(BaseClientModule, SyncApi):
    @DefaultClientModule(name=StaticConfig.Module.Sync, version=1)
    def __init__(self):
        super(SyncClientModule, self).__init__()
