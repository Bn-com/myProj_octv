# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】
#  Author : 韩虹
#  Data   : 2017_07
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

from idmt.maya.GA import GA_RedShiftRender
reload(GA_RedShiftRender)

from idmt.maya.GA import DDZ_FileFix
reload(DDZ_FileFix)

import json
import logging
import os
import re
import suds

import os
import re
class GA_RenderAutoCom(object):
    def __init__(self):
        # namespace清理
        pass
    #----------------------------------------------------------#
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
        #------------------------------#
    # 【渲染】【核心】【DDZ 自动渲染】
    #  Author  : 韩虹
    #  Data    : 2017_10
    #------------------------------#
    def GA_RenderAutoCom(self,shotType=2,server=1,fix=1,exr=0):
        # 【辅助】【修改file路径为   ${IDMT_PROJECTS}/】
        FileName=mc.file(q=1,sn=1,shn=1)
        # 文件优化
        self.checkRefUnload2Load()
        print u'==========================【%s】文件分层开始==========================' % FileName
        # 初始化灯光

        # 开始处理
        #基本
        self.GA_RendertimeRecord()
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
        tempath=''
        if os.path.exists('E:'):
            tempath='E:/Info_Temp/render/'
        else:
            tempath='D:/Info_Temp/render/'
        if shotType==2:
            tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        if shotType==3:
            tempath=tempath+shotInfo[0]+'/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        mc.sysFile(tempath, makeDir=True)
        #文件优化处理
        if fix==1:
            DDZ_FileFix.DDZ_FileFix().ddz_renderFileFIX(1,2,1)
        #smooth设置
        GA_RedShiftRender.GA_RedShiftRender().GA_RSmoothSet()
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_smooth设置' % FileName))
        #关闭其他时间段
        self.GA_DdzLightSet('set',0)
        #参考判断（文件是否有角色（包含道具），场景
        refconinfo=self.GA_refcondition()
        chrFile=''
        setFile=''
        setFile=''
        chalightFile=''
        if exr==1:
            #02--导出角色文件
            if refconinfo[0]==1:
                chrFile=self.GA_FileExr('chr',2)
                self.GA_timeRecord()
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出角色文件' % chrFile))
            #03--导出场景文件
            if refconinfo[1]==1:
                self.GA_timeRecord()
                setFile=self.GA_FileExr('set',2)
                self.GA_timeRecord()
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景文件' % setFile))
            #04--导出场景角色互动文件
            if refconinfo[0]==1 and refconinfo[1]==1:
                self.GA_timeRecord()
                GA_RedShiftRender.GA_RedShiftRender().GA_RefIm()
                print u'=====shadow属性已经设置 #Arnold 设置====='
                GA_RedShiftRender.GA_RedShiftRender().GA_RSShaderAssign(objs,'Lambert',0)
                setFile=self.GA_FileExr('id31',2)
                self.GA_timeRecord()
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % id31File))
            #04--导出chalight文件
            if refconinfo[0]==1:
                self.GA_timeRecord()
                GA_RedShiftRender.GA_RedShiftRender().GA_RefIm()
                print u'=====shadow属性已经设置 #Arnold 设置====='
                GA_RedShiftRender.GA_RedShiftRender().GA_RSShaderAssign(objs,'Lambert',0)
                chalightFile=self.GA_FileExr('chalight',2)
                self.GA_timeRecord()
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出场景角色互动文件' % chalightFile))
            #05--导出角色灯光文件
            if refconinfo[0]==1 and refconinfo[1]==1:
                lightingFile=self.GA_FileExr('chalighting',2)
            if refconinfo[0]==1:
                #角色文件
                mc.file(chrFile,options='v=0',type=fileTypeAll,f=1,o=1)
                chalightPath=lightingFile
                if refconinfo[1]==0:
                    chalightPath='//file-cluster/gdc/Projects/DouDiZhu/Project/data/AI2(Light)/cha_light.ma'
                mc.file((chalightPath),i=1,pr=1)
                GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co",'chr',0,1,1,1,2,1,1)
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成创建角色文件' % chrFile))
            #场景文件
            if refconinfo[1]==1:
                mc.file(setFile,options='v=0',type=fileTypeAll,f=1,o=1)
                GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","set",0,1,1,1,2,1,1)
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成创建场景文件' % setFile))
            #IDP31文件
            if refconinfo[0]==1 and refconinfo[1]==1:
                mc.file(id31File,options='v=0',type=fileTypeAll,f=1,o=1)
                GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("id31","",0,1,1,1,2,1,1)
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成创建ID31文件' % id31File))
            #chlight文件
            if refconinfo[0]==1 and refconinfo[1]==1:
                mc.file(chalightFile,options='v=0',type=fileTypeAll,f=1,o=1)
                GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("light","chr",0,1,1,1,2,1,1)
                print (u'===============!!!End 【%s】!!!===============' % (u'%s_已完成创建角色灯光文件' % chalightFile))
        else:
            if refconinfo[0]==1 and refconinfo[1]==0:
                if refconinfo[1]==0:
                    chalightPath='Z:/Projects/DouDiZhu/DDZ_Scratch/MODEL/AI2(Light)/cha_light.ma'
                mc.file((chalightPath),i=1,pr=1)
                self.GA_DdzLightSet('chr',0)
                chrFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","chr",0,1,1,1,2,1,1)
                chalightFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("light","chr",0,1,1,1,2,1,1)
                id31File=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("id31","",0,1,1,1,2,1,1)
            elif refconinfo[0]==1 and refconinfo[1]==1:
                self.GA_DdzLightSet('set',0)
                setFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","set",0,1,1,1,2,1,1)
                self.GA_DdzLightSet('chr',0)
                chrFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","chr",0,1,1,1,2,1,1)
                chalightFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("light","chr",0,1,1,1,2,1,1)
                id31File=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("id31","",0,1,1,1,2,1,1)
            elif refconinfo[0]==0 and refconinfo[1]==1:
                setFile=GA_RedShiftRender.GA_RedShiftRender().GA_RSRenderLayerCreat("co","set",0,1,1,1,2,1,1)
            else:
                mc.error(u'文件中没有角色，道具，及场景参考，请检查文件')
