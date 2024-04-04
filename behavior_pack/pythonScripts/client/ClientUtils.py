# -*- coding: utf-8 -*-
# @Author  : Ree
import math
import mod.client.extraClientApi as clientApi

import pythonScripts.share.StaticConfig as config


def registerSystem(modName=None, systemName=None, path=None):
    # type: (str,str,str) -> MyClientSystem
    modName = modName if modName is not None else config.ServiceDomain
    systemName = systemName if systemName is not None else config.ClientSystemName
    return clientApi.RegisterSystem(modName, systemName, path)


def getSystem(modName=None, systemName=None):
    # type: (str,str) -> MyClientSystem
    modName = modName if modName is not None else config.ServiceDomain
    systemName = systemName if systemName is not None else config.ClientSystemName
    return clientApi.GetSystem(modName, systemName)


def getModule(name):
    # type: (str) -> BaseClientModule
    return getSystem().getModule(name)


def hasEntity(entityId, includeDeath=False):
    """
    检测实体是否存在
    :param entityId:
    :param includeDeath:
    :return:
    """
    if includeDeath:
        comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
        return comp.HasEntity(entityId) > 0
    else:
        comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
        return comp.IsEntityAlive(entityId)


lastPerspective = None


def setPerspective(lock):
    """
    锁定视角
    @param lock:
    """
    global lastPerspective
    # print "set perspect", lock
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "playerView")
    if lastPerspective is None:
        lastPerspective = comp.GetPerspective()
    comp.SetPerspective(lock)
    comp.LockPerspective(lock)


def releasePerspective():
    """
    释放视角并回到原视角
    """
    global lastPerspective
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "playerView")
    comp.LockPerspective(-1)
    if lastPerspective is not None:
        comp.SetPerspective(lastPerspective)
        lastPerspective = None


def lockCameraYaw():
    """
    锁定相机偏转角
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    if comp:
        comp.LockModCameraYaw(1)


def lockCameraPitch():
    """
    锁定相机俯仰角
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    if comp:
        comp.LockModCameraPitch(1)


def releaseCameraLock():
    """
    解除摄像机锁定
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    if comp:
        comp.LockModCameraYaw(0)
        comp.LockModCameraPitch(0)


def setCanOperation(operation):
    """
    设置是否可操作
    """
    comp = clientApi.GetEngineCompFactory().CreateOperation(clientApi.GetLocalPlayerId())
    # 全部设置为不响应
    comp.SetCanAll(operation)


def getMyPosition():
    """
    获取本地玩家位置
    @return:
    """
    return getPosition(clientApi.GetLocalPlayerId())


def getPos(entityId):
    """
    获取实体位置（玩家在摄像机位置）
    @param entityId:
    @return:
    """
    pos = clientApi.GetEngineCompFactory().CreatePos(entityId)
    if pos:
        return pos.GetPos()


def getFootPos(entityId):
    """
    获取实体脚的位置
    @param entityId:
    @return:
    """
    pos = clientApi.GetEngineCompFactory().CreatePos(entityId)
    if pos:
        return pos.GetFootPos()


def getRot(entityId):
    """
    获取实体yaw pitch
    @param entityId:
    @return:
    """
    rot = clientApi.GetEngineCompFactory().CreateRot(entityId)
    if rot:
        return rot.GetRot()


def getPosition(entityId):
    """
    获取实体pos与rot
    @param entityId:
    @return:
    """
    return getPos(entityId), getRot(entityId)


def getCameraPosition():
    """
    获取camera中心位置
    @return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    if comp:
        return comp.GetPosition(), comp.GetForward()


def getFacing():
    # type: () -> dict
    """
    获取玩家准心所对方块
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    return comp.PickFacing()


def getChosen():
    """
    获取点击位置所指向的方块活实体信息
    @return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    return comp.GetChosen()


def getTouchPos():
    """
    获取点击位置
    :return:
    """
    return clientApi.GetTouchPos()


_screenInfo = None


def getScreenViewInfo():
    """
    获取屏幕大小信息
    @return:
    """
    global _screenInfo
    if _screenInfo is None:
        comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
        _screenInfo = comp.GetScreenSize()
    return _screenInfo


