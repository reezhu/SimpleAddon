# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.client.modules.BaseClientModule import *

"""
这是一个通用的ui按钮模块，会在装备或者手持物品时显示按钮，快速制作拔刀剑类型的模组，支持长按拖动并保存对应位置

"""


class EquipmentInteractModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.EquipmentInteract, version=-1)
    def __init__(self):
        super(EquipmentInteractModule, self).__init__()

    def example(self, system):
        """
        数据格式举例，只用于参考，请配置在modMain.py
        :param system:
        """
        system.addData(StaticConfig.Data.ITEM_BUTTON, {
            # 需要显示按钮的物品
            "minecraft:diamond_sword": {
                # 是否是手持，False时只有穿戴时才会显示
                "hand": True,
                # 打开这个开关，会使用EquipmentDynamicButtonStatusEvent向服务器进行广播，服务端可以返回动态配置
                "dynamic": True,
                # 按钮，可包含多个按钮
                "buttons": {
                    # 每个按钮的唯一key,建议添加组件名与其他组件形成区分
                    config.ModName + ":shoot": {
                        # 按钮默认图片
                        "tx": "textures/netease/common/button/default",
                        # 按钮按下图片
                        "txp": "textures/netease/common/button/pressed",
                        # 按钮悬浮图片
                        "txh": "textures/netease/common/button/hover",
                        # 初始位置，范围为0~1，代表左上角占整个屏幕的百分比
                        "pos": (0.72, 0.7),
                        # 按钮的大小，像素
                        "size": (30, 20),
                        # 按钮上的文本
                        "text": "剑的",
                        # 按钮上字体的缩放比例
                        "textSize": 1,
                        # 点击按钮时向服务器通知的事件，如果不清楚是干什么的，请留给技术填
                        "notify": "123",
                        # 冷却时间，如果配置就会在客户端设置点击冷却，注意会覆盖text，单位tick
                        "cooldown": 1800,
                        # 冷却时的提示
                        "cooling": "你的武器还在蓄力中",
                        # 这个设置可以让不同的按钮只显示一个（比如多个准心开关）
                        "single": "aim",
                    },
                    # 这是这个物品的另一个按钮配置
                    config.ModName + ":doSomething": {
                        "tx": "textures/netease/common/button/default",
                        "txp": "textures/netease/common/button/pressed",
                        "txh": "textures/netease/common/button/hover",
                        "pos": (0.72, 0.8),
                        "size": (30, 20),
                        "text": "剑的2",
                        "textSize": 1,
                        # dict格式，会以 PlayerSkillButtonNotifyEvent 事件向服务端进行通知，用于skill模块统一处理
                        "notify": {
                            "identifier": "A",
                            "duplicate": 0,
                            "kwargs": {}
                        }
                    },
                }
            },
            # 这是另一个物品的配置
            "minecraft:diamond_helmet": {
                # 标记为False时只有穿在身上才会显示按钮
                "hand": False,
                "buttons": {
                    "hel": {
                        "tx": "textures/netease/common/button/default",
                        "txp": "textures/netease/common/button/pressed",
                        "txh": "textures/netease/common/button/hover",
                        "pos": (0.72, 0.3),
                        "size": (30, 20),
                        "text": "头的",
                        "textSize": 1,
                        "notify": "456",
                        # 当包含switch时，添加按钮会向服务器发送EquipmentSwitchStatusEvent，服务端可以通过下发EquipmentSwitchStatusEvent来控制显示什么按钮，default为默认按钮
                        "switch": {
                            # 用于调用的key
                            "disable": {
                                "tx": "textures/items/skill6",
                                "txp": "textures/items/skill6",
                                "txh": "textures/items/skill6",
                            }

                        }

                    },
                }
            },
        }, version=0)
