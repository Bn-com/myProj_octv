# -*- coding: utf-8 -*-

#Created on 2016
#author: 沈康

import maya.cmds as mc
import maya.mel as mel

import time

import os
class GDCAlembicCommon(object):
    def __init__(self):
        self.tempNs = '_foodTemp'
        self.tempBlend = 'foodBlend_'
        self.pointLimit = -4
        self.projFull = 'ShunLiu'
        self.shotType = 3
        self.fps = 25
        self.resW = 1280
        self.resH = 720
        self.fileFomat = '.mb'
        self.fileExt = 'mayaBinary'

    def testS(self,index):
        print '---------%s'%index
        tempObjs = mc.ls('*_s*:*',type = 'transform')
        if tempObjs:
            print tempObjs[0]

    #------------------------------#
    # 【通用】【FS后台工具】【核心】(改自Final工具）
    #  Author  : 韩虹
    #  Data    : 2015_03
    #  abcBy_ns 按asset模式输出
    #------------------------------#
    def GDC_FinaloutABC(self,server=1,cachePre=-12,shotType=2,shave=0,abcBy_ns = 0,replaceMode = 1,justCache = 0,bkMode = 1,printMode = 0):
        import os

        print '\n-------------All Start-------------'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport')
        # 关闭材质球更新
        mc.renderThumbnailUpdate(False)
        delGrps = ['goldLine_Grp']
        for delGrp in delGrps:
            if mc.ls(delGrp):
                mc.delete(delGrp)
        #---------------------------#
        # Setup 000  外部操作，
        #---------------------------#
        if printMode:self.testS('001')
        #---------------------------#
        # Setup 001  多级非参考的namespace清理。
        # 某些外包，喜欢做动作模板，然后import进来，这样形成了两级namespace，而在参考是不会记录import的那级参考。
        # 这种情况，要处理掉，不然后面记录参考信息时会出问题
        #---------------------------#
        # 处理非参考的namespace
        self.sk_sceneNoRefNamespaceClean()
                #---------------------------#
        # Setup 002  判断是否动画shot里的参考是否都有render 版本。如果没有，报错退出
        #---------------------------#
        # 检测参考是否正确，是否有render参考
        refInfos = self.checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]

        #---------------------------#
        # Setup 003  记录基本信息，修正时间轴
        #---------------------------#
        if printMode:self.testS('002')
        # 记录项目，场次，镜头号,文件类型
        shotInfos = self.checkShotInfo()
        shotType = self.shotType
        shotID = self.checkShotID()
        maType = 0
        fileFormat = self.fileFomat
        self.pTest(0)
        print u'\n'
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取FS临时路径
        localPath = self.alembicLocalPath(shotType)
        # 获取FS服务器端路径
        serverPath = self.alembicServerPath(shotType)

        # 本地另存
        shotName=''
        if shotType==2:
           shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType==3:
            shotName= shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        localFile = localPath + shotName+'_an_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        #---------------------------#
        # Setup 005  清理外包残留的playblast表达式
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'
        if printMode:self.testS('003')
        #---------------------------#
        # Setup 006  清理未勾选的参考，清理垃圾节点，更新camera，IKR再启动
        #---------------------------#
        self.sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================未勾选参考清理完毕========================'
        print u'\n'

        # 初步清理垃圾节点
        self.checkDonotNodeClean(unuse=1 , turtle=1)
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print u'\n'
        # 更新摄像机
        projectInfo = self.projFull
        camServerPath = 'Z:/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPath = camServerPath + shotName+ '_cam.ma'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        self.pTest(1)
        if printMode:self.testS('005')
        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        #预处理，约束清理
        startFrame = mc.playbackOptions(min=True,q=True)
        endFrame = mc.playbackOptions(max=True,q=True)
        print '-------------bkStart'
        print mc.playbackOptions(min=True,q=True)
        print mc.playbackOptions(max=True,q=True)
        if bkMode:
            self.sk_checkBakeConstraints()
        print '-------------bkEnd'
        print mc.playbackOptions(min=True,q=True)
        print mc.playbackOptions(max=True,q=True)
        print(u'========================【约束】【烘焙】【成功】========================')
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('006')
        #---------------------------#
        # Setup 008 清除服务器data目录残留的SET和OTC文件
        # 【注意】 如果有SD环节，酌情清理OTC，SET需要从服务器端参考
        #---------------------------#
        # 非参考物体清理
        self.sk_sceneNotRefMeshClean()

        # 清理服务器端旧的SET和OTC文件
        self.sk_sceneGRPDelete('SET')
        self.sk_sceneGRPDelete('OTC')

        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        self.sk_sceneReorganize(0)
        # 记录OTC里的参考
        otcRefList = self.otcRefCheck()
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print u'\n'
        if printMode:self.testS('007')
        #---------------------------#
        # Setup 010 动画文件内，隐藏的物体，记录下来，cache之后恢复隐藏
        #---------------------------#
        unDisplayLayerObjs = self.sk_FL_RefHideObjsRecord(server=1,shotType=shotType)
        # 记录cacheDict
        cacheDict = {}
        yetiNodes = mc.ls(type = 'pgYetiMaya')
        for checkNode in yetiNodes:
            attrKey = 'cacheFileName'
            cachePath = mc.getAttr('%s.%s'%(checkNode,attrKey))
            if not cachePath:
                continue
            cacheDict[checkNode] = [attrKey,cachePath]
        if printMode:self.testS('008')
        #---------------------------#
        # Setup 011 获取anim shot的参考信息
        #---------------------------#
        # 获取references信息
        refInfos = self.checkReferenceListInfo()
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
        self.sk_sceneGRPExport('SET',server,shotType,[])
        self.sk_sceneGRPExport('OTC',server,shotType,otcRefList)

        self.pTest(2)
        print u'\n'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'
        if printMode:self.testS('009')
        #---------------------------#
        # Setup 015 删除set参考，加快速度
        #---------------------------#
        # 首先删除set参考，加快速度
        '''
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        '''
        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'

        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        # 判断是否ms_anim文件
        if shotType==2 and shotInfos[3] in ['an','sa','dy']:
            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================line3205')
            print u'\n'
        if shotType==3 and shotInfos[4] in ['an','sa','dy']:

            if refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================line3224')
            print u'\n'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        self.pTest(3)
        if printMode:self.testS('010')
        #---------------------------#
        # Setup 016 输出cache，以及传递动画的控制器动画
        # cache过程中，加入了对隐藏|组K帧物体的检测，记录显示隐藏动画以便还原
        #---------------------------#
        # 特告梁宇:由于你不是选组导出的cache,而是按物体选的导出，而设置是用组约束的显示隐藏，因此物体根本不能通过abc继承显示隐藏！
        #---------------------------#
        # 输出显示隐藏动画信息
        self.checkCacheVStateExport([],shotType )
        print u'\n'
        print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
        print u'\n'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 输出ABC
        self.pTest(3)
        if shotInfos[0] not in ['mi']:
            self.abc_AttrAdd()
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            # 输出cache
            # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
            if abcBy_ns:
                self.checkAbcCacheExport(cacheObjs,server=server,exportType='mesh',cachePre=-50,step=1)
            print u'\n'
            print(u'=====================【alembic】【服务器端】【输出】完毕=====================')
            print u'\n'
        else:
            print u'\n'
            print(u'=====================【alembic】无物体！！！！！！=====================')
            print u'\n'
        self.pTest(3)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('011')
        curveObjs= self.GDC_shaveInfo(3,'abc_curve')
        if shave and curveObjs:
            if  abcBy_ns:
                self.checkAbcCacheExport(curveObjs,server=server,exportType='abc_curve',cachePre=-50,step=1)
            print u'\n'
            print(u'=====================【abc_curve】【服务器端】【输出】完毕=====================')
            print u'\n'
        else:
            print u'\n'
            print (u'=====================【abc_curve】无物体！！！！！或 不需要输出curve 的abc 缓存==========================')
            print u'\n'
        self.pTest(4)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        if justCache:
            return
        #---------------------------#
        # Setup 017 对动画文件的处理告一段落，这里处理SET和OTC里面的参考替换，同时清理参考材质覆盖
        #---------------------------#
        # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
        self.sk_sceneSETRefShaderReset(shotInfos,serverModify = 1 , shotType =shotType)
        if printMode:self.testS('012')
        #---------------------------#
        # Setup 018 开始新文件的架构
        #---------------------------#
        # 新建文件,临时文件夹另存
        mc.file(f=1, new=1)
        # 关闭材质球更新
        mc.renderThumbnailUpdate(False)
        print '\n'
        print '[Ref Info]'
        print refInfos[0][0]
        print '\n'
        print(u'=========================【创建新文件】=========================')
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        print '\n'
        if printMode:self.testS('015')
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
        self.sk_sceneGRPImport('SET',shotType)
        self.sk_sceneGRPImport('OTC',shotType)
        print u'\n'
        print(u'=====================【Group】【服务器端】【导入】完毕=====================')
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('016')
        #---------------------------#
        # Setup 020 加载需要的角色和道具类的render参考
        #---------------------------#
        # 导入reference及share nodes（新导入场景，后导入参考）
        self.sk_FLRefRebuild(refInfos,noNeedRefNodeInfo)
        self.pTest(5)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机
        self.camServerReference(info=shotType)
        if printMode:self.testS('017')
        # Setup 022 新建后的文件大组重新处理
        #---------------------------#
        # 处理大组
        self.sk_sceneReorganize(1)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        #---------------------------#
        # Setup 023 动画文件和fl文件的cache list对比，不一致则报错。
        # 这里不一致一般在两种情况里发生
        # 1,anim文件和render文件cache list不一致;
        # 2.约束bake失败，某些CHR和PROP和SET有约束残留，导出去的时候CHR,PROP进了SET文件，而SET文件是默认不加载的，丢失部分cacheList
        #---------------------------#
        # 检测cache物体列表
        '''
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
        '''
        # 场景搭建完毕
        # 备份材质

        MatLists = self.checkCacheRecordMaterial(finalLayout=1,shotType = shotType)
        if printMode:self.testS('018')
        self.pTest(6)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        # 处理buging
        # 载入cache及自带的anim
        if shotInfos[0] not in ['mi']:
            self.abc_AttrAdd()
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            self.GDC_alembicImp('fs',1,shotType = shotType,abcBy_ns = abcBy_ns,replaceMode = replaceMode)
            print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
            if abcBy_ns:
                self.assetAbcRebuild('mesh',shotID,server)
            else:
                #mesh abc按replace方式进行连接  梁宇
                if projectInfo in ['North','MiniTiger']:
                    self.LY_alembicMeshImp()
            # 处理还原物体
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

        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('019')
        if shave==1:
            curveObjs=self.GDC_shaveInfo(3,'abc_curve')
            if curveObjs:
                if not abcBy_ns:
                    mc.select(curveObjs)
                self.GDC_curvealembicImp(1,shotType = shotType,abcBy_ns = abcBy_ns)
                if abcBy_ns:
                    self.assetAbcRebuild('curve',shotID,server)
                else:
                    #曲线abc按replace方式进行连接  梁宇
                    if projectInfo in ['North','MiniTiger']:
                        self.LY_alembicCurveImp()
                # rebuild
                for checkCurve in curveObjs:
                    mc.rebuildCurve(checkCurve,ch =1,rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,s=0,d=3,tol=0.01)
                print u'\n'
                print(u'=====================【abc_curve】【服务器端】【导入】完毕=====================')
                print u'\n'
            else:
                print u'\n'
                print(u'=====================【abc_curve】无物体！！！！！！=====================')
                print u'\n'
        if printMode:self.testS('020')
        # 清理非参考namespace
        self.sk_sceneNoRefNamespaceClean()
        # renderState fix
        self.checkRenderStateRebuild()

        self.pTest(7)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        # 还原cache属性
        cacheNodes = cacheDict.keys()
        for checkNode in cacheNodes:
            attrKey = cacheDict[checkNode][0]
            cachePath = cacheDict[checkNode][1]
            objType = mc.nodeType(checkNode)
            mc.setAttr('%s.%s'%(checkNode,attrKey),cachePath,type = 'string')
            if objType in ['pgYetiMaya']:
                mc.setAttr('%s.%s'%(checkNode,'fileMode'),2)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('021')
        # 处理显示层相关物体
        if unDisplayLayerObjs:
            hideObjs = []
            for obj in unDisplayLayerObjs:
                if mc.ls(obj):
                    hideObjs.append(obj)
            # 放到norender层
            if hideObjs:
                disLayers = mc.ls(type = 'displayLayer')
                norenderState = 0
                norenderLayer = 'norender'
                for checkLayer in disLayers:
                    if checkLayer.lower() in [norenderLayer]:
                        norenderState = 1
                        norenderLayer = checkLayer
                if not norenderState:
                    mc.createDisplayLayer(empty = 1, name = norenderLayer)
                mc.setAttr('%s.visibility'%norenderLayer,0)
                mc.editDisplayLayerMembers(norenderLayer,hideObjs , nr = 1)
        print u'\n'
        print(u'=====================【Displayer】隐藏恢复=====================')
        print u'\n'
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        self.pTest(8)

        # 清理未知节点
        self.checkDonotNodeCleanBase(0)
        if printMode:self.testS('022')
        # 强行还原材质
        returnMaterialMode = 0
        if shotInfos[0] in ['LION']:
            returnMaterialMode = 1
        if returnMaterialMode:
            self.checkCacheReturnMaterial(MatLists,finalLayout = 1, shotType = shotType)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        self.pTest(9)

        #---------------------------#
        # Setup 025 备份FL文件
        #---------------------------#
        # 本地保存
        fileTypeFull = self.fileExt
        mc.file(force=1, options="v=0", type=fileTypeFull , save=1)

        # 设置时间轴等消息
        # 命令
        shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
        if shotType == 3:
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('023')
        #---------------------------#
        # Setup 026 镜头信息，时间轴信息处理
        #---------------------------#
        # 开始处理
        fpsFrame = self.fps
        resW = self.resW
        resH = self.resH
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
        mc.currentTime(startFrame)
        if printMode:self.testS('025')
        # 允许undo
        mc.undoInfo(state=True, infinity=True)

        description = 'FinalLayout Base File'

        # 烘焙表情贴图
        self.checkCacheBakeTexAniFiles()

        # 属性处理
        self.csl_setattr(attrtype='aiStandIn',attr='visibility',num=1)

        # 导入显示隐藏信息,必须放这，不然会被帧初始化干掉时间轴
        self.checkCacheVStateImport(shotType)
        self.pTest(10)

        mc.file(save=1, force = 1)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'

        #---------------------------#
        # Setup 029
        # 清理所有asset 材质连接
        # 由于之前还原了材质，asset的reference
        # edit列表里会有记录，需要在没加载参考的情况下清理
        #---------------------------#
        self.pTest(11)
        if printMode:self.testS('026')
        # 缺少check in baseFile
        mc.sysFile((localPath + shotName+'_an_c001' + fileFormat),delete=True)
        print '\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2],shotInfos[3]))
        print(u'=====================【%s】文件处理完毕=====================CHECKMARK1'%(localPath + shotName+'_base_fs_c001' + fileFormat))

        #---------------------------#
        # Setup 030 本地备份之后，check in
        #---------------------------#
        # 上传服务器处理

        if server == 1:
            print '\n---------FilePath'
            print mc.file(exn=1,q=1)
            print '\n'
        self.pTest(12)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if printMode:self.testS('027')
        #批处理器强制关闭，到下个任务
        # 缺少check in baseFile
        print u'\n'
        print(u'=========================================================================')
        print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))

    # 数据断句测试
    def pTest(self,value):
        # 获取时间轴
        #print '------%s'%(str(value))
        pass

    #-----------------------------#
    # abc 导出
    # #选中版
    #-----------------------------#
    def checkAbcCacheExport(self,objsCache, server = 1,exportType = 'mesh' ,cachePre = 0 ,step = 1 ):
        if not objsCache:
            return
        print '-----Abc001'
        print mc.pluginInfo('AbcExport',loaded = 1,q = 1)
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport')
        print '-----Abc002'
        print mc.pluginInfo('AbcExport',loaded = 1,q = 1)
        nsObjs = {}
        for checkObj in objsCache:
            ns = checkObj.split('|')[-1].split(':')[0]
            if ns not in nsObjs.keys():
                nsObjs[ns] = [checkObj]
            else:
                nsObjs[ns].append(checkObj)

        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)

        shotID = self.checkShotID()

        localPath  = self.checkShotDataInfoPath(server = 0,infoMode = 2.5)
        serverPath = self.checkShotDataInfoPath(server = 1,infoMode = 2.5)
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
            if os.path.exists(abcLocalPath):
                mc.sysFile(abcLocalPath,delete = 1)
            print abcLocalPath
            rootObjs = ''
            for obj in needObjs:
                rootObjs = rootObjs + ' -root ' + mc.ls(obj,l=1)[0]
            cacheCMD = 'AbcExport -verbose -j \"-frameRange ' + str(frameStart+cachePre)  + ' ' + str(frameEnd) + ' -step ' + str(step) + ' -uvWrite -worldSpace -writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath + '\"'
            mel.eval(cacheCMD)
            fileList.append([(localPath + abcFile),(serverPath + abcFile)])
        if server:
            for info in fileList:
                mc.sysFile(info[0],copy = info[1])
                print '--------------abcFile'
                print info[0]
                print info[1]
        else:
            print '--------------localFile'
            print localPath


    # nsList指定输出
    def checkAbcCacheExportByNs(self,needTypes = ['c','p'],checkNsList = [],server=1,exportType = 'mesh',st = 0,et = 0,step = 1,bkMode = 1):
        # 处理大组
        self.sk_sceneReorganize(0)
        # 约束
        if bkMode:
            self.sk_checkBakeConstraints()
        objsCache = self.GDC_alembicInfo(3)
        if exportType in ['curve']:
            objsCache = self.GDC_shaveInfo(3,'abc_curve')
        nsObjs = {}
        for checkObj in objsCache:
            ns = checkObj.split('|')[-1].split(':')[0]
            if checkNsList and ns not in checkNsList:
                continue
            if ns.split('_')[1][0].lower() not in needTypes:
                continue
            if ns not in nsObjs.keys():
                nsObjs[ns] = [checkObj]
            else:
                nsObjs[ns].append(checkObj)

        if not st:
            st = mc.playbackOptions(q=1, min=1)
        if not et:
            et = mc.playbackOptions(q=1, max=1)

        frameStart = st
        frameEnd = et

        shotID = self.shotType

        localPath  = self.checkShotDataInfoPath(server = 0,infoMode = 2.5)
        serverPath = self.checkShotDataInfoPath(server = 1,infoMode = 2.5)
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
            if os.path.exists(abcLocalPath):
                mc.sysFile(abcLocalPath,delete = 1)
            print abcLocalPath
            rootObjs = ''
            for obj in needObjs:
                rootObjs = rootObjs + ' -root ' + mc.ls(obj,l=1)[0]
            cacheCMD = 'AbcExport -verbose -j \"-frameRange ' + str(frameStart)  + ' ' + str(frameEnd) + ' -step ' + str(step) + ' -uvWrite -worldSpace -writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath + '\"'
            mel.eval(cacheCMD)
            fileList.append([(localPath + abcFile),(serverPath + abcFile)])
        if server:
            for info in fileList:
                mc.sysFile(info[0],copy=info[1])
                print '--------------abcFile'
                print info[0]
                print info[1]
        else:
            print '--------------localFile'
            print localPath

    #---------------------------------------------------------#
    # asset abc replace  沈康 2016.4
    # 本来是万能型，但是要匹配finallayout主体分为mesh和nurbs，故加参数,extra
    def assetAbcRebuild(self,checkType = 'mesh',shotName = '',server = 1,clean = 1,printMode = 0):
        nsList = self.getNsListOfFile()
        errorList = []
        for ns in nsList:
            print '\n' + '[%s:Start]'%ns + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
            abcNode = '%s_%s_alembic_AlembicNode'%(shotName,ns)
            if checkType in ['curve']:
                abcNode = '%s_%s_abc_curve_AlembicNode'%(shotName,ns)
            if checkType in ['extra']:
                abcNode = '%s_%s_extra_AlembicNode'%(shotName,ns)
            errorList = errorList + self.replaceRebuildPerform(checkAbcNode=abcNode,checkType=checkType,checkNs=ns,clean=clean,printMode=printMode)
            print '\n' + '[%s:End]'%ns + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 记录
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        self.checkAbcConnectInfoExport(server)
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 清理blend
        #self.checkCacheCleanBlendShapes()
        print '\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if errorList:
            print '---------------BlendErrorList'
            for errorObj in errorList:
                print errorObj
            print u'-----------请检查以上物体,anim和render不匹配-----------'
            #mc.error()
        self.sk_fixShapeRenderStateAttrs()

    #------------------------------#
    # 【辅助】修正deformerShape 的 renderState
    #------------------------------#
    def sk_fixShapeRenderStateAttrs(self):
        meshes = mc.ls(type = 'mesh',l=1)
        checkObjs = mc.listRelatives(meshes,p=1,f=1)
        for checkObj in checkObjs:
            meshList = mc.listRelatives(checkObj,s=1,type = 'mesh',f=1)
            if len(meshList) == 1:
                continue
            renderMesh = mc.listRelatives(checkObj,ni=1,s=1,type = 'mesh',f=1)[0]
            inrState = mc.referenceQuery(renderMesh,inr=1)
            if inrState:
                continue
            for checkMesh in meshList:
                inr = mc.referenceQuery(checkMesh,inr=1)
                if not inr:
                    continue
                self.sk_attrGo(checkMesh,renderMesh)

    def sk_attrGo(self,source,target):
        attrList = ['castsShadows','receiveShadows','motionBlur','primaryVisibility','smoothShading','visibleInReflections','visibleInRefractions','doubleSided','aiSelfShadows','aiOpaque','aiVisibleInDiffuse','aiVisibleInGlossy','aiMatte']
        for checkAttr in attrList:
            mc.setAttr('%s.%s'%(target,checkAttr),mc.getAttr('%s.%s'%(source,checkAttr)))

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

    #--------------------------------------#
    def getNsListOfFile(self):
        refNodes = mc.ls(type = 'reference')
        nsList = []
        for checkRef in refNodes:
            try:
                checkNs = mc.referenceQuery(checkRef,namespace=1).split(':')[-1]
                nsList.append(checkNs)
            except:
                pass
        return nsList

    #--------------------------------------#
    # 重连模式
    def replaceRebuildPerform(self,checkAbcNode = '',checkType= 'mesh',checkNs = '',clean = 1,printMode = 0):
        #if checkType not in ['mesh'] and not mc.ls(checkAbcNode):
        #    print mc.ls(checkAbcNode)
        #    return []
        print '---------abcRebuild'
        print checkAbcNode
        print checkNs
        testMode = 1
        abcNS = checkNs+self.tempNs
        # replace模式下没有连接状态的物体
        nsStaticAbcObjs  = self.getNoConsAbcObj(checkType,abcNS)
        if printMode:print '----------nsStaticAbcObjs'
        if printMode:print nsStaticAbcObjs
        # 参考状态的asset物体列表
        sourceObjsInfo = self.getShotAssetAbcObj(checkType,checkNs)
        sourceObjs = sourceObjsInfo[0]
        sourceObjsDict = sourceObjsInfo[1]
        if printMode:print '----------sourceObjsDict'
        if printMode:print sourceObjsDict
        errorObjs = []
        if printMode:print '\n' + '[%s:001]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # replace模式下的非参考物体列表
        abcObjsInfo  = self.getReplaceAbcObj(checkType,abcNS,checkAbcNode)
        abcObjs = abcObjsInfo[0]
        abcObjsDict = abcObjsInfo[1]
        if printMode:print '----------abcObjsDict'
        if printMode:print abcObjsDict
        #--------------------------------------#
        # 处理显示隐藏,给maya bug擦屁股,隐藏物体无法做blend,显示后可以
        nsObjs = mc.ls('%s:*'%checkNs,l=1)
        sourceVDict = self.blendSetVOn(nsObjs)
        abcVDict = self.blendSetVOn(abcObjs)
        #--------------------------------------#
        # 检测不匹配情况,视情况做blendShape
        if len(sourceObjsDict.keys()) != (len(abcObjsDict.keys()) + len(nsStaticAbcObjs)):
            for checkObj in abcObjsDict.keys():
                if checkObj not in sourceObjsDict.keys():
                    errorObjs = errorObjs + abcObjsDict[checkObj]
            for checkObj in sourceObjsDict.keys():
                if checkObj not in abcObjsDict.keys():
                    errorObjs = errorObjs + sourceObjsDict[checkObj]
            if errorObjs:
                errorObjs = list(set(errorObjs))
        if printMode:print '\n' + '[%s:002]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        #--------------------------------------#
        # 处理基础位移,只有MODEL组外的曲线没有去做对比检测
        for checkKey in sourceObjsDict.keys():
            if checkKey not in abcObjsDict.keys():
                continue
            fileGrp = sourceObjsDict[checkKey][0]
            abcGrp  = abcObjsDict[checkKey][0]
            if checkType in ['curve']:
                # 坐标
                self.checkSamePosition(abcGrp,fileGrp)
            if checkType in ['mesh']:
                # blend形变
                shapeS = mc.listRelatives(abcGrp,s=1,ni=1,f=1)
                shapeT = mc.listRelatives(fileGrp,s=1,ni=1,f=1)
                if not shapeS or not shapeT:
                    continue
                # 若有blend连接，删除
                blendCons = mc.listConnections(shapeT,s=1,d=0,type='blendShape')
                if blendCons:
                    mc.delete(blendCons)
                self.singleFrameCacheBlendConfig(abcGrp,fileGrp,checkType,blendPre = self.tempBlend)
        #--------------------------------------#
        # attrlist
        if mc.ls(checkAbcNode):
            abcConsObjsAttrList= mc.listConnections(checkAbcNode,d=1,plugs=1)
            abcConsObjsAttrList.remove('time1.outTime')
        else:
            abcConsObjsAttrList = []
        abcConsObjsAttrDict = dict()
        tempAttrList = []
        tempObjs =  []
        for abcObjAttr in abcConsObjsAttrList:
            if 'hyperLayout' in abcObjAttr:
                continue
            checkObj = abcObjAttr.split('.')[0]
            inr = mc.referenceQuery(checkObj,inr = 1)
            if inr:
                continue
            tempAttrList.append(abcObjAttr)
            if checkObj not in tempObjs:
                tempObjs.append(checkObj)
            # 根源物体
            checkObjT = abcObjAttr.split('.')[0]
            checkNodeType = mc.nodeType(checkObjT)
            if checkNodeType not in ['transform']:
                if checkNodeType in ['unitConversion']:
                    # 获取下游物体
                    checkObjT = mc.listConnections(checkObjT,s=0,d=1)[0]
                else:
                    checkObjT = mc.listRelatives(checkObjT,p=1,type='transform',f=1)[0].split('|')[-1]
            if '|' in checkObjT:
                checkObjT = checkObjT.split('|')[-1]
            if self.tempNs in checkObjT:
                checkObjT = checkObjT.replace(self.tempNs,'')
            if checkObjT not in abcConsObjsAttrDict.keys():
                abcConsObjsAttrDict[checkObjT] = [abcObjAttr]
            else:
                if abcObjAttr not in abcConsObjsAttrDict[checkObjT]:
                    abcConsObjsAttrDict[checkObjT] = abcConsObjsAttrDict[checkObjT] + [abcObjAttr]
        # abc节点连接下的所有链接属性
        abcConsObjsAttrList = tempAttrList
        # abc节点下连接的物体数量
        abcConsObjs = tempObjs

        if printMode:print '\n' + '[%s:003]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if checkType in ['mesh','curve']:
            print '-------objList'
            print checkNs
            print '[%s]   [%s]'%(str(len(sourceObjs)),'sourceObjs')
            print '[%s]   [%s]'%(str(len(sourceObjsDict.keys())),'sourceObjsKeyList')
            #print sourceObjs
            print '[%s]   [%s]'%(str(len(abcObjs)),'abcObjs')
            print '[%s]   [%s]'%(str(len(abcObjsDict.keys())),'abcObjsKeyList')
            #print abcObjs
            print '[%s]   [%s]'%(str(len(abcConsObjs)),'abcConsObjs')
            #print abcConsObjs
            print '[%s]   [%s]'%(str(len(abcConsObjsAttrList)),'abcConsObjsAttrList')
            print '[%s]   [%s]'%(str(len(abcConsObjsAttrDict.keys())),'abcConsObjsAttrKeyList')
            #print abcConsObjsAttrList
            print '[%s]   [%s]'%(str(len(nsStaticAbcObjs)),'nsStaticAbcObjs')
            #print nsStaticAbcObjs
            for checkObjS in abcObjs:
                checkType = mc.nodeType(checkObjS)
                if checkType not in ['transform']:
                    checkKeyS = mc.listRelatives(checkObjS,p=1,type='transform',f=1)[0].split('|')[-1]
                else:
                    checkKeyS = checkObjS.split('|')[-1]
                if '|' in checkKeyS:
                    checkKeyS = checkObjS.split('|')[-1]
                if self.tempNs in checkKeyS:
                    checkKeyS = checkKeyS.replace(self.tempNs,'')
                if (checkKeyS not in abcConsObjsAttrDict.keys()) and (checkObjS not in errorObjs):
                    if printMode:print '----------showKey\n%s'%abcConsObjsAttrDict.keys()
                    errorObjs.append(checkObjS)

        if errorObjs:
            print '---------------------uTestGrpsCheck'
            print len(errorObjs)
            for errorObj in errorObjs:
                print errorObj
            if not testMode:
                mc.error()

        if printMode:print '\n' + '[%s:005]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 正式处理
        fixedObjs  = []
        # 变形情况
        deformInfos = []
        # 位移直接连接情况
        transInfos  = []
        # 只断,不连(rebuild使用)
        unitInfos   = []
        usedNodes   = ['unitConversion']
        for abcObjAttr in abcConsObjsAttrList:
            # 源 mesh 连接属性
            abcObjAttr = mc.ls(abcObjAttr,l=1)[0]
            nodeType = mc.nodeType(abcObjAttr[:-1*(1+len(abcObjAttr.split('.')[-1]))])
            # abc节点连接信息
            abcSAttr = mc.listConnections(abcObjAttr,s = 1,type = 'AlembicNode',plugs=1)
            if not abcSAttr:
                continue
            abcSAttr = abcSAttr[0]
            abcObj = abcObjAttr.split('.')[0].split('|')[-1]
            if nodeType in ['mesh','nurbsCurve']:
                abcObj = mc.listRelatives(abcObjAttr.split('.')[0],p=1,type='transform')[0]
            if nodeType in ['transform']:
                abcObj = abcObjAttr.split('.')[0]
            if nodeType in ['unitConversion']:
                abcObj = mc.listConnections(abcObjAttr.split('.')[0],s=0,d=1)[0]
            checkAbcKey = abcObj
            if '|' in checkAbcKey:
                checkAbcKey = checkAbcKey.split('|')[-1]
            if self.tempNs in checkAbcKey:
                checkAbcKey = checkAbcKey.replace(self.tempNs,'')
            needCheckObj = ''
            if checkAbcKey in sourceObjsDict.keys():
                needCheckList = sourceObjsDict[checkAbcKey]
                needCheckObj = needCheckList[0]
            # 没加属性的物体来查询
            else:
                tempObjs = mc.ls('%s*'%checkAbcKey,type = 'transform',l=1)
                for tempObj in tempObjs:
                    inr = mc.referenceQuery(tempObj,inr=1)
                    if not inr:
                        continue
                    if 'Constraint' in tempObj:
                        continue
                    needCheckObj = tempObj
            if not needCheckObj:
                errorObjs.append(abcObj)
                continue
            # 对polygon物体而言,shape节点已经不同名
            # 需要处理既有.inMesh也有属性连接的状况
            if '.inMesh' in abcObjAttr or '.create' in abcObjAttr:
                targetShape = mc.listRelatives(needCheckObj,s=1,ni=1,f=1)[0]
                targetInfo = ''
                if '.inMesh' in abcObjAttr:
                    targetInfo = '%s.inMesh'%(targetShape)
                if '.create' in abcObjAttr:
                    targetInfo = '%s.create'%(targetShape)
                deformInfos.append([abcSAttr,abcObjAttr,targetInfo])
            else:
                if nodeType in usedNodes:
                    nextNodeAttr = mc.listConnections(abcObjAttr.split('.')[0],s=0,d=1,plugs=1)
                    if not nextNodeAttr:
                        print '-----------abcAttrError'
                        print abcObjAttr
                        continue
                    nextNodeAttr = nextNodeAttr[0]
                    targetInfo = '%s.%s'%(needCheckObj,nextNodeAttr.split('.')[-1])
                    unitInfos.append(([abcSAttr,abcObjAttr]))
                else:
                    targetInfo = '%s.%s'%(needCheckObj,abcObjAttr.split('.')[-1])
                transInfos.append([abcSAttr,abcObjAttr,targetInfo])
            fixedObjs.append(abcObjAttr.split('.')[0])

        if printMode:print '\n' + '[%s:006]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 处理deform
        for infos in deformInfos:
            abcSAttr = infos[0]
            abcObjAttr = infos[1]
            needInfo = infos[2]
            # 某些特殊情况可在这里不处理
            #mc.disconnectAttr(abcSAttr,abcObjAttr)
            cons = mc.listConnections(needInfo,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],needInfo)
            mc.connectAttr(abcSAttr,needInfo,f=1)

        if printMode:print '\n' + '[%s:007]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 处理transP
        for infos in  transInfos:
            abcSAttr = infos[0]
            abcObjAttr = infos[1]
            needInfo = infos[2]
            #mc.disconnectAttr(abcSAttr,abcObjAttr)
            cons = mc.listConnections(needInfo,s=1,d=0,plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],needInfo)
            mc.connectAttr(abcSAttr,needInfo,f=1)

        if printMode:print '\n' + '[%s:008]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # 处理 unitInfos
        for infos in unitInfos:
            abcSAttr = infos[0]
            abcObjAttr = infos[1]
            mc.disconnectAttr(abcSAttr,abcObjAttr)
            #mc.connectAttr(abcSAttr,abcObjAttr,f=1)
            unitNode = abcObjAttr.split('.')[0]
            if mc.ls(unitNode):
                mc.delete(unitNode)

        if printMode:print '\n' + '[%s:009]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # blend弥补 单帧物体
        if nsStaticAbcObjs:
            for checkObj in nsStaticAbcObjs:
                # 获取物体
                targetObj = ''
                checkTempKey = checkObj.split('|')[-1]
                if self.tempNs in checkTempKey:
                    checkTempKey = checkTempKey.replace(self.tempNs,'')
                allObjs = mc.ls('*%s*'%checkTempKey,l=1,type = 'transform')
                for temp in allObjs:
                    inr = mc.referenceQuery(temp,inr=1)
                    if not inr:
                        continue
                    if checkTempKey != temp.split('|')[-1]:
                        continue
                    targetObj = temp
                if not targetObj:
                    errorObjs.append(checkObj)
                    continue
                # 位移
                self.checkSamePivot(checkObj,targetObj)
                # blend
                shapeS = mc.listRelatives(checkObj,s=1,ni=1,f=1)
                shapeT = mc.listRelatives(targetObj,s=1,ni=1,f=1)
                if not shapeS or not shapeT:
                    continue
                # 若有blend连接，删除
                blendCons = mc.listConnections(shapeT,s=1,d=0,type='blendShape')
                if blendCons:
                    mc.delete(blendCons)
                self.singleFrameCacheBlendConfig(checkObj,targetObj,checkType)
        # 处理显示隐藏
        self.blendSetVOff(sourceVDict)
        self.blendSetVOff(abcVDict)
        # 收尾
        if printMode:print '\n' + '[%s:010]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if abcObjs and clean:
            mc.delete(abcObjs)
        if printMode:print '\n' + '[%s:011]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        if nsStaticAbcObjs and clean:
            mc.delete(nsStaticAbcObjs)
        return errorObjs

    #--------------------------------------#
    # blend之前显示隐藏处理
    def blendSetVOn(self,checkOjs):
        vDict = {}
        for checkObj in checkOjs:
            checkAttr = checkObj+'.v'
            if not mc.ls(checkAttr):
                continue
            try:
                vValue = mc.getAttr(checkAttr)
            except:
                continue
            vDict[checkObj] = vValue
            if vValue:
                continue
            try:
                mc.setAttr(checkAttr,1)
            except:
                pass
        return vDict

    # 还原显示属性
    def blendSetVOff(self,vDIct):
        checkOjs = vDIct.keys()
        for checkObj in checkOjs:
            vValue = vDIct[checkObj]
            if vValue:
                continue
            try:
                mc.setAttr((checkObj+'.v'),vValue)
            except:
                pass

    #--------------------------------------#
    # 获取指定asset的abc属性物体
    def getShotAssetAbcObj(self,checkType = 'mesh',checkNs=''):
        needObjsDict = dict()
        checkObjs = []
        needObjs = []
        if not checkObjs:
            if checkNs:
                checkObjs = mc.ls('%s:*'%checkNs,type = 'transform',l=1)
            else:
                checkObjs = mc.ls('*:*',type = 'transform',l=1)
        attrKey = 'alembic'
        if checkType in ['curve']:
            attrKey ='abc_curve'
        for checkObj in checkObjs:
            inr = mc.referenceQuery(checkObj,inr=1)
            if not inr:
                continue
            if checkType in ['mesh','curve'] and (not mc.ls('%s.%s'%(checkObj,attrKey))):
                continue
            needObjs.append(checkObj)
            objKey = checkObj.split('|')[-1]
            if objKey not in needObjsDict.keys():
                needObjsDict[objKey] = [checkObj]
            else:
                if checkObj in needObjsDict[objKey]:
                    continue
                needObjsDict[objKey] = needObjsDict[objKey] + [checkObj]
        return [needObjs,needObjsDict]


    #--------------------------------------#
    # replace模式的abc物体
    def getReplaceAbcObj(self,checkType = 'mesh',checkNs = '',abcNode  = ''):
        needObjsDict = dict()
        checkObjs = []
        needObjs = []
        if checkType in ['extra']:
            grps = mc.ls('%s:*'%checkNs,type = 'transform',l=1)
            for checkGrp in grps:
                inr = mc.referenceQuery(checkGrp,inr=1)
                if inr:
                    continue
                if len(checkGrp.split('|')) !=2:
                    continue
                checkObjs.append(checkGrp)
        if not checkObjs:
            if checkNs:
                checkObjs = mc.ls('%s:*'%checkNs,type = 'transform',l=1)
            else:
                checkObjs = mc.ls('*:*',type = 'transform',l=1)
            #checkObjs = mc.listRelatives(checkObjs,p=1,type='transform',f=1)
        abcKey = 'alembic'
        if checkType in ['curve']:
            abcKey = 'abc_curve'
        for checkObj in checkObjs:
            inr = mc.referenceQuery(checkObj,inr=1)
            if inr:
                continue
            if checkType in ['mesh','curve']:
                if mc.ls('%s.%s'%(checkObj,abcKey)):
                    continue
            if len(checkObj.split('|')) !=2:
                continue
            # 和指定abc连接
            consState = self.checkAbcConsState(checkObj,abcNode)
            if not consState:
                continue
            needObjs.append(checkObj)
            objKey = checkObj.split('|')[-1]
            if self.tempNs in objKey:
                objKey = objKey.replace(self.tempNs,'')
            if objKey not in needObjsDict.keys():
                needObjsDict[objKey] = [checkObj]
            else:
                if checkObj in needObjsDict[objKey]:
                    continue
                needObjsDict[objKey] = needObjsDict[objKey] + [checkObj]
        return [needObjs,needObjsDict]

    #--------------------------------------#
    # 判断有没有指定abc节点连接
    def checkAbcConsState(self,checkObj,abcNode):
        consState = 0
        nodeCons = mc.listConnections(checkObj,s=1,d=0)
        if not nodeCons:
            nodeCons = []
        shapeCons = []
        shape = mc.listRelatives(checkObj,s=1,ni=1,f=1)
        if shape:
            shapeCons = mc.listConnections(shape,s=1,d=0)
        for checkNode in  nodeCons:
            if abcNode in checkNode:
                consState = 1
                break
            else:
                checkType = mc.nodeType(checkNode)
                if checkType in ['unitConversion']:
                    nowCons = mc.listConnections(checkNode,s=1,d=0)
                    while nowCons:
                        pCons = mc.listConnections(nowCons[0],s=1,d=0)
                        nowCons = pCons
                    if not nowCons:
                        nowCons = []
                    if abcNode in nowCons:
                        consState = 1
                        break
        if shapeCons and abcNode in shapeCons:
            consState = 1
        return consState

    #--------------------------------------#
    # 获取没有abc节点连接的物体,为单帧服务
    def getNoConsAbcObj(self,checkType,checkNs= ''):
        needObjs = []
        if checkNs:
            checkObjs = mc.ls('%s:*'%checkNs,type = 'transform',l=1)
        else:
            checkObjs = mc.ls('*:*',type = 'transform',l=1)
        for checkObj in checkObjs:
            inr = mc.referenceQuery(checkObj,inr=1)
            if inr:
                continue
            abcKey = 'alembic'
            if checkType in ['curve']:
                abcKey = 'abc_curve'
            if mc.ls('%s.%s'%(checkObj,abcKey)):
                continue
            if len(checkObj.split('|')) !=2:
                continue
            shape = mc.listRelatives(checkObj,s=1,ni=1,f=1)
            shapeCons = []
            if shape:
                shapeCons = mc.listConnections(shape,s=1,d=0)
            transCos = mc.listConnections(checkObj,s=1,d=0)
            if transCos or shapeCons:
                continue
            if checkObj in needObjs:
                continue
            needObjs.append(checkObj)
        return needObjs

    #--------------------------------------#
    # 匹配位移及旋转中心，避免rg参考mo状态下修型导致的mo和rg不匹配
    def checkSamePivot(self,sourceObj,targetObj):
        # 第一轮处理
        # rotateP local
        localP = mc.xform(sourceObj,rotatePivot = 1, q = 1)
        mc.xform(targetObj,rotatePivot = localP )

        # scaleP local
        localS = mc.xform(sourceObj,scalePivot = 1, q = 1)
        mc.xform(targetObj,scalePivot = localS)

        # rotateP world
        #worldP = mc.xform(sourceObj,rotatePivot = 1,ws = 1, q = 1)
        #mc.xform(targetObj,rotatePivot = worldP ,ws = 1 )

        # scaleP
        #worldS = mc.xform(sourceObj,scalePivot = 1,ws = 1, q = 1)
        #mc.xform(targetObj,scalePivot = worldS ,ws = 1 )

        # translate
        self.checkSamePosition(sourceObj,targetObj)

        # 第二轮处理
        noList = []
        localPS = mc.xform(sourceObj,rotatePivot = 1, q = 1)
        localPT = mc.xform(targetObj,rotatePivot = 1, q = 1)
        worldPS = mc.xform(sourceObj,rotatePivot = 1,ws = 1, q = 1)
        worldPT = mc.xform(targetObj,rotatePivot = 1,ws = 1, q = 1)
        if localPS != localPT and worldPS != worldPT:
            mc.parentConstraint(sourceObj ,targetObj, maintainOffset = 0)
            noList.append(targetObj)

    # 预先匹配
    def checkSamePosition(self,sourceObj,targetObj):
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        for attr in attrList:
            targetAttr = targetObj + attr
            targetValue = mc.getAttr(targetAttr)
            sourceAttr = sourceObj + attr
            sourceValue = mc.getAttr(sourceAttr)
            if abs(targetValue - sourceValue) < pow(10,self.pointLimit):
                continue
            mc.setAttr(targetAttr,sourceValue)

    #--------------------------------------#
    # 单帧形变处理,避免某些物体有毛发关闭清理历史
    def singleFrameCacheBlendConfig(self,source,target,checkType='mesh',delHistory = 0,blendPre = ''):
        mc.select(cl=1)
        mc.select(source)
        mc.select(target,add= 1)
        checkNodeType = mc.nodeType(source)
        nodeType = ''
        if checkNodeType in ['transform']:
            shape = mc.listRelatives(source,s=1,ni=1,f=1)
            if not shape:
                return
            nodeType = mc.nodeType(shape[0])
        if checkNodeType in ['mesh','nurbsCurve']:
            nodeType = checkNodeType
        if nodeType not in ['mesh','nurbsCurve']:
            return
        if nodeType in ['curve']:
            self.checkRebuildCurves(source,target)
        if nodeType in ['mesh']:
            try:
                blendNode = mc.blendShape(frontOfChain=0,origin = 'local')
            except:
                print '\n----------BlendGetError'
                print source
                print target
                print '\n'
                mc.error()
            if ':' in source:
                attr = source.split(':')[-1]
            else:
                attr = source.split('|')[-1]
            mc.setAttr((blendNode[0] + '.' + attr),1)
            if blendPre:
                mc.rename(blendNode[0],blendPre+blendNode[0])
        if delHistory:
            mc.select(target)
            mel.eval('DeleteHistory')
            mc.select(cl=1)

    #--------------------------------------#
    # 曲线rebuild一致
    def checkRebuildCurves(self,source,target):
        shape = mc.listRelatives(source,s=1,ni=1,f=1)
        if not shape:
            return
        if mc.nodeType(shape[0]) not in ['nurbsCurve']:
            return
        sourceDegree = mc.getAttr(source+'.degree')
        sourceSpans  = mc.getAttr(source+'.spans')
        targetDegree = mc.getAttr(target+'.degree')
        targetSpans  = mc.getAttr(target+'.spans')
        if sourceSpans == targetSpans and sourceDegree == targetDegree:
            return
        mc.rebuildCurve(target,ch =1,rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,s=sourceSpans,d=sourceDegree,tol=0.01)

    #--------------------------------------#
    # 修正deformer renderState
    def checkRenderStateRebuild(self):
        meshes = mc.ls(type = 'mesh',l=1)
        if not meshes:
            return
        meshGrps = mc.listRelatives(meshes,p=1,type='transform',f=1)
        if not meshGrps:
            return
        for checkObj in meshGrps:
            renderMesh = mc.listRelatives(checkObj,s=1,ni=1,type = 'mesh',f=1)
            if not renderMesh:
                continue
            renderMesh = renderMesh[0]
            inr = mc.referenceQuery(renderMesh,inr=1)
            if inr:
                continue
            meshes = mc.listRelatives(checkObj,s=1,type = 'mesh',f=1)
            for checkMesh in meshes:
                if renderMesh == checkMesh:
                    continue
                inr = mc.referenceQuery(checkMesh,inr=1)
                if not inr:
                    continue
                self.checkFixRenderStates(checkMesh,renderMesh)

    # 执行修正
    def checkFixRenderStates(self,soureMesh ,targetMesh):
        renderStatesList = ['.castsShadows','.receiveShadows','.motionBlur','.primaryVisibility','.smoothShading']
        renderStatesList +=['.visibleInReflections','.visibleInRefractions','.doubleSided']
        renderStatesList +=['.aiSelfShadows','.aiOpaque','.aiVisibleInDiffuse','.aiVisibleInGlossy','.aiMatte']
        for checkAttr in renderStatesList:
            if not mc.ls(soureMesh + checkAttr):
                continue
            value = mc.getAttr(soureMesh + checkAttr)
            if not value:
                mc.setAttr(targetMesh+checkAttr,value)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【输出|重连abc cache节点连接】
    #  用途：finish阶段输出abc cache节点连接信息
    #      方便修复时使用
    #  Author  : 沈  康
    #  Data    : 2015_06_22  move in GDC 2016.4
    #------------------------------#
    # 输出
    def checkAbcConnectInfoExport(self,server = 1):
        # 记录
        abcNodes = mc.ls(type = 'AlembicNode')
        if not abcNodes:
            return
        usedNodes      = ['unitConversion']
        abcConsInfos = []
        abcPaths  = []
        for abcNode in abcNodes:
            # 属性信息
            cachePath = mc.getAttr(abcNode + '.abc_File')
            abcPaths = abcPaths + [abcNode , cachePath]
            # 连接信息
            inr = mc.referenceQuery(abcNode,inr = 1)
            if inr:
                continue
            consInfos = mc.listConnections(abcNode,s=0,d=1,plugs=1,c=1)
            if not consInfos:
                continue
            for num in range(len(consInfos)/2):
                checkInfo = consInfos[2*num+1]
                nodeType = mc.nodeType(checkInfo.split('.')[0])
                if nodeType not in usedNodes:
                    abcConsInfos = abcConsInfos + [consInfos[2*num],consInfos[2*num+1]]
                    continue
                targetAttr = mc.listConnections(checkInfo.split('.')[0],s=0,d=1,plugs=1)
                if not targetAttr:
                    continue
                targetAttr = targetAttr[0]
                if not mc.ls(targetAttr):
                    targetName = targetAttr.split('|')[-1]
                    targetObjSimp = targetName.split('.')[0]
                    targetObj = mc.ls(targetObjSimp,l=1)[0]
                    targetAttr = '%s%s'%(targetObj,targetName[len(targetObjSimp):])
                abcConsInfos = abcConsInfos + [consInfos[2*num],targetAttr]
        # 输出
        infoKey = 'abcInfos'
        shotType = self.shotType
        localSetAnimPath = self.alembicLocalPath(shotType)

        self.checkFileWrite((localSetAnimPath + infoKey + '_Cons.txt'),abcConsInfos)
        self.checkFileWrite((localSetAnimPath + infoKey + '_Path.txt'),abcPaths)

        # 更新
        if server:
            serverSetAnimPath = self.alembicServerPath(shotType)
            if not os.path.exists(serverSetAnimPath):
                mc.sysFile(serverSetAnimPath,mdr = 1)
            mc.sysFile((localSetAnimPath + infoKey + '_Cons.txt'),copy=(serverSetAnimPath + infoKey +  '_Cons.txt'))
            mc.sysFile((localSetAnimPath + infoKey + '_Path.txt'),copy=(serverSetAnimPath + infoKey +  '_Path.txt'))
            print serverSetAnimPath

    #--------------------------------------#
    # 导入连接
    def checkAbcConnectInfoImport(self,server = 1):
        # 检测
        infoKey = 'abcInfos'
        shotType = self.shotType
        localSetAnimPath = self.alembicLocalPath(shotType)
        serverSetAnimPath = self.alembicServerPath(shotType)
        if server:
            needPath = serverSetAnimPath
        else:
            needPath = localSetAnimPath
        if not os.path.exists(needPath + infoKey + '_Cons.txt') or not os.path.exists(needPath + infoKey + '_Path.txt'):
            return
        # 分析
        abcConsInfos = self.checkFileRead(needPath + infoKey + '_Cons.txt')
        abcPathInfos = self.checkFileRead(needPath + infoKey + '_Path.txt')
        abcNodes = []
        abcPaths = []
        for idNum in range(len(abcPathInfos)/2):
            abcNodes.append(abcPathInfos[2*idNum])
            abcPaths.append(abcPathInfos[2*idNum+1])
        # 修正节点准备阶段
        for abcNode in abcNodes:
            idNum = abcNodes.index(abcNode)
            abcPath = abcPaths[idNum]
            abcNodesNow = mc.ls(type = 'AlembicNode')
            if not mc.ls(abcNode):
                checkTarget = self.checkAbcPathTarget(abcPath,abcNodesNow)
                # 无则创建
                if not checkTarget:
                    mc.createNode('AlembicNode',name = abcNode)
                    mc.connectAttr('time1.outTime',(abcNode + '.time'))
                    mc.setAttr((abcNode + '.abc_File'),abcPath , type = 'string')
                # 有则改名
                else:
                    mc.rename(checkTarget,abcNode)
            else:
                nowPath = mc.getAttr(abcNode + '.abc_File')
                # 不匹配改路径
                if nowPath.lower() != abcPath.lower():
                    mc.setAttr((abcNode + '.abc_File'),abcPath , type = 'string')
        # 重新连接
        for num in range(len(abcConsInfos)/2):
            sourceAttr = abcConsInfos[2*num]
            targetAttr = abcConsInfos[2*num + 1]
            # 检测目标有没有连接
            checkTargetCons = mc.listConnections(targetAttr,s=1,d=0,plugs = 1)
            if checkTargetCons:
                checkTargetCons = checkTargetCons[0]
                # 处理unitConversion
                checkNodeType = mc.nodeType(checkTargetCons.split('.')[0])
                if checkNodeType in ['groupParts']:
                    # 连到inputGeometry里
                    upPartsNode = self.checkGetFirtPairsNode(checkTargetCons.split('.')[0])
                    upPartsNodeAttr = '%s.%s'%(upPartsNode,'inputGeometry')
                    parNodeCons = mc.listConnections(upPartsNodeAttr,s=1,d=0,plugs=1)
                    if parNodeCons:
                        parNodeCons = parNodeCons[0]
                        if parNodeCons == sourceAttr:
                            continue
                        else:
                            mc.disconnectAttr(parNodeCons,upPartsNodeAttr)
                            mc.connectAttr(sourceAttr,upPartsNodeAttr)
                    else:
                        mc.connectAttr(sourceAttr,upPartsNodeAttr)
                if checkNodeType in ['unitConversion']:
                    elderCheckTargetCons = mc.listConnections(checkTargetCons,s=1,d=0,plugs = 1)
                    # 中间节点无上游输入节点，干掉重连
                    if not elderCheckTargetCons:
                        mc.disconnectAttr(checkTargetCons,targetAttr)
                        # 连接
                        try:
                            mc.connectAttr(sourceAttr,targetAttr)
                        except:
                            mc.connectAttr(sourceAttr.split('[')[0],targetAttr)
                        # 清理中间节点
                        mc.delete(checkTargetCons.split('.')[0])
                    else:
                        elderCheckTargetCons = elderCheckTargetCons[0]
                        # 中间节点上游和源不匹配，干掉重连
                        if elderCheckTargetCons != sourceAttr:
                            mc.disconnectAttr(checkTargetCons,checkTargetCons)
                            # 连接
                            try:
                                mc.connectAttr(sourceAttr,targetAttr)
                            except:
                                mc.connectAttr(sourceAttr.split('[')[0],targetAttr)
                            # 清理中间节点
                            mc.delete(checkTargetCons.split('.')[0])
                else:
                    # 无中间节点时，上游和源不匹配，干掉重连
                    if checkTargetCons != sourceAttr:
                        #mc.disconnectAttr(sourceAttr,checkTargetCons)
                        mc.disconnectAttr(checkTargetCons,targetAttr)
                        # 连接
                        try:
                            mc.connectAttr(sourceAttr,targetAttr)
                        except:
                            mc.connectAttr(sourceAttr.split('[')[0],targetAttr)

            else:
                # 无输入节点，连接即可
                # 连接
                try:
                    mc.connectAttr(sourceAttr,targetAttr)
                except:
                    mc.connectAttr(sourceAttr.split('[')[0],targetAttr)

    #--------------------------------------#
    # 获取最上游pairsNode
    def checkGetFirtPairsNode(self,groupPartsNode):
        inAttr = 'inputGeometry'
        checkType = ['groupParts','tweak']
        upNodeAttr = mc.listConnections('%s.%s'%(groupPartsNode,inAttr),s=1,d=0,plugs = 1)
        needInfo = ''
        while upNodeAttr:
            upNodeAttr = upNodeAttr[0]
            upNode = upNodeAttr.split('.')[0]
            checkNodeType = mc.nodeType(upNode)
            if checkNodeType in ['groupParts']:
                inAttr = 'inputGeometry'
                outAttr = 'outputGeometry'
            if checkNodeType in ['tweak']:
                inAttr = 'input[0].inputGeometry'
                outAttr = 'outputGeometry[0]'
            if checkNodeType in checkType:
                needInfo = upNodeAttr
                tempUpAttr = mc.listConnections('%s.%s'%(upNode,inAttr),s=1,d=0,plugs=1)
                tempUpNode = ''
                checkNodeType = ''
                if tempUpAttr:
                    tempUpNode = tempUpAttr[0].split('.')[0]
                    checkNodeType = mc.nodeType(tempUpNode)
                    if checkNodeType in checkType:
                        upNodeAttr = tempUpAttr
                    else:
                        upNodeAttr = ''
                else:
                    upNodeAttr = ''
            else:
                needInfo = '%s.%s'%(groupPartsNode,inAttr)
                upNodeAttr = ''
        return needInfo.split('.')[0]

    #--------------------------------------#
    # 检测路径拍屏abcNodes
    def checkAbcPathTarget(self,abcPath,abcNodes):
        targetNode = ''
        for abcNode in abcNodes:
            if not mc.ls(abcNode):
                continue
            nowPath = mc.getAttr(abcNode + '.abc_File')
            if nowPath.lower() != abcPath.lower():
                continue
            targetNode = abcNode
            break
        return targetNode

    #------------------------------------#
    ###ABC-replace模式(绝对保证链接正确)    梁宇
    def LY_alembicMeshImp(self):
        needNodes=[]
        nodes = mc.ls(type='transform',l=1)
        if nodes:
            for node in nodes:
                shape = mc.listRelatives(node, c=1, type='mesh',f=1)
                if shape:
                    if node not in needNodes:
                        needNodes.append(node)

        nodeNeeds=[]
        if needNodes:
            for node in needNodes:
                if mc.objExists(node+'.alembic'):
                    nodeNeeds.append(node)

        grp=[]
        abcNodes = mc.ls(type = 'AlembicNode')
        for abcNode in abcNodes:
            objs = mc.listConnections(abcNode,d=1,plugs=1)
            if objs:
                for obj in objs:
                    if obj.split('.')[-1]=='inMesh':
                        grp.append(obj)


        objs=grp
        if objs:
            abcshapes=[]
            for obj in objs:
                abcshapes.append(obj.split('.')[-2])
            for shape in abcshapes:
                for obj in nodeNeeds:
                    if (mc.listRelatives(shape, p=1, type='transform', f=1)[0]).split('|')[-1] == obj.split('|')[-1]:
                        sInfo = mc.listConnections(shape,s = 1,type = 'AlembicNode',plugs=1)[0]
                        needInfo = mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)[0]
                        if mc.isConnected(sInfo,(needInfo+'.inMesh'))!= True:
                            mc.connectAttr(sInfo,(needInfo+'.inMesh'),f=1)

                    else:
                       if (mc.listRelatives(shape, p=1, type='transform', f=1)[0]).split('|')[-1] == obj.split('|')[-1].split(':')[-1]:
                            sInfo = mc.listConnections(shape,s = 1,type = 'AlembicNode',plugs=1)[0]
                            needInfo = mc.listRelatives(obj, ad=1, ni=1, type='mesh', f=1)[0]
                            if mc.isConnected(sInfo,(needInfo+'.inMesh'))!= True:
                                mc.connectAttr(sInfo,(needInfo+'.inMesh'),f=1)
                       #else: print u'OBJS: %s has no match cache object ' %(obj) #=====add by zhangben

    def LY_alembicCurveImp(self):
        needCurs=[]
        curves = mc.ls(type='transform',l=1)
        if curves:
            for cur in curves:
                shape = mc.listRelatives(cur,ad=1,f=1,ni=1,type='nurbsCurve')
                if shape:
                    if cur not in needCurs:
                        needCurs.append(cur)

        CurNeeds=[]
        if needCurs:
            for node in needCurs:
                if mc.objExists(node+'.abc_curve'):
                    CurNeeds.append(node)

        CurshapeNeeds=[]
        for cur in CurNeeds:
            CurshapeNeeds.append(mc.listRelatives(cur, c=1, type='nurbsCurve',f=1)[0])

        grp=[]
        abcNodes = mc.ls(type = 'AlembicNode')
        for abcNode in abcNodes:
            objs = mc.listConnections(abcNodes,d=1,plugs=1)
        if objs:
            for obj in objs:
                if obj.split('.')[-1]=='create':
                    grp.append(obj)
        objs=grp
        if objs:
            abcshapes=[]
            for obj in objs:
                abcshapes.append(obj.split('.')[-2])

            for shape in abcshapes:
                for shapecur in CurshapeNeeds:
                    if shapecur.split('|')[-1] == shape.split('|')[-1]:
                        sInfo = mc.listConnections(shape,s = 1,type = 'AlembicNode',plugs=1)[0]
                        if mc.isConnected(sInfo,(shapecur+'.create'))!= True:
                            mc.connectAttr(sInfo,(shapecur+'.create'),f=1)

                    else:
                        if shapecur.split('|')[-1].split(':')[-1] == shape.split('|')[-1]:
                            sInfo = mc.listConnections(shape,s = 1,type = 'AlembicNode',plugs=1)[0]
                            if mc.isConnected(sInfo,(shapecur+'.create'))!= True:
                                mc.connectAttr(sInfo,(shapecur+'.create'),f=1)


    #---------------------------------#
    # abc属性添加
    #---------------------------------#
    def abc_AttrAdd(self):
        tempGrps = mc.ls('*:MODEL',l=1)
        needGrps = []
        for tempgrp in tempGrps:
            state = 0
            if '|CHR_GRP|' in tempgrp:
                state = 1
            if '|PRP_GRP|' in tempgrp:
                state = 1
            if state:
                needGrps.append(tempgrp)
        for needgrp in needGrps:
            if mc.ls(needgrp+'.alembic'):
                continue
            mc.select(needgrp)
            self.csl_AttrAction(line="add",attrtype="alembic")
        mc.select(cl =1)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核】【属性添加工具】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#
    #添加（删减）物体属性（)
    def csl_AttrAction(self,line='add',attrtype='GD',printMode = 0):
        if line=='select':
            objs=mc.ls(type='transform',l=1)
            if objs :
                objList=[]
                for obj in objs:
                    if mc.objExists(obj+'.'+attrtype):
                        objList.append(obj)
                if objList:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================' % attrtype
                    print u'\n'
                else:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择物体，请选择物体' )
        else:
            meshList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            for obj in objs:
                meshcs=mc.listRelatives(obj,ad=1,f=1)
                if not meshcs:
                    meshcs = []
                for meshc in meshcs:
                    if mc.nodeType(meshc) in ['mesh','light']:
                        meshList.append(meshc)
                    if 'light' in mc.nodeType(meshc).lower():
                        meshList.append(meshc)
            if meshList:
                for mesh in meshList:
                    objs=mc.listRelatives(mesh,p=1,f=1)
                    if mc.objExists(objs[0]) and  line=='add':
                        try:
                            mc.setAttr((objs[0]+'.'+attrtype),1)
                        except:
                            mc.addAttr(objs[0],ln=attrtype,at='double',dv=1,k=1)
                    if printMode:
                        print u'==========================已添加选择物体的【%s】属性==========================' % attrtype
                    if mc.objExists(objs[0]) and  line=='remove':
                        obj=objs[0]
                        try:
                             mc.deleteAttr(objs[0],at=attrtype)
                        except:
                             pass
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )

        return 0

    #---------------------------------------------------#
    #ABC属性添加【通用】【输助】【返回添加ABC属性的物体】
    #@author 韩虹
    #2015/03/24
    #infotype 为1 导出信息，为0 导出信息，为3则为ABC物体信息
    #---------------------------------------------------#
    def GDC_alembicInfo(self,infotype=1):
        self.csl_AttrAction(line='select',attrtype='alembic')
        print u' now pinrt lineNum: 188' #===add by zhangben ,label line number
        abcOjbs=mc.ls(sl=1,l=1)
        abcInfo=''
        abcInfos=[]
        if abcOjbs:
            for i in range(len(abcOjbs)):
                if infotype==0:
                    if i==0:
                        abcInfo=abcOjbs[0]
                    else:
                        abcInfo=abcInfo+' '+abcOjbs[i]
                if infotype==1:
                    if i==0:
                        abcInfo=' -root '+abcOjbs[0]
                    else:
                        abcInfo=abcInfo+' -root '+abcOjbs[i]
                if infotype==3:
                    abcInfos.append(abcOjbs[i])
        else:
            print u'缺少ABC属性物体'
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos

        print '-------------S005'

        return abcInfos

    #---------------------------------------------------#
    #abc_curve属性物体【通用】【输助】【用在shave curve】
    #@author 韩虹    修改：梁宇
    #---------------------------------------------------#
    def GDC_shaveInfo(self,infotype=0,type='abc_curve'):
        curves=mc.ls(type='transform',l=1)
        abcInfo=''
        abcInfos=[]
        abcobjs=[]
        needCurs=[]
        if curves:
            for cur in curves:
                shape = mc.listRelatives(cur,ad=1,f=1,ni=1,type='nurbsCurve')
                if shape:
                    if cur not in needCurs:
                        needCurs.append(cur)
        CurNeeds=[]
        if needCurs:
            for node in needCurs:
                if mc.objExists(node+'.'+type):
                    CurNeeds.append(node)

        abcobjs=CurNeeds

        if abcobjs:
            for i in range(len(abcobjs)):
                if infotype==0:
                    if i==0:
                        abcInfo=abcobjs[0]
                    else:
                        abcInfo=abcInfo+' '+abcobjs[i]
                if infotype==1:
                    if i==0:
                        abcInfo=' -root '+abcobjs[0]
                    else:
                        abcInfo=abcInfo+' -root '+abcobjs[i]
                if infotype==3:
                    abcInfos.append(abcobjs[i])
        else:
            print u'缺少abc_curve属性'
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos

        return abcInfos

    #-------------------------------------------#
    #ABC属性添加【通用】【核心】【创建并导入abc（前期）】
    #@author 韩虹
    #2015/03/24
    #-------------------------------------------#
    def GDC_alembicImp(self,line='pre',server = 1,shotType = 1,UI=0,replaceMode = 0,abcBy_ns = 0):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        shotInfo=self.checkShotInfo()
        #本机
        FlocalPath=self.checkLocalInfoPath()
        #服务器路径
        FserverPath=self.checkProjectServerPath()
        if line=='fs':
            shotType = self.shotType
        # 获取alembic临时路径
        localPath = self.alembicLocalPath(shotType)
        # 获取alembic服务器端路径
        serverPath = self.alembicServerPath(shotType )
        projectInfo = self.projFull
        if line=='fs':
            frameStart = mc.playbackOptions(q=1, min=1)
            frameEnd = mc.playbackOptions(q=1, max=1)
            mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
            shotName=''
            alebicName=''
            if  shotType==2:
                shotName = shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]
            if  shotType==3:
                shotName = shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+ shotInfo[3]
            if UI==1:
                if shotType==2:
                    result = mc.promptDialog(title='north_abcImportTools',message=u'请键入需要cache名称\nEnter Name:\n例如：ice_999_008curve_mrGreene.abc',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                    if result == 'OK':
                            text = mc.promptDialog(query=True, text=True)
                            if text:
                                if text.split('.')[-1]=='abc':
                                    alebicName=text
                                else:
                                    mc.error(u'请输入正确文件名注意扩展名:".abc"')
                            else:
                                mc.error(u'请输入正确文件名,并按“OK”键')

            else:
                alebicName=shotName+'.abc'
            if server:
                basePath = serverPath
            else:
                basePath = localPath
            if not replaceMode:
                abcinfo=self.GDC_alembicInfo(0)[0]
                mc.AbcImport((basePath+alebicName),mode='import',connect=abcinfo)
            else:
                # 整体模式
                if not abcBy_ns:
                    mc.AbcImport((basePath+alebicName),mode='replace')
                # asset单位模式
                else:
                    nsList = self.getNsListOfFile()
                    for checkNs in nsList:
                        alebicName = '%s_%s_alembic.abc'%(shotName,checkNs)
                        mc.AbcImport((basePath+alebicName),mode='replace')
                        # 赋予namespace
                        self.abcMeshAddNs(checkNs)
            mc.playbackOptions(min=frameStart, max=frameEnd)
            mc.currentTime(int(frameStart))
        return 0

    # 获取当前文件的nslist
    def getNsListOfFile(self,noSet = 1,justRef = 1):
        nsList = mc.namespaceInfo(listOnlyNamespaces=1)
        nsList.remove('UI')
        nsList.remove('shared')
        needNsList = []
        for checkNs in nsList:
            meshes = mc.ls('%s:*'%checkNs,type='mesh')
            if not meshes:
                continue
            refState = 0
            for checkMesh in meshes:
                refState = mc.referenceQuery(checkMesh,inr=1)
                if refState:
                    break
            if not refState:
                continue
            if noSet and checkNs.split('_')[1][0].lower() not in ['c','p']:
                continue
            needNsList.append(checkNs)
        return needNsList

    # 非参考replace物体赋予namespace
    def abcMeshAddNs(self,ns):
        checkObjs = mc.ls(type = 'transform',l=1)
        tempNs = ns + self.tempNs
        if not mc.namespace(exists = tempNs):
            mc.namespace(set = ':')
            mc.namespace(add = tempNs)
            mc.namespace(set = ':')
        for checkObj in checkObjs:
            if not mc.ls(checkObj):
                continue
            inr = mc.referenceQuery(checkObj,inr=1)
            if inr:
                continue
            splitNum = len(checkObj.split('|'))
            if splitNum != 2:
                continue
            if '%s:'%ns not in checkObj:
                continue
            result = mc.rename(checkObj,'%s:%s'%(tempNs,checkObj.split('|')[-1]))
            result = mc.rename(result,'%s:%s'%(tempNs,result.split('|')[-1]))

    #---------------------------------------------------------#
    #ABC属性【通用】【核心】【创建并导入毛发曲线abc（前期）】
    #@author 韩虹
    #2015/03/24
    #---------------------------------------------------------#
    def GDC_curvealembicImp(self,server = 1,shotType = 2,UI = 0,abcBy_ns=0,replaceMode = 1):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')

        shotInfo=self.checkShotInfo()
        #本机
        FlocalPath=self.checkLocalInfoPath()
        #服务器路径
        FserverPath=self.checkProjectServerPath()
        shotType = self.shotType
        # 获取alembic临时路径
        localPath = self.alembicLocalPath(shotType)
        # 获取alembic服务器端路径
        serverPath = self.alembicServerPath(shotType )
        projectInfo = self.projFull

        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
        shotName=''
        alebicName=''
        if  shotType==2:
            shotName = shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]
        if  shotType==3:
            shotName = shotInfo[0]+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+ shotInfo[3]
        if UI==1:
            if shotType==2:
                result = mc.promptDialog(title='north_abcImportTools',message=u'请键入需要cache名称\nEnter Name:\n例如：ice_999_008curve_mrGreene.abc',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                if result == 'OK':
                        text = mc.promptDialog(query=True, text=True)
                        if text:
                            if text.split('.')[-1]=='abc':
                                alebicName=text
                            else:
                                mc.error(u'请输入正确文件名注意扩展名:".abc"')
                        else:
                            mc.error(u'请输入正确文件名,并按“OK”键')
        else:
            alebicName=shotName+'curve.abc'
        abcinfo=self.GDC_shaveInfo(0,'abc_curve')[0]
        if server:
            basePath = serverPath
        else:
            basePath = localPath
        # curve使用导入模式?
        if projectInfo in ['ShunLiu']:
            mc.AbcImport((basePath+alebicName),mode='import',connect=abcinfo)
        else:
            # 整体模式
            if not abcBy_ns:
                mc.AbcImport((basePath+alebicName),mode='replace')
            # asset单位模式
            else:
                nsList = self.getNsListOfFile()
                for checkNs in nsList:
                    alebicName = '%s_%s_abc_curve.abc'%(shotName,checkNs)
                    curveCache = basePath+alebicName
                    if not os.path.exists(curveCache):
                        continue
                    mc.AbcImport(curveCache,mode='replace')
                    # 赋予namespace
                    self.abcMeshAddNs(checkNs)
        #if projectInfo in ['MiniTiger']:
        #    mc.AbcImport((basePath+alebicName),mode='import')
        #else:
        #    mc.AbcImport((basePath+alebicName),mode='replace')
        mc.playbackOptions(min=frameStart, max=frameEnd)
        mc.currentTime(int(frameStart))
        return 0

   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【属性添加工具】
    #  Author  : 韩虹
    #  Data    : 2014_11
    #------------------------------#
    #添加（删减）物体属性（)
    def csl_AttrAction(self,line='add',attrtype='GD'):
        if line=='select':
            objs=mc.ls(type='transform',l=1)
            objList=[]
            if objs :
                for obj in objs:
                    if not mc.objExists(obj+'.'+attrtype):
                        continue
                    if ':RIG' in obj :
                        continue
                    if ':DEFORMERS' in obj :
                        continue
                    if '|OTC_GRP|' in obj :
                        continue
                    if '|SET_GRP|' in obj:
                        continue
                    objList.append(obj)
                try:
                    mc.select(objList)
                    print u'\n'
                    print u'==========================已选择有【%s】属性的物体==========================line:448' % attrtype
                    print u'\n'
                except:
                    print u'\n'
                    print u'==========================文件中没有【%s】属性的物体==========================line:452' % attrtype
                    print u'\n'
            else:
                mc.warning(u'没有选择物体，请选择物体' )
        else:
            meshList=[]
            objs=mc.ls(sl=1,type='transform',l=1)
            for obj in objs:
                meshcs=mc.listRelatives(obj,ad=1,f=1)
                if not meshcs:
                    meshcs = []
                for meshc in meshcs:
                    if mc.nodeType(meshc) in ['mesh','light']:
                        meshList.append(meshc)
                    if 'light' in mc.nodeType(meshc).lower():
                        meshList.append(meshc)
            if meshList:
                for mesh in meshList:
                    objs=mc.listRelatives(mesh,p=1,f=1)
                    checkObj = objs[0]
                    if line=='add':
                        checkAttr = checkObj+'.'+attrtype
                        if mc.ls(checkAttr):
                            lockState = mc.getAttr(checkAttr,l=1)
                            if not lockState:
                                mc.setAttr((objs[0]+'.'+attrtype),1)
                        else:
                            mc.addAttr(objs[0],ln=attrtype,at='double',dv=1,k=1)
            else:
                mc.warning( u'没有选择物体，或者所选择的物体是空组，请选择有效物体' )

        return 0

   #----------------------------------------------------------------------------------------------#
    def checkCurveSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        for temp in tempSet:
            if 'CURVES' in temp:
                objsSet.append(temp)
        cache_curs = ''
        if objsSet:
            for objSet in objsSet:
                cache_curs = mc.sets(objSet, q=1)
        if cache_curs:
            print (u'[Cache curve]    ' + str(len(cache_curs)))
        else:
            print (u'[Cache curve]    0')
        return cache_curs


   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【辅助】【FL文件 ReferenceEdit还原】
    #------------------------------#
    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info ):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = self.fileFomat
        fileGrpType = '_base_fs_c001'

        needFilePath = self.checkFinalLayoutLocalPath()
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat

        print needFsFile

        # 不加载参考导入
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # 处理好所有参考
        mc.file(save = 1, force = 1)


    #----------------------------------------------------------------------------------------------#
    def csl_setattr(self,attrtype='aiStandIn',attr='visibility',num=1):
        objs=mc.ls(type=attrtype ,l=1)
        if objs:
            for obj in objs:
                Arnold=mc.listRelatives(obj,p = 1,f=1)
                if Arnold and mc.nodeType(Arnold[0])=='transform':
                    mc.setAttr((Arnold[0]+'.'+attr),int(num))

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有约束BK，确保动画及camera正确】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self ,simulation = 1,step = 1,fixEuler = 0):
        min = mc.playbackOptions(minTime=1,q=1)
        max = mc.playbackOptions(maxTime=1,q=1)
        mc.playbackOptions(minTime=min-10)
        mc.playbackOptions(maxTime=max+5)

        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if  not constraintsAll:
            mc.playbackOptions(minTime=min)
            mc.playbackOptions(maxTime=max)

        tobake= []
        # 处理非参考的物体
        constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
        for checkCons in constraints:
            needObj = ''
            listAttrs = mc.listConnections(checkCons,s=1,d=0,plugs = 1)
            if not listAttrs:
                continue
            listAttrs = list(set(listAttrs))
            for checkConsAttr in listAttrs:
                if checkCons in checkConsAttr:
                    continue
                targetAttr = mc.listConnections(checkConsAttr,s=0,d=1,plugs = 1)[0]
                if '.constraint' in targetAttr:
                    needObj = checkConsAttr.split('.')[0]
                    needObj = mc.ls(needObj,l=1)[0]
                if needObj:
                    checkType = mc.nodeType(needObj)
                    if checkType in nodeTypeConfig and needObj not in tobake:
                        tobake.append(needObj)
                    continue
        io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)

        tobake = list(set(tobake))
        if not tobake:
            mc.playbackOptions(minTime=min)
            mc.playbackOptions(maxTime=max)
            return

        # 改进版，不bake，而是给新locator bake
        # 删除locators
        locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
        if locators:
            mc.delete(locators)


        #数值传递到locators
        locators = []
        constraintTemp = []
        print '---Step 01:'
        for i in range(len(tobake)):
            locTemp = mc.spaceLocator()
            locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
            cons = mc.parentConstraint(tobake[i] , locTemp)
            constraintTemp.append(cons[0])
            locators.append(locTemp)
            print '------'
            print tobake[i]
            print locTemp
        # 一次烘焙
        mc.bakeResults(locators,  t=io,
                simulation=simulation,
                sampleBy=step,
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
        if not locators:
            mc.playbackOptions(minTime=min)
            mc.playbackOptions(maxTime=max)
            return

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
        mc.bakeResults(tobake,    t=io,
                simulation=simulation,
                sampleBy=step,
                disableImplicitControl=1,
                preserveOutsideKeys=1,
                sparseAnimCurveBake=1,
                removeBakedAttributeFromLayer=0,
                bakeOnOverrideLayer=0,
                controlPoints=0,
                shape=1)

        # 删除约束
        #add by zhangben ---  extract constraint type node to world
        constraintConfigs = [x for x in (constraints) if not mc.referenceQuery(x,inr=1)]
        for cons in constraintConfigs:
            ref = mc.referenceQuery(cons,isNodeReferenced = 1)
            if not ref:
                mc.delete(cons)

        # 删除locators
        mc.delete(locators)

        # 修正欧拉角
        if fixEuler:
            self.checkAnimCurvesFix()

        mc.playbackOptions(minTime=min)
        mc.playbackOptions(maxTime=max)
        print(u'\n========================【约束】【烘焙】【成功】========================')
        print u'\n'

    #------------------------------#
    # 【辅助】修正动画曲线的欧拉翻转
    #------------------------------#
    # 修正动画曲线欧拉翻转
    def checkAnimCurvesFix(self):
        animCurvs = mc.ls(type = 'animCurve')
        checkRotGrps = {}
        rotateKey = '_rotate'
        for animC in animCurvs:
            checkKeys = checkRotGrps.keys()
            inr = mc.referenceQuery(animC,inr=1)
            if inr:
                continue
            if rotateKey not in animC:
                continue
            baseObj = animC.split(rotateKey)[0]
            if baseObj not in checkKeys:
                checkRotGrps[baseObj] = []
            if animC not in checkRotGrps[baseObj]:
                checkRotGrps[baseObj].append(animC)

        if not checkRotGrps.keys():
            return

        for obj in checkRotGrps.keys():
            rotateCurves = checkRotGrps[obj]
            animKey = ''
            for animC in rotateCurves:
                animKey = animKey + animC + ' '
            mel.eval('filterCurve %s'%animKey)

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

            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    checkInr = mc.referenceQuery(src,inr=1)
                    if checkInr:
                        return
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)

  #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 OTC及SET结构处理
    #  Author  : 沈康
    #  Data    : 2013_07_28
    #------------------------------#
    # OTC结构处理：删除 [更改：otc由mb强制变更ma;删除先删除ma文件，后找mb，若有则删除]
    def sk_sceneGRPDelete(self, fileGRP='OTC' , shotType = 2):

        shotInfo = self.checkShotInfo()
        fileFomat = '.ma'
        renderFilePathServer = self.checkCacheLocalPath(shotType)

        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            mc.sysFile( otcFileServer, delete=True)
        else:
            fileFomat = '.mb'
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            if os.path.exists(otcFileServer):
                mc.sysFile( otcFileServer, delete=True)
                print otcFileServer

    #------------------------------#

    #-------------------------------------#
    # 记录hide输出
    def sk_FL_RefHideObjsRecord(self,server,shotType):
        unDisplayLayerObjs = []
        # 记录：shot文件非参考的隐藏的显示层的物体
        displayLayers = mc.ls(type = 'displayLayer')
        for layer in displayLayers:
            isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
            if isRef == 0 and layer != 'defaultLayer':
                viewState  = mc.getAttr(layer + '.visibility')
                if not viewState:
                    objs = mc.editDisplayLayerMembers( layer, query=True )
                    if objs:
                        unDisplayLayerObjs += objs
        hideObjsServerPath = self.checkShotDataInfoPath(server = 1,infoMode = 2)
        hideObjsLocalPath = self.checkShotDataInfoPath(server = 0,infoMode = 2)
        mc.sysFile(hideObjsLocalPath,makeDir = 1)
        fileName = 'shotHideObjs.txt'
        self.checkFileWrite((hideObjsLocalPath +  fileName), unDisplayLayerObjs)
        if server:
            mc.sysFile((hideObjsLocalPath + fileName),copy = (hideObjsServerPath + fileName))
            print u'\n'
            print(u'=====================[hideObjs][Server][Update] Done=====================')
            print u'\n'
        return unDisplayLayerObjs

    #-------------------------------------#

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

    #-------------------------------------#
    # 输出角色道具信息
    def skFLAssetNeedInfo(self,refInfos,noNeedRefNodeInfo,shotType,server = 0):
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
        hideObjsLocalPath = self.checkShotDataInfoPath(server = 0,infoMode = 2)
        mc.sysFile(hideObjsLocalPath,makeDir = 1)
        fileName = 'assetReference.txt'
        self.checkFileWrite((hideObjsLocalPath +  fileName), assetNeedOutputInfo)
        if server:
            hideObjsServerPath = self.checkShotDataInfoPath(server = 1,infoMode = 2)
            mc.sysFile((hideObjsLocalPath + fileName),copy = (hideObjsServerPath + fileName))
            print u'\n'
            print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
            print u'\n'
        return assetNeedOutputInfo

    #-------------------------------------#

   #------------------------------#
    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC' , server=1 , shotType = 2 ,needNsList = []):
        renderFilePath = self.checkCacheLocalPath(shotType)

        shotInfo = self.checkShotInfo()
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
            animRefInfos = self.checkFileRead(otcFile)
            renderRefInfos = []
            for line in animRefInfos:
                if '_ms_anim.m' in line:
                    line = line.replace('_ms_anim.m','_ms_render.m')
                elif '_ms_gpu.m' in line and shotInfo[0] == u'mi':#=========add by zhangben for minitiger  set gpu.mb file ==== 2016.3.8===========
                    line = line.replace(u'_ms_gpu.m',u'_ms_render.m')
                renderRefInfos.append(line)
            self.checkFileWrite(otcFile,renderRefInfos)

        # 对otc进行转参考处理
        if fileGRP == 'OTC':
            # ma模式处理
            animRefInfos = self.checkFileRead(otcFile)
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
            self.checkFileWrite(otcFile,renderRefInfos)
        print '--------target'
        print  otcFile
        # 传至服务器
        if server:
            renderFilePathServer = self.checkCacheServerPath(shotType)
            if not os.path.exists(renderFilePathServer):
                mc.sysFile(renderFilePathServer,makeDir = 1)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            #mc.sysFile(otcFile,copy=otcFileServer)
            print '------------otcFile'
            print otcFile
            print otcFileServer
            mc.sysFile(otcFile,copy = otcFileServer)

    #------------------------------#
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
    # 处理数据，并输出
    def checkCacheVStateExport(self , cacheObjs= [], shotType = 2 ,server = 1,rootMode = 0):
        if not cacheObjs:
            modelGrps = mc.ls('*:MODEL*',type = 'transform',l=1)
            # 排除多个MODEL组的
            needModeGrps = []
            for checkGrp in modelGrps:
                tempInfos = checkGrp.split('MODEL')
                if len(tempInfos) != 2:
                    continue
                if '|SET_GRP|' in checkGrp:
                    continue
                needModeGrps.append(checkGrp)
            for rootGrp in needModeGrps:
                childGrps = mc.listRelatives(rootGrp,ad=1,type = 'transform',f=1)
                if not childGrps:
                    childGrps = []
                # 排除掉curve
                tempGrps = []
                for childGrp in childGrps:
                    shape = mc.listRelatives(childGrp,s=1,ni=1,f=1)
                    if not shape:
                        # root模式下,可以不输出V属性
                        # 非root模式下，只需要记住polygon即可
                        #tempGrps.append(childGrp)
                        pass
                    else:
                        checkNodeType = mc.nodeType(shape[0])
                        if checkNodeType in ['mesh']:
                            tempGrps.append(childGrp)
                childGrps = tempGrps
                cacheObjs = cacheObjs + [rootGrp] + childGrps
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
        # 输出本地
        ObjsVDataLocalPath = self.checkShotDataInfoPath(server = 0,infoMode = 2)
        fileName = 'cacheObjVInfo.txt'
        self.checkFileWrite((ObjsVDataLocalPath + fileName ), resultData)
        if server:
            ObjsVDataServerPath = self.checkShotDataInfoPath(server = 1,infoMode = 2)
            mc.sysFile((ObjsVDataLocalPath + fileName),copy = (ObjsVDataServerPath + fileName))
            print u'\n'
            print(u'=====================【cacheObjVInfo】【服务器端】【输出】完毕=====================')
            print u'\n'
        return  resultData

    #------------------------------#

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
        import maya.api.OpenMaya as OpenMaya
        objList = OpenMaya.MGlobal.getSelectionListByName(checkObj)
        result = int(objList.getDagPath(0).isVisible())
        return result

    #------------------------------#
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
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result

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
    #　objsCache     用于输出cache的物体
    # serverFile    服务器端输出
    # cachePre      预算范围，给特效用;默认是前后5帧，给动态模糊做预留
    #　refMode    　 是否一个参考一个cache
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
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'

        # mel用path
        localPathCache = self.checkCacheLocalPath(shotType)
        # local_animPath___python用转mel
        localPathAnim = self.checkAnimLocalPath(shotType).replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = self.checkCacheServerPath(shotType)
        # server_animPath___python用转mel
        serverPathAnim = self.checkAnimServerPath(shotType).replace('\\', '/')


        # 清理历史文件
        oldFiles = mc.getFileList(folder=localPathCache)
        for of in oldFiles:
            if of not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in of:
                mc.sysFile((localPathCache + of), delete=1)

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
        #MatLists = self.checkCacheRecordMaterial(shotType = shotType)

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
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        if shotType == 3:
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_' + dirInfo[3] + '_geoCache'

        # mel用path
        localPathCache = self.checkCacheLocalPath(shotType)
        # server端path
        if serverFile == 1:
            serverPathCache = self.checkCacheServerPath(shotType)
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
            localPathAnim = self.checkAnimLocalPath(shotType)
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
        localPathAnim = self.checkAnimLocalPath(shotType).replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = self.checkAnimServerPath(shotType).replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        mc.sysFile((localPathAnim + fileInfo),copy = (serverPathAnim + fileInfo))
        fileInfo = infoFile + '_objs.txt'
        mc.sysFile((localPathAnim + fileInfo),copy = (serverPathAnim + fileInfo))
        fileInfo = infoFile + '_Lobjs.txt'
        if os.path.exists(localPathAnim + fileInfo):
            mc.sysFile((localPathAnim + fileInfo),copy = (serverPathAnim + fileInfo))

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
    #------------------------------#
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , shotInfo , serverModify = 1 , shotType = 2):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = self.fileFomat
        fileGrpType = '_set_render'

        if serverModify == 0:
            needFilePath = self.checkCacheLocalPath(shotType)

        if serverModify == 1:
            needFilePath = self.checkCacheServerPath(shotType)

        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        needSetFile = needFilePath + baseShotInfo + fileGrpType + fileFomat
        print needSetFile
        import os
        if os.path.exists(needSetFile):
            # 不加载参考导入
            mc.file(needSetFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            print u'====================开始处理SET_GRP文件===================='
            # 处理好文件
            # 在importOTC之前处理好anim中材质更改的情况
            mc.file(save = 1, force = 1)

        if serverModify == 0:
            # 传至服务器
            renderFilePathServer = self.checkCacheServerPath(shotType)
            if not os.path.exists(renderFilePathServer):
                mc.sysFile(renderFilePathServer,makeDir = 1)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            print otcFileServer
            mc.sysFile(needSetFile,copy=otcFileServer)
        print u'====================SET_GRP更新完毕===================='

    #------------------------------#

    #------------------------------#
    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC' , shotType = 2):

        renderFilePathServer = self.checkCacheServerPath(shotType)
        # ma文件利于文本读取改参考
        shotInfo = self.checkShotInfo()
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'

        baseShotInfo = ''
        if shotType == 2:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            baseShotInfo = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        print otcFileServer
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
            if fileGRP == 'OTC':
                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))

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

    #------------------------------#
    # 【辅助】【备份材质】
    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,faceMode = 1,cacheMode = 1 ,shotType = 3):
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
            inr = mc.referenceQuery(node,inr = 1)
            if not inr:
                continue
            connectObjsSG = mc.sets(node, q=1)
            if not connectObjsSG:
                continue
            if not faceMode:
                MatLists[node] = connectObjsSG
            else:
                connectObjsSG = self.checkFaceMode(connectObjsSG)
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.checkCacheRecordMaterialExport(MatLists,shotType)
        return MatLists

    # 查询处理选面模式
    def checkFaceMode(self,objInfos):
        resultObjs = []
        for objInfo in objInfos:
            if '.f[0:' not in objInfo:
                resultObjs.append(objInfo)
            else:
                obj = objInfo.split('.f[')[0]
                lastFaceNum = int(objInfo.split('.f[0:')[-1].split(']')[0])
                faceNum = mc.polyEvaluate(obj,face = 1)
                if faceNum == lastFaceNum+1:
                    shape = mc.listRelatives(obj,ni= 1,s = 1)
                    if not shape:
                        continue
                    shape = shape[0]
                    resultObjs.append(shape)
                else:
                    resultObjs.append(objInfo)
        return resultObjs

    #------------------------------#
    #------------------------------#
    # 【辅助】【还原材质】
    #------------------------------#
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = {} ,finalLayout = 0,shotType = 2,forceMode = 1):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport(shotType)
        if not MatLists:
            return
        '''
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)
        '''
        keysSG = MatLists.keys()
        # 关闭材质球刷新
        mc.renderThumbnailUpdate(False)
        # 创建临时材质球
        # 通用材质
        shaderNode = 'SHD_Food_Shader'
        if mc.ls(shaderNode):
            mc.delete(shaderNode)
        shaderSG = 'SHD_Food_SG'
        if mc.ls(shaderSG):
            mc.delete(shaderSG)
        shaderNode = mc.shadingNode('lambert', asShader=True, name=shaderNode)
        shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=shaderSG)
        mc.connectAttr((shaderNode + '.outColor'), (shaderSG + '.surfaceShader'))
        #处理
        aee = []
        for key in keysSG:
            if not forceMode and not mc.ls(key):
                continue
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if not objs:
                continue
            newObjs = []
            for obj in objs:
                allObjs = mc.ls(obj,l=1)
                if allObjs:
                    for grp in allObjs:
                        if 'MODEL|' not in grp and '|OTC_GRP|' not in grp:
                            continue
                        if '_MODEL|' in grp:
                            continue
                        newObjs.append(grp)
                else:
                    abcShape = obj + 'Deformed'
                    if mc.ls(abcShape):
                        newObjs.append(abcShape)
            if newObjs:
                newObjs = list(set(newObjs))
            if not newObjs:
                continue
            # 避免该死的线框，先给个别的材质球
            for checkObj in newObjs:
                if not mc.ls(checkObj):
                    # 某些设置里使用该材质的模型复制出来的，排除
                    aee.append(checkObj)
                    continue
                try:
                    mc.sets(checkObj, forceElement = shaderSG)
                    mc.sets(checkObj, forceElement = key)
                except:
                    aee.append(checkObj)

            mc.sets(newObjs, forceElement = key)
        # 清理临时材质球
        if mc.ls(shaderNode):
            mc.delete(shaderNode)
        if mc.ls(shaderSG):
            mc.delete(shaderSG)

    #------------------------------#
    # 【辅助】【材质信息备份到服务器端】【拆分用】
    #------------------------------#
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists,shotType = 2):
        localShaderInfoPath = self.checkShotDataInfoPath(server = 0,infoMode = 1)
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
        serverDataPath = self.checkShotDataInfoPath(server = 1,infoMode = 1)
        mc.sysFile((localShaderInfoPath + fileInfo),copy = (serverDataPath + fileInfo))
        print serverDataPath
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo

    #------------------------------#
    # 【核心】回到原点cache处理，导入信息
    #------------------------------#
    def checkCacheResetPositionImport(self,serverFile = 1, shotType = 2):
        # 读控制器
        infoFile = 'moveInfo'
        if serverFile:
            path = self.checkAnimServerPath(shotType)
        else:
            path = self.checkAnimLocalPath(shotType)
        print '---'
        print (path + infoFile + '_objs.txt')
        needCtrls = self.checkFileRead(path + infoFile + '_objs.txt')
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
                serverPathAnim = self.checkAnimServerPath(shotType)
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = self.checkAnimLocalPath(shotType)
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
                                value = float(value)
                            mc.setAttr(key, value)
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

    #------------------------------#
    # v信息导入
    def checkCacheVStateImport(self , shotType = 2):
        vData = self.checkObjsVData(shotType)
        if not vData:
            return
        cacheObjs = vData.keys()
        for cacheObj in cacheObjs:
            realObj = cacheObj
            if not mc.ls(realObj):
                realObj = mc.ls(cacheObj.split('|')[-1],l=1)
                if not realObj:
                    continue
                realObj = realObj[0]
            keyInfo = vData[cacheObj]
            objAttr = realObj + '.v'
            cons = mc.listConnections(objAttr,s=1,d=0,plugs = 1)
            if cons:
                checkType = mc.nodeType(cons[0].split('.')[0])
                if 'animCurve' not in checkType:
                    continue
                else:
                    mc.disconnectAttr(cons[0],objAttr)
            # 单帧
            if len(keyInfo) == 1:
                vState = keyInfo[0][0]
                if not mc.objExists(objAttr):
                    continue
                mc.setAttr(objAttr,vState)
            # 多帧
            else:
                for i in range(len(keyInfo)):
                    vState = keyInfo[i][0]
                    frame = keyInfo[i][1]
                    mc.currentTime(frame)
                    mc.setAttr(objAttr,vState)
                    mc.setKeyframe(objAttr)

    #------------------------------#
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#
    # 输出材质信息
    def checkCacheRecordMaterialImport(self,shotType,server = 1):
        serverDataPath = self.checkShotDataInfoPath(server=server,infoMode=1)
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = self.checkFileRead(serverDataPath + fileInfo)
        if not allInfo:
            return {}
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
    # vData数据结构处理
    def checkObjsVData(self, shotType = 2):
        ObjsVDataServerPath = self.checkShotDataInfoPath(server = 1,infoMode = 2)
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

    # ------------------------------#
    # 【核心】 【非参考 namespace 清理】
    # ------------------------------#
    # 文件内非参考的namespace清理，必须在参考都加载的时候处理
    def sk_sceneNoRefNamespaceClean(self):
        namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaces.remove('UI')
        namespaces.remove('shared')
        refNamespace = []
        while namespaces:
            # 备份当前默认ns
            nsNow = mc.namespaceInfo(currentNamespace=1)
            if nsNow != ':':
                nsNow = ':' + nsNow
            # 处理所有namespace
            for ns in namespaces:
                mc.namespace(set=':')
                ns = ':' + ns
                checkNs = ns
                objs = mc.ls(checkNs + ':*')
                if objs:
                    for obj in objs:
                        if mc.objExists(obj):
                            if not mc.referenceQuery(obj, isNodeReferenced=1):
                                newName = obj.split(checkNs + ':')[-1]
                                mc.lockNode(obj, lock=False)
                                mc.rename(obj, newName)
                try:
                    mc.namespace(moveNamespace=[ns, ':'], f=1)
                    mc.namespace(removeNamespace=ns)
                except:
                    refNamespace.append(ns.split(':')[-1])
            # 还原ns
            mc.namespace(set=nsNow)
            namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            namespaces.remove('UI')
            namespaces.remove('shared')
            if refNamespace:
                for info in refNamespace:
                    if info in namespaces:
                        namespaces.remove(info)

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

    # 通过refNode 获取refNode的namespace
    def checkReferenceGetNamespaceInfo(self,refNode):
        refObjs = mc.referenceQuery( refNode ,nodes = 1 )
        namespace = ''
        if refObjs:
            nmInfo = refObjs[0].split(':')
            for i in range(len(nmInfo)-1):
                if i == 0:
                    namespace = nmInfo[i]
                else:
                    namespace =  namespace + ':' + nmInfo[i]
        return namespace

    # 通过refPath 获取refNode的namespace
    def checkReferenceGetNamespaceInfoByPath(self,refPth):
        namespace = mc.file( refPth ,namespace = 1 ,q = 1 )
        # 判断是不是子参考
        parentRef = mc.referenceQuery( refPth , referenceNode=True, parent = True )
        if parentRef:
            namespace = parentRef[:-2] + ':' + namespace
        return namespace

    # 处理reference路径，清楚后面可能存在的{}
    def checkReferencePathConfig(self, path):
        if '{' in path:
            path = path.split('{')[0]
        return path

    def checkShotInfo(self,noFormat = 0):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
            if noFormat and '.' in info[-1]:
                info[-1] = info[-1].split('.')[0]
        else:
            #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
        return info

    def checkShotID(self):
        shotInfos = self.checkShotInfo()
        shotType = self.shotType
        shotID = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfos[3])
        if '.' in shotID:
            shotID = shotID.split('.')[0]
        return shotID

    # 本地cache路径
    def alembicLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        if shotType == 2:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/alembic/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache

    # 服务器端cache路径
    def alembicServerPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        shotType = self.shotType
        serverPathCache=''
        projectServerBas = self.checkProjectServerPath(stepMode='cache')
        if shotType == 2:
            serverPathCache = (projectServerBas + 'data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = (projectServerBas + 'data/alembic/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache

    # 本地infot路径
    def checkLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath

    # 服务器端project路径
    # typeMode 0 输出 '/' 数据 | typeMode 1 输出 '\\' 数据
    def checkProjectServerPath(self,typeMode = 0,stepMode = ''):
        dirInfo = self.checkShotInfo()
        project = self.projFull
        projectServerPath = 'Z:/Projects/' + project + '/Project/'
        if typeMode:
            projectServerPath = projectServerPath.replace('/','\\')
        return projectServerPath

    # 本地anim路径
    def checkAnimLocalPath(self,shotType = 2,rebuild = 0):
        # python用
        animInfo = 'animInfoTemp'
        if rebuild:
            animInfo = 'animRebuild'
        shotInfo = self.checkShotInfo()
        localPathAnim = ('D:\\Info_Temp\\temp\\' + animInfo + '\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        if shotType == 3:
            localPathAnim = ('D:\\Info_Temp\\temp\\' + animInfo + '\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # 服务器端anim路径
    def checkAnimServerPath(self,shotType = 2,rebuild = 0):
        # python用
        animInfo = 'AnimInfo'
        if rebuild:
            animInfo = 'AnimRebuild'
        shotInfo = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath(typeMode=1)
        serverPathAnim=''
        if shotType == 2:
            serverPathAnim = (projectPathBase + 'data\\' + animInfo + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        if shotType == 3:
            serverPathAnim = (projectPathBase + 'data\\' + animInfo + '\\'  + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\' + str(shotInfo[3]) + '\\')
        return serverPathAnim

    #----------------------------------#
    # 万能版路径查询，以后可改成此方案
    # 沈康 2016.5
    #----------------------------------#
    #-----------------------------------------#
    # infoMode 通用
    # ShotInfo : 1 data/ShotShaderInfo  | 2 data/AbcCache | 3 dyCacheFolder | 4 vfxCacheFolder | 5 camInfoOutInfo |
    #            6 animCleanTemp        | 7 fxAbcCache    | 8 camAbc        | 9 lightInfo      | 10 ShotDisTemp
    def checkShotDataInfoPath(self,server = 0,infoMode = 1,shotInfos = []):
        infoKey = ''
        if server:
            pathBase = self.checkProjectServerPath()
        else:
            pathBase = self.checkLocalInfoPath()
        if not shotInfos:
            shotInfos = self.checkShotInfo()
        shotType = self.shotType

        infoKey = ''

        if infoMode == 0:
            infoKey = 'GeoCache'
        if infoMode == 1:
            infoKey = 'ShotShaderInfo'
        if infoMode == 2:
            infoKey = 'AbcCache'
        if infoMode == 2.5:
            infoKey = 'alembic'
        if infoMode == 3:
            infoKey = 'DyCache'
        if infoMode == 4:
            infoKey = 'VfxCache'
        if infoMode == 5:
            infoKey = 'CamInOutInfo'
        if infoMode == 6:
            infoKey = 'AnimCleanTemp'
        if infoMode == 7:
            infoKey = 'FxAbcCache'
        if infoMode == 8:
            infoKey = 'CamAbc'
        if infoMode == 9:
            infoKey = 'LightInfos'
        if infoMode == 10:
            infoKey = 'ShotDisTemp'

        shotFolder = '%s/%s'%(shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotFolder = '%s/%s/%s'%(shotInfos[1],shotInfos[2],shotInfos[3])

        if infoKey:
            needPathShot = '%sdata/%s/%s/'%(pathBase,infoKey,shotFolder)
        else:
            needPathShot = '%s%s/%s/'%(pathBase,shotInfos[0],shotFolder)

        if not os.path.exists(needPathShot):
            os.makedirs(needPathShot)
        return needPathShot

    # 本地cache路径
    def checkCacheLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache

    # 服务器端cache路径
    def checkCacheServerPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.projFull
        projectPathBase = self.checkProjectServerPath()
        serverPathCache=''
        import re
        p_crwd = re.compile(u'crowd[a-zA-Z1-9]*')
        if shotType == 2:
            serverPathCache = projectPathBase + 'data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/'
            if project in ['DiveollyDive5','ShunLiu','LION'] and p_crwd.search(dirInfo[3]):
                serverPathCache = (projectPathBase + '/data/CROWDS_CACHE/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            serverPathCache = (projectPathBase + 'data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        return serverPathCache


    # 删除|加载 未勾选的参考
    def sk_sceneUnloadRefDel(self, deleteMode=1, reloadMode=0):
        refInfos = self.checkReferenceListInfo()
        if refInfos[0]:
            for i in range(len(refInfos[0][0])):
                loadInfo = mc.referenceQuery(refInfos[0][0][i], isLoaded=1)
                if loadInfo:
                    pass
                else:
                    if deleteMode:
                        mc.file(rfn=refInfos[0][0][i], removeReference=1)
                        mc.warning(u'===============【清理警告】未勾选的【%s】参考被清理完毕！===============' % (refInfos[0][0][i]))
                    if reloadMode:
                        mc.file(refInfos[1][0][i], loadReference=refInfos[0][0][i])

    # ------------------------------#
    # 全流程用
    def checkDonotNodeCleanBase(self, unuse=1, turtle=1):
        # 清理unusedNodes
        if unuse == 1:
            mel.eval('MLdeleteUnused')
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        for node in unknownNodes:
            if mc.ls(node):
                mc.lockNode(node, l=0)
                mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer') + mc.ls(type='ilrUIOptionsNode') + mc.ls(
            type='ilrOptionsNode') + mc.ls(type='ilrBakeLayerManager')
        if turtle and turtleNodes:
            for node in turtleNodes:
                # 非参考才执行删除
                if mc.referenceQuery(node, inr=1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)

   # ------------------------------#
    # 清理无用节点
    def checkDonotNodeClean(self, unuse=1, turtle=1,shotMode = 0):
        # 清理finalRender插件
        try:
            mel.eval('unloadPlugin "finalRender"')
        except:
            pass
            # 清理孙望参考
        # 清理无用SG节点
        if shotMode:
            sgNodes = mc.ls(type = 'shadingEngine')
            for checkSG in sgNodes:
                if checkSG in ['initialParticleSE','initialShadingGroup']:
                    continue
                inr = mc.referenceQuery(checkSG,inr=1)
                if inr:
                    continue
                meshes = mc.sets(checkSG,q=1)
                if meshes:
                    continue
                mc.lockNode(checkSG,l=0)
                mc.delete(checkSG)
        # 清理无用贴图节点
        if shotMode:
            nodeList = ['file','aiImage']
            for nodeType in nodeList:
                checkNodes = mc.ls(type = nodeType)
                for checkNode in checkNodes:
                    inr = mc.referenceQuery(checkNode,inr=1)
                    if inr:
                        continue
                    mc.lockNode(checkNode,l=0)
                    mc.delete(checkNode)
        # 清理unusedNodes
        if unuse:
            mel.eval('MLdeleteUnused')
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        for node in unknownNodes:
            if mc.ls(node):
                mc.lockNode(node, l=0)
                mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer') + mc.ls(type='ilrUIOptionsNode') + mc.ls(
            type='ilrOptionsNode') + mc.ls(type='ilrBakeLayerManager')
        if turtle:
            for node in turtleNodes:
                # 非参考才执行删除
                if mc.referenceQuery(node, inr=1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)

    # 清理OTC_GRP里非VFX_GRP和Cluster_GRP的非参考物体
    def sk_sceneNotRefMeshClean(self):
        otcGrp = '|OTC_GRP'
        if not mc.ls(otcGrp):
            return
        childGrps = mc.listRelatives(otcGrp,c=1,f=1)
        if not childGrps:
            return
        for checkGrp in childGrps:
            if checkGrp in ['|OTC_GRP|VFX_GRP','|OTC_GRP|Cluster_GRP']:
                continue
            if not mc.ls(checkGrp):
                continue
            if 'RNgroup' in checkGrp:
                mc.delete(checkGrp)
                continue
            inr = mc.referenceQuery(checkGrp,inr=1)
            if inr:
                continue
            childNodes = mc.listRelatives(checkGrp,ad=1,type = 'transform',f=1)
            if childNodes:
                for childGrp in childNodes:
                    if not mc.ls(childGrp):
                        continue
                    mesh = mc.listRelatives(childGrp,s=1,type= 'mesh',f=1)
                    if mesh:
                        mc.lockNode(childGrp,l=0)
                        mc.delete(childGrp)
                    if not mc.ls(childGrp):
                        continue
                    cam = mc.listRelatives(childGrp,s=1,type= 'camera',f=1)
                    if cam:
                        mc.lockNode(checkGrp,l=0)
                        mc.delete(checkGrp)
            else:
                mesh = mc.listRelatives(checkGrp,s=1,type= 'mesh',f=1)
                if mesh:
                    mc.lockNode(checkGrp,l=0)
                    mc.delete(checkGrp)
                if not mc.ls(checkGrp):
                    continue
                cam = mc.listRelatives(checkGrp,s=1,type= 'camera',f=1)
                if cam:
                    mc.lockNode(checkGrp,l=0)
                    mc.delete(checkGrp)

    def sk_sceneReorganize(self, finalLayout=0):
        # CAM_GRP
        checkGrp = '|CAM_GRP'
        if mc.ls(checkGrp):
            camGrp = checkGrp
        else:
            camGrp = mc.group(em=1, name=checkGrp.split('|')[1])
        if camGrp[0] not in ['|']:
            camGrp = '|' + camGrp
        # CHR_GRP
        if mc.ls('|CHR_GRP'):
            chrGrp = '|CHR_GRP'
        else:
            chrGrp = mc.group(em=1, name='CHR_GRP')
        if chrGrp[0] not in ['|']:
            chrGrp = '|' + chrGrp
        # PRP_GRP
        if mc.ls('|PRP_GRP'):
            prpGrp = '|PRP_GRP'
        else:
            prpGrp = mc.group(em=1, name='PRP_GRP')
        if prpGrp[0] not in ['|']:
            prpGrp = '|' + prpGrp
        # SET_GRP
        if mc.ls('|SET_GRP'):
            setGrp = '|SET_GRP'
        else:
            setGrp = mc.group(em=1, name='SET_GRP')
        if setGrp[0] not in ['|']:
            setGrp = '|' + setGrp
        # VFX_GRP
        if mc.ls('|VFX_GRP'):
            vfxGrp = '|VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        if vfxGrp[0] not in ['|']:
            vfxGrp = '|' + vfxGrp
        # 鱼群集群
        if mc.ls('|Cluster_GRP'):
            clusterFlowGrp = '|Cluster_GRP'
        else:
            clusterFlowGrp = mc.group(em=1, name='Cluster_GRP')
        if clusterFlowGrp[0] not in ['|']:
            clusterFlowGrp = '|' + clusterFlowGrp
        # OTC_GRP
        if mc.ls('|OTC_GRP'):
            otcGrp = '|OTC_GRP'
        else:
            otcGrp = mc.group(em=1, name='OTC_GRP')
        if clusterFlowGrp[0] not in ['|']:
            clusterFlowGrp = '|' + clusterFlowGrp
        # 打组
        if otcGrp not in mc.ls(vfxGrp, l=1)[0]:
            mc.parent(vfxGrp, otcGrp)
        if otcGrp not in mc.ls(clusterFlowGrp, l=1)[0]:
            mc.parent(clusterFlowGrp, otcGrp)
        if otcGrp[0] not in ['|']:
            otcGrp = '|' + otcGrp
        # 根组处理
        for checkKey in ['CHR_GRP','PRP_GRP','SET_GRP','OTC_GRP']:
            checkGrp = mc.ls(checkKey,l=1)[0]
            if len(checkGrp.split('|')) == 2:
                continue
            mc.parent(checkGrp,world = 1)
        # rootGrp
        refRoot = []
        refNodes = []
        refInfos = self.checkReferenceListInfo()
        for refLeval in refInfos[0]:
            refNodes = refNodes + refLeval
        for refNode in refNodes:
            # 全名处理
            refObjs = mc.referenceQuery(refNode, nodes=1, dagPath=1)
            # Q,need to test
            if not refObjs:
                continue
            for num in range(len(refObjs)):
                checkType = mc.nodeType(refObjs[num])
                if checkType in ['transform','stereoRigTransform']:
                    refRoot.append(refObjs[num])
                    break
        # needRoot
        needRoot = ['persp', 'top', 'front', 'side', 'CAM_GRP', 'CHR_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        keepRoot = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP', 'persp', 'top', 'front', 'side']
        # 开始处理
        # 优先记录：带有namespace的基本GRP
        ogGrp = ['CHR_GRP', 'CAM_GRP', 'PRP_GRP', 'SET_GRP', 'OTC_GRP']
        ogNsGrp = []
        for grp in ogGrp:
            checkGrps = mc.ls(('*:*' + grp + '*'), l=1) + mc.ls(('*:*:*' + grp + '*'), l=1)
            for obj in checkGrps:
                inr = mc.referenceQuery(obj,inr = 1)
                if inr:
                    continue
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
                    if ( camGrp + '|') not in mc.ls(root, l=1)[0]:
                        mc.parent(root, camGrp)
                # CHR
                if '/characters/' in path:
                    # 判断是否在CHR_GRP组里
                    if (chrGrp + '|') not in mc.ls(root, l=1)[0]:
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
                if '/props/' in path:
                    # 判断是否在PRP_GRP组里
                    if (prpGrp + '|') not in mc.ls(root, l=1)[0]:
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
                if '/sets/' in path or '/environments/' in path or '/locations/' in path:
                    # 判断是否在SET_GRP组里
                    if (setGrp + '|') not in mc.ls(root, l=1)[0]:
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
            for ns in ogNsGrp:
                self.sk_deleteNamespace(ns)

    def sk_deleteNamespace(self,namespace):
        ns = namespace
        try:
            # 使得namespace成为空的namespace
            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
            # 清理空namespace
            mc.namespace(removeNamespace= (':' + ns))
        except:
            pass

    # 服务器端camera路径
    def checkCameraServerPath(self,dirInfo = []):
        # mel用
        if not dirInfo:
            dirInfo = self.checkShotInfo()
        projectPathBase = self.checkProjectServerPath()
        ServerPathCamera = projectPathBase + 'scenes/Animation/episode_' + str(dirInfo[1]) + '/episode_camera/'
        return ServerPathCamera

    def camServerReference(self,info = 2):
        shotInfo = self.checkShotInfo()
        info = self.shotType
        projectInfo = self.projFull
        # serve目录
        camServerPath = self.checkCameraServerPath()
        camFileKey = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        import  os
        if info == 3:
            camFileKey = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        camServerFilePath = camServerPath + camFileKey + '_cam.ma'
        # 玩偶奇兵切换，一个文件只能一个camera
        if shotInfo[0] in ['mi']:
            camKeyList = ['_near','_mid','_far']
            tempFileInfo = ''
            for camKey in camKeyList:
                checkFile = camServerPath + camFileKey + camKey + '_cam.ma'
                if not os.path.exists(checkFile):
                    continue
                tempFileInfo = checkFile
                if tempFileInfo:
                    camServerFilePath = tempFileInfo
                    break
        # 开始参考
        refPaths = mc.file(reference = 1,q=1)
        camIn = 0
        import re
        for refPath in refPaths:
            #if camServerFilePath in refPath:
            if re.search('^' + re.escape(camServerFilePath) + '$', refPath, re.IGNORECASE) != None:
                camIn =1
        # 无则导入参考相机
        if camIn == 0:
            mc.file(camServerFilePath,reference = 1,ignoreVersion=1,namespace='CAM')
        # 有则重载入相机
        if camIn == 1:
            refNode = mc.referenceQuery(camServerFilePath,referenceNode=1)
            # 清除
            mc.file(rfn=refNode , removeReference=1)
            #载入
            mc.file(camServerFilePath,reference = 1,ignoreVersion=1,namespace='CAM')

    # 本地finalLayout路径
    def checkFinalLayoutLocalPath(self,shotType = 2):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        if shotType == 3:
            localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/' + str(dirInfo[3]) + '/')
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout

    # 获取otc里参考物体列表
    def otcRefCheck(self):
        refInfos = self.checkReferenceListInfo()
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
