#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/8/16:11:30'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import re, os, sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

class StudioA2Kits_anim(object):
    """
    A2 studio kits : animation part
    """
    def __init__(self):
        pass
    def remove_unk_plgs(self):
        all_unk_plugins = pm.unknownPlugin(list=True,q=True)
        if not all_unk_plugins:return
        for each_unk_plg in all_unk_plugins:
            if each_unk_plg not in ['mtoa','vrayformaya']:
                try:
                    pm.unknownPlugin(each_unk_plg,r=True)
                    print("+++++Plugin :: {} Removed Succeed!!+++++".format(each_unk_plg))
                except:
                    pm.warning("===========UNKNOWN PLUGIN::{} PERHAPERS COME FROME REFERENCE FILE=============".format(each_unk_plg))