def createSfx(path="", pos=(0, 5, 0), rot=(0, 0, 0), scale=(1, 1, 1), faceCamera=True, layer=1, loop=False, bind=None, bindOffset=(0, 1, 0), bindRot=(0, 0, 0)):
    """
    创建序列帧
    :param path: 资源路径，不用json后缀
    :param pos: 世界上的位置
    :param rot: 选择欧拉角
    :param scale: 缩放
    :param faceCamera: 是否朝向镜头
    :param layer: 覆盖层级
    :param loop: 是否循环播放
    :param bind: 是否绑定在某个生物身上（绑定后pos失效）
    :param bindOffset: 绑定相对偏移位置（需要绑定）
    :param bindRot: 绑定相对旋转（需要绑定）
    :return:
    """
    frameEntityId = getSystem().CreateEngineSfx(path)
    frameAniTransComp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniTrans")
    frameAniTransComp.SetPos(tuple(pos))
    frameAniTransComp.SetRot(tuple(rot))
    frameAniTransComp.SetScale(tuple(scale))
    frameAniControlComp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniControl")
    if not faceCamera:
        frameAniControlComp.SetFaceCamera(False)
    if layer != 1:
        frameAniControlComp.SetLayer(layer)
    if loop:
        frameAniControlComp.SetLoop(True)
    if bind is not None:
        comp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniEntityBind")
        comp.Bind(bind, tuple(bindOffset), tuple(bindRot))
    frameAniControlComp.Play()
    # print "create sfx", path, frameEntityId,
    return frameEntityId


def updateSfx(sfxId, pos=None, rot=None, scale=None):
    frameAniTransComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(sfxId)
    if pos is not None:
        frameAniTransComp.SetPos(tuple(pos))
    if rot is not None:
        frameAniTransComp.SetRot(tuple(rot))
    if scale is not None:
        frameAniTransComp.SetScale(tuple(scale))


def createEditorSfx(path="", pos=None, rot=None, scale=None, faceCamera=True, layer=1, loop=False, bind=None, bindOffset=(0, 1, 0), bindRot=(0, 0, 0)):
    """
    创建【编辑器】序列帧
    :param path:
    :param pos:
    :param rot:
    :param scale:
    :param faceCamera:
    :param layer:
    :param loop:
    :param bind:
    :param bindOffset:
    :param bindRot:
    :return:
    """
    frameEntityId = getSystem().CreateEngineSfxFromEditor(path)
    frameAniTransComp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniTrans")
    if pos is not None:
        frameAniTransComp.SetPos(tuple(pos))
    if rot is not None:
        frameAniTransComp.SetRot(tuple(rot))
    if scale is not None:
        frameAniTransComp.SetScale(tuple(scale))
    frameAniControlComp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniControl")
    if not faceCamera:
        frameAniControlComp.SetFaceCamera(False)
    if layer != 1:
        frameAniControlComp.SetLayer(layer)
    if loop:
        frameAniControlComp.SetLoop(True)
    if bind is not None:
        comp = clientApi.CreateComponent(frameEntityId, "Minecraft", "frameAniEntityBind")
        comp.Bind(bind, tuple(bindOffset), tuple(bindRot))
    frameAniControlComp.Play()
    # print "create sfx", path, frameEntityId,
    return frameEntityId


def removeSfx(frameEntityId):
    """
    移除序列帧
    :param frameEntityId:
    """
    getSystem().DestroyEntity(frameEntityId)


def createParticle(path, pos=(0, 5, 0), layer=1, bind=None, bindOffset=(0, 1, 0), bindRot=(0, 0, 0), correction=False):
    """
    创建粒子
    :param path:
    :param pos:
    :param layer:
    :param bind:
    :param bindOffset:
    :param bindRot:
    :param correction:
    :return:
    """
    particleEntityId = getSystem().CreateEngineParticle(path, pos)
    particleControlComp = clientApi.CreateComponent(particleEntityId, "Minecraft", "particleControl")
    if layer != 1:
        particleControlComp.SetLayer(layer)
    if bind is not None:
        comp = clientApi.CreateComponent(particleEntityId, "Minecraft", "particleEntityBind")
        comp.Bind(bind, bindOffset, bindRot, correction=correction)

    particleControlComp.Play()
    # print "create particle", type(particleEntityId), particleEntityId
    return particleEntityId


def removeParticle(particleEntityId):
    """
    移除粒子
    :param particleEntityId:
    """
    getSystem().DestroyEntity(particleEntityId)


