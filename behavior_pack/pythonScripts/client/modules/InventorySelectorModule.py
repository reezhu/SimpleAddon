# -*- coding: utf-8 -*-
# @Author  : Ree
from pythonScripts.client.modules.BaseClientModule import *

"""
用于给玩家一个物品栏的弹窗，快速选择使用的物品
创建时把过滤器filter和回调函数传入即可
"""


class InventorySelectorModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.InventorySelector, version=-1)
    def __init__(self):
        super(InventorySelectorModule, self).__init__()

    def pop(self, callback=None, filter=None):
        # type: (callable(int,dict), callable(dict)) -> None
        """

        :param callback: 点击物品的回调，变量为位置与物品,返回True时关闭ui
        :param filter: 显示过滤器，变量为物品，返回True或者False表示是否高亮该物品
        """
        pass
