# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.client.modules.BaseClientModule import *

"""
浮动文本功能
只要发送StaticConfig.Event.ClientTextEvent到客户端即可
参考发送格式{"entityId":生物id,"pos":位置,"info":文本,"color":文本颜色,"size":大小,"depth":是否有深度遮挡,}默认数值见TextEvent
"""


class ClientTextFloatModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.TextFloat, version=-1)
    def __init__(self):
        super(ClientTextFloatModule, self).__init__()
        # 当前tick进度
        self.tick = 0
        # 字符面板数据    textId:{'damage':damage, 'tick':tick}
        self.textDict = {}

    # {"entityId":-1,"pos":(1,1,1),"info":"text","size":(1,1,1),"color":(1,1,1),"depth":True}
    def TextEvent(self, data):
        # print "TextEvent", data
        entityId = data["entityId"]
        pos = data["pos"]
        info = data["info"]
        color = data.get("color", (1, 1, 1))
        size = data.get("size", (1, 1, 1))
        depth = data.get("depth", True)
        if utils.getPos(entityId) is not None:
            self.addMessagePop(entityId, pos, info, color, size, depth)

    def addMessagePop(self, entityId, pos, info, color, size=(1, 1, 1), depth=True):
        """
        添加一个字符面板
        :param size:
        :param entityId:
        :param pos:
        :param info:
        :param color:
        :return:
        """
        pass
