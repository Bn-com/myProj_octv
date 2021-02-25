# -*- coding: utf-8 -*-
# ��ͨ�á���FinalLayout���ڹ��ߡ�
#  Author : ����
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')


#��Ⱦ��̨

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)


from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)

from idmt.maya.ShunLiu_common import csl_checkin
reload(csl_checkin)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
import os
import re
class csl_RenderAutoCommons(object):
    def __init__(self):
        # namespace����
        pass

    def csl_RenderLayerAuto(self,shotType=3,server=1):
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================��%s���ļ��ֲ㿪ʼ==========================' % FileName        
        self.csl_RendertimeRecord()        
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
        tempath='D:/Info_Temp/temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        mc.sysFile(tempath, makeDir=True)
#   �ļ�����
        self.sk_sceneReorganize(0)
        #��Ҫ�������ļ����ƣ�
#        fileType=['cha','set','cs','chrlight','setlight']
        #��ɫ�ļ����������ߣ�        
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #�����ļ�  
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType 
        #��ɫ���������ļ�              
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #��ɫ�ƹ��ļ� 
        chrlightName=Project+'_'+shotName+'_'+'chrlight_lr_c001.'+fileType
        
        #01�������볡��
        self.csl_RenderEnvLoad()
        print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���볡���ο�' % FileName))        
        #smooth����        
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start ��%s��!!!===============' % (u'%s_smooth����' % FileName)) 
        #����
        self.csl_HideList()
        #�ο��жϣ��ļ��Ƿ��н�ɫ���������ߣ�������  
        refconinfo=self.csl_refcondition()                                        
        #02--������ɫ�ļ� 
        if refconinfo[0]==1:       
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫ�ļ�' % ChabaseName))        
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[2]:
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)            
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_������ɫ�ļ�' % ChabaseName))
        #03--���������ļ�
        if refconinfo[1]==1: 
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���������ļ�' % SetbaseName))          
            mc.select(self.csl_GroupSelect()[1])
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1) 
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���������ļ�' % SetbaseName))        
        #04--����������ɫ�����ļ�
        if refconinfo[0]==1 and refconinfo[1]==1:
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_����������ɫ�����ļ�' % CSbaseName))         
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[1]:
                mc.select(self.csl_GroupSelect()[1],add=1)
            if self.csl_GroupSelect()[2]:    
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:    
                mc.select(self.csl_GroupSelect()[3],add=1)            
            mc.file((tempath+CSbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_����������ɫ�����ļ�' % CSbaseName)) 
        #05--������ɫ�ƹ��ļ�
        if refconinfo[0]==1 and refconinfo[1]==1:        
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫ�ƹ��ļ�' % chrlightName)) 
            #ɾ��OTC
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()

            if mc.ls('OTC_GRP'):
                mc.delete('OTC_GRP')
    #        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
            lightgroups=self.csl_lightInfoList(Type='chr',lightType='group')
            if lightgroups:
                lightgroup=lightgroups[0]
            else:
                mc.error( u"û�н�ɫ�ƹ�����ɫ�ƹ�����������ȷ�����뻷�ڸ�������ϵ" )             
            if (lightgroup+'.visibility'):
                mc.setAttr((lightgroup+'.visibility'),1)
            mc.select(lightgroup)
            mc.file((tempath+chrlightName),options='v=0',f=1,type=fileTypeAll,es=1)               
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_�ѵ�����ɫ�ƹ��ļ�' % chrlightName))
            #��ɫ�ļ�
        if refconinfo[0]==1 :
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_��ɫ�ļ�����' % ChabaseName))         
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('03')
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            chaColorName=Project+'_'+shotName+'_'+'l2chrcolor_lr_c001.'+fileType
            chaAOVName=Project+'_'+shotName+'_'+'l5chrAOV_lr_c001.'+fileType
            chaMoblurName=Project+'_'+shotName+'_'+'l1chrMotionBlur_lr_c001.'+fileType
            chaID01Name=Project+'_'+shotName+'_'+'l3chrIDP01_lr_c001.'+fileType
            chaID02Name=Project+'_'+shotName+'_'+'l1chrIDP21_lr_c001.'+fileType
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_��ɫ�ļ�����' % ChabaseName))         
            #��ɫcolor�ļ�
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫcolor�ļ�' % chaColorName)) 
            #�����ɫ�ƹ��ļ� 
            if refconinfo[1]==1 :                   
                mc.file((tempath+chrlightName),i=1,pr=1,namespace=chrlightName.split('.')[0])   
            if refconinfo[1]==0: 
                chalightpath='//file-cluster/GDC/Projects/ShunLiu/Project/data/ChrLight/'+shotName+'/'
                chalightName=shotName+'_chr_light.mb'
                mc.file((chalightpath+chalightName),i=1,pr=1,namespace=chrlightName.split('.')[0])                        
            mc.file(rename=(tempath+chaColorName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')[0]
            meshs=meshchr+meshprp+[lightgroup]
    #       ��shape ͸����Ϣ�̳и�shapeDeform(������maya2013��        
            mc.select(meshchr+meshprp) 
            self.csl_ShapeInfoApply(infoType='aiOpaque') 
             
            colorlayerName='chr'
            mc.createRenderLayer(meshs,name=colorlayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='sss')
        #��Ⱦ��������
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('03')
    #    ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0) 
            if shotInfo[1]=='103':
                mel.eval('setAttr "defaultArnoldRenderOptions.AASamples" 4;')
                mel.eval('setAttr "defaultArnoldRenderOptions.GITotalDepth" 0;')
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
    # ����                       
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)              
            csl_checkin.csl_checkin().csl_timeRecord()
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_������ɫcolor�ļ�' % chaColorName))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l2chrlight_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'��ɫcolor�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')                       
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫcolor�ļ�' % chaColorName))                    
        #��ɫAOV�ļ�
        if refconinfo[0]==1 :
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            #�����ɫ�ƹ��ļ�
            if refconinfo[1]==1 :                   
                mc.file((tempath+chrlightName),i=1,pr=1,namespace=chrlightName.split('.')[0])   
            if refconinfo[1]==0: 
                chalightpath='//file-cluster/GDC/Projects/ShunLiu/Project/data/ChrLight/'+shotName+'/'
                chalightName=shotName+'_chr_light.mb'
                mc.file((chalightpath+chalightName),i=1,pr=1,namespace=chrlightName.split('.')[0])  

            mc.file(rename=(tempath+chaAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval("source \"//file-cluster/GDC/Resource/Support/Maya/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            aovlayerName='chr_light'
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')[0]
            meshs=meshchr+meshprp+[lightgroup]
            mc.createRenderLayer(meshs,name=aovlayerName, noRecurse=1, makeCurrent=1)
            #�������
            skylight=mc.ls('*:*:*skylight')
            if skylight:
                mc.setAttr((skylight[0]+'.v'),0)
            mc.editRenderLayerGlobals(currentRenderLayer=aovlayerName)
            mc.select(meshs)
            #��lambert����
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            #key fill rim  R G B
            self.csl_LightAssign(Type='chr') 
            mc.setAttr("defaultRenderLayer.renderable", 0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Normal')
    #        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Shadow')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Fre')
    #        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='motionvector')            
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
        # ��Ⱦ��������
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')   
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)               
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)             
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)             
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫ�ǵƹ���ļ�' % chaAOVName))         
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l5chrAOV_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'��ɫAOV�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ���ɫ�ļ�' % chaAOVName)) 
#     #��ɫ motion�ļ�             
#            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
#            mc.file(rename=(tempath+chaMoblurName))                
#            mc.file(save=1,type = fileTypeAll,f = 1)
#        #��Ⱦ��������
#            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')          
#            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
#            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()') 
#            moblurLayerName='cha_motionblur'
#            meshchr=self.csl_meshInfo(meshtype='c')
#            meshprp=self.csl_meshInfo(meshtype='p')
#            meshs=meshchr+meshprp
#            mc.select(meshs)
#            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldMotionBlurShaderCreate()
#            mc.createRenderLayer(meshs,name=moblurLayerName, noRecurse=1, makeCurrent=1)
#            mc.setAttr("defaultRenderLayer.renderable", 0)
#            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
#    #   ����Ⱦ�������
#            self.csl_camRenderSet(shotType,serve=0)  
#            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
#            print u'\n'
#            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫmotionblur�ļ�' % chaMoblurName))
#            if  server==1  :
#                fileInfo='1|' + projectInfo + '|' + shotName + '_l1chrMotionBlur_lr|' + userName
#                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
#                mel.eval(checkOutCmd) 
#                description = u'��ɫmothionblur�ļ�'
#                # checkIn
#                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
#            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���ϴ���ɫ�ļ�' % chaMoblurName))                   
            #��ɫidpass01�ļ�
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaID01Name))
            mc.file(save=1,type = fileTypeAll,f = 1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_IDRenderLayerCreatAll(type="chr",ref=1)
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)  
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)          
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫidpass01�ļ�' % chaID01Name)) 
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3chrIDP01_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'��ɫid�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ���ɫ�ļ�' % chaID01Name))                    
            #���idp
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaID02Name))
            mc.file(save=1,type = fileTypeAll,f = 1) 
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')         
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            meshs=meshchr+meshprp
            mc.select(meshs)
            mc.createRenderLayer(meshs,name='chr_id21', noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0) 
            self.csl_id21Render() 
        #��Ⱦ��������
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')      
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)  
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)        
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫidpass21�ļ�' % chaID02Name)) 
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3chrIDP01_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'��ɫid21�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ���ɫ�ļ�' % chaID02Name))            
# �����ļ�����
        #����AOV�ļ�
        #�ļ���
        if refconinfo[1]==1:
            setAOVName=Project+'_'+shotName+'_'+'l6setAOV_lr_c001.'+fileType
            setMoblurName=Project+'_'+shotName+'_'+'l1setMotionBlur_lr_c001.'+fileType
            setIDName=Project+'_'+shotName+'_'+'l3setIDP11_lr_c001.'+fileType
            #����
            setAOVlayerName='set'
            setmoblurLayerName='set_motionblur'
            #�򿪳����ļ�
            print u'\n'
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_��������AOV�ļ�' % setAOVName))          
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1) 
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('03')
            mc.file(rename=(tempath+setAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshs=self.csl_GroupSelect()[1][1]
            mc.createRenderLayer(meshs,name=setAOVlayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Normal')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Zdp')
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='Fre')
    #        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='motionvector')              
    #���ݲ�ͬMS����zdp
            self.csl_SetRefZD()        
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)   
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)       
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l6setAOV_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'����AOV�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�����AOV�ļ�' % setAOVName)) 
#     #���� motion�ļ�               
#            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_��������motionblur�ļ�' % setMoblurName))
#            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
#            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')
#            mc.file(rename=(tempath+setMoblurName))                
#            mc.file(save=1,type = fileTypeAll,f = 1)
#            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
#            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()') 
#            meshs=self.csl_meshInfo(meshtype='s')
#            mc.select(meshs)
#            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldMotionBlurShaderCreate()
#            mc.createRenderLayer(meshs,name=setmoblurLayerName, noRecurse=1, makeCurrent=1)
#            mc.setAttr("defaultRenderLayer.renderable", 0)
#            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
#    #   ����Ⱦ�������
#            self.csl_camRenderSet(shotType,serve=0) 
#            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
#            if  server==1  :
#                fileInfo='1|' + projectInfo + '|' + shotName + '_l1setMotionBlur_lr|' + userName
#                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
#                mel.eval(checkOutCmd) 
#                description = u'����mothionblur�ļ�'
#                # checkIn
#                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
#            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�����motionblur�ļ�' % setMoblurName))                   
            #����idpass11�ļ�
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_��������idpass11�ļ�' % setIDName)) 
    # ����ID�ļ�   
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+setIDName))
            mc.file(save=1,type = fileTypeAll,f = 1)
        #��Ⱦ��������
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')          
        #���س����ƹ� 
            setLights=self.csl_lightInfoList(Type='set',lightType='all')
            if  setLights:
                for light in setLights:
                    try: 
                        mc.setAttr((light+'.visibility'),0)
                    except:
                        pass                    
        #�رճ���meshLight:
            setmesh=self.csl_meshInfo(meshtype='s')
            if setmesh:
                for mesh in setmesh:
                    try:
                        mc.setAttr((light+'.lightVisible'),0) 
                    except:
                        pass                        
                                               
            hh_RenderArnoldLayer.hh_RenderArnold().csl_IDRenderLayerCreatAll(type='set',ref=1)        
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)   
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1) 
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3setIDP11_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'����id�ļ�'
                #checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�����idpass11�ļ�' % setIDName)) 
