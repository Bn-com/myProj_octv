# -*- coding: utf-8 -*-
'''
@Title:file_name
Created on 2014年9月23日
@author: zhangben
@Description:todo
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
import idmt.maya.ShunLiu_common.csl_RenderAutoCommons
import idmt.pipeline.project
from pymel.core import *
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
from fileinput import filename
from pymel.core.general import PyNode
#from pip._vendor.distlib.util import split_filename
#from idmt.maya.Ninjago.zzjAnimCleanupScene import fileName_split
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
reload(sk_hbExportCam)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)
from idmt.maya.ShunLiu_common import csl_checkin
reload(csl_checkin)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from  idmt.maya.ShunLiu_common import csl_RenderAutoCommons
reload(csl_RenderAutoCommons)
from idmt.maya.DOD.scripts import dod_RenderArnoldLayer 
reload(dod_RenderArnoldLayer)
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp
reload(docp)
from idmt.maya.DOD.scripts import dod_common_proc
reload(dod_common_proc)
class dod_Rnd_Auto_Common(object):
    ins_cslRAC = csl_RenderAutoCommons.csl_RenderAutoCommons()
    ins_dod_arnTools = dod_RenderArnoldLayer.hh_RenderArnold()
    ins_dod_com_proc = dod_common_proc.dod_common_proc()
    def __init__(self):
        pass
    def dod_RenderLayerAuto(self,shotType=2,server=1):
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================【%s】文件分层开始==========================' % FileName        
        self.ins_cslRAC.csl_RendertimeRecord()        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        userName = os.environ['USERNAME']       
        Project=shotInfo [0]
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]
        shotName=''
        LineName=''
        serPath=''
        chr_light_file_path = ''
        proj_path = sceneName()
        if fileType=='mb':
            fileTypeAll='mayaBinary'
        if fileType=='ma':
            fileTypeAll='mayaAscii'
        if shotType == 3:
            shotName=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
            LineName=shotInfo[4]+'_'+shotInfo[5]
            serPath=serverPath+'scenes/Animation/episode_'+shotInfo[1]+'/sequence_'+shotInfo[2]+'/scene_'+shotInfo[3]+'/lighting/'
        if shotType == 2: 
            shotName=shotInfo[1]+'_'+shotInfo[2]
            LineName=shotInfo[3]+'_'+shotInfo[4]
            serPath=serverPath+'scenes/Animation/episode_'+shotInfo[1]+'/scene_'+shotInfo[2]+'/lighting/'   
            chr_light_file_path = u'%sscenes/Animation/episode_%s/scene_%s/chrlight'%(serverPath,shotInfo[1],shotInfo[2])    
        tempath='E:/Info_Temp/temp/RenderLayer/'+shotInfo[1]+'/'
        #需要导出的文件名称：
        #角色文件（包括道具）
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #场景文件  
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType 
        #角色场景互动文件              
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #焦散灯光文件
        causLightName = u'%s_%s_causlight_lr_c001.%s'%(Project,shotName,fileType)
        #角色灯光文件 名字
        chrlightName=Project+'_'+shotName+'_'+'chrlight'
        #灯光雾灯文件名字
        fogLightName = u'%s_%s_foglight_lr_c001.%s'%(Project,shotName,fileType)
        #=======================================================================
        # #远景物体文件
        # setFarName = u'%s_%s_setF_lr_c001.%s'%(Project,shotName,fileType)
        #=======================================================================
        #01——载入场景
        self.ins_cslRAC.csl_RenderEnvLoad()
        #smooth设置        
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_smooth设置' % FileName)) 
        #参考判断（文件是否有角色（包含道具），场景  
        refconinfo=self.dod_refcondition()
        #=======================================================================
        # #=======================================================================
        # # #06--导出远景物体 ====优先导出后，将远景物体从场景中删除
        # #=======================================================================
        # if refconinfo[1] == 1 and refconinfo[2] == 1:
        #     far_objects = self.set_far_check()
        #     if far_objects:
        #         print u'===================!!!Start 【导出远景文件%s 】!!!=================' % setFarName
        #         mc.select(far_objects)
        #         lights_Grps = self.dod_lightInfoList(u'', True,u'set',u'RGB')
        #         mc.select(lights_Grps,add=True)
        #         mc.file(u'%s%s' % (tempath,setFarName),options = u'v=0',f=True,type = fileTypeAll,preserveReferences = True,es=True)
        #         csl_checkin.csl_checkin().csl_timeRecord()
        #         mc.delete(far_objects) #===============删除远景物体======================================
        #         print u'=======================!!! End 【%s  导出远景文件】===================' % setFarName
        #     else:
        #         print u'===================================没有远景物体======================================='
        #=======================================================================
        #02--导出焦散灯光文件
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出焦散灯光文件' % causLightName)) 
        #=======================================================================
        # #删除OTC
        # hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
        # if mc.ls('OTC_GRP'):
        #     mc.delete('OTC_GRP')
        #=======================================================================
        try:
            lightgroup=PyNode(self.dod_lightInfoList(u'',True,u'caus')[0]) # self.ins_cslRAC.csl_lightInfoList(Type='chr',lightType='group')[0]
        except:
            mc.error( "No caustic light" )             
        lightgroup.visibility.set(1)
        for each_causLight in lightgroup.getChildren():#======设置焦散灯贴图file节点的帧数便宜=====================
            connect_node = each_causLight.getChildren()[0].listConnections(type=u'aiGobo')
            if connect_node and connect_node[0].slidemap.isConnected():
                fram_offset_value = PyNode( 'defaultRenderGlobals').startFrame.get() - 1001
                connect_node[0].listConnections(type = u'file')[0].frameOffset.set(fram_offset_value)
        select(lightgroup)
        PyNode(lightgroup).setParent(world=True)
        mc.file((tempath+causLightName),options='v=0',f=1,type=fileTypeAll,es=1)               
        print (u'===============!!!End 【%s】!!!===============' % (u'%s_已导出焦散灯光文件' % causLightName))
        delete(lightgroup)
        #03--导出角色文件 
        if refconinfo[0]==1:       
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))        
            mc.select(self.ins_cslRAC.csl_GroupSelect()[0])
            if self.ins_cslRAC.csl_GroupSelect()[2]:
                mc.select(self.ins_cslRAC.csl_GroupSelect()[2],add=1)
            if self.ins_cslRAC.csl_GroupSelect()[3]:
                mc.select(self.ins_cslRAC.csl_GroupSelect()[3],add=1)            
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
        #04-导出场景文件
        if refconinfo[1]==1: 
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))          
            mc.select(self.ins_cslRAC.csl_GroupSelect()[1])
            if self.ins_cslRAC.csl_GroupSelect()[3]:
                mc.select(self.ins_cslRAC.csl_GroupSelect()[3],add=1) 
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))        
        #05--导出场景角色互动文件
        if refconinfo[0]==1 and refconinfo[1]==1:
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))         
            mc.select(self.ins_cslRAC.csl_GroupSelect()[0])
            if self.ins_cslRAC.csl_GroupSelect()[1]:
                mc.select(self.ins_cslRAC.csl_GroupSelect()[1],add=1)
            if self.ins_cslRAC.csl_GroupSelect()[2]:    
                mc.select(self.ins_cslRAC.csl_GroupSelect()[2],add=1)
            if self.ins_cslRAC.csl_GroupSelect()[3]:    
                mc.select(self.ins_cslRAC.csl_GroupSelect()[3],add=1)            
            mc.file((tempath+CSbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName)) 
            #======添加层数量变量 layerCount=========================
            layerCount = 2
#========================================================================
# #角色文件
#========================================================================
        if refconinfo[0]==1 :
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_角色文件设置' % ChabaseName))
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            self.ins_dod_arnTools.ArnoldRendererSettings()         
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            chaColorName=Project+'_'+shotName+'_'+'l1chrcolor_lr_c001.'+fileType
            chaAOVName=Project+'_'+shotName+'_'+'l1chrAOV_lr_c001.'+fileType
            chaMoblurName=Project+'_'+shotName+'_'+'l1chrMotionBlur_lr_c001.'+fileType
            chaID01Name=Project+'_'+shotName+'_'+'l3chrIDP01_lr_c001.'+fileType
            chaID02Name=Project+'_'+shotName+'_'+'l1chrIDP21_lr_c001.'+fileType
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_角色文件设置' % ChabaseName))         
#===================================================================
# #角色color文件 #chaColorName='l1chrcolor_lr_c001.';colorlayerName='chrClr'
#===================================================================
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色color文件' % chaColorName)) 
            #导入角色灯光文件 
            im_chrligh = self.import_light_file(u'chrlight')
            print u'================chr light import succeed!====================================='                  
            mc.file(rename=(tempath+chaColorName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshchr=self.ins_cslRAC.csl_meshInfo(meshtype='c')
            meshprp=self.ins_cslRAC.csl_meshInfo(meshtype='p')
            lightgroup=self.dod_lightInfoList('',True,u'chr')
            meshs=meshchr
            meshs.extend(meshprp)
            meshs.extend(lightgroup)
            #       将shape 透明信息继承给shapeDeform(适用于maya2013后）        
            mc.select(meshchr) 
            self.ins_cslRAC.csl_ShapeInfoApply(infoType='aiOpaque') 
            colorlayerName='chrClr'
            mc.createRenderLayer(meshs,name=colorlayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='sss')
            #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings(u'dod_hi')
            #    可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0) 
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            # 存盘
            chaColorName_new = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()                       
            #mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_创建角色color文件' % chaColorName_new))
            if  server==1  :
                description = u'角色color文件'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')      # checkIn                 
            print u'===================CHECKIN SECCEED!!!===【FILE %s】==========================='%  chaColorName_new           
#===================================================================
# #角色AOV文件 #chaAOVName=l1chrAOV_lr_c001.';aovlayerName='chrlight',chrlight_AO,chrlight_Normal,chrlight_Fre
#===================================================================
        if refconinfo[0]==1 :
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色aov层文件' % chaAOVName))         
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            #导入bgLight灯光文件 
            self.import_light_file(u'bglight')
            #=====================================
            mc.file(rename=(tempath+chaAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            aovlayerName='chrlight'
            meshchr=self.ins_cslRAC.csl_meshInfo(meshtype='c')
            meshprp=self.ins_cslRAC.csl_meshInfo(meshtype='p')
            lightgroup=self.dod_lightInfoList(u'',True,u'bg')
            if lightgroup: lightgroup = lightgroup[0]
            meshs=meshchr+meshprp+[lightgroup]
            mc.createRenderLayer(meshs,name=aovlayerName, noRecurse=1, makeCurrent=1)
            mc.editRenderLayerGlobals(currentRenderLayer=aovlayerName)
            mc.select(meshs)
            #赋lambert材质
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            #key fill rim  R G B
            #self.ins_cslRAC.csl_LightAssign(Type='chr') 
            mc.setAttr("defaultRenderLayer.renderable", 0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Normal')
            #          hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Shadow')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Fre')
            #          hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='motionvector')            
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
            #=====读取数据库上每个静头的不同zDepth值=========================================
            self.dod_adjust_zdp_argument()
            # 渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()   
            #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)               
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)             
            chaAOVName = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()         
            if  server==1  :
                description = u'角色AOV文件,chrlight'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传角色AOV文件' % chaAOVName)) 
#===================================================================
# #角色idpass01文件 #haID01Name='l3chrIDP01_lr_c001.'
#===================================================================
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色idpass01文件' % chaID01Name)) 
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mc.file(rename=(tempath+chaID01Name))
            mc.file(save=1,type = fileTypeAll,f = 1)
            print u'=====================【file】 saved %s==================================== ' % ChabaseName
            self.ins_dod_arnTools.csl_IDRenderLayerCreatAll(type="chr")
    #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)  
    #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            chaID01Name = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()         
            if  server==1  :
                description = u'角色id文件'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传角色文件' % chaID01Name))                    
#===================================================================
# #随机idp #chaID02Name=l1chrIDP21  renderLyaer name : 'chrId21'
#===================================================================
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色idpass21文件' % chaID02Name)) 
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaID02Name))
            mc.file(save=1,type = fileTypeAll,f = 1) 
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')         
            meshchr=self.ins_cslRAC.csl_meshInfo(meshtype='c')
            meshprp=self.ins_cslRAC.csl_meshInfo(meshtype='p')
            meshs=meshchr+meshprp
            mc.select(meshs)
            mc.createRenderLayer(meshs,name='chrId21', noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0) 
            self.csl_id21Render() 
        #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()      
    #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)  
    #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            chaID02Name = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()         
            if  server==1  :
                description = u'角色id21文件,随机idpass'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传角色文件' % chaID02Name))            
# 场景文件处理：
#=======================================================================
# #场景AOV文件 # setAOVName='l2setAOV_lr_c001.'#  RenderLayer: 'setCaus' ,u'RGBLight'
#=======================================================================
        #文件名
        if refconinfo[1]==1:
            setAOVName=Project+'_'+shotName+'_'+'l2setAOV_lr_c001.'+fileType
            #setMoblurName=Project+'_'+shotName+'_'+'l1setMotionBlur_lr_c001.'+fileType
            setIDName=Project+'_'+shotName+'_'+'l3setIDP11_lr_c001.'+fileType
            setClrName = u'%s_%s_l%dsetClr_lr_c001.%s'%(Project,shotName,layerCount,fileType)           
            setShadowName = u'%s_%s_l1setShadow_lr_c001.%s'%(Project,shotName,fileType)  
            #层名
           #====================================================================
           #  setAOVlayerName='set_Caustic'
           # # setmoblurLayerName='set_motionblur'
           #  setClrBG_RL_name = u'set_bgClr'
           #  setClrGD_RL_name = u'set_gdClr'
           #  setShadow_RL_name = u'set_shadow'
           #  setRGB_RL_name = u'set_rgb'
           #====================================================================
            #层名
            setAOVlayerName='setCaus'
           # setmoblurLayerName='set_motionblur'
            setClrBG_RL_name = u'setBgClr'
            setClrGD_RL_name = u'setGdClr'
            setClrFG_RL_name = u'setFgClr'
            setClrTr_RL_name = u'setTrClr'
            setClrDy_RL_name = u'setDyClr'
            setShadow_RL_name = u'setShadow'
            setRGB_RL_name = u'RGBLight'
            setIdFBgrnd_RL_name = u'IdFBgrnd'
            #打开场景文件
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景AOV文件' % setAOVName))          
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1) 
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+setAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            #===================================================================
            # #=========删除远景物体，给物体赋lambert材质==================
            # far_objs = self.set_far_check()
            # if far_objs :delete(far_objs)
            # #===================================================
            #===================================================================
            #meshSet=self.ins_cslRAC.csl_meshInfo(meshtype='s')
            meshSet=self.ins_cslRAC.csl_GroupSelect()[1][1:]
            select(meshSet)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            #========导入焦散灯====================================
            #PyNode(u'defaultRenderLayer').setCurrent()
            self.ins_dod_com_proc.import_file_specialNameSpace((tempath+causLightName),u'CAUSLIGHT')
            #======================================================
            #======================创建RGB层==============================
            select(cl=True)
            RGB_lightGrp = self.dod_lightInfoList(u'',True,u'RGB',u'set')
            delete(RGB_lightGrp.pop())
            if not RGB_lightGrp:
                warning( u'==============场景里没有RGB灯=====================')
            mc.createRenderLayer(meshSet,name=setRGB_RL_name, noRecurse=1, makeCurrent=1)
            PyNode(RGB_lightGrp[0]).visibility.set(1)
            #======================创建Caustic层，加入焦散灯=============================
            mc.createRenderLayer(meshSet,name=setAOVlayerName, noRecurse=1, makeCurrent=1)
            PyNode(setAOVlayerName).addMembers(self.dod_lightInfoList('causticLight_L',False,u'caus')[0])
            #=========隐藏其他灯光组合焦散灯2==========================
            PyNode(self.dod_lightInfoList('causticLight_s',False,u'caus')[0]).visibility.set(0)
            PyNode(RGB_lightGrp[0]).visibility.set(0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Normal')
            self.ins_dod_arnTools.ArnoldAOVCreat(AOVtype='Zdp')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Fre')
            #hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='motionvector')              
    #===========================================================================
    # #根据不同MS设置zdp
    #         self.ins_cslRAC.csl_SetRefZD()        
    #===========================================================================
            mc.setAttr("defaultRenderLayer.renderable", 0)
    #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)   
    #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
    # 设置RGB层，不输出AOV ==========================================================           
            PyNode(setRGB_RL_name).setCurrent()
            editRenderLayerAdjustment(u'defaultArnoldRenderOptions.aovMode',layer = setRGB_RL_name)
            setAttr(u'defaultArnoldRenderOptions.aovMode',0)
    #============================================================================
            setAOVName = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()         
            if  server==1  :
                description = u'场景AOV文件,renderLayer:setCaus;RGBLight'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景AOV文件' % setAOVName)) 
#===================================================================
# #场景idpass11文件 #setIDName='l3setIDP11' #RenderLayer:id_11,id_12,id_13
#===================================================================
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景idpass11文件' % setIDName)) 
            #===================================================================
            # #=========删除远景物体，给物体赋lambert材质==================
            # far_objs = self.set_far_check()
            # delete(far_objs)
            # #===================================================
            #===================================================================
            mc.file(rename=(tempath+setIDName))
            mc.file(save=1,type = fileTypeAll,f = 1)
        #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()          
        #隐藏场景灯光 
            setLights=self.dod_lightInfoList('',True,u'set')
            if  setLights:
                for light in setLights:
                    PyNode(light).visibility.set(0)            
        #关闭场景meshLight:
            setmesh=self.ins_cslRAC.csl_meshInfo(meshtype='s')
            if setmesh:
                for mesh in setmesh:
                    try:
                        mc.setAttr((light+'.lightVisible'),0) 
                    except:
                        pass                        
            self.ins_dod_arnTools.csl_IDRenderLayerCreatAll(type='set')
            #================添加前景背景物体不同idp==============================
            #===========将场景中的前景物体，半透明物体，其他背景物体区分========================================================
            foregroundObjs = self.filter_obj_byAttr(u'Fore')
            if foregroundObjs:
                otherObjsIterater = (eachOne for eachOne in ins_dod_com_proc.dod_listAll_RndMeshes()[u'SET_GRP'] if eachOne not in foregroundObjs)
                otherBackObjs = [each for each in otherObjsIterater]
                createRenderLayer(foregroundObjs,n=setIdFBgrnd_RL_name,nr=True,mc=True )
                PyNode(setIdFBgrnd_RL_name).addMembers(otherBackObjs)
                select(cl=True)
                select(otherBackObjs)
                self.ins_dod_arnTools.ArnoldIDCreat(idpShader=u'ArnoldIdpR')
                select(cl=True)
                select(foregroundObjs)
                self.ins_dod_arnTools.ArnoldIDCreat(idpShader=u'ArnoldIdpG') 
            #===================================================================       
    #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)   
    #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            setIDName = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()          
            if  server==1  :
                description = u'场景id文件'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')   #checkIn
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景idpass11文件' % setIDName)) 
#=======================================================================
# #场景灯光文件===setClrName = _l2setClr_==setClrBG_RL_name = u'setBgClr'   setClrGD_RL_name = u'setGdClr' ;setClrFG_RL_name = u'setFgClr', setClrTr_RL_name = u'setTrClr'=========================================================
#=======================================================================
#setClrName = u'%s_%s_l4setClr_lr_c001.%s'%(Project,shotName,fileType)           
#           #层名
#            setClrBG_RL_name = u'set_bgClr'
#            setClrGD_RL_name = u'set_gdClr'
#            setClrFG_RL_name = u'setFgClr'
#            setClrTr_RL_name = u'setTrClr'
#            setClrDy_RL_name = u'setDyClr'
            #打开场景文件
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1) 
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景light文件' % setClrName))          
            self.ins_dod_arnTools.ArnoldRendererSettings(u'dod_m')
            mc.file(rename=(tempath+setClrName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            #===========将场景中的前景物体，半透明物体，其他背景物体区分========================================================
            all_setObjs = self.ins_dod_com_proc.dod_listAll_RndMeshes()[u'SET_GRP']
            foregroundObjs = self.filter_obj_byAttr(u'Fore')
            translucidObjs = self.filter_obj_byAttr(u'Translucid')
            tempStor = []
            if foregroundObjs:
                tempStor.extend(foregroundObjs)
            if translucidObjs:
                tempStor.extend(translucidObjs)
            otherObjsIterater = (eachOne for eachOne in all_setObjs if eachOne not in tempStor)
            otherBackObjs = [each for each in otherObjsIterater]
            #==============将动态植物列出=======================================
            p_dy = re.compile(u'_dynamics',re.I)
            dy_objs_interater = (eachDy for eachDy in all_setObjs if p_dy.search(eachDy.longName()))
            dy_objs = [eachDyObj for eachDyObj in dy_objs_interater]
#===================================================================
            #allTrans = (eachTran for eachTran in mc.ls(transforms = True) if mc.attributeQuery(u'Far',n = eachTran,exists=True))
            GD_objs = (PyNode(each_obj) for each_obj in mc.ls(type = u'transform') if mc.attributeQuery(u'GD',n=each_obj,exists=True))
            GD_objs_list = [each for each in GD_objs]
                #error(u'+++++++场景里没有地面物体或地面物体没有添加GD属性===========================')
            set_key_light_grp = self.dod_lightInfoList(u'',True,'set')
            #PyNode(set_key_light_grp[1]).visibility.set(0)#隐藏keylight组
            #meshSst.remove(GD_objs_list[0].longName())
            if GD_objs_list:#===========创建地面层===================================
                gd_clr_objs = GD_objs_list + set_key_light_grp
                mc.createRenderLayer(gd_clr_objs,name=setClrGD_RL_name, noRecurse=1, makeCurrent=1)
            #================创建背景物体层====================================
            mc.createRenderLayer(otherBackObjs,name=setClrBG_RL_name, noRecurse=1, makeCurrent=1)
            PyNode(setClrBG_RL_name).setCurrent()
            select(cl=True)
            #================================开启ground物体ai材质的enable matte 属性===================================
            if GD_objs_list:
                for each_GD in GD_objs_list:
                    self.set_ai_matt(each_GD,True)
            PyNode(setClrBG_RL_name).addMembers(set_key_light_grp)
            #==========================关闭动态植物的可渲染属性,开启投射阴影属性================================================
            if dy_objs:
                for eachDy in dy_objs:
                    eachDy.getShape(ni=True).primaryVisibility.set(0)
                    eachDy.getShape(ni=True).castsShadows.set(1)
            #=========================创建动态植物层================================
            if dy_objs:
                mc.createRenderLayer(all_setObjs,name = setClrDy_RL_name,noRecurse=1,makeCurrent=1)
                un_dy_objs = [each for each in all_setObjs if each not in dy_objs]
                select(un_dy_objs)
                self.ins_dod_arnTools.ArnoldIDCreat(idpShader="ArnoldIdpM")
            #===============创建前景物体层==========================================
            if foregroundObjs:
                mc.createRenderLayer(foregroundObjs,name=setClrFG_RL_name, noRecurse=1, makeCurrent=1)
                PyNode(setClrFG_RL_name).setCurrent()
                select(cl=True)
                #================================开启ground物体ai材质的enable matte 属性===================================
                PyNode(setClrFG_RL_name).addMembers(set_key_light_grp)
                if GD_objs_list:
                    PyNode(setClrFG_RL_name).addMembers(GD_objs_list)
                    for each_GD in GD_objs_list:
                        self.set_ai_matt(each_GD,True)
            #==============创建半透明物体层=============================================
            if translucidObjs:
                mc.createRenderLayer(translucidObjs,name=setClrTr_RL_name, noRecurse=1, makeCurrent=1)
                PyNode(setClrTr_RL_name).setCurrent()
                PyNode(setClrTr_RL_name).addMembers(set_key_light_grp)
                PyNode(setClrTr_RL_name).addMembers(otherBackObjs) 
                for eachbg in otherBackObjs:
                    eachbg.getShape(ni=True).primaryVisibility.set(0)
                if foregroundObjs:
                    PyNode(setClrTr_RL_name).addMembers(foregroundObjs)
                    for eachFg in foregroundObjs:
                        eachFg.getShape(ni=True).primaryVisibility.set(0)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            #hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='sss')
            #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()
            #    可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0) 
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            # 存盘                       
            setClrName = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()          
            csl_checkin.csl_checkin().csl_timeRecord()
            if  server==1  :
                description = u'场景灯光文件'
                if dy_objs:
                    description += u'=====注：有动态植物层'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')        # checkIn     
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景灯光文件' % setClrName))           
    #===============================================================================
    # 场景shadow文件  地面上物体投射到地面的阴影
    #Relatives Variable: 
    #setShadowName = u'%s_%s_l1setShadow_lr_c001.%s'%(Project,shotName,fileType)  
    #setShadow_RL_name = u'setShadow'
    #===============================================================================
            #打开场景文件
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景shadow文件' % setShadowName))          
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            #===================================================================
            # #========================删除远景物体==================
            # far_objs = self.set_far_check()
            # if far_objs : delete(far_objs)
            # #================================================== 
            #===================================================================
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+setShadowName))
            mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            mc.file(save=1,type = fileTypeAll,f = 1)
            GD_objs = (PyNode(each_obj) for each_obj in mc.ls(type = u'transform') if mc.attributeQuery(u'GD',n=each_obj,exists=True))
            GD_objs_list = [each for each in GD_objs]
            light_keyLight = ''
            if GD_objs_list:
                #error(u'+++++++场景里没有地面物体或地面物体没有添加GD属性===========================')
                try:
                    light_keyLight = self.dod_lightInfoList(u'key_light',False,u'set')
                except:
                    light_keyLight = self.dod_lightInfoList(u'keylight',False,'set')
                others_lights = self.dod_lightInfoList(u'',False,'set')
                others_lights.remove(light_keyLight[0])
                for eachLight in others_lights:
                    PyNode(eachLight).visibility.set(0)#隐藏其他灯光
                meshSet=self.ins_cslRAC.csl_meshInfo(meshtype='s')
                bg_shadow_objs = meshSet + light_keyLight
                mc.createRenderLayer(bg_shadow_objs,name=setShadow_RL_name, noRecurse=1, makeCurrent=1)
                select(meshSet)
                self.ins_dod_arnTools.ArnoldShaderAssign(u'Shadow')#===assign shadow shader to all mesh===ins_dod_arnTools.ArnoldShaderAssign(u'Zdp')==
                PyNode(setShadow_RL_name).setCurrent()
                for each_GD_obj in GD_objs_list: #pass    #===========shut off Ground castsShadow attribute====
                    each_GD_obj.getShape(ni=True).castsShadows.set(0)
                    each_GD_obj.getShape(ni=True).primaryVisibility.set(1)
                    meshSet.remove(each_GD_obj.longName())
                for each_bg_obj in meshSet:#================shut off overground objects primary visibility attribute
                    PyNode(each_bg_obj).getShape(ni=True).primaryVisibility.set(0)
                for each_aiSTin in mc.ls(type=u'aiStandIn'):#==================turn off standIn object primary visibility
                    mc.setAttr(u'%s.primaryVisibility' % each_aiSTin,0)
                    mc.setAttr(u'%s.overridePrimaryVisibility' % each_aiSTin,1)
                for each_GD_obj in GD_objs_list: #pass    #===========shut off Ground castsShadow attribute====
                    each_GD_obj.getShape(ni=True).primaryVisibility.set(1)
                select(cl=True)
                mc.setAttr("defaultRenderLayer.renderable", 0)
                #hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='sss')
                #渲染精度设置
                self.ins_dod_arnTools.ArnoldRendererSettings()
                #    可渲染相机设置
                self.dod_camRenderSet(shotType,serve=0) 
                #   动画帧数，渲染尺寸设置
                self.ins_cslRAC.csl_FileSet(shotType=2)   
                # 存盘                       
                setShadowName = self.ins_dod_com_proc.formatting_fileName_leyerdescrption()          
                csl_checkin.csl_checkin().csl_timeRecord()
                if  server==1  :
                    description = u'场景shadow文件'
                    mel.eval('idmtProject -checkin -description \" ' + description + '\"') # checkIn 
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景Shadow文件' % setShadowName)) 
            else:
                print u'======================场景里没有地面物体，将不渲染setShadow层============================'
#===============================================================================
# #场景角色互动文件处理
#    CSidp31=Project+'_'+shotName+'_'+'l1idp31_lr_c001.'+fileType
#    shadowLayer='conshadow' 
#===============================================================================
        if refconinfo[0]==1 and refconinfo[1]==1:
#===================================================================================================================
#=========角色场景交互阴影=====File Key character : '_l2InterShadow_',RenderLayer:  u'interShadow'; u'interAO'================================================
#===================================================================================================================
            #Relatives variable:
            char_set_inter_shadow = u'%s_%s_l2InterShadow_lr_c001.%s' %(Project,shotName,fileType)
            inter_chrShadow_RL_name = u'interShadow' #== character cast shadow on setting
            inter_AO_RL_name = u'interAO' #=====character interact setting AO===============
           # inter_shadow_chr_RL_name = u'interShadow'
            #inter_shadow_set_RL_name = u'interAO'
            #CSSetName=Project+'_'+shotName+'_'+'l2InterShadow_lr_c001.'+fileType
            #shadowLayer='conshadow' 
            #id31Layer='id31'
            #shadow conocc                    
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建interect shadow 文件' % char_set_inter_shadow))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+char_set_inter_shadow))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshes_ls_dic = self.ins_dod_com_proc.dod_listAll_RndMeshes()#======场景中物体的分类列表=====返回字典的key值为组名========================
            light_ls = self.dod_lightInfoList(u'',True,u'set')
            try:
                light_keyLight = self.dod_lightInfoList(u'key_light',False,u'set')
            except:
                light_keyLight = self.dod_lightInfoList(u'keylight',False,'set')
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            allMeshes_pynd = []
            for eachKey in meshes_ls_dic.keys():
                allMeshes_pynd.extend(meshes_ls_dic[eachKey])
            add2RL_objs = []
            for eachMesh in allMeshes_pynd:
                add2RL_objs.append(eachMesh.longName())
            select(add2RL_objs)
            self.ins_dod_arnTools.ArnoldShaderAssign(u'Shadow')#===assign shadow shader to all mesh=====
            select(cl=True)
            #add2RL_objs.extend(light_ls)
            mc.createRenderLayer(add2RL_objs,name=inter_chrShadow_RL_name, noRecurse=1, makeCurrent=1) #====create char shadow renderLayer ==========
            PyNode(inter_chrShadow_RL_name).setCurrent()
            PyNode(inter_chrShadow_RL_name).addMembers(light_keyLight)
            for each_chrMesh in meshes_ls_dic[u'CHR_GRP']: #===turn off chr meshes primary visibiliyt attribute=====
                each_chrMesh.getShape(ni=True).primaryVisibility.set(0)
                each_chrMesh.getShape(ni=True).castsShadows.set(1)
            for each_prpMesh in meshes_ls_dic[u'PRP_GRP']: #===turn off prop meshes primary visibiliyt attribute=====
                each_prpMesh.getShape(ni=True).primaryVisibility.set(0)
                each_prpMesh.getShape(ni=True).castsShadows.set(1)
            for each_setMesh in meshes_ls_dic[u'SET_GRP']: #===shut off set meshes casts shadow attribute=====
                if each_setMesh.name().find(u'_nr_') == -1:
                    each_setMesh.getShape(ni=True).primaryVisibility.set(1)
                    each_setMesh.getShape(ni=True).castsShadows.set(0)
                else:
                    each_setMesh.getShape(ni=True).primaryVisibility.set(0)
            for each_aiSTin in mc.ls(type=u'aiStandIn'):#==================turn off standIn object caste shadow========
                mc.setAttr(u'%s.castsShadows' % each_aiSTin,0)
                mc.setAttr(u'%s.overrideCastsShadows' % each_aiSTin,1)
            #PyNode(light_ls[1]).visibility.set(0)#=====隐藏key light group=====================
            mc.createRenderLayer(add2RL_objs,name=inter_AO_RL_name, noRecurse=1, makeCurrent=1) #====create char shadow renderLayer ==========
            PyNode(inter_AO_RL_name).setCurrent()
            for each_chrMesh in meshes_ls_dic[u'CHR_GRP']: #===shut off chr meshes casts shadow attribute=====
                each_chrMesh.getShape(ni=True).primaryVisibility.set(0)
                each_chrMesh.getShape(ni=True).castsShadows.set(1)
            for each_prpMesh in meshes_ls_dic[u'PRP_GRP']: #===shut off prop meshes casts shadow attribute=====
                each_prpMesh.getShape(ni=True).primaryVisibility.set(0)
                each_prpMesh.getShape(ni=True).castsShadows.set(1)
            for each_setMesh in meshes_ls_dic[u'SET_GRP']: #===shut off set meshes primary visibiliyt attribute=====
                each_setMesh.getShape(ni=True).primaryVisibility.set(1)
                each_setMesh.getShape(ni=True).castsShadows.set(0)
            for each_aiSTin in mc.ls(type=u'aiStandIn'):#==================turn off standIn object primary visibility
                mc.setAttr(u'%s.castsShadows' % each_aiSTin,0)
                mc.setAttr(u'%s.overrideCastsShadows' % each_aiSTin,1)
            select(add2RL_objs)
            self.ins_dod_arnTools.ArnoldShaderAssign(u'AO')#===assign shadow shader to all mesh=====
            #PyNode(light_ls[0]).visibility.set(0)#=====hide set light group=====================
            mc.setAttr("defaultRenderLayer.renderable", 0)
            #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()
            #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)  
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            char_set_inter_shadow = self.ins_dod_com_proc.formatting_fileName_leyerdescrption() 
            if  server==1  :
                description = u'场景交互阴影文件'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')         # checkIn
            print u'\n'        
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景角色交互阴影文件' % char_set_inter_shadow))  
#==================================================================
#====场景角色RGB================================================================================================
#==================================================================
#====relatives variable:
            chr_set_inter_RGB = u'%s_%s_l1InterRGB_lr_c001.%s' %(Project,shotName,fileType)
            inter_rgb_RL_name = u'interRGB'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建interect RGB 文件' % chr_set_inter_RGB))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+chr_set_inter_RGB))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshes_ls_dic = self.ins_dod_com_proc.dod_listAll_RndMeshes()#======场景中物体的分类列表=====返回字典的key值为组名========================
            light_ls = self.dod_lightInfoList(u'',True,u'set')
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            delete(light_ls)
            select(cl=True)
            createRenderLayer(meshes_ls_dic.values(),n=inter_rgb_RL_name,nr=True,mc=True )
            select(meshes_ls_dic[u'CHR_GRP'])
            self.ins_dod_arnTools.ArnoldIDCreat(idpShader="ArnoldIdpG")
            select(meshes_ls_dic[u'PRP_GRP'])
            self.ins_dod_arnTools.ArnoldIDCreat(idpShader="ArnoldIdpA")
            GD_meshes = self.ins_cslRAC.csl_Attrlist(attrtype='GD')
            setMeshes = meshes_ls_dic[u'SET_GRP']
            if GD_meshes:
                for each_gd in GD_meshes:
                     setMeshes.remove(PyNode(each_gd))
                     select(GD_meshes)
                     self.ins_dod_arnTools.ArnoldIDCreat(idpShader="ArnoldIdpB")
            select(setMeshes)
            self.ins_dod_arnTools.ArnoldIDCreat(idpShader="ArnoldIdpR")
            
            PyNode(u'defaultRenderLayer').renderable.set(0)
            #渲染精度设置
            self.ins_dod_arnTools.ArnoldRendererSettings()
            #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)  
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            chr_set_inter_RGB = self.ins_dod_com_proc.formatting_fileName_leyerdescrption() 
            if  server==1  :
                description = u'场景角色RGB'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
            print u'\n'        
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景角色交互RGB文件' % chr_set_inter_RGB))  
#===================================================================
#======场景角色交互综合文件===包括交互zDepth，焦散灯2，灯光雾，角色灯照射场景 4层=================================================================
#===================================================================
#===relatives variable:
            char_set_inter_synth = u'%s_%s_l4InterSynth_lr_c001.%s' %(Project,shotName,fileType)
            inter_synth_zDepth_RL_name = u'interZDepth'
            inter_synth_caus_RL_name = u'interCaus'
            inter_synth_fog_RL_name = u'interFog'
            inter_synth_setLight_RL_name = u'setLight'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建interect sythese 文件' % char_set_inter_synth))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+char_set_inter_synth))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshes_ls_dic = self.ins_dod_com_proc.dod_listAll_RndMeshes()#======场景中物体的分类列表=====返回字典的key值为组名========================
            light_ls = self.dod_lightInfoList(u'',True,u'set')
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            select(meshes_ls_dic)
            #赋lambert材质
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            #=====create cuastic layer======================================================================
            #========导入焦散灯====================================
            self.ins_dod_com_proc.import_file_specialNameSpace((tempath+causLightName),u'CAUSLIGHT')
            caus_light_s = self.dod_lightInfoList(u'causticlight_s',False,u'caus')
            caus_light_l = self.dod_lightInfoList(u'causticlight_l',False,u'caus')
            PyNode(caus_light_l[0]).visibility.set(0)
            createRenderLayer(meshes_ls_dic.values(),n=inter_synth_caus_RL_name,nr=True,mc=True)
            PyNode(inter_synth_caus_RL_name).addMembers(caus_light_s,noRecurse=True)
            for each_chrMesh in meshes_ls_dic[u'CHR_GRP']: #===shut off chr meshes casts shadow attribute=====
                each_chrMesh.getShape(ni=True).primaryVisibility.set(1)
                each_chrMesh.getShape(ni=True).castsShadows.set(0)
            print u'#============caustic layer created====================='
            #=====create fog layer======================================================================
            #========导入fog light======================================================================
            self.ins_dod_com_proc.import_file_specialNameSpace((tempath+fogLightName),u'FOGLIGHT')
            fog_light_grp= self.dod_lightInfoList(u'',True,u'fog')
            if fog_light_grp:
                createRenderLayer(meshes_ls_dic.values(),n=inter_synth_fog_RL_name,nr=True,mc=True)
                PyNode(inter_synth_fog_RL_name).addMembers(fog_light_grp,noRecurse=True)
                print u'#============fog light layer created====================='
            #=====create zDepth layer===================================================================
            createRenderLayer(meshes_ls_dic.values(),n=inter_synth_zDepth_RL_name,nr=True,mc=True)
            select(meshes_ls_dic.values())
            self.ins_dod_arnTools.ArnoldShaderAssign(u'Zdp') #===create zdp shader name: SHD_Zdp_arnold ===================
            #=====读取数据库上每个静头的不同zDepth值=========================================
            self.dod_adjust_zdp_argument()
            #================create setlight shine to setting layer =================================================
            PyNode(u'defaultRenderLayer').setCurrent()
            #===========================导入背景灯光文件 ========================================
            im_bgLight = self.import_light_file(u'bglight')
            if im_bgLight:
                print u'================bg light import succeed!====================================='
                lightgroup=self.dod_lightInfoList('',True,u'bg')
                if lightgroup: lightgroup = lightgroup[0]
                #===================================================================
                # p_setGrp = re.compile(u'set_grp',re.I)
                # set_group = [eachGrp for eachGrp in meshes_ls_dic.keys() if p_setGrp.search(eachGrp) ][0]            
                #===================================================================
                createRenderLayer(meshes_ls_dic[u'SET_GRP'],n=inter_synth_setLight_RL_name,nr=True,mc=True)         
                PyNode(inter_synth_setLight_RL_name).addMembers(lightgroup)
                select(meshes_ls_dic[u'SET_GRP'])
                self.ins_dod_arnTools.ArnoldShaderAssign(u'aiStand')
                print  u'+++++++++++++++++++setLight Layer Created!!!!!++++++++++++++++++++++++++++++++'
            else:
                print u'++++++++++++++++++++没有bglight文件++++++++++++++++++++++++++++++++++++++++++'
            #===================================================================== 
            PyNode(u'defaultRenderLayer').renderable.set(0)
            #========add pre render mel :to make samplerInfor node recalculate==========================
            PyNode(u'defaultRenderGlobals').preMel.set("setAttr \"dod_samplerInfo_arnold.cameraFarClipPlane\" 3000;")
            #================================================================================
            #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)   
            #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            char_set_inter_synth = self.ins_dod_com_proc.formatting_fileName_leyerdescrption() 
            if  server==1  :
                description = u'角色场景接触OCC，焦散，fog，setLight'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
            print u'\n'        
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景角色交互文件' % char_set_inter_synth))  
#===========================================================================
#=====================互动idp31文件============================================ 
#===========================================================================
#==Relatives Variable:
            CSidp31=Project+'_'+shotName+'_'+'l1idp31_lr_c001.'+fileType
            id31Layer='id31'
            print u'\n'                                  
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景角色交互idp31' % CSidp31))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            self.ins_dod_arnTools.ArnoldRendererSettings()
            mc.file(rename=(tempath+CSidp31))
            mc.file(save=1,type = fileTypeAll,f = 1)
            chrmesh=self.ins_cslRAC.csl_meshInfo(meshtype='c')
            promesh=self.ins_cslRAC.csl_meshInfo(meshtype='p')
            setmesh=self.ins_cslRAC.csl_meshInfo(meshtype='s')
            self.csl_id31Creat()
    #   可渲染相机设置
            self.dod_camRenderSet(shotType,serve=0)   
    #   动画帧数，渲染尺寸设置
            self.ins_cslRAC.csl_FileSet(shotType=2)   
            mc.createRenderLayer((chrmesh+promesh+setmesh),name=id31Layer, noRecurse=1, makeCurrent=1)                       
            mc.setAttr("defaultRenderLayer.renderable", 0)        
            CSidp31 = self.ins_dod_com_proc.formatting_fileName_leyerdescrption() 
            if  server==1  :
                description = u'互动id文件'
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  # checkIn
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传idp31文件' % CSidp31))
    #成功代码        
        print u'\n'
        print u'==========================【%s】文件分层结束==========================' % FileName
        print u'\n'
        self.ins_cslRAC.csl_RendertimeRecord()         
        return 0                                   
#===============================================================================
# #============dumped fuction=====================   
#         def checkin_file(self,shotType = 2,descripton_str):#=============dumped function===
#             checkin_filename = sceneName()
#             fName_split = os.path.split(checkin_filename)
#             fName_text = os.path.splitext(fName_split[-1])
#             fName_split_short = fName_text[0].split(u'_')
#             proj_info =sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
#             shot_num = u''
#             file_description = u''
#             for i in range(shotType):
#                 if i< shotType -1:
#                     shot_num += u'%s_' % fName_split_short[i+1]
#                 else:
#                     shot_num += fName_split_short[i+1]
#             file_description = fName_split_short[shotType+1]
#             file_link = fName_split_short[shotType +2]
#             checkUser = os.environ['USERNAME']
#             file_info = u'1|%s|%s_%s_%s|%s' % (proj_info,shot_num,file_description,file_link,checkUser)
#             checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
#             print checkOutCmd
#             mel.eval(checkOutCmd) 
#             # checkIn
#             mel.eval('idmtProject -checkin -description \" ' + descripton_str + '\"')  
#             print u'\n', u'===============!!!End 【%s 已上传】!!!===============' % (fName_split[-1])
#===============================================================================
    #随机idp
    def csl_id21Render(self):
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB','ArnoldIdpA']
        chrgroup=self.ins_cslRAC.csl_GroupSelect()[0]
        chrgroup.remove(chrgroup[0])
        prpgroup=self.ins_cslRAC.csl_GroupSelect()[2]
        prpgroup.remove(prpgroup[0])      
        namespaces=chrgroup+prpgroup
        if namespaces:
            if 0<len(namespaces)<5:
                for i in range(len(namespaces)):
                    idc=idcolor[i]
                    mc.select(namespaces[i])
                    self.ins_dod_arnTools.ArnoldIDCreat(idc)
            if len(namespaces)>4:
                for i in range(len(namespaces)):
                    if i <4:
                        idc=idcolor[i]
                        mc.select(namespaces[i])
                        self.ins_dod_arnTools.ArnoldIDCreat(idc)
                    if i>4:
                        idc=idcolor[i-int(i/4)*4]
                        mc.select(namespaces[i])
                        self.ins_dod_arnTools.ArnoldIDCreat(idc)
        else:
            print u'文件中没有角色道具物体，请检查文件'                    
        return 0
#角色,道具，场景idp
    def csl_id31Creat(self):
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB','ArnoldIdpA']
        chrmeshInfo=self.ins_cslRAC.csl_meshInfo(meshtype='c')
        setmeshInfo=self.ins_cslRAC.csl_meshInfo(meshtype='s')
        prpmeshInfo=self.ins_cslRAC.csl_meshInfo(meshtype='p')
        gdInfo=self.ins_cslRAC.csl_Attrlist(attrtype='GD')
        #mlInfo=self.csl_Attrlist(attrtype='MLight')
        if gdInfo!=None and setmeshInfo!=None:
           for gd in gdInfo:
                try:
                    setmeshInfo.remove(gd)
                except:
                    pass  
        if  chrmeshInfo:
            mc.select(chrmeshInfo)
            self.ins_dod_arnTools.ArnoldIDCreat(idcolor[0])  
        if  setmeshInfo:
            mc.select(setmeshInfo)
            self.ins_dod_arnTools.ArnoldIDCreat(idcolor[1]) 
        if  gdInfo:
            mc.select(gdInfo)
            self.ins_dod_arnTools.ArnoldIDCreat(idcolor[2])              
        if  prpmeshInfo:
            mc.select(prpmeshInfo)
            self.ins_dod_arnTools.ArnoldIDCreat(idcolor[3]) 
        return 0        
    def dod_adjust_zdp_argument(self):
        print u'++++++++++++++++++++++PLEASE　ＷＡＩＴＩＮＧ．．．．．．．．＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋＋'
    def dod_camRenderSet(self,shortType=2,serve=0):
        camname = docp.config_shotFile_cameraParameter()
        #mel.eval(u'updateMayaSoftwareCameraControl')
        return camname                                     
    def dod_refcondition(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace=refInfos[2][0]
        if 'CAM' in refNamespace:
            refNamespace.remove('CAM')
        setRef=[]
        chpRef=[]
        for ns in refNamespace:
            if ns.split('_')[1][0] in ['s', 'S']:
                setRef.append(ns)    
            if ns.split('_')[1][0] in ['c','p']:
                chpRef.append(ns)
        set,chp = 0,0
        if setRef:  set=1 
        if chpRef:  chp=1 
        if self.SET_GRP_memberInfo():   
            set = 1
        return [chp,set]       
    def filter_obj_byAttr(self,attr_name):
        allTrans = (eachTran for eachTran in mc.ls(transforms = True) if mc.attributeQuery(attr_name,n = eachTran,exists=True))
        match_objs = [PyNode(eachOne) for eachOne in allTrans if PyNode(eachOne).longName().find(u':MODEL') != -1]
        if match_objs:
            return match_objs
        else:
            return None                           
    def SET_GRP_memberInfo(self): 
        if mc.objExists(u'SET_GRP'):
            if mc.listRelatives(u'SET_GRP',c=True,ad=True,type=u'mesh',ni=True):
                return True
            else:
                return False    
    def dod_lightInfoList(self,represent_2nd,getGrp = False,*represent_1st): #===根据指定的参数返回对应的灯光组或者灯光们============
        finally_result = []
        for each_represent in represent_1st:
            #pass
            all_objs = (each for each in mc.ls(dag=True,l=True) if not mc.nodeType(each) in [u'mesh','nurbsCurve','joint',u'transform',u'aiStandIn','camera',u'stereoRigFrustum',u'stereoRigCamera',u'stereoRigTransform'])
            #lights = (eachNode for eachNode in mc.ls(dag=True,l=True) if nodeType(eachNode) in listNodeTypes('light'))
            p_light_sort = re.compile(u'_%s_'%each_represent,re.I)
            p_lightGrp = re.compile(u'[\W\w]+%s_light\|' % each_represent,re.I)
            listResult = []
            listResult_detail = []
            for each in all_objs:
                if p_light_sort.search(each) and nodeType(each) in listNodeTypes('light'):
                    listResult.append(PyNode(each).getParent().longName())
            if len(listResult) != 0:
                if getGrp:
                    specify_lightGrp = [] 
                    if p_lightGrp.search(listResult[0]):
                        try:
                            specify_lightGrp.append(p_lightGrp.search(listResult[0]).group())
                            finally_result.extend(specify_lightGrp)
                        except:
                            error(u'======场景里没有名字为%s的灯光1' % specify_lightGrp)
                else:
                    if represent_2nd:
                        for eachLight in listResult:
                            p_represent_2 = re.compile(represent_2nd,re.I)
                            if p_represent_2.search(eachLight):
                                listResult_detail.append(eachLight)
                        if not listResult_detail:
                            error(u'======场景里没有名字为%s的灯光2' % specify_lightGrp)
                        finally_result.extend(listResult_detail)
                    else:
                        finally_result.extend(listResult)
            else:
                print "========There is no light matching :%s===========" % (each_represent)
                pass
        return finally_result
    def set_ai_matt(self,meshObject,value=1):#====================设置物体ai材质球的enable matte 属性
    #meshObject = selected()[0]
        con_shape = meshObject.getShape(type=u'mesh',ni=True)
        sg_node = con_shape.listConnections(type = u'shadingEngine')
        current_RL = mc.editRenderLayerGlobals(crl=True,q=True)
        if sg_node:
            shader_node = sg_node[0].surfaceShader.listConnections()
            if shader_node and shader_node[0].hasAttr(u'aiEnableMatte'):
                mc.editRenderLayerAdjustment(u'%s.aiEnableMatte' % shader_node[0],lyr = current_RL)
                shader_node[0].aiEnableMatte.set(value)
    
    #===========================导入灯光文件 ========================================
    def import_light_file(self,lightGrpType = u'chrlight'): 
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        LtFile_servPath = u'%sscenes/Animation/episode_%s/scene_%s/%s'%(serverPath,shotInfo[1],shotInfo[2],lightGrpType)    
        if os.path.isdir(LtFile_servPath):
            im_ligt_file = ''
            im_namespace = ''
            list_bgLtFolder= os.listdir(LtFile_servPath)
            if list_bgLtFolder:
                for each_name in list_bgLtFolder:
                    im_ligt_file = u'%s/%s' %(LtFile_servPath,each_name)
                    if os.path.isfile(im_ligt_file):
                        im_namespace = os.path.splitext(os.path.split(im_ligt_file)[-1])[0]
                        mc.file(im_ligt_file,i=1,pr=1,namespace=im_namespace.split('.')[0])
                        break
                print u'================light file import succeed!====================================='
                return True
            else:
                print  u'=====================THERE IS　NO  bglight FILE=================================='
                return None
        else:
            print  u'=====================THERE IS　NO  bglight FILE=================================='
            return None