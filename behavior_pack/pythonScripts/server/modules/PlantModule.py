# -*- coding: utf-8 -*-
# @Author  : Ree


from pythonScripts.server.modules.BaseServerModule import *

"""种植相关模块，用法见example"""


class PlantModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Plant, version=-1)
    def __init__(self):
        super(PlantModule, self).__init__()

    def example(self, system):
        # 可以被骨粉扩散的植物
        system.addData(
            StaticConfig.Data.PLANT_SPREAD,
            {
                "tofucraft:blockleek": {
                    # 生成的方块
                    "target": ["tofucraft:blockleek"],
                    # 生成的概率
                    "rate": 0.5,
                    # 尝试次数
                    "count": 8,
                    # 尝试范围
                    "range": (4, 1, 4),
                    # 下发允许的方块，*代表任何方块
                    "dirt": {"*"},
                },
            },
        )
        # 可以被骨粉催熟的灌木（单格）
        system.addData(
            StaticConfig.Data.PLANT_GROW,
            {
                "tofucraft:blockedamame0": {
                    "next": "tofucraft:blockedamame1",
                    "rate": 0.5,
                },
                "tofucraft:blockedamame1": {"next": "tofucraft:blockedamame2"},
                "tofucraft:blockedamame2": {"next": "tofucraft:blockedamame3"},
            },
        )
        # 下方方块被破坏掉落的植物
        system.addData(
            StaticConfig.Data.PLANT_DEPEND,
            {
                "tofucraft:blockleek": {
                    # 允许种植在哪些方块上
                    "dirt": {
                        "tofucraft:blocktofumomen",
                        "tofucraft:blocktofumomen_fake",
                        "tofucraft:blocktofukinu",
                    },
                    # 检测位置偏移量
                    "offset": [(0, -1, 0)],
                    # 掉落物，掉落方块的掉落
                    "dropBlock": ["tofucraft:blockleek"],
                }
            },
        )
        # 会产生掉落物的方块
        system.addData(
            StaticConfig.Data.PLANT_CORP,
            {
                "fossils_archeology:palaeoraphe": {
                    # 经过几个随机刻成长为大树
                    "tick": 1,
                    # 位置偏移量
                    "offset": (0.5, 0, 0.5),
                    # 掉落物，物品结构见 http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发beta/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                    "drop": [
                        {"itemName": "minecraft:apple", "auxValue": 0, "count": 1}
                    ],
                }
            },
        )
        # 破坏草后会产生掉落物的方块
        system.addData(
            StaticConfig.Data.PLANT_DROP,
            {
                # key可以随意填写，但是推荐与物品相同，每个物品独立概率，
                "minecraft:apple": {
                    "rate": 1.0,
                    "item": {"itemName": "minecraft:apple", "auxValue": 0, "count": 1},
                },
                "minecraft:stick": {
                    "rate": 1.0,
                    "item": {"itemName": "minecraft:stick", "auxValue": 0, "count": 1},
                },
            },
        )
        # 破坏非草方块后产生掉落物的功能，根据方块id索引，用于掉无法配置loottable的部分
        system.addData(
            StaticConfig.Data.PLANT_DROP_BLOCK,
            {
                "xjcraft:example": {
                    # 掉落物，物品结构见 http://mc.163.com/mcstudio/mc-dev/MCDocs/2-ModSDK模组开发beta/02-Python脚本开发/99-ModAPI/0-名词解释.html#物品信息字典
                    "drops": [
                        {
                            "rate": 1.0,
                            "item": {
                                "itemName": "minecraft:apple",
                                "auxValue": 0,
                                "count": 1,
                            },
                        },
                        {
                            "rate": 0.5,
                            "item": {
                                "itemName": "minecraft:stick",
                                "auxValue": 0,
                                "count": 1,
                            },
                        },
                    ]
                }
            },
        )
        # 会生长的树
        system.addData(
            StaticConfig.Data.PLANT_TREE,
            {
                "fossils_archeology:palaeoraphe": {
                    # 经过几个随机刻成长为大树
                    "tick": 7,
                    # 结构模板，可以从若干模板中选一个
                    "structures": [
                        {
                            # mcstructure文件，位置在behavior_pack/structures内，以冒号分割文件夹与文件
                            "file": "fossils:tree",
                            # 生成的偏移量
                            "offset": (-2, 0, -2),
                        }
                    ],
                }
            },
        )
        # 检测当占据的格子包含非空气方块，自身会被销毁
        system.addData(
            StaticConfig.Data.PLANT_EXPAND,
            {
                # 只检测上方方块的例子
                "fossils_archeology:orange1": {
                    "expand": [
                        (0, 1, 0),
                    ],
                    # 销毁是是否掉落自己
                    "drop": False,
                },
                # 检测四周一圈
                "fossils_archeology:orange2": {
                    "expand": [
                        (1, 0, 0),
                        (-1, 0, 0),
                        (0, 0, 1),
                        (0, 0, -1),
                    ],
                    "drop": False,
                },
                # 检测两层
                "fossils_archeology:orange3": {
                    "expand": [
                        (1, 0, 0),
                        (-1, 0, 0),
                        (0, 0, 1),
                        (0, 0, -1),
                        (1, 1, 0),
                        (-1, 1, 0),
                        (0, 1, 1),
                        (0, 1, -1),
                        (0, 1, 0),
                    ],
                    "drop": False,
                },
            },
            version=0,
        )
