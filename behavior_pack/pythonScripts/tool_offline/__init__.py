# -*- coding: utf-8 -*-
# @Author  : Ree
import os


def _find_resource_folder(root_path):
    for root, dirs, files in os.walk(root_path):
        for name in dirs:
            if 'resource' in name.lower():
                return os.path.join(root, name)
    return None


SCRIPT_ROOT = os.path.abspath(os.path.join(os.curdir, os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(os.curdir, os.pardir, os.pardir, os.pardir))
BEHAVIOR_ROOT = os.path.abspath(os.path.join(os.curdir, os.pardir, os.pardir))
RESOURCE_ROOT = _find_resource_folder(PROJECT_ROOT)
