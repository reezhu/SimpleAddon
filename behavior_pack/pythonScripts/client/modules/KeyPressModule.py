# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.modules.BaseClientModule import *

"""这是一个监听键盘按键的示例"""


def response(args):
    print("question is ", args)
    return {"answer": "pong"}


class KeyPressModule(BaseClientModule):
    def __init__(self):
        super(KeyPressModule, self).__init__()
        self.profile_server = False
        self.profile_client = False

    def onRegister(self):
        pass

    #     self.listenVanillaEvent(ClientEvent.OnKeyPressInGame, self.OnKeyPressInGame)
    @Event.Vanilla(ClientEvent.OnKeyPressInGame)
    @Event.Wrapper(EventObj.OnKeyPressInGame)
    def OnKeyPressInGame(self, data):
        # type: (EventObj.OnKeyPressInGame) -> None

        if data.isDown == "0":
            print("OnKeyPressInGame", data.__dict__)
            if data.key == "100":
                utils.getModule(StaticConfig.Module.InventorySelector).pop(callback=lambda index, item: index % 2 == 0, filter=lambda item: True)
            elif data.key == "101":
                # rpc模块的例子
                def callback(args):
                    print("answer is ", args)

                utils.getModule(StaticConfig.Module.Rpc).sendRequest(response, {"question": "ping", }, callback)
            elif data.key == "102":
                # 同步模块的例子
                module = utils.getModule(StaticConfig.Module.Sync)  # type:SyncApi
                print("before test", module.getAll(clientApi.GetLocalPlayerId()))
                from random import random
                def onCallback():
                    print("after test", module.getAll(clientApi.GetLocalPlayerId()))

                utils.getModule(StaticConfig.Module.Scheduler).runFuncTaskLater(1, onCallback)
                module.set(clientApi.GetLocalPlayerId(), "test", random(), override=True)
                module.set(clientApi.GetLocalPlayerId(), "test", random(), override=False)  # 这会触发异常
            elif data.key == "104":
                self.profile_server = not self.profile_server
                if self.profile_server:
                    clientApi.StartProfile()
                    print("Start Client Profile")
                else:
                    clientApi.StopProfile("flame_client.html")
                    print("Stop Client Profile")
            elif data.key == "105":
                self.profile_client = not self.profile_client
                import mod.server.extraServerApi as serverApi
                if self.profile_client:
                    serverApi.StartProfile()
                    print("Start Server Profile")
                else:
                    serverApi.StopProfile("flame_server.html")
                    print("Stop Server Profile")
