# -*- coding: utf-8 -*-
# @Author  : Ree
import itertools

from pythonScripts.client.UiComponents import *
from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.client.modules.StandModule import StandModule
from pythonScripts.server.modules.BroadcastModule import AnswerPlayerInfoEvent
from pythonScripts.server.modules.BroadcastModule import QueryPlayerInfoEvent
from pythonScripts.share.DecoratorConfig import DECORATOR_SLOT_TYPE
from pythonScripts.share.DecoratorConfig import SlotType

ScreenNode = clientApi.GetCustomUIControlProxyCls()
"""
这是饰品主模块，用于配置饰品的模型与动画
仅提供配置
"""


class DecoratorMainModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.DecoratorMainModule, version=-1)
    def __init__(self):
        super(DecoratorMainModule, self).__init__()

    def example(self, system):
        system.addData(
            StaticConfig.Data.DECORATOR,
            {
                # 饰品
                "minecraft:diamond_sword": {
                    # 饰品可以放入的格子，理论上可以写多个
                    "type": {SlotType.AVATAR},
                    # 用于渲染的美术资源，可选字段
                    "render": {
                        # 原版状态下的模型、贴图、材质
                        "vanilla_geometry": "geometry.decorator.ring.vanilla",
                        "vanilla_texture": "textures/blocks/wool_colored_lime",
                        "vanilla_material": 0,
                        # tpos状态下的模型、贴图、材质
                        "tpos_geometry": "geometry.decorator.ring.tpos",
                        "tpos_texture": "textures/blocks/wool_colored_red",
                        "tpos_material": 2,
                    },
                    # 需要播放的第三与第一人称动画，可选字段
                    "animations": [
                        {
                            "third": "third_animation",
                            "first": "first_animation",
                        },
                        {
                            "third": "third_animation",
                            "first": "first_animation",
                        },
                    ],
                    # 只有SlotType.AVATAR会生效，放入后会变身
                    "avatar": {
                        # 变身的几何体
                        "geometry": "geometry.t_pos.pain",
                        # 变身的贴图
                        "texture": "textures/entity/pain",
                        # 变身的材质
                        "material": 0,
                        # 变身是否tpos
                        "tpos": True,
                        # 变身后替换的原版动作
                        "animations": {"move.arms": "animation.ninja.move.arms"},
                        # 变身后持续播放的额外动作
                        "loop": {"wave_wings", "shake_hands"},
                    },
                },
                "minecraft:diamond_axe": {"type": {SlotType.BELT}},
                "minecraft:diamond_pickaxe": {
                    "type": {SlotType.TALISMAN},
                    # 加入这个字段可以让这个物品无法取下
                    "canRemove": False,
                },
            },
            version=0,
        )
