# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具(ABC)】
#  Author : 韩虹
#  Data   : 2013_04~2013_06
#  Mender:韩虹
#  Data  :2014_05
# import sys
# sys.path.append('D:\\food\pyp\common')


# Q:an标记是_an_还是_ca_
# A:_ct_an

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式

# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import pymel.core as pm
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)
from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
reload(sk_hbExportCam)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.Hh_common import hh_RenderArnoldLayer
reload(hh_RenderArnoldLayer)
from idmt.maya.ShunLiu_common import csl_checkin
reload(csl_checkin)

import os
import re

class csl_cacheFinalLayout(object):
    def __init__(self):
        # namespace清理
        pass
        
    #----------------------------------------------------------------------------------------------#
    

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【总篇】【灯光】【FinalLayout环节工具】【后台】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#
    
    # cache最好先本地使用，最后upload并更新cache路径
    # anim可直接upload至服务器
    # 需要增加每个角色创建cache的功能
    # 新增功能：但凡cache物体和anim物体，只要其属于OTC_GRP,一概不参与cache和anim记录
    # template模式下，强制换anim参考，不处理帧信息，不导入相机，只输出cache到服务器端，不check in到服务器
    def csl_checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -50,shotType = 3, resetPosition= 1,smooth=1,EnvExort=1,ImageSizeCover=1, ):
        #---------------------------#
        # Setup 000  外部操作，
        #---------------------------#
        
        
        mel.eval('cycleCheck -e off')
        #---------------------------#
        # Setup 001  多级非参考的namespace清理。
        # 某些外包，喜欢做动作模板，然后import进来，这样形成了两级namespace，而在参考是不会记录import的那级参考。
        # 这种情况，要处理掉，不然后面记录参考信息时会出问题
        #---------------------------#
        # 处理非参考的namespace
        
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================多层namespace清理完毕===================='
        
        #---------------------------#
        # Setup 002  判断是否动画shot里的参考是否都有render 版本。如果没有，报错退出
        #---------------------------#
        # 检测参考是否正确，是否有render参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FLCheckRenderFile(refInfos)
        
        #---------------------------#
        # Setup 003  记录基本信息，修正时间轴
        #---------------------------#
        
        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
        


        if shotInfos[1] > '113':
            try:
                attrs = pm.ls('*:*.collarVis', r = True)
                for attr in attrs:
                    attr.disconnect(inputs = True,outputs = False)
                    attr.set(True) 
            except:
                pass
        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType )
        
        
        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType )
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath(shotType )
        
        # 本地另存
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]  
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]   
        localFile = localPath + shotName+'_an_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        
        
        
        #---------------------------#
        # Setup 005  清理外包残留的playblast表达式
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'
        
        #---------------------------#
        # Setup 006  清理未勾选的参考，清理垃圾节点，更新camera，IKR再启动
        #---------------------------#
        sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================未勾选参考清理完毕========================'
        print u'\n'
        
        # 初步清理垃圾节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(unuse=1 , turtle=1)
        
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print u'\n'
        
        # 更新摄像机           
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath=''
        if projectInfo in ['YongTai']:
            camServerPath = '//file-cluster/GDC/Projects/DomesticProject/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        else:            
            camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPathN = camServerPath + shotName+ '_cam.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,3)
                print u'\n'
                print u'==========================camera传输完毕=========================='
                print u'\n'
        
        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        #预处理，约束清理
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
        print(u'========================【约束】【烘焙】【成功】========================')
        
        self.csl_fixedcamfar()
        
        #---------------------------#
        # Setup 008 清除服务器data目录残留的SET和OTC文件
        # 【注意】 如果有SD环节，酌情清理OTC，SET需要从服务器端参考
        #---------------------------#
        # 清理服务器端旧的SET和OTC文件
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('SET')
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('OTC')
        
        
        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'
        
        
        #---------------------------#
        # Setup 010 动画文件内，隐藏的物体，记录下来，cache之后恢复隐藏
        #---------------------------#
        if shotType==2:
            unDisplayLayerObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FL_RefHideObjsRecord(server=1,shotType=2)
        if shotType==3:
            unDisplayLayerObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FL_RefHideObjsRecord(server=1,shotType=3)
        
                
        #---------------------------#
        # Setup 011 获取anim shot的参考信息
        #---------------------------#
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

        
        
        #---------------------------#
        # Setup 012 默认OTC和SET组内的参考不参与cache及重新参考，这里记录不需要的参考信息
        #---------------------------#
        # 处理大组
        noNeedRefNodeInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLNoNeedRefNodeInfo()
        
        #---------------------------#
        # Setup 013 本文件asset参考信息导出，给分解步骤用
        # 这里只记录角色和道具
        #---------------------------#
        # 输出需要的角色和道具参考信息
        if server:
            assetNeedOutputInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLAssetNeedInfo(refInfos,noNeedRefNodeInfo,shotType)
        

        #---------------------------#
        # Setup 014 OTC和SET组导出
        # 务必使用ma格式，之后会用文本读取方式替换参考，避免打开后又加载参考，提高效率
        #---------------------------#
        # 导出SET_GRP和OTC_GRP文件
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET',server,shotType)
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC',server,shotType )
#        if EnvExort==1:
#            self.csl_EnverInfoWrite (EnvInfo=[],shotType=shotType)
#            EnvFileName=self.csl_EnverInfoRead (EnvFileName='',shotType=shotType)
        
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'
        
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
        
        # 判断是否ms_anim文件
        if shotType==2 and shotInfos[3] == 'an':
            #---------------------------#
            # Setup 015 删除set参考，加快速度
            #---------------------------#
            # 首先删除set参考，加快速度
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================')
            print u'\n'
        if shotType==3 and shotInfos[4] == 'an':
            #---------------------------#
            # Setup 015 删除set参考，加快速度
            #---------------------------#
            # 首先删除set参考，加快速度
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================')
            print u'\n'            
            
            
        #---------------------------#
        # Setup 016 输出cache，以及传递动画的控制器动画
        # cache过程中，加入了对隐藏|组K帧物体的检测，记录显示隐藏动画以便还原
        #---------------------------#
        # 输出cache 及 anim
        # 先输出anim
        animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 1,shotType=shotType )
        #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
        print u'\n'
        print(u'=====================【Anim】【服务器端】【输出】完毕=====================')
        print u'\n'
        # 输出cache
        # 需要加入250分割处理
        # checkCacheSetObjects
        cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
        if cacheObjs:
            # 输出显示隐藏动画信息
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType )
            print u'\n'
            print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
            print u'\n'
            # 输出cache
            # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, serverFile = server , cachePre = 0, refMode = 1 , createType = 0 , shotType=shotType ,resetPosition=resetPosition)            
            if server:
                print u'\n'
                print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【Cache】【本地】【输出】完毕=====================')
                print u'\n'
        else:
            print u'\n'
            print(u'=====================【Cache】无物体！！！！！！=====================')
            print u'\n'
        
        #---------------------------#
        # Setup 017 对动画文件的处理告一段落，这里处理SET和OTC里面的参考替换，同时清理参考材质覆盖
        #---------------------------#
        # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify = 1 , shotType =shotType)


        #---------------------------#
        # Setup 018 开始新文件的架构
        #---------------------------#
        # 新建文件,临时文件夹另存
        mc.file(f=1, new=1)
        
        print '\n'
        print '[Ref Info]'
        print refInfos[0][0]
        print '\n'
        print(u'=========================【创建新文件】=========================')
        print '\n'
        
        # 准备先另存，因为update需要用到文件名
        fileName = shotName +'_base_fs_c001' + fileFormat
        # 本地文件
        localFile = localPath + fileName
        # 服务器端文件
        # serverFile = serverPath + fileName
        # 重命名
        mc.file( rename= localFile )
        mc.file(save = 1 ,force = 1)
        
    
        #---------------------------#
        # Setup 019 先导入OTC及SET，后创建参考。这里OTC和SET默认不加载，提高速度
        #---------------------------#
        # 导入场景
        # 必须先导入OTC，后载入参考，否则容易出错(PORORO经验)
        # 导回SET_GRP和OTC_GRP
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('SET',shotType)
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('OTC',shotType)
        print u'\n'
        print(u'=====================【Group】【服务器端】【导入】完毕=====================')
        print u'\n'
        #---------------------------#
        # Setup 020 加载需要的角色和道具类的render参考
        #---------------------------#
        # 导入reference及share nodes（新导入场景，后导入参考）
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_FLRefRebuild(refInfos,noNeedRefNodeInfo)
        
        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机
        if shotType ==2:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=2)
        if shotType ==3:
            sk_hbExportCam.sk_hbExportCam().camServerReference(info=3)                    
    
        #---------------------------#
        # Setup 022 新建后的文件大组重新处理
        #---------------------------#
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1)
        
    
        #---------------------------#
        # Setup 023 动画文件和fl文件的cache list对比，不一致则报错。 
        # 这里不一致一般在两种情况里发生
        # 1,anim文件和render文件cache list不一致;
        # 2.约束bake失败，某些CHR和PROP和SET有约束残留，导出去的时候CHR,PROP进了SET文件，而SET文件是默认不加载的，丢失部分cacheList
        #---------------------------#
        # 检测cache物体列表
        errorObjs = []
        for obj in cacheObjs:
            if mc.ls(obj) == []:
                errorObjs.append(obj)
        if errorObjs:
            print u'-------------------以下物体不存在-------------------'
            for info in errorObjs:
                print info
            print u'-------------------以上物体不存在-------------------'
            mc.error(u'=====================请通知前期检测anim和render版本cache list=====================')
    
        #---------------------------#
        # Setup 024 import cache
        # 1.备份材质，zwcache合并cache节点应用会出现线框模式，后面会还原材质。还原点很关键，否则会出现线框模式。
        # 2.载入cache，同时把K组导致的显示隐藏信息还原
        # 3.显示层物体还原
        #---------------------------#
        # 强行备份材质
        if cacheObjs:
            MatLists = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial(cacheObjs,1,shotType=shotType)
    
        # 场景搭建完毕
        # 载入anim
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(serverFile = 1 ,shotType=shotType)
        
        print u'\n'
        print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
        print u'\n'
        # 处理buging
    
        # 载入cache及自带的anim
        cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()           
        if cacheObjs:
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, server ,shotType , resetPosition)
            # 处理还原物体
            if resetPosition:
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheResetPositionImport.checkCacheResetPositionImport(server,shotType)            
            # 进行参考reload
            rfnLv1 = refInfos[0][0]
            for i in range(len(rfnLv1)):
                ns = refInfos[2][0][i]
                refNode = refInfos[0][0][i]
                if noNeedRefNodeInfo:
                    if refNode not in noNeedRefNodeInfo:
                        print u'================='
                        print refNode
                        print noNeedRefNodeInfo
                        print u'================='
                        newPath = mc.referenceQuery(refNode, filename=True)
            # 导入显示隐藏信息
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateImport(shotType )
            if server:
                print u'\n'
                print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【Cache】【本地】【导入】完毕=====================')
                print u'\n'
        else:
            print u'\n'
            print(u'=====================【Cache】无物体！！！！！！！=====================')
            print u'\n'
    
        # 处理显示层相关物体
        if unDisplayLayerObjs:
            hideObjs = []
            for obj in unDisplayLayerObjs:
                if mc.ls(obj):
                    hideObjs.append(obj)
            # 放到norender层
            if hideObjs:
                if mc.ls('norender',type = 'displayLayer'):
                    pass
                else:
                    mc.createDisplayLayer(empty = 1, name = 'norender')
                mc.setAttr('norender.visibility',0)
                mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
        print u'\n'
        print(u'=====================【Displayer】隐藏恢复=====================')
        print u'\n'
        self.chage_FileAndCacheFilePath_To_L_File_To_Half() #修改贴图及缓存路径为$(L_PROJECT)及把4K贴图改为半尺寸
        try:
            allRef = pm.system.listReferences()
            unloadFiles = []
            for ref in allRef:
                if not ref.isLoaded():
                    unloadFiles.append(ref)
                    ref.load()
                for k in ref.subReferences():
                    node = ref.subReferences()[k]
                    oldPath = node.path
                    if oldPath.find('_h_tx') > -1:
                        path = oldPath.replace('_h_tx','_h_ms_render').replace('/texture/','/master/')
                        try:
                            node.replaceWith(path)
                        except:
                            pass

            self.chage_FileAndCacheFilePath_To_L_File_To_Half()
            self.csl_fixedcamfar_Cam()
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            for un in unloadFiles:
                un.unload()

        except:
            pass
        

        #---------------------------#
        # Setup 025 备份FL文件
        #---------------------------#
        # 本地保存
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
        mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
        # 设置时间轴等消息
        # 命令
        if shotType == 2:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        
        #---------------------------#
        # Setup 026 镜头信息，时间轴信息处理
        #---------------------------#
        # 开始处理
        anim = idmt.pipeline.db.GetAnimByFilename(shot)
        startFrame = anim.frmStart

        endFrame = anim.frmEnd
        fpsFrame = anim.fps
        resW = anim.resolutionW
        resH = anim.resolutionH
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
            preStartFrame = startFrame - 10
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=endFrame)
            # 结束预留
            posEndFrame = endFrame + 10
            mc.playbackOptions(animationEndTime=posEndFrame)
        # 设置帧播放模式每帧
        mc.playbackOptions(playbackSpeed=0)
            
        # 允许undo
        mc.undoInfo(state=True, infinity=True)
        
        description = 'FinalLayout Base File'
    
        #---------------------------#
        # Setup 027 还原材质
        #---------------------------#
        # 强行还原材质
        if cacheObjs:
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheReturnMaterial(MatLists,finalLayout=1,shotType=shotType )
        
        # 烘焙表情贴图
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheBakeTexAniFiles()
    
        #---------------------------#
        # Setup 028 camera视野检测
        #---------------------------#
        # 处理camera视野
        if viewCheck:
            # 加载所有参考
            sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(0,1)
            from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene
            reload(sk_camMatrixScene)
            print '\n'
            print(u'=====================【Camera】【全自动检测视野】【开始】=====================')
            print '\n'
            # 记录显示层，默认全开启
            
            
            camName = 'CAM:cam_' + shotName + '_baked'
            if mc.ls(camName):
                sk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamConfig( startFrame, endFrame ,camName,[],8)
            else:
                pass
            # 特殊处理大面积低密度类物体，如_sea_
            seaObj = mc.ls('*:*_sea_*',type = 'transform') + mc.ls('*_sea_*',type = 'transform')
            if seaObj:
                for obj in seaObj:
                    mc.setAttr((obj+'.v'),1)
                    
            # 还原显示层        
            
            print '\n'
            print(u'=====================【Camera】【全自动检测视野】【成功】=====================')
            print '\n'
            description = 'FinalLayout Base File | View Sight Configed'

        try:

            eyebrows = pm.ls('*csl_c017006ZhaoJingS*:MSH_*_eyebrows_ca_')

            for eye in eyebrows:
                eye.visibility.set(False)

    
            allRef = pm.system.listReferences()
            refNodeS = []
            for ref in allRef:
                path = ref.path
                if '_anim' in path:
                    rndPath = path.replace('_anim','_render')
                    for r in allRef:
                        if rndPath == r.path:
                            refNodeS.append(ref)
                            
            if refNodeS:
                for n in refNodeS:
                    n.remove()

        except:
            pass

        #---------------------------#
        # Setup 029 smooth设置
        #---------------------------# 
