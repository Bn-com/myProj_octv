#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '11:16'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import re, os, sys
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
def lion_ren_camNM_for_an():
    sc_nm = sceneName().namebase
    sc_nm_spl = u''
    if sc_nm:sc_nm_spl = sc_nm.split(u'_')
    shot_label = u'_'.join(sc_nm_spl[1:3])
    try:
        sel_cam = selected()[0]
    except:
        error(u'++++++++++++请选择要重命名的camera++++++++++++++++++++++')
    sel_cam_shape = [ea_c for ea_c in sel_cam.getChildren() if ea_c.nodeType()==u'camera'][0]
    sel_cam.rename(u'cam_%s'%shot_label,ignoreShape=True)
    sel_cam_shape.rename(u'cam_%sShape'%shot_label)
    print u'=============rename camera name match Scene\'sName============================='