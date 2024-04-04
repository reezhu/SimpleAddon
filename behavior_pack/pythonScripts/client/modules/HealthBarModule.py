# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.client.modules.BaseClientModule import *

'''
给部分生物显示网易那个丑丑的血条
仅提供配置
'''


class HealthBarModule(BaseClientModule):

    @DefaultClientModule(name=StaticConfig.Module.HealthBar, version=-1)
    def __init__(self):
        super(HealthBarModule, self).__init__()

    def example(self, system):
        system.addData(StaticConfig.Data.HEALTHBAR, {
            # lambda用于判断是否显示血条，默认不显示
            "minecraft:pig": lambda entityId: True,
        })
