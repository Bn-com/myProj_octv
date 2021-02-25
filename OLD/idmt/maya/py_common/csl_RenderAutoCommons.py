# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')


#渲染后台

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm

from idmt.maya.py_common import sk_infoConfig
reload(sk_infoConfig)


from idmt.maya.py_common import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.py_common import GDC_ArnoldCommon
reload(GDC_ArnoldCommon)


import os
import re
class csl_RenderAutoCommons(object):
    def __init__(self):
        # namespace清理
        pass

    def csl_RenderLayerAuto(self,shotType=3,server=1):
        self.changeFilePathToDollarPath()
        FileName=mc.file(q=1,sn=1,shn=1)
        # 加载参考
        self.checkRefUnload2Load()
        # 转路径
        import csl_VariablePathSwitch
        reload(csl_VariablePathSwitch)
        csl_VariablePathSwitch.csl_VariablePathSwitch().csl_VariableSwitch(abc=1,aiimage=1)
        print u'==========================【%s】文件分层开始==========================' % FileName
        # 初始化灯光
        shotDict = self.ydRLReadEXcle()
        setIDList = shotDict['setID']
        nsList = mc.namespaceInfo(listOnlyNamespaces=1)
        setNsList = []
        for checkNs in nsList:
            if '_' not in checkNs:
                continue
            if checkNs.split('_')[1] in setIDList:
                setNsList.append(checkNs)

        if not setNsList:
            errorInfo = u'\n-----Can not find set %s-----\n'%setIDList
            print errorInfo
            mc.error()

        allLgtGrps = mc.ls('*:MSH_Set_light',type='transform')+mc.ls('*:MSH_Chr_light',type='transform')
        chrLgtGrp = []
        setLgtGrp = []
        for checkGrp in allLgtGrps:
            checkState = 0
            for setNs in setNsList:
                if setNs not in checkGrp:
                   checkState = 1
            if not checkState:
                mc.setAttr(checkGrp+'.v',0)
            if 'MSH_Set_light' in checkGrp:
                setLgtGrp.append(checkGrp)
            if 'MSH_Chr_light' in checkGrp:
                chrLgtGrp.append(checkGrp)

        timeInfo = shotDict['time']
        for checkGrp in (chrLgtGrp+setLgtGrp):
            if not checkGrp:
                continue
            childGrps = mc.listRelatives(checkGrp,c=1,type = 'transform',f=1)
            for childGrp in childGrps:
                if ':%s_'%timeInfo in childGrp:
                    mc.setAttr(childGrp+'.v',1)
                else:
                    mc.setAttr(childGrp+'.v',0)

        # 开始处理
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
        tempath='D:/Info_Temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        mc.sysFile(tempath, makeDir=True)
        #   记录帧数信息
        self.csl_AnimFramInfoWrite(shotType)
        #   文件打组
        self.sk_sceneReorganize(0)
        #需要导出的文件名称：
        #        fileType=['cha','set','cs','chrlight','setlight']
        #角色文件（包括道具）
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #场景文件
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType
        #角色场景互动文件
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #角色灯光文件
        chrlightName=Project+'_'+shotName+'_'+'chrlight_lr_c001.'+fileType

        #01——载入场景
        self.csl_RenderEnvLoad()
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_载入场景参考' % FileName))
        #smooth设置
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_smooth设置' % FileName))
        #隐藏
        self.csl_HideList()
        #参考判断（文件是否有角色（包含道具），场景
        refconinfo=self.csl_refcondition()
        #02--导出角色文件
        if refconinfo[0]==1:
            self.csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[2]:
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
        #03--导出场景文件
        if refconinfo[1]==1:
            self.csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))
            mc.select(self.csl_GroupSelect()[1])
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))
        #04--导出场景角色互动文件
        if refconinfo[0]==1 and refconinfo[1]==1:
            self.csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[1]:
                mc.select(self.csl_GroupSelect()[1],add=1)
            if self.csl_GroupSelect()[2]:
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+CSbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % CSbaseName))
        #05--导出角色灯光文件
        if refconinfo[0]==1 and refconinfo[1]==1:
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色灯光文件' % chrlightName))
            #删除OTC
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()

            if mc.ls('OTC_GRP'):
                mc.delete('OTC_GRP')
            # sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
            lightgroups=self.csl_lightInfoList(Type='chr',lightType='group')
            lightInfo=[]
            if lightgroups:
                for i in range(len(lightgroups)):
                    if mc.ls(lightgroups[i]):
                        lightInfo.append(lightgroups[i])
            else:
                mc.error( u"没有角色灯光组或角色灯光组命名不正确，请与环节负责人联系" )
            if lightInfo:
                for j in range(len(lightInfo)):
                    if mc.objExists(lightInfo[j]+'.visibility'):
                        mc.setAttr((lightInfo[j]+'.visibility'),1)
                mc.select(lightInfo)
                mc.file((tempath+chrlightName),options='v=0',f=1,type=fileTypeAll,es=1)
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已导出角色灯光文件' % chrlightName))
            else:
                mc.error( u"没有角色灯光组或角色灯光组命名不正确，请与环节负责人联系" )
            #角色文件
        if refconinfo[0]==1 :
            self.csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_角色文件设置' % ChabaseName))
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('03')
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            chaColorName=Project+'_'+shotName+'_'+'l2chrcolor_lr_c001.'+fileType
            chaAOVName=Project+'_'+shotName+'_'+'l5chrAOV_lr_c001.'+fileType
            chaMoblurName=Project+'_'+shotName+'_'+'l1chrMotionBlur_lr_c001.'+fileType
            chaID01Name=Project+'_'+shotName+'_'+'l3chrIDP01_lr_c001.'+fileType
            chaID02Name=Project+'_'+shotName+'_'+'l1chrIDP21_lr_c001.'+fileType
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_角色文件设置' % ChabaseName))
            #角色color文件
            self.csl_timeRecord()
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色color文件' % chaColorName))
            #导入角色灯光文件
            if refconinfo[1]==1 :
                mc.file((tempath+chrlightName),i=1,pr=1,namespace=chrlightName.split('.')[0])
            if refconinfo[1]==0:
                chalightpath='Z:/Projects/ShunLiu/Project/data/ChrLight/'+shotName+'/'
                chalightName=shotName+'_chr_light.mb'
                try:
                    mc.file((chalightpath+chalightName),i=1,pr=1,namespace=chrlightName.split('.')[0])
                except:
                    mc.error(u'==========================缺少灯光文件【%s】==========================' % (chalightpath+chalightName))
            mc.file(rename=(tempath+chaColorName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')
            meshs=meshchr+meshprp+lightgroup
            #       将shape 透明信息继承给shapeDeform(适用于maya2013后）
            mc.select(meshchr+meshprp)
            self.csl_ShapeInfoApply(infoType='aiOpaque')

            colorlayerName='chr'
            mc.createRenderLayer(meshs,name=colorlayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='sss')
            #渲染精度设置
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('03')
            #    可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
            #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            # 存盘
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            self.csl_timeRecord()
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_创建角色color文件' % chaColorName))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l2chrlight_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'角色color文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色color文件' % chaColorName))
        #角色AOV文件
        if refconinfo[0]==1 :
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            #导入角色灯光文件
            if refconinfo[1]==1 :
                mc.file((tempath+chrlightName),i=1,pr=1,namespace=chrlightName.split('.')[0])
            if refconinfo[1]==0:
                chalightpath='Z:/Projects/ShunLiu/Project/data/ChrLight/'+shotName+'/'
                chalightName=shotName+'_chr_light.mb'
                mc.file((chalightpath+chalightName),i=1,pr=1,namespace=chrlightName.split('.')[0])
            mc.file(rename=(tempath+chaAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval("source \"Z:/Resource/Support/OEM/2013/zzjUtilityTools.mel\";lighting_DeleteUnusedNode()")
            aovlayerName='chr_light'
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')
            meshs=meshchr+meshprp+lightgroup
            mc.createRenderLayer(meshs,name=aovlayerName, noRecurse=1, makeCurrent=1)
            #隐藏天光
            skylight=mc.ls('*:*:*skylight*')
            if skylight:
                for i in range(len(skylight)):
                    mc.setAttr((skylight[i]+'.v'),0)
            mc.editRenderLayerGlobals(currentRenderLayer=aovlayerName)
            mc.select(meshs)


            #赋lambert材质
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldShaderAssign(shaderType='Lambert',transparency=0)
            #key fill rim  R G B
            self.csl_LightAssign(Type='chr')
            mc.setAttr("defaultRenderLayer.renderable", 0)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='AO')
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Normal')
    #        GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Shadow')
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Fre')
    #        GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='motionvector')
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
        # 渲染精度设置
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色非灯光层文件' % chaAOVName))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l5chrAOV_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'角色AOV文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色文件' % chaAOVName))
#     #角色 motion文件
#            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
#            mc.file(rename=(tempath+chaMoblurName))
#            mc.file(save=1,type = fileTypeAll,f = 1)
#        #渲染精度设置
#            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
#            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
#            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
#            moblurLayerName='cha_motionblur'
#            meshchr=self.csl_meshInfo(meshtype='c')
#            meshprp=self.csl_meshInfo(meshtype='p')
#            meshs=meshchr+meshprp
#            mc.select(meshs)
#            GDC_ArnoldCommon.GDCRenderArnold().ArnoldMotionBlurShaderCreate()
#            mc.createRenderLayer(meshs,name=moblurLayerName, noRecurse=1, makeCurrent=1)
#            mc.setAttr("defaultRenderLayer.renderable", 0)
#            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
#    #   可渲染相机设置
#            self.csl_camRenderSet(shotType,serve=0)
#            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
#            print u'\n'
#            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色motionblur文件' % chaMoblurName))
#            if  server==1  :
#                fileInfo='1|' + projectInfo + '|' + shotName + '_l1chrMotionBlur_lr|' + userName
#                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
#                mel.eval(checkOutCmd)
#                description = u'角色mothionblur文件'
#                # checkIn
#                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
#            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_已完成角色文件' % chaMoblurName))
            #角色idpass01文件
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaID01Name))
            mc.file(save=1,type = fileTypeAll,f = 1)
            GDC_ArnoldCommon.GDCRenderArnold().csl_IDRenderLayerCreatAll(type="chr",ref=1)
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.file(save=1,type = fileTypeAll,f = 1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色idpass01文件' % chaID01Name))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3chrIDP01_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'角色id文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色文件' % chaID01Name))
            #随机idp
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaID02Name))
            mc.file(save=1,type = fileTypeAll,f = 1)
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            if 1 > 0: #测试每层三个角色分别是RGB
                self.csl_setRGBPerLayer()
            else:
                meshchr=self.csl_meshInfo(meshtype='c')
                meshprp=self.csl_meshInfo(meshtype='p')
                meshs=meshchr+meshprp
                mc.select(meshs)
                mc.createRenderLayer(meshs,name='chr_id21', noRecurse=1, makeCurrent=1)
                mc.setAttr("defaultRenderLayer.renderable", 0)
                self.csl_id21Render()
        #渲染精度设置
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色idpass21文件' % chaID02Name))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3chrIDP01_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'角色id21文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色文件' % chaID02Name))
# 场景文件处理：
        #场景AOV文件
        #文件名
        if refconinfo[1]==1:
            setAOVName=Project+'_'+shotName+'_'+'l6setAOV_lr_c001.'+fileType
            setMoblurName=Project+'_'+shotName+'_'+'l1setMotionBlur_lr_c001.'+fileType
            setIDName=Project+'_'+shotName+'_'+'l3setIDP11_lr_c001.'+fileType
            #层名
            setAOVlayerName='set'
            setmoblurLayerName='set_motionblur'
            #打开场景文件
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景AOV文件' % setAOVName))
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('03')
            mc.file(rename=(tempath+setAOVName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            meshs=self.csl_GroupSelect()[1][1]
            mc.createRenderLayer(meshs,name=setAOVlayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='AO')
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Normal')
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Zdp')
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='Fre')
    #        GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='motionvector')
    #根据不同MS设置zdp
            self.csl_SetRefZD()
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.setAttr('defaultArnoldDriver.prefix','<RenderLayer>_<RenderPass>/<Scene>_<RenderLayer>_<RenderPass>',type='string')
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l6setAOV_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'场景AOV文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成场景AOV文件' % setAOVName))
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景idpass11文件' % setIDName))
    # 场景ID文件
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+setIDName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            mc.select(self.csl_GroupSelect()[1])
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+setIDName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            mc.file((tempath+setIDName),options='v=0',type=fileTypeAll,f=1,o=1)
        #渲染精度设置
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
        #隐藏场景灯光
            setLights=self.csl_lightInfoList(Type='set',lightType='all')
            if  setLights:
                for light in setLights:
                    try:
                        mc.setAttr((light+'.visibility'),0)
                    except:
                        pass
        #关闭场景meshLight:
            setmesh=self.csl_meshInfo(meshtype='s')
            if setmesh:
                for mesh in setmesh:
                    try:
                        mc.setAttr((light+'.lightVisible'),0)
                    except:
                        pass

            GDC_ArnoldCommon.GDCRenderArnold().csl_IDRenderLayerCreatAll(type='set',ref=1)
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.file(save=1,type = fileTypeAll,f = 1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l3setIDP11_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'场景id文件'
                #checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成场景idpass11文件' % setIDName))
#场景角色互动文件处理
        if refconinfo[0]==1 and refconinfo[1]==1:
            CSSetName=Project+'_'+shotName+'_'+'l2setcon_lr_c001.'+fileType
            CSidp31=Project+'_'+shotName+'_'+'l1idp31_lr_c001.'+fileType
            shadowLayer='conshadow'
            id31Layer='id31'
            #shadow conocc
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建CONS文件' % CSSetName))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            mc.file(save=1,type = fileTypeAll,f = 1)
            mc.file(rename=(tempath+CSSetName))
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.file(save=1,type = fileTypeAll,f = 1)
     #显示角色灯光
            lightgroup=self.csl_lightInfoList(Type='chr',lightType='group')[0]
            if (lightgroup+'.visibility'):
                mc.setAttr((lightgroup+'.visibility'),1)
        #删除场景灯光
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
    #设置属性
            if chameshs:
                for mesh in chameshs:
                    shapes=mc.listRelatives(mesh,s=1,f=1)
                    if shapes:
                        for shape in shapes:
                            if mc.nodeType(shape)=='mesh':
                                try:
                                    mc.setAttr((shape+'.primaryVisibility'),0)
                                except:
                                    pass
            if setshpes:
                if setshpes[0] :
                    for shape in setshpes[0]:
                        try:
                            mc.setAttr((shape+'.castsShadows'),0)
                            mc.setAttr((shape+'.lightVisible'),0)
                        except:
                            pass
                else:
                    mc.warning(u'文件中没有GD物体')
                if setshpes[1] :
                    for errormesh in setshpes[1]:
                        mc.warning(errormesh+':'+u'物体层级超过三层，请检查')
            if keylight:
                for key in keylight:
                    shapes=mc.listRelatives(keylight,s=1,f=1)
                    if shapes and re.search(('Light'), mc.nodeType(shapes[0]))!=None:
                        try:
                            mc.setAttr((shapes[0]+'.color'),1,1,1,type = 'double3')
                            mc.setAttr((shapes[0]+'.aiAngle'),0)
                            mc.setAttr((shapes[0]+'.shadowColor'),0,0,0,type = 'double3')
                        except:
                            pass
                        try:
                            mc.setAttr((shapes[0]+'.aiSamples'),6)
                            mc.setAttr((shapes[0]+'.aiAffectVolumetrics'),0)
                            mc.setAttr((shapes[0]+'.aiCastVolumetricShadows'),0)

                        except:
                            pass
            meshlights=chameshs+keylight+setmesh
            meshs=chameshs+setmesh
            mc.select(meshs)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldShaderAssign(shaderType='Shadow',transparency=0)
            mc.createRenderLayer(meshlights,name=shadowLayer, noRecurse=1, makeCurrent=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldAOVCreat(AOVtype='AO')
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + 'l2setcon_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'shadow，接触occ文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成场景CS文件' % CSSetName))
    #互动idp31文件
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建idp31' % CSidp31))
            mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('05')
            mc.file(save=1,type = fileTypeAll,f = 1)
            mc.file(rename=(tempath+CSidp31))
            mc.file(save=1,type = fileTypeAll,f = 1)
            chrmesh=self.csl_meshInfo(meshtype='c')
            promesh=self.csl_meshInfo(meshtype='p')+self.csl_objInfo(meshtype='p',objtype='aiStandIn')
            setmesh=self.csl_meshInfo(meshtype='s')+self.csl_objInfo(meshtype='s',objtype='aiStandIn')
            self.csl_id31Creat()
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
    #   动画帧数，渲染尺寸设置
            self.csl_FileSet(shotType=3)
            mc.createRenderLayer((chrmesh+promesh+setmesh),name=id31Layer, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1idp31_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'互动id文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成idp31文件' % CSidp31))

#删除不需要文件
        DeFile=[ChabaseName,SetbaseName,CSbaseName,chrlightName]
        if DeFile:
            for fil in DeFile:
                if fil in mc.getFileList(folder=tempath):
                    try:
                        mc.sysFile((tempath+fil),delete=True)
                    except:
                        pass
#成功代码
        print u'\n'
        print u'==========================【%s】文件分层结束==========================' % FileName
        print u'==========================文件路径【%s】==========================' % tempath
        print u'\n'
        self.csl_RendertimeRecord()
        return 0



# 【辅助】【修改file路径为   ${IDMT_PROJECTS}/】
    #------------------------------#
    def changeFilePathToDollarPath(self):
        mapFiles = mc.ls(type = 'file')
        for f in mapFiles:
            originPath =  mc.getAttr(f + '.fileTextureName')
            if '//file-cluster/GDC/Projects/' in originPath:
                dollarPath = originPath.replace('//file-cluster/GDC/Projects/', '${IDMT_PROJECTS}/')
                mc.setAttr(f + '.fileTextureName', dollarPath, type = 'string')
                print(u'=========================【Change file path to $ path】=========================')


#每层三个角色，每个角色分别是RGB
    def csl_setRGBPerLayer(self):
        chars = mc.ls('*:CHR')

        count = 0
        charsLayer = []

        while count < len(chars):
            tempList = []
            for i in range(3):
                if count < len(chars):
                    tempList.append(chars[count])
                    count += 1
            charsLayer.append(tempList)


        gCount = 1
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB']

        for cc in charsLayer:

            mc.select(chars,r = True)

            charGrp = mc.ls(sl = True)

            mc.createRenderLayer(charGrp,name='chr_id21G' + str(gCount), noRecurse=1, makeCurrent=1)

            for index, g in enumerate(cc):
                mc.select(g, r = True)
                idc=idcolor[index]
                GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idc)

            mGrp = []
            for mg in chars:
                if mg not in cc:
                    mGrp.append(mg)
            if mGrp:
                mc.select(mGrp, r = True)
                GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat('ArnoldIdpM')

            gCount += 1

        mc.setAttr("defaultRenderLayer.renderable", 0)

