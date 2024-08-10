# coding=utf-8
import random

from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share.RandomUtils import RandomGenerator

"""
向原版奖励箱动态添加奖励
"""


class ChestModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Chest, version=-1)
    def __init__(self):
        super(ChestModule, self).__init__()

    def example(self, system):
        system.addData(
            StaticConfig.Data.CHEST_LOOT,
            {
                # key只用于合并，与其他配置不同即可
                config.ModName
                + ":some_drop": {
                    # 迭代次数
                    "rolls": {
                        # 最少迭代次数
                        "min": 1,
                        # 最大迭代次数
                        "max": 1,
                    },
                    "entries": [
                        {
                            # 权重
                            "weight": 1,
                            # 掉落的物品，参考标准格式http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                            "items": [
                                {
                                    "itemName": "minecraft:bed",
                                    "auxValue": 0,
                                    "count": 1,
                                },
                                {
                                    "itemName": "minecraft:redstone",
                                    "auxValue": 0,
                                    "count": 1,
                                },
                            ],
                        }
                    ],
                },
                # 这种方式展示了如何配置0.1%掉落概率的方案
                config.ModName
                + ":another_drop": {
                    # 迭代次数
                    "rolls": 1,
                    "entries": [
                        {
                            "weight": 1,
                            "items": {
                                "itemName": "minecraft:dirt",
                                "auxValue": 0,
                                "count": 1,
                            },
                        },
                        {"weight": 999, "item": None},
                    ],
                },
            },
        )
