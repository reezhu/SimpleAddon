# -*- coding: utf-8 -*-
# @Author  : Ree
import random

import math

from pythonScripts.client import ClientUtils
from pythonScripts.server import ServerUtils
from pythonScripts.share import StaticConfig
from pythonScripts.share import VectorUtils
from pythonScripts.share.skills.SkillSelector import TargetSelector, VictimSelector

"""
这里定义了大量可以直接使用的技能效果，配置见技能模块
"""


class BaseSkillEffect(object):
    def __init__(self, time):
        self.time = time

    def onClientDispatch(self, playerId, system, **kwargs):
        pass

    def onServerDispatch(self, playerId, system, **kwargs):
        pass


class DamageEffect(BaseSkillEffect):
    exclude = {"minecraft:item", "minecraft:xp_orb"}

    def __init__(self, time=0, damage=1, target=TargetSelector.ALL, radius=5, effects=[]):
        # type:  (int,int, callable[[str,tuple,tuple], bool], int, list) -> None

        BaseSkillEffect.__init__(self, time)
        self.effects = effects
        self.radius = radius
        self.target = target
        self.damage = damage

    def onServerDispatch(self, playerId, system, **kwargs):
        shake = 1
        pos = ServerUtils.getPos(playerId)
        rot = ServerUtils.getRot(playerId)
        rot = VectorUtils.angle2vector(rot)
        for entityId in ServerUtils.getEntitiesAround(playerId, radius=self.radius):
            if ServerUtils.getIdentifier(entityId) not in self.exclude and entityId != playerId:
                # print "target", self.target, type(self.target)
                if ServerUtils.getPos(entityId) is None or not self.target(entityId, pos, rot):
                    # print "skip", entityId, ServerUtils.getIdentifier(entityId)
                    continue

                damage = self.damage
                if "damageBooster" in kwargs:  # 使用damageBooster来后期调整伤害
                    damage = kwargs["damageBooster"](playerId, damage)
                if damage > 0:
                    ServerUtils.attack(playerId, entityId, damage)
                elif damage < 0:
                    ServerUtils.killEntity(entityId)
                shake += 1
                for effect in self.effects:
                    effect.onServerDispatch(system, playerId, entityId)


class AreaDamageEffect(BaseSkillEffect):
    exclude = {"minecraft:item", "minecraft:xp_orb"}

    def __init__(self, time=0, damage=1, offset=(0, 0), target=TargetSelector.ALL, radius=5, effects=[]):
        # type:  (int,int,tuple, callable[[str,tuple,tuple], bool], int, list) -> None

        BaseSkillEffect.__init__(self, time)
        self.offset = offset
        self.effects = effects
        self.radius = radius
        self.target = target
        self.damage = damage

    def onServerDispatch(self, playerId, system, **kwargs):
        shake = 1
        pos = ServerUtils.getPos(playerId)
        rot = ServerUtils.getRot(playerId)
        face = VectorUtils.angle2vector((0, rot[1]))
        face = VectorUtils.normalize(face)
        side = VectorUtils.cross(face, (0, 1, 0))
        side = VectorUtils.normalize(side)
        targetPos = VectorUtils.add(pos, (VectorUtils.multiple(face, self.offset[0])))
        targetPos = VectorUtils.add(targetPos, (VectorUtils.multiple(side, self.offset[1])))
        # ServerUtils.dispatchCmd(playerId,"particle minecraft:lava_drip_particle %.1f %.1f %.1f"%tpos)
        for entityId in ServerUtils.getEntitiesAroundPos(ServerUtils.getDimension(playerId), targetPos, radius=self.radius):
            if ServerUtils.getIdentifier(entityId) not in self.exclude and entityId != playerId:
                # print "target", self.target, type(self.target)
                if ServerUtils.getPos(entityId) is None or not self.target(entityId, pos, rot):
                    # print "skip", entityId, ServerUtils.getIdentifier(entityId)
                    continue

                damage = self.damage
                if "damageBooster" in kwargs:  # 使用damageBooster来后期调整伤害
                    damage = kwargs["damageBooster"](playerId, damage)
                if damage > 0:
                    ServerUtils.attack(playerId, entityId, int(damage))
                elif damage < 0:
                    ServerUtils.killEntity(entityId)
                shake += 1
                for effect in self.effects:
                    effect.onServerDispatch(system, playerId, entityId)


