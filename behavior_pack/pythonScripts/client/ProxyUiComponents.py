# -*- coding: utf-8 -*-
# @Author  : Ree
import mod.client.extraClientApi as clientApi

# from mod.client.ui.controls.baseUIControl import BaseUIControl
from mod.client.ui.screenNode import ScreenNode

ProxyScreenNode = clientApi.GetCustomUIControlProxyCls()  # type:ScreenNode


class ModularProxyScreen(ProxyScreenNode):
    def __init__(self, customData, customUIControl):
        ProxyScreenNode.__init__(self, customData, customUIControl)
        self.__init = False

    def GetCustomUIControl(self):
        # type: () -> BaseUIControl
        return ProxyScreenNode.GetCustomUIControl(self)

    def OnCreate(self):
        pass

    def OnDestroy(self):
        pass

    def OnInit(self):
        pass

    def OnTick(self):
        if not self.__init:
            self.__init = True
            self.OnInit()

    def _isTouchUpEvent(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]

        return touchEvent == touchEventEnum.TouchUp

    def _isTouchDownEvent(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]

        return touchEvent == touchEventEnum.TouchDown


class ModularComponent:
    _screenNode = None  # type: ProxyScreenNode
    _instance = None  # type:BaseUIControl

    def __init__(self, screenNode, path):
        self._screenNode = screenNode
        self._path = path
        self._instance = screenNode.GetCustomUIControl().GetChildByName(path)

    def __getattr__(self, item):
        return self._instance.__getattribute__(self, item)


class ImageButton(ModularComponent):

    def __init__(self, screenNode, buttonPath):
        ModularComponent.__init__(self, screenNode, buttonPath)
        self._instance = self._instance.asButton()

    def SetButtonTouchUpCallback(self, callback):
        self._instance.AddTouchEventParams({"isSwallow": True})
        self._instance.SetButtonTouchUpCallback(callback)