#            if smooth==1 :
#                hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_0',renderusing='arnold')
#                hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_1',renderusing='arnold') 
#                hh_RenderArnoldLayer.hh_RenderArnold().csl_FinalSmoothSet(smoothInfo='smooth_2',renderusing='arnold')                
        #---------------------------#
        # Setup 039 由于之前还原了材质，asset的reference edit列表里会有记录，需要在没加载参考的情况下清理
        #---------------------------#
        self.csl_setattr(attrtype='aiStandIn',attr='visibility',num=1)       
        mc.file(save=1, force = 1)
        # 重打开FL文件
        #mc.file(localFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        # 处理cache环境变量
        #sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheEnvPath()
        
       #mc.file(save=1, force = 1)



        #---------------------------#
        # Setup 030 本地备份之后，check in
        #---------------------------#
        # 上传服务器处理
        if server == 1:
            #sk_cacheFinalLayout.sk_cacheFinalLayout().checkFinalLayoutUpdate()
            # 开始提交文件至服务器
            mc.file(save=1,force = 1)
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            fileInfo=''
            if shotType==3:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
            if shotType==2:
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]  + '|' + userName                    
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')
    
        # 缺少check in baseFile
        print '\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))
        
        #---------------------------#
#            # Setup 040 导出场景fs
#            #---------------------------#
#            if EnvExort==1:
#                mc.file( EnvFileName, open=True )
#                
#                anim = idmt.pipeline.db.GetAnimByFilename(shot)
#                startFrame = anim.frmStart
#        
#                endFrame = anim.frmEnd
#                fpsFrame = anim.fps
#                resW = anim.resolutionW
#                resH = anim.resolutionH
#                # 分辨率
#                mc.setAttr(('defaultResolution.width'), resW)
#                mc.setAttr(('defaultResolution.height'), resH)
#                # FPS
#                if fpsFrame == 25:
#                    mc.currentUnit(time='pal')
#                if fpsFrame == 24:
#                    mc.currentUnit(time='film')
#                if fpsFrame == 30:
#                    mc.currentUnit(time='ntsc')
#                # frame
#                if startFrame and fpsFrame:
#                    # 起始帧
#                    mc.playbackOptions(min=startFrame)
#                    # 起始预留
#                    preStartFrame = startFrame - 10
#                    mc.playbackOptions(animationStartTime=preStartFrame)
#                    # 结束帧
#                    mc.playbackOptions(max=endFrame)
#                    # 结束预留
#                    posEndFrame = endFrame + 10
#                    mc.playbackOptions(animationEndTime=posEndFrame)
#                # 设置帧播放模式每帧
#                mc.playbackOptions(playbackSpeed=0)
#                    
#                # 允许undo
#                mc.undoInfo(state=True, infinity=True)
#                
#                descriptionEnv = 'FinalLayout Env File'
#                if smooth==1:
#                    self.csl_FinalSmoothSet(smoothInfo='smooth_0')
#                    self.csl_FinalSmoothSet(smoothInfo='smooth_1')  
#                    self.csl_FinalSmoothSet(smoothInfo='smooth_2') 
#                fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
#                mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
#                if server == 1:
#               # 用户名
#                    userName = os.environ['USERNAME']
#                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
#                    projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
#                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] +'_'+newInfo[5] +'|' + userName
#                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
#                    #print checkOutCmd
#                    mel.eval(checkOutCmd)
#                    # checkIn
#                    mel.eval('idmtProject -checkin -description \" ' + descriptionEnv + '\"')    
                            
        # 成功代码
        return 0
        
    #----------------------------------------------------------------------------------------------#
    def csl_fixedcamfar(self):
    
        #import getpass
        #if getpass.getuser() != 'zhongming':
        #    return 0
        pm.currentTime(1001)
        sn = os.path.basename(pm.system.sceneName()).split('_')
        baseCamName = '_'.join(['cam',sn[1],sn[2],sn[3]])
          
        cams = pm.ls(type = 'camera')
        cam = ''

        for ca in cams:
            tmpCam = ca.getParent()
            if re.search(baseCamName, tmpCam.name(),re.IGNORECASE):
                cam = tmpCam
                print cam
                
        if cam != '':
            trans = pm.xform(cam,q = True , ws = True, a = True, t =True )
            x = trans[0] #pm.getAttr(cam + '.translateX')
            y = trans[1] #pm.getAttr(cam + '.translateY') 
            z = trans[2] #pm.getAttr(cam+ '.translateZ')
                        
                           
            scLsit = []
            allRef = pm.system.listReferences()

            isMove = False
            #s011010MountainRoad        
            for ref in allRef:
                if str(ref).find('csl_s007005SnowmountainAndGobi_h_ms_anim.mb') > -1 or str(ref).find('csl_s011010MountainRoad_h_ms_anim.mb') > -1:
                    ns = ref.namespace
                    isMove = True
                    for n in [':Set']:
                        node = pm.PyNode(ns + n)
                        scLsit.append(node)
                    

                if str(ref).find('csl_s008004SnowRange_h_ms_anim.mb') > -1:
                    isMove = True


                                 
            if isMove:
                
                ms1 = pm.ls('*:Master')
                ms2 = pm.ls('*:*:Master')
                ms3 = pm.ls('*:*:*:Master')
                
                 
                sels = ms1 + ms2 + ms3 + scLsit
                #sels.append(cam)
                for sel in sels:
                    self.doTransformToOrigin(sel,x,y,z)

    def doTransformToOrigin(self,sel,x,y,z):
        
        if sel.attr('tx').isLocked() or sel.attr('ty').isLocked() or sel.attr('tz').isLocked():

            sel = pm.group(sel)
            print '+'*50
            print sel
            print '+'*50

        w = pm.xform(sel,q = True, a = True, ws = True, t = True)
        o = sel.translateZ.get()
        mlt = 1
        if w[2] != o :
            if o != 0:
                mlt = w[2] / o
        
        mtx = x / mlt
        mty = y / mlt
        mtz = z / mlt
        
        n_tx = sel.translateX.get() - mtx
        n_ty = sel.translateY.get() - mty
        n_tz = sel.translateZ.get() - mtz
        
        
        
                
        sel.translateX.set(n_tx) 
        sel.translateY.set(n_ty) 
        sel.translateZ.set(n_tz) 

        key_channels_tx = pm.keyframe( sel.tx,  query=True,  name=True)
        key_channels_ty = pm.keyframe( sel.ty,  query=True,  name=True)
        key_channels_tz = pm.keyframe( sel.tz,  query=True,  name=True)
        pm.select(cl = True)
        if key_channels_tx:
            
            frames = pm.keyframe( key_channels_tx[0],  query=True,  timeChange=True)
            pm.keyframe(key_channels_tx[0],e = True, iub = True, r = True, o = 'over', vc = mtx * -1)
           
        if key_channels_ty:
            frames = pm.keyframe( key_channels_ty[0],  query=True,  timeChange=True)
            pm.keyframe(key_channels_ty[0],e = True, iub = True, r = True, o = 'over', vc = mty * -1)
            
        if key_channels_tz:
            frames = pm.keyframe( key_channels_tz[0],  query=True,  timeChange=True)
            pm.keyframe(key_channels_tz[0],e = True, iub = True, r = True, o = 'over', vc = mtz * -1)


    def csl_fixedcamfar_Cam(self):
    
        #import getpass
        #if getpass.getuser() != 'zhongming':
        #    return 0
        pm.currentTime(1001)
        sn = os.path.basename(pm.system.sceneName()).split('_')
        baseCamName = '_'.join(['cam',sn[1],sn[2],sn[3]])
          
        cams = pm.ls(type = 'camera')
        cam = ''
        moveCams = []
        for ca in cams:
            tmpCam = ca.getParent()
            if re.search(baseCamName, tmpCam.name(),re.IGNORECASE):
                moveCams.append(tmpCam)
                
                
        if moveCams:
            
            trans = pm.xform(moveCams[0],q = True , ws = True, a = True, t =True )
            x = trans[0] #pm.getAttr(cam + '.translateX')
            y = trans[1] #pm.getAttr(cam + '.translateY') 
            z = trans[2] #pm.getAttr(cam+ '.translateZ')
                        
                           
            
            allRef = pm.system.listReferences()

            isMove = False
            bigScene = ['csl_s008004SnowRange','csl_s007005SnowmountainAndGobi','csl_s011010MountainRoad']
            for ref in allRef:
                for bs in bigScene:
                    if str(ref).find(bs) > -1:
                        isMove = True

                                 
            if isMove:
                for c in moveCams:
                    self.doTransformToOrigin(c,x,y,z)

    def chage_FileAndCacheFilePath_To_L_File_To_Half(self):

        shotInfo= sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfo[0] == "csl":
            cacheFiles = mc.ls(type = 'cacheFile')

            for cache in cacheFiles:
                cachePath = mc.getAttr(cache + '.cachePath')
                pat = re.compile('${IDMT_PROJECTS}',re.IGNORECASE)
                cachePath = pat.sub('${L_PROJECTS}',cachePath)

                pat = re.compile('//file-cluster/GDC/Projects',re.IGNORECASE)
                cachePath = pat.sub('${L_PROJECTS}',cachePath)
                mc.setAttr(cache +'.cachePath', cachePath, type = 'string' )

            #csl_checkin.csl_checkin().csl_ImageSizeReadF(sizetype="half")

            mapFiles = mc.ls(type = 'file')
            eps = ['114','118','119']
            ep_scene_shot = shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
            for map in mapFiles:
                mapPath = mc.getAttr(map +'.fileTextureName')
                if shotInfo[1] in eps or ep_scene_shot == '117_014_003':
                    if 'c017004ZhaoJingCityH' in mapPath:
                        
                        pat = re.compile(r'csl_c017001ZhaoJing_coat_color_4k')
                        if re.search(pat,mapPath):
                            mapPath = os.path.dirname(mapPath) + '\\' + 'csl_c017001ZhaoJing_coat_color_xiashi_4k_half.png'
                            print mapPath
                    if 'c017006ZhaoJingS' in mapPath:
                        pat = re.compile(r'csl_c017001ZhaoJing_coat_color_4k_new')
                        if re.search(pat,mapPath):
                            mapPath = os.path.dirname(mapPath) + '\\' + 'csl_c017001ZhaoJing_coat_color_xiashi_4k_new_half.png'
                            print mapPath

                finalPath = mapPath
                
                mapPath = os.path.expandvars(mapPath)
                
                 
                mapPath = os.path.abspath(mapPath)
                dirname = os.path.dirname(mapPath)
                basename = os.path.splitext(os.path.basename(mapPath))
                
                
                halfSize = dirname + '\\' +  basename[0] + '_half' + basename[1]
                if os.path.isfile(halfSize):
                    finalPath = halfSize
                print finalPath
                
                pat = re.compile(r'\\\\file-cluster\\GDC\\Projects',re.IGNORECASE)
                finalPath = pat.sub('${L_PROJECTS}',finalPath)
                
                pat = re.compile(r'Z:\\Projects',re.IGNORECASE)
                finalPath = pat.sub('${L_PROJECTS}',finalPath)
                
                pat = re.compile(r'L:\\Projects',re.IGNORECASE)
                finalPath = pat.sub('${L_PROJECTS}',finalPath)

                #print '========================== renew path ================> ' + finalPath
                mc.setAttr(map +'.fileTextureName', finalPath, type = 'string' )


    #------------------------------#
    # 【辅助】【FL文件 ReferenceEdit还原】
    #------------------------------#

    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info ):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath() 
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
        print needFsFile
        
        # 不加载参考导入
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # 处理好所有参考
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        mc.file(save = 1, force = 1)

    #------------------------------#
    # 【辅助】【FL文件Cache上传】
    #------------------------------#

    # finalLayout上传服务器
    def checkFinalLayoutUpdate(self):
        # 获取cacheSet物体
        cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
        if cacheObjs:
            # 上传服务器
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheLocalUpdate()
            #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
            print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
        # 最后保存
        mc.file(save=1)

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【拆分】【重新输出数据】【后台】
    #------------------------------#

    # 重新输出数据
