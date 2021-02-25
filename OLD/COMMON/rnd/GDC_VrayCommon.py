# -*- coding: utf-8 -*-
# 【通用】【Vray 渲染】
#  Author : 韩虹
#  Data   : 2016
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

import re
class GDC_VrayCommon(object):
    def __init__(self):
        pass
        #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray,Load，并设为当前渲染器】
    #  Author  : 韩虹
    #  Data    : 2016_02_16
    #------------------------------#
    def VrayLoading(self):
        print (u'===============!!!Start 【%s】!!!===============' % (u'Vray设置'))
        print 'Working...'
        mc.setAttr('defaultRenderGlobals.imageFormat', 7)
        try:
           mel.eval('loadPlugin "vrayformaya"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray设置】
    #  Author  : 韩虹
    #  Data    : 2015_01_26
    #------------------------------#
    def VraySettings(self,resW=1280,resH=720,format=1,startFrame=1,endFrame=75,type=1):
        #设置当前渲染器为vray渲染器
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'vray', type='string')
        mc.setAttr('vraySettings.imageFormatStr',1,type='string')
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
        #nj2017前期渲染设置
        if type==1:
            mc.setAttr ('vraySettings.samplerType',2)
            mc.setAttr ('vraySettings.minShadeRate',1)
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray材质球创建】
    #  Author  : 韩虹
    #  Data    : 2016_02_16
    #------------------------------#
    def VrayShaderAssign(self,shaderType='WireFrame',transparency=0):
        meshs=mc.ls(sl=1,l=1)
        if transparency==0:
            Shade='SHD_'+shaderType+'_vray'
            SG=Shade+'SG'
            #删除已有材质球和SG节点
            if mc.objExists(Shade):
                mc.delete(Shade)
            if mc.objExists(SG):
                mc.delete(SG)
            #创建新材质球和SG节点
            if shaderType=='WireFrame':
                mc.shadingNode('VRayMtl', asShader=True,n=Shade)
            else:
                mc.shadingNode('VRayMtl', asShader=True,n=Shade)
            mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SG)
            mc.connectAttr(('%s.outColor' % Shade),('%s.surfaceShader' % SG))
            if meshs:
                mc.sets(meshs,e=1, forceElement = SG)
            else:
                pass
            if shaderType=='WireFrame':
                #节点
                VRayEdge='VRayEdges'
                #创建节点
                if mc.objExists(VRayEdge):
                    mc.delete(VRayEdge)
                #创建节点
                #mc.shadingNode('aiUtility', asShader=True,n=Shade)
                mc.shadingNode('VRayEdges',asUtility=True,n=VRayEdge)
                #shade参数设置
                #VRayEdge设置
                mc.setAttr((VRayEdge+".edgesColor"), 0,0,0,type='double3')
                mc.setAttr((VRayEdge+".backgroundColor"), 0.5,0.5,0.5,type='double3')
                mc.setAttr((VRayEdge+".pixelWidth"),0.5)

                #连接节点
                #VRayEdge 与Shade连接
                mc.connectAttr((VRayEdge+'.outColor'),(Shade+'.diffuseColor'),f=1)
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【前期发客户固有层创建】
    #  Author  : 韩虹
    #  Data    : 2016_02_17
    #------------------------------#
    def nj_VrayPreLayer(self):
        self.VrayLoading()