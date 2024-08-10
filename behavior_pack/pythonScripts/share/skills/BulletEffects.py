# -*- coding: utf-8 -*-
# @Author  : Ree
import mod.server.extraServerApi as serverApi

import pythonScripts.server.ServerUtils as utils
from pythonScripts.share.skills.SmeltConfig import SMELTING_CONFIG_DICT
from pythonScripts.share.skills.SpellConfig import *

"""
这里定义的子弹的效果
"""


class BaseEffect(object):
    def __init__(self, identifier):
        self.identifier = identifier


class ExplodeEffect(BaseEffect):
    def __init__(self, args):
        BaseEffect.__init__(self, "explode")
        self.radius = args.get("radius", 1)
        self.damage = args.get("damage", self.radius)
        self.knock = args.get("knock", self.radius)
        self.fire = args.get("fire", False)
        self.breaks = args.get("breaks", False)

    def onHit(self, bullet, module, entityId, args):
        # print ("explosion!", self.__dict__, entityId, args)
        utils.createOptimizeExplosion(bullet.shooter, utils.getDimension(entityId), utils.getPos(entityId), damage=self.damage, radius=self.radius, knockPower=self.knock, fire=self.fire, breaks=self.breaks)


class MotionEffect(BaseEffect):
    def __init__(self, motion):
        BaseEffect.__init__(self, "motion")
        self.motion = motion

    def onTickMotion(self, motionOffset, motion, vertical, origin, time, entityId):
        if self.motion is not None:
            return self.motion(motionOffset, motion, vertical, origin, time)


# 持續傷害
class ContinuedDamageEffect(BaseEffect):
    def __init__(self, radius, frequencyTick, damage):
        BaseEffect.__init__(self, "gravitational")
        self.radius = radius
        self.frequencyTick = frequencyTick
        self.damage = damage
        self.tick = 0

    def onTickMotion(self, motionOffset, motion, vertical, origin, time, projectileId):
        if self.tick % self.frequencyTick == 0:
            entityList = utils.getEntitiesAround(projectileId, self.radius)
            playerId = utils.getExtraData("shooter", projectileId)
            for entityId in entityList:
                if entityId != projectileId and entityId != playerId:
                    utils.attack(playerId, entityId, self.damage)

        self.tick += 1
        return motionOffset


# 萬有引力
class GravityEffect(BaseEffect):
    def __init__(self, radius, power):
        BaseEffect.__init__(self, "gravitational")
        self.radius = radius
        self.power = power

    def onTickMotion(self, motionOffset, motion, vertical, origin, time, projectileId):
        entityList = utils.getEntitiesAround(projectileId, self.radius)
        projectilePos = utils.getPos(projectileId)
        playerId = utils.getExtraData("shooter", projectileId)
        for entityId in entityList:
            if entityId != projectileId and entityId != playerId:
                entityVector = VectorUtils.minus(projectilePos, utils.getPos(entityId))
                moveVector = VectorUtils.multiple(VectorUtils.normalize(entityVector), self.power)
                if VectorUtils.length(entityVector) <= 4:
                    moveVector = VectorUtils.multiple(moveVector, -1)

                if utils.getIdentifier(entityId) == "minecraft:player":
                    from pythonScripts.share import StaticConfig
                    utils.getSystem().NotifyToClient(entityId, StaticConfig.Event.BossSkillEvent, {"key": "AddMotion", "offset": VectorUtils.multiple(moveVector, 0.3)})

                utils.setMotion(entityId, moveVector)

        return motionOffset


