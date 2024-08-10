# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server.modules.BaseServerModule import *

"""
抛射物模块
todo: 添加配置生成使用抛射物的功能
"""


class ProjectileModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Projectile, version=-1)
    def __init__(self):
        super(ProjectileModule, self).__init__()

    def shoot(
        self, playerId, spellList, costCallback=None, costTips=False, damageBooster=None
    ):
        """
        发射一个自定义子弹
        :param playerId: 发射的玩家
        :param sList: 发射的魔咒配置，见SpellConfig.spells
        :param costCallback: 消耗扣除的回调（比如魔力），接受参数：cost
        :param showTips: 是否显示tip
        @param damageBooster: 伤害加成，用于后期根据等级或者其他参数加强子弹威力，接受参数：playerId, damage
        :return:
        """
        pass
