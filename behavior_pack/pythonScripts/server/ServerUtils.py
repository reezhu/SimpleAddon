# -*- coding: utf-8 -*-
# @Author  : Ree
import random

import mod.server.extraServerApi as serverApi

import pythonScripts.share.StaticConfig as config
from pythonScripts.share import MathUtils
from pythonScripts.share import StaticConfig
from pythonScripts.share import VectorUtils


def registerSystem(modName=None, systemName=None, path=None):
    # type: (str,str,str) -> MyServerSystem
    modName = modName if modName is not None else config.ServiceDomain
    systemName = systemName if systemName is not None else config.ServerSystemName
    return serverApi.RegisterSystem(modName, systemName, path)


def getSystem(modName=None, systemName=None):
    # type: (str,str) -> MyServerSystem
    modName = modName if modName is not None else config.ServiceDomain
    systemName = systemName if systemName is not None else config.ServerSystemName
    return serverApi.GetSystem(modName, systemName)


def getModule(name):
    # type: (str) -> BaseServerModule
    return getSystem().getModule(name)


def hasEntity(entityId):
    """
    检测实体是否存在，不包含死亡生物
    :param entityId:
    :param includeDeath:
    :return:
    """

    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return comp.IsEntityAlive(entityId)


def getEntityHealth(entityId):
    """
    获取当前血量
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    if comp:
        return comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)


def setEntityHealth(entityId, health=None, maxHealth=None):
    """
    设置血量
    :param entityId:
    :param health:
    :param maxHealth:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    if comp:
        if maxHealth is not None:
            comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, maxHealth)
        if health is not None:
            comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, health)


def getPos(entityId):
    """
    获取坐标
    :param entityId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
    if comp:
        return comp.GetPos()
    return None


def setPos(entityId, pos):
    """
    设置坐标
    :param entityId: 实体id
    :param pos: 要设置的坐标
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
    comp.SetPos(pos)


def getRot(entityId):
    """
    获取俯仰角和偏移角
    :param entityId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
    if comp:
        return comp.GetRot()
    return None


def setRot(entityId, rot):
    """
    设置俯仰角和偏移角
    :param entityId: 实体id
    :param rot: 要设置的角度
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
    comp.SetRot(rot)


def changeDimension(entityId, dimensionId, pos):
    """
    切换维度
    :param entityId:
    :param dimensionId:
    :param pos:
    """
    comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
    comp.ChangePlayerDimension(dimensionId, pos)


def dispatchCmd(player, command):
    """
    执行指令
    :param player:
    :param command:
    """
    comp = serverApi.GetEngineCompFactory().CreateCommand(player)
    comp.SetCommand(command, player, False)


def playSound(dimensionId, pos, sound):
    print("cmd", "playsound %s %.1f %.1f %.1f" % (sound, pos[0], pos[1], pos[2]))
    dispatchCmd(getPlayerByDimension(dimensionId), "playsound %s @a %.1f %.1f %.1f" % (sound, pos[0], pos[1], pos[2]))


def getEquipment(playerId):
    """
    获取盔甲
    :param playerId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetPlayerItem(3, 0), comp.GetPlayerItem(3, 1), comp.GetPlayerItem(3, 2), comp.GetPlayerItem(3, 3), comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)


def getArmor(playerId):
    """
    获取盔甲
    :param playerId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetPlayerItem(3, 0), comp.GetPlayerItem(3, 1), comp.GetPlayerItem(3, 2), comp.GetPlayerItem(3, 3),


def getDecorators(playerId):
    """
    获取饰品
    :param key:
    :param entityId:
    :param default:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateExtraData(playerId)
    from pythonScripts.share.DecoratorConfig import DECORATOR_SLOT_TYPE
    return [comp.GetExtraData(StaticConfig.Data.DECORATOR + str(i)) for i in range(len(DECORATOR_SLOT_TYPE))]


def setDecorator(playerId, slot, item):
    """
    设置饰品
    @param playerId:
    @param slot:
    @param item:
    @return:
    """
    return getModule(StaticConfig.Module.DecoratorMainModule).setDecorator(playerId, slot, item)


def replaceTempDecorator(playerId, slot, item):
    """
    设置临时饰品，主要用于变身，其中当原物品可移除时尝试放入背包，或者掉在地上
    @param playerId:
    @param slot:
    @param item:
    @return:
    """
    module = getModule(StaticConfig.Module.DecoratorMainModule)
    old = getDecorators(playerId)[slot]
    cfg = module.getCfg(old)
    if cfg is not None:
        canRemove = cfg.get("canRemove", True)
        if canRemove:
            remain = addItemToEmptySlot(playerId, old)
            if remain is not None:
                dropItemDict(getDimension(playerId), getPos(playerId), remain)
    return module.setDecorator(playerId, slot, item)


def findIndexOfDecoratorItem(playerId, name):
    """
    返回某个物品在装饰中的第几个
    @param playerId:
    @param name:
    @return:
    """
    for index, item in enumerate(getDecorators(playerId)):
        if item is not None and item["itemName"] == name:
            return index
    return -1


def addEffect(entityId, buff="empty", duration=5, amplifier=0, showParticles=True):
    """
    添加buff
    :param entityId:
    :param buff:
    :param duration:
    :param amplifier:
    :param showParticles:
    """
    # print "addEffect", entityId, buff, duration, amplifier, showParticles
    comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
    return comp.AddEffectToEntity(buff, duration, amplifier, showParticles)


def removeEffect(entityId, buff):
    """
    移除buff
    @param entityId:
    @param buff:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
    return comp.RemoveEffectFromEntity(buff)


def addHealth(entityId, health):
    """
    给玩家加血
    :param entityId:
    :param health:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    maxHealth = comp.GetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
    oldHealth = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
    comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, max(0, min(maxHealth, oldHealth + health)))


def getDimension(entityId):
    """
    获取玩家所在维度
    :param playerId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
    dimension = comp.GetEntityDimensionId()
    return dimension


