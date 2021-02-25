# -*- coding: utf-8 -*-
# 【lion 项目】【自动渲染工具】
#  Author : 韩虹
#  Data   : 2016_04
# import sys
# sys.path.append('D:\\food\pyp\common')


#渲染后台

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)
from idmt.maya.ShunLiu_common import csl_RenderAutoCommons
reload(csl_RenderAutoCommons)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.Lion import Lion_renderLayer
reload(Lion_renderLayer)

from idmt.maya.ShunLiu_common import csl_checkin
reload(csl_checkin)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
import os
import re

class lion_RenderAutoCommons(object):
    def __init__(self):
        # namespace清理
        pass

    def lion_RenderLayerAuto(self,shotType=2,server=1):
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================【%s】文件分层开始==========================' % FileName        
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
        tempath='D:/Info_Temp/'+Project+'/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        mc.sysFile(tempath, makeDir=True)
#   文件打组
        csl_RenderAutoCommons.csl_RenderAutoCommons().sk_sceneReorganize(0)
        #需要导出的文件名称：
#        fileType=['cha','set','cs','chrlight','setlight']
        #角色文件（包括道具）        
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #角色ID文件（包括道具）        
        ChaIDName=Project+'_'+shotName+'_'+'chaID_lr_c001.'+fileType
        #场景文件  
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType 
        #场景ID文件  
        SetIDName=Project+'_'+shotName+'_'+'setID_lr_c001.'+fileType
        #角色场景互动文件              
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #场景GD文件：
        SetGDName=Project+'_'+shotName+'_'+'gd_lr_c001.'+fileType
        #01——载入场景
        #self.lion_RenderEnvLoad()
        #print (u'===============!!!Start 【%s】!!!===============' % (u'%s_载入场景参考' % FileName))        
        #smooth设置        
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_smooth设置' % FileName)) 
        #隐藏
        #self.lion_HideList()
        #参考判断（文件是否有角色（包含道具），场景  
        refconinfo=self.lion_refcondition()
        #文件中物体：
        objs = self.LionGrpList()
        refCHR = [objs[0]]
        refPROP = [objs[1]]
        refSET = [objs[2]]
        GDList=self.gdc_Attrlist(type='mesh',attrtype='GD')


        #objs = self.LionRLObjectsTList()
        #refCHR = objs[0]
        #refPROP = objs[1]
        #refSET = objs[2]



        #02--导出角色文件 
        if refconinfo[0]==1:       
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))        
            mc.select(refCHR+refPROP)
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
        #03--导出场景文件
        if refconinfo[1]==1: 
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))          
            mc.select(refSET)
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))

        #导入参考，删除材质
        self.lion_RefIm()
        mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        #04--导出角色ID文件
        if refconinfo[0]==1:       
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色ID文件' % ChaIDName))        
            mc.select(refCHR+refPROP)
            mc.file((tempath+ChaIDName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色ID文件' % ChaIDName))  
        #05--导出场景ID文件
        if refconinfo[1]==1: 
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景文件' % SetIDName))          
            mc.select(refSET)
            mc.file((tempath+SetIDName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % SetIDName))                    
        #06--导出场景角色互动文件
        if refconinfo[0]==1 and refconinfo[1]==1:
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))         
            mc.select(refCHR+refPROP+refSET)
            mc.file((tempath+CSbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))
        #07--导出场景GD文件
        if refconinfo[0]==1 and refconinfo[1]==1:
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))
            if GDList:
                mc.select(GDList)
                mc.file((tempath+SetGDName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))
            #角色文件
        if refconinfo[0]==1 :
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_角色文件设置' % ChabaseName))         
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            if os.path.exists(tempath+SetGDName):
                mc.file((tempath+SetGDName),options='v=0',type=fileTypeAll,i=1)
                mel.eval('zjRemoveNamespace')
            chaColorName=Project+'_'+shotName+'_'+'l7chrcolor_lr_c001.'+fileType
            chaIDName=Project+'_'+shotName+'_'+'chrID_lr_c001.'+fileType
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色文件' % chaColorName))
            Lion_renderLayer.Lion_renderLayer().Lion_CHRcolorCreate()
            self.lion_ArnoldSet()
            mc.file(rename=(tempath+chaColorName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l7chrcolor_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'角色文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传角色文件' % chaColorName)) 
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色' % chaColorName)) 
            
            mc.file((tempath+ChaIDName),options='v=0',type=fileTypeAll,f=1,o=1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建chaID文件' % chaIDName))
            Lion_renderLayer.Lion_renderLayer().Lion_CHRidpCreate()
            self.lion_ArnoldSet()
            mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
            mc.setAttr('defaultArnoldDriver.tiffFormat',0)
            mc.setAttr('defaultArnoldDriver.tiffCompression',1)
            mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
            mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
            mc.file(rename=(tempath+chaIDName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            print '--------------------------------'
            print tempath
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_chrID_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'角色ID文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传角色ID文件' % chaIDName))             
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色ID文件' % chaIDName))      
# 场景文件处理：
        #场景AOV文件

        #文件名
        if refconinfo[1]==1:
            setAOVName=Project+'_'+shotName+'_'+'l4setAOV_lr_c001.'+fileType
            setIDNam=Project+'_'+shotName+'_'+'l3setIDP11_lr_c001.'+fileType
            #层名
            setAOVlayerName='set'
            #打开场景文件
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景AOV文件' % setAOVName))          
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            Lion_renderLayer.Lion_renderLayer().Lion_SETcolorCreate()
            self.lion_ArnoldSet()
            mc.file(rename=(tempath+setAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l4setAOV_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'场景文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景文件' % setAOVName))             
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色ID文件' % setAOVName))
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景ID文件' % setIDNam))
            mc.file((tempath+SetIDName),options='v=0',type=fileTypeAll,f=1,o=1)
            Lion_renderLayer.Lion_renderLayer().Lion_SETidpCreate()
            self.lion_ArnoldSet()
            renderLayer=mc.ls(type='renderLayer') 
            idInfo=0
            for layer in renderLayer:
               if '_id1' in renderLayer:
                  idInfo=1
            if idInfo==0:
                try:
                    mc.delete(tempath+SetIDName)
                except:
                    pass
                mc.warning(u'========该场景没有ID层==========' )
            else:
                mc.file(rename=(tempath+setIDNam))
                mc.file(save=1,type = fileTypeAll,f = 1)
                if  server==1  :
                    fileInfo='1|' + projectInfo + '|' + shotName + '_l3setIDP11_lr|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    mel.eval(checkOutCmd) 
                    description = u'场景IDP文件'
                    # checkIn
                    mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                    print u'\n'
                    print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景IDP文件' % setIDNam))

        if refconinfo[0]==1 and refconinfo[1]==1:
            CSSetName=Project+'_'+shotName+'_'+'l2setcon_lr_c001.'+fileType
            CSidp31=Project+'_'+shotName+'_'+'l1idp31_lr_c001.'+fileType
            shadowLayer='conshadow' 
            id31Layer='id31'                
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建CONS文件' % CSSetName))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1) 
            CHR_light= 'Z:/Projects/LION/Lion_Scratch/render/char_light/Lion_CHRLT_new.mb'
            lightfile=CHR_light
            if mc.ls('CHR_light'):
                mc.delete('CHR_light')      
            mc.file(lightfile, i=1)              
            keylight= []
            if mc.ls('charlight_meshKey_Light'):
                keylight=mc.ls('charlight_meshKey_Light')   
            objs =self.LionRLObjectsTList()
            CHR = objs[0]
            PROP = objs[1]
            SET = objs[2]
            chrobjs = CHR + PROP
            #setobjs=refSET
            setobjs=self.gdc_Attrlist(type='mesh',attrtype='GD')
            if not setobjs:
                setobjs=SET
            if keylight:
                for key in keylight:
                    shapes=mc.listRelatives(keylight,s=1,f=1) 
                    if shapes and re.search(('Light'), mc.nodeType(shapes[0]))!=None:
                        try:
                            mc.setAttr((shapes[0]+'.color'),1,1,1,type = 'double3')
                            mc.setAttr((shapes[0]+'.shadowColor'),0,0,0,type = 'double3')
                            mc.setAttr((shapes[0]+'.aiSamples'),6) 
                            mc.setAttr((shapes[0]+'.aiAffectVolumetrics'),0)
                            mc.setAttr((shapes[0]+'.aiCastVolumetricShadows'),0)                            
                        except:
                            pass  
            if setobjs:
                for obj in setobjs:
                    shapes=mc.listRelatives(obj, s=1,ni=1, f=1, type='mesh')
                    if shapes:
                        shape=shapes[0] 
                        try:
                            mc.setAttr((shape+'.castsShadows'),0)
                        except:
                            mc.warning('No object matches name: ' + shape + '.castsShadows')
                        try:
                            mc.setAttr((shape+'.lightVisible'),0)
                        except:
                            mc.warning('No object matches name: ' + shape + '.lightVisible')
                    else:
                        mc.warning(u'文件中没有场景物体')                    
                     
            if chrobjs:
                for mesh in chrobjs:
                    shapes=mc.listRelatives(mesh,s=1,f=1,type='mesh')
                    if shapes:
                        for shape in shapes:
                            mc.setAttr((shape+'.primaryVisibility'),0)  
            meshlights=chrobjs+keylight+setobjs
            meshs=chrobjs+setobjs
            Lion_renderLayer.Lion_renderLayer().nor_SmoothSet()
            Lion_renderLayer.Lion_renderLayer().camImoprt()
            Lion_renderLayer.Lion_renderLayer().zmRLCamSetting()
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')
            self.lion_ArnoldSet()
            mc.select(meshs)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Shadow',transparency=0)  
            mc.createRenderLayer(meshlights,name=shadowLayer, noRecurse=1, makeCurrent=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            mc.setAttr("defaultRenderLayer.renderable", 0)        
            mc.file(rename=(tempath+CSSetName))
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)             
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + 'l2setcon_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'shadow，接触occ文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'        
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传场景CS文件' % CSSetName))  
                #互动idp31文件 
            print u'\n'                                  
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建idp31' % CSidp31))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')
            self.lion_ArnoldSet()
            mc.file(rename=(tempath+CSidp31))
            mc.file(save=1,type = fileTypeAll,f = 1)

            objs = self.LionRLObjectsTList()
            CHR = objs[0]
            PROP = objs[1]
            SET = objs[2]
            meshs=CHR+PROP+SET
            Lion_renderLayer.Lion_renderLayer().nor_SmoothSet()
            Lion_renderLayer.Lion_renderLayer().camImoprt()
            Lion_renderLayer.Lion_renderLayer().zmRLCamSetting()
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')                         
            self.lion_ArnoldSet()
            csl_RenderAutoCommons.csl_RenderAutoCommons().csl_id31Creat()
            mc.createRenderLayer(meshs,name=id31Layer, noRecurse=1, makeCurrent=1)
            # tif
            mc.setAttr('defaultRenderGlobals.imageFormat',3 )
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1) 
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1idp31_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'互动id文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传idp31文件' % CSidp31))  
        print u'\n'
        print u'==========================【%s】文件分层结束==========================' % FileName
        print u'\n'
        self.csl_RendertimeRecord()         
        return 0
