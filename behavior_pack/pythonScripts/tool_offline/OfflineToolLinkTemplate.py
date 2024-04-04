# -*- coding: utf-8 -*-

import subprocess

import os

from pythonScripts.tool_offline import SCRIPT_ROOT

"""
该工具用于将所有模块，软连接到另一个项目，如果你是使用开源版本，无需使用此功能
"""
whitelist = {"modMain.py", "ModConfig.py", "OfflineToolLinkTemplate.py", "pack_manifest.json", "_ui_defs.json", "textures_list.json", "TutorialModule.py", "KeyPressModule.py", "CommandsModule.py", "zh_CN.lang", "entity.material"}


def linkShaderFolder(file, targetParent):
    targetPath = os.path.join(targetParent, file, "shaders")
    if os.path.exists(targetPath):
        os.removedirs(targetPath)
    ignoreGlslFolder = os.path.join(targetParent, ".glsl")
    if not os.path.exists(ignoreGlslFolder):
        os.mkdir(ignoreGlslFolder)
    for i in range(65, 91):
        vol = chr(i) + ':\MCStudioDownload\game\MinecraftPE_Netease'
        if os.path.isdir(vol):
            files = os.listdir(vol)
            files = filter(lambda f: os.path.isdir(os.path.join(vol, f)), files)
            if len(files) > 0:
                files.sort(reverse=True)
                versionFolder = files[0]
                glslPath = os.path.join(vol, versionFolder, "data\shaders\glsl")
                if os.path.isdir(glslPath):
                    print "found game file in ", glslPath
                    dispatchCmd('mklink /J "%s" "%s"' % (targetPath, glslPath))
                    dispatchCmd(["@echo off", chr(i) + ":", "cd " + targetParent, "svn propset svn:ignore shaders ./"])
                    dispatchCmd(["@echo off", chr(i) + ":", "cd " + targetParent, "svn propset svn:ignore .clang-format ./"])
                    dispatchCmd(["@echo off", chr(i) + ":", "cd " + os.path.join(targetParent), "svn propset svn:ignore .glsl ./"])

                    return
    print "[ERROR]no game file found!!!!!!"


def process(file, sourceParent, targetParent):
    # print file, sourceParent, targetParent
    if file in whitelist or file.endswith(".pyc"):
        return
    if file == "glsl" and sourceParent.endswith("shaders"):
        linkShaderFolder(file, targetParent)
        return
    targetPath = os.path.join(targetParent, file)
    sourcePath = os.path.join(sourceParent, file)

    if os.path.isfile(sourcePath):
        if os.path.exists(targetPath):
            # print "del", targetPath
            os.remove(targetPath)
        dispatchCmd('mklink /h "%s" "%s"' % (targetPath, sourcePath))
    else:
        if not os.path.exists(targetPath):
            os.mkdir(targetPath)
        for f in os.listdir(sourcePath):
            process(f, sourcePath, targetPath)


def dispatchCmd(cmds):
    if type(cmds) != list:
        res = subprocess.Popen(cmds, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        message, error = res.communicate()
        code = res.returncode
    else:
        res = subprocess.Popen("cmd.exe", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, )
        message, error = res.communicate("\n".join(cmds) + "\n")
        code = res.returncode
    if code:
        print "[ERROR]", cmds, error.decode("gbk")  # ,message.decode("gbk")
    else:
        print message.decode("gbk"),  # 由于系统编码问题，进行一次解码


if __name__ == "__main__":
    sourcePath = raw_input('请输入源项目的脚本路径，如D:\ProjectsPython\sample\\behavior_pack\pythonScripts\n')
    if len(sourcePath) == 0:
        sourcePath = "D:\OneDrive\ProjectsPython\sample\\behavior_pack\pythonScripts"
    while not os.path.exists(sourcePath) or not os.path.isdir(sourcePath):
        sourcePath = raw_input("项目路径不存在！请重新输入！")
    sourcePath = os.path.abspath(sourcePath)
    pwd = SCRIPT_ROOT
    for folder in os.listdir(sourcePath):
        process(folder, sourcePath, pwd)

    sourceResourcePath = os.path.abspath(os.path.join(sourcePath, os.path.pardir, os.path.pardir, "resource_pack"))
    targetResourcePath = os.path.abspath(os.path.join(pwd, os.path.pardir, os.path.pardir, "resource_pack"))
    for folder in os.listdir(sourceResourcePath):
        # print folder
        process(folder, sourceResourcePath, targetResourcePath)