class CommandEffect(BaseSkillEffect):
    def __init__(self, time=0, cmd=""):
        BaseSkillEffect.__init__(self, time)
        self.cmd = cmd

    def onServerDispatch(self, playerId, system, **kwargs):
        ServerUtils.dispatchCmd(playerId, self.cmd)


class SoundEffect(BaseSkillEffect):
    def __init__(self, time=0, name="", volume=1.0):
        BaseSkillEffect.__init__(self, time)
        self.volume = volume
        self.name = name

    def onServerDispatch(self, playerId, system, **kwargs):
        x, y, z = ServerUtils.getPos(playerId)
        ServerUtils.dispatchCmd(playerId, "playsound %s @a %.1f %.1f %.1f %.1f" % (self.name, x, y, z, self.volume))


class ExplosionEffect(BaseSkillEffect):
    def __init__(self, time=0, front=10, power=10):
        BaseSkillEffect.__init__(self, time)
        self.power = power
        self.front = front

    def onServerDispatch(self, playerId, system, **kwargs):
        pos = VectorUtils.findFront(ServerUtils.getPos(playerId), ServerUtils.getRot(playerId), self.front)
        ServerUtils.createExplosion(playerId, pos, self.power, sourceId=playerId, fire=False, breaks=True)


class ExplosionOptimizedEffect(BaseSkillEffect):
    def __init__(self, time=0, front=10, radius=10, damage=None, knockPower=None, fire=True, breaks=True):
        BaseSkillEffect.__init__(self, time)
        self.radius = radius
        self.front = front
        self.damage = damage if damage is not None else radius
        self.knockPower = knockPower if knockPower is not None else radius
        self.fire = fire
        self.breaks = breaks

    def onServerDispatch(self, playerId, system, **kwargs):
        pos = VectorUtils.findFront(ServerUtils.getPos(playerId), ServerUtils.getRot(playerId), self.front)
        ServerUtils.createOptimizeExplosion(playerId, ServerUtils.getDimension(playerId), pos, self.radius, self.damage, self.knockPower, self.fire, self.breaks)


class TeleportEffect(BaseSkillEffect):
    def __init__(self, time=0, range=10):
        BaseSkillEffect.__init__(self, time)
        self.range = range

    def onServerDispatch(self, playerId, system, **kwargs):
        pos = ServerUtils.getPos(playerId)
        rot = ServerUtils.getRot(playerId)
        x, y, z = VectorUtils.angle2vector(rot)
        rot = VectorUtils.normalize((x, 0, z))
        pos = VectorUtils.add(pos, VectorUtils.multiple(rot, self.range))
        ServerUtils.setPos(playerId, pos)


class MotionEffect(BaseSkillEffect):
    def __init__(self, time=0, speed=1):
        BaseSkillEffect.__init__(self, time)
        self.speed = speed

    def onClientDispatch(self, playerId, system, **kwargs):
        rot = ClientUtils.getRot(playerId)
        x, y, z = VectorUtils.angle2vector(rot)
        rot = VectorUtils.normalize((x, 0, z))
        ClientUtils.setMotion(playerId, VectorUtils.multiple(rot, self.speed))

    def onServerDispatch(self, playerId, system, **kwargs):
        rot = ServerUtils.getRot(playerId)
        x, y, z = VectorUtils.angle2vector(rot)
        rot = VectorUtils.normalize((x, 0, z))
        ServerUtils.addMotion(playerId, VectorUtils.multiple(rot, self.speed))


# Y 軸速度
class MotionByYEffect(BaseSkillEffect):
    def __init__(self, time=0, speed=1):
        BaseSkillEffect.__init__(self, time)
        self.speed = speed

    def onClientDispatch(self, playerId, system, **kwargs):
        ClientUtils.setMotion(playerId, VectorUtils.multiple((0, 1, 0), self.speed))

    def onServerDispatch(self, playerId, system, **kwargs):
        ServerUtils.addMotion(playerId, VectorUtils.multiple((0, 1, 0), self.speed))