def createExplosion(entityId, pos, radius, fire=True, breaks=True, sourceId=None, explodeId=None):
    """
    创建爆炸
    :param entityId:
    :param pos:
    :param radius:
    :param fire:
    :param breaks:
    :param sourceId:
    :param explodeId:
    """
    comp = serverApi.GetEngineCompFactory().CreateExplosion(entityId)
    return comp.CreateExplosion(pos, radius, fire, breaks, sourceId if sourceId is not None else entityId, explodeId if explodeId is not None else entityId)


def createOptimizeExplosion(entityId, dimensionId, pos, radius, damage=0, knockPower=1.0, fire=False, breaks=True):
    """
    优化后的爆炸效果
    :param entityId:
    :param dimensionId:
    :param pos:
    :param radius: 爆炸范围
    :param damage: 伤害
    :param knockPower: 击退力度
    :param fire: 是否点燃
    :param breaks: 是否破坏方块
    :return:
    """

    def getRadius(r):
        for rr in [1, 2, 3, 4, 5, 6, 7, 8, 16, 32]:
            if rr >= r:
                return rr
        return 32

    # print "createOptimizeExplosion", entityId, dimensionId, pos, radius, damage
    compG = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    comp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
    import math
    pos = tuple([int(math.ceil(x)) for x in pos])
    pos = VectorUtils.minus(pos, (1, 1, 1))
    comp.SetCommand("particle minecraft:huge_explosion_emitter %d %d %d" % pos)
    comp.SetCommand("playsound random.explode @a %d %d %d" % pos)
    if breaks:
        squareRadius = getRadius(radius)
        compG.PlaceStructure(None, (pos[0] - squareRadius, pos[1] - squareRadius, pos[2] - squareRadius), "xjcraft:explosion_r" + str(squareRadius), dimensionId)
        length = (squareRadius * 2 + 1)
        stp = int(math.floor(32768.0 / (length ** 2))) if length ** 3 >= 32768 else length
        for y in range(pos[1] - squareRadius, pos[1] + squareRadius + 1, stp):
            cmd = "fill %d %d %d %d %d %d air 0 replace barrier 0" % \
                  (pos[0] - squareRadius, MathUtils.clip(y, 0, 255), pos[2] - squareRadius,
                   pos[0] + squareRadius, MathUtils.clip(y + stp - 1, 0, 255), pos[2] + squareRadius,)
            # sendMessage(entityId, cmd)
            comp.SetCommand(cmd)
    if fire:
        distanceS = (radius + 3) ** 2
        center = VectorUtils.add(pos, (-1, -1, -1))
        for x in range(pos[0] - radius, pos[0] + radius + 1):
            for z in range(pos[2] - radius, pos[2] + radius + 1):
                if random.random() > 0.5: continue
                safe = findSafePlace(dimensionId, (x, pos[1], z), 1, minHeight=min(pos[1] - radius, 0), maxHeight=pos[1] + radius + 1)
                if safe is not None and VectorUtils.distanceSquard(safe, center) < distanceS:
                    setBlock(None, safe, "minecraft:fire", dimension=dimensionId)
                # elif safe is not None:
                #     print "safe", VectorUtils.toInt((x, pos[1], z)), VectorUtils.toInt(safe), VectorUtils.minus(pos, safe), distance(safe, center), VectorUtils.length(VectorUtils.minus(pos, safe))

    if damage > 0:
        for entity in getEntitiesAroundPos(dimensionId, pos, radius):
            if entity == entityId: continue
            attack(entityId, entity, damage, knockback=False)
            if knockPower != 0:
                tpos = getPos(entity)
                if tpos is None:
                    continue
                offset = VectorUtils.minus(tpos, pos)

                offset = VectorUtils.multiple(offset, (radius - VectorUtils.length(offset)) * knockPower / radius)
                addMotion(entity, offset)
                if getIdentifier(entity) == "minecraft:player":
                    getSystem().NotifyToClient(entity, StaticConfig.Event.BossSkillEvent, {"key": "AddMotion", "offset": offset})


def getBlock(playerId=None, pos=(0, 0, 0), dimension=-1):
    """
    获取方块
    :param playerId:
    :param pos:
    :param dimension:
    :return:
    """
    if playerId is not None:
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
    else:
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
    return comp.GetBlockNew(pos, dimension)


def setBlock(playerId, pos, name, aux=0, dimension=-1, oldBlockHandling=0):
    """
    设置方块
    :param playerId:
    :param pos:
    :param name:
    :param aux:
    """
    blockDict = {
        'name': name,
        'aux': aux
    }
    if playerId is not None:
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)  # 此处playerId为block的设置者
        return comp.SetBlockNew(pos, blockDict, oldBlockHandling=oldBlockHandling)
    else:
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
        return comp.SetBlockNew(pos, blockDict, oldBlockHandling=oldBlockHandling, dimensionId=dimension)


def breakBlock(playerId, pos):
    """
    设置方块
    :param playerId:
    :param pos:
    :param name:
    :param aux:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)  # 此处playerId为block的设置者
    return comp.PlayerDestoryBlock(pos)


def getExtraData(key, entityId=None, default=None):
    """
    获取生物额外数据
    :param key:
    :param entityId:
    :param default:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateExtraData(serverApi.GetLevelId() if entityId is None else entityId)
    res = comp.GetExtraData(key)
    return res if res is not None else default


def setExtraData(key, object, entityId=None):
    """
    设置生物额外数据
    :param key:
    :param object:
    :param entityId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateExtraData(serverApi.GetLevelId() if entityId is None else entityId)
    return comp.SetExtraData(key, object)


def getIdentifier(entityId):
    """
    获取唯一id
    :param entityId:
    :return:
    """
    try:
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        return comp.GetEntityIdentifier(entityId)
    except Exception as e:
        comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
        return comp.GetEngineTypeStr()


def sendTip(playerId, text):
    """
    发送提示
    :param playerId:
    :param text:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
    comp.SetOneTipMessage(playerId, text)


