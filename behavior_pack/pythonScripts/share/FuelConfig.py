# -*- coding: utf-8 -*-
# @Author  : Ree
"""原版熔炉的燃烧时间"""

Fuels = {
    ("minecraft:bucket", 10): 20000,
    "minecraft:coal_block": 16000,
    "minecraft:dried_kelp_block": 4000,
    "minecraft:blaze_rod": 2400,
    "minecraft:coal": 1600,
    "minecraft:boat": 1200,
    "minecraft:scaffolding": 1200,
    "minecraft:acacia_button": 300,
    "minecraft:acacia_fence_gate": 300,
    "minecraft:acacia_pressure_plate": 300,
    "minecraft:acacia_stairs": 300,
    "minecraft:acacia_trapdoor": 300,
    "minecraft:banner": 300,
    "minecraft:barrel": 300,
    "minecraft:birch_button": 300,
    "minecraft:birch_fence_gate": 300,
    "minecraft:birch_pressure_plate": 300,
    "minecraft:birch_stairs": 300,
    "minecraft:birch_trapdoor": 300,
    "minecraft:bookshelf": 300,
    "minecraft:brown_mushroom_block": 300,
    "minecraft:cartography_table": 300,
    "minecraft:chest": 300,
    "minecraft:composter": 300,
    "minecraft:crafting_table": 300,
    "minecraft:crimson_button": 300,
    "minecraft:crimson_double_slab": 300,
    "minecraft:crimson_fence": 300,
    "minecraft:crimson_fence_gate": 300,
    "minecraft:crimson_planks": 300,
    "minecraft:crimson_pressure_plate": 300,
    "minecraft:crimson_slab": 300,
    "minecraft:crimson_stairs": 300,
    "minecraft:crimson_stem": 300,
    "minecraft:crimson_trapdoor": 300,
    "minecraft:dark_oak_button": 300,
    "minecraft:dark_oak_fence_gate": 300,
    "minecraft:dark_oak_pressure_plate": 300,
    "minecraft:dark_oak_stairs": 300,
    "minecraft:dark_oak_trapdoor": 300,
    "minecraft:daylight_detector": 300,
    "minecraft:double_wooden_slab": 300,
    "minecraft:fence": 300,
    "minecraft:fence_gate": 300,
    "minecraft:fishing_rod": 300,
    "minecraft:fletching_table": 300,
    "minecraft:jukebox": 300,
    "minecraft:jungle_button": 300,
    "minecraft:jungle_fence_gate": 300,
    "minecraft:jungle_pressure_plate": 300,
    "minecraft:jungle_stairs": 300,
    "minecraft:jungle_trapdoor": 300,
    "minecraft:ladder": 300,
    "minecraft:lectern": 300,
    "minecraft:log": 300,
    "minecraft:log2": 300,
    "minecraft:loom": 300,
    "minecraft:noteblock": 300,
    "minecraft:oak_stairs": 300,
    "minecraft:planks": 300,
    "minecraft:red_mushroom_block": 300,
    "minecraft:smithing_table": 300,
    "minecraft:spruce_button": 300,
    "minecraft:spruce_fence_gate": 300,
    "minecraft:spruce_pressure_plate": 300,
    "minecraft:spruce_stairs": 300,
    "minecraft:spruce_trapdoor": 300,
    "minecraft:stripped_acacia_log": 300,
    "minecraft:stripped_birch_log": 300,
    "minecraft:stripped_crimson_stem": 300,
    "minecraft:stripped_dark_oak_log": 300,
    "minecraft:stripped_jungle_log": 300,
    "minecraft:stripped_oak_log": 300,
    "minecraft:stripped_spruce_log": 300,
    "minecraft:stripped_warped_stem": 300,
    "minecraft:trapped_chest": 300,
    "minecraft:warped_button": 300,
    "minecraft:warped_double_slab": 300,
    "minecraft:warped_fence": 300,
    "minecraft:warped_fence_gate": 300,
    "minecraft:warped_planks": 300,
    "minecraft:warped_pressure_plate": 300,
    "minecraft:warped_slab": 300,
    "minecraft:warped_stairs": 300,
    "minecraft:warped_stem": 300,
    "minecraft:warped_trapdoor": 300,
    "minecraft:wooden_button": 300,
    "minecraft:wooden_pressure_plate": 300,
    "minecraft:wooden_slab": 300,
    "minecraft:wooden_trapdoor": 300,
    "minecraft:bow": 200,
    "minecraft:bowl": 200,
    "minecraft:sign": 200,
    "minecraft:wooden_axe": 200,
    "minecraft:wooden_door": 200,
    "minecraft:wooden_hoe": 200,
    "minecraft:wooden_pickaxe": 200,
    "minecraft:wooden_shovel": 200,
    "minecraft:wooden_sword": 200,
    "minecraft:sapling": 100,
    "minecraft:stick": 100,
    "minecraft:wool": 100,
    "minecraft:carpet": 67,
    "minecraft:bamboo": 50,

}


def isFuel(item):
    """
    检测是不是燃料
    @param item:
    @return:
    """
    if item is not None:
        if item["itemName"] in Fuels:
            return True
        elif (item["itemName"], item["auxValue"]) in Fuels:
            return True
    return False


def getBurnTime(item):
    """
    获取燃料燃烧时间
    @param item:
    @return:
    """
    if item is not None:
        if item["itemName"] in Fuels:
            return Fuels[item["itemName"]]
        elif (item["itemName"], item["auxValue"]) in Fuels:
            return Fuels[(item["itemName"], item["auxValue"])]
    return 0
