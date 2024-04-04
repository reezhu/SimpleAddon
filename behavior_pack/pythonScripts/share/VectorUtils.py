# -*- coding: utf-8 -*-
# @Author  : Ree
import math

"""向量计算工具"""
__degree = math.pi / 180.0


def add(vector1, vector2):
    """
    加法
    @vector vector1:
    @vector vector2:
    @return:
    """
    return tuple([x + y for x, y in zip(vector1, vector2)])


def minus(vector1, vector2):
    """
    减法
    @vector vector1:
    @vector vector2:
    @return:
    """
    return tuple([x - y for x, y in zip(vector1, vector2)])


def multiple(vector, multiple):
    """
    数乘
    @vector vector:
    @vector multiple:
    @return:
    """
    return tuple([i * multiple for i in vector])


def cross(vector1, vector2):
    """
    叉乘（仅三维）
    @vector vector1:
    @vector vector2:
    @return:
    """
    xa, ya, za = vector1
    xb, yb, zb = vector2
    return ya * zb - za * yb, za * xb - xa * zb, xa * yb - ya * xb


def dot(vector1, vector2):
    """
    点乘
    @vector vector1:
    @vector vector2:
    @return:
    """
    total = 0
    for x, y in zip(vector1, vector2):
        total += x * y
    return total


def normalize(vector):
    """
    标准化
    @vector vector:
    @return:
    """
    ls = 0
    for i in vector:
        ls += i * i
    if ls == 0:
        return (0, 0, 0)
    ls = math.sqrt(ls)
    return tuple([i / ls for i in vector])


def isZeroPoint(vector):
    """
    是不是原点
    @vector vector:
    @return:
    """
    for i in range(len(vector)):
        if vector[i] != 0:
            return False
    return True


def findVelocity(vector, radians):
    """
    获取某个向量垂直的向量,通常用于环绕某个轴的特效
    @vector face: 输入向量
    @vector radians: 旋转的角度
    @return:
    """
    if vector is None:
        return

    a = cross(vector, (0, 1, 0))

    if isZeroPoint(a):
        a = cross(vector, (1, 1, 1))
    b = cross(a, vector)
    a = normalize(a)
    b = normalize(b)
    return add(multiple(a, math.sin(radians)), multiple(b, math.cos(radians)))


def angle2vector(rot):
    """
    yaw-pitch转向量
    @vector rot:
    @return:
    """
    pitch, yaw = rot  # 由于网易getRot返回的两个变量与习惯是反的，所以增加了一次反向

    y = math.sin((float)(-pitch * __degree))
    xz = math.cos((float)(pitch * __degree))
    x = -math.sin((float)(yaw * __degree)) * xz
    z = math.cos((float)(yaw * __degree)) * xz
    return x, y, z


def vector2angle(vector):
    """
    向量转yaw-pitch
    @vector vector:
    @return:
    """
    x, y, z = vector
    yaw = math.atan2(-x, z) / __degree
    sqrt = math.sqrt(x * x + z * z)
    pitch = math.atan2(-y, sqrt) / __degree
    while yaw < -180:
        yaw += 360
    while yaw > 180:
        yaw -= 360
    return pitch, yaw


def length(motion):
    """
    取向量长度
    @param motion:
    @return:
    """
    total = 0
    for x in motion:
        total += x * x
    return math.sqrt(total)


def distance(vector1, vector2):
    """
    计算距离
    @param vector1:
    @param vector2:
    @return:
    """
    return math.sqrt(distanceSquard(vector1, vector2))


def distanceToLine(pointInLine, vector, targetPoint):
    """
    计算点到线的距离
    @param pointInLine: 线上的任意点
    @param vector:线的方向
    @param targetPoint:目标点
    @return:
    """
    offset = minus(pointInLine, targetPoint)
    return length(cross(offset, normalize(vector)))


def distanceSquard(vector1, vector2):
    """
    计算距离的平方和
    @param vector1:
    @param vector2:
    @return:
    """
    distance = 0
    for x, y in zip(vector1, vector2):
        distance += (x - y) ** 2
    return distance


def findFront(pos, rot, distance, ignoreYaw=True):
    """
    计算某个位置前的某个举例
    @param pos:
    @param rot:
    @param distance:
    @return:
    """
    x, y, z = angle2vector(rot)
    return add(pos, multiple(normalize((x, 0 if ignoreYaw else y, z)), distance))


def toInt(vector1):
    """
    向量内数值取整
    @vector vector1:
    @vector vector2:
    @return:
    """
    return tuple([int(x) for x in vector1])


class Link(object):
    """
    一个用于计算两点之间序列帧的工具
    """

    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

    def getPos(self):
        return add(multiple(add(self.pos1, self.pos2), 0.5), (0.1, 0.1, 0.1))

    def getScale(self, scale=0.05):
        return scale, length(minus(self.pos1, self.pos2)) * 0.5, scale

    def getRot(self, offset=(0, 1, 1)):
        p, y = vector2angle(minus(self.pos1, self.pos2))
        return add((0, y + 90, -p - 90), offset)