#选择所有mesh物体
    def csl_meshList(self,meshlist=[],fileType='cha'):
        meshs=mc.ls(type='mesh',l=1)
        if meshs and fileType=='cha':
            for meshShape in meshs:
                if '_ca_' in meshShape:
                    meshp=mc.listRelatives(meshShape,p=1)
                    mesh=mc.ls(meshp[0],l=1)
                    meshlist.append(mesh[0])
        if meshs and fileType=='set':
            for meshShape in meshs:
                meshp=mc.listRelatives(meshShape,p=1)
                mesh=mc.ls(meshp[0],l=1)
                meshlist.append(mesh)
        return meshlist
#Load场景参考
    def csl_RenderEnvLoad(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        caN = mc.ls('CAMRN')
        if caN:
            for n in caN:
                try:
                    refRN.remove(n)
                except:
                    pass

        refFile=refInfos[1][0]
        for i in range(len(refRN)):
            if refRN[i].split('_')[1][0].lower() in ['s']:
                try:
                    mc.file(loadReference=refRN[i])
                except:
                    pass
        return 0


#选择需要导出的（'CHR_GRP','SET_GRP')
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
#应该mesh信息
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
                        if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()=='p':
                            meshList[namespaces[j]]=meshs[i]

            if meshtype=='set':
                for i in range(len(meshs)):
                    for j in range(len(namespaces)) :
                        if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()=='s':
                            meshList[namespaces[j]]=meshs[i]

        return meshList

    def csl_objInfo(self,meshtype='s',objtype='aiStandIn'):
        meshs=mc.ls(type=objtype,l=1)
        meshList=[]
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        namespa=[]
        if namespaces:
            for ns in namespaces:
                if '_' in ns:
                    namespa.append(ns)
        namespaces=namespa
        for i in range(len(meshs)):
            for j in range(len(namespaces)) :
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()==meshtype.lower():
                    meshP=mc.listRelatives(meshs[i],p=1,f=1)
                    if meshP:
                        meshList.append(meshP[0])

        if meshtype.lower() == 's':
            csl_stn = pm.ls('*:*_StandIn*', l = True,type = 'transform') + pm.ls('*:*_ArnoldStandIn*', l = True,type = 'transform')
            for st in csl_stn:
                pg = st.getParent()
                if pg and re.search(r"_grp",pg.name()):
                    meshList.append(pg.name())


        return meshList
#随机idp
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
                    GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idc)
            if len(namespaces)>6:
                for i in range(len(namespaces)):
                    if i <6:
                        idc=idcolor[i]
                        mc.select(namespaces[i])
                        GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idc)
                    if i>6:
                        idc=idcolor[i-int(i/6)*6]
                        mc.select(namespaces[i])
                        GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idc)
        else:
            print u'文件中没有角色道具物体，请检查文件'
        return 0
