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
        mel.eval('source "vrayRegisterRenderer"')
        mel.eval('vrayCreateVRaySettingsNode()')
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Vray设置】
    #  Author  : 韩虹
    #  Data    : 2015_01_26
    #------------------------------#
    def VraySettings(self,resW=1280,resH=720,format=1,startFrame=1,endFrame=75,type=1):
        self.VrayLoading()
        #设置当前渲染器为vray渲染器
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        try:
            mc.setAttr('vraySettings.imageFormatStr',1,type='string')
        except:
            pass

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
    def VrayShaderAssign(self,meshs,shaderType='wf',transparency=0):
        #self.VrayLoading()
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
            if shaderType=='wf':
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
            if shaderType=='uv':
                image='//file-cluster/gdc/Projects/Ninjago/Ninjago_scratch/Modeling/prop/pe0012006001RonanMech/daily/UV_tex.TGA'
                fil='uvFile'
                if mc.objExists(fil):
                    mc.delete(fil)
                fi=mel.eval('createRenderNodeCB -as2DTexture "" file ""')
                mc.rename(fi,fil)
                mc.setAttr((fil+'.fileTextureName'), image, type='string')
                #连接节点
                mc.connectAttr((fil+'.outColor'),(Shade+'.diffuseColor'),f=1)
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【前期发客户固有层创建】
    #  Author  : 韩虹
    #  Data    : 2016_02_17
    #------------------------------#
    def nj_VrayPreLayer(self):
        wireLayer='wf'
        txLayer='tx'
        uvLayer='uv'
        #self.VrayLoading()
        #self.VraySettings(resW=1280,resH=720,format=1,startFrame=1,endFrame=75,type=1)
        meshs=[]
        objs=mc.ls(type='mesh',l=1)
        for obj in objs:
            mesh=mc.listRelatives(obj,p=1,type = 'transform',f=1)
            if mesh:
                mesh=mesh[0]
                meshs.append(mesh)
        try:
            mc.setAttr("defaultRenderLayer.renderable", 0)
        except:
            pass
        #创建wf层
        for layer in [wireLayer,txLayer,uvLayer]:
            mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
            if mc.objExists(layer):
                mc.delete(layer)
            mc.createRenderLayer(meshs,name=layer, noRecurse=1, makeCurrent=1)
            self.VrayShaderAssign(meshs,layer,0)
        print '==========================================='
        try:
            mc.setAttr("defaultRenderLayer.renderable", 0)
        except:
            pass
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【前期发客户旋转角色或道具】
    #  Author  : 韩虹
    #  Data    : 2016_02_17
    #------------------------------#
    def nj_PreAni(self):
        loc='locator_Pre'
        if mc.objExists(loc):
            mc.delete(loc)
        loca=mc.CreateLocator()
        loc=mc.rename(loca,loc)
        mc.setKeyframe((loc+'.rotateY'),v=1,t=1)
        mc.setKeyframe((loc+'.rotateY'),v=360,t=25)
        mc.keyTangent((loc+'.rotateY'),e=1,itt='linear', ott='linear',time=(1,25))
        objs=mc.ls('*MODEL',tr=1,l=1)+mc.ls('*:MODEL',tr=1,l=1)
        if objs:
            for obj in objs:
                try:
                    mc.parentConstraint(loc,obj)
                except:
                    mc.warning(u'===============[%s]无法加约束，请检查==============='%obj)
                    mc.error(u'===============[%s]无法加约束，请检查==============='%obj)
        else:
            mc.warning(u'======================文件中没有MODEL组，请检查文件============')
            mc.error(u'======================文件中没有MODEL组，请检查文件============')
        print u'==============MODEL组已旋转360度==============='
        return 0

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【NJ2017】【客户要求统一修角色bump值】
    #  Author  : 韩虹
    #  Data    : 2016_06_08
    #------------------------------#
    def nj_MatModifBump(self):
        count = 0
        mshades=['PlasticBlack','PlasticYellow','PlasticWhite']
        shades=mc.ls(type='VRayMtl',l=1)
        shadeList=[]
        if shades:
            for shade in shades:
                for  ms in mshades:
                    if ms in shade:
                       shadeList.append(shade)
        if shadeList:
            for sha in shadeList:
                if mc.getAttr(sha+'.bumpMult') != 0.0001:
                    mc.setAttr((sha+'.bumpMult'),0.0001)
                    count = count + 1
        return count
