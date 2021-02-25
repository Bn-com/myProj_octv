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

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_cacheFinalLayout(object):
    def __init__(self):
        # namespace清理
        pass
        
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
    def checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -50 ):
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        import os

        # 检测参考是否正确，是否有render参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
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
            mc.error(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')

        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')

        # 修正时间轴
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame')

        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath()
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath()

        # 本地另存
        localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'

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
        camServerPath = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_cam_baked.ma'
        if server:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1)
            print u'\n'
            print u'==========================camera传输完毕=========================='
            print u'\n'
        
        # 预处理，约束清理
        self.sk_checkBakeConstraints()
        #print(u'========================【约束】【烘焙】【成功】========================')

        # 清理服务器端旧的SET和OTC文件
        self.sk_sceneGRPDelete('SET')
        self.sk_sceneGRPDelete('OTC')

        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'
        
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
                            objs = mc.editDisplayLayerMembers( layer, query=True,fullNames=1 )
                            if objs:
                                unDisplayLayerObjs = unDisplayLayerObjs + objs
            hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            mc.sysFile(hideObjsServerPath,makeDir = 1)
            self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
            print u'\n'
            print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')
            print u'\n'

                
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

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
        
        # 输出需要的角色和道具参考信息
        if server:
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
            assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
            print u'\n'
            print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
            print u'\n'
        
        # 导出SET_GRP和OTC_GRP文件
        self.sk_sceneGRPExport('SET')
        self.sk_sceneGRPExport('OTC')
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'

        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'
    
        # 判断是否ms_anim文件
        if shotInfos[3] == 'an':
            # 输出cache 及 anim
            # 先输出anim
            animObjs = self.checkAnimSetObjects()
            self.checkAnimCurveInfoExport(animObjs, 1)
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
                self.checkCacheVStateExport(cacheObjs)
                # 输出cache
                # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                self.checkCacheSetCacheExport(cacheObjs, server , cachePre , 1 , 0)
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
            
            
            # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
            self.sk_sceneSETRefShaderReset([shotInfos[0],shotInfos[1],shotInfos[2]])

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
            # 本地文件
            localFile = localPath + fileName
            # 服务器端文件
            # serverFile = serverPath + fileName
            # 重命名
            mc.file( rename= localFile )
            mc.file(save = 1 ,force = 1)
            
            # 导入场景
            # 必须先导入OTC，后载入参考，否则容易出错(PORORO经验)
            # 导回SET_GRP和OTC_GRP
            self.sk_sceneGRPImport('SET')
            self.sk_sceneGRPImport('OTC')
            print u'\n'
            print(u'=====================【Group】【服务器端】【导入】完毕=====================')
            print u'\n'
            
            # 导入reference及share nodes（新导入场景，后导入参考）
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
                    if refNode.split('_')[1][0] not in ['s', 'S']:
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        #mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns)
                        mc.file(newPath, r=1, namespace=ns , referenceNode = refNode )
                        print u'\n'
                        print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                        print u'\n'
            
            # 导入cam
            # 导入相机
            sk_hbExportCam.sk_hbExportCam().camServerReference()  
    
            # 处理大组
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1)
            
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

            # 强行备份材质
            if cacheObjs:
                MatLists = self.checkCacheRecordMaterial(cacheObjs,1)

            # 场景搭建完毕
            # 载入anim
            self.checkAnimCurveInfoImport(1)
            
            print u'\n'
            print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
            print u'\n'
            # 处理buging

            # 载入cache及自带的anim
            cacheObjs = self.checkCacheSetObjects()
            if cacheObjs:
                self.checkCacheSetCacheImport(cacheObjs, server)
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
                self.checkCacheVStateImport()
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
            
            # 本地保存
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            # 设置时间轴等消息
            # 命令
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
            
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

            # 强行还原材质
            if cacheObjs:
                self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()
            
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
                
            mc.file(save=1, force = 1)
            # 重打开FL文件
            mc.file(localFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            mc.file(save=1, force = 1)
            
            # 上传服务器处理
            if server == 1:
                #self.checkFinalLayoutUpdate()
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
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            # 上传服务器
            self.checkCacheLocalUpdate()
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
                self.sk_sceneGRPDelete('SET')
                self.sk_sceneGRPDelete('OTC')
                # 导出SET_GRP和OTC_GRP文件
                self.sk_sceneGRPExport('SET')
                self.sk_sceneGRPExport('OTC')
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
                
                # 新建文件之前处理好SET_GRP文件
                self.sk_sceneSETRefShaderReset([shotInfos[0],shotInfos[1],shotInfos[2]])
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
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
                self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
                print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')

            # 输出cache 及 anim
            if animExport:
                # 输出anim
                animObjs = self.checkAnimSetObjects()
                self.checkAnimCurveInfoExport(animObjs, server , cachePre)
                #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【输出】完毕=====================')

            # 输出cache
            if cacheExport:
                # 需要加入250分割处理
                # checkCacheSetObjects
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    self.checkCacheVStateExport(cacheObjs)
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    self.checkCacheSetCacheExport(cacheObjs, server ,cachePre , 1, 0)
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
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
                self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
                print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')

            # 成功代码
            return 0

    #------------------------------#
    # 【拆分】【重新导入数据】【后台】
    #------------------------------#

    # 重新载入数据
    def checkFinalLayoutImport(self, grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 ,server = 1):
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
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS')
            # frame
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame')
            
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
                            if obj[-1] == '_' and mc.listRelatives(obj, c= 1,type = 'mesh'):
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
                self.sk_sceneGRPImport('SET')
                self.sk_sceneGRPImport('OTC')
                print(u'=====================【Group】【服务器端】【导入】完毕=====================')
            
            # 创建asset
            if assetInfoImport:
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
                self.checkAnimCurveInfoImport(server)
                #print(unicode('=====================【Anim】【服务器端】【导入】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【导入】完毕=====================')

            # 输入cache
            if cacheImport:
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    #self.checkCacheSetCacheImport(cacheObjs, server)
                    self.sk_flCacheImportRefreshShaders(server)
                    # 导入显示隐藏信息
                    self.checkCacheVStateImport()
                    #print(unicode('=====================【Cache】【服务器端】【导入】完毕=====================', "utf8"))
                    print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                else:
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    
            # 载入hideInfo
            if hideInfoImport :
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
                    shape = mc.listRelatives(node, c=1, type='mesh')
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
            print u'=========未发现有效的[%]Set组========='%setType

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
    def checkCacheVStateExport(self , cacheObjs ):
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
            # 输出服务器端
            ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            self.checkFileWrite((ObjsVDataServerPath +  'cacheObjVInfo.txt'), resultData)
            return  resultData
        
    #------------------------------#
    # v信息导入
    def checkCacheVStateImport(self):
        vData = self.checkObjsVData()
        if vData:
            cacheObjs = vData.keys()
            for cacheObj in cacheObjs:
                keyInfo = vData[cacheObj]
                #print '-----'
                #print len(keyInfo)
                #print keyInfo
                # 单帧
                if len(keyInfo) == 1:
                    vState = keyInfo[0][0]
                    mc.setAttr((cacheObj + '.v'),vState)
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
    def checkObjsVData(self):
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
    def checkCleanDisplayLayers(self,layers = []):
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
    def checkCacheSetCacheExport(self, objsCache, serverFile=1 ,cachePre = 0 , refMode = 1 ,createType = 1):
        if objsCache:
            # 获取时间轴
            frameStart = mc.playbackOptions(q=1, min=1) 
            frameEnd = mc.playbackOptions(q=1, max=1) 
            mc.playbackOptions(min=frameStart - 51, max=frameEnd + 5)
            
            # 镜头信息
            dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'

            # mel用path
            localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
            # local_animPath___python用转mel
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')
    
            # 服务器端Cache及Anim路径
            # server_cachePath___mel用
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
                self.checkAnimCurveInfoExport(animVObjs, 0 , 'ca_animV')
            else:
                # 输出空信息
                self.checkAnimCurveInfoExport([], 0 , 'ca_animV')
            # 处理自身隐藏的
            if hideObjs:
                self.checkAnimCurveInfoExport(hideObjs, 0 , 'ca_hideV')
            else:
                # 输出空信息
                self.checkAnimCurveInfoExport([], 0, 'ca_hideV')
                
            
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
            if refMode == 1:
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

                if nsInfo:
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
            #self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            #self.checkCacheBakeTexAniFiles()
            
            
            # 上传cache及animPath
            #if serverFile == 1:
            #    self.checkCacheLocalUpdate()

    #------------------------------#
    # 【总篇】【经典Cache 本地|服务器端  导入】
    #------------------------------#
    # 导入cache，还原V动画，yes!
    # 需要细看共享节点
    # 增加从服务器读取功能
    def checkCacheSetCacheImport(self, objsCache, serverFile=1):      
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 5, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        
        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        # server端path
        if serverFile == 1:
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
                self.checkAnimCurveInfoImport(serverFile, 'ca_hideV')
            except:
                pass
            try:
                self.checkAnimCurveInfoImport(serverFile, 'ca_animV')
            except:
                pass

            # 公用cache
            mel.eval('zwOptimizeGeoCache();')
            
            # 打断所有连接
            #mel.eval('eyRenderRehyperShade')
            
            # 还原材质
            self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()

            # 上传cache
            
        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)


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
            mc.cacheFile(f = fileName ,singleCache = 1,dir = path , st = (frameStart+cachePre) , et = frameEnd ,points = objsShape)
        
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
    def checkCacheLocalUpdate(self):
        # 本地Cache及Anim路径
        # local_cachePath___mel用
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
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
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if mc.ls(obj) == []:
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    mesh = mc.listRelatives(obj,ni=1,type = 'mesh',c =1 )[0]
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
            self.checkCacheRecordMaterialExport(MatLists)
        return MatLists
        
    #------------------------------#
    # 【辅助】【还原材质】
    #------------------------------#
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport()
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)
       
    #------------------------------#
    # 【辅助】【材质信息备份到服务器端】【拆分用】
    #------------------------------#        
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
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
        serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo
            
    #------------------------------#
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#    
    # 输出材质信息
    def checkCacheRecordMaterialImport(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
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
    # 【辅助】【分拆用】FL文件更新cache
    #------------------------------#  
    # fl文件处理cache并保持更新材质
    def sk_flCacheImportRefreshShaders(self,server):
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
                    self.checkCacheSetCacheImport(cacheObjs, server)
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
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = ''):
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
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath()
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
        
    #------------------------------#   
    # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile):
        # 本地路径转mel用
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        fileInfo = infoFile + '_objs.txt'
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
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = ''):
        # 考虑下清理动画
        # 错误信息
        errorInfo = []
        # fsMode，指定路径读取
        if targetPath == '':
            # 本地获取
            if serverFile == 1:
                serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath()
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath()
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
    def sk_sceneGRPDelete(self, fileGRP='OTC'):
      
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        #fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileFomat = '.ma'
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
            mel.eval(cmd)
        else:
            fileFomat = '.mb'
            otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
            if os.path.exists(otcFileServer):
                cmd = 'zwSysFile(\"del\",\"' + otcFileServer + '\",\"\",1)'
                mel.eval(cmd)

    #------------------------------#
    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC' , server=1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        renderFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFile = renderFilePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        
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

        # 传至服务器
        if server:
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
            cmd = 'zwSysFile(\"copy\",\"' + otcFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
            
    #------------------------------#
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , info , serverModify = 1):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_set_render'
        
        if serverModify == 0:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()

        if serverModify == 1:
            needFilePath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()

        needSetFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
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
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
            otcFileServer = renderFilePathServer + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
            print otcFileServer
            cmd = 'zwSysFile(\"copy\",\"' + needSetFile + '\",\"' + otcFileServer + '\",1)'
            mel.eval(cmd)
        print u'====================SET_GRP更新完毕===================='

    #------------------------------#
    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC'):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        
        # ma文件利于文本读取改参考
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()    
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + fileGrpType + fileFomat
        
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
            
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有约束BK，确保动画及camera正确】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#  
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self):
        constraintsAll = mc.ls(type='constraint')
        
        #约束烘焙
        if  constraintsAll:
            tobake= []
            # 处理非参考的物体
            constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) == "transform" or mc.nodeType(obj) == "joint") and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            print shape 
                            print obj
                            if mc.nodeType(shape[0]) != 'camera':
                                plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)

            # 处理参考的_ct_an物体
            constraints = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) == "transform" or mc.nodeType(obj) == "joint") and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            if mc.nodeType(shape[0]) != 'camera':
                                if '_ct_an' in obj:
                                    plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            if '_ct_an' in obj:
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
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
                mc.delete(constraintTemp)
                # 重新约束物体
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                #locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    for i in range(len(locators)):
                        # 打断t和r属性
                        for attr in attrs:
                            #mel.eval('CBdeleteConnection \"' + tobake[i] + attr + '\"')
                            self.checkDeleteConnection(tobake[i] + attr)
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
                                mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                            if skipTranslateAxis == [] and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i])
                    # 二次烘焙
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

                    # 删除约束
                    constraints = [x for x in constraints if not mc.referenceQuery(x,inr=1)]
                    for cons in constraints:
                        ref = mc.referenceQuery(cons,isNodeReferenced = 1)
                        if not ref:
                            mc.delete(cons)
                    # 删除locators
                    mc.delete(locators)

                    print(u'========================【约束】【烘焙】【成功】========================')
                    print u'\n'
        else:
            print(u'========================【约束】【烘焙】【失败】========================')
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
                mc.character(destination , e = 1 ,rm = srcConn[0])
            
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
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
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        for i in range(len(fileContent)):
            if len(fileContent[i].split('\r\n')) > 1:
                temp = fileContent[i].split('\r\n')
                fileContent[i] = temp[0]
        return fileContent
    
    #------------------------------#
    # 写文件
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
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
        