def startNavTo(pos, sfxPath="sfx/frame/navi", callback=None, sfxIntl=1, sfxMaxNum=128, sfxScale=(0.5, 0.5), maxIteration=800, isSwimmer=False):
    """
    开启导航
    :param pos:
    :param sfxPath:
    :param callback:
    :param sfxIntl:
    :param sfxMaxNum:
    :param sfxScale:
    :param maxIteration:
    :param isSwimmer:
    :return:
    """
    return clientApi.StartNavTo(pos, sfxPath, callback, sfxIntl, sfxMaxNum, sfxScale, maxIteration, isSwimmer)


def stopNav():
    """
    关闭导航
    """
    clientApi.StopNav()


def getBlock(pos):
    """
    获取方块
    @param pos:
    @return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "blockInfo")
    return comp.GetBlock(pos)


def getFpHeight():
    """
    获取第一人称摄像机与脚的高度，也是footpos和pos的高度差
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "camera")
    return comp.GetFpHeight()


def getMotion(playerId):
    """
    获取实体速度
    :param playerId:
    :return:
    """
    motionComp = clientApi.CreateComponent(playerId, "Minecraft", "actorMotion")
    return motionComp.GetMotion()


def setMotion(playerId, motion):
    """
    设置实体速度
    :param playerId:
    :param motion:
    :return:
    """
    motionComp = clientApi.CreateComponent(playerId, "Minecraft", "actorMotion")
    return motionComp.SetMotion(motion)


def isSneaking(playerId):
    """
    是否在潜行
    :param playerId:
    :return:
    """
    comp = clientApi.CreateComponent(playerId, "Minecraft", "player")
    return comp.isSneaking()


def popup(message, sub=""):
    """
    弹出物品栏消息
    :param message:
    :param sub:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "game")
    comp.SetPopupNotice(clientApi.GenerateColor("RED") + message, sub)


def getItemInHandId():
    """
    获取当前手持的快捷栏的槽i
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
    return comp.GetSlotId()


def getItemInHand():
    """
    获取手持物品
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
    return comp.GetCarriedItem()


def convertSlotIdToInventoryIndex(slotId):
    if 0 <= slotId <= 8:
        row = 3 - slotId / 9
        col = slotId % 9

        return row * 9 + col
    else:
        row = slotId / 9 - 1
        col = slotId % 9
        return row * 9 + col


def geteMolangValue(entityId, expr):
    import mod.client.extraClientApi as clientApi
    comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
    return comp.GetMolangValue(expr)


def registerMolang(variableName, value):
    comp = clientApi.GetEngineCompFactory().CreateQueryVariable(clientApi.GetLevelId())
    return comp.Register(variableName, value)


def setMolang(entityId, variableName, value):
    comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
    return comp.Set(variableName, value)


def isOnGround():
    """
    是否落地
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "player")
    return comp.isOnGround()


def getInputVector():
    """
    获取操作向量
    :return:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "actorMotion")
    return comp.GetInputVector()


def hideNameTag(player, hide):
    """
    隐藏玩家名
    :param player:
    :param hide:
    """
    comp = clientApi.CreateComponent(player, "Minecraft", "name")
    comp.SetShowName(not hide)


lastPlayedBgm = None


def playCustomBgm(name, unknow=1, unknow2=True):
    """
    播放自定义背景音乐（无位置）
    :param name:
    :param unknow:
    :param unknow2:
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "customAudio")
    if lastPlayedBgm is None:
        comp.DisableOriginMusic(True)
    else:
        comp.StopCustomMusic(lastPlayedBgm)
    comp.PlayGlobalCustomMusic(name, unknow, unknow2)


def stopCustomBgm():
    """
    停止播放自定义背景音乐
    """
    comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "customAudio")
    if lastPlayedBgm is not None:
        comp.StopCustomMusic(lastPlayedBgm)
    comp.DisableOriginMusic(False)


