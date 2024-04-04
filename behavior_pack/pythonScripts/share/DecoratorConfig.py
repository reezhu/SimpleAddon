# -*- coding: utf-8 -*-
# @Author  : Ree

# 用于标记格子类型
class SlotType:
    HEADWEAR = "headwear"  # 头饰
    NECKLACE = "necklace"  # 项链
    CAPE = "cape"  # 斗篷/翅膀
    TALISMAN = "talisman"  # 护符
    BELT = "belt"  # 腰带
    RING = "ring"  # 戒指
    AVATAR = "avatar"  # 人物外观


# 从左到右从上到下格子的类型
DECORATOR_SLOT_TYPE = [
    SlotType.HEADWEAR,
    SlotType.NECKLACE,
    SlotType.BELT,
    SlotType.TALISMAN,
    SlotType.CAPE,
    SlotType.RING,
    SlotType.RING,
    SlotType.AVATAR,
]