def addExp(playerId, count):
    """
    添加经验
    :param playerId:
    :param count:
    """
    comp = serverApi.GetEngineCompFactory().CreateExp(playerId)
    comp.AddPlayerExperience(int(count))


def getPlayerLevel(playerId):
    """
    获取玩家等级
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
    return comp.GetPlayerLevel()


def changePlayerLevel(playerId, count):
    """
    修改玩家等级
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
    return comp.AddPlayerLevel(count)


def dropBlockResources(block, pos, aux=0, bonusLootLevel=0):
    """
    生成某个方块的掉落物
    :param block:
    :param pos:
    :param aux:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
    return comp.SpawnResources(block, pos, aux, bonusLootLevel=bonusLootLevel)


def dropItem(dimension, pos, name, count=1, aux=0, enchant=[], customTips="", showInHand=True):
    """
    在世界上生成掉落物
    @param dimension:
    @param pos:
    @param name:
    @param count:
    @param aux:
    @param enchant:
    @param customTips:
    """
    itemDict = {
        'itemName': name,
        'count': count,
        'enchantData': enchant,
        'auxValue': aux,
        'showInHand': showInHand,

    }
    if enchant is not None and len(enchant) > 0:
        itemDict['customTips'] = customTips,
    dropItemDict(dimension, pos, itemDict)


def dropItemDict(dimension, pos, itemDict):
    """
    在世界上生成掉落物
    @param dimension:
    @param pos:
    @param itemDict:
    """
    # print "drop item@", dimension, pos, itemDict
    if itemDict is None: return
    return getSystem().CreateEngineItemEntity(itemDict, dimension, pos)
    # comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    # comp.SpawnItemToLevel(itemDict, dimension, pos)


def getBlockEntityData(dimensionId, pos):
    """
    获取方块的生物数据
    @param dimensionId:
    @param pos:
    @return:
    """
    blockEntitycomp = serverApi.GetEngineCompFactory().CreateBlockEntityData(serverApi.GetLevelId())
    entityData = blockEntitycomp.GetBlockEntityData(dimensionId, pos)
    return entityData


def getOffsetBlockPos(pos, face):
    """
    根据朝向获取方块面所对的位置
    :param pos:
    :param face:
    :return:
    """
    x, y, z = pos
    if face == 0:
        y -= 1
    elif face == 1:
        y += 1
    elif face == 2:
        z -= 1
    elif face == 3:
        z += 1
    elif face == 4:
        x -= 1
    elif face == 5:
        x += 1
    return x, y, z


def setItemInHand(playerId, itemDict):
    """
    设置手持物品
    :param playerId:
    :param itemDict:
    """
    itemDict = {'count': 0, 'itemName': 'minecraft:air', 'auxValue': 0} if itemDict is None else itemDict
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    comp.SpawnItemToPlayerCarried(itemDict, playerId)


def getItemInHandSlot(playerId):
    """
    获取手持物品的槽位
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetSelectSlotId()


def getItemInHand(playerId, getUserData=False):
    """
    获取手持物品
    :param playerId:
    :return:
    @param getUserData:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0, getUserData=getUserData)


def getItemInOffHand(playerId, getUserData=False):
    """
    获取副手物品
    :param playerId:
    :return:
    @param getUserData:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.OFFHAND, 0, getUserData=getUserData)


def getBiomeName(playerId, pos):
    """
    获取位置所在群系名称
    :param playerId:
    :param pos:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBiome(playerId)
    return comp.GetBiomeName(pos)


def GetBlockEntityData(dimensionId, pos):
    """
    获取方块实体数据
    :param dimensionId:
    :param pos:
    :return:
    """
    blockEntitycomp = serverApi.GetEngineCompFactory().CreateBlockEntityData(serverApi.GetLevelId())
    return blockEntitycomp.GetBlockEntityData(dimensionId, pos)


def isSneaking(playerId):
    """
    玩家是否在潜行
    :param playerId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.isSneaking()


def getMaxStackSize(item):
    """
    获取最大堆叠上限
    @param item:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    info = comp.GetItemBasicInfo(item)
    return None if info is None else info["maxStackSize"]


def getMaxDurability(item):
    """
    获取最大耐久度
    @param item:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    info = comp.GetItemBasicInfo(item)
    return None if info is None else info["maxDurability"]


def getChestSize(dimension, pos):
    """
    获取箱子大小
    @param dimension:
    @param pos:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateChestBlock(serverApi.GetLevelId())
    return comp.GetChestBoxSize(None, pos, dimension)


def getBlockInventory(dimension, pos, size, userData=True):
    """
    获取方块容器内容
    @param dimension:
    @param pos:
    @param size:
    @param userData:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    return [comp.GetContainerItem(pos, i, dimension, getUserData=userData) for i in range(size)]


def setBlockInventory(dimension, pos, slot, itemDict):
    """
    设置方块容器内容
    @param dimension:
    @param pos:
    @param slot:
    @param itemDict:
    """
    if itemDict is None or itemDict["count"] == 0:
        # 由于SpawnItemToChestBlock在设置数量为0的物品时会令客户端无法放东西近期，None的物品时直接报错，因此采用这种方式实现设置为空气
        x, y, z = pos
        comp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        comp.SetCommand("replaceitem block %d %d %d slot.container %d air" % (x, y, z, slot))
    else:
        comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
        comp.SpawnItemToChestBlock(itemDict, None, slot, pos, dimension)


def removeItem(playerId, item, ignoreAux=False, ignoreRest=False):
    """
    从玩家背包中移除某些物品
    @param playerId:
    @param item:
    @param ignoreAux:
    @param ignoreRest:
    @return:
    """
    if item is None: return False
    contents = getInventoryContents(playerId, True)
    total = item["count"]
    for index, content in enumerate(contents):
        if isSameItem(item, content, ignoreCount=True, ignoreAux=ignoreAux, ignoreRest=ignoreRest):
            remove = min(total, content["count"])
            total -= remove
            if remove == content["count"]:
                setInventorySlot(playerId, index, None)
            else:
                content["count"] -= remove
                setInventorySlot(playerId, index, content)
            if total <= 0:
                return 0
    return total


