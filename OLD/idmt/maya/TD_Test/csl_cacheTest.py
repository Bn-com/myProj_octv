# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】
#  Author : 沈康
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

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
reload(sk_cacheFinalLayout)

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
    def csl_checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -50):
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        import os
        #---------------------------#
        # Setup 000  外部操作，
        #---------------------------#
        
        
        
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
        
        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType = 3)
        
        
        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType = 3)
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath(shotType = 3)
        
        # 本地另存
        localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_c001' + fileFormat
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
        camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPathN = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] +'_' + shotInfos[3]+ '_cam.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1)
                print u'\n'
                print u'==========================camera传输完毕=========================='
                print u'\n'
        
        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        # 预处理，约束清理
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
        #print(u'========================【约束】【烘焙】【成功】========================')
        
        
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
            assetNeedOutputInfo = sk_cacheFinalLayout.sk_cacheFinalLayout().skFLAssetNeedInfo(refInfos,noNeedRefNodeInfo,shotType=3)
        
        #---------------------------#
        # Setup 014 OTC和SET组导出
        # 务必使用ma格式，之后会用文本读取方式替换参考，避免打开后又加载参考，提高效率
        #---------------------------#
        # 导出SET_GRP和OTC_GRP文件
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET',shotType = 3)
        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC',shotType = 3)
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'
        
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
        
        # 判断是否ms_anim文件
        if shotInfos[4] == 'an':
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
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 1,shotType = 3)
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
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType = 3)
                print u'\n'
                print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
                print u'\n'
                # 输出cache
                # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, serverFile = server , cachePre = 0, refMode = 1 , createType = 0 , shotType = 3,resetPosition = 1)
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
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify = 1 , shotType = 3)
        
        
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
            fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] +'_'+ shotInfos[3] +'_base_fs_c001' + fileFormat
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
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('SET')
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPImport('OTC')
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
                MatLists = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial(cacheObjs,1,shotType = 3)
        
            # 场景搭建完毕
            # 载入anim
            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(serverFile = 1 ,shotType= 3)
            
            print u'\n'
            print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
            print u'\n'
            # 处理buging
        
            # 载入cache及自带的anim
            cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
            if cacheObjs:
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, server,shotType = 3,resetPosition = 1)
                # 处理还原物体
       
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheResetPositionImport(server,shotType = 3)
                # 进行参考reload
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
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateImport(shotType = 3)
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
            
            #---------------------------#
            # Setup 025 备份FL文件
            #---------------------------#
            # 本地保存
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            # 设置时间轴等消息
            # 命令
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]+ '_' + shotInfos[3]
            
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
                self.csl_checkCacheReturnMaterial(MatLists,shotType = 3)
            
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
                
                
                camName = 'CAM:cam_' + shotInfos[1] + '_' + shotInfos[2] + '_baked'
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
                
            #---------------------------#
            # Setup 029 由于之前还原了材质，asset的reference edit列表里会有记录，需要在没加载参考的情况下清理
            #---------------------------#
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
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                #print checkOutCmd
                mel.eval(checkOutCmd)
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')
        
            # 缺少check in baseFile
            print '\n'
            print(u'=========================================================================')
            print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))
            
            # 成功代码
            return 0
        
    #----------------------------------------------------------------------------------------------#
    
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
    def checkFinalLayoutExport(self, grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1 , cachePre = -50):
        if grpExport or cacheExport or animExport or assetInfoExport or hideInfoExport:
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            
            # info记录
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # 强制更新IK解算器
            mc.ikSystem(e = 1,sol = 1)
            
            # 预处理，约束清理
            if not hideInfoExport or not assetInfoExport:
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

            # 获取references信息
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # 处理大组
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
            
            # 在输出SET和OTC之前处理好anim中材质更改的情况
            # 这个会出错。。导致新参考材质挂掉
            #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            
            #导出SET和OTC
            if grpExport:
                # 清理旧的SET和OTC文件
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('SET')
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPDelete('OTC')
                # 导出SET_GRP和OTC_GRP文件
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('SET')
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneGRPExport('OTC')
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
                
                # 新建文件之前处理好SET_GRP文件
                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_sceneSETRefShaderReset(shotInfos,serverModify=1,shotType=3)
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')

            # 输出assetInfo
            if assetInfoExport:
                # 处理大组
                noNeedRefNodeInfo = []
                if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
                    allGrps = []
                    if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                        allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
                    if mc.listRelatives('SET_GRP',ad = 1,f=1):
                        allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
                    if allGrps:
                        for grp in allGrps:
                            if mc.referenceQuery(grp,isNodeReferenced = 1):
                                refNode = mc.referenceQuery(grp,referenceNode = 1)
                                noNeedRefNodeInfo.append(refNode)
                        if noNeedRefNodeInfo:
                            noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
                # 处理asset
                assetNeedOutputInfo = []
                rfnLv1 = refInfos[0][0]
                rfnPathLv1 = refInfos[1][0]
                for i in range(len(rfnLv1)):
                    ns = refInfos[2][0][i]
                    refNode = refInfos[0][0][i]
                    if noNeedRefNodeInfo:
                        if refNode not in noNeedRefNodeInfo:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            assetNeedOutputInfo.append(newPath)
                            assetNeedOutputInfo.append(ns)
                    else:
                        if refNode.split('_')[1][0] not in ['s', 'S']:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            assetNeedOutputInfo.append(newPath)
                            assetNeedOutputInfo.append(ns)
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
                print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')

            # 输出cache 及 anim
            if animExport:
                # 输出anim
                animObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimSetObjects()
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, server , cachePre)
                #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【输出】完毕=====================')

            # 输出cache
            if cacheExport:
                # 需要加入250分割处理
                # checkCacheSetObjects
                cacheObjs = sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetObjects()
                if cacheObjs:
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheVStateExport(cacheObjs,shotType = 3)
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, server=1 ,cachePre=0 , refMode = 1 , createType = 0,shotType = 3,resetPosition = 1)
                    #creatType 如果为1，则250(或N）个合为一个，如果为0，则一个asset合一个
                    #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
                    print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
                else:
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    
            # 输出hideInfo
            if hideInfoExport:
                # 记录：shot文件非参考的隐藏的显示层的物体
                unDisplayLayerObjs = []
                displayLayers = mc.ls(type = 'displayLayer')
                if displayLayers:
                    for layer in displayLayers:
                        isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                        if isRef == 0 and layer != 'defaultLayer':
                            viewState  = mc.getAttr(layer + '.visibility')
                            if viewState == False:
                                objs = mc.editDisplayLayerMembers( layer, query=True )
                                if objs:
                                    unDisplayLayerObjs = unDisplayLayerObjs + objs
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
                print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')

            # 成功代码
            return 0