#    def checkFinalLayoutExport(self, grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1 , cachePre = -50):
#        if grpExport or cacheExport or animExport or assetInfoExport or hideInfoExport:
#            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
#            reload(sk_sceneTools)
#            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
#            reload(sk_referenceConfig)
#            
#            # info记录
#            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
#            
#            # 强制更新IK解算器
#            mc.ikSystem(e = 1,sol = 1)
#            
#            # 预处理，约束清理
#            if not hideInfoExport or not assetInfoExport:
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
#
#            # 获取references信息
#            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
#            
#            # 处理大组
#            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
#            
#            # 在输出SET和OTC之前处理好anim中材质更改的情况
#            # 这个会出错。。导致新参考材质挂掉
#            #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
#            
#            #导出SET和OTC
#            if grpExport:
#                # 清理旧的SET和OTC文件
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('SET')
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('OTC')
#                # 导出SET_GRP和OTC_GRP文件
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET')
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC')
#                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
#                
#                # 新建文件之前处理好SET_GRP文件
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify=1,shotType)
#                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
#
#            # 输出assetInfo
#            if assetInfoExport:
#                # 处理大组
#                noNeedRefNodeInfo = []
#                if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
#                    allGrps = []
#                    if mc.listRelatives('OTC_GRP',ad = 1,f=1):
#                        allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
#                    if mc.listRelatives('SET_GRP',ad = 1,f=1):
#                        allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
#                    if allGrps:
#                        for grp in allGrps:
#                            if mc.referenceQuery(grp,isNodeReferenced = 1):
#                                refNode = mc.referenceQuery(grp,referenceNode = 1)
#                                noNeedRefNodeInfo.append(refNode)
#                        if noNeedRefNodeInfo:
#                            noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
#                # 处理asset
#                assetNeedOutputInfo = []
#                rfnLv1 = refInfos[0][0]
#                rfnPathLv1 = refInfos[1][0]
#                for i in range(len(rfnLv1)):
#                    ns = refInfos[2][0][i]
#                    refNode = refInfos[0][0][i]
#                    if noNeedRefNodeInfo:
#                        if refNode not in noNeedRefNodeInfo:
#                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
#                            assetNeedOutputInfo.append(newPath)
#                            assetNeedOutputInfo.append(ns)
#                    else:
#                        if refNode.split('_')[1][0] not in ['s', 'S']:
#                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
#                            assetNeedOutputInfo.append(newPath)
#                            assetNeedOutputInfo.append(ns)
#                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType )
#                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
#                print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
#
#            # 输出cache 及 anim
#            if animExport:
#                # 输出anim
#                animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
#                sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, server , cachePre)
#                #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
#                print(u'=====================【Anim】【服务器端】【输出】完毕=====================')
#
#            # 输出cache
#            if cacheExport:
#                # 需要加入250分割处理
#                # checkCacheSetObjects
#                cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
#                if cacheObjs:
#                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType )
#                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
#                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, server=1 ,cachePre=0 , refMode = 1 , createType = 0,shotType,resetPosition )
#                    #creatType 如果为1，则250(或N）个合为一个，如果为0，则一个asset合一个
#                    #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
#                    print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
#                else:
#                    print(u'=====================【Cache】无物体！！！！！！！=====================')
#                    
#            # 输出hideInfo
#            if hideInfoExport:
#                # 记录：shot文件非参考的隐藏的显示层的物体
#                unDisplayLayerObjs = []
#                displayLayers = mc.ls(type = 'displayLayer')
#                if displayLayers:
#                    for layer in displayLayers:
#                        isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
#                        if isRef == 0 and layer != 'defaultLayer':
#                            viewState  = mc.getAttr(layer + '.visibility')
#                            if viewState == False:
#                                objs = mc.editDisplayLayerMembers( layer, query=True )
#                                if objs:
#                                    unDisplayLayerObjs = unDisplayLayerObjs + objs
#                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType )
#                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
#                print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')
#
#            # 成功代码
#            return 0

    #------------------------------#
    # 【拆分】【重新导入数据】【后台】
    #------------------------------#

