# -*- coding: utf-8 -*-
# @Author  : Ree
import random

import math

from pythonScripts.share import VectorUtils

# 抛射物主魔咒
PROJECTILE = 0
# 静态主魔咒
STATIC = 1
# 辅助魔咒，根据subtype区分
SUB = 2
# 多发魔咒
COMBO = 3
# 连射魔咒
SUB_COMBO = 4
# 属性魔咒
ADJUST_ATTR = 5

spells = {
    # 主魔咒的参数除了注释全部是从抛射物配置导出
    "default:main": {
        # 释放的抛射物identifier
        "uid": "common:empty_projectile",
        # 重力
        "gravity": 0.01,
        # 射速
        "power": 1.5,
        # 伤害
        "damage": 4.0,
        # 名字，无意义，下同
        "name": "魔法弹",
        # 生存时间
        "alive": 10,
        # 碰撞时会发出的事件，用于触发其他逻辑,可以接受列表
        "event_hit": ["ExampleEvent"],
        # 射中时的音效,可以接受列表
        "sound_hit": ["bow.hit"],
        # 射中时的帧粒子,可以接受列表
        "particle_hit": [
            "effects/lianyou2.json",
            {
                "path": "effects/lianyou2.json",
                # "pos": (0, 5, 0),这个字段会在运行时填入，不用填
                "layer": 1,
                "correction": False,
            },
        ],
        # 飞行时的绑定粒子,可以接受列表
        "particle_bind": [
            "effects/lianyou1.json",
            {
                "path": "effects/lianyou1.json",
                # "bind": None,这个字段会在运行时填入，不用填
                "bindOffset": (0, 5, 0),
                "bindRot": (0, 0, 0),
                "layer": 1,
                "correction": True,
            },
        ],
        # 射中时的帧动画（拉伸）,可以接受列表
        "frame_hit_drag": ["frame/wizard_projectile_magic_bullet"],
        # 射中时的帧动画的起始位置偏移量，（负左正右，负下正上）
        "frame_hit_drag_offset": (1, 1),
        # 射中时的帧动画,可以接受列表,带json会判定成编辑器序列帧
        "frame_hit": [
            "frame/wizard_projectile_magic_bullet",
            {
                "path": "frame/wizard_projectile_magic_bullet",
                # "pos": (0, 5, 0),这个字段会在运行时填入，不用填
                "rot": (0, 0, 0),
                "scale": (1, 1, 1),
                "faceCamera": True,
                "layer": 1,
                "loop": False,
            },
        ],
        # 飞行时绑定动画,可以接受列表
        "frame_bind": [
            "frame/wizard_projectile_magic_bullet",
            {
                "path": "frame/wizard_projectile_magic_bullet",
                # "bind": None,这个字段会在运行时填入，不用填
                "bindOffset": (0, 5, 0),
                "bindRot": (0, 0, 0),
                "scale": (1, 1, 1),
                "faceCamera": True,
                "layer": 1,
                "loop": False,
            },
        ],
        # # 飞行时曳光动画,可以接受列表
        "frame_tail": ["frame/wizard_projectile_magic_bullet"],
        # 飞行时曳光动画显示间隔
        "frame_tail_period": 30,
        # 消耗的魔法值，选填，下同
        "cost": 15,
    },
    "default:static_lightning": {
        "name": "瞬式:闪电",
        "type": STATIC,
        # 静态魔咒，落下闪电（原版，伤害不可调）
        "subtype": "lightning",
        "cost": 10,
    },
    "default:static_levitation": {
        "name": "瞬式:漂浮",
        "type": STATIC,
        # 静态魔咒，落下闪电（原版，伤害不可调）
        "subtype": "buff",
        "effects": [
            {"buff": "levitation", "duration": 5, "amplifier": 0, "showParticles": True}
        ],
        "cost": 10,
    },
    "default:static_light": {
        "name": "瞬式:光耀",
        "type": STATIC,
        # 召唤一个方块，延时置空
        "subtype": "light",
        # 设置为空的延时
        "delay": 20,
        # 将空气临时替换成的方块
        "block": "minecraft:lantern",
        "cost": 10,
    },
    "default:static_explosion_1": {
        "name": "瞬式:空爆",
        "type": STATIC,
        # 静态魔咒，创建一个原版爆炸
        "subtype": "explode",
        # 爆炸范围
        "radius": 4,
        # 伤害
        "damage": 4,
        # 击退力度
        "knock": 1.0,
        # 是否着火
        "fire": False,
        # 是否破坏方块
        "breaks": False,
        "cost": 10,
    },
    "default:static_explosion_2": {
        "name": "瞬式:爆破",
        "type": STATIC,
        # 静态魔咒，创建一个原版爆炸
        "subtype": "explode",
        # 爆炸范围
        "radius": 3,
        # 是否着火
        "fire": False,
        # 是否破坏方块
        "breaks": True,
        "cost": 10,
    },
    "default:static_explosion_3": {
        "name": "瞬式:优化空爆",
        "type": STATIC,
        # 静态魔咒，创建一个原版爆炸
        "subtype": "optimize_explode",
        # 爆炸范围
        "radius": 4,
        # 伤害
        "damage": 4,
        # 击退力度
        "knock": 1.0,
        # 是否着火
        "fire": False,
        # 是否破坏方块
        "breaks": False,
        "cost": 10,
    },
    "default:operator_speed_up_1": {
        "name": "塑形:加速",
        "type": SUB,
        # 加速魔咒，增加法杖速度
        "subtype": "speed",
        # 速度加成倍速
        "multiple": 1.2,
        # 消耗魔法的加成倍数，所有加成倍数相加后+1乘以基础消耗量为总消耗量，选填，下同
        "costMultiple": 1.5,
    },
    "default:operator_speed_up_2": {
        "name": "塑形:急速",
        "type": SUB,
        # 加速魔咒，增加法杖速度
        "subtype": "speed",
        # 速度加成倍速
        "multiple": 1.6,
        # 消耗魔法的加成倍数，所有加成倍数相加后+1乘以基础消耗量为总消耗量，选填，下同
        "costMultiple": 2,
    },
    "default:operator_speed_down_1": {
        "name": "塑形:减速",
        "type": SUB,
        # 加速魔咒，增加法杖速度
        "subtype": "speed",
        # 速度加成倍速
        "multiple": 0.8,
        # 消耗魔法的加成倍数，所有加成倍数相加后+1乘以基础消耗量为总消耗量，选填，下同
        "costMultiple": 0.8,
    },
    "default:operator_speed_down_2": {
        "name": "塑形:龟速",
        "type": SUB,
        # 加速魔咒，增加法杖速度
        "subtype": "speed",
        # 速度加成倍速
        "multiple": 0.6,
        # 消耗魔法的加成倍数，所有加成倍数相加后+1乘以基础消耗量为总消耗量，选填，下同
        "costMultiple": 0.5,
    },
    "default:operator_no_gravity": {
        "name": "塑形:精准",
        "type": SUB,
        # 设置抛射物的重力
        "subtype": "gravity",
        # 重力加成倍数，可为负
        "multiple": 0,
        "costMultiple": 2.0,
    },
    "default:operator_anti_gravity": {
        "name": "塑形:反重力",
        "type": SUB,
        # 同上
        "subtype": "gravity",
        "multiple": -1.0,
        "costMultiple": 1.5,
    },
    "default:operator_more_gravity": {
        "name": "塑形:快速下坠",
        "type": SUB,
        # 同上
        "subtype": "gravity",
        "multiple": 1.5,
        "costMultiple": 1.2,
    },
    "default:operator_less_gravity": {
        "name": "塑形:轻羽",
        "type": SUB,
        # 同上
        "subtype": "gravity",
        "multiple": 0.5,
        "costMultiple": 1.2,
    },
    "default:operator_reflect": {
        "name": "塑形:反射",
        "type": SUB,
        # 射中方块后进行反射
        "subtype": "reflect",
        # 增加的反射次数
        "reflect": 1,
        "costMultiple": 1.2,
    },
    "default:operator_rebound": {
        "name": "塑形:回弹",
        "type": SUB,
        # 射中方向后进行回弹，方向为入射反方向
        "subtype": "rebound",
        # 增加的反射次数
        "reflect": 1,
        "costMultiple": 1.2,
    },
    "default:operator_higher": {
        "name": "塑形:抬高",
        "type": SUB,
        # 发射点调整
        "subtype": "direction",
        # 发射点抬高
        "position": (0, 2, 0),
        # 发射角度调整
        "rotation": (0, 0, 0),
        "costMultiple": 1.0,
    },
    "default:operator_dispersion": {
        "name": "塑形:散布",
        "type": SUB,
        # 增加弹道散布
        "subtype": "spread",
        # 散布偏移量，相加
        "offset": 15,
        "costMultiple": 0.8,
    },
    "default:operator_double": {
        "name": "塑形:双重复制",
        "type": SUB,
        # 霰弹枪效果，一次发射多枚
        "subtype": "multiple",
        # 散布偏移量，相加
        "offset": 4,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 2,
        "costMultiple": 1.8,
    },
    "default:operator_triple": {
        "name": "塑形:三重复制",
        "type": SUB,
        # 霰弹枪效果，一次发射多枚
        "subtype": "multiple",
        # 散布偏移量，相加
        "offset": 6,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 3,
        "costMultiple": 2.6,
    },
    "default:operator_fourfold": {
        "name": "塑形:四重复制",
        "type": SUB,
        # 霰弹枪效果，一次发射多枚
        "subtype": "multiple",
        # 散布偏移量，相加
        "offset": 10,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 4,
        "costMultiple": 3.4,
    },
    "default:operator_mirror_double": {
        "name": "塑形:双面镜",
        "type": SUB,
        # 镜像，沿视角水平方向360度进行散射
        "subtype": "mirror",
        # 散布偏移量，相加
        "offset": 0,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 2,
        "costMultiple": 1.8,
    },
    "default:operator_mirror_triple": {
        "name": "塑形:三面镜",
        "type": SUB,
        # 镜像，沿视角水平方向360度进行散射
        "subtype": "mirror",
        # 散布偏移量，相加
        "offset": 0,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 3,
        "costMultiple": 2.6,
    },
    "default:operator_mirror_fourfold": {
        "name": "塑形:四面镜",
        "type": SUB,
        # 镜像，沿视角水平方向360度进行散射
        "subtype": "mirror",
        # 散布偏移量，相加
        "offset": 0,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 4,
        "costMultiple": 3.4,
    },
    "default:operator_mirror_five_times": {
        "name": "塑形:五面镜",
        "type": SUB,
        # 镜像，沿视角水平方向360度进行散射
        "subtype": "mirror",
        # 散布偏移量，相加
        "offset": 0,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 5,
        "costMultiple": 4.2,
    },
    "default:operator_mirror_sixfold": {
        "name": "塑形:六面镜",
        "type": SUB,
        # 镜像，沿视角水平方向360度进行散射
        "subtype": "mirror",
        # 散布偏移量，相加
        "offset": 0,
        # 发射子弹数量，多个相同符咒相乘
        "multiple": 6,
        "costMultiple": 5,
    },
    "default:operator_fire": {
        "name": "塑形:点燃",
        "type": SUB,
        # 火焰附加
        "subtype": "fire",
        # 燃烧时间，多个相同符咒相加
        "time": 2,
        "costMultiple": 1.1,
    },
    "default:operator_crit": {
        "name": "塑形:幸运一击",
        "type": SUB,
        # 概率进行双倍伤害
        "subtype": "crit",
        # 暴击概率，多个相同符咒相加
        "crit": 15,
        "costMultiple": 1.1,
    },
    "default:operator_reduction": {
        "name": "塑形:节制",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 0,
        "costMultiple": 0.5,
    },
    "default:operator_reduction_create": {
        "name": "塑形:无需魔力",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 0,
        "costMultiple": 0,
    },
    "default:operator_damage_1": {
        "name": "塑形:强力",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 2,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 1.1,
        "costMultiple": 1.4,
    },
    "default:operator_damage_2": {
        "name": "塑形:猛击",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 3,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 1.2,
        "costMultiple": 1.8,
    },
    "default:operator_damage_3": {
        "name": "塑形:绝唱",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 4,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 1.4,
        "costMultiple": 2.2,
    },
    "default:operator_damage_4": {
        "name": "塑形:禁忌",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 5,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 2.0,
        "costMultiple": 3.0,
    },
    "default:operator_explode": {
        "name": "塑形:反射爆炸",
        "type": SUB,
        # 反弹的同时出现一次爆炸
        "subtype": "explode",
        # 反弹类型可以时reflect反弹，也可以时rebound回弹，其他配置同爆炸与反弹
        "bounceType": "reflect",
        "reflect": 1,
        "radius": 2,
        "fire": False,
        "breaks": False,
        "costMultiple": 1.3,
    },
    # 如果你看到了这段注释，这个版本就已经移除了combo限制，你可以直接添加主魔咒
    "default:operator_combo_double": {
        "name": "塑形:双重施法",
        # 连续射出多个主魔咒，每个魔咒间会有0.1s的延迟
        "type": COMBO,
        # 可以连续射出多少魔咒，多个相同符咒相加
        "available": 1,
        "costMultiple": 1.8,
    },
    # 如果你看到了这段注释，这个版本就已经移除了combo限制，你可以直接添加主魔咒
    "default:operator_combo_triple": {
        "name": "塑形:三重施法",
        # 连续射出多个主魔咒，每个魔咒间会有0.1s的延迟
        "type": COMBO,
        # 可以连续射出多少魔咒，多个相同符咒相加
        "available": 2,
        "costMultiple": 2.6,
    },
    "default:operator_trigger": {
        "name": "塑形:触发",
        # 击中后释放下一个主魔咒
        "type": SUB_COMBO,
        "costMultiple": 1.8,
    },
    "default:operator_s_shaped_motion": {
        "name": "塑形:S形前进",
        "type": SUB,
        # 对子弹施加一个侧向的力
        "subtype": "motion",
        # 施加的力的公式，这个公式是蛇形机动
        "motion": lambda motionOffset, motion, vertical, origin, time: VectorUtils.multiple(
            vertical,
            math.cos(time * 15.0)
            * VectorUtils.length(motion)
            * 3
            * math.log10(time / 3 + 1),
        ),
        "costMultiple": 1.1,
    },
    "default:operator_random": {
        "name": "塑形:随机",
        "type": SUB,
        "subtype": "motion",
        # 施加的力的公式，这个公式是转圈
        "motion": lambda motionOffset, motion, vertical, origin, time: VectorUtils.multiple(
            VectorUtils.add(
                VectorUtils.multiple(vertical, random.random() - 0.5),
                VectorUtils.multiple(
                    VectorUtils.cross(motion, vertical), random.random() - 0.5
                ),
            ),
            VectorUtils.length(motion) * 2 * math.log10(time + 1),
        ),
        "costMultiple": 1.05,
    },
    "default:operator_spiral_motion_right": {
        "name": "塑形:右旋",
        "type": SUB,
        "subtype": "motion",
        # 施加的力的公式，这个公式是转圈
        "motion": lambda motionOffset, motion, vertical, origin, time: VectorUtils.multiple(
            vertical, VectorUtils.length(motion) * 1 * math.log10(time / 3 + 1)
        ),
        "costMultiple": 1.05,
    },
    "default:operator_spiral_motion_left": {
        "name": "塑形:左旋",
        "type": SUB,
        "subtype": "motion",
        # 施加的力的公式，这个公式是转圈
        "motion": lambda motionOffset, motion, vertical, origin, time: VectorUtils.multiple(
            vertical, VectorUtils.length(motion) * -1 * math.log10(time / 3 + 1)
        ),
        "costMultiple": 1.05,
    },
    "default:operator_homing": {
        "name": "塑形:自导",
        "type": SUB,
        # 跟踪最近的monster或者mob
        "subtype": "trace",
        # 跟踪的指向力
        "force": 1.0,
        # 检测范围
        "radius": 8,
        "target": None,  # 可配置追踪的Id，默认追踪附近
        "costMultiple": 1.5,
    },
    "default:operator_delay": {
        "name": "塑形:未来",
        "type": SUB,
        # 延迟发射时机
        "subtype": "delay",
        # 延迟,单位秒
        "delay": 0.5,
        "costMultiple": 0.6,
    },
    "default:operator_fast_cast": {
        "name": "塑形:快速施法",
        # 属性调整，下同
        "type": ADJUST_ATTR,
        # 前摇时间
        "subtype": "chargeTime",
        # 数值
        "value": -0.2,
    },
    "default:operator_hold_mana": {
        "name": "塑形:魔力掌握",
        "type": ADJUST_ATTR,
        # 最大魔法值
        "subtype": "maxMana",
        "value": 100,
    },
    "default:operator_mana_recovery": {
        "name": "塑形:魔力亲和",
        "type": ADJUST_ATTR,
        # 魔法恢复速度
        "subtype": "manaRecoverySpeed",
        "value": 10,
    },
    "default:operator_rapid_reload": {
        "name": "塑形:快速装填",
        "type": ADJUST_ATTR,
        # 魔法恢复速度
        "subtype": "cdTime",
        "value": -0.2,
    },
    "default:operator_demonic_power": {
        "name": "塑形:恶魔之力",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 5,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 3.0,
        "costMultiple": 3.0,
    },
    "default:operator_energy_absorpt": {
        "name": "塑形:回能吸收",
        "type": SUB,
        # 增加伤害
        "subtype": "damage",
        # 增加的伤害，多个相同符咒相加
        "damage": 0,
        # 增加的伤害，多个相同符咒相乘，与上面共存时先加后乘
        "damageMultiple": 0.9,
        "costMultiple": 0.6,
    },
    "default:operator_sin_strike": {
        "name": "塑形:罪恶一击",
        "type": SUB,
        # 概率进行双倍伤害
        "subtype": "crit",
        # 暴击概率，多个相同符咒相加
        "crit": 100,
        "costMultiple": 1.5,
    },
    "default:operator_scientific_magic": {
        "name": "塑形:科学子弹",
        "type": SUB,
        # 跟踪最近的monster或者mob
        "subtype": "trace",
        # 跟踪的指向力
        "force": 1.0,
        # 检测范围
        "radius": 16,
        "costMultiple": 1.2,
    },
    "default:operator_saikyo_magician": {
        "name": "塑形:最强巫术",
        "type": ADJUST_ATTR,
        # 最大魔法值
        "subtype": "maxMana",
        "value": 9999,
    },
    "default:operator_magic_confinement": {
        "name": "塑形:魔法集束",
        "type": SUB,
        "subtype": "converge",
        "converge": 120,
    },
    "default:operator_ender_teleport": {
        "name": "瞬式:末影",
        "type": SUB,
        # 传送
        "subtype": "teleport",
        "costMultiple": 1.05,
    },
    "default:operator_attract": {
        "name": "塑形:吸引",
        "type": SUB,
        # 吸引
        "subtype": "attract",
        "motion": lambda distance, x, y, z: (3 * x, 3 * y, 3 * z),
        "costMultiple": 1.1,
    },
    "default:operator_cure": {
        "name": "塑形:治愈",
        "type": SUB,
        # 回春
        "subtype": "cure",
        "costMultiple": 0.5,
    },
    "default:operator_calm": {
        "name": "塑形:冷静",
        "type": SUB,
        # 冷静
        "subtype": "calm",
        "costMultiple": 1.2,
    },
    "default:operator_life_leech": {
        "name": "塑形:生命汲取",
        "type": SUB,
        # 回报
        "subtype": "repay",
        "repay": 0.5,
        "costMultiple": 1.05,
    },
    "default:operator_excavation": {
        "name": "塑形:挖掘",
        "type": SUB,
        # 挖掘
        "subtype": "dig",
        "fortune": 0,
        "costMultiple": 1.1,
    },
    "default:operator_excavation_fortune": {
        "name": "塑形:挖掘（时运）",
        "type": SUB,
        # 挖掘
        "subtype": "dig",
        "fortune": 3,
        "costMultiple": 1.15,
    },
    "default:operator_smelting": {
        "name": "塑形:煅烧",
        "type": SUB,
        # 灼烧
        "subtype": "smelting",
        "fire": 3,
        "costMultiple": 1.1,
    },
    "default:operator_wide_replacer_one": {
        "name": "塑形:替换(蔓延同类)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": False,
        "radius": 2,
        "fortune": 0,
        "cost": 2,
        "costMultiple": 1.5,
    },
    "default:operator_wide_replacer_one_big": {
        "name": "塑形:大范围替换(蔓延同类)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": False,
        "radius": 5,
        "fortune": 0,
        "cost": 5,
        "costMultiple": 2.0,
    },
    "default:operator_wide_replacer_one_fortune": {
        "name": "塑形:时运替换(蔓延同类)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": False,
        "radius": 2,
        "fortune": 3,
        "cost": 2,
        "costMultiple": 2.0,
    },
    "default:operator_wide_replacer_one_big_fortune": {
        "name": "塑形:大范围时运替换(蔓延同类)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": False,
        "radius": 5,
        "fortune": 3,
        "cost": 5,
        "costMultiple": 2.5,
    },
    "default:operator_wide_replacer_all": {
        "name": "塑形:替换(贪婪蔓延)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": True,
        "radius": 2,
        "fortune": 0,
        "cost": 2,
        "costMultiple": 1.8,
    },
    "default:operator_wide_replacer_all_big": {
        "name": "塑形:大范围替换(贪婪蔓延)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": True,
        "radius": 5,
        "fortune": 0,
        "cost": 5,
        "costMultiple": 2.5,
    },
    "default:operator_wide_replacer_all_fortune": {
        "name": "塑形:时运替换(贪婪蔓延)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": True,
        "radius": 2,
        "fortune": 3,
        "cost": 2,
        "costMultiple": 2.5,
    },
    "default:operator_wide_replacer_all_big_fortune": {
        "name": "塑形:大范围时运替换(贪婪蔓延)",
        "type": SUB,
        # 替换蔓延
        "subtype": "replaceAreaBlock",
        "replaceAll": True,
        "radius": 5,
        "fortune": 3,
        "cost": 5,
        "costMultiple": 3.0,
    },
    "default:operator_replacer": {
        "name": "塑形:替换",
        "type": SUB,
        # 替换
        "subtype": "replaceBlock",
        "fortune": 0,
        "costMultiple": 1.1,
    },
    "default:operator_replacer_fortune": {
        "name": "塑形:时运替换",
        "type": SUB,
        # 替换
        "subtype": "replaceBlock",
        "fortune": 3,
        "costMultiple": 1.15,
    },
    "default:operator_gravitational": {
        "name": "塑形:万有引力",
        "type": SUB,
        # 引力
        "subtype": "gravitational",
        # 拋射物指定半徑內
        "radius": 3,
        # 吸力，越大越快 (可能會直接撞上拋射物導致效果中斷)
        "power": 1,
        "costMultiple": 1.1,
    },
    "default:operator_continued_damage": {
        "name": "塑形:持续伤害",
        "type": SUB,
        # 持續
        "subtype": "continuedDamage",
        # 拋射物指定半徑內
        "radius": 3,
        # 每次給予的傷害
        "damage": 2,
        # 攻擊頻率，如下: 每 15 tick 攻擊一次
        "frequencyTick": 15,
        "costMultiple": 1.1,
    },
}
# 禁止被替换的方块
REPLACE_BLOCK_FORBIDDEN_LIST = {
    "minecraft:air",
    "minecraft:bedrock",
    "minecraft:chest",
    "minecraft:trapped_chest",
    "minecraft:dispenser",
    "minecraft:dropper",
    "minecraft:furnace",
    "minecraft:lit_furnace",
    "minecraft:brewingstandblock",
    "minecraft:hopper",
    "minecraft:undyed_shulker_box",
    "minecraft:shulker_box",
    "minecraft:barrel",
    "minecraft:smoker",
    "minecraft:lit_smoker",
    "minecraft:blast_furnace",
    "minecraft:lit_blast_furnace",
    "minecraft:campfire",
    "minecraft:soul_campfire",
    "minecraft:jukebox",
    "minecraft:tallgrass",
}
