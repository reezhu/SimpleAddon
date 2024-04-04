# -*- coding: utf-8 -*-
# @Author  : PengPeng
import copy

import math

from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.share import StringUtils
from pythonScripts.share import VectorUtils

DynamicUi = config.ModName + "DynamicUi"


class DynamicUiModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.DynamicUiModule, version=-1)
    def __init__(self):
        super(DynamicUiModule, self).__init__()

    def CreateDynamicUi(self, name, cfg):
        """
        对外接口，创建动态ui
        @param name: 分配的唯一id
        @param cfg: ui的配置key或完整ui配置
        """
        pass

    def DestroyDynamicUi(self, name):
        """
        对外接口，移除一个动态ui
        @param name:
        """
        pass

    def example(self, system):
        """
        数据格式举例，只用于参考，请配置在modMain.py
        :param system:
        """
        system.addData(StaticConfig.Data.DYNAMIC_UI, {
            # key 為唯一
            "test": {
                "loop": False,  # 是否循環
                "reverseOrder": False,  # 是否倒序，僅在循環開啟時生效，播到最後一張後，從最後一張播回去
                "texturePath": "textures/custom_ui/test",  # 圖片位置，注意填的圖片是主名，檔名為 test1、test2...、test9
                "amount": 9,  # 圖片數量
                "intervalTick": 3,  # 每多少 tick 換一張圖
                "position": (50, 50),  # 圖片左上角的位置, 不填為默認中間, 可填百分比如: ("30%+1", 50) 表示從屏幕長度的 30%+1 與 Y軸向下 50 開始顯示
                "size": (200, 100),  # 圖片左上角開始向右 200、向下 100, 不填為默認圖片長寬比全螢幕, 目前只能等長寬比縮放
                "isUV": True,  # 是否是序列圖，序列圖必須是一橫排
                "layer": 100,  # 该图的层级
                "uvSize": (61, 64),  # 若是 isUV 是 True ，這裡表示每張序列的大小
                "arraySize": 5,  # 有幾排 ，若不填則默認一排
                "tickMotion": (1, 1),  # 每tick移动的位置
                "tickFade": 0.01,  # 每tick增加的透明度
                "tickScale": (1.1, 1.1),  # 每tick进行的缩放
            }
        }, version=0)
