# -*- coding: utf-8 -*-
# @Author  : Ree

import random

from pythonScripts.server.modules.BaseServerModule import *

"""掉落物模块，可以动态增加掉落物，并且进行不同mod之间的合并"""


class LootModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.LootModule, version=-1)
    def __init__(self):
        super(LootModule, self).__init__()

    def example(self, system):
        # 生物用代码掉落，控制一些无法用子id的东西
        system.addData(
            StaticConfig.Data.MOB_LOOT,
            {
                # 生物identifier
                "dayz:zombie_normal": [
                    {
                        # 掉落概率
                        "possibility": 0.2,
                        # 掉落的物品，参考标准格式http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                        "item": {
                            "itemName": "opweapon:genyuan",
                            "auxValue": 0,
                            "count": 1,
                        },
                    },
                ],
            },
        )
        # 这里的记录每个生物死亡都会触发
        system.addData(
            StaticConfig.Data.MOB_LOOT_GLOBAL,
            {
                # 任意id
                "drop_something": [
                    {
                        # 掉落概率
                        "possibility": 0.2,
                        # 掉落的物品，参考标准格式http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                        "item": {
                            "itemName": "opweapon:genyuan",
                            "auxValue": 0,
                            "count": 1,
                        },
                    },
                ],
            },
        )
        # 方块用代码掉落，控制一些无法用子id的东西
        system.addData(
            StaticConfig.Data.BLOCK_LOOT,
            {
                # 方块identifier
                "minecraft:stone": [
                    {
                        # 掉落概率
                        "possibility": 0.2,
                        # 掉落的物品，参考标准格式http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                        "item": {
                            "itemName": "opweapon:nengliang",
                            "auxValue": 0,
                            "count": 1,
                        },
                    },
                ],
            },
        )
        # 这里的记录每个方块破坏都会触发
        system.addData(
            StaticConfig.Data.BLOCK_LOOT_GLOBAL,
            {
                # 任意id
                "drop_something": [
                    {
                        # 掉落概率
                        "possibility": 0.2,
                        # 掉落的物品，参考标准格式http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                        "item": {
                            "itemName": "opweapon:nengliang",
                            "auxValue": 0,
                            "count": 1,
                        },
                    },
                ],
            },
        )
