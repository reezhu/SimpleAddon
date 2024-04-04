# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *

"""
自定义武器模块，会使用模型渲染手持武器（需要将物品配置为不可见）
另外提供了蓄力武器的一般功能
"""


class WeaponServerModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Weapon, version=-1)
    def __init__(self):
        super(WeaponServerModule, self).__init__()

    def example(self, system):
        system.addData(StaticConfig.Data.WEAPON_BOW, {
            # 物品id
            "minecraft:bow": {
                # 拉弓的最低有效比例
                "minDuration": 0.1,
                # 消耗的物品
                "cost": {("minecraft:arrow", 0): {
                    # 发射抛射物实体
                    "projectile": "minecraft:arrow",
                    # 抛射物属性
                    "projectile_params": lambda percent: {
                        "power": percent * 2.0,
                        "gravity": 0.1,
                        "damage": percent * 10,
                        "isDamageOwner": False
                    }
                }},

            }
        }, version=0)
        # 自动添加渲染的手持物品
        system.addData(StaticConfig.Data.WEAPON_CUSTOM, {
            # 物品id
            "minecraft:bow": {
                # 用于渲染的美术资源，必填字段
                "render": {
                    # 原版状态下的模型、贴图、材质
                    "vanilla_geometry": "geometry.pig",
                    "vanilla_texture": "textures/entity/pig/pig",
                    "vanilla_material": "entity_alphatest",
                    # tpos状态下的模型、贴图、材质
                    "tpos_geometry": "geometry.decorator.ring.tpos",
                    "tpos_texture": "textures/blocks/wool_colored_red",
                    "tpos_material": "entity_alphatest",
                },
                # 需要播放的第三与第一人称动画，可选字段
                "animations": [
                    {"third": "animation.pig.setup.v1.0", "first": "first_animation", },
                    {"third": "third_animation", "first": "first_animation", },
                ],

            }
        }, version=0)