#物体表
    def LionRLObjectsTList(self):
        # 获取root
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        refCHR = []
        refPROP = []
        refSET = []
        needSKY = []
        needPROP = []
        needrefSEA = []
        needInfo=[]
        if mc.ls('CHR_GRP'):
            if mc.listRelatives('CHR_GRP', c=1, f=1, type='transform'):
                refCHR = mc.listRelatives('CHR_GRP', c=1, f=1, type='transform')
        if mc.ls('PRP_GRP'):
            if mc.listRelatives('PRP_GRP', c=1, f=1, type='transform'):
                refPROP = mc.listRelatives('PRP_GRP', c=1, f=1, type='transform')
        if mc.ls('SET_GRP'):
            if mc.listRelatives('SET_GRP', c=1, f=1, type='transform'):
                refSETgroup = mc.listRelatives('SET_GRP', c=1, f=1, type='transform')
                refSET=mc.listRelatives(refSETgroup, c=1, f=1, type='transform')
        for i in range(3):
            needInfo = []
            if i == 0:
                refGrps = refCHR
            if i == 1:
                refGrps = refPROP
            if i == 2:
                refGrps = refSET
            if refGrps:
                meshes = mc.listRelatives(refGrps, ad=1, ni=1, type='mesh', f=1)
                if meshes:
                    for mesh in meshes:
                        objs=mc.listRelatives(mesh,p=1,f=1)
                        if  objs and 'MODEL|' in mesh and 'DEFORMERS|' not in mesh:
                          needInfo.append(objs[0])
            if i == 0:
                CHRR = needInfo
            if i == 1:
                PROPR = needInfo
            if i == 2:
                SETR = needInfo
        result = [CHRR,PROPR,SETR]
        return result