def hasItem(playerId, item, ignoreAux=False, ignoreRest=False):
    """
    玩家是否有足够的某物品
    @param playerId:
    @param item:
    @param ignoreAux:
    @param ignoreRest:
    @return:
    """
    if item is None: return False
    contents = getInventoryContents(playerId, True)
    total = 0
    for content in contents:
        if isSameItem(item, content, ignoreCount=True, ignoreAux=ignoreAux, ignoreRest=ignoreRest):
            total += content["count"]
            if total >= item["count"]:
                return True
    return False


def getTargetItemAmount(playerId, item, ignoreAux=False, ignoreRest=False):
    """
    取得玩家目標物品數量
    @param playerId:
    @param item:
    @param ignoreAux:
    @param ignoreRest:
    @return:
    """
    if item is None: return False
    contents = getInventoryContents(playerId, True)
    total = 0
    for content in contents:
        if isSameItem(item, content, ignoreCount=True, ignoreAux=ignoreAux, ignoreRest=ignoreRest):
            total += content["count"]

    return total


def isSameItem(item1, item2, ignoreCount=False, ignoreAux=False, ignoreRest=False):
    """
    判断两个物品是否相等，变量用来忽略数量、子id与其他参数
    @rtype: object
    """
    if item1 == item2:
        return True
    if item1 is None or item2 is None:
        return False
    if item1.get("itemName") == item2.get("itemName"):
        if ignoreCount or item1.get("count") == item2.get("count"):
            if ignoreAux or item1.get("auxValue") == item2.get("auxValue"):
                if ignoreRest:
                    return True
                else:
                    keys = set(dict(item1).keys())
                    keys.union(list(item2.keys()))
                    keys.remove("count")
                    keys.remove("auxValue")
                    keys.remove("itemName")
                    for k in keys:
                        if k not in item1 or k not in item2 or item1[k] != item2[k]:
                            return False
                    return True
    return False


def hasEmptySlot(playerId):
    """
    查询玩家背包中是否有空位
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    for slot in range(36):
        if comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot) is None:
            return True
    return False


def addItemToEmptySlotWithIdentifier(playerId, name, count=1, auxValue=None):
    """
    添加物品至玩家背包，会自动合并与返回放不下的物品,只判断名字和子id（可选）
    @param playerId:
    @param name:
    @param count:
    @param auxValue:
    @return:
    """
    return addItemToEmptySlot(playerId, {"itemName": name, "auxValue": 0, "count": count}, ignoreAux=auxValue is None, ignoreRest=True)


def addItemToEmptySlot(playerId, itemToAdd, ignoreAux=False, ignoreRest=False):
    """
    添加物品至玩家背包，会自动合并与返回放不下的物品
    @param playerId:
    @param itemToAdd:
    @param ignoreAux:
    @param ignoreRest:
    @return:
    """
    if itemToAdd is None or itemToAdd["count"] == 0:
        return None
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    items = [comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot, getUserData=True) for slot in range(36)]
    info = comp.GetItemBasicInfo(itemToAdd["itemName"])
    maxStackSize = info["maxStackSize"]
    count = itemToAdd["count"]
    for slot, item in enumerate(items):
        if maxStackSize > 1 and isSameItem(item, itemToAdd, ignoreCount=True, ignoreAux=ignoreAux, ignoreRest=ignoreRest):
            transaction = min(maxStackSize - item["count"], count)
            if transaction > 0:
                item["count"] += transaction
                comp.SpawnItemToPlayerInv(item, playerId, slot)
                count -= transaction
                if count == 0:
                    return None
    for slot, item in enumerate(items):
        if item is None:
            transaction = min(maxStackSize, count)
            if transaction > 0:
                import copy
                item = copy.deepcopy(itemToAdd)
                item["count"] = transaction
                comp.SpawnItemToPlayerInv(item, playerId, slot)
                count -= transaction
                if count == 0:
                    return None
    return itemToAdd if count != 0 else None


def getInventoryContents(playerId, nbt=False):
    # type: (str,bool) -> list
    """
    获取玩家背包所有物品
    :param nbt:
    :param playerId:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return [comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot, getUserData=nbt) for slot in range(36)]


def getInventorySlot(playerId, slot, nbt=False):
    """
    获取玩家背包中某个格子的物品
    :param playerId:
    :param slot:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, slot, getUserData=nbt)


def setInventorySlot(playerId, slot, itemDict):
    """
    设置玩家背包中某个格子的物品
    :param playerId:
    :param slot:
    :param itemDict:
    """
    itemDict = {'count': 0, 'itemName': 'minecraft:air', 'auxValue': 0} if itemDict is None else itemDict
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    comp.SpawnItemToPlayerInv(itemDict, playerId, slot)


def spawnItemToPlayerInv(playerId, itemDict, slotPos=None):
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)

    if slotPos is not None:
        return comp.SpawnItemToPlayerInv(itemDict, playerId, slotPos)
    else:
        return comp.SpawnItemToPlayerInv(itemDict, playerId)


def setItem(playerId, pos, slot, itemDict):
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    if pos == serverApi.GetMinecraftEnum().ItemPosType.INVENTORY:
        itemDict = {'count': 0, 'itemName': 'minecraft:air', 'auxValue': 0} if itemDict is None else itemDict
        comp.SpawnItemToPlayerInv(itemDict, playerId, slot)
    elif pos == serverApi.GetMinecraftEnum().ItemPosType.OFFHAND:
        itemDict = {'count': 0, 'itemName': 'minecraft:air', 'auxValue': 0} if itemDict is None else itemDict
        comp.SpawnItemToPlayerOffHand(itemDict, playerId)
    elif pos == serverApi.GetMinecraftEnum().ItemPosType.ARMOR:
        if itemDict is None:
            comp.SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.ARMOR, None, slot)
        else:
            comp.SpawnItemToArmor(itemDict, playerId, slot)


def addItem(playerId, item):
    """
    给玩家物品
    :param playerId:
    :param item:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.SpawnItemToPlayerInv(item, playerId)