#删除不需要文件
        if server!=1:
            DeFile=[chrFile,setFile,id31File,chalightFile]
            if DeFile:
                for fil in DeFile:
                    if os.path.exists(fil):
                        try:
                            os.remove(fil)
                        except:
                            pass
#成功代码
        print u'\n'
        print u'==========================【%s】文件分层结束==========================' % FileName
        if server!=1:
            print u'==========================文件路径【%s】==========================' % tempath
        else:
            print u'==========================文件已上传相应数据库=========================='
        print u'\n'
        return 0
        #------------------------------#
    # 【自动渲染】【DDZ 自动渲染】【an文件需要优化，base文件不需要优化】
    #  Author  : 韩虹
    #  Data    : 2017_10
    #------------------------------#
    def GA_RenderAutoComFinal(self,shotType=2,server=1,exr=0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType==2 and shotInfo[3]=='an':
            self.GA_RenderAutoCom(shotType,server,1,exr)
        elif shotType==2 and shotInfo[3]=='base':
            self.GA_RenderAutoCom(shotType,server,0,exr)
        else:
            mc.error(u'文件命名不正确，请检查')
        return 0
# 【自动渲染】【通用】【辅助】
#  Author  : 韩虹
#选择需要导出的（'CHR_GRP','SET_GRP')
    def GA_GroupSelect(self):
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
# 【自动渲染】【通用】【辅助】
#  Author  : 韩虹
#灯光选择
    def GA_RSlightInfoList(self,Type='chr',lightType='group'):
        lights=mc.ls(lt=1,l=1)
        RSlighttypeList=['RedshiftPhysicalLight','RedshiftIESLight','RedshiftPortalLight','RedshiftDomeLight']
        RsLights=[]
        for rstype in RSlighttypeList:
            rslight=mc.ls(type=rstype,l=1)
            if rslight:
                for light in rslight:
                    if light not in RsLights:
                        RsLights.append(light)
        lights += RsLights
        lightInfoList=[]
        if lights:
            for light in lights:
                lightP=light.split('|')
                for lig in lightP:
                    if Type=='chr' and lightType=='group' and 'chr_light' in lig.lower() and lig not in lightInfoList:
                        lightInfoList.append(lig)
                    if Type=='set' and lightType=='group' and 'set_light' in lig.lower() and lig not in lightInfoList:
                        lightInfoList.append(lig)
                if Type=='chr' and lightType=='key' and 'chr_light' in light.lower() and 'keylight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chr' and lightType=='fill' and 'chr_light' in light.lower() and  'fillight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='chr' and lightType=='rim' and 'chr_light' in light.lower() and  'rimlight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='key' and 'set_light' in light.lower() and 'keylight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='fill' and 'set_light' in light.lower() and  'fillight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
                if Type=='set' and lightType=='rim' and 'set_light' in light.lower() and  'rimlight' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                if Type=='set' and lightType=='all' and 'set_light' in light.lower() and ligt[0] not in lightInfoList:
                    ligt=mc.listRelatives(light,p=1,f=1)
                    lightInfoList.append(ligt[0])
        return  lightInfoList

#时间记录
    def GA_RendertimeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))