#角色,道具，场景idp
    def csl_id31Creat(self):
        idcolor=['ArnoldIdpR','ArnoldIdpG','ArnoldIdpB','ArnoldIdpY','ArnoldIdpK']
        chrmeshInfo=self.csl_meshInfo(meshtype='c')
        setmeshInfo=self.csl_meshInfo(meshtype='s')+self.csl_objInfo(meshtype='s',objtype='aiStandIn')
        prpmeshInfo=self.csl_meshInfo(meshtype='p')+self.csl_objInfo(meshtype='p',objtype='aiStandIn')
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
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idcolor[0])
        if  setmeshInfo:
            mc.select(setmeshInfo)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idcolor[1])
        if  gdInfo:
            mc.select(gdInfo)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idcolor[2])
        if  prpmeshInfo:
            mc.select(prpmeshInfo)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idcolor[3])
        if  mlInfo:
            mc.select(mlInfo)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldIDCreat(idcolor[4])
        return 0
#灯光选择
    def csl_lightInfoList(self,Type='set',lightType='group'):
        lights=mc.ls(lt=1,l=1)
        aiAreaLights = mc.ls(type = 'aiAreaLight', l = True)
        lights += aiAreaLights
        aiSkyDomeLights = mc.ls(type = 'aiSkyDomeLight', l = True)
        lights += aiSkyDomeLights
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
#keylight filllight rimlight 赋 RGB

    def csl_LightAssign(self,Type='chr'):
        keyLight=self.csl_lightInfoList(Type,lightType='key')
        fillLight=self.csl_lightInfoList(Type,lightType='fill')
        rimLight=self.csl_lightInfoList(Type,lightType='rim')
        if  keyLight:
            for key in keyLight:
                keyLightShape=mc.listRelatives(key,s=1,f=1)
                if keyLightShape:
                    try:
                        mc.setAttr((keyLightShape[0]+'.color'),1,0,0,type = 'double3')
                        mc.setAttr((keyLightShape[0]+'.shadowColor'),0,0,0,type = 'double3')
                    except:
                        pass
        if  fillLight:
            for fill in fillLight:
                fillLightShape=mc.listRelatives(fill,s=1,f=1)
                if fillLightShape:
                    try:
                        mc.setAttr((fillLightShape[0]+'.color'),0,1,0,type = 'double3')
                        mc.setAttr((fillLightShape[0]+'.shadowColor'),0,0,0,type = 'double3')
                    except:
                        pass
        if  rimLight:
            for rim in rimLight:
                rimLightShape=mc.listRelatives(rim,s=1,f=1)
                if rimLightShape:
                    try:
                        mc.setAttr((rimLightShape[0]+'.color'),0,0,1,type = 'double3')
                        mc.setAttr((rimLightShape[0]+'.shadowColor'),0,0,0,type = 'double3')
                    except:
                        pass
        return 0