#������ɫ�����ļ�����
        if refconinfo[0]==1 and refconinfo[1]==1:
            CSSetName=Project+'_'+shotName+'_'+'l2setcon_lr_c001.'+fileType
            CSidp31=Project+'_'+shotName+'_'+'l1idp31_lr_c001.'+fileType
            shadowLayer='conshadow' 
            id31Layer='id31'
            #shadow conocc                    
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_����CONS�ļ�' % CSSetName))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            mc.file(save=1,type = fileTypeAll,f = 1)
            mc.file(rename=(tempath+CSSetName))
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)  
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.file(save=1,type = fileTypeAll,f = 1)
     #��ʾ��ɫ�ƹ�
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')[0]
            if (lightgroup+'.visibility'):
                mc.setAttr((lightgroup+'.visibility'),1)
        #ɾ�������ƹ� 
            setLights=self.csl_lightInfoList(Type='set',lightType='group')
            if  setLights:
                mc.delete(setLights)
    #
            chrmesh=self.csl_meshInfo(meshtype='c')
            promesh=self.csl_meshInfo(meshtype='p')
    #        setmesh=self.csl_meshInfo(meshtype='s')       
            setmesh=self.csl_Attrlist(attrtype='GD')
            setshpes=self.csl_GDMeshList(attrtype='GD')
            keylight=self.csl_lightInfoList(Type='chr',lightType='key')
            chameshs=chrmesh+promesh                   
    #��������
            if chameshs:
                for mesh in chameshs:
                    shapes=mc.listRelatives(mesh,s=1,f=1)
                    if shapes:
                        for shape in shapes:
                            if mc.nodeType(shape)=='mesh':
                                mc.setAttr((shape+'.primaryVisibility'),0)                            
            if setshpes:
                if setshpes[0] :
                    for shape in setshpes[0]:
                        mc.setAttr((shape+'.castsShadows'),0)
                        mc.setAttr((shape+'.lightVisible'),0) 
                else:
                    mc.warning(u'�ļ���û��GD����')                    
                if setshpes[1] :
                    for errormesh in setshpes[1]:
                        mc.warning(errormesh+':'+u'����㼶�������㣬����')                               
            if keylight:
                for key in keylight:
                    shapes=mc.listRelatives(keylight,s=1,f=1) 
                    if shapes and re.search(('Light'), mc.nodeType(shapes[0]))!=None:
                        mc.setAttr((shapes[0]+'.color'),1,1,1,type = 'double3')
                        mc.setAttr((shapes[0]+'.shadowColor'),0,0,0,type = 'double3')
                        try:
                            mc.setAttr((shapes[0]+'.aiSamples'),6) 
                            mc.setAttr((shapes[0]+'.aiAffectVolumetrics'),0)
                            mc.setAttr((shapes[0]+'.aiCastVolumetricShadows'),0)
                            
                        except:
                            pass                                                                                  
            meshlights=chameshs+keylight+setmesh
            meshs=chameshs+setmesh
            mc.select(meshs)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign(shaderType='Shadow',transparency=0)
            mc.createRenderLayer(meshlights,name=shadowLayer, noRecurse=1, makeCurrent=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldAOVCreat(AOVtype='AO')
            mc.setAttr("defaultRenderLayer.renderable", 0)        
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)             
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + 'l2setcon_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'shadow���Ӵ�occ�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print u'\n'        
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�����CS�ļ�' % CSSetName))  
    #����idp31�ļ� 
            print u'\n'                                  
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_����idp31' % CSidp31))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('05')
            mc.file(save=1,type = fileTypeAll,f = 1)
            mc.file(rename=(tempath+CSidp31))
            mc.file(save=1,type = fileTypeAll,f = 1)
            chrmesh=self.csl_meshInfo(meshtype='c')
            promesh=self.csl_meshInfo(meshtype='p')
            setmesh=self.csl_meshInfo(meshtype='s') 
            self.csl_id31Creat()
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0)   
    #   ����֡������Ⱦ�ߴ�����
            self.csl_FileSet(shotType=3)   
            mc.createRenderLayer((chrmesh+promesh+setmesh),name=id31Layer, noRecurse=1, makeCurrent=1)                       
            mc.setAttr("defaultRenderLayer.renderable", 0)        
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1) 
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1idp31_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'����id�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�idp31�ļ�' % CSidp31))

