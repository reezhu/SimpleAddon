# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *


class RpcServerModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Broadcast, version=-1)
    def __init__(self):
        super(RpcServerModule, self).__init__()

    def example(self, system):
        """
        特殊！此配置会被调用，请勿修改
        @param system:
        """
        # ---------------------------------------以下需要配置---------------------------------------
        # 未特殊说明物品支持盔甲、饰品、手持物品与套装
        # 攻击特效
        system.addData(
            StaticConfig.Data.BROADCAST_QUERY,
            {
                "inventory": lambda playerId: utils.getInventoryContents(playerId),
                "equipment": lambda playerId: utils.getArmor(playerId),
                "decorator": lambda playerId: utils.getDecorators(playerId),
                "hold": lambda playerId: utils.getItemInHand(playerId),
                "offhand": lambda playerId: utils.getItemInOffHand(playerId),
                "health": lambda playerId: {
                    "now": utils.getEntityAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH
                    ),
                    "max": utils.getEntityMaxAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH
                    ),
                },
                "speed": lambda playerId: {
                    "now": utils.getEntityAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.SPEED
                    ),
                    "max": utils.getEntityMaxAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.SPEED
                    ),
                },
                "damage": lambda playerId: {
                    "now": utils.getEntityAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.DAMAGE
                    ),
                    "max": utils.getEntityMaxAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.DAMAGE
                    ),
                },
                "hunger": lambda playerId: {
                    "now": utils.getEntityAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.HUNGER
                    ),
                    "max": utils.getEntityMaxAttr(
                        playerId, serverApi.GetMinecraftEnum().AttrType.HUNGER
                    ),
                },
                "online": lambda playerId: utils.getOnlinePlayers(),
                "name": lambda playerId: utils.getName(playerId),
            },
            version=0,
        )
