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
from idmt.maya.py_common import GDC_RenderVrayLayer
reload(GDC_RenderVrayLayer)
import shutil
import os
import re

import sys
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)
sys.setdefaultencoding('utf8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
#【nj2017】自动分层工具
class nj17_RenderAutoCommons(object):
    def __init__(self):
        # namespace清理
        pass
#crs为1，角色和场景一起渲染，crs为0，角色和场景分别渲染
    def nj17_RenderLayerAuto(self,crs=0,shotType=3,server=1,framrender=1):
        FileName=mc.file(q=1,sn=1,shn=1)        
        print u'==========================【%s】文件分层开始==========================' % FileName        
        shotInfo = self.checkShotInfo()[0]
        shotName=self.checkShotInfo()[1]
        serverPath = '//file-cluster/GDC/Projects/Ninjago/Project/'
        refInfos = self.checkReferenceListInfo()
        projectInfo = 'Ninjago'
        userName = os.environ['USERNAME']       
        Project=shotInfo [0]
        fileType=shotInfo[len(shotInfo)-1].split('.')[1]
        lightcheck=self.lightGrpInfo()
        check=lightcheck[0]
        lightGrp=lightcheck[1]
        grp=lightcheck[2]
       #场景灯光检测
        if check==0:
            mc.error(u'==================场景缺少【%s】灯光组，请检查==========='%grp)
        #shotName=''
        LineName=''
        serPath=''
        if fileType=='mb':
            fileTypeAll='mayaBinary'
        if fileType=='ma':
            fileTypeAll='mayaAscii'
        if shotType == 3:
            LineName=shotInfo[4]+'_'+shotInfo[5]
            serPath=serverPath+'scenes/Animation/episode_'+shotInfo[1]+'/sequence_'+shotInfo[2]+'/scene_'+shotInfo[3]+'/lighting/'
        if shotType == 2: 
            #shotName=shotInfo[1]+'_'+shotInfo[2]
            LineName=shotInfo[3]+'_'+shotInfo[4]
            serPath=serverPath+'scenes/Animation/episode_'+shotInfo[1]+'/scene_'+shotInfo[2]+'/lighting/'   
        tempath='D:/Info_Temp/'+Project+'/RenderLayer/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        mc.sysFile(tempath, makeDir=True)

        #需要导出的文件名称：
#        fileType=['CHR','SET','CRS','IDZ','MOB']
        #base_lr
        baseName=Project+'_'+shotName+'_'+'base_lr_c001.'+fileType
        #color文件（包括道具）
        ColorbaseName=Project+'_'+shotName+'_'+'color_lr_c001.'+fileType
        #非灯光文件
        CSbaseName=Project+'_'+shotName+'_'+'CS_lr_c001.'+fileType
        #sky文件
        SKYName=Project+'_'+shotName+'_'+'SKY_lr_c001.'+fileType

        #01——载入场景
        #self.nj17_RenderEnvLoad()
        #print (u'===============!!!Start 【%s】!!!===============' % (u'%s_载入场景参考' % FileName))        
        #优化文件
        if shotInfo[-2]=='lr' and shotInfo[-3]=='base':
            pass
        else:
            print u'================文件优化【star】================'
            from idmt.maya.py_common import nj17_CheckTools
            reload(nj17_CheckTools)
            nj17_CheckTools.nj17_CheckTools().nj_FixBeforeRender()
            self.sk_sceneReorganize(0)
            mc.setAttr("vraySettings.cam_overrideEnvtex",0)
            mc.file(rename=(tempath+baseName))
            mc.file(save=1,type = fileTypeAll,f = 1)
            print (tempath+baseName)
            print u'================文件优化【end】================'
        #   文件打组
        if server==1:
            fileInfo='1|' + projectInfo + '|' + shotName + '_base_lr|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'优化后基础文件（不参与渲染）'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'%s_已上传优化后文件' % baseName))
        mc.file((tempath+baseName),options='v=0',type=fileTypeAll,f=1,o=1)

        #隐藏
        #self.nj17_HideList()
        #参考判断（文件是否有角色（包含道具），场景  
        refconinfo=self.nj_refcondition()
        #文件中物体：
        objs = self.NJ17RLObjectsTList()
        refCHR = objs[0]
        refPROP = objs[1]
        refSET = objs[2]
        #需要导出文件物体：
        Grps=self.nj_GroupSelect()
        grpCHR=Grps[0]
        grpPROP=Grps[1]
        grpSET=Grps[2]
        grpCAM=Grps[3]
        #02--导出color文件
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出灯光文件' % ColorbaseName))
        mc.select(grpCHR+grpPROP+grpSET+grpCAM)
        mc.file((tempath+ColorbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)

        print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出灯光文件' % ColorbaseName))
        
        #导入参考，删除材质
        self.nj_RefIm()
        #mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        mel.eval('zwResetShadingEnginesN')
        skys=self.OBJAttrInfo('SKY')
        checksky=skys[0]
        objsky=skys[1]
        if checksky==1:
            mc.select(objsky+grpCAM)
            mc.file((tempath+SKYName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
        #导出天空物体
        #04--导出非灯光文件
        print (u'===============!!!Start 【%s】!!!===============' % (u'%s_导出非灯光文件' % CSbaseName))
        mc.select(grpCHR+grpPROP+grpSET+grpCAM)
        mc.file((tempath+CSbaseName),options='v=0',f=1,type=fileTypeAll,preserveReferences=1,es=1)
        print (u'===============!!!End 【%s】!!!===============' % (u'%s_导出非灯光文件' % CSbaseName))
        if crs==0 and refconinfo[0]==1:
            print u'\n'
            print (u'===============!!!Start 【%s】!!!===============' % (u'角色文件设置'))
            mc.file((tempath+ColorbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            print (u'===============!!!Start 【%s】!!!===============' % (u'创建角色文件'))
            #相机设置
            self.camSet()
            #灯光信息
            lightcheck=self.lightGrpInfo()
            check=lightcheck[0]
            lightGrp=lightcheck[1]
            objs=refCHR+refPROP+refSET+[lightGrp]
            mc.select(objs)
            GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('CHR')
            mc.setAttr("vraySettings.cam_overrideEnvtex",0)
            print 'test'
            #试渲一帧
            if framrender==1:
                mc.setAttr("vraySettings.samplerType",3)
                mc.setAttr("vraySettings.progressiveMaxTime",5)
                mc.editRenderLayerGlobals(currentRenderLayer='CHR')
                testChr=self.nj_RenderFileTestSave('CHR')
                self.gdc_batchRender(testChr)
            #mc.file(rename=(tempath+'test/'+baseName))
            #mc.file(save=1,type = fileTypeAll,f = 1)
            #又回到原设置，并存盘
                mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
                GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VraySettings('co')
            self.nj_RenderFileSave('CHR')

            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_CHR_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'角色灯光文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'_已上传角色文件'))
            print (u'===============!!!End 【%s】!!!===============' % (u'已完成角色角色'))

            print (u'===============!!!Start 【%s】!!!===============' % (u'创建场景灯光文件'))
        if crs==0 and refconinfo[1]==1:
            mc.file((tempath+ColorbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            self.camSet()
            mc.select(objs)
            GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('SET')
            mc.setAttr("vraySettings.cam_overrideEnvtex",0)
            #试渲一帧
            if framrender==1:
                mc.setAttr("vraySettings.samplerType",3)
                mc.setAttr("vraySettings.progressiveMaxTime",5)
                mc.editRenderLayerGlobals(currentRenderLayer='SET')
                testSet=self.nj_RenderFileTestSave('SET')
                self.gdc_batchRender(testSet)
            #又回到原设置，并存盘
                mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
                GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VraySettings('co')
            self.nj_RenderFileSave('SET')
            #文件上传
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_SET_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd) 
                description = u'场景灯光文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')  
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'已上传场景灯光文件'))
            print (u'===============!!!End 【%s】!!!===============' % (u'已完成场景灯光文件'))
# 场景角色一起渲染：
        if crs==1:
            mc.file((tempath+ColorbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
            self.camSet()
            lightcheck=self.lightGrpInfo()
            check=lightcheck[0]
            ightGrp=lightcheck[1]
            objs=refCHR+refPROP+refSET+[lightGrp]
            mc.select(objs)
            GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('CRS')
            mc.setAttr("vraySettings.cam_overrideEnvtex",0)
            #试渲一帧
            if framrender==1:
                mc.setAttr("vraySettings.samplerType",3)
                mc.setAttr("vraySettings.progressiveMaxTime",5)
                mc.editRenderLayerGlobals(currentRenderLayer='CRS')
                testCRS=self.nj_RenderFileTestSave('CRS')
                self.gdc_batchRender(testCRS)
            #又回到原设置，并存盘
                mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
                GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VraySettings('co')
            self.nj_RenderFileSave('CRS')
            #文件上传
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_CRS_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'场景角色灯光文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'已上传角色场景灯光文件'))
            print (u'===============!!!End 【%s】!!!===============' % (u'已完成角色场景灯光文件'))
#非灯光层
        #idz文件
        mc.file((tempath+CSbaseName),options='v=0',type=fileTypeAll,f=1,o=1)
        print (u'===============!!!Start 【%s】!!!===============' % (u'创建IDZ文件' ))
        self.camSet()
        objs=refCHR+refPROP+refSET
        mc.select(objs)
        GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('IDZ')
        mc.setAttr("vraySettings.cam_overrideEnvtex",0)
        #试渲一帧
        if framrender==1:
            mc.editRenderLayerGlobals(currentRenderLayer='IDZ')
            testIDZ=self.nj_RenderFileTestSave('IDZ')
            self.gdc_batchRender(testIDZ)
        #又回到原设置，并存盘
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
            GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VraySettings('id')
        self.nj_RenderFileSave('IDZ')
        #文件上传
        if  server==1  :
            fileInfo='1|' + projectInfo + '|' + shotName + '_IDZ_lr|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'IDZ文件'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'已上传IDZ文件'))
        print (u'===============!!!End 【%s】!!!===============' % (u'已完成IDZ文件'))
        print (u'===============!!!Start 【%s】!!!===============' % (u'创建motionblur文件'))
        self.camSet()
        mc.select(objs)
        GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('MBL')
        mc.setAttr("vraySettings.cam_overrideEnvtex",0)
        #试渲一帧
        if framrender==1:
            mc.editRenderLayerGlobals(currentRenderLayer='MBL')
            testMBL=self.nj_RenderFileTestSave('MBL')
            self.gdc_batchRender(testMBL)
        #又回到原设置，并存盘
            mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        self.nj_RenderFileSave('MBL')
        #文件上传
        if  server==1  :
            fileInfo='1|' + projectInfo + '|' + shotName + '_MBL_lr|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            mel.eval(checkOutCmd)
            description = u'motionblur文件'
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
            print u'\n'
            print (u'===============!!!End 【%s】!!!===============' % (u'已上传MBL文件'))
        print (u'===============!!!End 【%s】!!!===============' % (u'已完成MBL文件'))

        if checksky==1:
            print (u'===============!!!Start 【%s】!!!===============' % (u'创建SKY文件'))
            mc.file((tempath+SKYName),options='v=0',type=fileTypeAll,f=1,o=1)
            self.camSet()
            skys=self.OBJAttrInfo('SKY')
            #天空球设置
            self.nj_SKYSET()
            objsky=skys[1]
            mc.select(objsky)
            GDC_RenderVrayLayer.GDC_RenderVrayLayer().nj_VrayRenderCreatAuto('SKY')
            #试渲一帧
            if framrender==1:
                mc.editRenderLayerGlobals(currentRenderLayer='SKY')
                testSKY=self.nj_RenderFileTestSave('SKY')
                self.gdc_batchRender(testSKY)
            #又回到原设置，并存盘
                mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
            self.nj_RenderFileSave('SKY')
            #文件上传
            print (u'===============!!!End 【%s】!!!===============' % (u'创建SKY文件'))
            if  server==1  :
                fileInfo='1|' + projectInfo + '|' + shotName + '_SKY_lr|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                mel.eval(checkOutCmd)
                description = u'SKY文件'
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
                print u'\n'
                print (u'===============!!!End 【%s】!!!===============' % (u'已上传天空文件'))
        print u'\n'
        print u'==========================【%s】文件分层结束==========================' % FileName
        print u'\n'
        return 0
#项目
    def checkShotInfo(self,shotType=3):
        filename=mc.file(q=1,shn=1,sn=1)
        shotInfo=[]
        shot=[]
        if '_' in filename and filename.split('_')[0]=='nj' and len(filename.split('_'))>4:
            shotInfo=filename.split('_')
        else:
            mc.error(u'================================文件命名不正确，请检查================================')
        if shotInfo:
            shot=shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        return [shotInfo,shot]
#参考
    def checkReferenceListInfo(self):
        #import pymel.core.system
        # 获取第一级references信息
        # 返回数据是一个FileReference的class
        #referencesClassLV_0 = pymel.core.system.listReferences()
        referencesLV_0 = mc.file(q = 1,reference =1)
        # reference参考节点名
        refNodes = []
        # reference参考路径
        # 起始路径可以从rfNode查询到
        refPaths = []
        # 起始路径可以从rfNode查询到
        refNamespace = []
        # 处理第一级数据
        #for refInfo in referencesClassLV_0:
        for refInfo in referencesLV_0:
            # 注意将class返回内容处理成str
            refNodeName = mc.referenceQuery(refInfo,referenceNode=1)
            refNodes.append(refNodeName)
            #refNodes.append(str(refInfo._refNode))
            refPaths.append(self.checkReferencePathConfig(refInfo))
            #refPaths.append(self.checkReferencePathConfig(str(refInfo.path)))
            refPath = mc.referenceQuery(refInfo , filename = 1)
            refNamespace.append(self.checkReferenceGetNamespaceInfoByPath(refPath))
            #refNamespace.append(self.checkReferenceGetNamespaceInfo(refNodeName))
            #refNamespace.append(self.checkReferenceGetNamespaceInfo(str(refInfo._refNode)))
        # 准备存储，根据子参考级别不同有不同的元素
        referencesNodeInfo = []
        referencesNodeInfo.append(refNodes)
        referencePathInfo = []
        referencePathInfo.append(refPaths)
        referencesNameSpaceInfo = []
        referencesNameSpaceInfo.append(refNamespace)
        # 开始处理下级reference
        for refNode in refNodes:
            referenceNodeDown = mc.referenceQuery(refNode, child=1, rfn=1)
            if referenceNodeDown:
                while referenceNodeDown:
                    # 开始循环判断
                    refNodeDowns = referenceNodeDown[:]
                    # 下级reference节点名
                    refNodesDown = []
                    refPathsDown = []
                    refNamespaceDown = []
                    # 记录本层refNode
                    referencesNodeInfo.append(referenceNodeDown)
                    referenceNodeDown = []
                    for refNodeD in refNodeDowns:
                        # reference节点
                        refNodesDown.append(refNodeD)
                        # 处理好是否有子节点再处理路径
                        # 这里直接是list
                        referenceNodeDownTemp = mc.referenceQuery(refNodeD, child=1, rfn=1)
                        if referenceNodeDownTemp:
                            for node in referenceNodeDownTemp:
                                referenceNodeDown.append(node)
                        # 记录路径
                        refPathsDown.append(self.checkReferencePathConfig(mc.referenceQuery(refNodeD, f=1)))
                        # 记录namespace
                        refNamespaceDown.append(self.checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNodeD, f=1)))
                        #refNamespaceDown.append(self.checkReferenceGetNamespaceInfo(refNodeD))
                    # 记录本层路径
                    referencePathInfo.append(refPathsDown)
                    # 记录本层namespace,强制记录完整namespace
                    referencesNameSpaceInfo.append(refNamespaceDown)

        # result分3个数据，0为node名字，1为path信息，2为namespace
        # 多少个元素意味着多少层父子节点
        result = []
        result.append(referencesNodeInfo)
        result.append(referencePathInfo)
        result.append(referencesNameSpaceInfo)
        return result
    # 处理reference路径，清楚后面可能存在的{}
    def checkReferencePathConfig(self, path):
        if '{' in path:
            path = path.split('{')[0]
        return path
    # 通过refPath 获取refNode的namespace
    def checkReferenceGetNamespaceInfoByPath(self,refPth):
        namespace = mc.file( refPth ,namespace = 1 ,q = 1 )
        # 判断是不是子参考
        parentRef = mc.referenceQuery( refPth , referenceNode=True, parent = True )
        if parentRef:
            namespace = parentRef[:-2] + ':' + namespace
        return namespace
    # ------------------------------#
    #【场景文件整理】
    # Author:shengkang
    #  ------------------------------#
    # 根据参考整理文件 0 不删除多余物体，保留在OTC | 1 删除多余物体
    # finalLayout环节先清理约束再处理分组
    def sk_sceneReorganize(self, finalLayout=0):
        refInfos = self.checkReferenceListInfo()
        refRoot = []
        refNodes = []
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            # 全名处理
            refObjs = mc.referenceQuery(refNode, nodes=1, dagPath=1)
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
        # 根组处理
        for checkKey in ['CHR_GRP','PRP_GRP','SET_GRP','OTC_GRP']:
            checkGrp = mc.ls(checkKey,l=1)[0]
            if len(checkGrp.split('|')) == 2:
                continue
            mc.parent(checkGrp,world = 1)
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # 开始处理
        # 优先记录：带有namespace的基本GRP
        ogGrp = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        ogNsGrp = []
        for grp in ogGrp:
            checkGrps = mc.ls(('*:*' + grp + '*'), l=1) + mc.ls(('*:*:*' + grp + '*'), l=1)
            if checkGrps:
                for obj in checkGrps:
                    lastName = obj.split(':')[-1]
                    ogNsGrp.append(obj[0:-1 * (len(lastName) + 1)])
        ogNsGrp = list(set(ogNsGrp))
        print refRoot
        # 1为参考方式处理
        # 这个方式对VFX会有影响,所以要修正
        for root in refRoot:
            # 首先判断是否在VFX_GRP和Cluster_GRP
            if mc.ls(root, l=1) and '|VFX_GRP|' not in mc.ls(root, l=1)[0] and 'Cluster_GRP' not in mc.ls(root, l=1)[0]:
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
                        upGrp = mc.listRelatives(root, p=1, f=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, chrGrp)
                                mc.delete(upGrp)
                # PRP
                if '/props/' in path or '/misc/' in path:
                    # 判断是否在PRP_GRP组里
                    if ('|' + prpGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, prpGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root, p=1, f=1)
                        if upGrp:
                            upGrp = upGrp[0]
                            if 'rngroup' in upGrp.lower():
                                mc.parent(root, prpGrp)
                                mc.delete(upGrp)
                # SET
                if '/sets/' in path or '/environments/' in path:
                    # 判断是否在SET_GRP组里
                    if ('|' + setGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, setGrp)
                    else:
                        # 处理上级物体有RNgroup的组的情况
                        upGrp = mc.listRelatives(root, p=1, f=1)
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
                        mc.parent(root, 'OTC_GRP')
        # 清理不必要的namespace
        if ogNsGrp:
            import sk_pyCommon

            reload(sk_pyCommon)
            for ns in ogNsGrp:
                self.sk_deleteNamespace(ns)
    #------------------------------#
    # 【通用：删除指定非参考namespace的工具】
    # Author  : 沈  康
    # Data    : 2013_09_23
    #------------------------------#
    def sk_deleteNamespace(self,namespace):
        ns = namespace
        try:
            # 使得namespace成为空的namespace
            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
            # 清理空namespace
            mc.namespace(removeNamespace= (':' + ns))
        except:
            pass
#物体表
    def NJ17RLObjectsTList(self):
        # 获取root
        refCHR = []
        refPROP = []
        refSET = []
        needSKY = []
        needPROP = []
        needrefSEA = []
        needInfo=[]
        light=[]
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
                        if  objs and 'MODEL|' in mesh and 'DEFORMERS' not in mesh :
                          needInfo.append(objs[0])
            if i == 0:
                CHRR = needInfo
            if i == 1:
                PROPR = needInfo
            if i == 2:
                SETR = needInfo
        result = [CHRR,PROPR,SETR]
        return result
    #------------------------------#
    # 【通用：判断文件中是否有角色或场景】
    # Author  : 韩虹
    # Data    : 2016_06_13
    #------------------------------#
    def nj_refcondition(self):
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
#导入参考
    def nj_RefIm(self):
        while mc.file(q=1,r=1):
          refPath=mc.file(q=1,r=1)
          if len(refPath)!=0:
              for r in refPath:
                  refRN=mc.file(r,q=1,rfn=1)
                  if(mc.file(r,q=1,dr=1)):
                      mc.file(refRN,loadReference=1)
                  mc.file(r,ir=1)
        return 0
    #------------------------------#
    # 【通用：场景中基本GRP】
    # Author  : 韩虹
    # Data    :
    #------------------------------#
    def nj_GroupSelect(self):
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
    #设置
    def camSet(self):
        shotName=self.checkShotInfo()[1]
        camName='cam_'+shotName
        cas=mc.ls(ca=1,l=1)
        for cam in cas:
            mc.setAttr((cam+'.depthOfField'),0)
            if camName not in cam:
                mc.setAttr((cam+'.renderable'),0)
            else:
                mc.setAttr((cam+'.renderable'),1)
        return 0

    #------------------------------#
    # 【NJ2017：场景中基本灯光组读取
    # Author  : 韩虹
    # Data    :
    #------------------------------#
    def lightGrpInfo(self):
        shotInfo = self.checkShotInfo()[0]
        project='Ninjago'
        EP=shotInfo[1]
        SQ=shotInfo[2]
        SC=shotInfo[3]
        check=0
        TOD=self.GDC_TODMsSQL(project,EP,SQ,SC)
        lights=[]
        grp=''
        lightGrp=['MLA_lights','MLB_lights','MLC_lights','MLD_lights','MLE_lights','MLO_lights','MLF_lights','MLG_lights','MLH_lights']
        TimeW=['Morning','Noon','Afternoon','Evening','Night','Original','EarlyMorning','LateAfternoon','LateEvening']
        for i in range(len(lightGrp)):
            if TimeW[i].lower()==TOD.lower():
                grp=lightGrp[i]
        grpL=''
        for gr in  lightGrp:
            lig=mc.ls(('*:'+gr),l=1,tr=1)
            if lig:
                for li in lig:
                    if mc.objExists(li) and 'Move_ctrl' in li and 'Character' in li and grp and grp not in li.split('|')[-1]:
                        lights.append(li)
                    if lig and 'Master' in lig[0] and 'Move_ctrl' in lig[0] and 'Character' in lig[0] and grp and grp  in lig[0].split('|')[-1]:
                        grpL=lig[0]
                        check=1
        SET=self.NJ17RLObjectsTList()[-1]
        if check==0:
            mc.error(u'==================场景缺少【%s】灯光组，请检查==========='%grp)
        if check==1 and lights:
            for light in lights:
                try:
                    mc.setAttr((light+'.visibility'),0)
                except:
                    mc.warning(u'===========【%s】被锁，无法隐藏，请检查文件===========')
                    pass

        if grpL:
            mc.setAttr((grpL+'.visibility'),1)
        return [check,grpL,grp]
    #------------------------------#
    # 【NJ2017：场景特殊属性物体选择
    # Author  : 韩虹
    # Data    :
    #------------------------------#
    def OBJAttrInfo(self,attr='SKY'):
        objs=mc.ls(tr=1,l=1)
        infos=[]
        check=0
        for obj in objs:
            if mc.objExists(obj+'.'+attr):
                infos.append(obj)
        if infos:
            check=1
        else:
            check=0
        return [check,infos]
#----------------------------------------------------------------------------------------------------------#
#【通用】数据库时间段查询
#@author:韩虹
#data：2016-06-20
#---------------------------------------------------

    def GDC_TODMsSQL(self,project,ep,sq,sc):
        import pyodbc
        try:
            cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=idmt-engine08;DATABASE=idmtPlex_%s;UID=EReader;PWD=123123'%(project))
        except:
            return None
        cursor = cnxn.cursor()
        cmd_sql = 'SELECT [T.O.D] FROM [TB_CommentsInfo] WHERE [EP] = \'%s\' AND [SEQ] = \'%s\' AND [SHOT] = \'%s\''%(ep,sq,sc)
        scInfo = cursor.execute(cmd_sql).fetchone()
        if scInfo:
            tod=scInfo[0]
        else:
            mc.error(u'=======')
        return scInfo[0]
#----------------------------------------------------------------------------------------------------------#
#【nj2017】SKY天空设置
#@author:韩虹
#data：2016-06-23
#---------------------------------------------------
#sky天空设置
    def nj_SKYSET(self):
        skys=self.OBJAttrInfo('SKY')
        check=skys[0]
        skyObj=skys[1]
        skyInfo=[]
        if check==1:
            for obj in skyObj:
                shape=mc.listRelatives(obj, s=1, f=1,type='VRayLightDomeShape')
                if shape:
                    for shap in shape:
                        if mc.objExists(shap+'.invisible') and mc.objExists(shap+'.domeSpherical'):
                            mc.setAttr((shap+'.invisible'),0)
                            mc.setAttr((shap+'.domeSpherical'),1)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【自动分层，单渲一帧】
    #  Author  : 韩虹
    #  Data    : 2016_6_28
    #infotype,co，普通灯光+color层设置
    #------------------------------#
    def gdc_renderPre(self):
        shotInfo = self.checkShotInfo()[0]
        shotname=self.checkShotInfo()[-1]
        serverPath = 'Z:/Projects/Ninjago/Ninjago_scratch/TD/renderInfo/'
        shotpath=serverPath+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        mc.sysFile(shotpath, makeDir=True)
        mc.renderSettings(fp=1)
        shot=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        #当前设置
        cam=self.gdc_camInfo()[0]
        camS=self.gdc_camInfo()[1]
        mc.loadModule(scan=True)
        mc.setFocus('modelPanel4')
        mc.modelEditor('modelPanel4', q=1,av=1)
        mc.lookThru(camS)
        #渲染起始帧
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        mc.currentTime(startFrame)

        mc.renderSettings(fp=1)
        #激活
        mc.modelEditor('modelPanel4', q=1,av=1)
        print '==========【render】 start============'
        mel.eval('source "renderWindowPanel.mel"')
        cmd="renderWindowRender redoPreviousRender renderView"
        mc.select(cam)
        mc.setFocus('modelPanel4')
        mel.eval(cmd)
        print '==========【render】 end============'
        #素材路径
        images=mc.renderSettings(firstImageName=True)[0].replace(('.'+str(startFrame)+'.iff'),'.png')
        mc.renderSettings(fp=1)
        imgDir=mc.workspace("images",q=1,fileRuleEntry=1)
        fullPath=mc.workspace(expandName=imgDir)
        if '/' in images:
            fileName=images.split('/')[0]
        else:
            fileName=images
        if os.path.exists(shotpath+fileName):
            try:
                shutil.rmtree(shotpath+fileName)
            except:
                pass
        if os.path.exists(fullPath+'/tmp/'+fileName):
            try:
                shutil.move((fullPath+'/tmp/'+fileName),shotpath)
            except:
                pass
        elif os.path.exists(fullPath+'/'+fileName):
            try:
                shutil.move((fullPath+'/'+fileName),shotpath)
            except:
                mc.error(u'==========文件移动出错，请检查【%s】是否为打开状态============='%(fullPath+'/'+fileName))
        else:
            mc.error(u'===========文件渲染路径无法找到，请设置project===========')
        return (shotpath+fileName)
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【相机】
    #  Author  : 韩虹
    #  Data    : 2016_6_29
    #
    #------------------------------#
    def gdc_camInfo(self):
        shotInfo = self.checkShotInfo()[0]
        shotname=self.checkShotInfo()[-1]
        camName='cam_'+shotname
        cams=mc.ls(ca=1,l=1)
        camInfo=[]
        cam=[]
        camN=''
        camS=''
        if cams:
            for ca in cams:
                if camName in ca and mc.listRelatives(ca,p=1,type='transform',f=1) and mc.listRelatives(ca,p=1,type='transform',f=1)[0] not in camInfo:
                    camInfo.append(mc.listRelatives(ca,p=1,type='transform',f=1)[0])
                    cam.append(ca)
        if len(camInfo)<1:
            mc.warning(u'========文件中缺少正确相机，请检查=======')
            mc.error(u'========文件中缺少正确相机，请检查=======')
        elif len(camInfo)>1:
            mc.warning(u'========文件中有多余相机，请检查=======')
            mc.error(u'========文件中有多余相机，请检查=======')
        else:
            camN=camInfo[0]
            camS=cam[0]
        return [camN,camS]
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【单渲一帧】
    #  Author  : 韩虹
    #  Data    : 2016_6_28
    #infotype,co，普通灯光+color层设置
    #------------------------------#
    def gdc_batchRender(self,filename=''):
        shotInfo = self.checkShotInfo()[0]
        shotname=self.checkShotInfo()[-1]
        serverPath = 'Z:/Projects/Ninjago/Ninjago_scratch/TD/renderInfo/'
        shotpath=serverPath+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        mc.sysFile(shotpath, makeDir=True)
        mc.renderSettings(fp=1)
        shot=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        #当前设置
        '''
        cam=self.gdc_camInfo()[0]
        camS=self.gdc_camInfo()[1]
        mc.loadModule(scan=True)
        mc.setFocus('modelPanel4')
        mc.modelEditor('modelPanel4', q=1,av=1)
        mc.lookThru(camS)

        #渲染起始帧
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        mc.currentTime(startFrame)

        mc.renderSettings(fp=1)
        #激活
        mc.modelEditor('modelPanel4', q=1,av=1)
        print '==========【render】 start============'
        #mel.eval('source "renderWindowPanel.mel"')
        #cmd="renderWindowRender redoPreviousRender renderView"
        mc.select(cam)
        mc.setFocus('modelPanel4')
        mel.eval(cmd)
        #mc.setAttr('defaultRenderGlobals.startFrame',startFrame)
        #mc.setAttr('defaultRenderGlobals.endFrame',startFrame)
        #mc.workspace(renderType=['images',shotpath])
        #mc.file(save=1,f = 1)
        #mc.render()
        '''
        print u'================试渲【%s】1001帧 start================'%filename
        self.gdc_RendertimeRecord()
        cmd='system ("Render  -rd \\\"'+shotpath+'\\\" -s 1001 -e 1001  -b 1 \\\"'+filename+'\\\" ")'
        mel.eval(cmd)
        print u'================开始试渲【%s】1001帧 end================'%filename
        self.gdc_RendertimeRecord()
        #素材路径
    def ImageMove(self):
        shotInfo = self.checkShotInfo()[0]
        shotname=self.checkShotInfo()[-1]
        serverPath = 'Z:/Projects/Ninjago/Ninjago_scratch/TD/renderInfo/'
        shotpath=serverPath+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        shot=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart
        images=mc.renderSettings(firstImageName=True)[0].replace(('.'+str(startFrame)+'.iff'),'.png')
        mc.renderSettings(fp=1)
        imgDir=mc.workspace("images",q=1,fileRuleEntry=1)
        fullPath=mc.workspace(expandName=imgDir)
        if '/' in images:
            fileName=images.split('/')[0]
        else:
            fileName=images
        if os.path.exists(shotpath+fileName):
            try:
                shutil.rmtree(shotpath+fileName)
            except:
                pass
        if os.path.exists(fullPath+'/tmp/'+fileName):
            try:
                shutil.move((fullPath+'/tmp/'+fileName),shotpath)
            except:
                pass
        elif os.path.exists(fullPath+'/'+fileName):
            try:
                shutil.move((fullPath+'/'+fileName),shotpath)
                print u'==========【render】 end============'
            except:
                mc.error(u'==========文件移动出错，请检查【%s】是否为打开状态============='%(fullPath+'/'+fileName))
        else:
            mc.error(u'===========文件渲染路径无法找到，请设置project===========')

        return (shotpath+fileName)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【渲染文件测存】
    #  Author  : 韩虹
    #  Data    : 2016_06_07
    #------------------------------#
    def nj_RenderFileTestSave(self,rendType='CHR'):
        locaPath='D:/TempInfo/renderLayerFile/'
        fileName=mc.file(q=1,sn=1,shn=1)
        if '_' in fileName and fileName.split('_')[0]=='nj' and len(fileName.split('_'))>4:
            shotInfo=fileName.split('_')
            fileSaveFile=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+rendType+'_lr_c001.mb'
            filepath=locaPath+shotInfo[0]+'/'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'/test/'
            mc.sysFile(filepath, makeDir=True)
            mc.file(type='mayaBinary')
            mc.file(rename=filepath+fileSaveFile)
            mc.file(save=1,type ='mayaBinary',f = 1)
        else:
            mc.warning(u'==========文件命名不正确，请检查文件命名=========')
            mc.error(u'==========文件命名不正确，请检查文件命名=========')
        return (filepath+fileSaveFile)
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【渲染文件测存】
    #  Author  : 韩虹
    #  Data    : 2016_06_07
    #------------------------------#
    def nj_RenderFileSave(self,rendType='CHR'):
        locaPath='D:/TempInfo/renderLayerFile/'
        fileName=mc.file(q=1,sn=1,shn=1)
        if '_' in fileName and fileName.split('_')[0]=='nj' and len(fileName.split('_'))>4:
            shotInfo=fileName.split('_')
            fileSaveFile=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_'+rendType+'_lr_c001.mb'
            filepath=locaPath+shotInfo[0]+'/'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'/'
            mc.sysFile(filepath, makeDir=True)
            mc.file(type='mayaBinary')
            mc.file(rename=filepath+fileSaveFile)
            mc.file(save=1,type ='mayaBinary',f = 1)
        else:
            mc.warning(u'==========文件命名不正确，请检查文件命名=========')
            mc.error(u'==========文件命名不正确，请检查文件命名=========')
        return 0
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【记录时间】
    #  Author  : 韩虹
    #  Data    :
    #------------------------------#
    def gdc_RendertimeRecord(self):
        import time
        print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【乐高2017项目】【时光刀材质转换】
    #  Author  : 韩虹
    #  Data    :
    #------------------------------#
    def nj17_TimeBladeC(self):
        objs=['MSH_TimeBladeBlue_nopower15_','MSH_TimeBladeBlue_power15_']
        meshs=mc.ls(type='mesh',l=1)
        blades=[]
        for mesh in meshs:
            ms=mc.listRelatives(mesh,ap=1,type = 'transform',f=1)
            for obj in objs:
                if obj in mesh and  ms and mc.objExists(ms[0]+'.visibility') and mc.getAttr(ms[0]+'.visibility')==1:
                    blades.append(mesh)
        meshF=[]
        shadeF=[]
        if not blades:
            print u'文件中没有时光刀'
            mc.error(u'文件中没有时光刀,请检查')
        for i in range(len(blades)):
            sg=mc.listConnections(blades[i],type='shadingEngine')
            if sg:
                shade=mc.listConnections((sg[0]+'.surfaceShader'),s=1,c=0,p=0)
                if shade and mc.objExists(shade[0]+'.coat_material_0'):
                    opshade=mc.listConnections((shade[0]+'.coat_material_0'),s=1,c=0,p=0)
                    if opshade and mc.objExists(opshade[0]+'.opacityMap') and mc.listConnections((opshade[0]+'.opacityMap'),s=1,c=0,p=0)!=[]:
                        meshF.append(blades[i])
                        shadeF.append(opshade[0])
        return [shadeF,meshF]

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【乐高2017项目】【时光刀渲染层创建】
    #  Author  : 韩虹
    #  Data    :
    #------------------------------#
    def nj17_TimeBladeRenderLayer(self):
        objs=mc.ls(sl=1,l=1)
        meshs=[]
        if not objs:
            mc.error(u'====没有选择物体，请选择======')
        for obj in objs:
            shape=mc.listRelatives(obj,s=1,f=1,type='mesh')
            if shape and 'MODEL' in obj:
                meshs.append(obj)
        if not meshs:
            mc.error(u'=====没有选择MODEL组下的mehs物体，请选择=====')
        info=self.nj17_TimeBladeC()
        shadeF=info[0]
        meshF=info[1]
        #lightcheck=self.lightGrpInfo()
        #check=lightcheck[0]
        #lightGrp=lightcheck[1]
        self.nj_RefIm()
        if not shadeF:
            mc.error(u'文件中没有时光刀或者时光刀透明贴图')
        GDC_RenderVrayLayer.GDC_RenderVrayLayer().gdc_VrayRenderDel(1,1)
        #mesL=meshs+[lightGrp]
        mesL=meshs
        mc.select(mesL)
        mc.createRenderLayer(mesL,name='TBC', noRecurse=1, makeCurrent=1)
        mc.editRenderLayerGlobals(currentRenderLayer='TBC')
        for i in range(len(shadeF)):
            op=mc.listConnections((shadeF[i]+'.opacityMap'),s=1,c=1,p=1)
            try:
                mc.disconnectAttr(op[1],op[0])
                mc.setAttr((shadeF[i]+'.opacityMap'),1,1,1)
            except:
                mc.warning(u'无法断开透明贴图，请检查文件')
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
        mc.select(meshF)
        mc.createRenderLayer(meshF,name='TBO', noRecurse=1, makeCurrent=1)
        mc.editRenderLayerGlobals(currentRenderLayer='TBO')
        for i in range(len(shadeF)):
            op=mc.listConnections((shadeF[i]+'.opacityMap'),s=1,c=1,p=1)
            shadeN=shadeF[i]+'_OP'
            SGN=shadeN+'SG'
            if mc.objExists(shadeN)==0:
                mc.shadingNode('VRayMtl', asShader=True,n=shadeN)
            if mc.objExists(SGN)==0:
                mc.sets(renderable=1,noSurfaceShader=1,em=1,n=SGN)
            try:
                mc.connectAttr(('%s.outColor' % shadeN),('%s.surfaceShader' % SGN))
            except:
                pass
            try:
                mc.connectAttr(op[1],('%s.diffuseColor' % shadeN),f=1)
            except:
                pass
            mc.sets(meshF[i],e=1, forceElement =SGN)
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")