#�ɹ�����        
        print u'\n'
        print u'==========================��%s���ļ��ֲ����==========================' % FileName
        print u'\n'
        self.csl_RendertimeRecord()         
        return 0                                   
                                                      
#ѡ������mesh����
    def csl_meshList(self,meshlist=[],fileType='cha'):
        meshs=mc.ls(type='mesh',l=1)
        if meshs and fileType=='cha':
            for meshShape in meshs:
                if '_ca_' in meshShape:
                    meshp=mc.listRelatives(meshShape,p=1,f=1)
                    mesh=mc.ls(meshp[0],l=1)
                    meshlist.append(mesh[0])
        if meshs and fileType=='set':
            for meshShape in meshs:            
                meshp=mc.listRelatives(meshShape,p=1,f=1) 
                mesh=mc.ls(meshp[0],l=1)           
                meshlist.append(mesh)        
        return meshlist 
#Load�����ο� 
    def csl_RenderEnvLoad(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        if mc.ls('CAMRN'):
            refRN.remove('CAMRN')
        refFile=refInfos[1][0]
        for i in range(len(refRN)):
            if refRN[i].split('_')[1][0] in ['s', 'S']:
                try:
                    mc.file(loadReference=refRN[i])
                except:
                    pass
        return 0            
                                    
    
#ѡ����Ҫ�����ģ�'CHR_GRP','SET_GRP')
    def csl_GroupSelect(self):
        chaSelect=[]
        camSelect=[]
        setSelect=[]
        prpSelect=[]
        Groups=['CHR_GRP','CAM_GRP','SET_GRP','PRP_GRP']
        for Gr in Groups:
            if Gr=='CHR_GRP' and mc.objExists('CHR_GRP'):
                chaSelect.append(Gr)
                GrL=mc.listRelatives(Gr,c = 1,f=1)
                if GrL:
                    for i in range(len(GrL)):
                        if mc.objExists(GrL[i]):
                            chaSelect.append(GrL[i])
            if Gr=='CAM_GRP' and mc.objExists('CAM_GRP'):
                camSelect.append(Gr)
                GrL=mc.listRelatives(Gr,c = 1,f=1)
                if GrL:
                    for i in range(len(GrL)):
                        if mc.objExists(GrL[i]):
                            camSelect.append(GrL[i])  
        
            if Gr=='SET_GRP' and mc.objExists('SET_GRP'):
                setSelect.append(Gr)
                GrL=mc.listRelatives(Gr,c = 1,f=1)
                if GrL:
                    for i in range(len(GrL)):
                        if mc.objExists(GrL[i]):
                            setSelect.append(GrL[i])
            if Gr=='PRP_GRP' and mc.objExists('PRP_GRP'):
                prpSelect.append(Gr)
                GrL=mc.listRelatives(Gr,c = 1,f=1)
                if GrL:
                    for i in range(len(GrL)):
                        if mc.objExists(GrL[i]):
                            prpSelect.append(GrL[i])                        
                        
        FileGroup=[chaSelect,setSelect,prpSelect,camSelect] 
        return  FileGroup 
#Ӧ��mesh��Ϣ
    def csl_meshInfoRead(self,meshtype='chr'):
        meshs=mc.ls(type='mesh',l=1)
        meshList=dict({})
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        if meshtype=='chr':
            for mesh in meshs :
                for ns in namespaces :
                    if ns in mesh:
                                   
                        meshList[ns]=mesh
                            
            if meshtype=='prp':
                for i in range(len(meshs)):
                    for j in range(len(namespaces)) :
                        if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0]=='p':
                            meshList[namespaces[j]]=meshs[i]
                            
            if meshtype=='set':
                for i in range(len(meshs)):
                    for j in range(len(namespaces)) :
                        if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0]=='s':
                            meshList[namespaces[j]]=meshs[i]
                        
        return meshList 
