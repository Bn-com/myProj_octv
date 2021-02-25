#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-8-202014

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
from pymel.core import *
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp


class dod_prep_kit(object):

    def __init__(self):
        pass

    def convert_to_relative_path(self, path=""):
        folder = os.path.dirname(__file__)
        print folder

    def modefy_cacheFile_cachePath(self):  # ==========修正有缓存的植物，缓存节点路径===================
        CF_list = mc.ls(type=u'cacheFile')
        for each_cf in CF_list:
            attr_cachePath = mc.getAttr(u'%s.cachePath' % each_cf)
            attr_cachePath = mc.getAttr(u'%s.cachePath' % CF_list[2])
            if attr_cachePath.find(ur'Z:/Projects/DiveollyDive4') != -1:
                path_stuff = attr_cachePath.replace(ur'Z:/Projects/DiveollyDive4', ur'//file-cluster/GDC/Projects/DiveollyDive5')
                mc.setAttr(u'%s.cachePath' % each_cf, path_stuff, type=u'string')
    def set_selObj_opaqueAttr(self, attr_v):
        selObjes = mc.ls(sl=True, l=True)
        for each in selObjes:
            child = mc.listRelatives(each, s=True, type=u'mesh', c=True, ni=True, f=True)
            if child != None and mc.attributeQuery(u'aiOpaque', node=child[0], exists=True):
                mc.setAttr(u'%s.aiOpaque' % child[0], attr_v)
    def set_ai_proxy_disMode(self): #===================arnold渲染代理显示模式的开关函数============================
        state = selected()[0].getChildren()[0].mode.get()
        for eachSel in selected():
            if  state == 0:
                eachSel.getShape().mode.set(6)
                eachSel.getParent().getChildren()[0].visibility.set(0)
            else:
                eachSel.getShape().mode.set(0)
                eachSel.getParent().getChildren()[0].visibility.set(1)
 #========添加标记属性窗口=============================================  
    def execute_add_bt_cmd(self,behavior):
        if    radioButton(u'gd_rb',q=True,sl=True):self.do_add_spec_attr(u'GD',behavior)
        elif radioButton(u'fa_rb',q=True,sl=True):self.do_add_spec_attr(u'Fore',behavior)
        elif radioButton(u'tr_rb',q=True,sl=True):self.do_add_spec_attr(u'Translucid',behavior)
   #     elif radioButton(u'tr_rb',q=True,sl=True):self.do_add_spec_attr(u'translucid',behavior)
    def do_add_spec_attr(self,attr_longName = u'GD',behavior = u'add',attr_type = u'bool'):
        if behavior == u'add':
            for each in selected():
                if each.type()!= u'transform': each = each.getParent()
                if not each.hasAttr(attr_longName):  each.addAttr(attr_longName,at=u'bool',k=True,dv=True)
        elif behavior == u'minus':
            for each in selected():
                if each.hasAttr(attr_longName): each.deleteAttr(attr_longName)
        elif behavior == u'select':
            select(cl=True)
            allTrans = [eachTran for eachTran in mc.ls(transforms = True) if mc.attributeQuery(attr_longName,n = eachTran,exists=True)]
            if allTrans:
                try:
                    far_objs = [eachOne for eachOne in allTrans if PyNode(eachOne).longName().find(u'MODEL') != -1]
                    mc.select(far_objs)
                except:
                    mc.select(allTrans)
                    warning(u'===标记%s物体没有在MODEL组下' % attr_longName)
            else:
                warning(u'=========场景里没有标记为%s的物体============' % attr_longName)
#====================================================================