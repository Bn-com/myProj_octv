#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'maya_del_unkonws'    
__author__ = zhangben
__mtime__ = 2018/12/14:20:01
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import pymel.core as pm

for each in pm.unknownPlugin(q=True, l=True):
    pm.unknownPlugin(each, r=True)

for each in pm.ls(type='unknown'):
    pm.lockNode(each, lock=False)
    pm.delete(each)