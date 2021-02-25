#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on '2015/11/11'
@author = 'zhangben'

'''
import maya.mel as mel
import maya.cmds as mc
from pymel.core import *
import re, os, sys
def rm_skyBall():
    sky_ball_rf = ur'\\file-cluster\GDC\Projects\MiniTiger\Project\scenes\sets\s900001SkyBall\master\mi_s900001SkyBall_h_ms_anim.mb'
    if sky_ball_rf in listReferences():
        ins_skyBall_rn = system.FileReference(pathOrRefNode = sky_ball_rf)
        ins_skyBall_rn.remove()
        print "================天空球参考已经移除 - - ！================"
def mi_selChr_AddfacialAnimCame():
    find_head_ctrls = []
    for eachSel in selected():
        if eachSel.stripNamespace().nodeName() == u'head_ctrl':find_head_ctrls.append(eachSel)
        else:
            try:
                find_head_ctrls.append(PyNode(u'%shead_ctrl' % (eachSel.namespace())))
            except:
                error(u'你选择了没有头部控制器的物体，可能不是角色哦')
    for each_h_ctrl in find_head_ctrls:
        mi_create_facialCame(each_h_ctrl)
def mi_create_facialCame(head_ctrl):
    #head_ctrl = selected()[0]
    chr_name = head_ctrl.name().split(':')[0]
    chr_facialCamName = u'%s_facialAnimCam' % chr_name
    facialAnimCams = ls(u'%s*'%chr_facialCamName)
    #delete(facialAnimCams)
    if not facialAnimCams:
        facialAnimCams = camera(name=chr_facialCamName)
        tem_constraint = parentConstraint(head_ctrl,facialAnimCams[0],mo=False)
        delete(tem_constraint)
        facialAnimCams[0].setParent(head_ctrl)
        xform(facialAnimCams[0],r=True,t=(0,10,40))
        facialAnimCams[1].renderable.set(0)
        facialAnimCams[1].renderable.lock(1)
    get_focPanel = getPanel(wf=True)
    mel.eval("lookThroughModelPanel %s %s" % (facialAnimCams[1],get_focPanel))
def find_root_joint(boneList):#=======用到递归函数，找到 一个或一个以上的head头部骨骼的root =====
    rootBones_intermediate = []
    rootBones_stor = boneList
    for each_hj in boneList:
        other_ls=[]
        other_ls.extend(boneList)
        other_ls.remove(each_hj)
        for each_other in other_ls:
            if each_other.hasParent(each_hj):rootBones_intermediate.append(each_hj)
    rootBones = [rootBones_intermediate[i] for i in range(len(rootBones_intermediate)) if rootBones_intermediate[i] not in rootBones_intermediate[:i]]
    if not rootBones: return rootBones_stor
    else: return find_root_joint(rootBones)


