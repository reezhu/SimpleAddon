# -*- coding: utf-8 -*-
import glob
import json
import uuid

import os

from pythonScripts.tool_offline import PROJECT_ROOT, BEHAVIOR_ROOT, RESOURCE_ROOT

"""
该工具用于
上线前删除编辑器默认生成的垃圾文件
修改uuid
扫描textures/ui/common目录，加入启动缓存资源列表
"""
JSON_SETTING = {"separators": (',', ': '), "sort_keys": True, "indent": 2}
# 垃圾文件列表
uselessFile = [
    "resource_pack/textures/blocks/custom_brah.png",
    "resource_pack/textures/blocks/custom_dirt.png",
    "resource_pack/models/skeleton/invisible_bind_skeleton.json",
    "resource_pack/textures/sfxs/custom_sun.png",
    "resource_pack/textures/items/custom_apple.png",
    "resource_pack/models/effect/_effect.json",
    "resource_pack/models/bind/_bind.json",
    # "resource_pack/pack_icon.jpg",
    # "behavior_pack/pack_icon.jpg",
    "world_behavior_packs.json",
    "world_resource_packs.json",
    "editor.name",
    "studio.json",
    "world_icon.jpeg",
]
# 需要缓存的贴图
cacheFile = [
    "textures/items/*.png",
    "textures/blocks/*.png",
    "textures/ui/common/*.png",
]


def recursiveDel(parent):
    for p in os.listdir(parent):
        file = os.path.join(parent, p)
        if os.path.isdir(file):
            recursiveDel(file)
    if len(os.listdir(parent)) <= 0 and not (parent.endswith("textures") or parent.endswith("entities") or parent.endswith("entity")):
        print "delete rubbish", parent
        os.rmdir(parent)


def randomUuid():
    for folder in os.listdir(path):
        p = os.path.join(path, folder, "pack_manifest.json")
        if os.path.exists(p):
            with open(p) as file:
                j = json.load(file)
                j["header"]["uuid"] = str(uuid.uuid4())
                for ls in j["modules"]:
                    ls["uuid"] = str(uuid.uuid4())
                with open(p, "w") as f:
                    json.dump(j, f, **JSON_SETTING)
        if os.path.isdir(os.path.join(path, folder)) and not folder.startswith("."):
            recursiveDel(os.path.join(path, folder))


def deleteRubbish():
    for f in uselessFile:
        uselessPath = os.path.join(path, f)
        if os.path.exists(uselessPath):
            os.remove(uselessPath)
    blocksJson = os.path.join(path, "resource_pack/blocks.json")
    if os.path.exists(blocksJson):
        with open(blocksJson, "r") as f:
            js = json.load(f)
        if len(js) <= 1:
            os.remove(blocksJson)
    blocksJson = os.path.join(path, "resource_pack/textures/terrain_texture.json")
    if os.path.exists(blocksJson):
        with open(blocksJson, "r") as f:
            js2 = json.load(f)
        if len(js2["texture_data"]) < 1:
            os.remove(blocksJson)
    blocksJson = os.path.join(path, "resource_pack/models/netease_models.json")
    if os.path.exists(blocksJson):
        with open(blocksJson, "r") as f:
            js3 = json.load(f)
        if len(js3) < 1:
            os.remove(blocksJson)
    shaderFolder = os.path.join(path, "resource_pack/shaders/glsl/shaders")
    if os.path.exists(shaderFolder):
        shaderFolder = os.path.abspath(shaderFolder)
        os.removedirs(shaderFolder)


def listTextures():
    resource_path = os.path.join(path, "resource_pack/")
    textures = []
    j = []
    for f in cacheFile:
        textures += glob.iglob(os.path.join(resource_path, f))
    for texture in textures:
        bn = os.path.splitext(os.path.basename(texture))[1]
        tx = texture.replace(bn, "").replace(resource_path, "").replace("\\", "/")
        j.append(tx)
    with open(os.path.join(resource_path, "textures/textures_list.json"), "w") as f:
        json.dump(j, f, **JSON_SETTING)


blacklist = [
    "entity/player.entity.json"
]


def duplicateCheck():
    for path in blacklist:
        if os.path.exists(os.path.join(RESOURCE_ROOT, path)):
            print "ERROR:为了避免mod之间冲突，将会删除", os.path.join(RESOURCE_ROOT, path)
            break


if __name__ == "__main__":
    path = PROJECT_ROOT

    deleteRubbish()
    randomUuid()
    listTextures()
    duplicateCheck()
    if os.path.exists(os.path.join(BEHAVIOR_ROOT, "pythonScripts")):
        print "WARNING: 你需要重命名pythonScripts以避免自测时组件之间的冲突！！！！！！！！!"