def getTime():
    """
    获取游戏时间（注意游戏时间永远不会后退）
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateTime(serverApi.GetLevelId())
    return comp.GetTime()


def getDay():
    """
    获取游戏日
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateTime(serverApi.GetLevelId())
    return comp.GetTime() / 24000


def setAttr(entityId, attrType, maxValue=None, currentValue=None):
    """
    设置生物属性
    :param entityId:
    :param attrType:
    :param maxValue:
    :param currentValue:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    if maxValue is not None:
        comp.SetAttrMaxValue(attrType, maxValue)
    if currentValue is not None:
        comp.SetAttrValue(attrType, currentValue)


def attack(srcId, targetId, damage, ignoreArmor=False, knockback=True):
    """
    造成伤害
    :param srcId:
    :param targetId:
    :param damage:
    :param ignoreArmor:
    :param knockback:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateHurt(targetId)
    return comp.SetHurtByEntity(srcId, damage, ignoreArmor, knockback)


def shootProjectile(playerId, identifier, param):
    """
    发射抛射物
    @param playerId:
    @param identifier:
    @param param:
    """
    comp = serverApi.GetEngineCompFactory().CreateProjectile(serverApi.GetLevelId())
    return comp.CreateProjectileEntity(playerId, identifier, param)


def getMotion(entityId):
    """
    获取生物速度
    :param entityId:
    :return:
    """
    motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
    return motionComp.GetMotion()


def setMotion(entityId, motion):
    """
    设置生物速度
    :param entityId:
    :return:
    """
    motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
    return motionComp.SetMotion(motion)


def addMotion(entityId, motion):
    """
    加成生物速度
    :param entityId:
    :return:
    """
    motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
    motion = VectorUtils.add(motionComp.GetMotion(), motion)
    return motionComp.SetMotion(motion)


def findPickingEntity(playerId, checkRange=10, pickRange=3.0):
    # type: (str, int, float) -> str
    """
    根据玩家朝向查找靠近光标的生物，注意查找范围过大可能会影响性能
    @param playerId:
    @param checkRange: 查找范围
    @param pickRange: 只返回距离视线小于此距离的生物
    @return:
    """
    pos = getPos(playerId)
    face = VectorUtils.angle2vector(getRot(playerId))
    target = None
    radius = 0
    for entity in getEntitiesAround(playerId, radius=checkRange):
        if entity == playerId: continue
        distance = VectorUtils.distanceToLine(pos, face, getPos(entity))
        if distance < pickRange:
            if target is None or distance < radius:
                target = entity
                radius = distance
    return target


def getEntitiesAround(entityId, radius=10, filters={"test": "is_family", "subject": "other", "operator": "not", "value": "drop_item"}):
    """
    获取实体周围实体
    :param entityId: 中心生物id
    :param radius: 范围
    :param filters: 过滤器
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
    return comp.GetEntitiesAround(entityId, radius, filters)


def getEntitiesAroundPos(dimensionId, pos, radius=5):
    """
    获取坐标周围实体
    :param entityId: 中心生物id
    :param radius: 范围
    :param filters: 过滤器
    :return:
    """
    x, y, z = pos
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return comp.GetEntitiesInSquareArea(None, (x - radius, y - radius, z - radius), (x + radius, y + radius, z + radius), dimensionId)


def setFbxModel(entityId, modelName, texture=None):
    """
    设置fbx模型
    :param entityId:
    :param modelName:
    :param texture:
    """
    # print "setFBXModel", entityId, modelName, texture
    modelComp = serverApi.GetEngineCompFactory().CreateModel(entityId)
    modelComp.SetModel(modelName)
    if texture is None:
        modelComp.SetUsingModelSkin()
    else:
        modelComp.SetModelTexture(str(texture))


def setAiEnable(entityId, enable):
    """
    启用或禁用ai
    :param entityId:
    :param enable:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
    return comp.SetBlockControlAi(enable)  # 产品命名为block但是其实是设置启用


def triggerCustomEvent(entityId, event):
    """
    触发生物自定义事件
    @param entityId:
    @param event:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateEntityEvent(entityId)
    return comp.TriggerCustomEvent(entityId, event)


def getEntityMaxAttr(entityId, type):
    # type: (str, int) -> float
    """
    获取实体最大属性
    @param entityId:
    @param type: serverApi.GetMinecraftEnum().AttrType
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.GetAttrMaxValue(type)


def getEntityAttr(entityId, type):
    # type: (str, int) -> float
    """
    获取实体当前属性
    @param entityId:
    @param type: serverApi.GetMinecraftEnum().AttrType
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.GetAttrValue(type)


def setEntityAttr(entityId, type, value):
    # type: (str, int,int) -> float
    """
    设置实体当前属性
    @param entityId:
    @param type: serverApi.GetMinecraftEnum().AttrType
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.SetAttrValue(type, value)


def setEntityMaxAttr(entityId, type, value):
    # type: (str, int,int) -> float
    """
    设置实体当前最大属性
    @param entityId:
    @param type: serverApi.GetMinecraftEnum().AttrType
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.SetAttrMaxValue(type, value)


def spawnLootWithEntityId(pos, entityId, playerId, damageEntity=None):
    """
    生成一次掉落
    @param pos:
    @param entityId:
    @param playerId:
    @param damageEntity:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateActorLoot(playerId)
    return comp.SpawnLootTableWithActor(pos, entityId, playerKillerId=playerId, damageCauseEntityId=damageEntity if damageEntity is not None else playerId)


def spawnLootWithIdentifier(pos, identifier, playerId, damageEntity=None):
    """
    生成一次掉落
    @param pos:
    @param entityId:
    @param playerId:
    @param damageEntity:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateActorLoot(playerId)
    return comp.SpawnLootTable(pos, identifier, playerKillerId=playerId, damageCauseEntityId=damageEntity if damageEntity is not None else playerId)


def setFireTick(entityId, tick):
    """
    设置着火时间
    @param entityId:
    @param tick:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.SetEntityOnFire(tick)