#选择相关mesh
    def csl_meshInfo(self,meshtype='s'):
        meshs=mc.ls(type='mesh',l=1)
        meshList=[]
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        namespa=[]
        if namespaces:
            for ns in namespaces:
                if '_' in ns:
                    namespa.append(ns)
        namespaces=namespa
        for i in range(len(meshs)):
            for j in range(len(namespaces)) :
                if namespaces[j] in meshs[i] and namespaces[j].split('_')[1][0].lower()==meshtype.lower():
                    meshP=mc.listRelatives(meshs[i],p=1,f=1)
                    if meshP:
                        meshList.append(meshP[0])
        return meshList


#属性物体信息
    def csl_Attrlist(self,attrtype='GD'):
        objList=[]
        objs=mc.ls(type='transform',l=1)
        if objs:
            for obj in objs:
                if mc.objExists(obj+'.'+attrtype) and mc.getAttr(obj+'.'+attrtype)==1:
                     objList.append(obj)
        return objList
# GD mehs 物体list
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

# 将shape 相关属性赋予shapeD(maya2013后版本适用）
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
#时间记录
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
                if '_' in ns and ns.split('_')[1][0].lower()=='s':
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
        tempath='D:/Info_Temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
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
            cam=mc.listRelatives(cams[0],p=1)[0]
            if cam.split(':')[-1] == camname:
                mc.setAttr((cams[0]+'.renderable'),1)
            else:
                mc.error(u'请检查相机，文件中没有正确相机')
        if len(cams)==0:
            mc.error(u'请检查相机，文件中缺少镜头相机')
        if len(cams)>1 :
            pattern = re.compile(shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3],re.IGNORECASE)
            cam_ok = True
            for cam in cams:
                if re.search(pattern,cam) and cam_ok:
                    mc.setAttr(cam + '.renderable',True)
                    cam_ok = False

                else:
                    mc.setAttr(cam + '.renderable',0)
            mc.warning(u'请检查相机，文件中有多余相机')
            #mc.error(u'请检查相机，文件中有多余相机')
        if serve==1:
            userName = os.environ['USERNAME']
            mc.file(rename=(tempath+shortName))
            mc.file(save=1,type ='mayaBinary',f = 1)
            fname=shortName.split(shotInfo[0]+'_')[1].split('_c0')[0]
            fileInfo='1|' + projectInfo + '|' + fname+'|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'修改可渲染相机文件'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print (u'===============!!!End【%s】!!!===============' % (u'%s_已完成文件' % shortName))
        return camname
