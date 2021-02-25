#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = maya_openlegacy_start
__author__ = zhangben 
__mtime__ = 2020/8/25 : 9:08
__description__: 

    code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
"""
import sys,os,subprocess
sys.path.append(r"F:\Development\octProj\oct\maya_sixteen\Python\OCT_Pipeline\scripts\utility")
import Kits

k=Kits.Kits()
maya19_root = k.getAppRootPath('Autodesk Maya 2019')[0]
maya19_exe = "{}/bin/maya.exe".format(maya19_root)
MAYA_ENABLE_LEGACY_VIEWPORT = 1
os.putenv('MAYA_ENABLE_LEGACY_VIEWPORT','1')
os.popen(maya19_exe)