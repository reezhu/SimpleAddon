# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *

ScreenNode = clientApi.GetScreenNodeCls()
ThisUi = "org.xjcraft.common.confirm"

"""
确认弹窗模块
创建时把过滤器filter和回调函数传入即可
"""


class ConfirmModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.Confirm, version=-1)
    def __init__(self):
        super(ConfirmModule, self).__init__()

    def ConfirmPopEvent(self, args):
        text = args.get("text", "")
        icon = args.get("icon", None)
        callback = args.get("callback", None)  # 当callback有event时，会向服务器发回请求
        if callback:
            self.pop(
                text,
                icon,
                callback=lambda res: self.NotifyToServer(
                    callback, {"playerId": clientApi.GetLocalPlayerId(), "result": res}
                ),
            )
        else:
            self.pop(text, icon)

    def pop(self, text, icon=None, callback=None):
        """
        弹出一个确认窗口
        @param text: 文本内容
        @param icon: 图标，默认为红石火把
        @param callback: 回调操作，接收信息为确认与否定
        """
        pass
