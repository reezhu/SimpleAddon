# -*- coding: utf-8 -*-
# @Author  : Ree

import random

from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *

ScreenNode = clientApi.GetScreenNodeCls()
ThisUi = "org.xjcraft.common.barrage.ui"

"""
这是一个通用的弹幕模块
在屏幕上渲染一个从右到左移动的text文本，实现类似bilibili弹幕的功能
开发只需要参考CreateBarrageEvent发的数据包，向客户端广播StaticConfig.Event.CreateBarrageEvent即可
"""


class BarrageModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.Barrage, version=-1)
    def __init__(self):
        super(BarrageModule, self).__init__()

    # {"scale":0.5,"color":(1,1,1,1),"text":"text","speed":1.5,"age":300}
    def CreateBarrageEvent(self, args):
        pass
