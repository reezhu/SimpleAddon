# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *

"""
物品相关的模块
当前功能:
首次登录发放物品
物品右键变成实体
物品替换名称
"""


class ItemDispatchModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.ItemDispatch, version=-1)
    def __init__(self):
        super(ItemDispatchModule, self).__init__()

    def example(self, system):
        # 配置举例
        # 开局会给与玩家的物品
        system.addData(StaticConfig.Data.ITEM_DISPATCH, {
            config.ModName + "guide": {
                "itemName": "fossils_archeology:guide",
                "auxValue": 0,
                "count": 1,
            }
        })
        # 物品放下会变成实体
        system.addData(StaticConfig.Data.ITEM_PLACE_ENTITY, {
            "minecraft:ghast_tear": {
                "entity": "minecraft:ghast",
            }
        })
        # 物品获取后会替换成lore
        system.addData(StaticConfig.Data.ITEM_Lore_Replace, {
            "minecraft:stone": {
                "lore": "%name%\n被玩家${player}拾起于${time}"
            },
            "minecraft:book": {
                "lore": "%name%%category%%enchanting%%attack_damage%"
            }
        })