#    # 重新载入数据
#    def checkFinalLayoutImport(self, grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 ,server = 1):
#        if grpImport or cacheImport or animImport or assetInfoImport or hideInfoImport:
#            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
#            reload(sk_sceneTools)
#            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
#            reload(sk_referenceConfig)
#            import os
#            
#            # info记录
#            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
#            
#            # 处理大组
#            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
#            
#            # 获取references信息
#            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
#            
#            # 首先处理好时间轴
#            # FPS
#            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS')
#            # frame
#            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame')
#            
#            #导入SET和OTC
#            if grpImport:
#                # 清除SET_GRP和OTC的参考
#                # 目前通过namespace获取物体判断是否在两个组内
#                refNode = refInfos[0][0]
#                #refPathInfo = refInfos[1][0]
#                refNsInfo = refInfos[2][0]
#                for i in range(len(refNsInfo)):
#                    mc.namespace(setNamespace = (  ':' + refNsInfo[i]))
#                    objs = mc.namespaceInfo(ls= 1,dagPath =1 )
#                    mc.namespace(setNamespace = ':')
#                    if objs:
#                        needObj = ''
#                        for obj in objs:
#                            if obj[-1] == '_' and mc.listRelatives(obj, c= 1,type = 'mesh'):
#                                needObj = obj
#                                break
#                        if needObj:
#                            objLong = mc.ls(needObj,l=1)[0]
#                            # 判断是否在两个组
#                            if 'SET_GRP' in objLong or 'OTC_GRP' in objLong:
#                                print objLong
#                                print refNode[i]
#                                # 执行删除参考
#                                mc.file(rfn = refNode[i] , removeReference = 1)
#                    print(u'=====================【Group】【原参考】【清理】完毕=====================')
#                # 删除SET_GRP和OTC_GRP
#                if mc.ls('SET_GRP'):
#                    mc.delete('SET_GRP')
#                if mc.ls('OTC_GRP'):
#                    mc.delete('OTC_GRP')
#                # 导回SET_GRP和OTC_GRP
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('SET')
#                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('OTC')
#                print(u'=====================【Group】【服务器端】【导入】完毕=====================')
#            
#            # 创建asset
#            if assetInfoImport:
#                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType )
#                if os.path.exists(assetNeedServerPath +  'assetReference.txt'):
#                    assetNeedOutputInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead((assetNeedServerPath +  'assetReference.txt'))
#                    if assetNeedOutputInfo:
#                        for i in range(len(assetNeedOutputInfo)/2):
#                            newPath = assetNeedOutputInfo[i*2]
#                            ns = assetNeedOutputInfo[i*2 + 1]
#                            mc.file(newPath, r=1, namespace= ns , referenceNode = (ns + 'RN') )
#                            print u'\n'
#                            print(u'=====================【创建参考】【%s】=====================' % (ns))
#                            print u'\n'
#                else:
#                    print u'\n'
#                    print(u'=====================【server缺少】【%s】请重新【输出】=====================' % ('assetInfo'))
#                    print u'\n'
#                
#            # 载入anim
#            if animImport:
#                #animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
#                sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(server)
#                #print(unicode('=====================【Anim】【服务器端】【导入】完毕=====================', "utf8"))
#                print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
#
#            # 输入cache
#            if cacheImport:
#                cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
#                if cacheObjs:
#                    #sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, server)
#                    sk_cacheFinalLayout.sk_cacheFinalLayout().sk_flCacheImportRefreshShaders(shotType )
#                    # 导入显示隐藏信息
#                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateImport(shotType ,resetPosition )
#                    # 处理cache环境变量
#                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheEnvPath()
#                    #print(unicode('=====================【Cache】【服务器端】【导入】完毕=====================', "utf8"))
#                    print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
#                else:
#                    print(u'=====================【Cache】无物体！！！！！！！=====================')
#                    
#            # 载入hideInfo
#            if hideInfoImport :
#                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType )
#                unDisplayLayerObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead((hideObjsServerPath +  'shotHideObjs.txt'))
#                if unDisplayLayerObjs:
#                    hideObjs = []
#                    for obj in unDisplayLayerObjs:
#                        if mc.ls(obj):
#                            hideObjs.append(obj)
#                    # 放到norender层
#                    if hideObjs:
#                        if mc.ls('norender',type = 'displayLayer'):
#                            pass
#                        else:
#                            mc.createDisplayLayer(empty = 1, name = 'norender')
#                        mc.setAttr('norender.visibility',0)
#                        mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
#                        print u'\n'
#                        print(u'=====================【Displayer】隐藏恢复=====================')
#                        print u'\n'

    def csl_checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0,shotType=3 ):
        if finalLayout:
            MatLists = self.csl_checkCacheRecordMaterialImport(shotType)
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)
                
    def csl_checkCacheRecordMaterialImport(self,shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = self.checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        MatLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            MatLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                MatLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return MatLists 
#
    def csl_FinalcheckFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.csl_FinalcheckFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
#
    def csl_FinalcheckFileRead(self, path):
        print u'>>>>>>[read]'
        print path
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
#读取smooth信息
    def csl_FinalSmoothMeshRead(self,meshinfo=[],smoothInfo='smooth_2'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        nsList = refInfos[2][0]
        if 'UI' in nsList:
            nsList.remove('UI')
        if 'shared' in nsList:
            nsList.remove('shared')
        if 'CAM' in nsList:
            nsList.remove('CAM')  
        for ns in nsList:
            #ns='csl_c001001ShunLiuFin'
            if '_' in ns and ":" not in ns:
                assetInfo = ns.split('_')
                Infopath=serverPath+'data/AssetInfos/smoothSetInfo/'+assetInfo[0]+'/'+assetInfo[1]+ '/h/'+smoothInfo+'.txt'
                if Infopath:
                    meshsmooth=sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileRead(Infopath)
                    #mesh='MSH_c_hi_logo_ca_'
                    #mc.select(mesh)
                    #mc.ls(mesh)
                    
                    if meshsmooth:
                        for mesh in meshsmooth:
                            meshShapes=mc.ls(type='mesh',l=1)
                            for i in range(len(meshShapes)):
                                if "|" not in mesh and mesh in meshShapes[i]:
                                    meshinfo.append(meshShapes[i])
                                if "|" in mesh:
                                    mes=mesh.split('|')
                                    if len(mes)==1 and mes[0] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])
                                    if len(mes)==2 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])                                    
                                    if len(mes)==3 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i] and mes[2] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i]) 
                                    if len(mes)==4 and mes[0] in  meshShapes[i] and mes[1] in  meshShapes[i] and mes[2] in  meshShapes[i] and mes[3] in  meshShapes[i]:
                                        meshinfo.append(meshShapes[i])
                        break
        return meshinfo
