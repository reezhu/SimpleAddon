# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *

ScreenNode = clientApi.GetScreenNodeCls()
ThisUi = "org.xjcraft.common.equipment.ui"

SLOT_CHEST = 5
SLOT_HAND = 1
SLOT_ARROW = 7
SLOT_OFFHAND = 3
SLOT_HELMET = 2
SLOT_CHESTPLATE = 4
SLOT_LEGGINGS = 6
SLOT_FOOT = 8

"""这个装备的ui可以拿来参考如何快速的开发一个ui"""


class EquipmentDisplayModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.EquipmentDisplay, version=1)
    def __init__(self):
        super(EquipmentDisplayModule, self).__init__()

    def onRegister(self):
        self.listenServerEvent(StaticConfig.Event.RpcPlayerInfoAnswerEvent, self.AnswerPlayerInfoEvent)
        # self.listenVanillaEvent(ClientEvent.OnKeyPressInGame, self.OnKeyPressInGame)

    def onUiInited(self):
        super(EquipmentDisplayModule, self).onUiInited()
        # ui初始化完成后，注册ui，根据需要来看是否创建，创建时将本module以参数形式传入
        clientApi.RegisterUI(config.ModName, ThisUi, "pythonScripts.client.modules.EquipmentDisplayModule.UiScreen", "redstone_equipment_v2.main")
        clientApi.CreateUI(config.ModName, ThisUi, {"isHud": 1, "module": self})

    def AnswerPlayerInfoEvent(self, args):
        """
        监听BroadcastModule的回调，传入对应的ui
        :param args:
        """
        # print "AnswerPlayerInfoEvent", args
        ui = clientApi.GetUI(config.ModName, ThisUi)  # type: UiScreen
        if ui is not None:
            if args["key"] == "inventory":
                ui.updateInventory(args["result"])
            elif args["key"] == "equipment":
                ui.updateArmor(args["result"])
            elif args["key"] == "hold":
                ui.updateHand(args["result"])
            elif args["key"] == "offhand":
                ui.updateOffhand(args["result"])
            elif str(args["key"]).startswith(StaticConfig.Data.UI_POSITION_PREFIX):
                ui.OnUpdatePosition(args["result"])


# 继承ModularScreen，这个包装的screen中包含了很多功能，比如按钮的拖动
class UiScreen(ModularScreen):
    def __init__(self, namespace, name, param):
        super(UiScreen, self).__init__(namespace, name, param)
        # 把module保存方便调用
        self.module = param.get("module")
        # 有一些可能影响性能的需要手工开关，比如这个开关用来启用UpdatePerSecond
        self._tickAble = True

    def Create(self):
        """
        创建时绑定已生成的按钮，并进行一些初始化功能
        """
        print "UiScreen created"
        self.AddTouchEventHandler("/background", self.move, {"isSwallow": True})

    def UpdateInit(self):
        """
        这个方法只有在ui第一次被tick时才会触发，这比Create会晚一点，有一些Create时并没有创建的空间（比如grid的子控件）可以在这里绑定
        """
        super(UiScreen, self).UpdateInit()
        self.module.NotifyToServer(StaticConfig.Event.RpcPlayerInfoGetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": StaticConfig.Data.UI_POSITION_PREFIX + ThisUi})
        # print self.GetAllChildrenPath("/background/equipments")

    def move(self, args):
        """
        如果要让一个按钮可以长按拖动，就在调用时传给_onClickMovableButton，如果返回的是True代表未拖动，在进行按钮的逻辑
        :param args:
        """
        if self._onClickMovableButton(args):
            pass

    def UpdatePerSecond(self):
        """
        需要持续更新的信息，可以持续向服务端进行请求，这样虽然会浪费一些性能，但是代码来说可以把通讯简化，减少出问题的概率
        """
        super(UiScreen, self).UpdatePerSecond()
        self.module.NotifyToServer(StaticConfig.Event.RpcPlayerInfoGetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": "inventory"})
        self.module.NotifyToServer(StaticConfig.Event.RpcPlayerInfoGetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": "equipment"})
        self.module.NotifyToServer(StaticConfig.Event.RpcPlayerInfoGetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": "hold"})
        self.module.NotifyToServer(StaticConfig.Event.RpcPlayerInfoGetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": "offhand"})

    def updateInventory(self, param):
        """
        可以自己编写方法，对ui进行更新
        :param param:
        """
        empty = 0
        arrow = 0
        for item in param:
            if item is None:
                empty += 1
            elif "arrow" in item["itemName"]:
                arrow += item["count"]
        ItemRender(self, "/background/equipments/equipmentCell%s/equipmentRender" % SLOT_CHEST).setItem("minecraft:chest", 0)
        ItemRender(self, "/background/equipments/equipmentCell%s/equipmentRender" % SLOT_ARROW).setItem("minecraft:arrow", 0)
        ModularComponent(self, "/background/equipments/equipmentCell%s/equipmentText" % SLOT_CHEST).setText(str(empty))
        ModularComponent(self, "/background/equipments/equipmentCell%s/equipmentText" % SLOT_ARROW).setText(str(arrow))

    def updateArmor(self, param):
        for armor, slot in zip(param, [SLOT_HELMET, SLOT_CHESTPLATE, SLOT_LEGGINGS, SLOT_FOOT]):
            item = ItemRender(self, "/background/equipments/equipmentCell%s/equipmentRender" % slot)
            text = ModularComponent(self, "/background/equipments/equipmentCell%s/equipmentText" % slot)
            if armor is None:
                item.setVisible(False)
                text.setText("")
            else:
                item.setItem(armor["itemName"], armor["auxValue"])
                item.setVisible(True)
                info = utils.getItemBasicInfo(armor)
                if armor["durability"] > info["maxDurability"] * 0.75:
                    prefix = "§a"
                elif armor["durability"] > info["maxDurability"] * 0.5:
                    prefix = "§f"
                elif armor["durability"] > info["maxDurability"] * 0.25:
                    prefix = "§e"
                else:
                    prefix = "§4"
                text.setText(prefix + str(armor["durability"]))

    def updateHand(self, param):
        item = ItemRender(self, "/background/equipments/equipmentCell%s/equipmentRender" % SLOT_HAND)
        text = ModularComponent(self, "/background/equipments/equipmentCell%s/equipmentText" % SLOT_HAND)
        if param is None:
            item.setVisible(False)
            text.setText("")
        else:
            item.setItem(param["itemName"], param["auxValue"])
            item.setVisible(True)
            text.setText(str(param["durability"]))

    def updateOffhand(self, param):
        item = ItemRender(self, "/background/equipments/equipmentCell%s/equipmentRender" % SLOT_OFFHAND)
        text = ModularComponent(self, "/background/equipments/equipmentCell%s/equipmentText" % SLOT_OFFHAND)
        if param is None:
            item.setVisible(False)
            text.setText("")
        else:
            item.setItem(param["itemName"], param["auxValue"])
            item.setVisible(True)
            text.setText(str(param["durability"]))

    def OnUploadPosition(self):
        """
        如果需要上报ui的位置，需要复写这个方法，然后把js发送给服务端使用对应的key进行保存，一般规定使用StaticConfig.Data.UI_POSITION_PREFIX加上ui的名称
        :return:
        """
        js = super(UiScreen, self).OnUploadPosition()
        self.module._system.NotifyToServer(StaticConfig.Event.RpcPlayerInfoSetEvent, {"playerId": clientApi.GetLocalPlayerId(), "target": clientApi.GetLocalPlayerId(), "key": StaticConfig.Data.UI_POSITION_PREFIX + ThisUi, "result": js})
        return js