class TrackerEffect(BaseEffect):
    def __init__(self, args):
        BaseEffect.__init__(self, "track")
        self.force = args.get("force", 0.05)
        self.radius = args.get("radius", 64)
        self.target = args.get("target", None)

    def onTickMotion(self, motionOffset, motion, vertical, origin, time, entityId):
        target = utils.getExtraData("targetId", entityId)
        if target is None:
            if self.target is not None:
                ls = utils.getEntitiesAround(entityId, self.radius, {
                    "any_of": [
                        {
                            "subject": "other",
                            "test": "is_family",
                            "value": "monster"
                        },
                        {
                            "subject": "other",
                            "test": "is_family",
                            "value": "mob"
                        },
                    ]
                })
                nearest = None
                nearestRange = 0
                myPos = utils.getPos(entityId)
                for entity in ls:
                    if entityId == entity:
                        continue
                    pos = utils.getPos(entity)
                    if pos is None:
                        continue
                    rang = VectorUtils.dot(myPos, pos)
                    if nearest is None or rang < nearestRange:
                        nearest = entity
                        nearestRange = rang
                if nearest is not None:
                    utils.setExtraData("targetId", nearest, entityId)
                    # print ("found target:", utils.getIdentifier(nearest))
            else:
                utils.setExtraData("targetId", self.target, entityId)
        else:
            targetPos = utils.getPos(target)
            if targetPos is None:
                utils.setExtraData("targetId", None, entityId)
            else:
                pos = utils.getPos(entityId)
                # print "has target", utils.getIdentifier(target), target, targetPos, pos
                return VectorUtils.multiple(VectorUtils.normalize(VectorUtils.minus(targetPos, pos)), self.force)
        return 0, 0, 0


reflectMotion = {
    0: lambda x_y_z: (x_y_z[0], -x_y_z[1], x_y_z[2]),
    1: lambda x_y_z1: (x_y_z1[0], -x_y_z1[1], x_y_z1[2]),
    2: lambda x_y_z2: (x_y_z2[0], x_y_z2[1], -x_y_z2[2]),
    3: lambda x_y_z3: (x_y_z3[0], x_y_z3[1], -x_y_z3[2]),
    4: lambda x_y_z4: (-x_y_z4[0], x_y_z4[1], x_y_z4[2]),
    5: lambda x_y_z5: (-x_y_z5[0], x_y_z5[1], x_y_z5[2]),
}


# 弹射类型
class BounceEffect(BaseEffect):
    def __init__(self):
        BaseEffect.__init__(self, "bounce")
        self.reflect = 0

    def onHit(self, bullet, module, entityId, args):
        # print ("onHit", module, entityId, args)
        pass


class ReflectEffect(BounceEffect):
    def __init__(self):
        BounceEffect.__init__(self)

    def onHit(self, bullet, module, entityId, args):
        BounceEffect.onHit(self, bullet, module, entityId, args)
        if self.reflect > 0:
            reflect = utils.getExtraData("reflect", entityId)
            reflect = 0 if reflect is None else reflect
            if reflect < self.reflect:
                motion = utils.getMotion(entityId)
                pos = utils.getPos(entityId)
                motion = reflectMotion.get(args["hitFace"])(motion)
                utils.getSystem().DestroyEntity(entityId)
                del module.entities[entityId]
                entityId = bullet.shootSingleProjectileVector(utils.getExtraData("shooter", entityId), pos, motion)
                utils.setExtraData("reflect", reflect + 1, entityId)
                module.entities[entityId] = bullet


class ReboundEffect(BounceEffect):
    def __init__(self):
        BounceEffect.__init__(self)

    def onHit(self, bullet, module, entityId, args):
        BounceEffect.onHit(self, bullet, module, entityId, args)
        if self.reflect > 0:
            reflect = utils.getExtraData("reflect", entityId)
            reflect = 0 if reflect is None else reflect
            if reflect < self.reflect:
                motion = utils.getMotion(entityId)
                pos = utils.getPos(entityId)
                motion = VectorUtils.multiple(motion, -1)
                utils.getSystem().DestroyEntity(entityId)
                del module.entities[entityId]
                entityId = bullet.shootSingleProjectileVector(utils.getExtraData("shooter", entityId), pos, motion)
                utils.setExtraData("reflect", reflect + 1, entityId)
                module.entities[entityId] = bullet


