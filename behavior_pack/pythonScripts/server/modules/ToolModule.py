# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *

"""工具模块，有一些挖掘相关功能，功能见example"""


class ToolModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Tool, version=-1)
    def __init__(self):
        super(ToolModule, self).__init__()

    def example(self, system):
        """
        例子
        :param system:
        """
        # 范围耕地，数值作为转换的范围
        system.addData(StaticConfig.Data.TOOL_AREA_FARM, {
            "minecraft:diamond_hoe": 3
        }, version=0)
        # 快速挖掘，作为key的物品可以快速挖掘value的物品，*代表所有物品
        system.addData(StaticConfig.Data.TOOL_FAST, {
            "minecraft:diamond_pickaxe": {"*", },
            "minecraft:diamond_axe": {"minecraft:log", "minecraft:log2", "minecraft:planks", "minecraft:leaf", "minecraft:chest", },
        }, version=0)
        # 连锁挖掘，数值作为连锁最多破坏的范围
        system.addData(StaticConfig.Data.TOOL_CHAIN, {
            "tofucraft:tooldiamondaxe": 1,
            "tofucraft:tooldiamondaxe_lv1": 2,
            "tofucraft:tooldiamondaxe_lv2": 3,
            "tofucraft:tooldiamondaxe_lv3": 4,
            "tofucraft:tooldiamondpickaxe": 1,
            "tofucraft:tooldiamondpickaxe_lv1": 2,
            "tofucraft:tooldiamondpickaxe_lv2": 3,
            "tofucraft:tooldiamondpickaxe_lv3": 4,
            "tofucraft:tooldiamondshovel": 1,
            "tofucraft:tooldiamondshovel_lv1": 2,
            "tofucraft:tooldiamondshovel_lv2": 3,
            "tofucraft:tooldiamondshovel_lv3": 4,
        }, version=0)
        # 爆炸挖掘，数值作为破坏的范围
        system.addData(StaticConfig.Data.TOOL_EXPLODE, {
            "minecraft:diamond_pickaxe": 3,
            "tofucraft:tooldiamondaxe_lv1": 2,
            "tofucraft:tooldiamondaxe_lv2": 3,
            "tofucraft:tooldiamondaxe_lv3": 4,
            "tofucraft:tooldiamondpickaxe": 1,
            "tofucraft:tooldiamondpickaxe_lv1": 2,
            "tofucraft:tooldiamondpickaxe_lv2": 3,
            "tofucraft:tooldiamondpickaxe_lv3": 4,
            "tofucraft:tooldiamondshovel": 1,
            "tofucraft:tooldiamondshovel_lv1": 2,
            "tofucraft:tooldiamondshovel_lv2": 3,
            "tofucraft:tooldiamondshovel_lv3": 4,
        }, version=0)