def playSound(name, pos=None, volume=1.0, pitch=1.0, loop=False, entityId=None):
    """
    播放音效
    @param name: sounds_definitions里定义的音效名称
    @param pos:  播放位置
    @param volume: 音量
    @param pitch: 音调（播放速度）
    @param loop: 循环播放
    @param entityId: 实体id，与位置二选一
    @return:
    """
    # print "playsound", name, pos, volume, pitch, loop, entityId
    comp = clientApi.GetEngineCompFactory().CreateCustomAudio(clientApi.GetLevelId() if entityId is None else entityId)
    from pythonScripts.share import VectorUtils
    return comp.PlayCustomMusic(name, VectorUtils.toInt(pos) if pos is not None else (0, 0, 0), volume=volume, pitch=pitch, loop=loop, entityId=entityId)


def sendMessage(msg):
    """
    发送聊天信息
    :param msg:
    """
    comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(clientApi.GetLocalPlayerId())
    comp.SetLeftCornerNotify(msg)


def sendTipMessage(msg):
    """
    发送tip信息
    :param msg:
    """
    comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLocalPlayerId())
    comp.SetTipMessage(msg)


def setFbxModel(entity, model):
    """
    设置fbx模型
    :param entity:
    :param model:
    :return:
    """
    modelComp = clientApi.CreateComponent(entity, 'Minecraft', 'model')
    # 'xuenv'即为netease_models.json里配置的骨骼模型名称
    print "set model", entity, model
    return modelComp.SetModel(model)


def setFbxTexture(entity, texture):
    """
    设置fbx贴图
    :param entity:
    :param texture:
    :return:
    """
    modelComp = clientApi.CreateComponent(entity, 'Minecraft', 'model')
    # 'xuenv'即为netease_models.json里配置的骨骼模型名称
    return modelComp.SetModelTexture(texture)


def playFbxAnimation(entity, animation, isLoop=False):
    """
    播放fbx动画
    :param entity:
    :param animation:
    :param isLoop:
    """
    modelComp = clientApi.GetEngineCompFactory().CreateModel(entity)
    # 播放动画'prepare'，第二个参数设置为True表示循环播放该动画，接口详细信息可以查看modAPI接口文档
    modelComp.PlayAnim(animation, isLoop)


def getIdentifier(entityId):
    """
    获取唯一id
    :param entityId:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreateEngineType(entityId)
    return comp.GetEngineTypeStr()


def getItemBasicInfo(item):
    """
    获取本地化属性，主要是本地化名称
    @param item:
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreateItem(clientApi.GetLevelId())
    return comp.GetItemBasicInfo(item.get("itemName"), item.get("auxValue", 0))


def getCurrentPlayerId():
    """
    获取当前客户端的playerId
    @return:
    """
    return clientApi.GetLocalPlayerId()


def getPerspective():
    """
    获取当前视角 0：第一人称视角；1：第三人称视角；2：前视第三人称视角
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePlayerView(clientApi.GetLocalPlayerId())
    return comp.GetPerspective()


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


def isWordValid(word):
    """
    敏感词校验
    :param word:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
    return comp.CheckWordsValid(word)


def setSkyColor(r, g, b):
    """
    设置天空颜色
    @param r:
    @param g:
    @param b:
    """
    if r > 1.0: r /= 256.0
    if g > 1.0: g /= 256.0
    if b > 1.0: b /= 256.0
    comp = clientApi.GetEngineCompFactory().CreateSkyRender(clientApi.GetLevelId())
    comp.SetSkyColor((r, g, b, 0.5))


def resetSkyColor():
    """
    重置天空颜色
    """
    comp = clientApi.GetEngineCompFactory().CreateSkyRender(clientApi.GetLevelId())
    comp.ResetSkyColor()


def setFog(lengthMin=None, lengthMax=None, color=None):
    """
    设置雾效
    @param lengthMin:
    @param lengthMax:
    @param color:
    """
    comp = clientApi.GetEngineCompFactory().CreateFog(clientApi.GetLevelId())
    if lengthMin is not None and lengthMax is not None:
        comp.SetFogLength(10, 50)
    if color is not None:
        comp.SetFogColor(color)


def resetFog():
    """
    重置雾效
    """
    comp = clientApi.GetEngineCompFactory().CreateFog(clientApi.GetLevelId())
    comp.ResetFogLength()
    comp.ResetFogColor()


def getLine(total, colPerLine):
    """
    获取grid行数
    @param total: 总数
    @param colPerLine: 每行多少物品
    @return:
    """
    return int(math.ceil(float(total) / colPerLine))


def getFov():
    """
    获取视野
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.GetFov()


def setFov(fov):
    """
    设置视野
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.SetFov(fov)


