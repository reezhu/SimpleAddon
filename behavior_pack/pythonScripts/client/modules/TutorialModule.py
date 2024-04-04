# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *

"""
todo 改成纯配置模式
"""
ScreenNode = clientApi.GetScreenNodeCls()
TutorialUi = config.ModName + "TutorialUi"
# 这里配置触发使用的物品
GuideItem = "minecraft:compass"
# 这里配置目录
Index = [
    {"text": "",  # 显示文本
     "tx": "textures/items/book/introduce",  # 默认状态贴图
     "txp": "textures/items/book/introduce",  # 当前是这一页时的贴图
     "jump": 0},  # 点击后跳到哪一页
    {"text": "",
     "tx": "textures/items/book/dragon",
     "txp": "textures/items/book/dragon",
     "jump": 1},
    {"text": "",
     "tx": "textures/items/book/tool",
     "txp": "textures/items/book/tool",
     "jump": 6},
    {"text": "",
     "tx": "textures/items/book/equip",
     "txp": "textures/items/book/equip",
     "jump": 9},
    {"text": "",
     "tx": "textures/items/book/food",
     "txp": "textures/items/book/food",
     "jump": 11}
]
# 这里配置内容
Content = [
    {
        "image": "textures/items/book/1",  # 图片内容
        "text": ""  # 文字内容（不推荐使用）
    },
    {
        "image": "textures/items/book/2",
        "text": ""
    },
    {
        "image": "textures/items/book/3",
        "text": ""
    },
    {
        "image": "textures/items/book/4",
        "text": ""
    },
    {
        "image": "textures/items/book/5",
        "text": ""
    },
    {
        "image": "textures/items/book/6",
        "text": ""
    },
    {
        "image": "textures/items/book/7",
        "text": ""
    },
    {
        "image": "textures/items/book/8",
        "text": ""
    },
    {
        "image": "textures/items/book/9",
        "text": ""
    },
    {
        "image": "textures/items/book/10",
        "text": ""
    },
    {
        "image": "textures/items/book/11",
        "text": ""
    },
]

"""教程模块，因为不需要单例，所以手工注册"""


class TutorialModule(BaseClientModule):
    def __init__(self):
        super(TutorialModule, self).__init__()

    def onUiInited(self):
        clientApi.RegisterUI(config.ModName, TutorialUi, "pythonScripts.client.modules.TutorialModule.UiScreen", "redstone_tutorial_v2.main")

    def onRegister(self):
        # self.listenVanillaEvent(ClientEvent.OnKeyPressInGame, self.OnKeyPressInGame)
        self.listenVanillaEvent(ClientEvent.OnCarriedNewItemChangedClientEvent, self.OnCarriedNewItemChangedClientEvent)
        self.listenVanillaEvent("GridComponentSizeChangedClientEvent", self.GridComponentSizeChangedClientEvent)
        self.listenVanillaEvent("ClientItemUseOnEvent", self.ClientItemUseOnEvent)

    def OnKeyPressInGame(self, data):
        # print "OnKeyPressInGame", data
        if data.get("key") == "96" and data.get("isDown") == "0":
            self.OnCarriedNewItemChangedClientEvent({"itemName": GuideItem})

    def ClientItemUseOnEvent(self, args):
        if args["itemDict"] is not None and args["itemDict"]["itemName"] == GuideItem:
            ui = clientApi.GetUI(config.ModName, TutorialUi)
            if ui is None:
                clientApi.CreateUI(config.ModName, TutorialUi, {"isHud": 0})

    def OnCarriedNewItemChangedClientEvent(self, args):
        name = args["itemName"]
        if name == GuideItem:
            ui = clientApi.GetUI(config.ModName, TutorialUi)
            if ui is None:
                clientApi.CreateUI(config.ModName, TutorialUi, {"isHud": 0})

    def GridComponentSizeChangedClientEvent(self, args):
        ui = clientApi.GetUI(config.ModName, TutorialUi)  # type:UiScreen
        if ui is not None:
            ui.updateGrid()


class UiScreen(ModularScreen):
    def __init__(self, namespace, name, param):
        super(UiScreen, self).__init__(namespace, name, param)
        self.__Grid = ScrollingPanel(self, "/background/homepage/index")
        self.page = param.get("page", 0)
        self.__index = None
        self._image = Image(self, "/background/page/image")
        self._text = ModularComponent(self, "/background/page/text")
        self._paginationLeft = ModularComponent(self, "/background/page/paginationLeft")
        self._paginationRight = ModularComponent(self, "/background/page/paginationRight")
        self.touchHandler = {}

    def Create(self):
        print "Create with page:", self.page, self.GetAllChildrenPath("/background/homepage/index")
        self.AddTouchEventHandler("/background/operation/left", self.LastPage, {"isSwallow": True})
        self.AddTouchEventHandler("/background/operation/right", self.NextPage, {"isSwallow": True})
        self.AddTouchEventHandler("/background/operation/close", self.Close, {"isSwallow": True})
        self.SetGridDimension(self.__Grid.getContentPath(), (1, len(Index)))

        self.SetSize(self.__Grid.getContentPath(), (self.GetSize(self.__Grid.getContentPath())[0], 25 * len(Index)), True)
        self.refreshContent()

    def updateGrid(self):
        paths = self.GetChildrenName(self.__Grid.getContentPath())
        print "paths", paths
        if paths:
            for path in paths:
                order = int(path.replace("button", "")) - 1
                buttonPath = self.__Grid.getContentPath() + "/" + path

                if buttonPath not in self.touchHandler:
                    button = self.touchHandler[buttonPath] = ImageButton(self, buttonPath)
                    self.AddTouchEventHandler(buttonPath, self.OnClick, {"isSwallow": True})
                else:
                    button = self.touchHandler[buttonPath]
                button.setText(Index[order].get("text", ""))
                button.setAllStateImages(Index[order].get("tx", "textures/netease/common/button/default") if Index[order].get("jump", 0) != self.page else Index[order].get("txp", "textures/netease/common/button/pressed"))

    def refreshContent(self):
        self.page = max(0, min(self.page, len(Content) - 1))
        content = Content[self.page]

        self._image.setImage(content.get("image"))
        self._text.setText(content.get("text", ""))
        self._paginationLeft.setText("%s/%s" % (self.page * 2 + 1, len(Content) * 2))
        self._paginationRight.setText("%s/%s" % (self.page * 2 + 2, len(Content) * 2))
        self.updateGrid()

    def OnClick(self, data):
        if data["TouchEvent"] == 0:
            buttonPath = data["ButtonPath"]
            index = str(buttonPath).replace(self.__Grid.getContentPath() + "/button", "")
            index = int(index) - 1
            entry = Index[index]
            old = self.page
            self.page = entry.get("jump", self.page)
            print "on click", data, old, self.page
            if old == self.page:
                return
            else:
                self.refreshContent()

    def LastPage(self, args):
        if args["TouchEvent"] == 0:
            # print "LastPage", args
            self.page -= 1
            self.refreshContent()

    def NextPage(self, args):
        if args["TouchEvent"] == 0:
            # print "NextPage", args
            self.page += 1
            self.refreshContent()

    def Close(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        touchEvent = args["TouchEvent"]
        if touchEvent == touchEventEnum.TouchUp:
            self.SetRemove()
