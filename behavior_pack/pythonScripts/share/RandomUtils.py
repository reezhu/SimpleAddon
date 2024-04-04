# -*- coding: utf-8 -*-
# @Author  : Ree
import random

"""随机工具，可以对任意多样物品加权随机"""


class RandomGenerator:
    def __init__(self):
        self.total = 0.0
        self.lib = []

    def add(self, rate, obj):
        self.total += rate
        self.lib.append({"r": rate, "v": obj})
        return obj

    def remove(self, obj):
        for entry in self.lib:
            if entry["v"] == obj:
                self.total -= entry["r"]
                self.lib.remove(entry)
                return obj
        return None

    def getRandom(self):
        if self.total == 0: return None
        v = random.random() * self.total
        for entry in self.lib:
            v -= entry["r"]
            if v <= 0:
                return entry["v"]
        return None