class ReplaceBlockEffect(BaseEffect):
    def __init__(self, fortunelvl=0):
        BaseEffect.__init__(self, "replaceBlock")
        self.fortunelvl = fortunelvl

    def onHit(self, bullet, module, entityId, args):
        # 可能获得和放置的方块会有问题（aux值的问题）

        if args["hitTargetType"] != "BLOCK":
            return

        playerId = args["srcId"]

        pos = args["blockPosX"], args["blockPosY"], args["blockPosZ"]
        originBlock = utils.getBlock(playerId, pos)
        iscreative = utils.getGamemode(playerId) == serverApi.GetMinecraftEnum().GameType.Creative
        if not originBlock:
            return

        originBlockName = originBlock["name"]
        if self.__isBlockReplaceForbidden(playerId, originBlockName, pos):
            return

        result = False
        for slotId in range(9):
            itemDict = utils.getInventorySlot(playerId, slotId)
            if not itemDict:
                continue

            itemName = itemDict["itemName"]
            if itemName == originBlockName:
                break

            auxValue = itemDict["auxValue"]
            result = utils.setBlock(playerId, pos, itemName, auxValue)
            if result:
                if not iscreative:
                    count = itemDict["count"]
                    utils.setInventoryItemNum(playerId, slotId, count - 1)
                break

        if result:
            aux = originBlock["aux"]
            utils.dropBlockResources(originBlockName, utils.getFootPos(playerId), aux=aux, bonusLootLevel=self.fortunelvl)

    def __isBlockReplaceForbidden(self, playerId, blockName, blockPos):
        if blockName in REPLACE_BLOCK_FORBIDDEN_LIST:
            return True

        dimension = utils.getDimension(playerId)
        data = utils.getBlockEntityData(dimension, blockPos)
        return data is not None


class ReplaceAreaBlockEffect(BaseEffect):
    def __init__(self, radius, replaceAll, fortunelvl):
        BaseEffect.__init__(self, "replaceAreaBlock")
        self.radius = radius
        self.replaceAll = replaceAll
        self.fortunelvl = fortunelvl

    def onHit(self, bullet, module, entityId, args):
        utils.addTimer(0.1, self.__onHit, bullet, module, entityId, args)

    def __onHit(self, bullet, module, entityId, args):
        # 可能获得和放置的方块会有问题（aux值的问题）

        if args["hitTargetType"] != "BLOCK":
            print("hit target type not block")
            return

        playerId = args["srcId"]

        originPos = args["blockPosX"], args["blockPosY"], args["blockPosZ"]
        originBlock = utils.getBlock(playerId, originPos)
        iscreative = utils.getGamemode(playerId) == serverApi.GetMinecraftEnum().GameType.Creative
        if not originBlock:
            print("no origin block")
            return

        originBlockName = originBlock["name"]
        if not self.replaceAll and self.__isBlockReplaceForbidden(playerId, originBlockName, originPos):
            print("origin block forbidden")
            return

        result = False
        targetItemName = None
        for slotId in range(9):
            itemDict = utils.getInventorySlot(playerId, slotId)
            if not itemDict:
                continue

            itemName = itemDict["itemName"]
            if itemName == originBlockName:
                break

            auxValue = itemDict["auxValue"]
            result = utils.setBlock(playerId, originPos, itemName, auxValue)
            if result:
                if not iscreative:
                    count = itemDict["count"]
                    utils.setInventoryItemNum(playerId, slotId, count - 1)
                targetItemName = itemName
                break

        if not result:
            print("origin block replace failed")
            return

        aux = originBlock["aux"]
        utils.dropBlockResources(originBlockName, utils.getFootPos(playerId), aux=aux, bonusLootLevel=self.fortunelvl)
        for blockpos in self.search_blocks(originPos):
            self.replaceOneBlock(playerId, blockpos, originBlockName, targetItemName, iscreative=iscreative)

    def search_blocks(self, originPos):
        for r in range(1, self.radius + 1):
            for dy in range(-r, r + 1):
                for dz in range(-r, r + 1):
                    blockpos1 = originPos[0] + r, originPos[1] + dy, originPos[2] + dz
                    blockpos2 = originPos[0] - r, originPos[1] + dy, originPos[2] + dz
                    yield blockpos1
                    yield blockpos2
            for dx in range(-r + 1, r):
                for dz in range(-r + 1, r):
                    blockpos1 = originPos[0] + dx, originPos[1] + r, originPos[2] + dz
                    blockpos2 = originPos[0] + dx, originPos[1] - r, originPos[2] + dz
                    yield blockpos1
                    yield blockpos2
            for dx in range(-r + 1, r):
                for dy in range(-r, r + 1):
                    blockpos1 = originPos[0] + dx, originPos[1] + dy, originPos[2] + r
                    blockpos2 = originPos[0] + dx, originPos[1] + dy, originPos[2] - r
                    yield blockpos1
                    yield blockpos2

    def replaceOneBlock(self, playerId, blockPos, originBlockName, targetItemName, iscreative=False):
        targetSlotId, itemDict = self.__searchItemFromInv(playerId, targetItemName)
        if not itemDict:
            print(("no item dict", targetItemName))
            return

        block = utils.getBlock(playerId, blockPos)
        if not block:
            print(("no block", blockPos))
            return

        itemName = itemDict["itemName"]
        blockName = block["name"]

        if self.replaceAll and (blockName == itemName or self.__isBlockReplaceForbidden(playerId, blockName, blockPos)):
            print("same block or forbidden, skip")
            return

        if not self.replaceAll and (blockName != originBlockName or blockName == itemName or self.__isBlockReplaceForbidden(playerId, blockName, blockPos)):
            print("not origin block or same block or forbidden, skip")
            return

        auxValue = itemDict["auxValue"]
        result = utils.setBlock(playerId, blockPos, itemName, auxValue)
        if result:
            if not iscreative:
                count = itemDict["count"]
                utils.setInventoryItemNum(playerId, targetSlotId, count - 1)
            aux = block["aux"]
            utils.dropBlockResources(blockName, utils.getFootPos(playerId), aux=aux, bonusLootLevel=self.fortunelvl)

    def __isBlockReplaceForbidden(self, playerId, blockName, blockPos):
        if blockName in REPLACE_BLOCK_FORBIDDEN_LIST:
            return True

        dimension = utils.getDimension(playerId)
        data = utils.getBlockEntityData(dimension, blockPos)
        return data is not None

    def __searchItemFromInv(self, playerId, itemName):
        for slotId in range(35, -1, -1):
            itemDict = utils.getInventorySlot(playerId, slotId)
            if not itemDict:
                continue

            if itemName == itemDict["itemName"]:
                return slotId, itemDict

        return None, None