#���idp
    def csl_id21Render(self):
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB','ArnoldIdpY','ArnoldIdpC','ArnoldIdpK']
        chrgroup=self.csl_GroupSelect()[0]
        chrgroup.remove(chrgroup[0])
        prpgroup=self.csl_GroupSelect()[2]
        prpgroup.remove(prpgroup[0])      
        namespaces=chrgroup+prpgroup
        if namespaces:
            if 0<len(namespaces)<7:
                for i in range(len(namespaces)):
                    idc=idcolor[i]
                    mc.select(namespaces[i])
                    hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idc)
            if len(namespaces)>6:
                for i in range(len(namespaces)):
                    if i <6:
                        idc=idcolor[i]
                        mc.select(namespaces[i])
                        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idc)
                    if i>6:
                        idc=idcolor[i-int(i/6)*6]
                        mc.select(namespaces[i])
                        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idc)
        else:
            print u'�ļ���û�н�ɫ�������壬�����ļ�'                    
        return 0
#��ɫ,���ߣ�����idp
    def csl_id31Creat(self):
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB','ArnoldIdpY','ArnoldIdpK']
        chrmeshInfo=self.csl_meshInfo(meshtype='c')
        setmeshInfo=self.csl_meshInfo(meshtype='s')
        prpmeshInfo=self.csl_meshInfo(meshtype='p')
        gdInfo=self.csl_Attrlist(attrtype='GD')
        mlInfo=self.csl_Attrlist(attrtype='MLight')
        if gdInfo!=None and setmeshInfo!=None:
           for gd in gdInfo:
                try:
                    setmeshInfo.remove(gd)
                except:
                    pass  
        if mlInfo!=None and setmeshInfo!=None:
           for ml in gdInfo:
                try:
                    setmeshInfo.remove(ml)
                except:
                    pass                                                                        
        if  chrmeshInfo:
            mc.select(chrmeshInfo)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idcolor[0])  
        if  setmeshInfo:
            mc.select(setmeshInfo)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idcolor[1]) 
        if  gdInfo:
            mc.select(gdInfo)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idcolor[2])              
        if  prpmeshInfo:
            mc.select(prpmeshInfo)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idcolor[3]) 
        if  mlInfo:
            mc.select(mlInfo)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idcolor[4])                                                           
        return 0        
