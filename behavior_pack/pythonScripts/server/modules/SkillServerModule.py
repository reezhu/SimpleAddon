# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share import Scheduler
from pythonScripts.share.skills.SkillDamageEffect import *
from pythonScripts.share.skills.SkillSelector import TargetSelector

"""
技能模块，一般采用EquipmentInteractModule进行调用
"""


class SkillServerModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Skill, version=-1)
    def __init__(self):
        super(SkillServerModule, self).__init__()

    def example(self, system):
        from pythonScripts.share.skills.SkillEffect import (
            DamageEffect,
            ShakeEffect,
            AnimationEffect,
        )

        system.addData(
            StaticConfig.Data.SKILL_STAGES,
            {
                # 技能id
                "A": [
                    # 支持连招动画，所以是个列表，一般情况下配一段即可
                    {
                        "time": 30,  # 技能总时间
                        "stages": [  # 技能阶段，里面有各种效果
                            # 伤害效果
                            DamageEffect(
                                0,
                                10,
                                TargetSelector.ALL,
                                effects=[
                                    # 伤害里的敌方效果，因为主体不同所以不能使用普通EffectBean
                                    DamageEffectTargetSfx(
                                        "textures/sfxs/blade2/daoguang"
                                    ),
                                ],
                            ),
                            # 抖屏效果
                            ShakeEffect(0),
                            # 播放动画，记得加上时间字段
                            AnimationEffect(
                                0,
                                animation="animation.hello",
                                singleton=True,
                                duration=30,
                            ),
                        ],
                    },
                    {
                        "time": 30,  # 技能总时间
                        "stages": [  # 技能阶段，里面有各种效果
                            # 伤害效果
                            DamageEffect(
                                0,
                                10,
                                TargetSelector.ALL,
                                effects=[
                                    # 伤害里的敌方效果，因为主体不同所以不能使用普通EffectBean
                                    DamageEffectTargetSfx(
                                        "textures/sfxs/blade2/daoguang"
                                    ),
                                ],
                            ),
                            # 抖屏效果
                            ShakeEffect(0),
                            # 播放动画，记得加上时长字段
                            AnimationEffect(
                                0,
                                animation="animation.hello",
                                singleton=True,
                                duration=30,
                            ),
                        ],
                    },
                ],
            },
            version=0,
        )