class ServerBindSfxEffect(BaseSkillEffect):
    def __init__(self, time=0, path="", scale=(1, 1, 1), faceCamera=False, layer=1, loop=False, bindOffset=(0, 1, 0), bindRot=(0, 0, 0), randomRadius=0, livetime=-1):
        BaseSkillEffect.__init__(self, time)
        self.livetime = livetime
        self.randomRadius = randomRadius
        self.bindRot = bindRot
        self.bindOffset = bindOffset
        self.loop = loop
        self.layer = layer
        self.faceCamera = faceCamera
        self.scale = scale
        self.path = path

    def onServerDispatch(self, playerId, system, **kwargs):
        offset = self.bindOffset
        if type(self.randomRadius) == tuple:
            x, y, z = self.randomRadius
            offset = VectorUtils.add(offset, (x * random.random() * 2 - x, y * random.random() * 2 - y, z * random.random() * 2 - z))

        elif self.randomRadius > 0:
            offset = VectorUtils.add(offset, (self.randomRadius * random.random() * 2 - self.randomRadius, self.randomRadius * random.random() * 2 - self.randomRadius, self.randomRadius * random.random() * 2 - self.randomRadius))

        data = {"path": self.path, "bind": playerId, "scale": self.scale, "faceCamera": self.faceCamera, "layer": self.layer, "loop": self.loop, "bindOffset": offset, "bindRot": self.bindRot, "livetime": self.livetime}
        # print "ServerBindSfxEffect", data
        ServerUtils.getSystem().BroadcastToAllClient(StaticConfig.Event.SFXEvent, data)


class ServerBindParticleEffect(BaseSkillEffect):
    def __init__(self, time=0, path="", layer=1, bindOffset=(0, 1, 0), bindRot=(0, 0, 0), correction=False, livetime=-1):
        BaseSkillEffect.__init__(self, time)
        self.livetime = livetime
        self.correction = correction
        self.bindRot = bindRot
        self.bindOffset = bindOffset
        self.layer = layer
        self.path = path

    def onServerDispatch(self, playerId, system, **kwargs):
        data = {"path": self.path, "bind": playerId, "layer": self.layer, "bindOffset": self.bindOffset, "bindRot": self.bindRot, "correction": self.correction, "livetime": self.livetime}
        ServerUtils.getSystem().BroadcastToAllClient(StaticConfig.Event.ParticleEvent, data)


# 根據玩家朝向播放特效
class ParticleEffectByPlayerFace(BaseSkillEffect):
    def __init__(self, time=0, path="", layer=1, offset=(0, 0, 0), correction=False, livetime=-1):
        BaseSkillEffect.__init__(self, time)
        self.livetime = livetime
        self.correction = correction
        self.offset = offset
        self.layer = layer
        self.path = path

    def onServerDispatch(self, playerId, system, **kwargs):
        playerRot = ServerUtils.getRot(playerId)
        playerPos = ServerUtils.getPos(playerId)
        distance = self.offset[2]
        angle = math.atan2(self.offset[0], self.offset[2]) * 180.0 / math.pi
        rot = (playerRot[0], playerRot[1] + angle)
        targetPos = VectorUtils.add(playerPos, (0, self.offset[1], 0))
        data = {"path": self.path, "pos": VectorUtils.findFront(targetPos, rot, distance), "layer": self.layer, "correction": self.correction, "livetime": self.livetime}
        ServerUtils.getSystem().BroadcastToAllClient(StaticConfig.Event.ParticleEvent, data)


# 根據玩家朝向播放編輯器序列幀特效
class SfxEditorEffectByPlayerFace(BaseSkillEffect):
    def __init__(self, time=0, path="", layer=1, offset=(0, 0, 0), loop=False, livetime=-1):
        BaseSkillEffect.__init__(self, time)
        self.livetime = livetime
        self.loop = loop
        self.offset = offset
        self.layer = layer
        self.path = path

    def onServerDispatch(self, playerId, system, **kwargs):
        playerRot = ServerUtils.getRot(playerId)
        playerPos = ServerUtils.getPos(playerId)
        distance = self.offset[2]
        angle = math.atan2(self.offset[0], self.offset[2]) * 180.0 / math.pi
        rot = (playerRot[0], playerRot[1] + angle)
        targetPos = VectorUtils.add(playerPos, (0, self.offset[1], 0))
        data = {"path": self.path, "pos": VectorUtils.findFront(targetPos, rot, distance), "layer": self.layer, "loop": self.loop, "livetime": self.livetime}
        ServerUtils.getSystem().BroadcastToAllClient(StaticConfig.Event.SFXEditorEvent, data)