# 【自动渲染】【通用】【辅助】
#  Author  : 韩虹
#判断文件中是否有角色（道具）namespace，场景参考，以判断之后分层方案(参考导入也可适用）
    def GA_refcondition(self):
        namespaces=mc.namespaceInfo(listOnlyNamespaces=1)
        setRef=[]
        chpRef=[]
        for ns in namespaces:
            if '_' in ns and ns.split('_')[1][0].lower() in ['s']:
                setRef.append(ns)
            elif '_' in ns and ns.split('_')[1][0].lower() in ['c','p'] and 'p028001cloud' not in ns and 'p000007sky' not in ns:
                chpRef.append(ns)
            elif '_' in ns and ns.split('_')[1][0].lower() in ['p'] and 'p028001cloud' in ns or 'p000007sky' in ns:
                setRef.append(ns)
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

    #SG连接
    def GA_RestSG(self):
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
    def GA_ResetMat(self,shortType=3,serve=0) :
        FileName=mc.file(q=1,sn=1,shn=1)
        print u'==========================【%s】材质重置开始==========================' % FileName
        self.GA_RendertimeRecord()
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
        meshchr=self.GA_meshInfo(meshtype='c')
        meshprp=self.GA_meshInfo(meshtype='p')
        objs=meshchr+meshprp
        if objs:
            mc.select(objs)
            self.GA_RestSG()
            self.GA_ShapeInfoApply(infoType='aiOpaque')
    #smooth设置
        GDC_ArnoldCommon.GDCRenderArnold().GA_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().GA_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold',tangents=0)
        GDC_ArnoldCommon.GDCRenderArnold().GA_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold',tangents=0)
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



    def GA_checkReferenceShaderReset(self,configType = 0 , assetType = 0):
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

    def GA_HideList(self):
        objs=mc.ls(type='transform',l=1)
        HideInfo=['_sky_','GA_c017002ZhaoJingT_h:MSH_r_eyebrows_ca_','GA_c017002ZhaoJingT_h:MSH_l_eyebrows_ca_']
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
#    def GA_DataGridViewRead(self):
#        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
#        shotName=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
#        dt = idmt.pipeline.db.GetRcByEpsc(shotName)
#        val=dt.values()
#        return val
#文件设置
#def csl

    def GA_timeRecord(self):
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
    def GA_AnimFramInfoWrite(self,shotType=3):
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

    def checkRefUnload2Load(self):
        refNodes = mc.ls(type = 'reference')
        if refNodes:
            for i in range(len(refNodes)):
                if refNodes[i] in ['_UNKNOWN_REF_NODE_','sharedReferenceNode']:
                    continue
                isLoaded = mc.referenceQuery(refNodes[i],isLoaded = 1)
                if isLoaded:
                    continue
                try:
                    refPath = mc.referenceQuery(refNodes[i],filename = 1)
                    mc.file(refPath, loadReference=refNodes[i])
                except:
                    pass
    def GA_FileExr(self,ftype='chr',shotType=2):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        setList=mc.ls(set=1)
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        filName=shotName+'_'+ftype+'_lr_c001.mb'
        GROPS=self.GA_GroupSelect()
        chrlightGrp=self.GA_RSlightInfoList('chr','group')
        chrGrp=GROPS[0][0]
        prpGrops=GROPS[2][0]
        setGrops=GROPS[1][0]
        camGrops=GROPS[3][0]
        objs=[]
        if ftype=='chr':
            objs=[chrGrp]+[prpGrops]+[camGrops]
        elif ftype=='chrlight':
            objs=[chrGrp]+[prpGrops]+[camGrops]+[chrlightGrp]
        elif ftype in ['set','id31','shadow']:
            objs=[chrGrp]+[prpGrops]+[setGrops]+[camGrops]
        elif ftype in ['chalighting']:
            objs=chrlightGrp
            if not objs:
                mc.error(u'场景文件中缺少chr_light灯光组，请检查')
        else:
            objs=[chrGrp]+[prpGrops]+[setGrops]+[camGrops]
        tempath=''
        if os.path.exists('E:'):
            tempath='E:/Info_Temp/render/'
        else:
            tempath='D:/Info_Temp/render/'
        mc.sysFile(tempath, makeDir=True)
        mc.select(objs)
        mc.file((tempath+ filName),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)
        return  (tempath+ filName)
