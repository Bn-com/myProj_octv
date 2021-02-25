#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/9/14:15:17'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import re, os, sys
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

def ben_text2noTex(stor_path = os.path.abspath(ur'D:/temp_info/a2_set_tex2noTex')):
    if not os.path.isdir(stor_path):os.makedirs(stor_path)
    fn_read = mc.file(shn=True,q=True,sn=True)
    try:
        import Other.studio_a2.scripts.common.do3_modelAssignLambert as domal
        reload(domal)
        domal.do3_modelAssignLambert(delUnuse=True)
        fn_new_full = os.path.join(stor_path,fn_read)
        mc.file(rn=fn_new_full)
        pm.saveFile()
        print("The notexture File Saved Succeed!!   ::::{}".formath(fn_new_full) )
    except:
        Warning("There something wrong happened by change lambert shader on file :::{}".format(fn_read))
