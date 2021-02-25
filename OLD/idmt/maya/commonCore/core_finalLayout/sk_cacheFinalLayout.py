# -*- coding: utf-8 -*-
# 【通用】【FinalLayout环节工具】
#  Author : 沈康
#  Data   : 2013_04~2013_06
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
import os,re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_cacheFinalLayout(object):
    def __init__(self):
        # namespace清理
        self.tempNs = '_foodTemp'
        self.tempBlend = 'foodBlend_'

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【UI篇】【灯光】【FinalLayout界面】
    #------------------------------#

    # finalLayout界面
    def sk_sceneFinalLayoutUI(self):
        from idmt.maya.py_common import sk_checkCommon
        reload(sk_checkCommon)
        from idmt.maya.py_common import sk_camMatrixScene
        reload(sk_camMatrixScene)
        
        # 窗口
        if mc.window ("sk_sceneFinalLayoutTools",ex=1):
            mc.deleteUI( "sk_sceneFinalLayoutTools", window=True )
        mc.window("sk_sceneFinalLayoutTools",title="FinalLayout Tools", widthHeight=(260, 375),menuBar=0)
       
        # 面板
        mc.scrollLayout( 'scrollLayout' )
        
        # finalLayout自动
        mc.frameLayout( label=u'FinalLayout Auto| 自动化FinalLayout', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout(numberOfColumns = 2,columnWidth2=(120, 120))
        mc.button(l=u'FinalLayout快速版',bgc = [0.1,0.8,0.2],width = 120,height = 30,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutPerform()')
        mc.button(l=u'FinalLayout完整版',bgc = [0.1,0.8,0.8],width = 120,height = 30,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutPerform(1,1)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # finalLayout分解导出
        mc.frameLayout( label=u'FinalLayout Export| 【An】导出信息', borderStyle='etchedOut' ,width = 250 )
        # grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80 , 80 ,80))
        mc.button(l=u'导出OTC文件',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutExport(1,0,0,0,0)')
        mc.button(l=u'导出AssetInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutExport(0,0,0,1,0)')
        mc.button(l=u'输出Camera',bgc = [0.0,0.0,0.0],width = 80,height = 22,c='from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate()')
        mc.setParent( '..' )
        
        
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80, 80, 80 ))
        mc.button(l=u'导出Cache',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutExport(0,1,0,0,0)')
        mc.button(l=u'导出AnimInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutExport(0,0,1,0,0)')
        mc.button(l=u'导出HideInfo',bgc = [0.0,0.0,0.0],width = 80,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutExport(0,0,0,0,1)')
        mc.setParent( '..' )
        
        mc.setParent( '..' )

        # finalLayout分解导入
        mc.frameLayout( label=u'FinalLayout Import| 【Fs】导入信息', borderStyle='etchedOut' ,width = 250 )
        # grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80 , 80 ,80))
        mc.button(l=u'导入OTC文件',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutImport(1,0,0,0,0)')
        mc.button(l=u'创建Asset',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutImport(0,0,0,1,0)')
        mc.button(l=u'参考Camera',bgc = [0.0,0.0,0.0],width = 80,height = 22,c='mel.eval(\'source zwCameraImportExport.mel; zwGetCameraUI;\')')
        mc.setParent( '..' )
        
        mc.rowLayout(numberOfColumns = 3,columnWidth3=(80, 80 ,80))
        mc.button(l=u'导入Cache',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutImport(0,1,0,0,0)')
        mc.button(l=u'导入AnimInfo',bgc = [0.0,0.0,0.0],width = 75,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutImport(0,0,1,0,0)')
        mc.button(l=u'导入HideInfo',bgc = [0.0,0.0,0.0],width = 80,height = 22,c ='from idmt.maya.commonCore.core_finalLayout import sk_finalLayout\nreload(sk_finalLayout)\nsk_finalLayout.sk_finalLayout().checkFinalLayoutImport(0,0,0,0,1)')
        mc.setParent( '..' )
        
        mc.setParent( '..' )
        
        # 参考材质历史清理
        mc.frameLayout( label=u'参考材质历史清理 | 所有参考unload状态', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs文件】清理参考材质历史=====',bgc = [0.0,0.0,0.0],width = 240,height = 28,c ='from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig\nreload(sk_referenceConfig)\nsk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # 导入CamInOut信息
        mc.frameLayout( label=u'Camera视野信息导入 | 从服务器端读取已经解算好的数据', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'=====【Fs|Lr文件】Camera信息导入=====',bgc = [0.0,0.0,0.0],width = 240,height = 28,c ='from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene\nreload(sk_camMatrixScene)\nsk_camMatrixScene.sk_camMatrixScene().sk_sceneCamServerInfoImport()')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        
        # 视野检测
        mc.frameLayout( label=u'Camera视野检测 | 视野内显示，视野外隐藏', borderStyle='etchedOut' ,width = 250 )
        mc.rowLayout()
        mc.button(l=u'======【Fs文件】Camera视野检测======',bgc = [0.15,0.55,0.95],width = 240,height = 38,c ='from idmt.maya.commonCore.core_mayaCommon import sk_camMatrixScene\nreload(sk_camMatrixScene)\nsk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamConfigBatch(0)')
        mc.setParent( '..' )
        mc.setParent( '..' )
        
        # 视野检测
        mc.frameLayout(label = u'测试阶段，若有报错信息，请及时联系TD',borderStyle='etchedOut' ,width = 250 )
        mc.setParent( '..' )
        
        mc.setParent("..")
        mc.showWindow( "sk_sceneFinalLayoutTools" )

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
    #　shotType　字段信息　２　只有集/场 和 镜头号 | 3 集 场 镜头号都体现
    # resetPosition 原点出cache模式
    def checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -50 ,shotType = 2 , resetPosition = 0):
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
        self.sk_FLCheckRenderFile(refInfos)

        #---------------------------#
        # Setup 003  记录基本信息，修正时间轴
        #---------------------------#

        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        if shotType == 2:
            print(u'=====================【%s_%s】【FinalLayout】开始处理!!!====================='%(shotInfos[1],shotInfos[2]))
        if shotType == 3:
            print(u'=====================【%s_%s_%s】【FinalLayout】开始处理!!!====================='%(shotInfos[1],shotInfos[2],shotInfos[3]))
        print(u'=========================================================================')

        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType)


        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType)
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath(shotType)

        # 本地另存
        if shotType == 2:
            localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_c001' + fileFormat
        if shotType == 3:
            localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_' + shotInfos[4] + '_c001' + fileFormat
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
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(0)
        
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print u'\n'

        # 更新摄像机
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        if shotType == 2:
            camServerPath = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_cam_baked.ma'
        if shotType == 3:
            camServerPath = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_cam_baked.ma'
        if server:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,shotType)
            print u'\n'
            print u'==========================camera传输完毕=========================='
            print u'\n'
        
        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        # 预处理，约束清理
        self.sk_checkBakeConstraints()
        # 处理贴图动画
        self.sk_checkTextureAnimationExport(server)
        #print(u'========================【约束】【烘焙】【成功】========================')


        #---------------------------#
        # Setup 008 清除服务器data目录残留的SET和OTC文件
        # 【注意】 如果有SD环节，酌情清理OTC，SET需要从服务器端参考
        #---------------------------#
        # 清理服务器端旧的SET和OTC文件
        self.sk_sceneGRPDelete('SET',shotType)
        self.sk_sceneGRPDelete('OTC',shotType)


        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        # 记录otc参考
        otcRefList = self.otcRefCheck()
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'
        

        #---------------------------#
        # Setup 010 动画文件内，隐藏的物体，记录下来，cache之后恢复隐藏
        #---------------------------#
        unDisplayLayerObjs = self.sk_FL_RefHideObjsRecord(server,shotType)

        #---------------------------#
        # Setup 011 获取anim shot的参考信息
        #---------------------------#
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()


        #---------------------------#
        # Setup 012 默认OTC和SET组内的参考不参与cache及重新参考，这里记录不需要的参考信息
        #---------------------------#
        # 处理大组
        noNeedRefNodeInfo = self.skFLNoNeedRefNodeInfo()

        #---------------------------#
        # Setup 013 本文件asset参考信息导出，给分解步骤用
        # 这里只记录角色和道具
        #---------------------------#
        # 输出需要的角色和道具参考信息
        if server:
            assetNeedOutputInfo = self.skFLAssetNeedInfo(refInfos,noNeedRefNodeInfo,shotType)
        
        #---------------------------#
        # Setup 014 OTC和SET组导出
        # 务必使用ma格式，之后会用文本读取方式替换参考，避免打开后又加载参考，提高效率
        #---------------------------#
        # 导出SET_GRP和OTC_GRP文件
        self.sk_sceneGRPExport('SET',1,shotType,[])
        self.sk_sceneGRPExport('OTC',1,shotType,otcRefList)
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'

        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
    
        # 判断是否ms_anim文件
        if shotInfos[shotType + 1] not in ['an','sa']:
            return

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
        animObjs = self.checkAnimSetObjects()
        self.checkAnimCurveInfoExport(animObjs, serverFile =1 , shotType = shotType)
        #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
        print u'\n'
        print(u'=====================【Anim】【服务器端】【输出】完毕=====================')
        print u'\n'
        # 输出cache
        # 需要加入250分割处理
        # checkCacheSetObjects
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            # 输出显示隐藏动画信息
            self.checkCacheVStateExport(cacheObjs,shotType,server)
            print u'\n'
            print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
            print u'\n'
            # 输出cache
            # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
            self.checkCacheSetCacheExport(cacheObjs, serverFile = server , cachePre = cachePre , refMode = 1 , createType = 0 , shotType = shotType , resetPosition = resetPosition)
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
        if shotType == 2:
            configInfo = [shotInfos[0],shotInfos[1],shotInfos[2]]
        if shotType == 3:
            configInfo = [shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3]]
        self.sk_sceneSETRefShaderReset(configInfo)

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
        fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_base_fs_c001' + fileFormat
        if shotType == 3:
            fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_base_fs_c001' + fileFormat
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
        self.sk_sceneGRPImport('SET',shotType)
        self.sk_sceneGRPImport('OTC',shotType)
        print u'\n'
        print(u'=====================【Group】【服务器端】【导入】完毕=====================')
        print u'\n'

        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]

        #---------------------------#
        # Setup 020 加载需要的角色和道具类的render参考
        #---------------------------#
        # 导入reference及share nodes（新导入场景，后导入参考）
        self.sk_FLRefRebuild(refInfos,noNeedRefNodeInfo)

        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机
        sk_hbExportCam.sk_hbExportCam().camServerReference(shotType)

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
            print(u'=====================请通知前期检测anim和render版本cache list=====================')
            mc.error(u'=====================请通知前期检测anim和render版本cache list=====================')

        # 清理blend
        self.checkCacheCleanBlendShapes()

        #---------------------------#
        # Setup 024 import cache
        # 1.备份材质，zwcache合并cache节点应用会出现线框模式，后面会还原材质。还原点很关键，否则会出现线框模式。
        # 2.载入cache，同时把K组导致的显示隐藏信息还原
        # 3.显示层物体还原
        #---------------------------#
        # 强行备份材质
        if cacheObjs:
            MatLists = self.checkCacheRecordMaterial(cacheObjs,finalLayout = 1 ,shotType = shotType)

        # 场景搭建完毕
        # 载入anim
        self.checkAnimCurveInfoImport(serverFile = 1 , shotType= shotType)

        print u'\n'
        print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
        print u'\n'
        # 处理buging

        # 载入cache及自带的anim
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            self.checkCacheSetCacheImport(cacheObjs, server ,shotType , resetPosition)
            # 处理还原物体
            if resetPosition:
                self.checkCacheResetPositionImport(server,shotType)
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
            self.checkCacheReturnMaterial(MatLists,finalLayout = 1, shotType = shotType)

        # 烘焙表情贴图
        self.checkCacheBakeTexAniFiles()

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
            if shotType == 2:
                camName = 'CAM:cam_' + shotInfos[1] + '_' + shotInfos[2] + '_baked'
            if shotType == 3:
                camName = 'CAM:cam_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_baked'
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
        # 2012版本后,shaderReset清理ref编辑历史后会变成线框
        #---------------------------#
        mc.file(save=1, force = 1)
        # 重打开FL文件
        #mc.file(localFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        # 处理cache环境变量
        self.checkCacheEnvPath()

        # 处理贴图动画
        self.sk_checkTextureAnimationImport(server)


        # 导入显示隐藏信息,必须放这，不然会被帧初始化干掉时间轴
        self.checkCacheVStateImport(shotType)

        mc.file(save=1, force = 1)

        #---------------------------#
        # Setup 030 本地备份之后，check in
        #---------------------------#
        # 上传服务器处理
        if server == 1:
            #self.checkFinalLayoutUpdate()
            # 开始提交文件至服务器
            mc.file(save=1,force = 1)
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            newShotInfo=''
            if shotType == 2:
                newShotInfo = newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4]
            if shotType == 3:
                newShotInfo = newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '_' + newInfo[5]
            fileInfo = '1|' + projectInfo + '|' + newShotInfo + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            mel.eval(checkOutCmd)
            # checkIn
            mel.eval('idmtProject -checkin -description \" ' + description + '\"')

        # 缺少check in baseFile
        print '\n'
        print(u'=========================================================================')
        if shotType == 2:
            print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))
        if shotType == 3:
            print(u'=====================【%s_%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2],shotInfos[3]))
        # 成功代码
        return 0
        
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【辅助】【FL文件 ReferenceEdit还原】
    #------------------------------#

    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info , shotType = 2):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath(shotType) 
        if shotType == 2:
            needInfo = info[0] + '_' + info[1] + '_' + info[2]
        if shotType == 3:
            needInfo = info[0] + '_' + info[1] + '_' + info[2] + '_' + info[3]
        needFsFile = needFilePath + needInfo + fileGrpType + fileFomat
        
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
    def checkFinalLayoutUpdate(self,shotType):
        # 获取cacheSet物体
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            # 上传服务器
            self.checkCacheLocalUpdate(shotType)
            #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
            print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
        # 最后保存
        mc.file(save=1)

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【拆分】【重新输出数据】【后台】
    #------------------------------#

    # 重新输出数据
    def checkFinalLayoutExport(self, grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1 , cachePre = -50 , shotType = 2 , resetPosition = 0):
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
                self.sk_checkBakeConstraints()

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
                self.sk_sceneGRPDelete('SET',shotType)
                self.sk_sceneGRPDelete('OTC',shotType)
                # 导出SET_GRP和OTC_GRP文件
                self.sk_sceneGRPExport('SET',1,shotType)
                self.sk_sceneGRPExport('OTC',1,shotType)
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
                
                # 新建文件之前处理好SET_GRP文件
                if shotType == 2:
                    needInfo = [shotInfos[0],shotInfos[1],shotInfos[2]]
                if shotType == 3:
                    needInfo = [shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3]]
                self.sk_sceneSETRefShaderReset(needInfo , shotType)
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
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
                print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')

            # 输出cache 及 anim
            if animExport:
                # 输出anim
                animObjs = self.checkAnimSetObjects()
                self.checkAnimCurveInfoExport(animObjs, serverFile = server , shotType = shotType)
                #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【输出】完毕=====================')

            # 输出cache
            if cacheExport:
                # 需要加入250分割处理
                # checkCacheSetObjects
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    self.checkCacheVStateExport(cacheObjs,shotType,server)
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    self.checkCacheSetCacheExport(cacheObjs, serverFile = server ,cachePre = cachePre , refMode = 1 , createType = 0 , shotType = shotType ,resetPosition = resetPosition)
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
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
                print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')

            # 成功代码
            return 0

    #------------------------------#
    # 【拆分】【重新导入数据】【后台】
    #------------------------------#

    # 重新载入数据
    def checkFinalLayoutImport(self, grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 ,server = 1,shotType = 2,resetPosition = 0):
        if grpImport or cacheImport or animImport or assetInfoImport or hideInfoImport:
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            import os
            
            # info记录
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # 处理大组
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(server)
            
            # 获取references信息
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # 首先处理好时间轴
            # FPS
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS',shotType)
            # frame
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType)
            
            #导入SET和OTC
            if grpImport:
                # 清除SET_GRP和OTC的参考
                # 目前通过namespace获取物体判断是否在两个组内
                refNode = refInfos[0][0]
                #refPathInfo = refInfos[1][0]
                refNsInfo = refInfos[2][0]
                for i in range(len(refNsInfo)):
                    mc.namespace(setNamespace = (  ':' + refNsInfo[i]))
                    objs = mc.namespaceInfo(ls= 1,dagPath =1 )
                    mc.namespace(setNamespace = ':')
                    if objs:
                        needObj = ''
                        for obj in objs:
                            if obj[-1] == '_' and mc.listRelatives(obj, s= 1 ,ni = 1,type = 'mesh'):
                                needObj = obj
                                break
                        if needObj:
                            objLong = mc.ls(needObj,l=1)[0]
                            # 判断是否在两个组
                            if 'SET_GRP' in objLong or 'OTC_GRP' in objLong:
                                print objLong
                                print refNode[i]
                                # 执行删除参考
                                mc.file(rfn = refNode[i] , removeReference = 1)
                    print(u'=====================【Group】【原参考】【清理】完毕=====================')
                # 删除SET_GRP和OTC_GRP
                if mc.ls('SET_GRP'):
                    mc.delete('SET_GRP')
                if mc.ls('OTC_GRP'):
                    mc.delete('OTC_GRP')
                # 导回SET_GRP和OTC_GRP
                self.sk_sceneGRPImport('SET',shotType)
                self.sk_sceneGRPImport('OTC',shotType)
                print(u'=====================【Group】【服务器端】【导入】完毕=====================')
            
            # 创建asset
            if assetInfoImport:
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                if os.path.exists(assetNeedServerPath +  'assetReference.txt'):
                    assetNeedOutputInfo = self.checkFileRead((assetNeedServerPath +  'assetReference.txt'))
                    if assetNeedOutputInfo:
                        for i in range(len(assetNeedOutputInfo)/2):
                            newPath = assetNeedOutputInfo[i*2]
                            ns = assetNeedOutputInfo[i*2 + 1]
                            mc.file(newPath, r=1, namespace= ns , referenceNode = (ns + 'RN') )
                            print u'\n'
                            print(u'=====================【创建参考】【%s】=====================' % (ns))
                            print u'\n'
                else:
                    print u'\n'
                    print(u'=====================【server缺少】【%s】请重新【输出】=====================' % ('assetInfo'))
                    print u'\n'
                
            # 载入anim
            if animImport:
                #animObjs = self.checkAnimSetObjects()
                self.checkAnimCurveInfoImport(serverFile = server , shotType = shotType)
                #print(unicode('=====================【Anim】【服务器端】【导入】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【导入】完毕=====================')

            # 输入cache
            if cacheImport:
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    #self.checkCacheSetCacheImport(cacheObjs, server)
                    self.sk_flCacheImportRefreshShaders(server , shotType )
                    # 导入显示隐藏信息
                    self.checkCacheVStateImport(shotType = shotType)
                    # 处理cache环境变量
                    self.checkCacheEnvPath()
                    #print(unicode('=====================【Cache】【服务器端】【导入】完毕=====================', "utf8"))
                    print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                else:
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    
            # 载入hideInfo
            if hideInfoImport :
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                unDisplayLayerObjs = self.checkFileRead((hideObjsServerPath +  'shotHideObjs.txt'))
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
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【核心】cacheSet自动创建
    #0.仅在model,rig,texture通用
    #1.含创建、更新cacheSet
    #Author  : 沈  康
    #Data    : 2013_05_16
    #------------------------------#
    
    # 获取标记nodes    #同一物体，_ca_与_an_无法共存;_si_与_nr_
    def checkGetSignNodes(self, sign, noNeed):
        nodes = mc.ls(type='transform')
        signNodes = []
        for node in nodes:
            # 排除非nurbs及mesh类
            shape = mc.listRelatives(node, s=1,f=1)
            if shape:
                nodeType = mc.nodeType(shape[0])
                if nodeType == 'mesh' or nodeType == 'nurbsCurve':
                    # 全部小写处理
                    transNode = node.lower()
                    # transNode = node
                    if noNeed:
                        if sign in transNode and noNeed not in transNode:
                            signNodes.append(node)
                    else:
                        if sign in transNode:
                            signNodes.append(node)
        return signNodes
    
    #------------------------------#

    # 创建标准cacheSet
    def checkCacheSetCreate(self):
        if mc.objExists('CACHE_OBJS'):
            pass
        else:
            mc.createNode('objectSet', n='CACHE_OBJS')
        if mc.objExists('MESHES'):
            pass
        else:
            mc.createNode('objectSet', n='MESHES')
            mc.sets('MESHES', e=1, addElement='CACHE_OBJS')
        # 必须前面是指定物体，后面是set名
        #mc.sets(cl='MESHES')
        
    #------------------------------#
    
    # 创建标准AnimSet
    def checkTransAnimSetCreate(self):
        if mc.objExists('TRANSANIM_OBJS'):
            pass
        else:
            mc.createNode('objectSet', n='TRANSANIM_OBJS')
        if mc.objExists('CTRLS'):
            pass
        else:
            mc.createNode('objectSet', n='CTRLS')
            mc.sets('CTRLS', e=1, addElement='TRANSANIM_OBJS')
        #mc.sets(cl='CTRLS')

    #------------------------------#
    # 【辅助】cacheSet更新重建
    #------------------------------#
    
    # 更新CacheSet列表
    def checkCacheSetAdd(self):
        self.checkCacheSetCreate()
        mc.sets(cl='MESHES')
        self.checkTransAnimSetCreate()
        nodes = self.checkGetSignNodes('_ca_', '_ct_an')
        needNodes = []
        if nodes:
            # 再处理mesh判断
            for node in nodes:
                # 首先确保在MODEL组下
                if '|MODEL|' in mc.ls(node,l=1)[0]:
                    if node[-1] == '_':
                        needNodes.append(node)
                    shape = mc.listRelatives(node, s=1,ni = 1, type='mesh')
                    if shape:
                        if node not in needNodes:
                            needNodes.append(node)
            if needNodes:
                mc.sets(needNodes , e=1 , addElement='MESHES')
            print u'---'
        print (u'CacheList    ' + str(len(needNodes)))
        #else:
            #print(unicode('=====================【没有发现_ca_标记的物体】=====================', "utf8"))
        #    print(u'=====================【没有发现_ca_标记的物体】=====================')

    #------------------------------#
    # 【辅助】animSet更新重建
    #------------------------------#

    # 更新AnimSet列表 ，这个不会在mo阶段处理
    def checkTransAnimSetAdd(self):
        self.checkCacheSetCreate()
        self.checkTransAnimSetCreate()
        mc.sets(cl='CTRLS')
        #nodes = self.checkGetSignNodes('_ct_an', '_ca_')
        nodes = mc.ls('*_ct_an*',type = 'transform')
        if nodes:
            needNodes = []
            # 支持组传递信息，可以考虑隐藏hide组,控制器 的显示|隐藏 约束 隐藏专用grp
            for node in nodes:
                if '|MODEL|' in mc.ls(node,l=1)[0] and node[-1] != '_':
                    if '_nr_' not in node and '_si_' not in node and '_proxy_' not in node and '_ca_' not in node:
                        needNodes.append(node)
            if needNodes:
                mc.sets(needNodes , e=1 , addElement='CTRLS')
            print (u'AnimList    ' + str(len(needNodes)))
        #else:
            #print(unicode('=====================【没有发现_ct_an标记的物体】=====================', "utf8"))
        #    print(u'=====================【没有发现_ct_an标记的物体】=====================')

    #------------------------------#
    # 【核心】前期文件set合并处理
    # 支持：cacheSet,animSet,Proxy_Set
    #------------------------------#

    # cacheSet,animSet,Proxy_Set合并处理
    # 获取所有MESHES或CTRLS级别的objectSet，甄别出非正版的"CacheSetx"或"AnimSetx"，将盗版物体绑架到正版Set去
    def checkCacheAnimSetCombine(self, setType, proType = ''):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        checkReal = 0
        keyWords = ''
        # proType_A= ['Calimero']
        # 设置正版smoothSet名字
        if setType == 'Cache':
            keyWords = 'MESHES'
        if setType == 'Anim':
            keyWords = 'CTRLS'
        if setType == 'Proxy':
            keyWords = 'Proxy_Set'
        for temp in tempSet:
            # 判断正版在不在
            if temp == keyWords:
                checkReal = 1
            # 获取盗版Set
            if keyWords in temp and temp != keyWords:
                objsSet.append(temp)
        if checkReal:
            if objsSet:
                for objSet in objsSet:
                    # 获取盗版mesh
                    meshes = mc.sets(objSet, q=1)
                    if meshes:
                        mc.sets(meshes , e=1 , addElement=keyWords)
                    try:
                        # 对于参考，pass
                        mc.delete(objSet)
                    except:
                        pass
        else:
            print u'=========未发现有效的[%s]Set组========='%setType

    #------------------------------#
    # 【辅助】【获取场景中所有cacheSet的物体】
    #------------------------------#   
    # 获取场景中所有cacheSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkCacheSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsCache = [] 
        for temp in tempSet:
            if 'MESHES' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    for mesh in meshes:
                        # 排除otc信息
                        if otcGrp == 1:
                            if '|OTC_GRP|' in mc.ls(mesh,l=1)[0] or '|SET_GRP|' in mc.ls(mesh,l=1)[0] or mc.ls(mesh,l=1)[0].split('|')[-1][3] in ['s', 'S']:
                                pass
                            else:
                                # 不要长名，为shareNodes做准备
                                objsCache.append(mc.ls((mesh), l=0)[0])
                        else:
                            objsCache.append(mc.ls((mesh), l=0)[0])
        if objsCache:
            print (u'[Cache Object]    ' + str(len(objsCache)))
        else:
            print (u'[Cache Object]    0')
        return objsCache
                
    #------------------------------#
    # 【辅助】【获取场景中所有AnimSet的物体】
    #------------------------------#   
    # 获取场景中所有AnimSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkAnimSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsAnim = []
        for temp in tempSet:
            if 'CTRLS' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                ctrls = mc.sets(objSet, q=1)
                if ctrls:
                    for ctrl in ctrls:
                        # 排除otc组信息
                        if otcGrp == 1:
                            if 'OTC_GRP' not in mc.ls(ctrl,l=1)[0] and 'SET_GRP' not in mc.ls(ctrl,l=1)[0]:
                                print ctrl
                                objsAnim.append(ctrl)
        if objsAnim:
            print (u'[Anim  Object]    ' + str(len(objsAnim)))
        else:
            print (u'[Anim  Object]    0')
        return objsAnim
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【核心】【检测v属性】
    #  用途：将时间轴内因隐藏大组出现的显示|隐藏记录
    #      FL环节还原cache物体显示|隐藏动画
    #  Author  : 沈  康
    #  Data    : 2014_02_10
    #------------------------------#
    # 核心检测物体
    def checkObjVState(self,checkObj):
        # 物体不存在则返回0
        if not mc.objExists(checkObj):
            return 0
        # 物体v属性是否存在
        if not mc.attributeQuery('visibility',node = checkObj , exists = 1):
            return 0
        result = mc.getAttr(checkObj +'.visibility')
        # intermediate mesh
        if mc.attributeQuery('intermediateObject',node = checkObj , exists = 1):
            checkValue = mc.getAttr(checkObj + '.intermediateObject')
            result = result and (not checkValue)
        # displayLayer
        if mc.attributeQuery('overrideEnabled',node = checkObj , exists = 1) and mc.getAttr(checkObj + '.overrideEnabled'):
            checkValue = mc.getAttr(checkObj + '.overrideVisibility')
            result = result and checkValue
        # 层级
        if result:
            parentNodes = mc.listRelatives(checkObj,p = 1 ,f = 1 )
            if parentNodes:
                result = result and self.checkObjVState(parentNodes[0])
                
        return result
    
    #------------------------------#
    # 处理数据，并输出
    def checkCacheVStateExport(self , cacheObjs , shotType = 2 ,server = 1):
        if cacheObjs:
            # 获取时间轴
            startFrame  =   mc.playbackOptions(min=1,q = 1)
            endFrame    =   mc.playbackOptions(max=1,q = 1)
            # 数据创建
            vData = dict()
            for checkObj in cacheObjs:
                vData[checkObj] = []
            # 即时更新
            for i in range(int(endFrame - startFrame + 1)):
                frameNow = int(startFrame + i)
                mc.currentTime(frameNow)
                for checkObj in cacheObjs:
                    # 处理vState
                    vState = self.checkObjVState(checkObj)
                    if vState:
                        needInfo = [1 , frameNow]
                    else:
                        needInfo = [0 , frameNow]
                    # 处理记录与否
                    if vData[checkObj] == []:
                        vData[checkObj].append(needInfo)
                    else:
                        # 不同的数据则记录
                        if vData[checkObj][-1][0] != vState:
                            vData[checkObj].append(needInfo)
            # 进一步处理数据,处理成list
            resultData = []
            for checkObj in cacheObjs:
                resultData.append([checkObj,vData[checkObj]])
            if server:
                # 输出服务器端
                ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
                self.checkFileWrite((ObjsVDataServerPath +  'cacheObjVInfo.txt'), resultData)
            else:
                # 输出本地
                ObjsVDataLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
                self.checkFileWrite((ObjsVDataLocalPath +  'cacheObjVInfo.txt'), resultData)
            return  resultData
        
    #------------------------------#
    # v信息导入
    def checkCacheVStateImport(self , shotType = 2):
        vData = self.checkObjsVData(shotType)
        if vData:
            cacheObjs = vData.keys()
            for cacheObj in cacheObjs:
                keyInfo = vData[cacheObj]
                #print '-----'
                #print len(keyInfo)
                #print keyInfo
                # 单帧
                if len(keyInfo) == 1:
                    try:
                        vState = keyInfo[0][0]
                        mc.setAttr((cacheObj + '.v'),vState)
                    except:
                        pass
                # 多帧
                else:
                    for i in range(len(keyInfo)):
                        vState = keyInfo[i][0]
                        frame = keyInfo[i][1]
                        #print vState
                        #print frame
                        mc.currentTime(frame)
                        mc.setAttr((cacheObj + '.v'),vState)
                        mc.setKeyframe((cacheObj + '.v'))

    #------------------------------#
    # vData数据结构处理
    def checkObjsVData(self, shotType = 2):
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        resultData = self.checkFileRead(ObjsVDataServerPath +  'cacheObjVInfo.txt')
        vData = dict()
        import os
        if os.path.exists(ObjsVDataServerPath +  'cacheObjVInfo.txt'):
            for lineInfo in resultData:
                # obj
                obj = lineInfo.split(', ')[0][3:-1]
                vData[obj] = []
                # frameList
                frameList = lineInfo.split('\', ')[-1]
                # 单帧情况
                if '], ' not in frameList:
                    frameInfo = frameList.split(', ')
                    vState = frameInfo[0][2:]
                    frame = frameInfo[-1][:-3]
                    vData[obj].append([int(vState),int(frame)])
                # 多帧情况
                else:
                    allInfos = frameList.split('], ')
                    needInfo = []
                    for i in range(len(allInfos)):
                        frameInfo = allInfos[i].split(', ')
                        vState = frameInfo[0][1:]
                        frame = frameInfo[-1][:]
                        if i == 0:
                            vState = frameInfo[0][2:]
                        if i == (len(allInfos) - 1):
                            frame = frameInfo[-1][:-3]
                        needInfo.append([int(vState),int(frame)])
                    vData[obj] = needInfo
        return vData
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【通用】【清理工具系列】
    #  0.阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_05_16
    #------------------------------#
    # 清理displayLayer
    def checkCleanDisplayLayers(self,layers = [],donotLayers = []):
        if layers == []:
            layers = mc.listConnections('layerManager.displayLayerId')
        errorDelete = []
        if layers:
            for layer in layers:
                if 'defaultLayer' not in layer:
                    # 判断是否参考
                    refInfo = mc.referenceQuery(layer, isNodeReferenced=1)
                    if refInfo:
                        mc.warning(u'============【参考层】【%s】无法清理============' % (layer))
                    else:
                        # 断开layerManager和其连接再删除
                        layerManager = mc.connectionInfo( (layer + '.identification'),sourceFromDestination = 1)
                        if layerManager:
                            if 'layerManager' in layerManager:
                                mc.disconnectAttr(layerManager,(layer + '.identification'))
                        # 断开输出链接
                        outputs = mc.connectionInfo( (layer + '.drawInfo'),destinationFromSource = 1)
                        if outputs:
                            for out in outputs:
                                mc.disconnectAttr((layer + '.drawInfo'),out)
            for layer in layers:
                if 'defaultLayer' not in layer:
                    if donotLayers:
                        if layer not in donotLayers:
                            mc.delete(layer)
                    else:
                        mc.delete(layer)
        return errorDelete
    
    #------------------------------#
    # 清理renderLayer
    def checkCleanRenderLayers(self):
        # 回到masterLayer
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        layers = mc.ls(type='renderLayer')
        layers.remove('defaultRenderLayer')
        errorDelete = []
        if layers:
            for layer in layers:
                try:
                    cmd = 'renderLayerEditorDeleteLayer RenderLayerTab ' + layer
                    mel.eval(cmd)
                except:
                    pass
                if mc.objExists(layer):
                    try:
                        mc.delete(layer)
                    except:
                        mc.warning(u'========================【%s】删除失败========================' % (layer))
                        pass
        return errorDelete

    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【核心】【经典Cache函数集】
    #  0.仅在rig,texture及finallayout阶段使用
    #  1.需要添加log，以及加快效率
    #  Author  : 沈  康
    #  Data    : 2013_05_20
    #------------------------------#
    

    #------------------------------#
    # 【总篇】【经典Cache 本地|服务器端  创建导出】
    #  0.通用
    #  Author  : 沈  康
    #  Data    : 2013_05_28
    #------------------------------#
    # 传递v显示的动画，OK！！！
    # cache，需要开通GeoCache删写权限
    # 处理的分割情况，遵循一个asset输出一套cache
    # 加入上传服务器功能
    # objsCache     用于输出cache的物体
    # serverFile    服务器端输出
    # cachePre      预算范围，给特效用;默认是前后5帧，给动态模糊做预留
    # refMode       是否一个参考一个cache
    # createType    创建模式，只输出cache不连接还是输出cache并连接
    # shotType      镜头类型，2位定位还是3位定位
    # resetPosition 回归原点输出
    def checkCacheSetCacheExport(self, objsCache, serverFile = 1 ,cachePre = 0 , refMode = 1 ,createType = 1 ,shotType = 2 , resetPosition = 0 ):
        if not objsCache:
            return 0
        
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 51, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'

        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        # server_animPath___python用转mel
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
 

        # 清理历史文件
        oldFiles = mc.getFileList(folder=localPathCache)
        for of in oldFiles:
            if of not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in of:
                mc.sysFile((localPathCache + of), delete=1)

        # 获取cache物体
        # objsCache = self.checkCacheSetObjects()

        # 备份显示隐藏动画
        animVObjs = []
        hideObjs = []
        for obj in objsCache:
            animCurve = mc.listConnections((obj + '.v'), s=1, d=0)
            if animCurve:
                animVObjs.append(obj)
            else:
                if mc.getAttr(obj + '.v') != True:
                    hideObjs.append(obj)
                    
        # 先处理有动画的
        if animVObjs:
            self.checkAnimCurveInfoExport(animVObjs, serverFile = serverFile , infoFile = 'ca_animV' , shotType = shotType )
        else:
            # 输出空信息
            self.checkAnimCurveInfoExport([], serverFile = serverFile , infoFile = 'ca_animV' , shotType = shotType )
        # 处理自身隐藏的
        if hideObjs:
            self.checkAnimCurveInfoExport(hideObjs, serverFile = serverFile , infoFile = 'ca_hideV', shotType = shotType)
        else:
            # 输出空信息
            self.checkAnimCurveInfoExport([], serverFile = serverFile , infoFile = 'ca_hideV', shotType = shotType)
            
        
        # cachePath
        if serverFile:
            cachePath = serverPathCache
        else:
            cachePath = localPathCache
        
        # 清理目录内文件
        # 只清理txt和cache
        files = mc.getFileList(folder = cachePath , filespec = '*.mc') + mc.getFileList(folder = cachePath , filespec = '*.xml') + mc.getFileList(folder = cachePath , filespec = '*.txt')
        if files:
            for one in files:
                if one not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in one:
                    mc.sysFile( ( cachePath + one ) , delete = 1)
        print '\n'
        print u'=====================历史文件清理完毕====================='
        print '\n'
            
        # 备份材质
        #MatLists = self.checkCacheRecordMaterial()
        
        # 获取namespace信息
        needCacheObjs = dict()
        for obj in objsCache:
            nsInfo = needCacheObjs.keys()
            ns = obj.split(':')[0]
            if nsInfo == []:
                if ns:
                    needCacheObjs[ns] = [obj]
            else:
                if ns in nsInfo:
                    needCacheObjs[ns].append(obj)
                else:
                    needCacheObjs[ns] = [obj]
        nsInfo = needCacheObjs.keys()
        
        # 回归原点处理
        if resetPosition:
            self.checkCacheResetPositionExport(nsInfo , serverFile , shotType)

        # 经典版本cache处理
        mc.select(objsCache)
        # 删除已有的cache
        try:
            mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
        except:
            pass
        mc.select(cl=1)

        # 经典版本cache处理
        print '\n'
        print u'=====================【cache】【经典模式】【开始创建】====================='
        print '\n'
        
        # 执行缓存创建
        if refMode == 0:
            lenObjs = len(objsCache)
            splitStep = 250
            if lenObjs > splitStep:
                objTemp = []
                if lenObjs % splitStep == 0:
                    grpNum = lenObjs / splitStep
                else:
                    grpNum = lenObjs / splitStep + 1
                for i in range(grpNum):
                    # 判断最后一位的范围
                    if i == (grpNum - 1):
                        objTemp = objsCache[i * splitStep:]
                    else:
                        objTemp = objsCache[i * splitStep : (i + 1) * splitStep]
                    self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath , createType , cachePre )
                    # 输出分段物体信息
                    objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                    self.checkFileWrite(objPath, objTemp)
                # 输出分段信息
                cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                self.checkFileWrite(cacheIndexPath, [str(grpNum)])
            else:
                self.checkCacheDoCreate((fileName + '_0'), objsCache, cachePath , createType , cachePre)
                # 输出分段物体信息
                objPath = cachePath + 'cache_objs_0.txt'
                self.checkFileWrite(objPath, objsCache )
                # 输出分段信息
                cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                self.checkFileWrite(cacheIndexPath, '0')
        
        # 按namespace处理
        if refMode == 1 and nsInfo:
            for i in range(len(nsInfo)):
                ns = nsInfo[i]
                objTemp = needCacheObjs[ns]
                print u'-------------------------'
                print u'处理cache[%s]ing'%ns
                # 创建cache
                self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath, createType , cachePre)
                # 输出分段物体信息
                objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                self.checkFileWrite(objPath, objTemp)
                print u'处理cache[%s]完毕！'%ns
            # 输出分段信息 , 不加[]给str(len(nsInfo))，会把str(len(nsInfo))处理成list，每个单位一个字符,如16为1,6
            cacheIndexPath = cachePath + 'cache_objsIndex.txt'
            self.checkFileWrite(cacheIndexPath, [str(len(nsInfo))])
        
        # 公用cache
        mel.eval('zwOptimizeGeoCache();')

        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)
        
        # 还原材质
        #self.checkCacheReturnMaterial(MatLists,finalLayout = 1, shotType = shotType)
        
        # 烘焙表情贴图
        #self.checkCacheBakeTexAniFiles()
        
        
        # 上传cache及animPath
        #if serverFile == 1:
        #    self.checkCacheLocalUpdate()

    #-----------------------------#
    # abc 导出
    def checkAbcCacheExport(self,objsCache, server = 1,exportType = 'mesh' ,cachePre = 0 ,step = 1 ):
        if not objsCache:
            return
        nsObjs = {}
        for checkObj in objsCache:
            ns = checkObj.split('|')[-1].split(':')[0]
            if ns not in nsObjs.keys():
                nsObjs[ns] = [checkObj]
            else:
                nsObjs[ns].append(checkObj)

        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)

        shotID = sk_infoConfig.sk_infoConfig().checkShotID()

        localPath  = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 2)
        serverPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 2)
        fileList = []
        for ns in nsObjs.keys():
            needObjs = nsObjs[ns]
            mc.select(needObjs)
            exportInfo = exportType
            if exportType in ['mesh']:
                exportInfo = 'alembic'
            # file
            abcFile = '%s_%s.abc'%(ns,exportInfo)
            abcFile = '%s_%s_%s.abc'%(shotID,ns,exportInfo)
            abcLocalPath = localPath + abcFile
            rootObjs = ''
            for obj in needObjs:
                rootObjs = rootObjs + ' -root ' + mc.ls(obj,l=1)[0]
            cacheCMD = 'AbcExport -verbose -j \"-frameRange ' + str(frameStart+cachePre)  + ' ' + str(frameEnd) + ' -step ' + str(step) + ' -uvWrite -worldSpace -writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath + '\"'
            mel.eval(cacheCMD)
            fileList.append([(localPath + abcFile),(serverPath + abcFile)])
        if server:
            for info in fileList:
                sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',info[0],info[1])

    #------------------------------#
    # 【总篇】【经典Cache 本地|服务器端  导入】
    #------------------------------#
    # 导入cache，还原V动画，yes!
    # 需要细看共享节点
    # 增加从服务器读取功能
    def checkCacheSetCacheImport(self, objsCache, serverFile = 1 , shotType = 2,resetPosition = 0):      
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 5, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'
        
        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # server端path
        if serverFile == 1:
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            localPathCache = serverPathCache
        
        if objsCache:
            # 备份材质
            MatLists = self.checkCacheRecordMaterial()
            
            # 经典版本cache处理
            # 删除已有的cache
            try:
                mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            except:
                pass
            
            # 导入cache
            # 查看分段信息
            cacheIndexPath = localPathCache + 'cache_objsIndex.txt'
            splitInfo = self.checkFileRead(cacheIndexPath)
            splitNum = int(splitInfo[0])
            if splitNum == 0:
                mc.select(cl=1)
                mc.select(objsCache)
                localCacheFile = localPathCache + fileName + '_0' + '.xml'
                melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                mel.eval(melCacheCMD)
                mc.select(cl=1)
            else:
                mc.select(cl=1)
                for num in range(splitNum):
                    cacheObjsPath = localPathCache + 'cache_objs_' + str(num) + '.txt'
                    objs = self.checkFileRead(cacheObjsPath)
                    mc.select(objs)
                    localCacheFile = localPathCache + fileName + '_' + str(num) + '.xml'
                    melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                    mel.eval(melCacheCMD)
                    mc.select(cl=1)

            # 还原v状态
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'ca_hideV' , shotType = shotType)
            except:
                pass
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'ca_animV', shotType = shotType)
            except:
                pass

            # 公用cache
            mel.eval('zwOptimizeGeoCache();')
            
            # 控制器还原属性
            try:
                self.checkAnimCurveInfoImport(serverFile = serverFile, infoFile = 'moveInfo' , shotType = shotType)
            except:
                pass

            # 打断所有连接
            #mel.eval('eyRenderRehyperShade')
  
            # 还原材质
            self.checkCacheReturnMaterial(MatLists,finalLayout = serverFile, shotType = shotType)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()

            # 上传cache
            
        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)

    #------------------------------#
    # 【核心】回到原点cache处理，导出信息
    #------------------------------#
    def checkCacheResetPositionExport(self,nsInfo = [],serverFile = 1, shotType = 2):
        # 回归原点处理
        defaultCtrls = ['Master','Character','WORLD','World','Move','move_ctrl']
        needCtrls = []
        if nsInfo:
            # 搜集控制器
            for ns in nsInfo:
                for key in defaultCtrls:
                    if mc.ls(ns + ':' + key):
                        needCtrls.append(ns + ':' + key)
            if not needCtrls:
                return 0
            # 找到核心最内环
            insideCtrls = []
            for ns in nsInfo:
                nsCtrls = []
                for ctrl in needCtrls:
                    if ns in ctrl:
                        nsCtrls.append(ctrl)
                nsPathCtrls = mc.ls(nsCtrls,l = 1)
                nsDepthPath = []
                if not nsPathCtrls:
                    continue
                for ctrl in nsPathCtrls:
                    nsDepthPath.append(len(ctrl.split('|')))
                insideCtrls.append(nsCtrls[nsDepthPath.index(max(nsDepthPath))])
            
            # locator处理
            finalCtrls = []
            if insideCtrls:
                # 配置loc
                for ctrl in insideCtrls:
                    ns = ctrl.split(':')[0]
                    nsLoc = ns + ':Move_Loc'
                    if mc.ls(nsLoc):
                        mc.delete(nsLoc)
                    mc.spaceLocator(name = nsLoc)
                    mc.parentConstraint(ctrl ,nsLoc )
                    finalCtrls.append(nsLoc)
                # bake loc
                frameStart = mc.playbackOptions(q=1, min=1) 
                frameEnd = mc.playbackOptions(q=1, max=1) 
                mc.bakeResults(finalCtrls, t=(frameStart, frameEnd),
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
            # 输出
            if finalCtrls:
                self.checkAnimCurveInfoExport(finalCtrls, serverFile = serverFile, infoFile = 'moveInfo',shotType = shotType)
                # 还原原点
                for ctrl in needCtrls:
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    for i in range(len(attrs)):
                        attr = attrs[i]
                        connectAttr = mc.listConnections(( ctrl + attr), s=1,plugs=1)
                        if connectAttr:
                            mc.disconnectAttr(('%s') % (connectAttr[0]), ('%s') % (ctrl + attr))
                        mc.setAttr((ctrl + attr),0)
            else:
                self.checkAnimCurveInfoExport([], serverFile = serverFile, infoFile = 'moveInfo',shotType = shotType)

    #------------------------------#
    # 【核心】回到原点cache处理，导入信息
    #------------------------------#
    def checkCacheResetPositionImport(self,serverFile = 1, shotType = 2):
        # 读控制器
        infoFile = 'moveInfo'
        if serverFile:
            path = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
        else:
            path = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
        print '---'
        print (path + infoFile + '_objs.txt')
        needCtrls = sk_infoConfig.sk_infoConfig().checkFileRead(path + infoFile + '_objs.txt')
        #pathCtrls = sk_infoConfig.sk_infoConfig().checkFileRead(path + infoFile + '_Lobjs.txt')
        if not needCtrls:
            return 0
        # 创建控制器
        nsInfo = []
        rootCtrlGrp = 'Food_Temp_Ctrls'
        if mc.ls(rootCtrlGrp):
            mc.delete(rootCtrlGrp)
        mc.group(name = rootCtrlGrp,em = 1)
        for ctrl in needCtrls:
            if ':' in ctrl:
                nsInfo.append(ctrl.split(':')[0])
            if mc.ls(ctrl):
                mc.delete(ctrl)
            mc.circle(name = ctrl)
            mc.parent(ctrl,rootCtrlGrp)
        # 整理控制器
        ctrlInfo = []
        for i in range(len(nsInfo)):
            # namespace相关控制器
            ns = nsInfo[i]
            for ctrl in needCtrls:
                if ns in ctrl:
                    ctrlInfo.append(ctrl)
        # 传动画曲线
        self.checkAnimCurveInfoImport(serverFile=serverFile, infoFile='moveInfo' , replace = [] ,targetPath = '' , shotType = shotType)
        if not nsInfo:
            return 0
        # 给MODEL组K帧
        startFrame = mc.playbackOptions(min=1,q = 1)
        startFrame = startFrame - 5
        endFrame   = mc.playbackOptions(max=1,q = 1)
        endFrame   = endFrame + 5
        attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
        for frame in range(int(startFrame),int(endFrame+1)):
            mc.currentTime(frame)
            for j in range(len(nsInfo)):
                ns = nsInfo[j]
                nsctrl = ctrlInfo[j]
                if not nsctrl:
                    continue
                # 读属性写属性
                setObj = ns + ':' + 'MODEL'
                for attr in attrs:
                    value = mc.getAttr(nsctrl + attr)
                    mc.setAttr((setObj + attr),value)
                    mc.setKeyframe(setObj + attr)
        # 清理
        mc.delete(rootCtrlGrp)

    #------------------------------#
    # 【辅助】清理所有非参考非场景的blendShape
    #------------------------------#
    def checkCacheCleanBlendShapes(self):
        blendShapes = mc.ls(type = 'blendShape')
        blendPre = self.tempBlend
        temps = []
        for blend in blendShapes:
            isRef = mc.referenceQuery(blend, inr = 1)
            if isRef:
                continue
            if blendPre in blend:
                temps.append(blend)
        if temps:
            mc.delete(temps)

    #------------------------------#
    # 【核心】执行创建cache
    #------------------------------#
    def checkCacheDoCreate(self, fileName, objs, path , createType = 0 , cachePre = 0):
        # 标准设置
        cacheType = 'OneFilePerFrame'
        # cacheType = 'OneFile'
        cacheFormat = 'mcc'
        # 参数获取
        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        # 获取shape
        objsShape = []
        for obj in objs:
            # 需要进行甄别
            # 有输出的才有效；OG无效
            mesh = mc.listRelatives( obj ,pa=1,ni=1,s=1,type='mesh')
            if mesh:
                objsShape.append(mesh[0])
            
        # 本函数只创建，不连接
        if createType == 0:
            try:
                mc.cacheFile(f = fileName ,singleCache = 1,dir = path , st = (frameStart+cachePre) , et = frameEnd ,points = objsShape)
            except:
                pass
        # 创建并连接，比较慢
        if createType == 1:
            cacheType = 'OneFile'
            mc.select(objs)
            # doCreateGeometryCache 6 { "3", "1", "24", "OneFile", "1", "E:/TD_work/Data/test","0","","0", "add", "0", "1", "1","0","1","mcc","0" } ;
            # doCreateGeometryCache (版本号6) {(), (startFrame), (endFrame), (onFile), (), (path), (‘0‘),  (fileName) ,(‘0‘) ,('add'),(),('1'),('1'),('0').('1').('mcc'),'0'}
            # add后的参数为1时自动覆盖
            cacheCMD = 'doCreateGeometryCache 6 { "3", "%s", "%s", "%s", "1", "%s","0","%s","0", "add", "1", "1", "1","0","1","%s","0" }' % (str(frameStart+cachePre) , str(frameEnd) , cacheType, path , fileName , cacheFormat)
            mel.eval(cacheCMD)
            mc.select(cl = 1)
        
    #------------------------------#
    # 【辅助】cache分割。单一asset数量多处理
    #------------------------------#
    def checkCacheCreateConfig(self, fileName, objs, path , createType = 0,cachePre = 0):
        # textLogPath = path + 'geoCache_log.txt'
        # 255判断，进行250分割
        lenObjs = len(objs)
        step = 250
        if lenObjs > step:
            objTemp = []
            if lenObjs % step == 0:
                grpNum = lenObjs / step
            else:
                grpNum = lenObjs / step + 1
            for i in range(grpNum):
                if i < grpNum :
                    objTemp = objs[i * step : (i + 1) * step]
                else:
                    objTemp = objs[i * 250:]
                fileNameTemp = fileName + '_' + str(i)
                self.checkCacheDoCreate(fileNameTemp , objTemp , path , createType , cachePre)
        else:
            grpNum = 1
            self.checkCacheDoCreate(fileName , objs , path , createType , cachePre)

    #------------------------------#
    # 【辅助】【本地cache上传处理】
    #------------------------------#
    # 处理上传
    def checkCacheLocalUpdate(self,shotType):
        # 本地Cache及Anim路径
        # local_cachePath___mel用
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        # server_animPath___python用转mel
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
        # cache上传
        cacheInfos = mc.getFileList(folder=localPathCache)
        
        for cacheInfo in cacheInfos:
            fileInfo = cacheInfo
            updateCacheCMD = 'zwSysFile "copy" ' + '"' + (localPathCache + fileInfo) + '"' + ' ' + '"' + (serverPathCache + fileInfo) + '"' + ' true'
            mel.eval(updateCacheCMD)
            print u'===[Updating Cache To Server]===传输[%s]完毕==='%fileInfo
            
        # anim上传
        fileInfo = 'ca_animV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_animV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        
        print u'==============缓存及动画数据全部传输完毕=============='
    
    #------------------------------#
    # 【辅助】【备份材质】
    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0  ,shotType = 2):
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
                    meshsp = mc.listRelatives(obj,ni=1,type = 'mesh',s =1 ,f=True)
                    if meshsp:
                        mesh=meshsp[0]
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
            self.checkCacheRecordMaterialExport(MatLists,shotType)
        return MatLists
        
    #------------------------------#
    # 【辅助】【还原材质】
    #------------------------------#
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0,shotType = 2):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport(shotType)
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            print '=========还原材质======OBJS========='
            print objs

            # 必须加objs，不然会断掉
            if objs:
                try:
                    mc.sets(objs, forceElement = key)
                except:
                    pass
       
    #------------------------------#
    # 【辅助】【材质信息备份到服务器端】【拆分用】
    #------------------------------#        
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
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
            
    #------------------------------#
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#    
    # 输出材质信息
    def checkCacheRecordMaterialImport(self,shotType):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if shotType == 2:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        if shotType == 3:
            serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/'
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = self.checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = self.checkListSameAllIndex(allInfo,u'********')[0]
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

    #------------------------------#
    # 【辅助】【Bake表情贴图】
    #------------------------------#    
    # bake表情贴图
    def checkCacheBakeTexAniFiles(self):
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        files = mc.ls(type='file')
        for f in files:
            cons = mc.listConnections(f + '.frameExtension')
            if cons:
                mc.bakeResults(f + '.frameExtension', sb=1, t=(frameStart, frameEnd))

    #------------------------------#
    # 【辅助】【传递file动画】
    #------------------------------#
    # bake并导出动画信息
    def sk_checkTextureAnimationExport(self,server):
        # bake
        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        fileNodes = mc.ls(type = 'file')
        needNodes = []
        for checkNode in fileNodes:
            inr = mc.referenceQuery(checkNode,inr = 1)
            if not inr:
                continue
            checkAttr = checkNode + '.frameExtension'
            cons = mc.listConnections(checkAttr)
            if cons:
                mc.bakeResults(checkAttr, sb=1, t=(frameStart, frameEnd))
                needNodes.append(checkNode)
        # 导出
        if needNodes:
            ObjsVDataLocalPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 2)
            fileInfo = 'txAnimation'
            self.checkAnimCurveInfoExport(needNodes,infoFile = fileInfo,targetPath = ObjsVDataLocalPath)
            if server:
                ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 2)
                fileName = '%s.sla'%fileInfo
                runCmd = 'zwSysFile("copy","' + (ObjsVDataLocalPath + fileName ) + '","' + (ObjsVDataServerPath + fileName) + '",1)'
                mel.eval(runCmd)
                print ObjsVDataServerPath + fileName
                fileName = '%s_objs.txt'%fileInfo
                runCmd = 'zwSysFile("copy","' + (ObjsVDataLocalPath + fileName ) + '","' + (ObjsVDataServerPath + fileName) + '",1)'
                mel.eval(runCmd)
                print ObjsVDataServerPath + fileName
                print u'\n'
                print(u'=====================【txNodesAnimation】【服务器端】【输出】完毕=====================')
                print u'\n'

    # txFile动画导入
    def sk_checkTextureAnimationImport(self,server):
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 2)
        fileInfo = 'txAnimation'
        checkFileA = '%s%s.sla'%(ObjsVDataServerPath,fileInfo)
        checkFileB = '%s%s_objs.txt'%(ObjsVDataServerPath,fileInfo)
        if os.path.exists(checkFileA) and os.path.exists(checkFileB):
            self.checkAnimCurveInfoImport(infoFile = fileInfo,targetPath = ObjsVDataServerPath)
            print(u'=====================【txNodesAnimation】【还原】完毕=====================')

    #------------------------------#
    # 【辅助】【分拆用】FL文件更新cache
    #------------------------------#  
    # fl文件处理cache并保持更新材质
    def sk_flCacheImportRefreshShaders(self,server,shotType = 2):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            needIds = []
            for i in range(len(refNodes)):
                if 'CAM' not in refNodes[i]:
                    if refNodes[i].split('_')[1][0] in ['c','p']:
                        needIds.append(i)
            if needIds:
                # unload参考 ,cleanUp ,load参考
                for num in needIds:
                    mc.file(rfn=refNodes[num] , unloadReference=1)
                    mc.file(rfn=refNodes[num], cleanReference = refNodes[num])
                    mc.file(rfn=refNodes[num] , loadReference=1)
                # 导入cache
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    self.checkCacheSetCacheImport(cacheObjs, server,shotType)
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
                # 处理参考编辑列表
                for num in needIds:
                    mc.file(rfn=refNodes[num] , unloadReference=1)
                #  清理
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
                # load
                for num in needIds:
                    mc.file(rfn=refNodes[num] , loadReference=1)
                # 整理
                sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【辅助】【动画信息处理函数】
    # 0.动画通用
    # 1.动画曲线点问题修正
    # 2.动画曲线0清除
    # Author : 沈  康
    # Data   : 2013_03_01
    #------------------------------#   
    # 清理无用动画曲线，修正动画曲线问题
    def checkAnimCleanSingleKey(self):
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 删除单帧动画曲线
                keysNum = mc.keyframe(animC, query=True, keyframeCount=True)
                if keysNum == 3:
                    try:
                        # 清除动画曲线
                        mc.delete(animC)
                    except:
                        #mc.warning(unicode('=====================【错误】【单帧动画】【%s】 参考无法删除=====================') % (str(animC), "utf8"))
                        mc.warning(u'=====================【错误】【单帧动画】【%s】 参考无法删除=====================' % (animC))
                         
    #------------------------------#   
    # 判断静态动画
    def checkAnimNoneAnimationCurves(self):
        # 1.值不变
        # 每个点内的切线角度不为0
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 关键帧值
                keysValue = mc.keyframe(animC, query=True, vc=True)
                tempValue = list(set(keysValue))
                # 值相同判断
                if len(tempValue) == 1:
                    # 角度获取
                    # keyAngle = mc.keyTangent(animC, query =True, ia = 1,  oa = 1)
                    tempAngle = list(set(keysValue))
                    # 角度都为0打平判断
                    if len(tempAngle) == 1:
                        # 执行删除
                        mc.delete(animC)

    #------------------------------#   
    # 处理动画切线
    def checkAnimKeyTangentConfig(self):
        # 修正问题
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 曲线点数及时间
                # keysNum  = mc.keyframe( animC, query=True, keyframeCount=True )
                keysTime = mc.keyframe(animC, query=True, tc=True)
                # 切入和切出曲线类型
                inType_animKeys = mc.keyTangent(animC, query=True, itt=1)
                outType_animKeys = mc.keyTangent(animC, query=True, ott=1)
                # 合法切线类型
                types = ["spline", "linear" , "fast" , "slow" , "flat", "step", "stepnext", "fixed" , "clamped" , "plateau" , "auto"] 
                # 修正类型
                fiixType = 'auto'
                if inType_animKeys:
                    # 执行修正
                    for i in range(len(inType_animKeys)):
                        if inType_animKeys[i] not in types:
                            mc.selectKey(animC, k=1 , t=(keysTime[i], keysTime[i]))
                            mc.keyTangent(itt=fiixType)
                    for i in range(len(outType_animKeys)):
                        if outType_animKeys[i] not in types:
                            mc.selectKey(animC, k=1 , t=(keysTime[i], keysTime[i]))
                            mc.keyTangent(ott=fiixType)
                else:
                    mc.delete(animC)

    #------------------------------#   
    # 执行清理动画垃圾信息
    def checkAnimDoClean(self):
        # 清理单帧
        self.checkAnimCleanSingleKey()
        # 清理静止动画
        self.checkAnimNoneAnimationCurves()
        # 修正动画曲线问题
        self.checkAnimKeyTangentConfig()

    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【核心】【动画数据导入导出PYTHON版】
    # 0.动画
    # Author : 沈  康
    # 参考             : 万寿龙
    # Data   : 2013_05_24 - 2013_05_28
    #------------------------------#   
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = '' , shotType = 2):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.0   (Author: wanshoulong)')
        # 版本号
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';')
        # 单位类型
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        # 角度单位，弧度还是角度
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        # 制式，PAL等
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        # 获取objs
        if objs:
            for obj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(obj, k=1)
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(obj, cb=1)
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        if mc.objExists(obj + '.' + attr):
                            # 获取属性的动画曲线
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0])  
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(obj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if allAttr:
                                for attr in allAttr:
                                    animCurve = mc.listConnections((expShapes[0] + '.' + attr), type='animCurve', s=1, d=0)
                                    if animCurve:
                                        if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                            AnimsInfo.append('anim ' + expShapes[0] + '.' + attr + '\n{') 
                                            # 更新信息
                                            infoAll = (self.checkAnimCurveInfoGet(animCurve[0]))
                                            for info in infoAll:
                                                AnimsInfo.append(info)
                                            AnimsInfo.append('}')
                                    else:
                                        # 无动画的信息，不过对于点来说基本用不到
                                        if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :             
                                            value = mc.getAttr(expShapes[0] + '.' + attr)
                                            AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
            '''
            if infoFile in ['moveInfo']:
                objsLong = mc.ls(objs,l=1)
                personalObjsFile = localPathAnim + infoFile + '_Lobjs.txt'
                self.checkFileWrite(personalObjsFile, objsLong)
            '''
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile,shotType)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
        
    #------------------------------#   
    # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile , shotType = 2):
        import os
        # 本地路径转mel用
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
        fileInfo = infoFile + '_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
        fileInfo = infoFile + '_Lobjs.txt'
        if os.path.exists(localPathAnim + fileInfo):
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
            mel.eval(updateAnimCMD)
        
    #------------------------------#           
    # 模块：记录功能
    def checkAnimCurveInfoGet(self, animCurve):
        #print '-----------------'
        #print animCurve
        # 帧的时间值
        time = mc.keyframe(animCurve, q=1, tc=1)
        #print time
        # 帧的属性值
        value = mc.keyframe(animCurve, q=1, vc=1)
        # 切线 类型
        inputType = mc.keyTangent(animCurve, q=1, itt=1)
        outputType = mc.keyTangent(animCurve, q=1, ott=1)
        # 切线角度
        inputAngle = mc.keyTangent(animCurve, q=1, ia=1)
        outputAngle = mc.keyTangent(animCurve, q=1, oa=1)
        # 权重
        inputWeight = mc.keyTangent(animCurve, q=1, iw=1)
        outputWeight = mc.keyTangent(animCurve, q=1, ow=1)
        # 锁与否
        # lockType = mc.keyTangent(animCurve, q= 1, l=1)
        weightLock = mc.keyTangent(animCurve, q=1, wl=1)
        
        infoW = ''
        infoAll = []
        if time:
            for i in range(len(time)):
                # time  value  inputType   outputType weightLock
                infoW = (' ' + str(time[i]) + ' ' + str(value[i]) + ' ' + str(inputType[i]) + ' ' + str(outputType[i]) + ' ' + str(weightLock[i])) 
                specialFix = ['fixed']
                # 特殊情况补充行
                if inputType[i] in specialFix or outputType[i] in specialFix and weightLock[i]:
                    infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(outputAngle[i]))
                else:
                    if inputType[i] in specialFix  or outputType[i] in specialFix  and weightLock[i] != 'True':
                        infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(inputWeight[i]) + ' ' + str(outputAngle[i]) + ' ' + str(outputWeight[i]))
                infoAll.append(infoW + ';')
        return infoAll

    #------------------------------#   
    # 导入信息
    # 加入从服务器端读取功能
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = '' , shotType = 2):
        # 考虑下清理动画
        # 错误信息
        errorInfo = []
        # fsMode，指定路径读取
        if targetPath == '':
            # 本地获取
            if serverFile == 1:
                serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType)
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
                personalAmimFile = localPathAnim + infoFile + '.sla'
                personalObjFile = localPathAnim + infoFile + '_objs.txt'
        else:
            # 自定义读取路径
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        # 动画信息
        AnimsInfo = self.checkFileRead(personalAmimFile)
        # 获取objct信息，检测obj
        nsObjs = self.checkFileRead(personalObjFile)
        print nsObjs
        # 对物体有效性进行处理
        if nsObjs:
            checkNoneName = []
            for obj in nsObjs:
                # 替换物处理
                if replace:
                    obj = obj.replace(replace[0],replace[1])
                    if infoFile == 'proxy':
                        # master传proxy
                        if 'MSH_c_hi_proxy' not in replace[0]:
                            obj = obj + '_'
                        # proxy传master
                        if 'MSH_c_hi_proxy' in replace[0]:
                            obj = obj[0:-1]
                exist = mc.objExists(obj)
                if exist != True:
                    checkNoneName.append(obj)
            # 无错误
            if checkNoneName == []:
                linesInfo = len(AnimsInfo)
                if linesInfo > 5:
                    # 预设置
                    aniID = []
                    nonAnimID = []
                    # 单位
                    # linear = mc.currentUnit(q=1, f=1, l=1) 
                    linearSla = AnimsInfo[2].split(' ')[2][0:-1]
                    mc.currentUnit(linear=linearSla) 
                    # 角度
                    # anglular = mc.currentUnit(q=1, f=1, a=1)
                    anglularSla = AnimsInfo[3].split(' ')[2][0:-1]
                    mc.currentUnit(angle=anglularSla) 
                    # 制式
                    # timeType = mc.currentUnit(q=1, f=1, t=1)
                    timeTypeSla = AnimsInfo[4].split(' ')[2][0:-1]
                    mc.currentUnit(time=timeTypeSla) 
                    # 处理不对信息
                    for i in range(5, linesInfo):
                        # 去掉回车符
                        lineInfo = AnimsInfo[i][0:-1]
                        # 取anim行数信息
                        # maya的python中没有startsWith，换个方法
                        if 'anim ' in lineInfo and 'non-anim' not in lineInfo:
                            aniID.append(i)
                        if 'non-anim'  in lineInfo:
                            nonAnimID.append(i)
                    # 处理anim信息
                    for aid in aniID:
                        lineInfo = AnimsInfo[aid][0:-1]
                        # 获取属性
                        attr = lineInfo.split('.')[-1]
                        # 物体名处理
                        objCtrl = lineInfo.split('.')[0].split(' ')[-1]
                        # 替换
                        if replace:
                            objCtrl = objCtrl.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    objCtrl = objCtrl + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    objCtrl = objCtrl[0:-1]
                                    
                        key = ''
                        if 'Shape' not in objCtrl:
                            key = objCtrl + '.' + attr
                        else:
                            ctrolPoint = lineInfo.split('.')[-2]
                            key = objCtrl + '.' + ctrolPoint + '.' + attr
                        # key要存在，且只有一个，且可K帧，且没被锁
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取{}内数据
                            for j in range(1, linesInfo):
                                nextLine = AnimsInfo[aid + j ]
                                if (nextLine != '}') :
                                    if (nextLine != '{'):
                                        # 开始获取属性数据
                                        infoDetails = nextLine.split(' ')
                                        # time
                                        keyFrame = float(infoDetails[1])
                                        # value
                                        keyValue = float(infoDetails[2])
                                        # in & out
                                        keyInput = infoDetails[3]
                                        keyOutput = infoDetails[4]
                                        # weight
                                        infoWeightLock = infoDetails[5]
                                        if infoWeightLock == 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                            # in & out angle
                                            keyInputAngle = float(infoDetails[6])
                                            if ';' in infoDetails[7]:
                                                infoDetails[7] = infoDetails[7][0:-1]
                                            keyOutputAngle = float(infoDetails[7])
                                            # 还原帧
                                            mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                            mc.selectKey(key, k=keyFrame, r=1)
                                            mc.keyTangent(e=1, ia=keyInputAngle, iw=1, oa=keyOutputAngle, ow=1)
                                        else:
                                            if infoWeightLock != 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                                # in & out angle and weight
                                                keyInputAngle = float(infoDetails[6])
                                                keyInputWeight = float(infoDetails[7])
                                                keyOutputAngle = float(infoDetails[8])
                                                if ';' in infoDetails[9]:
                                                    infoDetails[9] = infoDetails[9][0:-1]
                                                keyOutputWeight = float(infoDetails[9])
                                                # 还原帧
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                                mc.selectKey(key, k=keyFrame, r=1)
                                                mc.keyTangent(e=1, ia=keyInputAngle, iw=keyInputWeight, oa=keyOutputAngle, ow=keyOutputWeight)
                                            else:
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue, itt=keyInput, ott=keyOutput)
                                else:       
                                    break
                        else:
                            #errorInfo.append(('===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============') % (str(key)))
                            errorInfo.append(u'===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============' % (key))
                    # 处理non-anim信息
                    for nid in nonAnimID:
                        # 获取属性
                        key = AnimsInfo[nid].split(' ')[1]
                        # 替换
                        if replace:
                            key = key.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    key = key + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    key = key[0:-1]
                        # key要存在，且只有一个，且可K帧，且没被锁
                        # 锁住后无法处理
                        # valueType 1,浮点数 | 0 字符串
                        valueType = 1
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取属性数据
                            value = AnimsInfo[nid].split(' ')[2][0:-1]
                            if value == 'True':
                                value = float(1.0)
                            if value == 'False':
                                value = float(0.0)
                            if value != 'True' and value != 'False':
                                try:
                                    value = float(value)
                                except:
                                    valueType = 0
                                    value = str(value)
                            if valueType:
                                mc.setAttr(key, value)
                            else:
                                mc.setAttr(key, value,type = 'string')
                else:  
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            # 丢失物体
            else:
                for error in checkNoneName:
                    #errorInfo.append(('=====================【！！！错误！！！】不存在传递物体【%s】=====================') % (error))
                    errorInfo.append(u'=====================【！！！错误！！！】不存在传递物体【%s】=====================' % (error))
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            for i in errorInfo:
                print(i)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 OTC及SET结构处理
    #  Author  : 沈康
    #  Data    : 2013_07_28
    #------------------------------#
    # OTC结构处理：删除 [更改：otc由mb强制变更ma;删除先删除ma文件，后找mb，若有则删除]
    def sk_sceneGRPDelete(self, fileGRP='OTC' , shotType = 2):
      
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        #fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileFomat = '.ma'
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
            mel.eval(cmd)
        else:
            fileFomat = '.mb'
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            if os.path.exists(otcFileServer):
                cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
                mel.eval(cmd)

    #------------------------------#
    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC' , server=1 , shotType = 2 ,needNsList = []):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        renderFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFile = renderFilePath + baseShotInfo + fileGrpType + fileFomat
        
        root = mc.ls(assemblies=True)
        if root:
            if (fileGRP + '_GRP') in root:
                # OTC和SET处理，导出
                mc.select(fileGRP + '_GRP')
                mc.file(otcFile, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
        mc.select(cl=1)
        
        # 对set进行转参考处理
        if fileGRP == 'SET':
            # ma模式处理
            animRefInfos = sk_infoConfig.sk_infoConfig().checkFileRead(otcFile)
            renderRefInfos = []
            for line in animRefInfos:
                if '_ms_anim.m' in line:
                    line = line.replace('_ms_anim.m','_ms_render.m')
                renderRefInfos.append(line)
            sk_infoConfig.sk_infoConfig().checkFileWrite(otcFile,renderRefInfos)
        # 对otc进行转参考处理
        if fileGRP == 'OTC':
            # ma模式处理
            animRefInfos = sk_infoConfig.sk_infoConfig().checkFileRead(otcFile)
            renderRefInfos = []
            for lineInfo in animRefInfos:
                if 'file' in lineInfo and '-ns' in lineInfo:
                    needState = 0
                    for checkNs in needNsList:
                        checkInfo = '-ns "%s"'%checkNs
                        if checkInfo in lineInfo:
                            needState = 1
                    if needState:
                        renderRefInfos.append(lineInfo)
                else:
                    renderRefInfos.append(lineInfo)
            sk_infoConfig.sk_infoConfig().checkFileWrite(otcFile,renderRefInfos)
        print '--------target'
        print  otcFile
        # 传至服务器
        if server:
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            cmd = 'zwSysFile(\"copy\",\"' + otcFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
            
    #------------------------------#
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , shotInfo , serverModify = 1 , shotType = 2):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileGrpType = '_set_render'
        
        if serverModify == 0:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)

        if serverModify == 1:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        needSetFile = needFilePath + baseShotInfo + fileGrpType + fileFomat
        
        import os
        if os.path.exists(needSetFile):
            # 不加载参考导入
            mc.file(needSetFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            print u'====================开始处理SET_GRP文件===================='
            # 处理好文件
            # 在importOTC之前处理好anim中材质更改的情况
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            mc.file(save = 1, force = 1)
        
        if serverModify == 0:
            # 传至服务器
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            print otcFileServer
            cmd = 'zwSysFile(\"copy\",\"' + needSetFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
        print u'====================SET_GRP更新完毕===================='

    #------------------------------#
    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC' , shotType = 2):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        
        # ma文件利于文本读取改参考
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        
        # 判断otcFile存在与否
        import os
        if os.path.exists(otcFileServer):
            # 在则删除OTC_GRP，并import去掉namespace
            # finalLayout阶段是OTC_GRP是空的
            if mc.ls(fileGRP + '_GRP'):
                mc.delete(fileGRP + '_GRP')
            # import 
            # 记录时间
            import time
            timeNow = time.ctime().split(" ")[3].replace(":", "_")
            # 记录毫秒
            import datetime
            msTime = datetime.datetime.now().microsecond
            timeNow = timeNow + str(msTime / 100000)
            #timeMsec = datetime.datetime.now().microsecond
            #timeNow = timeNow + '_' + str(timeMsec)
            ns = 'food' + timeNow
            if fileGRP == 'SET':
                # 导入,必须这里清理
                print '---'
                print otcFileServer
                mc.file(otcFileServer, i=1 , loadReferenceDepth="none", namespace = ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            if fileGRP == 'OTC':
                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))
    
    #-------------------------------------#
    # 检测是否存在render文件
    def sk_FLCheckRenderFile(self,refInfos):
        import os
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            errorAsset = []
            for i in range(len(refPaths)):
                refPath = refPaths[i]
                renderFilePath = refPath.replace('_anim.','_render.')
                if os.path.exists(renderFilePath):
                    pass
                else:
                    errorAsset.append(refNodes[i])
            if errorAsset:
                print u'-------------------以下render文件不存在-------------------'
                for info in errorAsset:
                    print info[:-2]
                print u'-------------------以上render文件不存在-------------------'
                print u'==================请先检查shot文件确定参考是否正确=================='
                print u'==================正确后请再和前期协商更新asset文件=================='
                mc.error(u'==================请和前期协商更新asset文件==================')
        else:
            print(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')
            mc.error(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')
    
    #-------------------------------------#
    # 记录hide输出
    def sk_FL_RefHideObjsRecord(self,server,shotType):
        unDisplayLayerObjs = []
        # 记录：shot文件非参考的隐藏的显示层的物体
        if server:
            displayLayers = mc.ls(type = 'displayLayer')
            if displayLayers:
                for layer in displayLayers:
                    isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                    if isRef == 0 and layer != 'defaultLayer':
                        viewState  = mc.getAttr(layer + '.visibility')
                        if viewState == False:
                            objs = mc.editDisplayLayerMembers( layer, query=True,fn=1)
                            if objs:
                                unDisplayLayerObjs = unDisplayLayerObjs + objs
            hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
            mc.sysFile(hideObjsServerPath,makeDir = 1)
            self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
            print u'\n'
            print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')
            print u'\n'
        return unDisplayLayerObjs
    
    #-------------------------------------#
    # 不用于cache的参考记录
    def skFLNoNeedRefNodeInfo(self):
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
        return noNeedRefNodeInfo
    
    #-------------------------------------#
    # 输出角色道具信息
    def skFLAssetNeedInfo(self,refInfos,noNeedRefNodeInfo,shotType):
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
                if '_' not in refNode:
                    continue                
                if refNode.split('_')[1][0] not in ['s', 'S']:
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    assetNeedOutputInfo.append(newPath)
                    assetNeedOutputInfo.append(ns)
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
        print u'\n'
        print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
        print u'\n'
        return assetNeedOutputInfo
    
    #-------------------------------------#        
    # 新建参考
    def sk_FLRefRebuild(self,refInfos,noNeedRefNodeInfo):
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        
        print '[Ref Info]'
        print refInfos[0][0]
        print '[NoNeedRef Info]'
        print noNeedRefNodeInfo
        # 导入参考，注意将_ms_anim替换成_ms_render
        # OTC内的参考不参与处理
        # shareNode只能对第一级reference处理。。。
        for i in range(len(rfnLv1)):
            ns = refInfos[2][0][i]
            refNode = refInfos[0][0][i]
            if noNeedRefNodeInfo:
                if refNode not in noNeedRefNodeInfo:
                    # 应清理refNode及namespace
                    if mc.ls(refNode):
                        try:
                            mc.file(rfn=refNode , removeReference=1)
                        except:
                            mc.lockNode(refNode, l=0)
                            mc.delete(refNode)
                    # 清理namespace
                    try:
                        # 使得namespace成为空的namespace
                        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                        # 清理空namespace
                        mc.namespace(removeNamespace= (':' + ns))
                    except:
                        pass
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    # 此处加referenceNode，是必须的，因为部分文件里即便namespace一致但数字1在refNode顺序不一样
                    # 保证强行一致
                    # shareNodes和cache以及ref list edit有冲突？角色道具可以关闭，同时场景已经合并材质节点
                    # mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns , referenceNode = refNode )
                    mc.file(newPath, r=1, namespace=ns , referenceNode = refNode )
                    print u'\n'
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print u'\n'
            else:
                if '_' not in refNode:
                    continue                
                if refNode.split('_')[1][0] not in ['s', 'S']:
                    # 应清理refNode及namespace
                    if mc.ls(refNode):
                        try:
                            mc.file(rfn=refNode , removeReference=1)
                        except:
                            mc.lockNode(refNode, l=0)
                            mc.delete(refNode)
                    # 清理namespace
                    try:
                        # 使得namespace成为空的namespace
                        mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                        # 清理空namespace
                        mc.namespace(removeNamespace= (':' + ns))
                    except:
                        pass
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    #mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns)
                    mc.file(newPath, r=1, namespace=ns , referenceNode = refNode )
                    print u'\n'
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print u'\n'
            
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有约束BK，确保动画及camera正确】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#  
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self):
        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if  constraintsAll:
            tobake= []
            # 处理非参考的物体
            constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,d=0,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    checkState = 0
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            #print shape 
                            #print obj
                            if mc.nodeType(shape[0]) != 'camera':
                                checkState = 1
                        else:
                            checkState = 1
                    if not checkState:
                        continue
                    # 进行属性检测
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    consState = 0
                    for attr in attrs:
                        cons = mc.listConnections((obj + attr),s=1,d=0)
                        if cons:
                            consState = 1
                            break
                    if consState:
                        plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)

            # 处理参考的_ct_an物体
            constraintRefs = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
            for constraint in constraintRefs:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,d=0,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    checkState = 0
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            if mc.nodeType(shape[0]) != 'camera':
                                if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                    checkState = 1
                        else:
                            if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                checkState = 1
                    if not checkState:
                        continue
                    # 进行属性检测
                    attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                    consState = 0
                    for attr in attrs:
                        cons = mc.listConnections((obj + attr),s=1,d=0)
                        if cons:
                            consState = 1
                            break
                    if consState:
                        plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)

            tobake = list(set(tobake))
            
            # 改进版，不bake，而是给新locator bake
            if tobake:
                # 删除locators
                locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    mc.delete(locators)
                '''
                # 老赵bake脚本
                mc.select(tobake)
                mel.eval('source \"zzjUtilityTools\"')
                mel.eval('zzjUtilityTools \"bakeAnim\"')
                '''
                # 数值传递到locators
                locators = []
                constraintTemp = []
                for i in range(len(tobake)):
                    locTemp = mc.spaceLocator()
                    locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
                    cons = mc.parentConstraint(tobake[i] , locTemp)
                    constraintTemp.append(cons[0])
                    locators.append(locTemp)
                # 一次烘焙
                mc.bakeResults(locators,  t=io,
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=0,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=0)
                mc.delete(constraintTemp)

                # 重新约束物体
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                #locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    for i in range(len(locators)):
                        # 打断t和r属性
                        for attr in attrs:
                            #mel.eval('CBdeleteConnection \"' + tobake[i] + attr + '\"')
                            #self.checkDeleteConnection(tobake[i] + attr)
                            #修改原因（有的锁定）
                            try:
                               self.checkDeleteConnection(tobake[i] + attr)
                            except:
                                pass    
                        locatorGrp = locators[i]
                        #  父子约束 ,cam已经锁住
                        if 'cam_' not in tobake[i]:
                            print u'----------------'
                            print locatorGrp
                            print tobake[i].split('|')[-1]
                            # 位移检测
                            skipTranslateAxis = []
                            checkTAttr = ['.tx','.ty','.tz']
                            for j in range(3):
                                passAttr = ['x','y','z']
                                tState = mc.getAttr((tobake[i] + checkTAttr[j]),settable = 1)

                                if tState:
                                    pass
                                else:
                                    skipTranslateAxis.append(passAttr[j])
                            # 旋转检测
                            skipRotateAxis = []
                            checkRAttr = ['.rx','.ry','.rz']
                            for k in range(3):
                                passAttr = ['x','y','z']
                                rState = mc.getAttr((tobake[i] + checkRAttr[k]),settable = 1)
                                if rState:
                                    pass
                                else:
                                    skipRotateAxis.append(passAttr[k])
                            # 父子约束
                            if skipTranslateAxis and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis)
                            if skipTranslateAxis == [] and skipRotateAxis:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipRotate = skipRotateAxis)
                            if skipTranslateAxis and skipRotateAxis:
                                print '------'
                                print locatorGrp
                                print tobake[i]
                                # 修正全忽略的问题，全部忽略再去创建约束会报错
                                if (skipTranslateAxis == ['x','y','z']) and (skipRotateAxis == ['x','y','z']):
                                    pass
                                else:
                                    
                                    #mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                    #忽略锁定
                                    try:
                                        mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                    except:
                                        pass                                          
                            if skipTranslateAxis == [] and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i])

                    # 二次烘焙
                    try:
                        mc.bakeResults(tobake,    t=io,
                                simulation=1,
                                sampleBy=1,
                                disableImplicitControl=1,
                                preserveOutsideKeys=1,
                                sparseAnimCurveBake=1,
                                removeBakedAttributeFromLayer=0,
                                bakeOnOverrideLayer=0,
                                controlPoints=0,
                                shape=1)
                    except:
                        pass

                    # 删除约束
                    constraintConfigs = [x for x in (constraints + constraintRefs) if not mc.referenceQuery(x,inr=1)]
                    for cons in constraintConfigs:
                        ref = mc.referenceQuery(cons,isNodeReferenced = 1)
                        if not ref:
                            mc.delete(cons)

                    # 删除locators
                    mc.delete(locators)

                    print(u'\n========================【约束】【烘焙】【成功】========================')
                    print u'\n'
        else:
            print(u'\n========================【约束】【烘焙】【失败】========================')
            print u'\n'
        
    #------------------------------#
    # 【辅助】完全断开指定属性
    #------------------------------#     
    # 完全断开指定属性
    def checkDeleteConnection(self , attr ):
        # 被输入方
        if mc.connectionInfo(attr , isDestination = 1):
            destination = mc.connectionInfo(attr , getExactDestination = 1)
            srcConn = mc.listConnections(destination, s = 1, d = 0 , type = 'character')
            if srcConn:
                # 断开
                mc.character(destination , e = 1 ,rm = srcConn[0])
