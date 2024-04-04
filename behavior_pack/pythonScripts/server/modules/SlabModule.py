# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.server.modules.BaseServerModule import *
from pythonScripts.share import VectorUtils

"""
半砖模块，主要用于处理玩家向上放置半砖时自动变成上半砖的功能
"""


class SlabModule(BaseServerModule):
    @DefaultServerModule(name=StaticConfig.Module.Slab, version=-1)
    def __init__(self):
        super(SlabModule, self).__init__()

    def example(self, system):
        # 这里配置的时下上半砖的对应，玩家手中只回包含下板砖，点击上半部分时替换成上半部分
        system.addData(StaticConfig.Data.SLAB_UPPER, {
            # 下半砖的id：上半砖的id
            "tofucraft:blocktofukinu_slab": "tofucraft:blocktofukinu_slabtop",
            "tofucraft:blocktofumomen_slab": "tofucraft:blocktofumomen_slabtop",
            "tofucraft:blocktofuishi_slab": "tofucraft:blocktofuishi_slabtop",
            "tofucraft:blocktofumetal_slab": "tofucraft:blocktofumetal_slabtop",
            "tofucraft:blocktofudiamond_slab": "tofucraft:blocktofudiamond_slabtop",
            "tofucraft:blocktofugrilled_slab": "tofucraft:blocktofugrilled_slabtop",
            "tofucraft:blocktofudried_slab": "tofucraft:blocktofudried_slabtop",
            "tofucraft:blocktofuegg_slab": "tofucraft:blocktofuegg_slabtop",
            "tofucraft:blocktofuminced_slab": "tofucraft:blocktofukinu_slabtop",
        })