class BindingSfxEffect(BaseSkillEffect):
    def __init__(self, time=0, path="", scale=(1, 1, 1), faceCamera=False, layer=1, loop=False, bindOffset=(0, 1, 0), bindRot=(0, 0, 0), firstOffset=None, firstRot=None, firstScale=None, livetime=-1):
        BaseSkillEffect.__init__(self, time)
        self.livetime = livetime
        self.firstScale = firstScale
        self.firstRot = firstRot
        self.firstOffset = firstOffset
        self.bindRot = bindRot
        self.bindOffset = bindOffset
        self.loop = loop
        self.layer = layer
        self.faceCamera = faceCamera
        self.scale = scale
        self.path = path

    def onClientDispatch(self, playerId, system, **kwargs):
        if ClientUtils.getCurrentPlayerId() == playerId and ClientUtils.getPerspective() == 0:
            entityId = ClientUtils.createSfx(self.path, bind=playerId, scale=self.scale if self.firstScale is None else self.firstScale, faceCamera=self.faceCamera, layer=self.layer, loop=self.loop,
                                             bindOffset=self.bindOffset if self.firstOffset is None else self.firstOffset,
                                             bindRot=self.bindRot if self.firstRot is None else self.firstRot)
        else:
            entityId = ClientUtils.createSfx(self.path, bind=playerId, scale=self.scale, faceCamera=self.faceCamera, layer=self.layer, loop=self.loop, bindOffset=self.bindOffset, bindRot=self.bindRot)
        if self.livetime > 0:
            scheduler = ClientUtils.getModule(StaticConfig.Module.Scheduler)
            scheduler.runFuncTaskLater(self.livetime, ClientUtils.removeParticle, entityId)


class FlySfxEffect(BaseSkillEffect):
    def __init__(self, time=0, path="", offset=(0, -1, 0), projectile=StaticConfig.Entity.EmptyProjectile, scale=(1, 1, 1), faceCamera=False, layer=1, loop=True, bindOffset=(0, 1, 0), bindRot=(0, 0, 0), power=1, gravity=0, needY=False):
        BaseSkillEffect.__init__(self, time)
        self.offset = offset
        self.gravity = gravity
        self.needY = needY
        self.power = power
        self.projectile = projectile
        self.bindRot = bindRot
        self.bindOffset = bindOffset
        self.loop = loop
        self.layer = layer
        self.faceCamera = faceCamera
        self.scale = scale
        self.path = path

    def onServerDispatch(self, playerId, system, **kwargs):
        pos = ServerUtils.getPos(playerId)
        rot = ServerUtils.getRot(playerId)
        x, y, z = VectorUtils.angle2vector(rot)
        x, y, z = VectorUtils.normalize((x, y, z) if self.needY else (x, 0, z))
        param = {
            'position': VectorUtils.add(pos, self.offset),
            'direction': (x, y, z),
            'power': self.power,
            'gravity': self.gravity,
            "damage": 0,
        }
        projectileId = ServerUtils.shootProjectile(playerId, self.projectile, param)
        ServerUtils.getSystem().BroadcastToAllClient(StaticConfig.Event.SFXEvent, {"path": self.path, "scale": self.scale, "faceCamera": self.faceCamera, "loop": self.loop, "bind": projectileId, "bindOffset": self.bindOffset, "bindRot": self.bindRot})


class ShakeEffect(BaseSkillEffect):  # todo 替换成camerashake
    def __init__(self, time=0, force=0.1, duration=5):
        BaseSkillEffect.__init__(self, time)
        self.force = force
        self.duration = duration

    def onClientDispatch(self, playerId, system, **kwargs):
        from pythonScripts.client.service.Camera import camera
        camera.makeFovShake(self.force, self.duration)