class SmeltingEffect(BaseEffect):

    def __init__(self):
        BaseEffect.__init__(self, "burning")

    def onHit(self, bullet, module, entityId, args):
        if args["hitTargetType"] != "BLOCK":
            print("hit target type not block")
            return

        playerId = args["srcId"]

        originPos = args["blockPosX"], args["blockPosY"], args["blockPosZ"]
        originBlock = utils.getBlock(playerId, originPos)
        if not originBlock:
            print("pos not block")
            return

        smeltingTimes = bullet.smeltingTimes

        smeltingResult, smeltingResult_aux, isBlock = self.__getSmeltingResult(originBlock, smeltingTimes)
        if smeltingResult is None:
            print(("smelting result not found", originBlock["name"], smeltingTimes))
            return

        if isBlock:
            utils.setBlock(playerId, originPos, smeltingResult, aux=smeltingResult_aux)
        else:
            utils.setBlock(playerId, originPos, "minecraft:air")
            dimension = utils.getDimension(playerId)
            itemDict = utils.createPlainItemDict(smeltingResult, 1, smeltingResult_aux)
            utils.dropItemDict(dimension, originPos, itemDict)

    def __getSmeltingResult(self, originBlock, smeltingTimes):
        print(("input ", originBlock, smeltingTimes))
        name = originBlock['name']
        aux = originBlock['aux']
        result_name, result_aux, isblock = None, None, None
        for i in range(smeltingTimes):
            result_name, result_aux, isblock = self.__getSmeltingResultaux(name, aux)
            if result_name:
                name = result_name
                aux = result_aux
            else:
                break
        return result_name, result_aux, isblock

    def __getSmeltingResultaux(self, name, aux):
        result_name, result_aux, isblock = None, None, None
        if name in SMELTING_CONFIG_DICT:
            result_name, result_aux, isblock = SMELTING_CONFIG_DICT[name]
        else:
            name = "{}:{}".format(name, aux)
            if name in SMELTING_CONFIG_DICT:
                result_name, result_aux, isblock = SMELTING_CONFIG_DICT[name]
        return result_name, result_aux, isblock


