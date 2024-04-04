# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.ProxyUiComponents import *
from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.client.modules.DecoratorMainModule import version as moduleVersion

ScreenNode = clientApi.GetCustomUIControlProxyCls()
"""
这是饰品模块，也是在原生ui上添加元素的例子
"""


class DecoratorModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.DecoratorModule, version=moduleVersion)
    def __init__(self):
        super(DecoratorModule, self).__init__()

    def onRegister(self):
        pass

    def onUiInited(self):
        super(DecoratorModule, self).onUiInited()
        # 需要把ui注册到对应的位置，这里注意可以不引用main而是screen下的元素
        manager = clientApi.GetNativeScreenManagerCls().instance()
        manager.RegisterCustomControl(clientApi.GetMinecraftEnum().NativeScreenDataType.POCKET_INVENTORY_CONTENT_PANEL, "redstone_decorator_v2.screen_pocket", "pythonScripts.client.modules.DecoratorModule.UiProxyScreen")
        manager.RegisterCustomControl(clientApi.GetMinecraftEnum().NativeScreenDataType.INVENTORY_CONTENT_PANEL, "redstone_decorator_v2.screen", "pythonScripts.client.modules.DecoratorModule.UiProxyScreen")


# 覆盖在原生ui上的ui需要继承ModularProxyScreen，注意它的生命周期函数与普通的不同，使用的Components也写法不同，初始化的传参也不同，无法传入参数
class UiProxyScreen(ModularProxyScreen):
    def __init__(self, customData, customUIControl):
        ModularProxyScreen.__init__(self, customData, customUIControl)

    def OnInit(self):
        """
        创建时绑定已生成的按钮，并进行一些初始化功能
        """
        print "UiScreen created"
        button = ImageButton(self, "button0")
        button.SetButtonTouchUpCallback(self.open)

    def open(self, args):
        if self._isTouchUpEvent(args):
            # print "click button", args
            from pythonScripts.client.modules.DecoratorMainModule import ThisUi as SelectUi
            clientApi.PushScreen(StaticConfig.ServiceDomain, SelectUi)