#物体表
    def LionGrpList(self):
        # 获取root
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        CHRGRP = ''
        PROPGRP = ''
        SETGRP = ''
        if mc.ls('CHR_GRP') and not mc.listRelatives('CHR_GRP',ni=1,s=1):
            CHRGRP=mc.ls('CHR_GRP',l=1,type='transform')[0]
        if mc.ls('PRP_GRP') and  not mc.listRelatives('PRP_GRP',ni=1,s=1):
            PROPGRP=mc.ls('PRP_GRP',l=1,type='transform')[0]
        if mc.ls('SET_GRP') and  not mc.listRelatives('SET_GRP',ni=1,s=1):
            SETGRP=mc.ls('SET_GRP',l=1,type='transform')[0]
        result = [CHRGRP,PROPGRP,SETGRP]
        return result
#记录时间
    def csl_RendertimeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
    def lion_refcondition(self):
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        setRef=[]
        chpRef=[]
        for ns in namespaces:
            if '_' in ns and ns.split('_')[1][0].lower() in ['s']:
                setRef.append(ns)
            if '_' in ns and ns.split('_')[1][0].lower() in ['c','p']:
                chpRef.append(ns)
        set=''
        chp=''
        if setRef:
           set=1
        else:
           set=0
        if chpRef:
           chp=1
        else:
           chp=0
        return [chp,set]
    def lion_RefIm(self):
        while mc.file(q=1,r=1):
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1)
        return 0
    def lion_ArnoldSet(self):
        mel.eval("setMayaSoftwareFrameExt(3,0)")
        mc.setAttr('defaultArnoldDriver.aiTranslator','tif',type='string')
        mc.setAttr('defaultArnoldDriver.tiffFormat',0)
        mc.setAttr('defaultArnoldDriver.tiffCompression',1)
        mc.setAttr ('defaultArnoldDriver.mergeAOVs', 0)
        mc.setAttr ('defaultArnoldRenderOptions.aovMode',1)
# 【lion 项目】【特殊属性列表】
#  Author : hanhong
    def gdc_Attrlist(self,type='mesh',attrtype='GD'):
        objList=[]
        objs=mc.ls(type=type,l=1)
        if objs:
            for obj in objs:
                tr=mc.listRelatives(obj,p=1,type='transform',f=1)
                if tr and mc.objExists(tr[0]+'.'+attrtype) and mc.getAttr(tr[0]+'.'+attrtype)==1 and tr[0] not in objList:
                     objList.append(tr[0])
        return objList