class DepartShakeEffect(BaseSkillEffect):
    def __init__(self, time=0, force=0.1, duration=5):
        BaseSkillEffect.__init__(self, time)
        self.force = force
        self.duration = duration

    def onClientDispatch(self, playerId, system, **kwargs):
        from pythonScripts.client.service.Camera import camera
        camera.makeShake(self.force, self.duration)


class TempDecoratorEffect(BaseSkillEffect):
    def __init__(self, time=0, key="temp", duration=5, geometry="", texture="", material="entity_alphatest", tpos_geometry=None, tpos_texture=None, tpos_material=None):
        BaseSkillEffect.__init__(self, time)
        self.geometry = geometry
        self.texture = texture
        self.material = material
        self.tpos_geometry = tpos_geometry if tpos_geometry is not None else geometry
        self.tpos_texture = tpos_texture if tpos_texture is not None else texture
        self.tpos_material = tpos_material if tpos_material is not None else material
        self.key = key
        self.duration = duration

    def onClientDispatch(self, playerId, system, **kwargs):
        module = ClientUtils.getModule(StaticConfig.Module.Stand)  # type:StandModule
        module.addDecorator(playerId, self.key, self.geometry, self.tpos_geometry, self.texture, self.tpos_texture, self.material, self.tpos_material)
        scheduler = ClientUtils.getModule(StaticConfig.Module.Scheduler)
        scheduler.runFuncTaskLater(self.duration, module.removeDecorator, playerId, self.key)


class AnimationEffect(BaseSkillEffect):
    def __init__(self, time=0, animation="", first_animation=None, tpos_animation=None, tpos_first_animation=None, duration=-1, singleton=False):
        BaseSkillEffect.__init__(self, time)
        self.tpos_first_animation = tpos_first_animation if tpos_first_animation is not None else first_animation
        self.tpos_animation = tpos_animation if tpos_animation is not None else animation
        self.animation = animation
        self.first_animation = first_animation if first_animation is not None else animation
        self.duration = duration
        self.singleton = singleton

    def onClientDispatch(self, playerId, system, **kwargs):
        module = ClientUtils.getModule(StaticConfig.Module.Stand)  # type:StandModule
        info = module.getAvatarStatus(playerId)
        isTpos = info.get("tpos", False)
        module.playAnimation(playerId, self.tpos_animation if isTpos else self.animation, t=self.duration, first_animation=self.tpos_first_animation if isTpos else self.first_animation, singleton=self.singleton)


class SoftAnimationEffect(BaseSkillEffect):
    # 注意！该效果的duration单位为秒
    def __init__(self, time=0, animation="", first_animation=None, duration=-1, fade_in=0.2, fade_out=0.2):
        BaseSkillEffect.__init__(self, time)
        self.animation = animation
        self.first_animation = first_animation if first_animation is not None else animation
        self.duration = duration
        self.fade_in = fade_in
        self.fade_out = fade_out

    def onClientDispatch(self, playerId, system, **kwargs):
        module = ClientUtils.getModule(StaticConfig.Module.StandAnimation)  # type:StandAnimation
        module.playAnimation(playerId, self.animation, t=self.duration, first_animation=self.first_animation, fade_in=self.fade_in, fade_out=self.fade_out)


class ProjectileEffect(BaseSkillEffect):
    def __init__(self, time=0, combos=[]):
        BaseSkillEffect.__init__(self, time)
        self.combos = combos

    def onServerDispatch(self, playerId, system, **kwargs):
        module = ServerUtils.getModule(StaticConfig.Module.Projectile)  # type:ProjectileModule
        dic = {}
        if "showTips" in kwargs: dic["showTips"] = kwargs["showTips"]  # 使用showTips来开启默认的消息提示
        if "costCallback" in kwargs: dic["costCallback"] = kwargs["costCallback"]  # 使用costCallback来扣除魔法量
        if "damageBooster" in kwargs: dic["damageBooster"] = kwargs["damageBooster"]  # 使用costCallback来调整伤害

        module.shoot(playerId, self.combos, **dic)


