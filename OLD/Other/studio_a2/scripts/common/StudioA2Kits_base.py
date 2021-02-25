#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/10/9:15:52'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import re, os, sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

class StudioA2Kits_base(object):
    def __init__(self):
        pass
    def im_all_refs(self):
        for eachRef in pm.listReferences():
            eachRef.load(force=True)
            eachRef.importContents()