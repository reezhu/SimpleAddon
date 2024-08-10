# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server import ServerUtils

"""
这里定义了大量可以直接使用的伤害效果，配置见技能模块
"""


class DamageEffectTargetBaseBean(object):

    def onServerDispatch(self, system, playerId, entityId):
        pass


class DamageEffectTargetSfx(DamageEffectTargetBaseBean):
    def __init__(self, path, scale=(1, 1, 1)):
        self.scale = scale
        self.path = path

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        pos = ServerUtils.getPos(entityId)
        from pythonScripts.share import StaticConfig

        system.BroadcastToAllClient(
            StaticConfig.Event.SFXEvent,
            {"path": self.path, "pos": pos, "bind": entityId, "scale": self.scale},
        )


class DamageEffectTargetParticle(DamageEffectTargetBaseBean):
    def __init__(self, path, bindOffset=(0, 0, 0), bindRot=(0, 0, 0)):
        self.bindRot = bindRot
        self.bindOffset = bindOffset
        self.path = path

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        pos = ServerUtils.getPos(entityId)
        from pythonScripts.share import StaticConfig

        system.BroadcastToAllClient(
            StaticConfig.Event.ParticleEvent,
            {
                "path": self.path,
                "pos": pos,
                "bind": entityId,
                "bindOffset": self.bindOffset,
                "bindRot": self.bindRot,
                "correction": True,
            },
        )


class DamageEffectTargetSound(DamageEffectTargetBaseBean):
    def __init__(self, sound):
        self.sound = sound

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        x, y, z = ServerUtils.getPos(entityId)

        ServerUtils.dispatchCmd(
            playerId, "playsound %s @a %.1f %.1f %.1f" % (self.sound, x, y, z)
        )


class DamageEffectTargetLightning(DamageEffectTargetBaseBean):
    def __init__(self):
        pass

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        x, y, z = ServerUtils.getPos(entityId)

        ServerUtils.dispatchCmd(
            playerId, "summon lightning_bolt %.1f %.1f %.1f" % (x, y, z)
        )


class DamageEffectTargetTNT(DamageEffectTargetBaseBean):
    def __init__(self):
        pass

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        x, y, z = ServerUtils.getPos(entityId)

        ServerUtils.dispatchCmd(playerId, "summon tnt %.1f %.1f %.1f" % (x, y + 2, z))


class DamageEffectTargetBuff(DamageEffectTargetBaseBean):
    def __init__(self, buff, duration, amplifier, showParticles):
        self.buff = buff
        self.duration = duration
        self.amplifier = amplifier
        self.showParticles = showParticles

    def onServerDispatch(self, system, playerId, entityId):
        DamageEffectTargetBaseBean.onServerDispatch(self, system, playerId, entityId)
        ServerUtils.addEffect(
            entityId, self.buff, self.duration, self.amplifier, self.showParticles
        )