def getAllEffects(entityId):
    """
    获取所有药水效果
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
    return comp.GetAllEffects()


def getInvItemDurability(playerId, slotId):
    """
    获取物品耐久
    @param playerId:
    @param slotId: 背包内的格子
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetInvItemDurability(slotId)


def setInvItemDurability(playerId, slotId, newDurability):
    """
    设置物品耐久
    @param playerId:
    @param slotId: 背包内的格子
    @param newDurability:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    comp.SetInvItemDurability(slotId, newDurability)


def getArmorDurability(playerId, slotId):
    """
    获取装备中盔甲的耐久
    @param playerId:
    @param slotId: 盔甲槽位
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetEquItemDurability(slotId)


def setArmorDurability(playerId, slotId, newDurability):
    """
    设置盔甲耐久
    @param playerId:
    @param slotId: 盔甲槽位
    @param newDurability:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    comp.SetEquItemDurability(slotId, newDurability)


def changePlayerItemTipsAndExtraId(playerId, posType, slotPos, customTips, extraId):
    """
    设置玩家物品tip和extraId
    @param playerId:
    @param posType:
    @param slotPos:
    @param customTips:
    @param extraId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.ChangePlayerItemTipsAndExtraId(posType, slotPos, customTips, extraId)


def createEngineEntityByTypeStr(engineTypeStr, pos, rot, dimension, isNpc=False):
    """
    使用identifier创建生物
    @param engineTypeStr:
    @param pos:
    @param rot:
    @param dimension:
    @param isNpc:
    @return:
    """
    return getSystem().CreateEngineEntityByTypeStr(engineTypeStr, pos, rot, dimension, isNpc)


def sendMessage(playerId, msg):
    """
    发送聊天栏消息
    @param playerId:
    @param msg:
    """
    comp = serverApi.GetEngineCompFactory().CreateMsg(playerId)
    comp.NotifyOneMessage(playerId, msg)


def getAttackTarget(entityId):
    """
    获取ai目标
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
    return comp.GetAttackTarget()


def addRepeatedTimer(delay, func, *args, **kwargs):
    """
    添加产品循环计时器
    @param delay:
    @param func:
    @param args:
    @param kwargs:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    if not kwargs and not args:
        return comp.AddRepeatedTimer(delay, func)
    elif not kwargs:
        return comp.AddRepeatedTimer(delay, func, *args)
    else:
        return comp.AddRepeatedTimer(delay, func, *args, **kwargs)


def addTimer(delay, func, *args, **kwargs):
    """
    添加产品计时器
    @param delay:
    @param func:
    @param args:
    @param kwargs:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    if not kwargs and not args:
        return comp.AddTimer(delay, func)
    elif not kwargs:
        return comp.AddTimer(delay, func, *args)
    else:
        return comp.AddTimer(delay, func, *args, **kwargs)


def cancelTimer(timer):
    """
    取消计时器
    @param timer:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    comp.CancelTimer(timer)


def getPlayerHunger(playerId):
    """
    获取玩家饱食度
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.GetPlayerHunger()


def setPlayerHunger(playerId, hungerlevel):
    """
    设置玩家饱和度
    @param playerId:
    @param hungerlevel:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.SetPlayerHunger(hungerlevel)


def getDifficulty(playerId):
    """
    获取游戏难度
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
    return comp.GetGameDiffculty()


def getCollisionBoxSize(entityId):
    """
    获取碰撞箱大小
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateCollisionBox(entityId)
    return comp.GetSize()


def getAuxValue(entityId):
    """
    获取实体附加值
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAuxValue(entityId)
    return comp.GetAuxValue()


def removeEntity(entityId):
    """
    移除生物（不会有死亡动画）
    @param entityId:
    @return:
    """
    return getSystem().DestroyEntity(entityId)


def killEntity(entityId):
    """
    杀死生物
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return comp.KillEntity(entityId)


def getEntitiesSquareArea(entityId, startPos, endPos):
    """
    获取方块范围内的生物
    @param entityId:
    @param startPos:
    @param endPos:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
    return comp.GetEntitiesInSquareArea(entityId, startPos, endPos)


def setMoveSetting(entityId, targetPos, speed, callback):
    """
    设置寻路
    @param entityId:
    @param targetPos:
    @param speed:
    @param callback:
    """
    comp = serverApi.GetEngineCompFactory().CreateMoveTo(entityId)
    comp.SetMoveSetting(targetPos, speed, 200, callback)


def getGamemode(playerId):
    """
    获取玩家的游戏模式
    @param playerId:
    @return:
    """
    gameComp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return gameComp.GetPlayerGameType(playerId)


def getEntitiesAroundByType(entityId, radius, type):
    """
    获取附近某个identifier的生物
    @param entityId:
    @param radius:
    @param type:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return comp.GetEntitiesAroundByType(entityId, radius, type)


def setBlockControlAi(entityId, block):
    """
    禁用ai
    @param entityId:
    @param block:
    """
    contServer = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
    contServer.SetBlockControlAi(block)


def getTopBlockData(playerId, pos):
    """
    获取最高层方块数据
    @param playerId:
    @param pos:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
    return comp.GetTopBlockData(pos)


def getTopBlockHeight(pos):
    """
    获取最高层方块高度
    @param pos:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
    return comp.GetTopBlockHeight(pos)


def getOnlinePlayers():
    """
    获取在线玩家列表
    @return:
    """
    return serverApi.GetPlayerList()


def checkFilter(entityId, filter={"test": "is_family", "subject": "other", "value": "player"}):
    """
    检查实体是否满足filter
    @param entityId:
    @param filter:
    @return:
    """
    res = entityId in getEntitiesAround(entityId, 1, filter)
    return res


def getPlayerByDimension(dimension):
    for player in getOnlinePlayers():
        if dimension == getDimension(player):
            return player

    return None