#设置相应smooth 
    def csl_FinalSmoothSet(self,meshinfo=[],smoothInfo='smooth_2'):
        meshinfo=self.csl_FinalSmoothMeshRead(meshinfo=[],smoothInfo=smoothInfo)
        if meshinfo:
            for meshShape in  meshinfo:
                if meshShape!=None and smoothInfo=='smooth_2':
                    mc.setAttr((meshShape+'.aiSubdivType'),1)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),2)
                if meshShape!=None and smoothInfo=='smooth_1':
                    mc.setAttr((meshShape+'.aiSubdivType'),1)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),1)
                if meshShape!=None and smoothInfo=='smooth_0':
                    mc.setAttr((meshShape+'.aiSubdivType'),0)
                    mc.setAttr((meshShape+'.aiSubdivIterations'),0)
                                     
        print(u'=====================【smooth设置完成】【%s】=====================' % (smoothInfo))          
#记录参考场景
    def csl_EnverInfoRecord (self,EnvInfo=[],shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]
        EnvInfoPath=''
        if shotType==3:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        mc.sysFile(temimagepath, makeDir=True)            
        if refName:
            for i in range(len(refName)):
                if refName[i].split('_')[1][0] in ['s', 'S']:
                    EnvInfo.append(refName[i])   
        
        self.csl_FinalcheckFileWrite((EnvInfoPath +  'EnvInfo.txt'), EnvInfo)
        return  EnvInfo

