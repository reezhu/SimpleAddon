# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share import VectorUtils

"""
传送门模块，可以按照配置的位置，自动生成传送门方块
支持四个方向自动匹配
支持不同维度生成不同的方块

"""


class PortalModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Portal, version=-1)
    def __init__(self):
        super(PortalModule, self).__init__()

    def example(self, system):
        # 传送门定义
        system.addData(StaticConfig.Data.PORTAL_DEFINE, {
            config.ModName + "portal": {
                # 横向切片，为了直观，简化为一个字符，具体方块配置于mapping字段
                "pattern": [
                    [
                        '    ',
                        '    ',
                        '    ',
                        '    ',
                        '    ',
                    ],
                    [
                        '####',
                        '#**#',
                        '#**#',
                        '#**#',
                        '####',
                    ], [
                        '    ',
                        '    ',
                        '    ',
                        '    ',
                        '    ',
                    ],
                ],
                # 方块匹配，必须对应位置符合方块名称才会认为是合法的传送门
                "mapping": {
                    '#': 'tofucraft:blocktofugrilled',
                    '*': 'minecraft:air'
                },
                # 触发物品
                "key": ["tofucraft:tofustick"],
                # 可以触发的方块（方块类型越少，匹配效率越高）
                "active": {
                    "#"
                },
                # 根据表达式，把对应位置的方块替换成新的方块，可根据dimensionId生成来或回的传送门方块，复用同一个结构配置
                "convert": {
                    '*': lambda dimension: 'tofu:portal_content_back' if dimension == 322372559 else "tofu:portal_content"
                },

            }
        })
