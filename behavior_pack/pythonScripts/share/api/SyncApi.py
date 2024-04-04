# -*- coding: utf-8 -*-
# @Author  : Ree
class SyncApi:
    def get(self, playerId, key):
        """
        获取值
        @param playerId:
        @param key:
        """
        pass

    def set(self, playerId, key, value, override=False):
        """
        设置值
        :param playerId: 玩家id
        :param key:
        :param value:
        :param override: 仅可在客户端使用，代表不同步时的处理方案，False抛异常，True为强制覆盖
        """
        pass

    def getAll(self, playerId):
        """
        获取玩家的所有字典
        @param playerId:
        """
        pass
