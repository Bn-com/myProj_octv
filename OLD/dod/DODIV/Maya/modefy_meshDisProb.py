#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-92013

@author: zhangben
'''
import maya.cmds as mc
import re,os
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp

def do_modefy_meshDisWrong():

    primaryObj_generator=(dod for dod in mc.ls(v=True,typ=u'mesh',ni=True,l=True) if mc.listConnections(u'%s.inMesh'%dod,d=True,t = u'polyTransfer'))
    
    for eachMesh in primaryObj_generator:
        polyTrans_node =  mc.listConnections(u'%s.inMesh'%eachMesh,d=True,t = u'polyTransfer')[0]
        mc.setAttr(u'%s.vertices'%polyTrans_node,1)
        mc.setAttr(u'%s.vertices'%polyTrans_node,0)


if __name__ == "__main__":
    do_modefy_meshDisWrong()