# -*- coding: utf-8 -*-

from pythonScripts.client.modules.BaseClientModule import *

"""
多段跳，数据见UpdateDoubleJumpEvent方法
"""


class DoubleJumpClientModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.DoubleJump, version=-1)
    def __init__(self):
        super(DoubleJumpClientModule, self).__init__()
        self.maxJump = 0  # 最大连跳次数
        self.power = 1  # 跳跃力度

    def UpdateDoubleJumpEvent(self, args):
        print("UpdateDoubleJump", args)
        self.maxJump = args.get("jump", 0)
        self.power = args.get("power", 1)