# 1.25版本，后处理
def getVignette():
    """
    检测是否开启了屏幕渐晕（Vignette）效果。
    @return: bool
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    return comp.CheckVignetteEnabled()


def setVignette(enable, center=(0.5, 0.5), color=(128, 0, 0), radius=0.5, smoothness=0.5):
    """
    设置开启屏幕渐晕效果
    @param enable:是否开启
    @param center:渐晕中心位置, 按顺序分别为屏幕位置的x及y值
    @param color:渐晕颜色, 值的范围为[0,255]
    @param radius:渐晕半径, 值的范围为[0,1]
    @param smoothness:渐晕模糊系数，值的范围为[0,1], 模糊系数越大，则渐晕边缘越模糊，模糊的范围也越大
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    comp.SetEnableVignette(enable)
    if enable:
        comp.SetVignetteCenter(center)
        comp.SetVignetteRGB(color)
        comp.SetVignetteRadius(radius)
        comp.SetVignetteSmoothness(smoothness)


def getGaussianBlur():
    """
    检测是否开启了高斯模糊效果。
    @return:bool
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    return comp.CheckGaussianBlurEnabled()


def setGaussianBlur(enable, radius=3):
    """
    开启高斯模糊效果，开启后玩家屏幕周围被模糊
    @param enable:是否开启
    @param radius:设置高斯模糊效果的模糊半径，值的范围为[0,10], 半径越大，模糊程度越大，反之则模糊程度越小
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    comp.SetEnableGaussianBlur(enable)
    if enable:
        comp.SetGaussianBlurRadius(radius)


def getColorAdjustment():
    """
    检测是否开启了色彩校正效果
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    return comp.CheckColorAdjustmentEnabled()


def setColorAdjustment(enable, brightness=3, contrast=3, saturation=3, tint=[0.3, (255, 0, 0)]):
    """
    开启色彩校正效果，开启后可进行屏幕色彩调整
    @param enable:是否开启
    @param brightness:调整屏幕色彩亮度，值的范围为[0,5]，亮度值越大，屏幕越亮，反之则越暗
    @param contrast:调整屏幕色彩对比度，值的范围为[0,5], 屏幕对比度值越大，色彩差异则越明显，反之则色彩差异越小
    @param saturation:调整屏幕色彩饱和度，值的范围为[0,5]，屏幕饱和度值越大，色彩则越明显，反之则越灰暗
    @param tint:调整屏幕色彩的色调，[色调强度, 色调值]根据输入的色调和强度来调整屏幕色彩，当强度越大时，屏幕整体颜色越偏向输入的色调，色调强度，值的范围为[0,1]，色调值，按顺序分别为颜色的RGB值，值的范围为[0,255]
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    comp.SetEnableColorAdjustment(enable)
    if enable:
        comp.SetColorAdjustmentBrightness(brightness)
        comp.SetColorAdjustmentContrast(contrast)
        comp.SetColorAdjustmentSaturation(saturation)
        comp.SetColorAdjustmentTint(*tint)


def getDepthOfField():
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    return comp.CheckDepthOfFieldEnabled()


def setDepthOfField(enable, blurRadius=0.3, farBlurScale=1.0, focusDistance=4, nearBlurScale=1.0, centerFocus=False):
    """
    开启景深效果，开启后屏幕出现景深效果，根据焦点距离呈现远处模糊近处清晰或者近处模糊远处清晰的效果
    @param enable:是否开启
    @param blurRadius:模糊半径值大小，值的范围为[0,5]，模糊半径越大，模糊程度越大
    @param farBlurScale:远景模糊大小，值的范围为[0,15]，远景模糊大小越大，远景的模糊程度越大
    @param focusDistance:焦点距离值大小，值的范围为[0,100]，距离越小，则远处模糊，近处清晰
    @param nearBlurScale:近景模糊大小，值的范围为[0,15]，近景模糊大小越大，近景的模糊程度越大
    @param centerFocus:景深效果屏幕中心聚焦模式，和focusDistance互斥，开启后聚焦距离将被自动设置为屏幕中心所对应的物体所在的距离
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    comp.SetEnableDepthOfField(enable)
    if enable:
        comp.SetDepthOfFieldFarBlurScale(blurRadius)
        comp.SetDepthOfFieldFarBlurScale(farBlurScale)
        comp.SetDepthOfFieldFocusDistance(focusDistance)
        comp.SetDepthOfFieldNearBlurScale(nearBlurScale)
        comp.SetDepthOfFieldUseCenterFocus(centerFocus)


def getLensStain():
    """
    检测是否开启了镜头污迹效果
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    return comp.CheckLensStainEnabled()