#�ƹ�ѡ��
    def csl_lightInfoList(self,Type='set',lightType='group'):
        lights=mc.ls(lt=1,l=1)
        lightInfoList=[]
        if lights:
            for light in lights:
                lightP=light.split('|')
                for lig in lightP:
                    if Type=='chr' and lightType=='group' and 'msh_chr_light' in lig.lower():
                        lightInfoList.append(lig)
                    if Type=='set' and lightType=='group' and 'msh_set_light' in lig.lower():  
                        lightInfoList.append(lig)
                if Type=='chr' and lightType=='key' and 'msh_chr_light' in light.lower() and 'keylight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chr' and lightType=='fill' and 'msh_chr_light' in light.lower() and  'filllight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])  
                if Type=='chr' and lightType=='rim' and 'msh_chr_light' in light.lower() and  'rimlight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0]) 
                if Type=='set' and lightType=='key' and 'msh_set_light' in light.lower() and 'keylight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='fill' and 'msh_set_light' in light.lower() and  'filllight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])  
                if Type=='set' and lightType=='rim' and 'msh_set_light' in light.lower() and  'rimlight' in light.lower(): 
                    ligt=mc.listRelatives(light,p=1,f=1)
                if Type=='set' and lightType=='all' and 'msh_set_light' in light.lower() : 
                    ligt=mc.listRelatives(light,p=1,f=1)                    
                    lightInfoList.append(ligt[0])                                                                                                  
        return  lightInfoList
#keylight filllight rimlight �� RGB
          
    def csl_LightAssign(self,Type='chr'):             
        keyLight=self.csl_lightInfoList(Type,lightType='key')
        fillLight=self.csl_lightInfoList(Type,lightType='fill')
        rimLight=self.csl_lightInfoList(Type,lightType='rim')  
        if  keyLight:      
            for key in keyLight:
                keyLightShape=mc.listRelatives(key,s=1,f=1)
                if keyLightShape:
                    mc.setAttr((keyLightShape[0]+'.color'),1,0,0,type = 'double3')
                    mc.setAttr((keyLightShape[0]+'.shadowColor'),0,0,0,type = 'double3') 
        if  fillLight:       
            for fill in fillLight:
                fillLightShape=mc.listRelatives(fill,s=1,f=1)
                if fillLightShape:
                    mc.setAttr((fillLightShape[0]+'.color'),0,1,0,type = 'double3')
                    mc.setAttr((fillLightShape[0]+'.shadowColor'),0,0,0,type = 'double3')                              
        if  rimLight:       
            for rim in rimLight:
                rimLightShape=mc.listRelatives(rim,s=1,f=1)
                if rimLightShape:
                    mc.setAttr((rimLightShape[0]+'.color'),0,0,1,type = 'double3')
                    mc.setAttr((rimLightShape[0]+'.shadowColor'),0,0,0,type = 'double3') 
        return 0
    
#ѡ�����mesh
    def csl_meshInfo(self,meshtype='s'):
        meshs=mc.ls(type='mesh',l=1)
        meshList=[]
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        for i in range(len(meshs)):
            for j in range(len(namespaces)) :
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0]==meshtype:
                    meshP=mc.listRelatives(meshs[i],p=1,f=1)
                    if meshP:
                        meshList.append(meshP[0])
        return meshList 

                                 
#����������Ϣ
    def csl_Attrlist(self,attrtype='GD'):
        objList=[]
        objs=mc.ls(type='transform',l=1)
        if objs: 
            for obj in objs:
                if mc.objExists(obj+'.'+attrtype) and mc.getAttr(obj+'.'+attrtype)==1:
                     objList.append(obj)
        return objList 
# GD mehs ����list
    def csl_GDMeshList(self,attrtype='GD'):
        setmesh=self.csl_Attrlist(attrtype)
        meshshapes=[]
        errormesh=[]
        if setmesh:
            for mesh in setmesh:
                cmeshs=mc.listRelatives(mesh,c=1,f=1)
                if cmeshs:
                    for cmesh in cmeshs:
                        if mc.nodeType(cmesh)=='mesh':
                            meshshapes.append(cmesh)
                        if mc.nodeType(cmesh)=='transform':
                            mshapes=mc.listRelatives(cmesh,c=1,f=1)
                            for shape in mshapes:
                                if mc.nodeType(shape)=='mesh':
                                    meshshapes.append(shape)
                                if mc.nodeType(shape)=='transform':  
                                    shapes=mc.listRelatives(shape,c=1,f=1)
                                    for fshape in shapes:
                                        if mc.nodeType(fshape)=='mesh': 
                                             meshshapes.append(shape)
                                        else:
                                            errormesh.append(shape)
        return [meshshapes, errormesh] 

# ��shape ������Ը���shapeD(maya2013��汾���ã�
    def csl_ShapeInfoApply(self,infoType='aiOpaque'):
        meshs=mc.ls(sl=1,l=1)
        Shape=[]
        ShapeDeformed=[]
        if meshs:
            for mesh in meshs:
                shapes=mc.listRelatives(mesh,s=1,type='mesh',f=1)
                if shapes and len(shapes)==2 and mc.objExists(shapes[0]+'.'+infoType)==True:
                    info=mc.getAttr(shapes[0]+'.'+infoType)
                    Shape.append(shapes[0])
                    ShapeDeformed.append(shapes[1])
                    try: 
                        mc.setAttr((shapes[1]+'.'+infoType) ,info)
                    except:
                        pass 
                if shapes and len(shapes)>2 and mc.objExists(shapes[0]+'.'+infoType)==True and re.search('Deformed',shapes[-1])!=None:
                    info=mc.getAttr(shapes[0]+'.'+infoType)
                    Shape.append(shapes[0])
                    ShapeDeformed.append(shapes[-1])
                    try: 
                        mc.setAttr((shapes[-1]+'.'+infoType) ,info)
                    except:
                        pass                                 
        return Shape                                                                                                                                                                                           
