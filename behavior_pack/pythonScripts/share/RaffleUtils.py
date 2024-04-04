# -*-coding:utf-8 -*-

"""
# File       : RaffleUtils.py
# Time       ：2021/8/16 14:44
# Author     ：Siyi
# version    ：python 2.7
# Description：通用抽奖模块，抽奖池结构和使用见example
"""
import RandomUtils


class RaffleSystem:
    def __init__(self, pools, minCount, maxCount, importance):
        """
        初始化抽奖系统
        @param pools: # 抽奖池
        @param minCount: # 大奖出现最低次数
        @param maxCount: # 大奖出现最多次数/保底次数
        @param importance: # 大奖池的最高rate，小于等于此rate的抽奖池为大奖池
        """
        self.raffleCount = 0  # 抽奖次数
        self.pools = pools  # 抽奖池
        self.min = minCount  # 大奖出现最低次数
        self.max = maxCount  # 大奖出现最多次数/保底次数
        self.importance = importance  # 大奖池的最高rate，小于等于此rate的抽奖池为大奖池

    def _random(self, pool):
        """
        从单个抽奖池中抽出一个奖品，也用于从多个抽奖池中抽出一个抽奖池
        @param pool: 单个抽奖池
        @return:
        """
        generator = RandomUtils.RandomGenerator()
        for prize in pool:
            generator.add(prize["rate"], prize["obj"])
        return generator.getRandom()

    def raffle(self, pools=None, raffleCount=None):
        """
        进行一次抽奖
        @param pools: 多个抽奖池
        @param raffleCount: 抽奖次数，用于外部控制抽奖，为空则默认每次增加 1次
        @return: 一个奖品 -> str
        """
        if not pools:
            pools = self.pools
        if raffleCount:
            self.raffleCount = raffleCount
        else:
            self.raffleCount += 1
        return self._random(self._random(pools))

    def raffleByRule(self):
        """
        根据__init__定义的抽奖规则进行一次抽奖
        @return: 一个符合抽奖规则的奖品 -> str
        """
        currentPools = []
        importantPools = []
        commonPools = []
        importantPoolsName = []
        for pool in self.pools:
            if pool["rate"] <= self.importance:
                importantPools.append(pool)
                importantPoolsName.append(pool["name"])
            else:
                commonPools.append(pool)

        self.raffleCount += 1
        if self.raffleCount >= self.max:
            currentPools = importantPools
        elif self.raffleCount > self.min:
            currentPools = commonPools + importantPools
        else:
            currentPools = commonPools
        prize = self.raffle(currentPools, self.raffleCount)
        # prize : {"name": "pool1:item1", "obj": {"rate": 2,  "enchanted": None, "icon": ""}}
        if prize.keys()[0].split(":")[0] in importantPoolsName:
            self.raffleCount = 0
        return prize

    def getRaffleItemList(self, length):
        """
        抽奖生成一个固定长度的奖品列表
        @param length: 奖品列表长度
        @return:
        """
        self.raffleCount = 0
        raffleItem = []
        for iter in xrange(0, length):
            raffleItem.append(self.raffleByRule())
        return raffleItem


def example():
    # 单个抽奖池 list[dict{"rate": int, "obj": str}]
    # 抽奖池1
    pool1 = [
        # 一个物品 dict{"rate": 权重概率->int, "obj": 物品}
        {"rate": 1, "obj": {"pool1:item1": {"rate": 1, "enchanted": None, "icon": "textures/ui/crystal_thunder_effect"}}},
        {"rate": 2, "obj": "pool1:item2"},  # 加权概率意思是 此权重概率 / 所有权重概率总和
        {"rate": 3, "obj": "pool1:item3"}  # 比如此物品的概率为 3 / (1+2+3) = 1/2，即0.5
    ]
    # 抽奖池2
    pool2 = [
        {"rate": 1, "obj": "pool2:item1"},
        {"rate": 1, "obj": "pool2:item2"},
        {"rate": 1, "obj": "pool2:item3"},
        {"rate": 1, "obj": "pool2:item4"},
    ]
    pool3 = [
        {"rate": 1, "obj": "pool3:item1"},
        {"rate": 2, "obj": "pool3:item2"},
        {"rate": 3, "obj": "pool3:item3"}
    ]
    pool4 = [
        {"rate": 1, "obj": "pool4:item1"},
        {"rate": 2, "obj": "pool4:item2"},
        {"rate": 3, "obj": "pool4:item3"}
    ]
    pool5 = [
        {"rate": 1, "obj": "pool5:item1"},
        {"rate": 2, "obj": "pool5:item2"},
        {"rate": 3, "obj": "pool5:item3"}
    ]
    # 总物品池，包含前5个物品池
    # 结构：list[dict{"rate": int, "name": str, "obj": 前面定义的pool}]
    pools = [
        {"rate": 1, "name": "pool1", "obj": pool1},  # 一个抽奖池
        {"rate": 2, "name": "pool2", "obj": pool2},  # dict{"rate": 权重概率, "name": 抽奖池名, "obj": 包含物品的抽奖池}
        {"rate": 3, "name": "pool3", "obj": pool3},  # 抽奖池名和抽奖池变量不必相同，不含抽奖池变量也可以
        {"rate": 4, "name": "pool4", "obj": pool4},  # 但抽奖池结构一定要是list[dict{"rate": int, "obj": str}]
        {"rate": 4, "name": "pool5", "obj": pool5},  # 抽奖池名和抽奖池内物品前缀也一定要相同
        {"rate": 1, "name": "bigPool",  # 一个没定义抽奖池变量的抽奖池结构
         "obj": [
             {"rate": 1, "obj": "bigPool:minecraft:pig"}
         ]
         }
    ]
    # 一个抽奖系统对象
    min = 3  # 大奖出现最低次数
    max = 10  # 大奖出现最多次数/保底次数
    importance = 1  # 大奖池的最高rate，小于等于此rate的抽奖池为大奖池
    raffleExample = RaffleSystem(pools, min, max, importance)
    # 通过抽奖系统生成一个长度为10的奖品列表
    print raffleExample.getRaffleItemList(10)