# 识别时间段，并处理其他时间段灯光组（关闭，开启）
    #------------------------------#
    # 【辅】 【时间段判断】
    #------------------------------#
    # 韩虹
    # Type:set,chr
    # key，其他时间段关闭还是
    def GA_DdzLightSet(self,Type='set',key=0):
        import idmt.pipeline.service
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        time=idmt.pipeline.service.Service().DDZGetTOD(shotInfo[1],shotInfo[2])
        allLightGrps=mc.ls(('*:'+Type+'_light'),tr=1,l=1)+mc.ls(('*'+Type+'_light'),tr=1,l=1)
        timeGrps=[]
        NtimeGrps=[]
        for checkGrp in allLightGrps:
            lightGrp=Type+'_'+time+'_light'
            grpA=lightGrp
            if '|' in checkGrp and ':' in checkGrp:
                grpS=checkGrp.split('|')[-1]
                grpA=grpS.split(':')[0]+':'+ lightGrp
            elif '|' not in checkGrp and ':' in checkGrp:
                grpA=checkGrp.split(':')[0]+':'+ lightGrp
            childGrps = mc.listRelatives(checkGrp,c=1,type = 'transform',f=1)
            if time!='day' and mc.objExists(grpA):
                for grp in childGrps:
                    shape=mc.listRelatives(grp,s=1)
                    if not shape and grp.split('|')[-1]==grpA and grp not in timeGrps:
                        timeGrps.append(grp)
                    if not shape and grp.split('|')[-1]!=grpA and grp not in NtimeGrps:
                        NtimeGrps.append(grp)
            if time=='day' and mc.objExists(grpA):
                for grp in childGrps:
                    shape=mc.listRelatives(grp,s=1)
                    if not shape and grp.split('|')[-1]==grpA and grp not in timeGrps:
                        timeGrps.append(grp)
                    if not shape and grp.split('|')[-1]!=grpA and grp not in NtimeGrps:
                        NtimeGrps.append(grp)
            if time=='day' and not mc.objExists(grpA) and mc.listRelatives(childGrps[0],s=1):
                timeGrps.append(checkGrp)
        if  timeGrps:
            for tgrp in timeGrps :
                mc.setAttr((tgrp+'.v'),1)
        if  NtimeGrps:
            for ntgrp in NtimeGrps :
                mc.setAttr((ntgrp+'.v'),key)
        return [timeGrps,NtimeGrps]


    #------------------------------#
    #自动分层批处理（仅用于TD）
    #韩虹
    #2017\10
    def GA_RednerAuto(self,ep='004',sc='028'):
        path='L:/Projects/DouDiZhu/Project/scenes/Animation/'+'episode_'+ep+'/'+'scene_'+sc+'/'+'anim/'
        fil=mc.getFileList(folder=path,filespec='*.mb')
        if fil and len(fil)==1:
            mc.file((path+fil[0]),options='v=0',type='mayaBinary',f=1,o=1)
            self.GA_RenderAutoComFinal(2,1,0)
        else:
            mc.warning(u'【%s】动画文件有问题，请检查' %path)
            mc.error(u'【%s】动画文件有问题，请检查' %path)
        result=path+fil[0]+u' 已处理'
        return result
    #可分层镜头信息
    def GA_ShotInfo(self,projectName = "DouDiZhu",state_rc = u"可制作"):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, u"SELECT [anim_ep], [anim_sc] FROM [View_SsomAnimTaskmodeState] WHERE [state_rc] = '%s'" % state_rc, None)
        dt = json.loads(reply)
        return dt
    #批量自动分层
    def GA_AutoReBatch(self):
        shotInfoList=self.GA_ShotInfo("DouDiZhu",u"可制作")
        if shotInfoList:
            for i in range(len(shotInfoList)):
                shotIn=shotInfoList[i].values()
                if not shotIn:
                    continue
                ep=shotIn[1]
                sc=shotIn[0]
                if ep in ['004','005','006']:
                    self.GA_RednerAuto(ep,sc)
        else:
            mc.error(u'无可制作镜头')
