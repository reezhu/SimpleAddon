# -*- coding: utf-8 -*-
# @Author  : Ree
import json

"""
这个工具用于比较方便的序列化blockentity数据,注意super要写在变量初始化后面，不需要使用json解析的字段必须给初始值，不能初始化为None
示例：
class CraftingTable(BlockEntity):

    def __init__(self, blockEntityData):
        self.items = [None for i in range(8)] # 这个字段会被当作json传输
        self.result = None # 这个字段会被当作json传输
        self.can_burn = True # 这个字段会当作bool传输 
        self.tick = 0 # 这个字段会当作num传输
        super(CraftingTable, self).__init__(blockEntityData)
"""


class BlockEntity(object):
    _blockEntityData = None
    _params = {}

    def __init__(self, blockEntityData):
        # log = "saved "
        for k, v in self.__dict__.items():
            if k.startswith("_"): continue

            data = blockEntityData[k]
            # log += "%s:%s," % (k, data)
            if type(v) in {int, float}:
                self._params[k] = "num"
                object.__setattr__(self, k, v if data is None else data)
            elif type(v) in {bool}:
                self._params[k] = "bool"
                object.__setattr__(self, k, v if data is None else data)
            elif type(v) == str:
                self._params[k] = "str"
                object.__setattr__(self, k, v if data is None else data)
            else:
                self._params[k] = "json"
                object.__setattr__(self, k, v if data is None else json.loads(data))
        # print log, self._params
        object.__setattr__(self, "_blockEntityData", blockEntityData)

    def __setattr__(self, key, value):
        if key.startswith("_"): return object.__setattr__(self, key, value)
        object.__setattr__(self, key, value)
        # print "set attr", key, value, self._blockEntityData is not None
        if self._blockEntityData is not None:
            if self._params.get(key) == "json":
                value = None if value is None else json.dumps(value)
            elif self._params.get(key) == "num":
                value = 0 if value is None else value
            elif self._params.get(key) == "bool":
                value = False if value is None else value
            elif self._params.get(key) == "str":
                value = "" if value is None else value
            self._blockEntityData[key] = value

    def __getattribute__(self, item):
        if item.startswith("_"): return object.__getattribute__(self, item)
        if self._params.get(item) == "num":
            value = object.__getattribute__(self, item)
            return value if value is not None else 0
        elif self._params.get(item) == "bool":
            value = object.__getattribute__(self, item)
            return value if value is not None else False
        else:
            return object.__getattribute__(self, item)

    def switchBlock(self, newBlock):
        """
        反序列化用于更新数据
        :param newBlock:
        """
        # print "switch", self.__dict__
        for k, v in self._params.items():
            newBlock[k] = getattr(self, k)
        self._blockEntityData = newBlock

    def getNetData(self):
        """
        序列化获取用于网络传输的数据
        :return:
        """
        result = {}
        for k, v in self._params.items():
            result[k] = getattr(self, k)
        return result