# 屏障
class ShieldEffect(BaseSkillEffect):
    def __init__(self, time=0, shieldId="", distance=2, duration=1, effects=[]):
        BaseSkillEffect.__init__(self, time)
        self.shieldId = shieldId
        self.distance = distance
        self.duration = duration
        self.effects = effects

    def onServerDispatch(self, playerId, system, **kwargs):
        pitch, yaw = ServerUtils.getRot(playerId)
        playerPos = ServerUtils.getFootPos(playerId)
        upVector = VectorUtils.angle2vector((pitch, yaw))
        upVector = (upVector[0], 0, upVector[2])
        upVector = VectorUtils.normalize(upVector)
        entityId = ServerUtils.createEngineEntityByTypeStr(self.shieldId,
                                                           VectorUtils.add(playerPos, VectorUtils.multiple(upVector, self.distance)),
                                                           (pitch, yaw),
                                                           ServerUtils.getDimension(playerId))
        ServerUtils.setExtraData("shield_owner", playerId, entityId)
        scheduler = ServerUtils.getModule(StaticConfig.Module.Scheduler)
        scheduler.runFuncTaskLater(self.duration, self.onShieldRemove, entityId, system, **kwargs)
        for effect in self.effects:
            scheduler.runFuncTaskLater(effect.time, effect.onServerDispatch, entityId, system, **kwargs)
            # effect.onServerDispatch(playerId=entityId, system=system, **kwargs)

    def onShieldRemove(self, entityId, system, **kwargs):
        ServerUtils.removeEntity(entityId)


class SpreadEffect(BaseSkillEffect):
    def __init__(self, time=0, spreadDistance=10, maxRange=64, victim=VictimSelector.Self):
        BaseSkillEffect.__init__(self, time)
        self.spreadDistance = spreadDistance
        self.maxRange = maxRange
        self.victim = victim

    def onServerDispatch(self, playerId, system, **kwargs):
        ServerUtils.dispatchCmd(playerId, "/spreadplayers ~ ~ {spreadDistance} {maxRange} {victim}".
                                format(spreadDistance=self.spreadDistance, maxRange=self.maxRange, victim=self.victim))


class SummonEntityEffect(BaseSkillEffect):
    def __init__(self, time=0, entityId=""):
        BaseSkillEffect.__init__(self, time)
        self.entityId = entityId

    def onServerDispatch(self, playerId, system, **kwargs):
        ServerUtils.createEngineEntityByTypeStr(self.entityId, ServerUtils.getPos(playerId), ServerUtils.getRot(playerId), ServerUtils.getDimension(playerId))


class SelfFrozenEffect(BaseSkillEffect):
    def __init__(self, time=0, duration=30):
        BaseSkillEffect.__init__(self, time)
        self.duration = duration

    def onServerDispatch(self, playerId, system, **kwargs):
        ServerUtils.setAiEnable(playerId, False)
        scheduler = ServerUtils.getModule(StaticConfig.Module.Scheduler)
        scheduler.runFuncTaskLater(self.duration, ServerUtils.setAiEnable, playerId, True)

    def onClientDispatch(self, playerId, system, **kwargs):
        import mod.client.extraClientApi as clientApi
        if playerId == clientApi.GetLocalPlayerId():
            comp = clientApi.GetEngineCompFactory().CreateOperation(clientApi.GetLocalPlayerId())
            comp.SetCanAll(False)
            scheduler = ClientUtils.getModule(StaticConfig.Module.Scheduler)
            scheduler.runFuncTaskLater(self.duration, comp.SetCanAll, True)


class DynamicUiEffect(BaseSkillEffect):
    def __init__(self, time=0, key="", name="temp", onlyFirst=True, duration=-1):
        BaseSkillEffect.__init__(self, time)
        self.duration = duration
        self.onlyFirst = onlyFirst
        self.name = name
        self.key = key

    def onClientDispatch(self, playerId, system, **kwargs):
        import mod.client.extraClientApi as clientApi
        if playerId == clientApi.GetLocalPlayerId() and (ClientUtils.getPerspective() == 0 or not self.onlyFirst):
            ClientUtils.getModule(StaticConfig.Module.DynamicUiModule).ConditionDynamicUiEvent({
                "isOpen": True,
                "name": self.name,
                "key": self.key,
            })
            if self.duration > 0:
                ClientUtils.getModule(StaticConfig.Module.DynamicUiModule).ConditionDynamicUiEvent({
                    "isOpen": False,
                    "name": self.name,
                    "key": self.key,
                })