#读表
    def GA_Exl(self,serverExcelPath):
        import xlrd
        reload(xlrd)
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]
        rowMax = shotAllData.nrows
        EPlists=[]
        shLists=[]
        for i in range(1,rowMax):
            # 集
            ep_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[0])
            # 镜
            sh_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[1])
            RR=shotAllData.row_values(i)[6]
            if RR and self.ydRLExcelInfoConfig(RR)=='1':
                EPlists.append(ep_ID)
                shLists.append(sh_ID)
        return [EPlists,shLists]
    def GA_AutoRenderExl(self):
        serverExcelPath ='F:/final/Rendering01.xls'
        ExlInfo=self.GA_Exl(serverExcelPath)
        if not ExlInfo[0]:
            mc.error(u'表中没有需要重渲的镜头')
        EPlists=ExlInfo[0]
        SHlists=ExlInfo[1]
        for i in range(len(EPlists)):
            self.GA_RednerAuto(EPlists[i],SHlists[i])

    # 处理表格信息
    #shenkang
    def ydRLExcelInfoConfig(self,info):
        info = str(info)
        while info[-1] in [';',' ']:
            info = info[:-1]
        while '.' in info:
            info = info.split('.')[0]
        return info
    #动画读表清理
    #韩虹
    #2017\11
    def GA_ExlAnim(self,serverExcelPath):
        import xlrd
        reload(xlrd)
        shotAllData = xlrd.open_workbook(serverExcelPath).sheets()[0]
        rowMax = shotAllData.nrows
        EPlists=[]
        shLists=[]
        for i in range(1,rowMax):
            # 集
            ep_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[0])
            # 镜
            sh_ID = self.ydRLExcelInfoConfig(shotAllData.row_values(i)[1])
            RR=shotAllData.row_values(i)[2]
            if RR and self.ydRLExcelInfoConfig(RR)=='wait':
                EPlists.append(ep_ID)
                shLists.append(sh_ID)
        return [EPlists,shLists]
    #动画自动清理
    def GA_AnimAuto(self,ep='004',sc='028'):
        path='//file-cluster/gdc/Projects/DouDiZhu/Project/scenes/Animation/'+'episode_'+ep+'/'+'scene_'+sc+'/'+'anim/'
        fil=mc.getFileList(folder=path,filespec='*.mb')
        if fil and len(fil)==1:
            mc.file((path+fil[0]),options='v=0',type='mayaBinary',f=1,o=1)
            mel.eval('source zwCalimeroCheckin.mel')
            mel.eval('zwCalimeroCheckin')
        else:
            mc.warning(u'【%s】动画文件有问题，请检查' %path)
            mc.error(u'【%s】动画文件有问题，请检查' %path)
        result=path+fil[0]+u' 已处理'
        return result
    #动画读表清理
    #韩虹
    #2017\11
    def GA_AutoAnimcheck(self):
        serverExcelPath ='F:/final/Rendering01.xls'
        ExlInfo=self.GA_ExlAnim(serverExcelPath)
        if not ExlInfo[0]:
            mc.error(u'表中没有需要动画清理的镜头')
        EPlists=ExlInfo[0]
        SHlists=ExlInfo[1]
        for i in range(len(EPlists)):
            self.GA_AnimAuto(EPlists[i],SHlists[i])
        return 0
