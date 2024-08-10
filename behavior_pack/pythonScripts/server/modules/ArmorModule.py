# -*- coding: utf-8 -*-
# @Author  : Ree
import itertools

from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share import Scheduler

"""盔甲模块，用法见下面的配置"""


class ArmorModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Armor, version=-1)
    def __init__(self):
        super(ArmorModule, self).__init__()

    def example(self, system):
        """
        这个方法已弃用，配置请放到modMain中,此处仅作为范例
        @param system:
        """
        # ---------------------------------------以下需要配置---------------------------------------
        # 未特殊说明物品支持盔甲、饰品、手持物品与套装
        # 攻击特效
        system.addData(
            StaticConfig.Data.ARMOR_EFFECT,
            {
                "minecraft:diamond_sword": [
                    # 对自己发送指令
                    ("cmd", {"cmd": "playsound @a player.hurt"}),
                    # 对自己播放序列帧
                    (
                        "sfx_source",
                        {"path": "sfx/1", "faceCamera": False, "bindRot": (0, 90, 0)},
                    ),
                    # 对目标播放序列帧
                    ("sfx_target", {"path": "sfx/2", "scale": (3, 3, 3)}),
                    # 对目标添加药水效果
                    (
                        "buff_target",
                        [
                            ("poison", 15, 1, False),
                        ],
                    ),
                    # 引燃目标
                    ("fire_target", 10),
                ],
            },
            version=0,
        )
        # 持续获得的buff
        system.addData(
            StaticConfig.Data.ARMOR_BUFF,
            {
                "minecraft:diamond_sword": [
                    # buff名、时长、等级、显示粒子
                    ("speed", 15, 1, False),
                    ("night_vision", 15, 0, False),
                    ("jump_boost", 15, 2, False),
                ],
            },
            version=0,
        )
        system.addData(
            StaticConfig.Data.ARMOR_PARTICLE,
            {
                # 盔甲的粒子
                "minecraft:diamond_sword": [
                    {
                        "type": "minecraft_particle",  # 粒子类型，可选值：minecraft_particle（原版粒子）、netease_particle（产品粒子）、netease_sfx（产品序列帧）
                        "args": (
                            "minecraft:xjcraft_wire_dust_particle",  # 粒子名
                            lambda tick, isMoving: isMoving
                            and tick % 1 == 0,  # tick是是否显示
                            lambda x, y, z: (x - 0.1, y - 1.2, z),
                        ),
                    },  # 显示坐标
                    {
                        "type": "minecraft_particle",
                        "args": (
                            "minecraft:xjcraft_wire_dust_particle",
                            lambda tick, isMoving: isMoving and tick % 3 == 0,
                            lambda x, y, z: (x, y - 1.2, z),
                        ),
                    },
                    {
                        "type": "minecraft_particle",
                        "args": (
                            "minecraft:xjcraft_wire_dust_particle",
                            lambda tick, isMoving: isMoving and tick % 5 == 0,
                            lambda x, y, z: (x + 0.1, y - 1.2, z),
                        ),
                    },
                    {
                        "type": "netease_sfx",  # 粒子类型：netease_sfx（产品序列帧）
                        "livetime": 90,  # 序列帧持续时间,单位为tick
                        "interval": 1,  # 序列帧间隔时间,单位为秒，最低为1秒，默认为1秒
                        "args": {
                            "path": "sfx/xxx",  # 资源路径，不用json后缀
                            "scale": (1, 1, 1),  # 缩放
                            "faceCamera": True,  # 是否面向相机
                            "layer": 1,  # 覆盖层级
                            "loop": False,  # 是否循环
                            "bindOffset": (0, 0, 0),  # 绑定偏移
                            "bindRot": (0, 0, 0),  # 绑定旋转
                        },
                    },
                    {
                        "type": "netease_particle",  # 粒子类型：netease_particle（产品粒子）
                        "livetime": 90,  # 粒子持续时间,单位为tick
                        "interval": 1,  # 粒子间隔时间,单位为秒，最低为1秒，默认为1秒
                        "args": {
                            "path": "effects/xxx.json",  # 资源路径，带json后缀
                            "layer": 1,  # 覆盖层级
                            "bindOffset": (0, 0, 0),  # 绑定的偏移量
                            "bindRot": (0, 0, 0),  # 绑定的旋转角度
                            "correction": True,  # 特效的旋转角度准确设置为参照玩家的相对角度
                        },
                    },
                ],
                # 套装的粒子
                (
                    "minecraft:diamond_helmet",
                    "minecraft:diamond_chestplate",
                    "minecraft:diamond_leggings",
                    "minecraft:diamond_boots",
                ): [
                    {
                        "type": "minecraft_particle",
                        "args": (
                            "minecraft:xjcraft_wire_dust_particle",
                            lambda tick, isMoving: isMoving and tick % 2 == 0,
                            lambda x, y, z: (x, y + 1, z),
                        ),
                    },
                    {
                        "type": "netease_sfx",  # 序列帧类型：netease_sfx（产品序列帧）
                        "livetime": 90,  # 序列帧持续时间,单位为tick
                        "interval": 1,  # 序列帧间隔时间,单位为秒，最低为1秒，默认为1秒
                        "args": {
                            "path": "sfx/xxx",  # 资源路径，不用json后缀
                            "scale": (1, 1, 1),  # 缩放
                            "faceCamera": True,  # 是否面向相机
                            "layer": 1,  # 覆盖层级
                            "loop": False,  # 是否循环
                            "bindOffset": (0, 0, 0),  # 绑定偏移
                            "bindRot": (0, 0, 0),  # 绑定旋转
                        },
                    },
                    {
                        "type": "netease_particle",  # 粒子类型：netease_particle（产品粒子）
                        "livetime": 90,  # 粒子持续时间,单位为tick
                        "interval": 1,  # 粒子间隔时间,单位为秒，最低为1秒，默认为1秒
                        "args": {
                            "path": "effects/xxx.json",  # 资源路径，带json后缀
                            "layer": 1,  # 覆盖层级
                            "bindOffset": (0, 0, 0),  # 绑定的偏移量
                            "bindRot": (0, 0, 0),  # 绑定的旋转角度
                            "correction": True,  # 特效的旋转角度准确设置为参照玩家的相对角度
                        },
                    },
                ],
            },
            version=0,
        )
        # 免疫的buff
        system.addData(
            StaticConfig.Data.ARMOR_IMMUNITY_BUFF,
            {
                "minecraft:diamond_sword": {"blindness"},
                (
                    "minecraft:diamond_helmet",
                    "minecraft:diamond_chestplate",
                    "minecraft:diamond_leggings",
                    "minecraft:diamond_boots",
                ): {"poison"},
            },
            version=0,
        )
        # 免疫的伤害,包含武器，这里定义所有伤害为*，击退为knock
        system.addData(
            StaticConfig.Data.ARMOR_IMMUNITY_DAMAGE,
            {
                "minecraft:diamond_sword": {"*"},
                (
                    "minecraft:diamond_helmet",
                    "minecraft:diamond_chestplate",
                    "minecraft:diamond_leggings",
                    "minecraft:diamond_boots",
                ): {"knock"},
            },
            version=0,
        )
        # 吸血(仅武器有效)，后面是伤害与加血的数值关系
        system.addData(
            StaticConfig.Data.ARMOR_SUCK_BLOOD,
            {
                "minecraft:diamond_sword": lambda damage: max(damage * 0.5, 1),
            },
            version=0,
        )
        # 秒杀
        system.addData(
            StaticConfig.Data.ARMOR_KILL,
            {
                "minecraft:diamond_sword": {},
            },
            version=0,
        )
        # 盔甲增伤
        system.addData(
            StaticConfig.Data.ARMOR_DAMAGE_BOOST,
            {
                "minecraft:diamond_helmet": lambda damage: max(damage, 7),
            },
            version=0,
        )
        # 反伤，后面是伤害与加血的数值关系
        system.addData(
            StaticConfig.Data.ARMOR_THRONE,
            {
                "minecraft:diamond_helmet": lambda damage: max(damage * 0, 1),
            },
            version=0,
        )
        # 属性切换,可用属性只有HEALTH与SPEED,
        # 添加了JUMP属性用于更新客户端二段跳,使用此功能必须在客户端添加二段跳模组
        system.addData(
            StaticConfig.Data.ARMOR_ATTR,
            {
                "minecraft:diamond_chestplate": {
                    "onEquipped": [("HEALTH", 40)],  # 装上增加的血量
                    "deEquipped": [
                        ("HEALTH", -40)  # 卸下扣除的血量，建议和onEquipped一致
                    ],
                },
                "minecraft:diamond_leggings": {
                    "onEquipped": [
                        ("SPEED", 2),  # 装上增加的速度
                    ],
                    "deEquipped": [
                        ("SPEED", -2),  # 卸下扣除的速度，建议和onEquipped一致
                    ],
                },
                "minecraft:diamond_boots": {
                    "onEquipped": [
                        ("JUMP", {"jump": 2, "power": 1}),
                    ],
                    "deEquipped": [
                        ("JUMP", {"jump": 0, "power": 0}),
                    ],
                },
                "minecraft:iron_boots": {
                    "onEquipped": [
                        ("FLY", {"canFly": True, "force": 2, "damping": 0}),
                    ],
                    "deEquipped": [
                        ("FLY", {"canFly": False, "force": 0, "damping": 0}),
                    ],
                },
                "minecraft:gold_boots": {
                    "onEquipped": [
                        ("CMD", "tag @s add " + StaticConfig.Tag.IMMUNITY_KILL),
                    ],
                    "deEquipped": [
                        ("CMD", "tag @s remove " + StaticConfig.Tag.IMMUNITY_KILL),
                    ],
                },
                "minecraft:diamond_helmet": {
                    "onEquipped": [
                        ("CameraAnchor", (0, 1, 0)),  # 设置相机锚点,暂时只支持高度
                    ],
                    "deEquipped": [
                        ("CameraAnchor", (0, 0, 0)),
                    ],
                },
                "minecraft:gold_helmet": {
                    "onEquipped": [
                        ("CameraOffset", (1, 1, 1)),  # 设置相机锚点,暂时只支持高度
                    ],
                    "deEquipped": [
                        ("CameraOffset", (1, 1, 1)),
                    ],
                },
            },
            version=0,
        )
        # 免疫仇恨
        system.addData(
            StaticConfig.Data.ARMOR_RESET_TARGET,
            {
                (
                    "minecraft:diamond_helmet",
                    "minecraft:diamond_chestplate",
                    "minecraft:diamond_leggings",
                    "minecraft:diamond_boots",
                ): {"zombie"}
            },
            version=0,
        )
        # 受到伤害执行指令
        system.addData(
            StaticConfig.Data.ARMOR_SET_COMMAND,
            {
                "minecraft:diamond_helmet": {
                    "durability": 15,  # 扣除耐久值
                    "command": "/spreadplayers ~ ~ 10 20 @s",
                },  # 执行的指令
            },
            version=0,
        )
        # 减伤，后面是伤害与减伤的数值关系
        system.addData(
            StaticConfig.Data.ARMOR_REDUCE_DAMAGE,
            {
                "minecraft:diamond_helmet": lambda damage: max(damage - 4, 1),
            },
            version=0,
        )
        # 每隔一段时间，增加耐久
        system.addData(
            StaticConfig.Data.ARMOR_ADD_DURABILITY,
            {
                "minecraft:diamond_sword": {
                    "duration": 2,  # 时间间隔，10秒的整数倍，2意味着20秒
                    "add_durability": 10,  # 给所有装备增加的耐久值
                    "durability": 20,
                },  # 扣除此装备的耐久值
            },
            version=0,
        )