#ʱ���¼
    def csl_RendertimeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())) 

    def csl_SetRefGet(self,ref=1):
        refNamespace=[]
        setRef=[]        
        if ref==1:
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNamespace=refInfos[2][0]
            if 'CAM' in refNamespace:
                refNamespace.remove('CAM')            
        else:
            refNamespace=mc.namespaceInfo(listOnlyNamespaces=1)                         
        if refNamespace:
            for ns in  refNamespace:
                if '_' in ns and ns.split('_')[1][0]=='s':                                                                                                   
                    setRef.append(ns) 
        return setRef        

    def csl_SetRefZD(self): 
        set= self.csl_SetRefGet(0)[0].split('_') 
        Shade='SHD_Zdp_arnold'
        if set[1]=='s004001GobiDesert':
            mc.setAttr((Shade+'.farClipPlane'),25000) 
        if set[1]=='s004002Desert':
            mc.setAttr((Shade+'.farClipPlane'),30000) 

    def csl_camRenderSet(self,shortType=3,serve=0):
        import re
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        shortName=mc.file(q=1,sn=1,shn=1)
        tempath='D:/Info_Temp/temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        shotName='' 
        if shortType==2:
            shotName= shotInfo[1]+'_'+shotInfo[2] 
        if shortType==3:
            shotName= shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3] 
        camname='cam_'+shotName+'_baked'                                
        cams=mc.ls(ca=1,l=1)
        if '|front|frontShape' in cams:
            mc.setAttr('|front|frontShape.renderable',0)            
            cams.remove('|front|frontShape')
        if '|persp|perspShape' in cams:
            mc.setAttr('|persp|perspShape.renderable',0)                     
            cams.remove('|persp|perspShape')
        if '|side|sideShape' in cams:
            mc.setAttr('|side|sideShape.renderable',0)   
            cams.remove('|side|sideShape')
        if '|top|topShape' in cams:
            mc.setAttr('|top|topShape.renderable',0)   
            cams.remove('|top|topShape')
        if  len(cams)==1:
            cam=mc.listRelatives(cams[0],p=1,f=1)[0]
            if cam.split(':')[-1] == camname:
                mc.setAttr((cams[0]+'.renderable'),1)
            else:
                mc.error(u'����������ļ���û����ȷ���')           
        if len(cams)==0:
            mc.error(u'����������ļ���ȱ�پ�ͷ���') 
        if len(cams)>1 :
            mc.error(u'����������ļ����ж������') 
        if serve==1:
            userName = os.environ['USERNAME']            
            mc.file(rename=(tempath+shortName))                
            mc.file(save=1,type ='mayaBinary',f = 1)
            fname=shortName.split(shotInfo[0]+'_')[1].split('_c0')[0]
            fileInfo='1|' + projectInfo + '|' + fname+'|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd) 
            description = u'�޸Ŀ���Ⱦ����ļ�'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print (u'===============!!!End��%s��!!!===============' % (u'%s_���ϴ��ļ�' % shortName))                            
        return camname                                               
#�ж��ļ����Ƿ��н�ɫ�����ߣ��ο��������ο������ж�֮��ֲ㷽��
    def csl_refconditionref(self):
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

#�ж��ļ����Ƿ��н�ɫ�����ߣ�namespace�������ο������ж�֮��ֲ㷽��(�ο�����Ҳ�����ã�
    def csl_refcondition(self):
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1) 
        setRef=[]
        chpRef=[]
        for ns in namespaces:
            if '_' in ns and ns.split('_')[1][0] in ['s', 'S']:
                setRef.append(ns)    
            if '_' in ns and ns.split('_')[1][0] in ['c','p']:
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
 
 # �����ļ�
    def csl_FileSet(self,shotType=3):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] 
               
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
        # �ֱ���
        mc.setAttr(('defaultResolution.width'), resW)
        mc.setAttr(('defaultResolution.height'), resH)
        # FPS
        if fpsFrame == 25:
            mc.currentUnit(time='pal')
        if fpsFrame == 24:
            mc.currentUnit(time='film')
        if fpsFrame == 30:
            mc.currentUnit(time='ntsc')
        # frame
        if startFrame and fpsFrame:
            # ��ʼ֡
            mc.playbackOptions(min=startFrame)
            # ��ʼԤ��
            preStartFrame = startFrame - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # ����֡
            mc.playbackOptions(max=endFrame)
            # ����Ԥ��
            posEndFrame = endFrame + 12
            mc.playbackOptions(animationEndTime=posEndFrame)
        # ����֡����ģʽÿ֡
        mc.playbackOptions(playbackSpeed=0)
            
        # ����undo
        mc.undoInfo(state=True, infinity=True) 
        # ���õ�ǰ֡��
        mc.currentTime(startFrame)
        # ����
        mel.eval('setMayaSoftwareFrameExt(3, 0)') 
        # ������Ⱦ֡��
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)      
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        # ����ļ����� 

