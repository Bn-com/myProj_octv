#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2016/5/27:12:25'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''

from pymel.core import *


def Lion_SHrl_Create(self):
    print (u'===============!!!Start !!!===============SH===' )
    print 'Working...'
    #self.ArnoldALLDelete('aiAOV')
    # 物体
    objs = self.LionRLObjectsTList()
    refCHR = objs[0]
    refPROP = objs[1]
    refSET = objs[2]
    rlObjs = []
    layerName=''
    if refCHR or refPROP:
        rlObjs = refCHR + refPROP
        layerName = 'SH'
    # 灯光
    #CHR_light= '//file-cluster/gdc/Projects/LION/Lion_Scratch/TD/charlight.ma'
    CHR_light= 'Z:/Projects/LION/Lion_Scratch/render/char_light/Lion_CHRLT_new.mb'
    lightfile=CHR_light
    if mc.ls('CHR_light'):
        mc.delete('CHR_light')
    mc.file(lightfile, i=1)
    # GDList=gdc_Attrlist(type='mesh',attrtype='GD')
    # if GDList:
    #     for obj in GDList:
    #         shapes=mc.listRelatives(obj,s=1,f=1)
    #         for shape in shapes:
    #             mc.setAttr((shape+'.primaryVisibility'),0)
    lightGRP = []
    if mc.ls('charlight_meshKey_Light'):
        lightGRP=mc.ls('charlight_meshKey_Light')
    self.NorCommonSetting('tif','mesh')
    mc.setAttr('defaultRenderGlobals.outFormatControl', 0)
    # 创建RenderLayer
    if mc.ls(layerName):
        mc.delete(layerName)
        # 要加灯光
    mc.createRenderLayer((refCHR+refPROP+refSET+lightGRP), name=layerName, noRecurse=1, makeCurrent=1)
    self.ArnoldAOVCreat('AO')
    #self.ArnoldAOVCreat('specular')
    #self.ArnoldAOVCreat('Shadow')
    self.nor_SmoothSet()
    self.camImoprt()
    self.zmRLCamSetting()
    self.NorCommonSetting('tif','mesh')
    for eachOne_chrMesh in rlObjs:
        rndShp_nd = PyNode(eachOne_chrMesh).getChildren(ni=True)
        if rndShp_nd:
            rndShp_nd[0].castsShadows.set(1)
            rndShp_nd[0].primaryVisibility.set(0)
            rndShp_nd[0].receiveShadows.set(0)
    for eachOne_set in refSET:
        rndShp_nd = PyNode(eachOne_set).getChildren(ni=True)
        if rndShp_nd:
            rndShp_nd[0].castsShadows.set(0)
            rndShp_nd[0].primaryVisibility.set(1)
            rndShp_nd[0].receiveShadows.set(1)
    #回master层
    mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
    mc.setAttr("defaultRenderLayer.renderable", 0)
    self.Lion_FileSave('INTER','shadow')
    print (u'===============!!!Done !!!===============SHADOW' )
    print '\n'
    return 0