class DigEffect(BaseEffect):
    def __init__(self, fortunelvl=0):
        BaseEffect.__init__(self, "dig")
        self.fortunelvl = fortunelvl

    def onHit(self, bullet, module, entityId, args):
        if args["hitTargetType"] != "BLOCK":
            print("hit target type not block")
            return

        targetId = args["targetId"]
        if targetId is None:
            return

        playerId = args["srcId"]

        originPos = args["blockPosX"], args["blockPosY"], args["blockPosZ"]
        block = utils.getBlock(playerId, originPos)
        if not block or block["name"] == "minecraft:air":
            return
        if self.__isBlockDigForbidden(playerId, block['name'], originPos):
            return

        utils.dropBlockResources(block["name"], originPos, block["aux"], bonusLootLevel=self.fortunelvl)
        utils.setBlock(playerId, originPos, "minecraft:air")

    def __isBlockDigForbidden(self, playerId, blockName, blockPos):
        if blockName in REPLACE_BLOCK_FORBIDDEN_LIST:
            return True

        dimension = utils.getDimension(playerId)
        data = utils.getBlockEntityData(dimension, blockPos)
        return data is not None


class RepayEffect(BaseEffect):
    def __init__(self, entry):
        BaseEffect.__init__(self, "repay")
        self.__repay = entry.get("repay", 0.5)

    def onHit(self, bullet, module, entityId, args):
        if args["hitTargetType"] != "ENTITY":
            print("hit target type not entity")
            return

        playerId = args["srcId"]

        maxHealth = utils.getEntityMaxAttr(playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH)
        if maxHealth is None:
            return

        health = utils.getEntityAttr(playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH)
        if health is None:
            return

        newHealth = min(maxHealth, health + self.__repay)
        print(("repay effect", maxHealth, health, newHealth))
        utils.setEntityAttr(playerId, serverApi.GetMinecraftEnum().AttrType.HEALTH, newHealth)


class CalmEffect(BaseEffect):
    def __init__(self):
        BaseEffect.__init__(self, "calm")

    def onHit(self, bullet, module, entityId, args):
        if args["hitTargetType"] != "ENTITY":
            print("hit target type not entity")
            return

        targetId = args["targetId"]
        if targetId is None:
            return

        utils.addTimer(0.1, utils.resetAttackTarget, targetId)


class AttractEffect(BaseEffect):
    def __init__(self, entry):
        BaseEffect.__init__(self, "attract")
        self.__motion = entry.get("motion")

    def onHit(self, bullet, module, entityId, args):
        if args["hitTargetType"] != "ENTITY":
            print("hit target type not entity")
            return

        targetId = args["targetId"]
        targetPos = utils.getPos(targetId)
        if not targetPos:
            return

        playerId = args["srcId"]

        playerPos = utils.getPos(playerId)
        if not playerPos:
            return

        v = VectorUtils.minus(playerPos, targetPos)

        distance = VectorUtils.length(v)
        v = VectorUtils.normalize(v)

        if self.__motion:
            v = self.__motion(distance, v[0], v[1], v[2])

        utils.setMotion(targetId, v)
        # print("target set motion", targetId, v)


class TeleportEffect(BaseEffect):
    def __init__(self):
        BaseEffect.__init__(self, "teleport")

    def onHit(self, bullet, module, entityId, args):
        if bullet.context.teleported:
            # print("player teleported")
            return

        if args["hitTargetType"] != "BLOCK":
            # print("hit target type not block")
            return

        playerId = args["srcId"]

        originPos = args["blockPosX"], args["blockPosY"], args["blockPosZ"]
        block = utils.getBlock(playerId, originPos)
        if not block or block["name"] == "minecraft:air":
            return

        faceIndex = args["hitFace"]

        import pythonScripts.share.FaceConfig as BlockFace
        blockFace = BlockFace.Faces[faceIndex]
        if not blockFace:
            # print("block face not found", faceIndex)
            return

        newPos = VectorUtils.add(originPos, blockFace)
        newPosBlock = utils.getBlock(playerId, newPos)

        if not newPosBlock or newPosBlock["name"] == "minecraft:air":
            utils.setPos(playerId, newPos)
            bullet.context.teleported = True