#判断文件中是否有角色（道具）参考，场景参考，以判断之后分层方案
    def csl_refconditionref(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace=refInfos[2][0]
        if 'CAM' in refNamespace:
            refNamespace.remove('CAM')
        setRef=[]
        chpRef=[]
        for ns in refNamespace:
            if ns.split('_')[1][0].lower() in ['s']:
                setRef.append(ns)
            if ns.split('_')[1][0].lower() in ['c','p']:
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

#判断文件中是否有角色（道具）namespace，场景参考，以判断之后分层方案(参考导入也可适用）
    def csl_refcondition(self):
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

 # 设置文件
    def csl_FileSet(self,shotType=3):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]

        animInfo = self.csl_AnimFramInfoRead(shotType)
        startFrame = float(animInfo[0])
        endFrame = float(animInfo[1])
        if shotInfos[0]=='csl':
            fpsFrame = int(25)
            resW = int(1280)
            resH = int(720)
        if shotInfos[0]=='do5' :
            fpsFrame = int(24)
            resW = int(2048)
            resH = int(1106)
        # 分辨率
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
            # 起始帧
            mc.playbackOptions(min=startFrame)
            # 起始预留
            preStartFrame = startFrame - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 12
            mc.playbackOptions(animationEndTime=posEndFrame)
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)

        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        # 设置当前帧数
        mc.currentTime(startFrame)
        # 设置
        mel.eval('setMayaSoftwareFrameExt(3, 0)')
        # 设置渲染帧数
        mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        mc.setAttr('defaultRenderGlobals.endFrame',endFrame)
        # 输出文件命名