#读取场景并导出场景
    def csl_EnverInfoWrite (self,EnvInfo=[],shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]
        EnvInfoPath=''
        EnvRnInfo=[]
        EnvFileInfo=[]
        EnvNameSpace=[]
        if shotType==3:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'
        if refName:
            for i in range(len(refName)):
                if refName[i].split('_')[1][0] in ['s', 'S']:
                    EnvNameSpace.append(refName[i])   
                    EnvRnInfo.append(refInfos[0][0][i])
                    EnvFileInfo.append(refInfos[1][0][i])            
        EnvInfo=EnvRnInfo + [u'----------------']+ EnvFileInfo+ [u'----------------']+  EnvNameSpace     
        self.csl_FinalcheckFileWrite((EnvInfoPath +  'EnvInfo.txt'), EnvInfo) 
        return EnvInfo
    
    def csl_EnverInfoRead (self,EnvFileName='',shotType=3):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType=3)
        
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refName = refInfos[2][0]    
        EnvName=''
        EnvInfoPath=''
        if shotType==3:
            EnvName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_env_fs.ma'
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'+shotInfo[3]+'/'
        if shotType==2:
            EnvName=shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_env_fs.ma'
            EnvInfoPath=serverPath+'data/AnimInfo/'+shotInfo[1]+'/'+shotInfo[2]+'/'  
        
        EnvFileName=renderFilePathServer+EnvName
           
        EnvInfo=self.csl_FinalcheckFileRead(EnvInfoPath+'EnvInfo.txt')
        EnvExr=[]
        if EnvInfo:
            signKeyIndex = sk_cacheFinalLayout.sk_cacheFinalLayout().checkListSameAllIndex(EnvInfo,u'----------------')[0]
            mc.select(cl=1)
            EnvExr=[]
            for i in range(signKeyIndex):
            #print (ImageInfo[i]+'.....'+ ImageInfo[i+signKeyIndex+1]+'==================')
                EnvRN=EnvInfo[i]
                EnvFile=EnvInfo[i+signKeyIndex+1]
                EnvNamespace=EnvInfo[i+2*signKeyIndex+2]
                EnvFileRender=EnvFile.replace('_ms_anim', '_ms_render')
                mc.file(EnvFileRender,loadReference=EnvRN)
    
                EnvExr.append(EnvNamespace+':SET')
    
        if EnvExr:   
            mc.select(EnvExr)
            mc.file(EnvFileName, force=1, options="v=0" , type='mayaAscii', preserveReferences=1, exportSelected=1)
            return  EnvFileName

