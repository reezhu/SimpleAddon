# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.server import ServerUtils
from pythonScripts.share import VectorUtils

"""
这里定义了一些目标选择器，配置见技能模块
"""


class TargetSelector(object):
    @staticmethod
    def ALL(entityId, pos, rot):
        return True  # 选择全体

    @staticmethod
    def FORWARD(entityId, pos, rot):
        return (
            VectorUtils.dot(VectorUtils.minus(ServerUtils.getPos(entityId), pos), rot)
            > 0
        )  # 选择前方

    @staticmethod
    def BACKWARD(entityId, pos, rot):
        return (
            VectorUtils.dot(VectorUtils.minus(ServerUtils.getPos(entityId), pos), rot)
            < 0
        )  # 选择后方


class VictimSelector(object):
    AllPlayer = "@a"
    AllEntity = "@e"
    NearestPlayer = "@p"
    RandomPlayer = "@r"
    Self = "@s"