def setLensStain(enable, reset=False, texture="", color=(0, 0, 0), intensity=0):
    """
    开启镜头污迹效果，开启后镜头出现污迹效果，可改变使用的污迹贴图及污迹颜色
    @param enable:
    @param reset:重置污迹效果使用的贴图为系统默认贴图
    @param texture:图的相对路径，以“textures/"开头，不需要后缀名，贴图最好使用透明背景，否则屏幕将被贴图覆盖
    @param color:镜头污迹颜色，按顺序分别为颜色的RGB值，值的范围为[0,255]
    @param intensity:颜色强度，值的范围为[0,1]，强度越大时，污迹颜色越偏向输入的颜色
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePostProcess(clientApi.GetLevelId())
    comp.SetEnableLensStain(enable)
    if texture == "":
        return
    if reset:
        comp.ResetLensStainTexture()
        return
    if enable and not reset:
        comp.SetLensStainTexture(texture)
        comp.SetLensStainColor(intensity, color)


def getCameraAnchor():
    # type: () -> tuple[float,float,float]
    """
    获取相机锚点
    @return: 锚点偏移量
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.GetCameraAnchor()


def setCameraAnchor(offset):
    # type: (tuple[float,float,float]) -> bool
    """
    设置相机锚点,暂时只支持高度,其他维度无效
    :param offset: 锚点偏移量
    :return: 是否成功
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.SetCameraAnchor(offset)


def getCameraOffset():
    # type: () -> tuple[float,float,float]
    """
    获取摄像机偏移量
    @return: 偏移量
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.GetCameraOffset()


def setCameraOffset(offset):
    # type: (tuple[float,float,float]) -> bool
    """
    设置摄像机偏移量
    注意，该接口仅改变第三人称的相机（包括前视第三人称和后视第三人称）的偏移量，对第一人称模式下的相机无效。
    与SetCameraAnchor不同的是，该接口改变的是相机的位置偏移值，不会对相机轨道的圆心位置进行改变。
    注意，设置后的效果不会存档
    @param offset:
    @return:
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.SetCameraOffset(offset)


def resetCameraBindActorId():
    # type: () -> bool
    """
    将摄像机重新绑定回主角身上
    @return: 是否设置成功
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.ResetCameraBindActorId()


def setCameraBindActorId(targetId):
    # type: (str) -> bool
    """
    将摄像机绑定到目标实体身上（调用者与目标必须在同一个dimension，同时需要在加载范围之内，若绑定后目标离开了范围或者死亡，则会自动解除绑定）
    @targetId: 目标实体id
    @return: 是否设置成功
    """
    comp = clientApi.GetEngineCompFactory().CreateCamera(clientApi.GetLevelId())
    return comp.SetCameraBindActorId(targetId)


def isGliding(playerId):
    """
    玩家是否在鞘翅飞行
    :param playerId:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.isGliding()


def isInWater(playerId):
    """
    玩家是否在水中
    :param playerId:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.isInWater()


def isMoving(playerId):
    """
    玩家是否在移动
    :param playerId:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.isMoving()


def isRiding(playerId):
    """
    玩家是否在骑乘
    :param playerId:
    :return:
    """
    comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
    return comp.isRiding()


def getVanillaQuery(playerId, query):
    """
    获取原版变量
    :param playerId:
    :param query:
    :return:
    """
    queryComp = clientApi.GetEngineCompFactory().CreateQueryVariable(playerId)
    return queryComp.GetMolangValue(query)


def getQuery(playerId, query):
    """
    获取查询变量
    :param playerId:
    :param query:
    :return:
    """
    queryComp = clientApi.GetEngineCompFactory().CreateQueryVariable(playerId)
    return queryComp.Get(query)


def setQuery(playerId, query, value):
    """
    设置查询变量
    :param playerId:
    :param query:
    :param value:
    """
    queryComp = clientApi.GetEngineCompFactory().CreateQueryVariable(playerId)
    queryComp.Set(query, float(value))