# ����motionblur �ֲ� 
    def csl_MotionblurLayerAuto(self,shotType=3,server=1):
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================��%s���ļ��ֲ㿪ʼ==========================' % FileName        
        self.csl_RendertimeRecord()        
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
        tempath='D:/Info_Temp/temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        #��Ҫ�������ļ����ƣ�
        #��ɫ�ļ����������ߣ�
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #�����ļ�  
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType 
        #��ɫ���������ļ�              
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #��ɫ�ƹ��ļ� 
        chrlightName=Project+'_'+shotName+'_'+'chrlight_lr_c001.'+fileType
        
        #01�������볡��
        self.csl_RenderEnvLoad()
        print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���볡���ο�' % FileName))        
        #smooth����        
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start ��%s��!!!===============' % (u'%s_smooth����' % FileName)) 
        #�ο��жϣ��ļ��Ƿ��н�ɫ���������ߣ�������  
        refconinfo=self.csl_refcondition()                                        
        #02--������ɫ�ļ� 
        if refconinfo[0]==1:       
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫ�ļ�' % ChabaseName))        
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[2]:
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)            
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_������ɫ�ļ�' % ChabaseName))
        #03--���������ļ�
        if refconinfo[1]==1: 
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���������ļ�' % SetbaseName))          
            mc.select(self.csl_GroupSelect()[1])
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1) 
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            csl_checkin.csl_checkin().csl_timeRecord()
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���������ļ�' % SetbaseName))

            chaMoblurName=Project+'_'+shotName+'_'+'l1chrMotionBlur_lr_c001.'+fileType
            setMoblurName=Project+'_'+shotName+'_'+'l1setMotionBlur_lr_c001.'+fileType
            setmoblurLayerName='set_motionblur'            
        #04--��ɫmotionblur   

     #��ɫ motion�ļ� 
        if refconinfo[0]==1:                  
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaMoblurName))                
            mc.file(save=1,type = fileTypeAll,f = 1)
        #��Ⱦ��������
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('mob')          
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()') 
            moblurLayerName='chr_motionblur'
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            meshs=meshchr+meshprp
            mc.select(meshs)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldMotionBlurShaderCreate()
            mc.createRenderLayer(meshs,name=moblurLayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            self.csl_FileSet(shotType)  
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('mob')               
    #   ����Ⱦ�������
    
            self.csl_camRenderSet(shotType,serve=0)            
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            print u'\n'
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_������ɫmotionblur�ļ�' % chaMoblurName))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1chrMotionBlur_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'��ɫmothionblur�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_���ϴ���ɫ�ļ�' % chaMoblurName)) 

     #���� motion�ļ�               
        if refconinfo[1]==1: 
            print (u'===============!!!Start ��%s��!!!===============' % (u'%s_��������motionblur�ļ�' % setMoblurName))
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('mob')
            mc.file(rename=(tempath+setMoblurName))                
            mc.file(save=1,type = fileTypeAll,f = 1)
            hh_RenderArnoldLayer.hh_RenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()') 
            meshs=self.csl_meshInfo(meshtype='s')
            mc.select(meshs)
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldMotionBlurShaderCreate()
            mc.createRenderLayer(meshs,name=setmoblurLayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            self.csl_FileSet(shotType)  
            hh_RenderArnoldLayer.hh_RenderArnold().ArnoldRendererSettings('mob')            
    #   ����Ⱦ�������
            self.csl_camRenderSet(shotType,serve=0) 
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1setMotionBlur_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'����mothionblur�ļ�'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
            print (u'===============!!!End ��%s��!!!===============' % (u'%s_���ϴ�����motionblur�ļ�' % setMoblurName)) 
#Load�ǳ����ο� 
    def csl_RefLoad(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        if mc.ls('CAMRN'):
            mc.file(loadReference='CAMRN')
            refRN.remove('CAMRN')
        refFile=refInfos[1][0]
        for i in range(len(refRN)):
            if refRN[i].split('_')[1][0] not in ['s', 'S']:
                try:
                    mc.file(loadReference=refRN[i])
                except:
                    pass
        return 0
#SG����
    def csl_RestSG(self):
        objs=mc.ls(sl=1,l=1)       
        if objs:
        	for obj in objs:
        		shapes=mc.listRelatives(obj,s=1,f=1)
        		if shapes:
        			SGN=mc.listConnections(shapes[0],destination = 1,type = 'shadingEngine')
        			for i in range(len(shapes)):
        				if len(shapes)>1 and i>0 and mc.nodeType(shapes[i])=='mesh' and SGN !=None :
    						try:							
    							mc.sets(shapes[i],e=1,forceElement=SGN[0])
    						except:
    							pass 
        return 0            			
# �������ʸ���
    def csl_ResetMat(self,shortType=3,serve=0) :
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================��%s���������ÿ�ʼ==========================' % FileName        
        self.csl_RendertimeRecord()        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0]) 
        userName = os.environ['USERNAME']       
        Project=shotInfo [0]
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]  
        tempath='D:/Info_Temp/temp/RenderLayer/ResetMat/'+shotInfo[1]+'/' 
        mc.sysFile(tempath, makeDir=True)
        # �ָ����Ӽ��������
        meshchr=self.csl_meshInfo(meshtype='c')
        meshprp=self.csl_meshInfo(meshtype='p')
        objs=meshchr+meshprp
        if objs:
            mc.select(objs)
            self.csl_RestSG()
            self.csl_ShapeInfoApply(infoType='aiOpaque') 
