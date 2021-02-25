#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/11/7:11:26'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

import maya.cmds as mc
import pymel.core as pm

class StudioA2Kits_Rnd(object):
    def __init__(self):
        pass
    @staticmethod
    def batch_Set_RedShiftID_attr():
        if not mc.pluginInfo('redshift4maya',l=True,q=True):
            mc.loadPlugin('redshift4maya')

        sel_objs = pm.selected()

        result = mc.promptDialog(title='RedShift ID Numeber',message='Enter ID Number:',
                button=['OK', 'Cancel'],
                defaultButton='OK',
                cancelButton='Cancel',
                dismissString='Cancel')
        if result == 'OK':
            ID_num = int(mc.promptDialog(q=True,t=True))

        for eachObj in sel_objs:
            get_shp = eachObj.listRelatives(ni=True,type='mesh')
            if get_shp:
                get_shp[0].attr('rsObjectId').set(ID_num)