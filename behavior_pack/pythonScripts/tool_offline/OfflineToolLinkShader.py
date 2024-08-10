# -*- coding: utf-8 -*-
# @Author  : Ree
import os

from pythonScripts.tool_offline import RESOURCE_ROOT
from pythonScripts.tool_offline.OfflineToolLinkTemplate import linkShaderFolder

"""
该工具用于链接原版的shader文件夹，方便vscode处理import语句
注意，当mcstudio更新改名后，软连接会失效，可能会导致游戏无法正常运行测试，删除shaders链接即可(OfflineToolBeforeRelease.py已包含此功能)
"""
if __name__ == '__main__':
    targetResourcePath = os.path.abspath(os.path.join(RESOURCE_ROOT, "shaders"))
    print(targetResourcePath)

    linkShaderFolder("glsl", targetResourcePath)
