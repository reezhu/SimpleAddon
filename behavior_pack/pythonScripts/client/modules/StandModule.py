# coding=utf-8

from pythonScripts.client.modules.BaseClientModule import *
from pythonScripts.share import StaticConfig


class Decorator:

    def __init__(self):
        self.vanilla = None  # steve模型贴图
        self.tpos = None  # t骨模型贴图


class Material:
    Default = "entity_alphatest"
    Blend = "redstone_blend_v1"
    Glint = "redstone_glint_v1"


legencyMaterialDict = {
    0: "entity_alphatest",
    1: "redstone_blend_v1",
    2: "redstone_glint_v1",
}


class FirstPerspectVisibility:
    arms = "query.mod.show_first_hand"
    head = "query.mod.show_first_head"
    body = "query.mod.show_first_body"
    legs = "query.mod.show_first_legs"
    rest = "query.mod.show_first_rest"


"""替换玩家的微软模型功能,非常复杂，一般使用配置即可"""


class StandModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.Stand, version=-1)
    def __init__(self):
        BaseClientModule.__init__(self)

    def setPlayerModel(self, playerId, model, persist=False):
        """
        设置玩家模型
        :param tpos: 是否初始化为T型骨骼
        :param playerId:
        :param geometry:
        :param texture:
        @param animationSets: 替换默认的动画组
        @param tpos: 是否是t字骨骼
        @param persist: 是否是持续装扮
        """

        pass

    def addDecorator(
        self,
        playerId,
        key,
        vanillaGeometry,
        tposGeometry,
        vanillaTexture,
        tposTexture,
        vanillaMaterial,
        tposMaterial,
    ):
        pass

    def removeDecorator(self, playerId, key):
        pass

    def playAnimation(
        self,
        playerId,
        animation,
        t=-1,
        callback=None,
        first_animation=None,
        singleton=False,
    ):
        """
        播放动画
        :param playerId:
        :param animation: 动画的key
        :param t: 播放时间，-1为永久,单位tick（每秒30）
        :param callback: 播放完成后的回调
        :param first_animation: 为第一人称播放单独的动画
        :param singleton: 此动画标记为唯一，无法与其他唯一动画同时播放，会停止之前的唯一动画
        """
        pass

    def stopAnimation(self, playerId, animation, first_animation=None):
        """
        停止某个动画
        :param playerId:
        :param animation:
        :param first_animation: 如果在播放时设定了第一人称动画，停止时也需要加上
        """
        pass

    def getAnimationTasks(self, playerId):
        """
        获取玩家当前在播放的动画
        :param playerId:
        :return:
        """
        pass

    def stopAllAnimation(self, playerId):
        """
        停止玩家所有动画
        :param playerId:
        """
        pass

    def resetPlayer(self, playerId, clearPersist=False):
        """
        重置玩家的模型与动画
        :param playerId:
        @param clearPersist: 是否清除持久装扮
        """

        pass

    def setPartVisible(self, playerId, part, visible):
        # type: (str, str, bool) -> None
        """
        设置部件可见性
        @param playerId:
        @param part: FirstPerspectVisibility中的字段
        @param visible:
        """
        pass

    def getPartVisible(self, playerId, part):
        # type: (str, str) -> float
        """
        获取部件可见性
        @param playerId:
        @param part: FirstPerspectVisibility中的字段
        @param visible:
        """
        pass

    def setFirstPersonDefaultPartVisibility(self, playerId, visible):
        """
        设置是否显示第一人称默认部位  todo 废弃
        :param playerId:
        :param visible:
        """
        pass

    def setHandDisplayed(self, playerId, visible):
        """
        设置是否显示手 todo 废弃
        :param playerId:
        :param visible:
        :return:
        """
        pass

    def getAvatarStatus(self, playerId):
        pass

    def isPlayerTpos(self, playerId):
        pass