def addNeteaseFeatureWhiteList(name):
    comp = serverApi.GetEngineCompFactory().CreateFeature(serverApi.GetLevelId())
    # 注意structureName格式为floderName:structureName
    return comp.AddNeteaseFeatureWhiteList(name)


def getSelectSlotId(playerId):
    """
    获取当前玩家选中的slotId
    @param playerId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.GetSelectSlotId()


def setEntityTamed(playerId, tameId, tameEvent='minecraft:on_tame'):
    """
    设置entity被驯服，需要在entity的定义文件中有tameable组件
    @param playerId:
    @param tameId:
    @param tameEvent: 驯服entity后需要触发的事件
    """
    tameComp = serverApi.GetEngineCompFactory().CreateTame(tameId)
    tameComp.SetEntityTamed(playerId, tameId)
    envComp = serverApi.GetEngineCompFactory().CreateEntityEvent(tameId)
    envComp.TriggerCustomEvent(tameId, tameEvent)


def getWholeExtraData(entityId=None):
    """
    获取所有的extra data
    @param entityId: 指定entityId则获得改entity的所有extra data，否则获得level的所有extra data
    @return:
    """
    if entityId is None:
        comp = serverApi.GetEngineCompFactory().CreateExtraData(serverApi.GetLevelId())
        return comp.GetWholeExtraData()
    else:
        comp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
        return comp.GetWholeExtraData()


def clearExtraDataByRegex(entityId=None, regex=".*"):
    """
    使用正则来清空生物的extra data
    @param entityId:
    @param regex:
    """
    import re
    comp = serverApi.GetEngineCompFactory().CreateExtraData(entityId if entityId is not None else serverApi.GetLevelId())
    dataDict = comp.GetWholeExtraData()
    count = 0
    if dataDict:
        for key in list(dataDict.keys()):
            if re.match(regex, key):
                comp.CleanExtraData(key)
                count += 1
    return count


def getOwnerId(entityId):
    """
    获取entity的主人的id
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateTame(entityId)
    return comp.GetOwnerId()


def getFootPos(entityId):
    """
    获取entity的脚底坐标
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
    return comp.GetFootPos()


def setName(entityId, name):
    """
    设置entity的name tag
    @param entityId:
    @param name:
    """
    comp = serverApi.GetEngineCompFactory().CreateName(entityId)
    comp.SetName(name)


def getName(entityId):
    """
    获取entity的name tag
    也可以用来获取玩家的名字
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateName(entityId)
    return comp.GetName()


def getEntityItem(entityId, posType, slotType):
    """
    获取entity所持有的道具
    @param entityId:
    @param posType:
    @param slotType:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
    return comp.GetEntityItem(posType, slotType)


def setEntityItem(entityId, posType, itemDict, slotPos=None):
    """
    设置entity所持有的道具
    @param entityId:
    @param posType:
    @param itemDict:
    @param slotPos: 容器槽位，如果ItemPosType为左右手可不传
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
    return comp.SetEntityItem(posType, itemDict, slotPos)


def getItemBasicInfo(itemName, auxValue=0):
    """
    获取该类型物品的信息，包括堆叠上限等
    @param itemName:
    @param auxValue:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    return comp.GetItemBasicInfo(itemName, auxValue)


def getItemMaxStackSize(itemName, auxValue=0):
    """
    获取物品的堆叠上限
    @param itemName:
    @param auxValue:
    @return:
    """
    basicInfo = getItemBasicInfo(itemName, auxValue)
    if basicInfo:
        return basicInfo["maxStackSize"]
    else:
        return None


def mergeItemDict(source, target):
    """
    将source item dict中的物品合并到target item dict中。如果两个item dict类型不同则无事发生。
    会检测物品的堆叠上限
    @param source:
    @param target:
    @return:
    """
    if source["itemName"] != target["itemName"] or source["auxValue"] != target["auxValue"]:
        return

    basicInfo = getItemBasicInfo(source["itemName"], source["auxValue"])
    if not basicInfo:
        return

    maxStackSize = basicInfo["maxStackSize"]
    leftRoom = maxStackSize - target["count"]

    if leftRoom >= source["count"]:
        target["count"] += source["count"]
        source["count"] = 0
    else:
        target["count"] = maxStackSize
        source["count"] -= leftRoom


def checkEntityComponent(entityId, operator, component):
    """
    检测entity是否拥有某种component
    @param entityId:
    @param operator:
    @param component:
    @return:
    """
    entities = getEntitiesAround(entityId, 1, {
        "all_of": [
            {
                "test": "has_component",
                "subject": "other",
                "operator": operator,
                "value": component
            }
        ]
    })

    return entityId in entities


def spawnItemToContainer(itemDict, slotPos, blockPos, dimensionId):
    """
    在容器（箱子等）中生成道具
    @param itemDict:
    @param slotPos:
    @param blockPos:
    @param dimensionId:
    @return:
    """
    playerList = serverApi.GetPlayerList()
    if not playerList:
        return False

    comp = serverApi.GetEngineCompFactory().CreateItem(playerList[0])
    return comp.SpawnItemToContainer(itemDict, slotPos, blockPos, dimensionId)


def getContainerItem(blockPos, slotPos, dimensionId):
    """
    获取容器（箱子等）中的道具
    @param blockPos:
    @param slotPos:
    @param dimensionId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    return comp.GetContainerItem(blockPos, slotPos, dimensionId)


def getContainerSize(pos, dimensionId):
    """
    获取容器（箱子等）的大小
    @param pos:
    @param dimensionId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
    return comp.GetContainerSize(pos, dimensionId)


def getEntityRider(entityId):
    """
    获取entity的直接骑乘对象
    @param entityId:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
    return comp.GetEntityRider()


def createPlainItemDict(itemName, count=1, auxValue=0):
    """
    创建普通的item dict
    @param itemName:
    @param count:
    @param auxValue:
    @return:
    """
    return {
        'itemName': itemName,
        'count': count,
        'auxValue': auxValue,
    }