#                try:
#                    mc.character(destination , e = 1 ,rm = srcConn[0])
#                except:
#                    pass
            
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)
                
    #----------------------------------------------------------------------------------------------#
   
    #------------------------------#
    # 【辅助】【分拆用】asset信息输出
    #------------------------------#   
    # asset信息输出
    # needType : 0 需要所有asset，chr,prop,set 标准信息 |  1 只要chr ,prop
    def sk_assetInfoUpdate(self,reorganize = [0,0],needType = 1):
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

        assetNeedOutputInfo = []    
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        
        # 只要reference标准信息
        if needType == 0:
            txtName = 'assetAllReference.txt'
            for i in range(len(rfnLv1)):
                refAsset = rfnPathLv1[i].split('/master/')[0].split('/')[-1]
                newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                assetNeedOutputInfo.append(newPath)
                assetNeedOutputInfo.append(refAsset)
        
        # 只要非VFX_GRP和SET_GEP的chr 和 prop
        if needType == 1:
            txtName = 'assetReference.txt'
            # 处理大组
            if reorganize[0]:
                sk_sceneTools.sk_sceneTools().sk_sceneReorganize(reorganize[1])

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
            # 输出数据
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

        assetLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        print assetNeedServerPath
        print txtName
        # 写
        self.checkFileWrite((assetLocalPath +  txtName), assetNeedOutputInfo)
        # 传递
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (assetLocalPath + txtName) + '"' + ' ' + '"' + (assetNeedServerPath + txtName) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'\n'
        print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
        print u'\n'
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【通用】【信息处理函数集】
    #  0.所有阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_05_16
    #------------------------------#
    # 文件名镜头信息
    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
             
        return info   
                    
    #------------------------------#
    # 获取本地文件路径
    def checkPCFilePath(self):
        filePath = (mc.file(query=1, exn=1)).split('/')
        path = ''
        if filePath[0] != 'Z' and filePath[0] != '':
            for i in range(len(filePath) - 1):
                path = path + filePath[i] + '\\'
        return path
    
    #------------------------------#
    # 本地infot路径
    def checkLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath
    
    #------------------------------#
    # 服务器端project路径
    def checkProjectServerPath(self):
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectServerPath = '//file-cluster/GDC/Projects/' + project + '/Project/'
        return projectServerPath
    
    #------------------------------#
    # 本地tex方案路径
    def checkTexLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathTex = ('D:/Info_Temp/temp/texTemp/' + str(dirInfo[1]) + '/' )
        mc.sysFile(localPathTex, makeDir=True)
        return localPathTex
    
    #------------------------------#
    # 服务器端tex方案路径
    def checkTexServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathTex = ('//file-cluster/GDC/Projects/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/')
        return serverPathTex
    
    #------------------------------#
    # 本地tx2AnimRender路径
    def checkTX2AnimRenderLocalPath(self):
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/tx2AnimRenderTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    #------------------------------#
    # 本地cache路径
    def checkCacheLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2])+ '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    #------------------------------#
    # 服务器端cache路径
    def checkCacheServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        return serverPathCache
    
    #------------------------------#
    # 本地anim路径
    def checkAnimLocalPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        localPathAnim = ('D:\\Info_Temp\\temp\\animInfoTemp\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim
    
    #------------------------------#
    # 服务器端cache路径
    def checkAnimServerPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        return serverPathAnim

    #------------------------------#
    # 本地finalLayout路径
    def checkFinalLayoutLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout
    
    #------------------------------#
    # 服务器端cache路径
    def checkFinalLayoutServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        return serverPathFinalLayout
    
    #------------------------------#
    # 特殊内部任务ID
    def checkStrangeIDInfo(self):
        dataPath = self.checkProjectServerPath() + 'data/localAsset.txt'
        strangeID = self.checkFileRead(dataPath)
        return strangeID

    
    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【通用】【读写文件数据处理】
    #  0.所有阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_03_01
    #------------------------------#
    # 创建目录
    def checkPathInfo(self):
        dirInfo = self.checkShotInfo()
        path = ('D:\\Info_Temp\\temp\\cacheTemp\\' + dirInfo[0] + '\\' + str(dirInfo[1]) + '\\' + str(dirInfo[2]) + '\\')
        mc.sysFile(path, makeDir=True)
        return path
    
    #------------------------------#
    # 读文件
    def checkFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        txt = open(os.path.normpath(path), 'r');
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
    # 写文件
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        mc.sysFile(os.path.dirname(path), makeDir=True)
        if addtion == 1:
            info = self.checkFileRead(path) + info
        #txt = open(path, 'w')
        try:
            txt = open(path,'w')
        except:
            print '----------'
            print path
            txt = open(path,'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
    
    #----------------------------------------------------------------------------------------------#

    #------------------------------#
    # 【通用】【项目数据处理】
    #  0.所有阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_06_4
    #------------------------------#
    # 简写 切 长写
    def checkProjectNameSimple2Full(self, simple):
        full = ''
        if simple == 'zm':
            full = 'ZoomWhiteDolphin'
        if simple == 'zo':
            full = 'Zorro'
        if simple == 'cl':
            full = 'Calimero'
        if simple == 'hf':
            full = 'HeroFactory'
        return full
        
    #------------------------------#
    # 长写 切  简写
    def checkProjectNameFull2Simple(self, full):
        simple = ''
        if full == 'ZoomWhiteDolphin':
            simple = 'zm'
        if full == 'Zorro':
            simple = 'zo'
        if full == 'Calimero':
            simple = 'cl'
        if full == 'HeroFactory':
            simple = 'hf'
        return simple
    
    #------------------------------#
    # 项目音频标记
    def checkProjectAudioPath(self, full):
        audioPath = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            audioPath = 'zm'
        if full == 'Zorro' or full == 'zo':
            audioPath = 'zo'
        if full == 'Calimero' or full == 'cl':
            audioPath = 'CA'
        if full == 'HeroFactory' or full == 'hf':
            audioPath = 'hf'
        return audioPath
    
    #------------------------------#
    # 项目初始帧（可用pipeline替代）
    def checkProjectStartFrame(self, full):
        startFrame = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            startFrame = 1001
        if full == 'Zorro' or full == 'zo':
            startFrame = 101
        if full == 'Calimero' or full == 'cl':
            startFrame = 1
        if full == 'HeroFactory' or full == 'hf':
            startFrame = 101
        return startFrame
    
    #------------------------------#
    # 项目文件格式读取   简写
    def checkProjectFileFormat(self, pro):
        fileType = ''
        maList = ['cl']
        if pro in maList:
            fileType = '.ma'
        else:
            fileType = '.mb'
        return fileType
    
    #------------------------------#
    # 项目文件格式   全称
    def checkProjectFileFormatFull(self, pro):
        fileType = self.checkProjectFileFormat(pro)
        fileTypeFull = ''
        if fileType == '.ma':
            fileTypeFull = 'mayaAscii'
        if fileType == '.mb':
            fileTypeFull = 'mayaBinary'
        return fileTypeFull

    #----------------------------------------------------------------------------------------------#
    
    #------------------------------#
    # 【专用】【杂项工具集】
    #  0.阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_04_10
    #------------------------------#
    # 不参与渲染的物体清单
    def checkNoRenderObjs(self):
        grps = mc.ls(type='transform', l=1)
        outGrps = []
        for grp in grps:
            if '_si_' in grp or  '_nr_' in grp:
                outGrps.append(grp)
        return outGrps
    
    #------------------------------#  
    # 获取物体的namespace
    def checkObjNamespace(self, obj):
        nmInfo = obj.split(':')
        namespace = ''
        for i in range(len(nmInfo) - 1):
            if i == 0:
                namespace = nmInfo[i]
            else:
                namespace = namespace + ':' + nmInfo[i]
        return namespace
    
    #------------------------------#
    # 【通用：空namespace清理工具，清理namespace工具】      
    def checkNamespaceCleanEmpty(self, configType=1):
        # 设置之前必须清除当前默认前缀，最后还原回去
        preName = mc.namespaceInfo(currentNamespace=1)
        mc.namespace(set=':')
        namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaces.remove('UI')
        namespaces.remove('shared')
        if namespaces :
            for name in namespaces:
                # 必须设置namespace才能返回当前默认set的信息
                mc.namespace(setNamespace=str(':' + name))
                # 1为处理空的namespace
                if configType == 1:
                    info = mc.namespaceInfo(listOnlyDependencyNodes=1, dagPath=1)
                    if info == None:
                        mc.namespace(set=':')
                        mc.namespace(removeNamespace=name)
                # 2为处理所有非参考namespace
                if configType == 2:
                    mc.namespace(set=':')
                    mc.namespace(force=1, moveNamespace=[name, ':'])
                    mc.namespace(removeNamespace=name)
        mc.namespace(set=str(':' + preName))

    
    #------------------------------# 
    # 强行将所有SG和shader打断，并重新连接
    def checkShaderSGReConnection(self):
        # 获取有效的mesh及shader及SG节点
        SGNodes = mc.ls(type = 'shadingEngine')
        if SGNodes:
            if 'initialParticleSE' in SGNodes:
                SGNodes.remove('initialParticleSE')
            if 'initialShadingGroup' in SGNodes:
                SGNodes.remove('initialShadingGroup')
            if SGNodes:
                # 开始获取信息
                shaderAttr = ''
                meshes = []
                for sgNode in SGNodes:
                    if mc.listConnections((sgNode + '.surfaceShader'),source = 1 , plugs = 1):
                        shaderAttr = mc.listConnections((sgNode + '.surfaceShader'),source = 1,plugs = 1)[0]
                    if mc.listConnections(sgNode,source = 1 , type = 'mesh'):
                        meshes = mc.listConnections(sgNode,source = 1 , type = 'mesh')
                    if shaderAttr and meshes:
                        # 删除SG节点
                        mc.delete(sgNode)
                        # 重连物体
                        newSGNode = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= (sgNode ))
                        mc.connectAttr((shaderAttr), (newSGNode + '.surfaceShader'))
                        mc.sets( meshes, e=1, forceElement= newSGNode )
                        
    #------------------------------# 
    # 【通用，对list实现乱序功能，lenList必须大于1】
    def checkRandomList(self,sourceList):
        if len(sourceList) > 1:
            import random
            tempList = sourceList[:]
            indexNum = len(tempList)
            needList = []
            for i in range(indexNum):
                tempIndex = int(random.uniform(1,indexNum))-1
                needList.append(tempList[tempIndex])
                tempList.remove(tempList[tempIndex])
                indexNum = indexNum - 1
            return needList

    #------------------------------# 
    # 【通用：同类判断归类脚本】（proxySYS用？）
    def checkSameIDConfig(self, objs, configType):
        details = dict({})
        # 处理循环
        for grp in objs:
            ID = ''
            # 处理类型
            # 截取'_'第二位
            if configType == 1:
                ID = grp.split('_')[1]
            if configType == 2: 
            # 截取'_'第二位和第三位
                size = len(grp.split('_'))
                if size >= 3:
                    ID = grp.split('_')[1] + '_' + grp.split('_')[2]
                else:
                    ID = grp.split('_')[1]
            # 开始处理数据
            keys = details.keys()
            if ID in keys:
                details[ID].append(grp)
            else:
                details[ID] = []
                details[ID].append(grp)
        return details
                        
                        
    #----------------------------#
    # 【通用：获取checkList内所有相同元素的编号】
    #----------------------------#
    # 获取list内所有相同元素的编号 ，index number
    def checkListSameAllIndex(self, checkList, checkObj):
        tempList = checkList[:]
        checkAdd = 0
        allIndex = []
        while tempList.count(checkObj) > 0:
            indexNow = tempList.index(checkObj)
            allIndex.append(checkAdd + indexNow)
            tempList.remove(checkObj)
            checkAdd = checkAdd + 1
        return allIndex
                        
    
    #------------------------------#  
    # 【构思】 anim传递版FL
    # 算法不好。。很多时候动画是有中间媒介的，最好控制器set组
    # 注意 mute！！！！
    def checkAnimCurveObjs(self):
        animCurveInfos = mc.ls(type = 'animCurve')
        needObjs = []
        for info in animCurveInfos:
            if 'CAM:' not in info:
                needObj = info [:-1*(1 + len(info.split('_')[-1]))]
                if mc.objExists(needObj):
                    needObjs.append(needObj)
                else:
                    needObj = mc.listConnections(info,d =1 )[0]
                    needObjs.append(needObj)
        needObjs = list(set(needObjs))
        return needObjs

    #------------------------------#  
    # cache path 环境变量处理
    def checkCacheEnvPath(self):
        cacheFiles = mc.ls(type='cacheFile')
        if cacheFiles:
            for node in cacheFiles:
                cachePath = mc.getAttr(node + '.cachePath')
                cachePathNew = cachePath.replace('//file-cluster/GDC/Projects','${IDMT_PROJECTS}')
                mc.setAttr((node + '.cachePath'),cachePathNew,type = 'string')


    #----------------------------------------------------------------------------------------------#
    def printTest(self):
        print u'大家好'
        print '大家好'
        

    
    '''
            【核心通用：检测关键字是否在其内，搜索，允许-屏蔽关键字】
    0.通用
    Author: 沈  康
    Data    :2013_03_16
    '''           
   
    def checkInfoSearch(self, KEYS, INFO):
    #    INFO = ['大碗是','大家 好/fw']
    #    KEYS = ['大','是','大家','大碗']
        do_y = []
        do_n = []
        do_o = []
        temp_keys = KEYS[:]
        for key in temp_keys:
            if '-' in key:
                temp_keys.remove(key)
                do_n.append(key.split('-')[1])   
                
        if do_n:    
            for info in INFO:
                for don in do_n:
                    if don in info:
                        return None         
                               
        for i in range(len(temp_keys)):
            do_o.append(1)
            do_y.append(0)
            for info in INFO:
                if temp_keys[i] in info:
                    do_y[i] = 1
         
        if do_y == do_o:
            return True   
        
    #---------------------#
    # displayLayer处理 nmr,norender,nodisplay
    #---------------------#
    def displayLayerInfoExport(self,shotID = '',fixType = 'nmf',server = 1):
        if not shotID:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
            shotID = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
            if shotType == 3:
                shotID += '_' + shotInfos[3]
        shotFolder = shotID.split(shotID.split('_')[0])[-1].replace('_','/')
        #本机
        localPath=sk_infoConfig.sk_infoConfig().checkLocalInfoPath() + fixType
        localPath = '%s%s'%(localPath,shotFolder)
        if not os.path.exists(localPath):
            mc.sysFile(localPath, makeDir=True)
        #服务器路径
        serverPath=sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverPath = '%sdata/%s%s'%(serverPath,fixType,shotFolder)
        if fixType in ['nmf']:
            disLayers = mc.ls('near',type = 'displayLayer')
            disLayers += mc.ls('mid',type = 'displayLayer')
            disLayers += mc.ls('far',type = 'displayLayer')
            if not disLayers:
                return
            # 提前检测
            checkObjs = []
            tempLayer = 'near'
            if mc.ls(tempLayer,type = 'displayLayer'):
                temp = mc.editDisplayLayerMembers(tempLayer,q=1,fn=1)
                if temp:
                    checkObjs = checkObjs + temp
            tempLayer = 'mid'
            if mc.ls(tempLayer,type = 'displayLayer'):
                temp = mc.editDisplayLayerMembers(tempLayer,q=1,fn=1)
                if temp:
                    checkObjs = checkObjs + temp
            tempLayer = 'far'
            if mc.ls(tempLayer,type = 'displayLayer'):
                temp = mc.editDisplayLayerMembers(tempLayer,q=1,fn=1)
                if temp:
                    checkObjs = checkObjs + temp
            noObjs = []
            for checkObj in checkObjs:
                if '_ms_gpu' in checkObj:
                    noObjs.append(checkObj)
            if noObjs:
                print '\n------]Gpu Objs Check[------'
                for i in noObjs:
                    print i
                print '------]Gpu Objs Check[------\n'
                #mc.error()
                # return
            # 运行
            for checkLayer in disLayers:
                localFile = '%s/%s.txt'%(localPath,checkLayer)
                serverFile= '%s/%s.txt'%(serverPath,checkLayer)
                layerObjs = mc.editDisplayLayerMembers(checkLayer,q=1,fn=1)
                if not layerObjs:
                    continue
                needObjs = []
                for checkObj in layerObjs:
                    if '|OTC_GRP|' in checkObj and ('|VFX_GRP' not in checkObj and '|CLUSTER_GRP' not in checkObj):
                        continue
                    checkType = mc.nodeType(checkObj)
                    if checkType in ['joint']:
                        continue
                    shape = mc.listRelatives(checkObj,s=1,ni=1,f=1)
                    if not shape:
                        # 空组
                        needObjs.append(checkObj)
                    else:
                        # 仅模型
                        if mc.nodeType(shape[0]) not in ['mesh']:
                            continue
                        if ':MODEL|' in checkObj:
                            needObjs.append(checkObj)
                sk_infoConfig.sk_infoConfig().checkFileWrite(localFile,needObjs)
                if server:
                    updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localFile) + '"' + ' ' + '"' + (serverFile) + '"' + ' true'
                    mel.eval(updateAnimCMD)
                    print serverFile
                    print u'===[Updating layerInfo To Server]===传输[%s]完毕==='%checkLayer

    def displayLayerInfoImport(self,shotID = '',fixType = 'nmf',server = 1):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        if not shotID:
            shotID = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
            if shotType == 3:
                shotID += '_' + shotInfos[3]
        shotFolder = shotID.split(shotID.split('_')[0])[-1].replace('_','/')
        if server:
            serverPath =sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            needPath = '%sdata/%s%s'%(serverPath,fixType,shotFolder)
        else:
            localPath =sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
            needPath = '%s%s/%s'%(localPath,fixType,shotFolder)
        if fixType in ['nmf']:
            lostObjs = []
            for checkLayer in ['near','mid','far']:
                # 清理旧显示层
                if mc.ls(checkLayer,type= 'displayLayer'):
                    self.deleteDisplayLayer(checkLayer)
                layerFile = '%s/%s.txt'%(needPath,checkLayer)
                if not os.path.exists(layerFile):
                    continue
                # 创建
                mc.createDisplayLayer(empty = 1, name = checkLayer)
                checkObjs = sk_infoConfig.sk_infoConfig().checkFileRead(layerFile)
                if checkObjs:
                    needObjs = []
                    for checkObj in checkObjs:
                        if not mc.ls(checkObj):
                            if '|OTC_GRP|' in checkObj:
                                continue
                            if shotInfos[1] in ['010'] and '|SET_GRP|' in checkObj:
                                continue
                            if '_joint' in checkObj.split('|')[-1]:
                                continue
                        else:
                            if mc.nodeType(checkObj) in ['displayLayer']:
                                continue
                        needObjs.append(checkObj)
                    if not needObjs:
                        continue
                    try:
                        mc.editDisplayLayerMembers(checkLayer,needObjs , nr = 1)
                    except:
                        for checkObj in needObjs:
                            if not mc.ls(checkObj):
                                lostObjs.append(checkObj)
                print u'===[Import layerInfo From Server]===传输[%s]完毕==='%checkLayer
            if lostObjs:
                for lostObj in lostObjs:
                    print '---------No Obj:'
                    print lostObj
                mc.error()

    def deleteDisplayLayer(self,layer):
        # 断开layerManager和其连接再删除
        layerManager = mc.connectionInfo( (layer + '.identification'),sourceFromDestination = 1)
        if layerManager:
            if 'layerManager' in layerManager:
                mc.disconnectAttr(layerManager,(layer + '.identification'))
        # 断开输出链接
        outputs = mc.connectionInfo( (layer + '.drawInfo'),destinationFromSource = 1)
        if outputs:
            for out in outputs:
                mc.disconnectAttr((layer + '.drawInfo'),out)
        mc.delete(layer)


    # 获取otc里参考物体列表
    def otcRefCheck(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNsList = refInfos[2][0]
        otcGrp = 'OTC_GRP'
        needNsList = []
        for checkNs in refNsList:
            nsObjs = mc.ls('%s:*'%checkNs,l=1,type = 'transform')
            for checkObj in nsObjs:
                inr = mc.referenceQuery(checkObj,inr=1)
                if not inr:
                    continue
                fullName = mc.ls(checkObj,l=1)[0]
                if '|%s|'%otcGrp in fullName:
                    needNsList.append(checkNs)
                break
        return needNsList