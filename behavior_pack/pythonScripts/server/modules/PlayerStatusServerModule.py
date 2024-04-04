# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *


class PlayerStatusServerModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Status, version=-1)
    def __init__(self):
        super(PlayerStatusServerModule, self).__init__()

    def addStatus(self, key, playerId, multiple=0.0, amount=0):
        """
        安全添加数值
        @param key:
        @param playerId:
        @param multiple:
        @param amount:
        """
        pass

    def addMaxStatus(self, key, playerId, multiple=0.0, amount=0):
        """
        安全添加数值上限
        @param key:
        @param playerId:
        @param multiple:
        @param amount:
        """
        pass

    def setMaxStatus(self, key, playerId, value):
        """
        安全设置数值上限
        :param value:
        :param key:
        :param playerId:
        """
        pass

    def getStatusSet(self, key, playerId):
        """
        查询数值状态
        @param key:
        @param playerId:
        @return:
        """
        pass

    def getStatusAmount(self, key, playerId):
        """
        只查询数值的数值
        @param key:
        @param playerId:
        @return:
        """
        pass

    def setStatus(self, key, playerId, current):
        """
        设置数值
        @param key:
        @param current:
        @param playerId:
        @return:
        """
        pass

    def example(self, system):
        system.addData(StaticConfig.Data.STATUS_DETAIL, {
            "mana": {
                "default_now": 0,  # 默认初始值
                "default_max": 10,  # 默认初始最大值
                "recover": {  # 选填，自动回复
                    "period": 1,  # 多少秒进行一次恢复
                    "multiple": 0.1,  # 恢复的百分比
                    "amount": 1,  # 恢复的具体值

                }
            },
            "exp": {
                "default_now": 0,
                "default_max": 20,
                "transfer": {  # 选填，自动升级
                    "to": "lvl",  # 升级的目标数值
                    "to_amount": lambda amount: amount + 1,  # 目标数值的变化量
                    "from_now": lambda now, max: max - now,  # 起始数值的变化量，此配置为做差，也可以直接配置变成0
                    "from_max": lambda max, tnow: tnow * 10 + 30,  # 起始数值的新最大值,max为当前最大值，tnow为目标值的当前值（尚未进行to_amount操作）
                },
                "recover": {  # 选填，自动回复
                    "period": 1,  # 多少秒进行一次恢复
                    "multiple": 0,  # 恢复的百分比
                    "amount": 1,  # 恢复的具体值

                }

            },
            "lvl": {
                "default_now": 0,
                "default_max": float("inf"),  # 这样可以表示无限

            },
        })