def setInventoryItemNum(playerId, slotId, num):
    """
    设置背包中的道具数量
    @param playerId:
    @param slotId:
    @param num:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    return comp.SetInvItemNum(slotId, num)


def checkEntityFilter(entityId, filter):
    """
    检测entity是否满足filter的条件
    @param entityId:
    @param filter:
    @return:
    """
    entities = getEntitiesAround(entityId, 1, filter)
    return entityId in entities


def resetAttackTarget(entityId):
    """
    清除仇恨目标
    @param entityId:
    @return: 设置结果
    """
    comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
    return comp.ResetAttackTarget()


def applyPlaceHolder(playerId, text):
    """
    替换占位符
    :param playerId:
    :param text:
    :return:
    """
    from pythonScripts.share import StaticConfig
    module = getModule(StaticConfig.Module.PlaceHolder)
    if not module:
        return ""
    return module.compile(playerId, text)


def getSmeltingRecipe(item):
    """
    获取一个物品的熔炼结果
    @param item:
    @return:
    """
    if item is None: return None
    from pythonScripts.share import StaticConfig
    smelting = getSystem().getData(StaticConfig.Data.RECIPE_SMELTING)
    res = smelting.get((item["itemName"], item["auxValue"]), smelting.get(item["itemName"]))
    if res is None: return None
    if type(res) == tuple:
        return {"itemName": res[0], "auxValue": res[1], "count": 1}
    elif type(res) == str:
        return {"itemName": res, "auxValue": 0, "count": 1}
    else:
        return None


def registerRecipe(json):
    """
    注册配方，重启失效
    :param json: 配方的原版json配置
    """
    serverApi.GetEngineCompFactory().CreateRecipe(serverApi.GetLevelId()).RegisterRecipe(json)


def isWordValid(word):
    """
    敏感词校验
    :param word:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    return comp.CheckWordsValid(word)


def addBlockListener(block):
    """
    添加方块监听，添加后才可以使用ServerBlockUseEvent监听
    :param word:
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(serverApi.GetLevelId())
    return comp.AddBlockItemListenForUseEvent(block)


def placeStructure(pos, structureName, playerId=None, dimension=-1):
    """
    放置结构
    @param pos:
    @param structureName:
    @param playerId:
    @param dimension:
    """
    comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
    comp.PlaceStructure(playerId, pos, structureName, dimension)


def setGravity(entityId, gravity):
    """
    设置重力
    @param entityId:
    @param gravity:
    """
    comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
    comp.SetGravity(gravity)


def getGravity(entityId):
    """
    获取重力
    @param entityId:
    @param gravity:
    """
    comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
    comp.GetGravity()


def knock(entityId, motion, speed):
    """
    击退生物
    @param entityId: 被击退生物
    @param motion: 向量方向
    @param speed: 速度
    """
    motion = VectorUtils.normalize(motion)
    x, y, z = motion
    height = speed * VectorUtils.dot((0, 1, 0), motion)
    vector = VectorUtils.normalize((x, 0, z))
    power = speed * VectorUtils.dot(vector, motion)
    comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
    comp.SetMobKnockback(x, z, power, height, height * 2)


def randomTeleport(entityId, radius, height=2, attempt=2, ignoreBlocks={"minecraft:water"}):
    """
    寻找随机传送安全位置
    :param entityId:
    :param radius: 随机范围
    :param height: 安全高度
    :param attempt: 尝试次数
    :param ignoreBlocks: 当空间包含这些方块时当作失败
    :return:
    """
    entityPos = getPos(entityId)
    for _ in range(0, attempt):
        basePos = (random.uniform(entityPos[0] - radius, entityPos[0] + radius), entityPos[1], random.uniform(entityPos[2] - radius, entityPos[2] + radius))
        outputPos = findSafePlace(getDimension(entityId), basePos, height, ignoreBlocks)
        if outputPos: return outputPos
    return None


def findSafePlace(dimensionId, pos, height, ignoreBlocks={"minecraft:water"}, minHeight=0, maxHeight=255):
    """
    查找某个位置的安全位置
    :param dimensionId: 坐标维度
    :param pos: 初始坐标
    :param height: 需要上面有多少空间
    :param ignoreBlocks: 当空间包含这些方块时当作失败
    :param minHeight: 最低高度
    :param maxHeight: 最高高度
    :return:
    """
    comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())

    def _getBlockName(bd, bp):
        return comp.GetBlockNew(bp, bd).get("name", "")

    def _isUpperBlockSatisfied(sd, sp, upHeight):
        for i in range(1, upHeight + 1):
            if _getBlockName(bp=(sp[0], sp[1] + i, sp[2]), bd=sd) == "minecraft:air":
                continue
            else:
                return False, (sp[0], sp[1] + i, sp[2])

        return True, (sp[0], sp[1] + 1, sp[2])

    while pos[1] <= maxHeight and pos[1] >= minHeight:
        if _getBlockName(dimensionId, pos) in ignoreBlocks:
            return None
        if _getBlockName(dimensionId, pos) == "minecraft:air":
            pos = (pos[0], pos[1] - 1, pos[2])
            continue

        elif _isUpperBlockSatisfied(dimensionId, pos, 1)[0]:
            upperBlockSatisfied = _isUpperBlockSatisfied(dimensionId, pos, height)
            if upperBlockSatisfied[0]:
                return upperBlockSatisfied[1]
            else:
                pos = upperBlockSatisfied[1]

        else:
            pos = (pos[0], pos[1] + 1, pos[2])
            continue
    return None


def getEntityFamily(entityId):
    """
    获取生物行为包的type_family字段
    @param entityId:
    @return: list(str)，type_family列表，例['cow', 'mob']
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
    return comp.GetTypeFamily()


def setStepHeight(playerId, height):
    # type: (str, float) -> bool
    """
    设置可以走上台阶的高度
    @param playerId:
    @param height:
    @return:
    """
    comp = serverApi.GetEngineCompFactory().CreateAttr(playerId)
    if height > 0:
        return comp.SetStepHeight(height)
    else:
        return comp.ResetStepHeight()