#适用于maya2014,修改自sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial
    def csl_checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ,shotType = 3):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if not mc.ls(obj):
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                print(u'------------------------请检测物体清单------------------------')
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    meshs = mc.listRelatives(obj,ni=1,type = 'mesh',s =1 )
                    for mesh in meshs:
                        if mc.listConnections(mesh,destination = 1,type = 'shadingEngine'):
                            nodeSG = mc.listConnections(mesh,destination = 1,type = 'shadingEngine')
                            for node in nodeSG:
                                needSG.append(node)
                SG = list(set(needSG))
        # 备份信息
        MatLists = dict({})
        for node in SG:
            connectObjsSG = mc.sets(node, q=1)
            if connectObjsSG:
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.csl_checkCacheRecordMaterialExport(MatLists,shotType)
        return MatLists

    def csl_checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        if shotType == 2:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        SGKeys = MatLists.keys()
        allInfo = []
        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        fileInfo = 'ShotShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)
        self.checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo         

    def csl_cachemeshAdd(self) :
        import re
        meshAdd=[]    
        meshs=mc.ls(type='transform',l=1)
        if meshs:
            for mesh in meshs:
                if 'CHR' in mesh.split('|') and 'MODEL' in mesh.split('|') and re.search('eye_highlight',mesh)!=None:
                    meshAdd.append(mesh)
        if meshAdd:
            return meshAdd 
        else:
            return 0 

    def csl_setattr(self,attrtype='aiStandIn',attr='visibility',num=1):
        objs=mc.ls(type=attrtype ,l=1)
        if objs:
            for obj in objs:
                Arnold=mc.listRelatives(obj,p = 1,f=1)
                if Arnold and mc.nodeType(Arnold[0])=='transform':
                    try:
                        mc.setAttr((Arnold[0]+'.'+attr),int(num))
                    except:
                        print u'==========================【%s】==========================' % (Arnold[0]+'.'+attr)                              

    def csl_refneedInfo(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refRN=refInfos[0][0]
        reffile=refInfos[1][0]
        refnamespace=refInfos[2][0]
        refRNneedList=[]
        reffileRNneedList=[]
        refneedList=[]    
        setneed=['s001007ShootingGallery','s001008DormitoryExt','s001009PlayGround','s001010MainBuilding','s001001TrainingGround','s001002TrainingGroundGate']
        for i in range(len(refRN)):
            if 'csl' in refRN[i] and '_' in refRN[i] and refnamespace[i].split('_')[1] in setneed:
                refRNneedList.append(refRN[i])
                reffileRNneedList.append(reffile[i])
                refneedList.append(refnamespace[i])     
    
        return [refRNneedList,reffileRNneedList ,refneedList]  

    def csl_setRefSwitch(self,ID='s001020MilitaryCamp'):
        setinfoList=self.csl_refneedInfo()
        fileshort=mc.file(q=1,shn=1,sn=1)
        temppath='D:/Info_Temp/setswitch/'
        mc.sysFile(temppath, makeDir=True)        
        setrefRN=setinfoList[0]
        if setrefRN:
            for i in range(len(setrefRN)):
                mc.file(rfn = setrefRN[i] , removeReference = 1)
                print u'====已经删除【%s】参考===' % setinfoList[2][i].split('_')[1]
                
            refRNnew='csl_'+ID+'RN'
            refNamespaceN='csl_'+ID+'_h'
            refoldfile=setinfoList[1][0]
            refoldinfo=setinfoList[1][0].split('_')[1]
            refFileN=refoldfile.replace(refoldinfo,ID)
            mc.file(refFileN, r=1, namespace=refNamespaceN , referenceNode = refRNnew) 
            mc.file(rename=(temppath+fileshort))
            mc.file(save=1,type ='mayaBinary',f = 1)
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
            print u'====【%s】场景已经替换===' %    fileshort 
            print u'====文件路径【%s】===' %    temppath
        else:
            print u'===【%s】没有需要替换的场景===='  %    fileshort                                                                                                                         