#smooth����        
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0) 
        hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)            
        #�汾��
        mc.file(rename=(tempath+FileName))                
        mc.file(save=1,type = 'mayaBinary',f = 1)
        if serve==1:
            fileInfo='1|' + projectInfo + '|'  + FileName.split('_c00')[0] +'|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd) 
            description = u'���ʸ����ļ�'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
        print (u'==========================��%s���������ý���==========================' % FileName )             
         
            

    def csl_checkReferenceShaderReset(self,configType = 0 , assetType = 0):
        # ��ȡ�ļ��ڲο���Ϣ
    	refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
    	refNodes = refInfos[0][0]
    	if refNodes:
    	    checkTypes = ['setAttr','connectAttr','disconnectAttr','addAttr','parent']
    	    for checkType in checkTypes:
    	        # ���Ĺ���������Ϣ
    	        modifyInfos = []
    	        for refNode in refNodes:
    	            if 'CAM' not in refNode :
    	                #print refNode
    	                if configType == 1:
    	                    modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
    	                if configType == 0:
    	                    if refNode.split('_')[1][0] not in ['s', 'S']:
    	                        modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
    	        if modifyInfos:
    	            # ��Ҫ��ӭ��SG�����Ϣ
    	            resetShaderInfo = []
    	            resetUVInfo = []
    	            for info in modifyInfos:
    	                if 'SG' in info :
    	                    if '\"' in info:
    	                        needInfo = info.split('\"')[1]
                                #print needInfo
                                resetShaderInfo.append(needInfo)
                        if '.uv' in info :
                            #print '-----------'
                            print info
                            needInfo = info.split(' ')[1]
                            #print needInfo
                            resetUVInfo.append(needInfo)
                        if 'initialShadingGroup.dagSetMembers' in info:
                            print info
                            needInfo = info.split('\"')[1]
                            #print needInfo
                            resetShaderInfo.append(needInfo)
                    # ��ʼ��ӭ
                    if resetShaderInfo:
                        for info in resetShaderInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)
                    if resetUVInfo:
                        for info in resetUVInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)  

    def csl_HideList(self): 
        objs=mc.ls(type='transform',l=1)
        HideInfo=['_sky_']
        HideList=[]
        if objs:
            for i in range(len(objs)):
                for j in range(len(HideInfo)): 
                    if  HideInfo[j] in objs[i]:
                        HideList.append(objs[i])
        if HideList:
            for Hide in HideList:
                mc.setAttr((Hide+'.visibility'),0)
        return 0

    #------------------------------#
    # �����ġ� �������ļ�����
    #------------------------------#
    # ���ݲο������ļ� 0 ��ɾ���������壬������OTC | 1 ɾ����������
    # finalLayout����������Լ���ٴ������
    def sk_sceneReorganize(self, finalLayout=0):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRoot = []
        refNodes = []
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            # ȫ������
            refObjs = mc.referenceQuery(refNode , nodes=1,dagPath = 1)
            # Q,need to test
            if refObjs:
                refRoot.append(refObjs[0])
        # CAM_GRP
        if mc.ls('CAM_GRP'):
            camGrp = 'CAM_GRP'
        else:
            camGrp = mc.group(em=1, name='CAM_GRP')
        # CHR_GRP
        if mc.ls('CHR_GRP'):
            chrGrp = 'CHR_GRP'
        else:
            chrGrp = mc.group(em=1, name='CHR_GRP')
        # PRP_GRP
        if mc.ls('PRP_GRP'):
            prpGrp = 'PRP_GRP'
        else:
            prpGrp = mc.group(em=1, name='PRP_GRP')
        # SET_GRP
        if mc.ls('SET_GRP'):
            setGrp = 'SET_GRP'
        else:
            setGrp = mc.group(em=1, name='SET_GRP')
        # VFX_GRP
        if mc.ls('VFX_GRP'):
            vfxGrp = 'VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        # ��Ⱥ��Ⱥ
        if mc.ls('Cluster_GRP'):
            clusterFlowGrp = 'Cluster_GRP'
        else:
            clusterFlowGrp = mc.group(em=1, name='Cluster_GRP')
        # OTC_GRP
        if mc.ls('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # ����
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)
        if otcGrp not in mc.ls(clusterFlowGrp, l=1)[0]:
            mc.parent(clusterFlowGrp, otcGrp)
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # ��ʼ����
        # ���ȼ�¼������namespace�Ļ���GRP
        ogGrp = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        ogNsGrp = []
        for grp in ogGrp:
            checkGrps = mc.ls(('*:*' + grp + '*'),l=1) + mc.ls(('*:*:*' + grp + '*'),l=1)
            if checkGrps:
                for obj in checkGrps:
                    lastName = obj.split(':')[-1]
                    ogNsGrp.append(obj[0:-1*(len(lastName)+1)])
        ogNsGrp = list(set(ogNsGrp))
        print refRoot
        # 1Ϊ�ο���ʽ����
        # �����ʽ��VFX����Ӱ��,����Ҫ����
        for root in refRoot:
            # �����ж��Ƿ���VFX_GRP��Cluster_GRP
            if '|VFX_GRP|' not in mc.ls(root, l=1)[0] and 'Cluster_GRP' not in mc.ls(root, l=1)[0]:
                print root
                refPath = mc.referenceQuery(root, filename=1)
                path = refPath.lower()
                # CAM
                if '/camera/' in path or '/episode_camera/' in path:
                    # �ж��Ƿ���CAM_GRP����
                    if ('|' + camGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, camGrp)
                # CHR
                if '/characters/' in path:
                    # �ж��Ƿ���CHR_GRP����
                    if ('|' + chrGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, chrGrp)
                    else:
                        # �����ϼ�������RNgroup��������
                        upGrp = mc.listRelatives(root,p=1,f=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, chrGrp)
                                mc.delete(upGrp)
                # PRP
                if '/props/' in path:
                    # �ж��Ƿ���PRP_GRP����
                    if ('|' + prpGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, prpGrp)
                    else:
                        # �����ϼ�������RNgroup��������
                        upGrp = mc.listRelatives(root,p=1,f=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, prpGrp)
                                mc.delete(upGrp)
                # SET
                if '/sets/' in path or '/environments/' in path:
                    # �ж��Ƿ���SET_GRP����
                    if ('|' + setGrp + '|') not in mc.ls(root , l=1)[0]:
                        mc.parent(root , setGrp)
                    else:
                        # �����ϼ�������RNgroup��������
                        upGrp = mc.listRelatives(root,p=1,f=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                # ���ڲο����Ӳο�ʹ��try
                                try:
                                    mc.parent(root, setGrp)
                                    mc.delete(upGrp)
                                except:
                                    pass
        # �����ⲿԼ��֮��ģ���outLine��ʽ����
        allGrps = mc.ls(assemblies=True)
        for root in allGrps:
            if finalLayout == 1 and root not in needRoot:
                try:
                    mc.delete(root)
                except:
                    pass
            if finalLayout == 2:
                if root:
                    if root not in keepRoot:
                        mc.parent(root , 'OTC_GRP')
        # ������Ҫ��namespace
        if ogNsGrp:
            import sk_pyCommon
            reload(sk_pyCommon)
            for ns in ogNsGrp:
                sk_pyCommon.sk_pyCommon().sk_deleteNamespace(ns) 
# ���ݿ��ȡ
    def csl_DataGridViewRead(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotName=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]    
        dt = idmt.pipeline.db.GetRcByEpsc(shotName)
        val=dt.values()
        return val
#�ļ�����
#def csl 

    def csl_ResolutionRead(self):
        withs=mc.getAttr('defaultResolution.width')
        height=mc.getAttr('defaultResolution.height')
        Device=mc.getAttr('defaultResolution.deviceAspectRatio')
        pixel=mc.getAttr('defaultResolution.pixelAspect')
        print [withs,height,Device,pixel]
        
                                                                      
                                                                                                                                                                                                                                                                                            