# 批量motionblur 分层
    def csl_MotionblurLayerAuto(self,shotType=3,server=1):
        FileName=mc.file(q=1,sn=1,shn=1)
        print u'==========================【%s】文件分层开始==========================' % FileName
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
        tempath='D:/Info_Temp/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        #需要导出的文件名称：
        #角色文件（包括道具）
        ChabaseName=Project+'_'+shotName+'_'+'cha_lr_c001.'+fileType
        #场景文件
        SetbaseName=Project+'_'+shotName+'_'+'set_lr_c001.'+fileType
        #角色场景互动文件
        CSbaseName=Project+'_'+shotName+'_'+'cs_lr_c001.'+fileType
        #角色灯光文件
        chrlightName=Project+'_'+shotName+'_'+'chrlight_lr_c001.'+fileType

        #01——载入场景
        self.csl_RenderEnvLoad()
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_载入场景参考' % FileName))
        #smooth设置
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_smooth设置' % FileName))
        #参考判断（文件是否有角色（包含道具），场景
        refconinfo=self.csl_refcondition()
        #02--导出角色文件
        if refconinfo[0]==1:
            self.csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
            mc.select(self.csl_GroupSelect()[0])
            if self.csl_GroupSelect()[2]:
                mc.select(self.csl_GroupSelect()[2],add=1)
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+ChabaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色文件' % ChabaseName))
        #03--导出场景文件
        if refconinfo[1]==1:
            self.csl_timeRecord()
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))
            mc.select(self.csl_GroupSelect()[1])
            if self.csl_GroupSelect()[3]:
                mc.select(self.csl_GroupSelect()[3],add=1)
            mc.file((tempath+SetbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
            self.csl_timeRecord()
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % SetbaseName))

            chaMoblurName=Project+'_'+shotName+'_'+'l1chrMotionBlur_lr_c001.'+fileType
            setMoblurName=Project+'_'+shotName+'_'+'l1setMotionBlur_lr_c001.'+fileType
            setmoblurLayerName='set_motionblur'
        #04--角色motionblur

     #角色 motion文件
        if refconinfo[0]==1:
            mc.file((tempath+ChabaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            mc.file(rename=(tempath+chaMoblurName))
            mc.file(save=1,type = fileTypeAll,f = 1)
        #渲染精度设置
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('mob')
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            moblurLayerName='chr_motionblur'
            meshchr=self.csl_meshInfo(meshtype='c')
            meshprp=self.csl_meshInfo(meshtype='p')
            meshs=meshchr+meshprp
            mc.select(meshs)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldMotionBlurShaderCreate()
            mc.createRenderLayer(meshs,name=moblurLayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            self.csl_FileSet(shotType)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('mob')
    #   可渲染相机设置

            self.csl_camRenderSet(shotType,serve=0)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建角色motionblur文件' % chaMoblurName))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1chrMotionBlur_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'角色mothionblur文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成角色文件' % chaMoblurName))

     #场景 motion文件
        if refconinfo[1]==1:
            print (u'===============!!!Start 【%s】!!!===============' % (u'%s_创建场景motionblur文件' % setMoblurName))
            mc.file((tempath+SetbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('mob')
            mc.file(rename=(tempath+setMoblurName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            GDC_ArnoldCommon.GDCRenderArnold().csl_RefIm()
            mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
            meshs=self.csl_meshInfo(meshtype='s')
            mc.select(meshs)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldMotionBlurShaderCreate()
            mc.createRenderLayer(meshs,name=setmoblurLayerName, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.ignoreMotionBlur',1)
            mc.setAttr('defaultArnoldRenderOptions.motion_blur_enable',1)
            mc.setAttr('defaultArnoldRenderOptions.range_type',0)
            self.csl_FileSet(shotType)
            GDC_ArnoldCommon.GDCRenderArnold().ArnoldRendererSettings('mob')
    #   可渲染相机设置
            self.csl_camRenderSet(shotType,serve=0)
            mc.file(force=1, options="v=0", type=fileTypeAll , save=1)
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_l1setMotionBlur_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'场景mothionblur文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成场景motionblur文件' % setMoblurName))

#删除不需要文件
        DeFile=[ChabaseName,SetbaseName,CSbaseName,chrlightName]
        if DeFile:
            for fil in DeFile:
                if fil in mc.getFileList(folder=tempath):
                    try:
                        mc.sysFile((tempath+fil),delete=True)
                    except:
                        pass
#成功代码
        print u'\n'
        print u'==========================【%s】motion文件分层结束==========================' % FileName
        print u'==========================文件路径【%s】=========================='  % tempath
        return 0
#Load非场景参考
    def csl_RefLoad(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        if mc.ls('CAMRN'):
            mc.file(loadReference='CAMRN')
            refRN.remove('CAMRN')
        refFile=refInfos[1][0]
        for i in range(len(refRN)):
            if refRN[i].split('_')[1][0].lower() not in ['s']:
                try:
                    mc.file(loadReference=refRN[i])
                except:
                    pass
        return 0
    #SG连接
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
    # 批量材质更新
    def csl_ResetMat(self,shortType=3,serve=0) :
        FileName=mc.file(q=1,sn=1,shn=1)
        print u'==========================【%s】材质重置开始==========================' % FileName
        self.csl_RendertimeRecord()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        userName = os.environ['USERNAME']
        Project=shotInfo [0]
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]
        tempath='D:/Info_Temp/RenderLayer/ResetMat/'+shotInfo[1]+'/'
        mc.sysFile(tempath, makeDir=True)
        # 恢复连接及相关属性
        meshchr=self.csl_meshInfo(meshtype='c')
        meshprp=self.csl_meshInfo(meshtype='p')
        objs=meshchr+meshprp
        if objs:
            mc.select(objs)
            self.csl_RestSG()
            self.csl_ShapeInfoApply(infoType='aiOpaque')
    #smooth设置
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
        #存本机
        mc.file(rename=(tempath+FileName))
        mc.file(save=1,type = 'mayaBinary',f = 1)
        if serve==1:
            fileInfo='1|' + projectInfo + '|'  + FileName.split('_c00')[0] +'|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'材质更新文件'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
        print (u'==========================【%s】材质重置结束==========================' % FileName )



    def csl_checkReferenceShaderReset(self,configType = 0 , assetType = 0):
        # 获取文件内参考信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        if refNodes:
            checkTypes = ['setAttr','connectAttr','disconnectAttr','addAttr','parent']
            for checkType in checkTypes:
                # 更改过的属性信息
                modifyInfos = []
                for refNode in refNodes:
                    if 'CAM' not in refNode :
                        #print refNode
                        if configType == 1:
                            modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                        if configType == 0:
                            if refNode.split('_')[1][0].lower() != 's':
                                modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                if modifyInfos:
                    # 需要欢迎的SG相关信息
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
                    # 开始欢迎
                    if resetShaderInfo:
                        for info in resetShaderInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)
                    if resetUVInfo:
                        for info in resetUVInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)

    def csl_HideList(self):
        objs=mc.ls(type='transform',l=1)
        HideInfo=['_sky_','csl_c017002ZhaoJingT_h:MSH_r_eyebrows_ca_','csl_c017002ZhaoJingT_h:MSH_l_eyebrows_ca_']
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
    # 【核心】 【场景文件整理】
    #------------------------------#
    # 根据参考整理文件 0 不删除多余物体，保留在OTC | 1 删除多余物体
    # finalLayout环节先清理约束再处理分组
    def sk_sceneReorganize(self, finalLayout=0):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRoot = []
        refNodes = []
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            # 全名处理
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
        # 鱼群集群
        if mc.ls('Cluster_GRP'):
            clusterFlowGrp = 'Cluster_GRP'
        else:
            clusterFlowGrp = mc.group(em=1, name='Cluster_GRP')
        # OTC_GRP
        if mc.ls('OTC_GRP'):
            otcGrp = 'OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        # 打组
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)
        if otcGrp not in mc.ls(clusterFlowGrp, l=1)[0]:
            mc.parent(clusterFlowGrp, otcGrp)
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # 开始处理
        # 优先记录：带有namespace的基本GRP
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
        # 1为参考方式处理
        # 这个方式对VFX会有影响,所以要修正
        for root in refRoot:
            # 首先判断是否在VFX_GRP和Cluster_GRP
            if '|VFX_GRP|' not in mc.ls(root, l=1)[0] and 'Cluster_GRP' not in mc.ls(root, l=1)[0]:
                print root
                refPath = mc.referenceQuery(root, filename=1)
                path = refPath.lower()
                # CAM
                if '/camera/' in path or '/episode_camera/' in path:
                    # 判断是否在CAM_GRP组里
                    if ('|' + camGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, camGrp)
                # CHR
                if '/characters/' in path:
                    # 判断是否在CHR_GRP组里
                    if ('|' + chrGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, chrGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, chrGrp)
                                mc.delete(upGrp)
                # PRP
                if '/props/' in path:
                    # 判断是否在PRP_GRP组里
                    if ('|' + prpGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, prpGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, prpGrp)
                                mc.delete(upGrp)
                # SET
                if '/sets/' in path or '/environments/' in path:
                    # 判断是否在SET_GRP组里
                    if ('|' + setGrp + '|') not in mc.ls(root , l=1)[0]:
                        mc.parent(root , setGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root,p=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                # 对于参考的子参考使用try
                                try:
                                    mc.parent(root, setGrp)
                                    mc.delete(upGrp)
                                except:
                                    pass
        # 整理外部约束之类的，用outLine方式修正
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
        # 清理不必要的namespace
        if ogNsGrp:
            import sk_pyCommon
            reload(sk_pyCommon)
            for ns in ogNsGrp:
                sk_pyCommon.sk_pyCommon().sk_deleteNamespace(ns)
# 数据库读取
#    def csl_DataGridViewRead(self):
#        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
#        shotName=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
#        dt = idmt.pipeline.db.GetRcByEpsc(shotName)
#        val=dt.values()
#        return val
#文件设置
#def csl

    def csl_timeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))

    #------------------------------#
    #------------------------------#
    # 写文件
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()

    #------------------------------#
    # 读文件
    def checkFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result

     #------------------------------#
    # 记录帧数信息
    def csl_AnimFramInfoWrite(self,shotType=3):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        refPath=sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
        if not os.path.exists(refPath):os.makedirs(refPath)
        FramFile=refPath + 'FramInfo.txt'
        starmfram=mc.playbackOptions(min=1,q = 1)
        endfram=mc.playbackOptions(max=1,q = 1)
        animFramInfo=[shotName,starmfram,endfram]
        self.checkFileWrite(FramFile,animFramInfo)
         #------------------------------#
        # 读取帧数信息
    def csl_AnimFramInfoRead(self,shotType=3):
        refPath=sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
        FramFile=refPath + 'FramInfo.txt'
        AnimInfo= self.checkFileRead(FramFile)
        startFrame=AnimInfo[1]
        endFrame=AnimInfo[2]
        return [startFrame,endFrame]

    def checkRefUnload2Load(self):
        refNodes = mc.ls(type = 'reference')
        if refNodes:
            for i in range(len(refNodes)):
                if refNodes[i] in ['_UNKNOWN_REF_NODE_']:
                    continue
                isLoaded = mc.referenceQuery(refNodes[i],isLoaded = 1)
                if isLoaded:
                    continue
                try:
                    refPath = mc.referenceQuery(refNodes[i],filename = 1)
                    mc.file(refPath, loadReference=refNodes[i])
                except:
                    pass


    #--------------------------------#
    # 读取excel信息
    def ydRLReadEXcle(self):
        # 处理excel信息？
        # 读文件名，获取项目及镜头号
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()  

        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])

        serverPath = '//file-cluster/GDC/Projects/' + projFullName + '/' + projFullName + '_Scratch/Render/ExcelInfo/'
        serverExcelPath = serverPath + str(shotInfo[1]) + '.xls'
        
        print '-----excelPath'
        print serverExcelPath
        
        import os
        if not os.path.exists(serverExcelPath):
            print(u'=======本集Excel文件不存在，请联系环节负责人处理=====')
            mc.error(u'=======本集Excel文件不存在，请联系环节负责人处理=====')

        import xlrd
        reload(xlrd)
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]  
        
        # 定位行数
        # 先找场名
        rowMax = shotAllData.nrows
        rowID = []
        for i in range(rowMax):
            # 集
            ep_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[0])
            # 场
            sc_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[1])
            # 镜
            sh_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[2])
            if ep_ID == shotInfo[1] and sc_ID == shotInfo[2] and sh_ID == shotInfo[3]:
                rowID.append(i)

        if not rowID:
            print u'=====本镜头信息不在指定表格内，请联系环节负责人处理====='
            mc.error(u'=====本镜头信息不在指定表格内，请联系环节负责人处理=====')

        # 读行数，具体的是镜头号加多少，视表格内容定
        shotData = shotAllData.row_values(rowID[0])
        shotDIct = {}

        shotDIct['ep'] = shotData[0]
        shotDIct['sc'] = shotData[1]
        shotDIct['sh'] = shotData[2]
        shotDIct['frames'] = shotData[3]
        if ';' in shotData[6]:
            tempInfos = shotData[6].split(';')
            if ';' in tempInfos[-1]:
                tempInfos.remove(tempInfos[-1])
            shotDIct['setID'] = tempInfos
        else:
            shotDIct['setID'] = [shotData[6]]
        shotDIct['outSide'] = shotData[7]
        shotDIct['time'] = shotData[8]
        
        return shotDIct

    # 处理表格信息
    def ydRLExcelInfoConfig(self,info):
        info = str(info)
        while info[-1] in [';',' ']:
            info = info[:-1]
        while '.' in info:
            info = info.split('.')[0]
        return info