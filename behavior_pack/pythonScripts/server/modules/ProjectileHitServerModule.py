# -*- coding: utf-8 -*-
# @Author  : PengPeng

from pythonScripts.server.modules.BaseServerModule import *

"""
击中的效果
现有功能：
被击中时触发动态ui
"""


class ProjectileHitServerModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.ProjectileHit, version=-1)
    def __init__(self):
        super(ProjectileHitServerModule, self).__init__()

    def example(self, system):
        from pythonScripts.share import StaticConfig
        system.addData(StaticConfig.Data.PROJECTILE_ANIMATION_UI, {
            # 投掷物 : 对应动态ui的 key (搭配 StaticConfig.Data.DYNAMIC_UI 配置使用)
            "minecraft:egg": "openMissionAnimation"
        }, version=0)
