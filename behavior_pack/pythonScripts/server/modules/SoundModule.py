# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *

"""可配置武器攻击音效，判断当前手持位置"""


class SoundModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Sound, version=-1)
    def __init__(self):
        super(SoundModule, self).__init__()

    def example(self, system):
        # 攻击时播放的音效
        system.addData(StaticConfig.Data.SOUND_ATTACK, {
            "minecraft:diamond_sword": {"sound": "random.glass"},
        })
