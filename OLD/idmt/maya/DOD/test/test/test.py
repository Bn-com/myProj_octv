#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-252013

@author: zhangben
'''
import maya.cmds as mc
import os,re
import idmt.maya.DOD.DODIV.Maya.do4_batchPreviewRender as dobpr
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp

def saveAsTestFile():
#===============================================================================
# #=====load all reference file================================
#    allRNIterator = (eachRN for eachRN in mc.ls(type=u'reference') if mc.listConnections(u'%s.message'%eachRN,d=True))
#    
#    for eachRN in allRNIterator:
#        if not mc.referenceQuery(eachRN,isLoaded=True):
#            rf_file = mc.referenceQuery(eachRN,f=True)
#            mc.file(rf_file,lr=eachRN)
# 
# #====set all camera renderable off===================
#===============================================================================
    
    objsIterator= (d for d in mc.ls(v=True,typ=[u'mesh',u'nurbsSurface'],ni=True,l=True) if mc.getAttr("%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)))
    objs = []
    for ec_pri in objsIterator:
        objs.append(ec_pri)
    dobpr.create_previewRenderLayer(objs)
    
    fileName = mc.file(q=True,sn=True)
    fn_split = os.path.split(fileName)
    
    mc.file(rn=u'%s/re_%s'%(fn_split[0],fn_split[1]))
    mc.file(save=True)


if __name__=="__main__":
    saveAsTestFile()
    
