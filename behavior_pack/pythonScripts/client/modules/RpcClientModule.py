# -*- coding: utf-8 -*-
# @Author  : Ree

from pythonScripts.client.modules.BaseClientModule import *

"""
可以进行一些静态方法的远程调用，方便从客户端查询服务端数据
"""


class RpcClientModule(BaseClientModule):
    @DefaultClientModule(name=StaticConfig.Module.Rpc, version=-1)
    def __init__(self):
        super(RpcClientModule, self).__init__()

    def sendRequest(self, method, data, callback=None):
        """
        发送一个rpc请求
        @param method: 静态方法
        @param data: 数据，即调用参数
        @param callback: 服务端有回复后的回调
        """
        pass
