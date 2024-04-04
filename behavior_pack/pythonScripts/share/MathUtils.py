# -*- coding: utf-8 -*-
# @Author  : Ree
"""一些数学工具"""


def clip(num, minN=0.0, maxN=0.0):
    return max(minN, min(num, maxN))


def lerp(a, b, t):
    t = clip(t, 0.0, 1.0)
    return a + (b - a) * t


def lerpSoft(a, b, t):
    t = clip(t, 0.0, 1.0)
    return a + (b - a) * (t * t * (3 - 2 * t))
