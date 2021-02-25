# -*- coding: utf-8 -*-
# 【通用】【sw自动分层工具】
#  Author : 虞丰盛
#  Data   : 2018
import  maya.cmds as mc
import maya.mel as mel
import time
import os

class yu_swAutoComTools(object):

    def __init__(self):
        # 切换渲染器
        mc.loadPlugin('redshift4maya',qt=1)
        try:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'mayaSoftware', type='string')
        except:
            pass
        try:
            mc.setAttr('defaultRenderGlobals.currentRenderer', 'redshift', type='string')
        except:
            pass
        mel.eval("source \"redshiftCreateOutputTab.mel\"")
        mel.eval("redshiftGetRedshiftOptionsNode(true);")

    def swAutoComTools(self):

        fileName=mc.file(q=1,sn=1,shn=1)
        if not 'Ani' in fileName:
            mc.error(u'请在SW动画文件里使用该插件！！！！')
        ch_Layers=mc.ls('CH_*',type='renderLayer')
        if not ch_Layers:
            mc.file('Z:/SW_S3_Pipeline/03_Main-Production/06_LightingSet/RS_LIGHT_V1.0/RenderLayer/RS_RenderLayer_V2.mb',i=True,type='mayaBinary',force=True,ignoreVersion=True)
        ch_Layers=mc.ls('CH_*',type='renderLayer')
        bg_Layers=mc.ls('BG_*',type='renderLayer')
        chObjs=mc.ls('ch_*:MODEL',type='transform')
        setObjs=mc.ls('bg_*:MODEL',type='transform')
        layerObjs=[]
        for ch_Layer in ch_Layers:
            if 'CH_AOP' in ch_Layer:
                print u'－－－－－添加角色和场景至%s渲染层－－－－－－' %ch_Layer
            else:
                print u'－－－－－添加角色至%s渲染层－－－－－－' %ch_Layer
            layerObjs=mc.editRenderLayerMembers(ch_Layer,query=True)
            #判断是否已经添加了角色，如果是就不再添加
            if layerObjs:
                for chObj in chObjs:
                    if chObj in layerObjs:
                        continue 
                    else:
                        mc.editRenderLayerMembers(ch_Layer,chObj,noRecurse=True)
            else:
                mc.editRenderLayerMembers(ch_Layer,chObjs,noRecurse=True)
            if 'CH_AOP' in ch_Layer and not layerObjs:
                mc.editRenderLayerMembers(ch_Layer,setObjs,noRecurse=True)
            elif 'CH_AOP' in ch_Layer and not 'SET' in layerObjs:
                mc.editRenderLayerMembers(ch_Layer,setObjs,noRecurse=True)
        for bg_Layer in bg_Layers:
            print u'－－－－－添加场景至%s渲染层－－－－－－' %bg_Layer
            layerObjs=mc.editRenderLayerMembers(bg_Layer,query=True)            
            #判断是否已经添加了场景，如果是就不再添加
            if layerObjs:
                for setObj in setObjs:
                    if chObj in layerObjs:
                        continue 
                    else:            
                        mc.editRenderLayerMembers(bg_Layer,setObj,noRecurse=True)
            else:
                mc.editRenderLayerMembers(bg_Layer,setObjs,noRecurse=True)

        mc.select('CH_COL')
        MainLight=mc.ls('Main_LIGHT')
        if not MainLight:
            mc.file('Z:/SW_S3_Pipeline/03_Main-Production/06_LightingSet/RS_LIGHT_V1.0/Main_Light_V1.3.mb',i=True,type='mayaBinary',force=True,ignoreVersion=True)
      
        mc.select('CH_COL')
        #切换成选择的渲染层
        mc.editRenderLayerGlobals(currentRenderLayer = 'CH_COL')
        cmd='redshiftChangeGlobalShader redshiftEnvironment_CH1_3 "environment"'
        try:
            mel.eval(cmd)
        except:
            pass
            

        mc.select('BG_COL')
        mc.editRenderLayerGlobals(currentRenderLayer = 'BG_COL')
        cmd='redshiftChangeGlobalShader redshiftPhysicalSky_BG1_3 "environment"'
        try:
            mel.eval(cmd)
        except:
            pass

        
        tmpPath='D:/TempInfo/sw_comp'
        #判断tmpPath目录是否存在，如果没有就创建
        if os.path.exists(tmpPath)==False:
            os.makedirs(tmpPath)
        
        tmpFileName=fileName.split('Ani')
        desFileName=tmpPath+'/'+tmpFileName[0]+'Ren_v01.mb'
        mc.file(rename=desFileName)
        mc.file(force=1,s=1)
        print desFileName.replace('/','\\'),