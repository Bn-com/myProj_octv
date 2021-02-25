# -*- coding: utf-8 -*-
'''
Created on 2014
@author: hanhong
Updated to V2 2016-2017 ShenKang
'''
import maya.cmds as mc
import maya.mel as mel
from pymel.core import *
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig

reload(sk_infoConfig)
import time

from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)

from idmt.maya.commonCore.core_mayaCommon import sk_backCmd
reload(sk_backCmd)

import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)

from idmt.maya.py_common import GA_Tools
reload(GA_Tools)

import os
class GDCAlembicCommon(object):
    def __init__(self):
        self.tempNs = '_sysTemp'
        self.tempBlend = 'foodBlend_'
        self.abcGrp = 'Alembic_T_Grp'
        self.pointLimit = -4

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def GDCAlembicCommonUI(self):
    # 窗口
        if mc.window('ABCcrowd', exists=True):
            mc.deleteUI('ABCcrowd')
        mc.window('ABCcrowd', title=u'ABC面板',
                  width=320, height=350, sizeable=True)
         # 面板
        form = mc.formLayout()
         # 切换面板
        tabs = mc.tabLayout('tabArnold',innerMarginWidth=5, innerMarginHeight=5)
        mc.formLayout(
            form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))
         # tab_渲染工具
        child1 = mc.columnLayout(adjustableColumn=True)
        mc.frameLayout(label=u'创建ABC', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.intSliderGrp('framemin',label='frammin', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(min=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))
        mc.intSliderGrp('framemax', label='frammax', field=True, minValue=-1000, maxValue=10000, fieldMinValue=-1000, fieldMaxValue=10000, value=mc.playbackOptions(max=1,q = 1),columnAttach=[(1,'left',40),(2,'left',0),(3,'both',0)],columnWidth3 = (100,60,150))
        mc.button(label=u'导出alembic', width=130, height=30,
                   command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicExr(server = 1,cachePre = 0,shotType = 1,ap=1,,UI=1)')
        mc.button(label=u'alembic属性添加', width=130, height=30,
                 command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicApply()')

        mc.button(label=u'一键式创建alembic', width=130, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().GDC_alembicImp(line="pre",server = 1,shotType = 1)')
        mc.setParent('..')
        mc.frameLayout(label=u'Edit(Select)', bgc=[0, 0, 0.0], borderStyle='in', cll=0,cl=0)
        mc.rowColumnLayout(numberOfColumns=1)
        mc.button(label=u'群组大组整理', width=130, height=30,
                 command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusterGroupR()')
        mc.rowColumnLayout(numberOfColumns=2)

        mc.intSliderGrp('offset',width=200,label='offset', field=True, minValue=-1000, maxValue=1000, fieldMinValue=-1000, fieldMaxValue=1000, value=0,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=1,sd=0)')



        mc.floatSliderGrp('speed',width=280,label='speed', field=True, minValue=0, maxValue=100, fieldMinValue=0, fieldMaxValue=100, value=1,columnAttach=[(1,'left',10),(2,'left',0),(3,'both',0)],columnWidth3 = (60,60,70))
        mc.button(label=u'set', width=30, height=30,
                  bgc=[0.13, 0.15, 0.25], command='from idmt.maya.py_common import GDC_alembicCommon\nreload(GDC_alembicCommon)\nGDC_alembicCommon.GDCAlembicCommon().gdc_clusteroffset(ot=0,sd=1)')
        #  Tab
        mc.tabLayout(tabs, edit=True, tabLabel=(child1, u'群组插件'))
        mc.showWindow('ABCcrowd')

    #------------------------------#
    # 【通用】【FS后台工具】【核心】(改自Final工具）
    #  Author  : 韩虹
    #  Data    : 2015_03
    #  升级修正  : 沈康 2016-2017
    #  升级: 支持多项目ProjStyle 沈康 2018(该死的华强规则,东施效颦)
    #  abcBy_ns 按asset模式输出: 0(整体版)-do5;1-应用项目-csl;2-mtd短片
    #  assetFrameDict = {'id':[stFrame,edFrame]}
    #  shapeMode: 专为blend模式服务 0为继承UV传递Shape , 1为继承Shape
    #------------------------------#
    def GDC_FinaloutABC(self,server = 1,cachePre = -10,shave = 1,abcBy_ns = 2,justCache = 0,bkMode = 1,
                        assetFrameDict = {},printMode = 1,shapeMode = 1,eulerFilter = 1,projStyle = 0):
        from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
        reload(sk_hbExportCam)
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)

        import os
        mc.cycleCheck(e = False)
        print('\n-------------All Start-------------')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

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
        # 参考修正
        from idmt.maya.commonPerform.projectTools import sk_projTools_base
        reload(sk_projTools_base)
        sk_projTools_base.sk_projTools_base().refReplacePerform(stepMode = 'fs')
        #---------------------------#
        # Setup 001  多级非参考的namespace清理。
        # 某些外包，喜欢做动作模板，然后import进来，这样形成了两级namespace，而在参考是不会记录import的那级参考。
        # 这种情况，要处理掉，不然后面记录参考信息时会出问题
        #---------------------------#
        # 处理非参考的namespace
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        #大组整理
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
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

        if printMode:self.testDef('---001')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        fsType = 1
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0],finalLayout = fsType)
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()

        fileDict = {}
        if projStyle in [2]:
            fileFormat = '.ma'
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfos,projStyle = projStyle)
        print(u'\n')
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 修正时间轴
        if server:
            sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame',shotType,projStyle = projStyle)

        # 项目特殊情况
        if shotInfos[0] in ['mk']:
            cachePre = -51
            shapeMode = 1

        #---------------------------#
        # 强制开启Stretch_Mesh属性
        #self.stretch_attr()
        #---------------------------#
        # Setup 004  本地另存，备份
        #---------------------------#
        # 获取FS临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,projStyle = projStyle)

        if printMode:self.testDef('---002')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 本地另存
        shotName = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType in [3]:
            shotName = '%s_%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
        if projStyle not in [1]:
            shotName = fileDict['shotID']
        bakLocalFile = localPath + shotName+'_an_c001' + fileFormat
        if projStyle in [2]:
            bakLocalFile = '%s%s_%s_%s_%s_an(test)%s'%(localPath,shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3],fileFormat)
        mc.file(rename = bakLocalFile)
        mc.file(save=1,force = 1,type = sk_infoConfig.sk_infoConfig().formatInfo[fileFormat])
        
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        #---------------------------#
        # Setup 005  清理外包残留的playblast表达式
        #---------------------------#
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print(u'\n')
            print(u'====================【zwHeadsUpDisplay】清理完毕====================')
            print(u'\n')

        if printMode:self.testDef('---003')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 006  清理未勾选的参考，清理垃圾节点，更新camera，IKR再启动
        #---------------------------#
        sk_sceneTools.sk_sceneTools().sk_sceneUnloadRefDel(1,0)
        print(u'\n')
        print(u'========================未勾选参考清理完毕========================')
        print(u'\n')

        # 初步清理垃圾节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(unuse=1 , turtle=1)
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print(u'\n')
        print(u'=========================IK解算器强制更新========================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print(u'\n')
        # 更新摄像机
        projSimp = shotInfos[0]
        if projStyle in [2]:
            projSimp = '%s_%s'%(shotInfos[0],shotInfos[1])
        #projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projSimp)
        if server:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate = 1,projStyle = projStyle)
            print(u'\n')
            print(u'==========================camera传输完毕==========================')
            print(u'\n')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---005')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 007  约束烘焙
        #---------------------------#
        #预处理，约束清理
        print('-------------bkStart')
        print(mc.playbackOptions(min=True,q=True))
        print(mc.playbackOptions(max=True,q=True))

        if bkMode:
            self.sk_checkBakeConstraints(preFrame = cachePre)

        if printMode:self.testDef('---005a')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 处理贴图动画
        self.sk_checkTextureAnimationExport(server,projStyle = projStyle)
        print('-------------bkEnd')
        print(mc.playbackOptions(min=True,q=True))
        print(mc.playbackOptions(max=True,q=True))
        print(u'========================【约束】【烘焙】【成功】========================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---006')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 008 清除服务器data目录残留的SET和OTC文件
        # 【注意】 如果有SD环节，酌情清理OTC，SET需要从服务器端参考
        #---------------------------#
        # 记录特效用物体,VFX物体
        vfxObjs = []
        vfxDL = 'VFX_REF'
        if mc.ls(vfxDL):
            vfxObjs = mc.editDisplayLayerMembers(vfxDL,fullNames = 1,q=1)
        if not vfxObjs:
            vfxObjs = []
        if vfxObjs:
            vfxObjs = mc.ls(vfxObjs,l=1)
        # 非参考物体清理
        self.sceneNotRefMeshClean(vfxObjs)

        if printMode:self.testDef('---007')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        #清理插件

        #if shotInfos[0] in ['do6']:
        #    GA_Tools.GA_Tools().GA_unknownPluginDel(1,'mayaBinary')
        # 清理服务器端旧的SET和OTC文件
        self.sk_sceneGRPDelete(fileGRP = 'SET',server = server,projStyle = projStyle)
        self.sk_sceneGRPDelete(fileGRP = 'OTC',server = server,projStyle = projStyle)
        #---------------------------#
        # Setup 009 文件内部大组归类
        #---------------------------#
        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(finalLayout = 0,projStyle = projStyle)
        # 记录otc参考
        otcRefList = self.otcRefCheck()
        # 导出多相机信息
        sk_cacheFinalLayout.sk_cacheFinalLayout().displayLayerInfoExport(projStyle = projStyle)
        print(u'\n')
        print(u'==========================文件整理完毕==========================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print(u'\n')

        if printMode:self.testDef('---008')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 010 动画文件内，隐藏的物体，记录下来，cache之后恢复隐藏 0
        #---------------------------#
        unDisplayLayerObjs = self.sk_FL_RefHideObjsRecord(server=server,shotType=shotType,projStyle = projStyle)
        # 记录cacheDict
        cacheDict = {}
        yetiNodes = mc.ls(type = 'pgYetiMaya')
        for checkNode in yetiNodes:
            attrKey = 'cacheFileName'
            cachePath = mc.getAttr('%s.%s'%(checkNode,attrKey))
            if not cachePath:
                continue
            cacheDict[checkNode] = [attrKey,cachePath]

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
        self.sk_sceneGRPExport(fileGRP = 'SET',server = server,shotType = shotType ,
                               needNsList = [],projStyle = projStyle)
        self.sk_sceneGRPExport(fileGRP = 'OTC',server = server,shotType = shotType ,
                               needNsList = otcRefList,projStyle = projStyle)

        if printMode:self.testDef('---009')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        print(u'\n')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print(u'\n')

        #---------------------------#
        # Setup 015 删除set参考，加快速度
        #---------------------------#
        # 首先删除set参考，加快速度
        '''
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        '''
        print(u'\n-------------------------')
        print('[Ref Info]')
        print(refInfos[0][0])
        print(u'-------------------------')

        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        # 判断是否ms_anim文件
        if projStyle in [1]:
            if shotType in [2] and shotInfos[3] in ['an','sa','dy'] and refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
                print(u'\n')
                print(u'=====================【SET类参考】【清理】完毕=====================')
                print(u'\n')
            if shotType in [3] and shotInfos[4] in ['an','sa','dy'] and refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
                print(u'\n')
                print(u'=====================【SET类参考】【清理】完毕=====================')
                print(u'\n')
        if projStyle in [2]:
            if shotInfos[4].split('(') in ['an','sa','dy'] and refNodes:
                for ref in refNodes:
                    if '_' not in ref:
                        continue
                    if ref.split('_')[2] in ['BG']:
                        # 删除参考
                        mc.file(rfn=ref, removeReference=1)
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---010')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 016 输出cache，以及传递动画的控制器动画
        # cache过程中，加入了对隐藏|组K帧物体的检测，记录显示隐藏动画以便还原
        #---------------------------#
        # 特告梁宇:由于你不是选组导出的cache,而是按物体选的导出，而设置是用组约束的显示隐藏，因此物体根本不能通过abc继承显示隐藏！
        #---------------------------#
        # 输出显示隐藏动画信息
        self.checkCacheVStateExport([],shotType,server = server ,projStyle = projStyle )
        print(u'\n')
        print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
        print(u'\n')
        if printMode:self.testDef('---010a')
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        # 输出ABC
        if printMode:self.testDef('---010b')
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        # mesh abc export
        addAttrState = 0
        if shotInfos[0] in ['do5']:
            addAttrState = 1
        if abcBy_ns in [1] and shotInfos[0] not in ['mi']:
            addAttrState = 1
        if abcBy_ns in [2]:
            addAttrState = 1
        if addAttrState:
            self.abc_AttrAdd(projStyle = projStyle)
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            # 输出cache
            # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
            if abcBy_ns:
                self.checkAbcCacheExport(cacheObjs,server=server,exportType='mesh',cachePre = cachePre,step=1,
                        assetFrameDict = assetFrameDict,abcBy_ns = abcBy_ns,eulerFilter = eulerFilter,projStyle = projStyle)
            else:
                self.GDC_alembicExr(server,0,shotType,0,0)
            print(u'\n')
            print(u'=====================【alembic】【服务器端】【输出】完毕=====================')
            print(u'\n')
        else:
            print(u'\n')
            print(u'=====================【alembic】无物体！！！！！！=====================')
            print(u'\n')
        if printMode:self.testDef('---010c')
        if printMode:print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        # curve abc export
        curveObjs= self.GDC_shaveInfo(3,'curve')
        if shave and curveObjs:
            if  abcBy_ns:
                self.checkAbcCacheExport(curveObjs,server=server,exportType='curve',cachePre = cachePre,step=1,
                        assetFrameDict = assetFrameDict,abcBy_ns = abcBy_ns,eulerFilter = eulerFilter,projStyle = projStyle)
            else:
                self.GDC_shavealembicExr(server,shotType)
            print(u'\n')
            print(u'=====================【abc_curve】【服务器端】【输出】完毕=====================')
            print(u'\n')
        else:
            print(u'\n')
            print(u'=====================【abc_curve】无物体！！！！！或 不需要输出curve 的abc 缓存==========================')
            print(u'\n')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---011')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        if justCache:
            return

        #---------------------------#
        # Setup 017 对动画文件的处理告一段落，这里处理SET和OTC里面的参考替换，同时清理参考材质覆盖
        #---------------------------#
        # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
        # 先处理删除导出，再处理Set文件
        if shotInfos[0] in ['mtd']:
            print('-----ExportPaperMather')
            from idmt.maya.commonPerform.projectTools import sk_projTools_mtd
            reload(sk_projTools_mtd)
            sk_projTools_mtd.sk_projTools_mtd().mtdExportExtra(server)

        self.sk_sceneSETRefShaderReset(shotInfos,serverModify = server , shotType =shotType,projStyle = projStyle)

        #---------------------------#
        # Setup 018 开始新文件的架构
        #---------------------------#
        mc.file(f=1, new=1)
        # 关闭材质球更新
        mc.renderThumbnailUpdate(False)
        print('\n')
        print('[Ref Info]')
        print(refInfos[0][0])
        print('\n')
        print(u'=========================【创建新文件】=========================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        print('\n')

        if printMode:self.testDef('---012')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 准备先另存，因为update需要用到文件名
        fileName = shotName +'_base_fs_c001' + fileFormat
        if projStyle in [2]:
            fileName = shotName + '_fs' + fileFormat
        # 本地文件
        fsLocalFile = localPath + fileName
        # 服务器端文件
        # serverFile = serverPath + fileName
        # 重命名
        mc.file(rename= fsLocalFile )
        mc.file(save = 1 ,force = 1,type = sk_infoConfig.sk_infoConfig().formatInfo[fileFormat])

        #---------------------------#
        # Setup 019 先导入OTC及SET，后创建参考。这里OTC和SET默认不加载，提高速度
        #---------------------------#
        # 导入场景
        # 必须先导入OTC，后载入参考，否则容易出错(PORORO经验)
        # 导回SET_GRP和OTC_GRP
        self.sk_sceneGRPImport(fileGRP = 'SET',server = server,shotType = shotType,projStyle = projStyle)
        self.sk_sceneGRPImport(fileGRP = 'OTC',server = server,shotType = shotType,projStyle = projStyle)

        print(u'\n')
        print(u'=====================【Group】【服务器端】【导入】完毕=====================')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        #---------------------------#
        # Setup 020 加载需要的角色和道具类的render参考
        #---------------------------#
        # 导入reference及share nodes（新导入场景，后导入参考）
        self.sk_FLRefRebuild(refInfos,noNeedRefNodeInfo,projStyle = projStyle)
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        #---------------------------#
        # Setup 021 参考最终相机
        #---------------------------#
        # 导入cam
        # 导入相机 modify
        sk_hbExportCam.sk_hbExportCam().camServerReference(info=shotType,projStyle = projStyle)

        if printMode:self.testDef('---013')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # Setup 022 新建后的文件大组重新处理
        #---------------------------#
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(1,projStyle = projStyle)
        if shotInfos[0] in ['mtd']:
            print('-----ImportPaperMather')
            from idmt.maya.commonPerform.projectTools import sk_projTools_mtd
            reload(sk_projTools_mtd)
            sk_projTools_mtd.sk_projTools_mtd().mtdImportExtra(server)

        if printMode:self.testDef('---013a')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 023 动画文件和fl文件的cache list对比，不一致则报错。
        # 这里不一致一般在两种情况里发生
        # 1,anim文件和render文件cache list不一致;
        # 2.约束bake失败，某些CHR和PROP和SET有约束残留，导出去的时候CHR,PROP进了SET文件，而SET文件是默认不加载的，丢失部分cacheList
        #---------------------------#
        # 场景搭建完毕
        # 备份材质

        MatLists = self.checkCacheRecordMaterial(finalLayout=1,shotType = shotType,projStyle = projStyle)

        if printMode:self.testDef('---013b')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 清理blend
        self.checkCacheCleanBlendShapes()

        # 处理buging
        # 载入cache及自带的anim
        addAttrState = 0
        if abcBy_ns in [1] and shotInfos[0] not in ['mi']:
            addAttrState = 1
        if abcBy_ns in [2]:
            addAttrState = 1
        if addAttrState:
            self.abc_AttrAdd(projStyle = projStyle)
        if printMode:self.testDef('---013c')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        # 所有transform数值归0
        if abcBy_ns in [2]:
            self.transformNodeGoZero(projStyle = projStyle)

        # transform
        #if abcBy_ns in [2]:
        #    self.GDC_alembicImp('fs',server,shotType = shotType,abcBy_ns = abcBy_ns,replaceMode = 1,checkType = 'trans')
        #    self.assetAbcRebuild(checkType = 'trans',shotName = shotID,server = server,abcBy_ns = abcBy_ns)
        #if printMode:self.testDef('---013d')
        #print('\n') + time.strftime('%Y-%m-%d %H:%M:%S') + '\n'
        # mesh
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            self.GDC_alembicImp('fs',server,shotType = shotType,abcBy_ns = abcBy_ns,
                                replaceMode = 1,checkType = 'mesh',projStyle = projStyle)
            print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
            if abcBy_ns:
                self.assetAbcRebuild(checkType = 'mesh',shotName = shotID,server = server,abcBy_ns = abcBy_ns,
                                shapeMode = shapeMode,projStyle = projStyle)
            else:
                #mesh abc按replace方式进行连接  梁宇
                #if projectInfo in ['North','MiniTiger','ShunLiu']:
                self.LY_alembicMeshImp()
            # 处理还原物体
            # 进行参考reload
            for i in range(len(rfnLv1)):
                ns = refInfos[2][0][i]
                refNode = refInfos[0][0][i]
                if noNeedRefNodeInfo:
                    if refNode not in noNeedRefNodeInfo:
                        print(u'=================')
                        print(refNode)
                        print(noNeedRefNodeInfo)
                        print(u'=================')
                        newPath = mc.referenceQuery(refNode, filename=True)
            if server:
                print(u'\n')
                print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                print(u'\n')
            else:
                print(u'\n')
                print(u'=====================【Cache】【本地】【导入】完毕=====================')
                print(u'\n')
        else:
            print(u'\n')
            print(u'=====================【Cache】无物体！！！！！！！=====================')
            print(u'\n')
        if printMode:self.testDef('---013e')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # curve
        if shave==1:
            curveObjs=self.GDC_shaveInfo(3,'curve')
            if curveObjs:
                if not abcBy_ns:
                    mc.select(curveObjs)
                self.GDC_curvealembicImp(server,abcBy_ns = abcBy_ns,projStyle = projStyle)
                if abcBy_ns:
                    self.assetAbcRebuild(checkType = 'curve',shotName = shotID,server = server,
                                         abcBy_ns = abcBy_ns,projStyle = projStyle)
                else:
                    #曲线abc按replace方式进行连接  梁宇
                    self.LY_alembicCurveImp()
                # rebuild
                for checkCurve in curveObjs:
                    mc.rebuildCurve(checkCurve,ch =1,rpo=1,rt=0,end=1,kr=0,kcp=0,kep=1,kt=0,s=0,d=3,tol=0.01)
                print(u'\n')
                print(u'=====================【abc_curve】【服务器端】【导入】完毕=====================')
                print(u'\n')
            else:
                print(u'\n')
                print(u'=====================【abc_curve】无物体！！！！！！=====================')
                print(u'\n')

        if printMode:self.testDef('---015')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 清理非参考namespace
        if abcBy_ns in [1]:
            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # renderState fix
        if abcBy_ns in [1]:
            self.checkRenderStateRebuild()

        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        # 还原cache属性
        cacheNodes = cacheDict.keys()
        for checkNode in cacheNodes:
            attrKey = cacheDict[checkNode][0]
            cachePath = cacheDict[checkNode][1]
            objType = mc.nodeType(checkNode)
            mc.setAttr('%s.%s'%(checkNode,attrKey),cachePath,type = 'string')
            if objType in ['pgYetiMaya']:
                mc.setAttr('%s.%s'%(checkNode,'fileMode'),2)
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

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
        # VFX层处理
        if vfxObjs:
            if not mc.ls(vfxDL):
                mc.createDisplayLayer(empty = 1, name = vfxDL)
            needObjs = []
            for checkObj in vfxObjs:
                if not mc.ls(checkObj):
                    continue
                needObjs.append(checkObj)
            if needObjs:
                mc.editDisplayLayerMembers(vfxDL,needObjs , nr = 1)

        print(u'\n')
        print(u'=====================【Displayer】隐藏恢复=====================')
        print(u'\n')
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---016')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 清理未知节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeCleanBase(0)

        # 强行还原材质
        returnMaterialMode = 0
        if shotInfos[0] in ['LION','mtd']:
            returnMaterialMode = 1
        if returnMaterialMode:
            self.checkCacheReturnMaterial(MatLists,finalLayout = 1, shotType = shotType)

        if printMode:self.testDef('---017')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 025 备份FL文件
        #---------------------------#
        # 本地保存
        mc.file(force=1, options="v=0",save = 1, type=sk_infoConfig.sk_infoConfig().formatInfo[fileFormat])

        # 设置时间轴等消息
        # 命令
        shot = ''
        if projStyle in [1]:
            shot = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
            if shotType == 3:
                shot = '%s_%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
        if projStyle not in [1]:
            shot = fileDict['shotID']
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---018')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

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
        mc.setAttr('defaultResolution.width', resW)
        mc.setAttr('defaultResolution.height', resH)
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

        # 允许undo
        mc.undoInfo(state=True, infinity=True)

        description = 'FinalLayout Base File | AssetMode:%s'%abcBy_ns

        if printMode:self.testDef('---019')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 烘焙表情贴图~
        self.checkCacheBakeTexAniFiles()

        # 处理贴图动画
        self.sk_checkTextureAnimationImport(server)

        # 属性处理
        fixNodes = mc.ls(type = 'aiStandIn',l=1)
        for fixNode in fixNodes:
            pNode = mc.listRelatives(fixNode,p=1,type='transform',f=1)
            if not pNode:
                continue
            mc.setAttr(pNode[0]+'.v',1)

        # 导入显示隐藏信息,必须放这，不然会被帧初始化干掉时间轴
        self.checkCacheVStateImport(shotType,server,projStyle = projStyle)
        mc.setAttr('defaultResolution.pixelAspect', 1.00)

        #if projStyle in [2]:
        #    fileNameNew = mc.file(exn=1,q=1).split('/')[-1].replace('_fs','_fs(%s-%s)'%(startFrame,endFrame))
        #    mc.file(rename = (localPath + fileNameNew))
        mc.file(save=1, force = 1)
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if printMode:self.testDef('---020')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 029
        #---------------------------#

        # 缺少check in baseFile
        if os.path.exists(bakLocalFile):
            mc.sysFile(bakLocalFile,delete=True)
        print('\n')
        print(u'=========================================================================')
        print(u'=====================【%s_%s_%s】【FinalLayout】重构完毕====================='%(shotInfos[1],shotInfos[2],shotInfos[3]))
        print(u'=====================【%s】文件处理完毕====================='%(localPath + shotName+'_base_fs_c001' + fileFormat))

        if printMode:self.testDef('---021')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))

        #---------------------------#
        # Setup 030 本地备份之后，check in
        #---------------------------#
        # 上传服务器处理
        if server == 1:
            # 开始提交文件至服务器
            # 用户名
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projSimp = newInfo[0]
            if projStyle in [2]:
                projSimp = '%s_%s'%(newInfo[0],newInfo[1])
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projSimp)
            fileInfo = ''
            if projStyle in [1]:
                fileInfo = '2|%s|%s_%s_%s_%s|%s'%(projectInfo,newInfo[0],newInfo[1],newInfo[2],newInfo[3].split('.')[0],userName)
                if shotType in [3]:
                    fileInfo = '2|%s|%s_%s_%s_%s_%s|%s'%(projectInfo,newInfo[0],newInfo[1],newInfo[2],newInfo[3],newInfo[4],userName)
            if projStyle in [2]:
                #fileInfo = '2|%s|%s_%s_%s_%s_%s(%s_%s)|%s'%(projectInfo,newInfo[0],newInfo[1],newInfo[2],newInfo[3],newInfo[4],startFrame,endFrame,userName)
                fileInfo = '2|%s|%s_%s_%s_%s_%s|%s'%(projectInfo,newInfo[0],newInfo[1],newInfo[2],newInfo[3],newInfo[4],userName)
            print('shotType: %s  fileInfo: %s' % (shotType, fileInfo))
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print(checkOutCmd)
            import maya.mel as mel
            mel.eval(checkOutCmd)
            # checkIn
            checkInCmd = 'idmtProject -checkin -description \" ' + description + '\"'
            #print(checkInCmd)
            mel.eval(checkInCmd)

        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        print(u'\n')
        print(u'\n')
        print(u'=========================================================================')
        print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))

    #-----------------------------#
    # abc 导出
    # #选中版
    #-----------------------------#
    def checkAbcCacheExport(self,objsCache, server = 1,exportType = 'mesh' ,cachePre = 0 ,step = 1,
                            assetFrameDict = {} ,abcBy_ns = 1,eulerFilter = 1,projStyle = 0):
        if not objsCache:
            return
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        nsObjs = {}
        for checkObj in objsCache:
            inr = mc.referenceQuery(checkObj,inr = 1)
            if not inr:
                continue
            ns = checkObj.split('|')[-1].split(':')[0]
            if ns not in nsObjs.keys():
                nsObjs[ns] = [checkObj]
            else:
                nsObjs[ns].append(checkObj)

        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()

        localPath  = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 2.5,projStyle = projStyle)
        serverPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 2.5,projStyle = projStyle)
        fileList = []
        worldSpaceKey = ' -worldSpace '
        if abcBy_ns in [2] and exportType in ['mesh','curve']:
            worldSpaceKey = ' -worldSpace '
        abcRunCmdList = []
        for ns in nsObjs.keys():
            needObjs = nsObjs[ns]
            mc.select(needObjs)
            exportInfo = exportType
            if exportType in ['mesh']:
                exportInfo = 'alembic'
            if exportType in ['curve']:
                exportInfo = 'abc_curve'
            # file
            abcFile = '%s_%s.abc'%(ns,exportInfo)
            abcFile = '%s_%s_%s.abc'%(shotID,ns,exportInfo)
            if projStyle in [2]:
                abcFile = '%s_%s.abc'%(ns,exportInfo)
            abcLocalPath = localPath + abcFile
            if os.path.exists(abcLocalPath):
                mc.sysFile(abcLocalPath,delete = 1)
            print(abcLocalPath)
            startNeed = frameStart+cachePre
            endNeed = frameEnd
            assetID = ns.split('_')[1]
            if assetID in assetFrameDict.keys():
                infoTemp = assetFrameDict[assetID]
                startNeed = infoTemp[0]
                endNeed = infoTemp[1]
            rootObjs = ''
            if exportType in ['mesh','curve']:
                for obj in needObjs:
                    rootObjs = rootObjs + ' -root ' + mc.ls(obj,l=1)[0]
            if exportType in ['trans']:
                mc.select(needObjs)
                rootObjs = '-sl '
            if eulerFilter:
                runCmd = '-frameRange ' + str(startNeed) + ' ' + str(endNeed) + ' -step ' + str(step) + ' -uvWrite' + worldSpaceKey+ '-writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath
            else:
                runCmd = '-frameRange ' + str(startNeed) + ' ' + str(endNeed) + ' -step ' + str(step) + ' -uvWrite' + worldSpaceKey+ '-writeVisibility ' + rootObjs + '  -file ' + abcLocalPath
            if exportType in ['trans']:
                cacheCMD =  'AbcExport -verbose -j "-frameRange ' + str(startNeed)  + ' ' + str(endNeed) + ' -step ' + str(step) + ' -uvWrite' + worldSpaceKey+ '-writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath + '\"'
                print(cacheCMD)
                mel.eval(cacheCMD)
            else:
                abcRunCmdList.append(runCmd)
                fileList.append([(localPath + abcFile),(serverPath + abcFile)])
        if abcRunCmdList:
            mc.AbcExport(verbose = 1,j = abcRunCmdList)
        if server:
            for info in fileList:
                sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',info[0],info[1])
                print('--------------abcFile')
                print(info[0])
                print(info[1])
        else:
            print('--------------localFile')
            print(localPath)

    # nsList指定输出
    def checkAbcCacheExportByNs(self,needTypes = ['c','p'],checkNsList = [],server=1,exportType = 'mesh',
                                st = 0,et = 0,step = 1,bkMode = 1,eulerFilter = 1,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        # 处理大组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0,projStyle = projStyle)
        # 约束
        if bkMode:
            self.sk_checkBakeConstraints()
        self.abc_AttrAdd(projStyle = projStyle)
        objsCache = self.GDC_alembicInfo(3)
        if exportType in ['curve']:
            objsCache = self.GDC_shaveInfo(3,'curve')
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

        shotID = sk_infoConfig.sk_infoConfig().checkShotID()

        localPath  = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 2.5,projStyle = projStyle)
        serverPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 2.5,projStyle = projStyle)
        fileList = []
        abcRunCmdList = []
        for ns in nsObjs.keys():
            needObjs = nsObjs[ns]
            mc.select(needObjs)
            exportInfo = exportType
            if exportType in ['mesh']:
                exportInfo = 'alembic'
            if exportType in ['curve']:
                exportInfo = 'abc_curve'
            # file
            abcFile = '%s_%s.abc'%(ns,exportInfo)
            abcFile = '%s_%s_%s.abc'%(shotID,ns,exportInfo)
            if projStyle in [2]:
                abcFile = '%s_%s.abc'%(ns,exportInfo)
            abcLocalPath = localPath + abcFile
            if os.path.exists(abcLocalPath):
                mc.sysFile(abcLocalPath,delete = 1)
            print(abcLocalPath)
            rootObjs = ''
            for obj in needObjs:
                rootObjs = rootObjs + ' -root ' + mc.ls(obj,l=1)[0]
            if eulerFilter:
                runCmd = '-frameRange ' + str(frameStart)  + ' ' + str(frameEnd) + ' -step ' + str(step) + ' -uvWrite -worldSpace -writeVisibility -eulerFilter ' + rootObjs + '  -file ' + abcLocalPath
            else:
                runCmd = '-frameRange ' + str(frameStart)  + ' ' + str(frameEnd) + ' -step ' + str(step) + ' -uvWrite -worldSpace -writeVisibility ' + rootObjs + '  -file ' + abcLocalPath
            abcRunCmdList.append(runCmd)
            fileList.append([(localPath + abcFile),(serverPath + abcFile)])
        if abcRunCmdList:
            mc.AbcExport(verbose = 1,j = abcRunCmdList)
        if server:
            for info in fileList:
                sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',info[0],info[1])
                print('--------------abcFile')
                print(info[0])
                print(info[1])
        else:
            print('--------------localFile')
            print(localPath)

    # 手动选物体，转nslist输出
    def checkAbcCacheExportByNsSel(self,needTypes = ['c','p'],server=1,exportType = 'mesh',st = 0,et = 0,step = 1,bkMode = 1,projStyle = 0):
        selObjs = mc.ls(sl=1,l=1)
        checkNsList = []
        for checkObj in selObjs:
            checkObj = checkObj.split('|')[-1]
            if ':' not in checkObj:
                continue
            ns = checkObj.split(':')[0]
            if ns in checkNsList:
                continue
            checkNsList.append(ns)
        if checkNsList:
            self.checkAbcCacheExportByNs(needTypes = needTypes,checkNsList = checkNsList,server=server,
                    exportType = exportType,st = st,et = et,step = step,bkMode = bkMode,projStyle = projStyle)

    #---------------------------------------------------------#
    # transformNode归零
    def transformNodeGoZero(self,minCheck = -3,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        transNode = mc.ls(type = 'transform',l=1)
        attrDict = {'.tx':0,'.ty':0,'.tz':0,'.rx':0,'.ry':0,'.rz':0,'.sx':1,'.sy':1,'.sz':1}
        for checkNode in transNode:
            if projStyle in [2]:
                renderGrp = ':MODEL|'
                nsInfo = checkNode.split('|')[-1].split(':')[0]
                if 'CH_' in nsInfo:
                    renderGrp = ':Moldel_Hight|'
                if 'BG_' in nsInfo:
                    renderGrp = ':SCENES|'
                if renderGrp not in checkNode:
                    continue
            inr = mc.referenceQuery(checkNode,inr = 1)
            if not inr:
                continue
            shape = mc.listRelatives(checkNode,s=1)
            if shape:
                continue
            for checkAttr in attrDict.keys():
                valueNow = mc.getAttr(checkNode+checkAttr)
                if abs(valueNow-attrDict[checkAttr]) > 5*pow(10,minCheck):
                    mc.setAttr(checkNode+checkAttr,attrDict[checkAttr])

    #---------------------------------------------------------#
    # asset abc replace  沈康 2016.4
    # 本来是万能型，但是要匹配finallayout主体分为mesh和nurbs，故加参数,extra
    def assetAbcRebuild(self,checkType = 'mesh',shotName = '',server = 1,abcBy_ns = 2,clean = 1,printMode = 0,shapeMode = 0,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        nsList = self.getNsListOfFile(projStyle = projStyle)
        # 第一个list是静态拓扑，有误差;第二个是位移产生的拓扑变化,rg的问题,确实要报错
        errorList = [[],[]]
        for ns in nsList:
            print('\n' + '[%s:Start]'%ns + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
            abcKey = 'alembic'
            if checkType in ['trans']:
                abcKey = 'trans'
            if checkType in ['curve']:
                abcKey = 'abc_curve'
            if checkType in ['extra']:
                abcKey = 'extra'
            abcNode = '%s_%s_%s_AlembicNode'%(shotName,ns,abcKey)
            if projStyle in [2]:
                abcNode = '%s_%s_AlembicNode'%(ns,abcKey)
            if abcBy_ns in [1]:
                tempInfosList = self.replaceRebuildPerform(checkAbcNode=abcNode,checkType=checkType,checkNs=ns,
                                                clean=clean,printMode=printMode,projStyle = projStyle)
                errorList[0] += tempInfosList[0]
                errorList[1] += tempInfosList[1]
            if abcBy_ns in [2]:
                tempInfosList =  self.replaceRebuildPerformV2(checkAbcNode=abcNode,checkType=checkType,checkNs=ns,
                                                    shapeMode=shapeMode,projStyle = projStyle)
                errorList[0] += tempInfosList[0]
                errorList[1] += tempInfosList[1]
            print('\n' + '[%s:End]'%ns + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if errorList[1]:
            print('---------------BlendErrorList')
            for num in range(len(errorList[1])/2):
                print('---------------BlendError')
                print(errorList[1][num*2])
                print(errorList[1][num*2+1])
            print(u'-----------请检查以上物体,anim和render不匹配-----------')
            mc.error()

        # 记录
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        self.checkAbcConnectInfoExport(server,projStyle = projStyle)
        print('\n' + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')

        if abcBy_ns in [1]:
            # 修正deformer shape renderState的问题
            self.sk_fixShapeRenderStateAttrs()

    #---------------------------------------------------------#
    # 渲染文件更新cache
    def sk_shotCacheUpdate(self,server = 1, abcBy_ns = 2,projStyle = 0):
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 清理
        self.checkCacheCleanBlendShapes()
        # 导入
        # trans
        if abcBy_ns in [2]:
            self.GDC_alembicImp('fs',server,shotType = shotType,abcBy_ns = abcBy_ns,replaceMode = 1,checkType = 'trans')
            self.assetAbcRebuild(checkType = 'trans',shotName = shotID ,server = server,abcBy_ns = abcBy_ns,projStyle = projStyle)
        # mesh
        cacheObjs = self.GDC_alembicInfo(3)
        if cacheObjs:
            self.GDC_alembicImp('fs',server,shotType = shotType,abcBy_ns = abcBy_ns,replaceMode = 1,checkType = 'mesh')
            self.assetAbcRebuild(checkType = 'mesh',shotName = shotID ,server = server,abcBy_ns = abcBy_ns,projStyle = projStyle)
        # curve
        curveObjs = self.GDC_shaveInfo(3,'curve')
        if curveObjs:
            self.GDC_curvealembicImp(server,abcBy_ns = abcBy_ns)
            self.assetAbcRebuild(checkType = 'curve',shotName = shotID,server = server,abcBy_ns = abcBy_ns,projStyle = projStyle)
        # V属性
        self.checkCacheVStateImport(shotType)

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
            sourceAttr = '%s.%s'%(source,checkAttr)
            targetAttr = '%s.%s'%(target,checkAttr)
            if mc.ls(targetAttr) and mc.ls(sourceAttr):
                mc.setAttr(targetAttr,mc.getAttr(sourceAttr))

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
    # 重连模式
    def replaceRebuildPerform(self,checkAbcNode = '',checkType= 'mesh',checkNs = '',clean = 1,printMode = 0,projStyle = 0):
        #if checkType not in ['mesh'] and not mc.ls(checkAbcNode):
        #    print(mc.ls(checkAbcNode)
        #    return []
        blendErrorList = []
        print('---------abcRebuild')
        print(checkAbcNode)
        print(checkNs)
        testMode = 1
        abcNS = checkNs + self.tempNs
        # replace模式下没有连接状态的物体
        nsStaticAbcObjs  = self.getNoConsAbcObj(checkType,abcNS)
        if printMode:print('----------nsStaticAbcObjs')
        if printMode:print(nsStaticAbcObjs)
        # 参考状态的asset物体列表
        sourceObjsInfo = self.getShotAssetAbcObj(checkType,checkNs)
        sourceObjs = sourceObjsInfo[0]
        sourceObjsDict = sourceObjsInfo[1]
        if printMode:print('----------sourceObjsDict')
        if printMode:print(sourceObjsDict)
        errorObjs = []
        if printMode:print('\n' + '[%s:001]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # replace模式下的非参考物体列表
        abcObjsInfo  = self.getReplaceAbcObj(checkType,abcNS,checkAbcNode)
        abcObjs = abcObjsInfo[0]
        abcObjsDict = abcObjsInfo[1]
        if printMode:print('----------abcObjsDict')
        if printMode:print(abcObjsDict)
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
        if printMode:print('\n' + '[%s:002]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
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
                self.singleFrameCacheBlendConfig(abcGrp,fileGrp,abcByNs= 1,projStyle = projStyle)
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

        if printMode:print('\n' + '[%s:003]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        if checkType in ['mesh','curve']:
            print('-------objList')
            print(checkNs)
            print('[%s]   [%s]'%(str(len(sourceObjs)),'sourceObjs'))
            print('[%s]   [%s]'%(str(len(sourceObjsDict.keys())),'sourceObjsKeyList'))
            #print(sourceObjs)
            print('[%s]   [%s]'%(str(len(abcObjs)),'abcObjs'))
            print('[%s]   [%s]'%(str(len(abcObjsDict.keys())),'abcObjsKeyList'))
            #print(abcObjs)
            print('[%s]   [%s]'%(str(len(abcConsObjs)),'abcConsObjs'))
            #print(abcConsObjs)
            print('[%s]   [%s]'%(str(len(abcConsObjsAttrList)),'abcConsObjsAttrList'))
            print('[%s]   [%s]'%(str(len(abcConsObjsAttrDict.keys())),'abcConsObjsAttrKeyList'))
            #print(abcConsObjsAttrList)
            print('[%s]   [%s]'%(str(len(nsStaticAbcObjs)),'nsStaticAbcObjs'))
            #print(nsStaticAbcObjs)
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
                    if printMode:print('----------showKey\n%s'%abcConsObjsAttrDict.keys())
                    errorObjs.append(checkObjS)

        if errorObjs:
            print('---------------------uTestGrpsCheck')
            print(len(errorObjs))
            #for errorObj in errorObjs:
            #    print(errorObj)
            if not testMode:
                mc.error()

        if printMode:print('\n' + '[%s:005]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
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
                    targetInfo = '%s.inMesh'%targetShape
                if '.create' in abcObjAttr:
                    targetInfo = '%s.create'%targetShape
                deformInfos.append([abcSAttr,abcObjAttr,targetInfo])
            else:
                if nodeType in usedNodes:
                    nextNodeAttr = mc.listConnections(abcObjAttr.split('.')[0],s=0,d=1,plugs=1)
                    if not nextNodeAttr:
                        print('-----------abcAttrError')
                        print(abcObjAttr)
                        continue
                    nextNodeAttr = nextNodeAttr[0]
                    targetInfo = '%s.%s'%(needCheckObj,nextNodeAttr.split('.')[-1])
                    unitInfos.append(([abcSAttr,abcObjAttr]))
                else:
                    targetInfo = '%s.%s'%(needCheckObj,abcObjAttr.split('.')[-1])
                transInfos.append([abcSAttr,abcObjAttr,targetInfo])
            fixedObjs.append(abcObjAttr.split('.')[0])

        if printMode:print('\n' + '[%s:006]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
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

        if printMode:print('\n' + '[%s:007]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
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

        if printMode:print('\n' + '[%s:008]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        # 处理 unitInfos
        for infos in unitInfos:
            abcSAttr = infos[0]
            abcObjAttr = infos[1]
            mc.disconnectAttr(abcSAttr,abcObjAttr)
            #mc.connectAttr(abcSAttr,abcObjAttr,f=1)
            unitNode = abcObjAttr.split('.')[0]
            if mc.ls(unitNode):
                mc.delete(unitNode)

        if printMode:print('\n' + '[%s:009]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
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
                    print('*' * 50)
                    print(temp)
                    print('*' * 50)
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
                blendErrorList += self.singleFrameCacheBlendConfig(checkObj,targetObj,abcByNs = 1,projStyle = projStyle)
        # 处理显示隐藏
        self.blendSetVOff(sourceVDict)
        self.blendSetVOff(abcVDict)
        # 收尾
        if printMode:print('\n' + '[%s:010]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        if abcObjs and clean:
            mc.delete(abcObjs)
        if printMode:print('\n' + '[%s:011]'%checkNs + time.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        if nsStaticAbcObjs and clean:
            mc.delete(nsStaticAbcObjs)
        return [errorObjs,blendErrorList]

    #--------------------------------------#
    # 重连模式
    def replaceRebuildPerformV2(self,checkAbcNode = '',checkType= 'mesh',checkNs = '',shapeMode=0,projStyle = 0):
        #if checkType not in ['mesh'] and not mc.ls(checkAbcNode):
        #    print(mc.ls(checkAbcNode)
        #    return []
        print('---------abcRebuild')
        print(checkAbcNode)
        abcNS = checkNs+self.tempNs +'_%s'%checkType
        print(abcNS)
        # 获取abc物体
        nsAbcObjs = mc.ls('%s:*'%abcNS,l=1,type ='transform')
        errorObjs = []
        blendErrorList = []
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        for checkAbcObj in nsAbcObjs:
            sourceObj = checkAbcObj.split('|')[-1].replace((self.tempNs +'_%s'%checkType),'')
            if not mc.ls(sourceObj):
                continue
            '''
            # rotateP local
            localP = mc.xform(checkAbcObj,rotatePivot = 1, q = 1)
            mc.xform(sourceObj,rotatePivot = localP )
            # scaleP local
            localS = mc.xform(checkAbcObj,scalePivot = 1, q = 1)
            mc.xform(sourceObj,scalePivot = localS)
            '''
            # blend World 模式,不用在乎位移
            # blend
            if checkType not in ['trans']:
                # blend
                blendErrorList += self.singleFrameCacheBlendConfig(checkAbcObj,sourceObj,abcByNs = 2,shapeMode=shapeMode,projStyle = projStyle)
            # transform
            else:
                for checkAttr in attrList:
                    cons = mc.listConnections(sourceObj+checkAttr,s=1,d=0,plugs=1)
                    # 断开
                    if cons:
                        mc.disconnectAttr(cons[0],(sourceObj+checkAttr))
                    # 静帧
                    if not mc.getAttr(sourceObj+checkAttr,l=1):
                        mc.setAttr((sourceObj+checkAttr),mc.getAttr(checkAbcObj+checkAttr))
                    # 连接
                    cons = mc.listConnections(checkAbcObj+checkAttr,s=1,d=0,plugs=1)
                    if cons:
                        mc.connectAttr(cons[0],(sourceObj+checkAttr))
        return [errorObjs,blendErrorList]

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
        if checkType in ['extra']:
            from idmt.maya.commonPerform.projectTools import sk_projTools_mi
            reload(sk_projTools_mi)
            checkObjs = sk_projTools_mi.sk_projTools_mi().miAssetGetExtraObjs(checkNs)
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
        abcKey = checkType
        if checkType in ['mesh']:
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
            
            try: 
                mc.parentConstraint(sourceObj ,targetObj, maintainOffset = 0)
                noList.append(targetObj)
            except:
                print('*' * 50)
                print('source object: %s,  target Object: %s' % (sourceObj, targetObj))
                print('*' * 50)

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
    # 单帧形变处理,避免某些物体有毛发关闭清理历史,source 和 target 都是transform
    def singleFrameCacheBlendConfig(self,source,target,delHistory = 0,abcByNs = 1,shapeMode=0,projStyle = 0):
        errorInfos = []
        blendOK = 0
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        mc.select(cl=1)
        mc.select(source)
        mc.select(target,add= 1)
        meshOld = mc.listRelatives(target,s=1,type = 'mesh',ni=1,f=1)
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
        if nodeType in ['nurbsCurve']:
            self.checkRebuildCurves(source,target)
        if nodeType in ['mesh'] or abcByNs in [2]:
            originMode = 'local'
            if projStyle in [2]:
                originMode = 'world'
            try:
                self.blendPerform(shapeMode)
                if shapeMode in [0]:
                    blendNode = mc.blendShape(envelope=1,origin = originMode,weight = [0,1])
                if shapeMode in [1]:
                    blendNode = mc.blendShape(frontOfChain = 1,envelope=1,origin = originMode,weight = [0,1])
                blendOK = 1
            except:
                errorInfos.append(source)
                errorInfos.append(target)
            #if ':' in source:
            #    attr = source.split(':')[-1]
            #else:
            #    attr = source.split('|')[-1]
            #mc.setAttr((blendNode[0] + '.' + attr),1)
            #if blendPre:
            #    mc.rename(blendNode[0],blendPre+blendNode[0])
        if blendOK:
            meshNow = mc.listRelatives(target,s=1,type = 'mesh',ni=1,f=1)
            # default模式会创建deformer节点，需要进行属性连接
            if shapeMode in [0] and (meshOld and meshNow):
                sk_backCmd.sk_backCmd().transAttrUpdate(target)
            if delHistory:
                mc.select(target)
                mel.eval('DeleteHistory')
                mc.select(cl=1)
        return errorInfos

    #-----------------------#
    # blendPerform
    def blendPerform(self,shapeMode=0):
        mc.optionVar(stringValue = ['blendShapeNode',''])
        mc.optionVar(floatValue = ['blendShapeEnv',1.0])
        mc.optionVar(intValue = ['blendShapeOrigin',1])
        mc.optionVar(intValue = ['blendShapeBetween',0])
        mc.optionVar(intValue = ['blendShapeTop',1])
        mc.optionVar(intValue = ['blendShapeDelTgt',0])
        if shapeMode in [0]:
            mc.optionVar(stringValue = ['blendShapePositioning','default'])
        if shapeMode in [1]:
            mc.optionVar(stringValue = ['blendShapePositioning','frontOfChain'])
        mc.optionVar(intValue = ['blendShapeExclusive',0])
        mc.optionVar(stringValue = ['blendShapePositioning','deformPartition'])

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
        renderStatesList +=['.aiSubdivType','.aiSubdivIterations','.aiDispHeight']
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
    def checkAbcConnectInfoExport(self,server = 1,projStyle = 0):
        # 记录
        abcNodes = mc.ls(type = 'AlembicNode')
        if not abcNodes:
            return
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
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
        localSetAnimPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,projStyle = projStyle)

        sk_infoConfig.sk_infoConfig().checkFileWrite((localSetAnimPath + infoKey + '_Cons.txt'),abcConsInfos)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localSetAnimPath + infoKey + '_Path.txt'),abcPaths)

        # 更新
        if server:
            serverSetAnimPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,projStyle = projStyle)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localSetAnimPath + infoKey + '_Cons.txt') + '"' + ' ' + '"' + (serverSetAnimPath + infoKey +  '_Cons.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localSetAnimPath + infoKey + '_Path.txt') + '"' + ' ' + '"' + (serverSetAnimPath + infoKey +  '_Path.txt') + '"' + ' true'
            mel.eval(updateAnimCMD)
            print(serverSetAnimPath)

    #--------------------------------------#
    # 导入连接
    def checkAbcConnectInfoImport(self,server = 1,projStyle = 0):
        # 检测
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        infoKey = 'abcInfos'
        needPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15,projStyle = projStyle)
        if not os.path.exists(needPath + infoKey + '_Cons.txt') or not os.path.exists(needPath + infoKey + '_Path.txt'):
            return
        # 分析
        abcConsInfos = sk_infoConfig.sk_infoConfig().checkFileRead(needPath + infoKey + '_Cons.txt')
        abcPathInfos = sk_infoConfig.sk_infoConfig().checkFileRead(needPath + infoKey + '_Path.txt')
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
                       #else: print(u'OBJS: %s has no match cache object ' %(obj) #=====add by zhangben)

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

    #删除非参考的abc cache
    def LY_deleteABCImp(self):
        needNodes=[]
        nodes = mc.ls(type='transform',l=1)
        sourceGrps=[]
        for grp in nodes:
            if mc.referenceQuery(grp,isNodeReferenced = 1) or grp in ['|CAM_GRP', '|CHR_GRP', '|PRP_GRP','|SET_GRP']:
                continue
            sourceGrps.append(grp)
        sourceGrps.remove('|persp')
        sourceGrps.remove('|front')
        sourceGrps.remove('|side')
        sourceGrps.remove('|top')
        if sourceGrps:
            mc.delete(sourceGrps)

    #开启Stretch_Mesh属性
    def stretch_attr(self):
        if not mc.pluginInfo('stretchMesh_2014_x64',loaded = 1,q = 1):
            mc.loadPlugin('stretchMesh_2014_x64')

        curves=mc.ls(type='transform',l=1)
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
                if mc.objExists(node+'.Stretch_Mesh'):
                    CurNeeds.append(node)

        if CurNeeds:
            for node in CurNeeds:
                if mc.getAttr(node+'.Stretch_Mesh')==0:
                    mc.setAttr(node+'.Stretch_Mesh',1)
                else:
                    pass


    ############################################################################################################################
    #ABC 导出【通用】【适用于前期群组，渲染FS，场景ABC导出】
    #@author 韩虹
    #2015/03/24
    ###########################################################################################################################
    def GDC_alembicExr(self,server = 1,cachePre = 0,shotType = 1,ap=1,UI=0):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport')

        framemin  =   mc.playbackOptions(min=1,q = 1)-50
        framemax  =   mc.playbackOptions(max=1,q = 1)+10
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(2)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        shotName=sk_infoConfig.sk_infoConfig().checkShotInfo()
        alembicName=''
        if shotType==1 or shotType==2:
            if UI==1:
                result = mc.promptDialog(title='north_abcExprotTools',message=u'请选择CACHE_OBJS SET组内物体\Enter Name:\n例如：ice_999_008_mrGreene.abc',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                if result == 'OK':
                        text = mc.promptDialog(query=True, text=True)
                        if text:
                            if text.split('.')[-1]=='abc':
                                alembicName=text
                            else:
                                mc.error(u'请输入正确文件名注意扩展名:".abc"')
                        else:
                            mc.error(u'请输入正确文件名,并按“OK”键')
            else:
                alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'.abc'
        if shotType==3:
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'_'+shotName[3]+'.abc'
        if ap==1:
            self.GDC_alembicApply()
        abccommon = "-frameRange"+' '+ str(framemin)+' '+str(framemax)+' -uvWrite -worldSpace -writeVisibility '+self.GDC_alembicInfo(infotype=1)[0]+' -file'+' '+str(localPath+alembicName)
        mc.select(cl=1)
        self.csl_AttrAction(line='select',attrtype='alembic')
        print(u' now pinrt lineNum: 110')#===add by zhangben ,label line number)
        mc.AbcExport(j=abccommon)
        print(u'ABC Export Succeed!!!!!!!!======================================')
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath+alembicName) + '"' + ' ' + '"' + (serverPath+alembicName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print(u'===[Updating alembic To Server]===传输[%s]完毕==='%alembicName)

        return [(localPath+alembicName),(serverPath+alembicName),framemin,framemax]


    ###########################################################################################################################
    def GDC_shavealembicExr(self,server = 1,shotType = 1,ap=1,UI=0):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport')
        framemin  =   mc.playbackOptions(min=1,q = 1)
        framemax  =   mc.playbackOptions(max=1,q = 1)+1
        # 获取alembic临时路径
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(2)
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        shotName=sk_infoConfig.sk_infoConfig().checkShotInfo()
        alembicName=''
        if shotName[0] == u'mi': #============add by zhangben  for  mi  shave curve===================
            framemin = mc.playbackOptions(min=1,q = 1) - 50
            framemax = mc.playbackOptions(max=1,q = 1) + 50
        if shotType==1 or shotType==2:
            if UI==1:
                result = mc.promptDialog(title='north_abcExprotTools',message=u'请选择CACHE_CURVES SET组内物体\nEnter Name:\n例如：ice_999_008curve_mrGreene.abc',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                if result == 'OK':
                        text = mc.promptDialog(query=True, text=True)
                        if text:
                            if text.split('.')[-1]=='abc':
                                alembicName=text
                            else:
                                mc.error(u'请输入正确文件名注意扩展名:".abc"')
                        else:
                            mc.error(u'请输入正确文件名,并按“OK”键')
            else:
                alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'curve.abc'
        if shotType==3:
            alembicName=shotName[0]+'_'+shotName[1]+'_'+shotName[2]+'_'+shotName[3]+'curve.abc'
        if ap==1:
            self.LY_abcCurApply()
        abccommon="-frameRange"+' '+ str(framemin)+' '+str(framemax)+' -uvWrite -worldSpace -writeVisibility '+self.GDC_shaveInfo(infotype=1)[0]+' -file'+' '+str(localPath+alembicName)
        mc.select(cl=1)
        mc.AbcExport(j=abccommon)
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath+alembicName) + '"' + ' ' + '"' + (serverPath+alembicName) + '"' + ' true'
            mel.eval(updateAnimCMD)
            print(u'===[Updating alembic To Server]===传输[%s]完毕==='%alembicName)

        return [(localPath+alembicName),(serverPath+alembicName),framemin,framemax]
################################################################
    #ABC属性添加【通用】【输助】【将cacheSet物体添加abc属性】
    #@author 韩虹
    #2015/03/24
    ###########################################################################################################################
    def GDC_alembicApply(self):
        cacheObjs=self.checkCacheSetObjects(otcGrp = 1)
        mc.select(cacheObjs)
        self.csl_AttrAction(line="add",attrtype="alembic")
        print(u' now pinrt lineNum: 170')#===add by zhangben ,label line number
        return cacheObjs

    ################################################################
    #@author 梁宇
    ###########################################################################################################################
    def LY_abcCurApply(self):
        cacheObjs=self.checkCurveSetObjects(otcGrp = 1)
        mc.select(cacheObjs)
        return cacheObjs

    #---------------------------------#
    # abc属性添加
    #---------------------------------#
    def abc_AttrAdd(self,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        needGrps = []
        tempGrps = mc.ls('*:MODEL',l=1)
        if projStyle in [2]:
            tempGrps = mc.ls('CH_*:Model_Hight',l=1) + \
                       mc.ls('PRO_*:MODEL',l=1) +\
                       mc.ls('BG_*:SCENES',l=1)
        for tempgrp in tempGrps:
            state = 0
            if '|CHR_GRP|' in tempgrp:
                state = 1
            if '|PRP_GRP|' in tempgrp:
                state = 1
            if state:
                needGrps.append(tempgrp)
        from idmt.maya.ShunLiu_common import csl_toolCommons
        reload(csl_toolCommons)
        for needgrp in needGrps:
            if mc.ls(needgrp+'.alembic'):
                continue
            mc.select(needgrp)
            csl_toolCommons.csl_toolComnnons().csl_AttrAction(line="add",attrtype="alembic")
        mc.select(cl =1)

    #------------------------------#
    # 收集MODEL组下的组
    def getGrpsOfModel(self):
        needGrps = []
        modelGrps = mc.ls('*:MODEL')
        if not modelGrps:
            return needGrps
        allGrps = mc.listRelatives(modelGrps,ad=1,type= 'transform',f=1)
        for checkGrp in allGrps:
            if 'Constraint' in checkGrp:
                continue
            #shape = mc.listRelatives(checkGrp,s=1)
            #if shape:
            #    continue
            needGrps.append(checkGrp)
        return needGrps

    ############################################################################################################################
    #ABC属性添加【通用】【输助】【返回添加ABC属性的物体】
    #@author 韩虹
    #2015/03/24
    #infotype 为1 导出信息，为0 导出信息，为3则为ABC物体信息
    ###########################################################################################################################
    def GDC_alembicInfo(self,infotype=1):
        self.csl_AttrAction(line='select',attrtype='alembic')
        print(u' now pinrt lineNum: 188') #===add by zhangben ,label line number
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
            print(u'缺少ABC属性物体')
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos

        return abcInfos

    ############################################################################################################################
    #abc_curve属性物体【通用】【输助】【用在shave curve】
    #@author 韩虹    修改：梁宇
    ###########################################################################################################################
    def GDC_shaveInfo(self,infotype=0,type='curve'):
        if type in ['mesh']:
            type = 'alembic'
        if type in ['curve']:
            type = 'abc_curve'
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
            print(u'缺少abc_curve属性')
        if infotype==0 or infotype==1:
            abcInfos=[abcInfo]
        else:
            abcInfos=abcInfos

        return abcInfos

   ############################################################################################################################
    #ABC属性添加【通用】【核心】【创建并导入abc（前期）】
    #@author 韩虹
    #2015/03/24
    ###########################################################################################################################
    def GDC_alembicImp(self,line='pre',server = 1,shotType = 1,UI=0,replaceMode = 0,abcBy_ns = 0,checkType = 'mesh',projStyle = 0):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfos=sk_infoConfig.sk_infoConfig().checkShotInfo()
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        #本机
        FlocalPath=sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        #服务器路径
        FserverPath=sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        if line=='fs':
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 获取alembic服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(shotType )
        if line in ['pre']:
            alebicName=shotInfos[0]+'_'+shotInfos[1]+'_'+shotInfos[2]+'.abc'
            filename=shotInfos[0]+'_'+shotInfos[1]+'_'+shotInfos[2]+'ABC_h_ms_render.mb'
            rendername=shotInfos[0]+'_'+shotInfos[1]+'_h_ms_render.mb'
            lineName=''
            if shotInfos[1][0] in ['c']:
                lineName='characters'
            if shotInfos[1][0] in ['p']:
                lineName='props'
            if shotInfos[1][0] in ['s', 'S']:
                lineName='sets'
            mslocalPath=FlocalPath+'ms_render/'
            mc.sysFile(mslocalPath, makeDir=True)
            msserverPath= FserverPath+'scenes/'+ lineName+'/'+ shotInfos[1]+'/master/'

            #创建abc
            self.GDC_alembicApply()
            abcfile=self.GDC_alembicExr(server = server,cachePre = 0,shotType = 1,ap=1,UI=1)
            mc.file(rename=(mslocalPath+rendername))
            mc.file(save=1,type = 'mayaBinary',f = 1)
            mc.file( force=True, new=True )
            #打开ms_render文件并导入abc
            mc.file((msserverPath+rendername),options='v=0',type='mayaBinary',f=1,o=1)
            mc.file(rename=(mslocalPath+rendername))
            mc.file(save=1,type = 'mayaBinary',f = 1)
            #设置帧数
            #开始帧
            mc.playbackOptions(min=int(abcfile[2]))
            preStartFrame = int(abcfile[2]) - 12
            mc.playbackOptions(animationStartTime=preStartFrame)
            # 结束帧
            mc.playbackOptions(max=int(abcfile[3]))
            # 结束预留
            posEndFrame = int(abcfile[3]) + 12
            mc.playbackOptions(animationEndTime=posEndFrame)
            mc.currentTime(int(abcfile[2]))
            self.GDC_alembicApply()
            mc.select(cl=1)

            self.csl_AttrAction(line='select',attrtype='alembic')
            print(u' now pinrt lineNum: 322') #===add by zhangben ,label line number
            abcinfo=self.GDC_alembicInfo(0)[0]
            if server ==1:
                mc.AbcImport(abcfile[1],mode='import',connect=abcinfo)
            else:
                mc.AbcImport(abcfile[0],mode='import',connect=abcinfo)
            try:
                mc.sysFile((mslocalPath+rendername),delete=True)
            except:
                pass
            mc.file(rename=(mslocalPath+filename))
            mc.file(save=1,type = 'mayaBinary',f = 1)
        if line in ['fs']:
            frameStart = mc.playbackOptions(q=1, min=1)
            frameEnd = mc.playbackOptions(q=1, max=1)
            mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
            shotName = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
            if shotType in [3]:
                shotName = '%s_%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
            if projStyle not in [1]:
                fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfos,projStyle = projStyle)
                shotName = fileDict['shotID']
            if UI==1 and shotType in [2]:
                result = mc.promptDialog(title='north_abcImportTools',message=u'请键入需要cache名称\nEnter Name:\n例如：ice_999_008curve_mrGreene.abc',button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
                if result == 'OK':
                    text = mc.promptDialog(query=True, text=True)
                    if text:
                        if text.split('.')[-1]=='abc':
                            alebicName = text
                        else:
                            mc.error(u'请输入正确文件名注意扩展名:".abc"')
                    else:
                        mc.error(u'请输入正确文件名,并按“OK”键')
            alebicName=shotName+'.abc'
            # path
            basePath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 2.5,projStyle = projStyle)
            print('----------abcPath')
            print(basePath)
            if replaceMode:
                # asset单位模式
                if abcBy_ns:
                    nsList = self.getNsListOfFile(projStyle = projStyle)
                    print(nsList)
                    abcKey = 'alembic'
                    if checkType in ['trans']:
                        abcKey = 'trans'
                    for checkNs in nsList:
                        # 清理
                        if abcBy_ns in [2]:
                            abcNode = '%s_%s_%s_AlembicNode'%(shotName,checkNs,abcKey)
                            abcGrp = '%s_%s_%s_Grp'%(checkNs,self.tempNs,abcKey)
                            if projStyle in [2]:
                                abcNode = '%s_%s_AlembicNode'%(checkNs,abcKey)
                                abcGrp = '%s_%s_Grp'%(self.tempNs,abcKey)
                            if mc.ls(abcNode):
                                mc.delete(abcNode)
                            if mc.ls(abcGrp):
                                mc.delete(abcGrp)
                        # 导入
                        alebicName = '%s_%s_%s.abc'%(shotName,checkNs,abcKey)
                        if projStyle in [2]:
                            alebicName = '%s_%s.abc'%(checkNs,abcKey)
                        abcFile = basePath+alebicName
                        if abcBy_ns in [1]:
                            mc.AbcImport(abcFile,mode='replace')
                        if abcBy_ns in [2]:
                            #mc.AbcImport(abcFile,mode='import')
                            abcNs = '%s%s_%s'%(checkNs,self.tempNs,checkType)
                            print('*' * 50)
                            print('file name: ' + abcFile)
                            print('ns: ' + abcNs)
                            print('*' * 50)
                            mc.file(abcFile,namespace = abcNs,type = 'Alembic',i=1)
                        # 赋予namespace
                        self.abcMeshAddNs(checkNs,abcBy_ns,checkType)
                # 整体模式
                else:
                    mc.AbcImport((basePath+alebicName),mode='replace')
            else:
                abcinfo=self.GDC_alembicInfo(0)[0]
                mc.AbcImport((basePath+alebicName),mode='import',connect=abcinfo)
            mc.playbackOptions(min=frameStart, max=frameEnd)
            mc.currentTime(int(frameStart))
        return 0

    # 获取当前文件的nslist
    def getNsListOfFile(self,noSet = 1,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
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
            if noSet:
                if projStyle in [1]:
                    if checkNs.split('_')[1][0].lower() not in ['c','p']:
                        continue
                if projStyle in [2]:
                    if checkNs.split('_')[0] not in ['CH','PRO']:
                        continue
            needNsList.append(checkNs)
        return needNsList

    # 非参考replace物体赋予namespace
    def abcMeshAddNs(self,ns,abcBy_ns,addType):
        if addType in ['trans']:
            self.abcGrpReGroup()
        checkObjs = mc.ls(type = 'transform',l=1)
        if abcBy_ns == 1:
            tempNs = ns + self.tempNs
        if abcBy_ns == 2:
            tempNs = ns + self.tempNs + '_%s'%addType
        if not mc.namespace(exists = tempNs):
            mc.namespace(set = ':')
            mc.namespace(add = tempNs)
            mc.namespace(set = ':')
        if abcBy_ns == 2:
            abcGrp = self.abcGrp
            if not mc.ls(abcGrp):
                mc.group(n=abcGrp,em=1)
            tempName = mc.ls(abcGrp,l=1)[0]
            otcGrp = 'OTC_GRP'
            if '|%s|'%otcGrp not in tempName:
                mc.parent(abcGrp,otcGrp)
            nsGrp = '%s_GRP'%tempNs
            if mc.ls(nsGrp):
                mc.delete(nsGrp)
            nsGrp = mc.group(name = nsGrp,em = 1)
            mc.parent(nsGrp,abcGrp)
            mc.setAttr('%s.v'%abcGrp,0)
        for checkObj in checkObjs:
            if not mc.ls(checkObj):
                continue
            inr = mc.referenceQuery(checkObj,inr=1)
            if inr:
                continue
            splitNum = len(checkObj.split('|'))
            if splitNum != 2:
                continue
            if abcBy_ns in [1]:
                if '%s:'%ns not in checkObj:
                    continue
                if tempNs in checkObj:
                    continue
                result = mc.rename(checkObj,'%s:%s'%(tempNs,checkObj.split('|')[-1]))
                result = mc.rename(result,'%s:%s'%(tempNs,result.split('|')[-1]))
            if abcBy_ns == 2:
                if tempNs not in checkObj:
                    continue
                mc.parent(checkObj,nsGrp)

    #---------------------------------------------------------#
    # Grp解组
    def abcGrpReGroup(self):
        rootGrps = mc.ls('CHR_GRP*',type = 'transform') + mc.ls('PRP_GRP*',type = 'transform')
        delGrps = []
        for rootGrp in rootGrps:
            if rootGrp in ['CHR_GRP','PRP_GRP']:
                continue
            delGrps.append(rootGrp)
            grps = mc.listRelatives(rootGrp,ad = 1,type = 'transform',f=1)
            if grps:
                for checkGrp in grps:
                    mc.parent(checkGrp,world = 1)
        mc.delete(delGrps)

    #---------------------------------------------------------#
    #ABC属性【通用】【核心】【创建并导入毛发曲线abc（前期）】
    #@author 韩虹
    #2015/03/24
    #---------------------------------------------------------#
    def GDC_curvealembicImp(self,server = 1,UI = 0,abcBy_ns=0,projStyle = 0):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        shotInfo =sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])

        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        mc.playbackOptions(min=frameStart - 12, max=frameEnd + 12)
        alebicName=''
        shotName = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType in [3]:
            shotName = '%s_%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2],shotInfo[3])
        if projStyle not in [1]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfo,projStyle = projStyle)
            shotName = fileDict['shotID']
        if UI==1:
            if shotType in [2]:
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
        abcinfo=self.GDC_shaveInfo(0,'curve')[0]
        basePath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 2.5,projStyle = projStyle)
        # curve使用导入模式?
        if projectInfo in ['ShunLiu']:
            mc.AbcImport((basePath+alebicName),mode='import',connect=abcinfo)
        else:
            # asset单位模式
            if abcBy_ns:
                nsList = self.getNsListOfFile(projStyle = projStyle)
                for checkNs in nsList:
                    # 清理
                    if abcBy_ns == 2:
                        abcNode = '%s_%s_abc_curve_AlembicNode'%(shotName,checkNs)
                        abcGrp = '%s_%s_curve_Grp'%(checkNs,self.tempNs)
                        if projStyle in [2]:
                            abcNode = '%s_abcCurve_AlembicNode'%checkNs
                            abcGrp = '%s_abcCurve_Grp'%self.tempNs
                        if mc.ls(abcNode):
                            mc.delete(abcNode)

                        if mc.ls(abcGrp):
                            mc.delete(abcGrp)
                    alebicName = '%s_%s_abc_curve.abc'%(shotName,checkNs)
                    if projStyle in [2]:
                        alebicName = '%s_abc_curve.abc'%checkNs
                    curveCache = basePath+alebicName
                    if not os.path.exists(curveCache):
                        continue
                    mc.AbcImport(curveCache,mode='replace')
                    # 赋予namespace
                    self.abcMeshAddNs(checkNs,abcBy_ns,'curve')
            # 整体模式
            else:
                mc.AbcImport((basePath+alebicName),mode='replace')
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
                    print(u'\n')
                    print(u'==========================已选择有【%s】属性的物体==========================line:448' % attrtype)
                    print(u'\n')
                except:
                    print(u'\n')
                    print(u'==========================文件中没有【%s】属性的物体==========================line:452' % attrtype)
                    print(u'\n')
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


    #------------------------------#

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
                                objsCache.append(mc.ls(mesh, l=0)[0])
                        else:
                            objsCache.append(mc.ls(mesh, l=0)[0])
        if objsCache:
            print(u'[Cache Object]    ' + str(len(objsCache)))
        else:
            print(u'[Cache Object]    0')
        return objsCache

   #----------------------------------------------------------------------------------------------#
#######Cache物体（from）
    def checkCurveSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        for temp in tempSet:
            if 'CURVES' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                cache_curs = mc.sets(objSet, q=1)
        if cache_curs:
            print(u'[Cache curve]    ' + str(len(cache_curs)))
        else:
            print(u'[Cache curve]    0')
        return cache_curs
    #------------------------------#
    # 【通用】【群组打组整理】
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#
    def gdc_clusterGroupR(self):
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
        # 群组
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
        print(refRoot)
        # 1为参考方式处理
        # 这个方式对VFX会有影响,所以要修正
        for root in refRoot:
            if '_' in root and ':' in root:
                shortName=root.split('_')[1].split(':')[0]
                clusteGrp=shortName+'_cluster'
                if mc.ls(clusteGrp):
                    try:
                        mc.parent(clusteGrp, clusterFlowGrp)
                    except:
                        pass
                else:
                    clusterG  = mc.group(em=1, name=clusteGrp)
                    mc.parent(clusterG, clusterFlowGrp)
                # 首先判断是否在VFX_GRP和Cluster_GRP
                if '_cluster' not in mc.ls(root,l=1)[0]:
                    mc.parent(root, clusterG)
        return 0

   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【选择的物体abc移帧及改变速度】
    #  Author  : 韩虹
    #  Data    : 2015_03
    #------------------------------#
    def gdc_clusteroffset(self,ot=1,sd=1):
        offset=int(mc.intSliderGrp('offset',q=1,v=1))
        speed=float(mc.floatSliderGrp('speed',q=1,v=1))
        objs=mc.ls(sl=1,type='transform',l=1)
        abcnodes=[]
        if objs:
            for obj in objs:
                shapes=mc.listRelatives(obj,s=1,type='mesh',f=1)
                if shapes:
                    abcnode=mc.listConnections((shapes[0]+'.inMesh'),s=1,p=0)
                    if mc.ls(abcnode) and abcnode[0] not in abcnodes:
                        abcnodes.append(abcnode[0])
        if abcnodes==[]:
            mc.error(u'no abc')
        if abcnodes and  ot==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.offset'),offset)
        if abcnodes and  sd==1:
            for abc in abcnodes:
                mc.setAttr((abc+'.speed'),speed)
        return 0

   #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【辅助】【FL文件 ReferenceEdit还原】
    #------------------------------#
    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info ):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath()
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat

        print(needFsFile)

        # 不加载参考导入
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # 处理好所有参考
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        mc.file(save = 1, force = 1)

    #-------------------------------------#
    # 检测是否存在render文件
    def sk_FLCheckRenderFile(self,refInfos):
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            errorAsset = []
            for i in range(len(refPaths)):
                refPath = refPaths[i]
                renderFilePath = refPath.replace('_anim.','_render.')
                checkKey = '_gpu_'
                if checkKey in renderFilePath:
                    renderFilePath = renderFilePath.replace(checkKey,'_')
                checkKey = '_GPU_'
                if checkKey in renderFilePath:
                    renderFilePath = renderFilePath.replace(checkKey,'_')
                if os.path.exists(renderFilePath):
                    pass
                else:
                    errorAsset.append(refNodes[i])
            if errorAsset:
                print(u'-------------------以下render文件不存在-------------------')
                for info in errorAsset:
                    print(info[:-2])
                print(u'-------------------以上render文件不存在-------------------')
                print(u'==================请先检查shot文件确定参考是否正确==================')
                print(u'==================正确后请再和前期协商更新asset文件==================')
                mc.error(u'==================请和前期协商更新asset文件==================')
        else:
            print(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')
            mc.error(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】【所有约束BK，确保动画及camera正确】
    #  Author  : 沈康
    #  Data    : 2013_06_03
    #------------------------------#
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self ,simulation = 1,step = 1,fixEuler = 0,preFrame = -50,printMode = 0):
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

        if printMode:
            print('--------bk001')
            self.testDef('--bk001')

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

        if printMode:
            print('--------bk002')
            print(tobake)
            self.testDef('--bk002')

        io = (mc.playbackOptions(q=1, minTime=1)+preFrame, mc.playbackOptions(q=1, maxTime=1)+10)

        if printMode:
            print('--------bk003')
            print(tobake)
            self.testDef('--bk003')

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
        print('---Step 01:')
        for i in range(len(tobake)):
            locTemp = mc.spaceLocator()
            locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
            cons = mc.parentConstraint(tobake[i] , locTemp)
            constraintTemp.append(cons[0])
            locators.append(locTemp)
            print('------')
            print(tobake[i])
            print(locTemp)

        if printMode:
            print('--------bk005')
            self.testDef('--bk005')

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

        if printMode:
            print('--------bk006')
            self.testDef('--bk006')

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
                print(u'----------------')
                print(locatorGrp)
                print(tobake[i].split('|')[-1])
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
                    print('------')
                    print(locatorGrp)
                    print(tobake[i])
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

        if printMode:
            print('--------bk007')
            self.testDef('--bk007')

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

        if printMode:
            print('--------bk008')
            self.testDef('--bk008')

        # 删除约束
        #add by zhangben ---  extract constraint type node to world
        constraintConfigs = [x for x in (constraints) if not mc.referenceQuery(x,inr=1)]
        for cons in constraintConfigs:
            ref = mc.referenceQuery(cons,isNodeReferenced = 1)
            if not ref:
                mc.delete(cons)

        if printMode:
            print('--------bk009')
            self.testDef('--bk009')

        # 删除locators
        mc.delete(locators)

        if printMode:
            print('--------bk010')
            self.testDef('--bk010')

        # 修正欧拉角
        if fixEuler:
            self.checkAnimCurvesFix()

        mc.playbackOptions(minTime=min)
        mc.playbackOptions(maxTime=max)
        print(u'\n========================【约束】【烘焙】【成功】========================')
        print(u'\n')

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


    #-------------------------------------#
    # 记录hide输出
    def sk_FL_RefHideObjsRecord(self,server,shotType,projStyle = 0):
        unDisplayLayerObjs = []
        # 记录：shot文件非参考的隐藏的显示层的物体
        displayLayers = mc.ls(type = 'displayLayer')
        for layer in displayLayers:
            isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
            if isRef == 0 and layer != 'defaultLayer':
                viewState  = mc.getAttr(layer + '.visibility')
                if not viewState:
                    objs = mc.editDisplayLayerMembers( layer, query=True,fullNames=1 )
                    if objs:
                        unDisplayLayerObjs += objs
        hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,projStyle = projStyle)
        hideObjsLocalPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,projStyle = projStyle)
        mc.sysFile(hideObjsLocalPath,makeDir = 1)
        fileName = 'shotHideObjs.txt'
        self.checkFileWrite((hideObjsLocalPath +  fileName), unDisplayLayerObjs)
        if server:
            runCmd = 'zwSysFile("copy","' + (hideObjsLocalPath + fileName) + '","' + (hideObjsServerPath + fileName) + '",1)'
            mel.eval(runCmd)
            print(u'\n')
            print(u'=====================[hideObjs][Server][Update] Done=====================')
            print(u'\n')
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
        hideObjsLocalPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 2)
        mc.sysFile(hideObjsLocalPath,makeDir = 1)
        fileName = 'assetReference.txt'
        self.checkFileWrite((hideObjsLocalPath +  fileName), assetNeedOutputInfo)
        if server:
            hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 2)
            runCmd = 'zwSysFile("copy","' + (hideObjsLocalPath + fileName) + '","' + (hideObjsServerPath + fileName) + '",1)'
            mel.eval(runCmd)
            print(u'\n')
            print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
            print(u'\n')
        return assetNeedOutputInfo

    #-------------------------------------#
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 OTC及SET结构处理
    #  Author  : 沈康
    #  Data    : 2013_07_28
    #------------------------------#
    # OTC结构处理：删除 [更改：otc由mb强制变更ma;删除先删除ma文件，后找mb，若有则删除]
    def sk_sceneGRPDelete(self, fileGRP='OTC' ,server = 1,projStyle = 0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        #fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileFomat = '.ma'
        # oldRule
        #if server:
        #    renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        #else:
        #    renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        # newRule
        renderFilePathServer = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15,
                                                    shotInfos = shotInfo,projStyle = projStyle)

        baseShotInfo = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType == 3:
            baseShotInfo = '%s_%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2],shotInfo[3])
        if projStyle not in [1]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfo,projStyle = projStyle)
            baseShotInfo = fileDict['shotID']
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
        import os
        if os.path.exists(otcFileServer):
            sk_infoConfig.sk_infoConfig().checkServerFileSystem('delete',otcFileServer)
        else:
            fileFomat = '.mb'
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            if os.path.exists(otcFileServer):
                sk_infoConfig.sk_infoConfig().checkServerFileSystem('delete',otcFileServer)
                print(otcFileServer)

    #------------------------------#

    #------------------------------#
    # OTC结构处理：导出
    def sk_sceneGRPExport(self, fileGRP='OTC',server = 1 , shotType = 2 ,needNsList = [] ,projStyle = 0 ):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        renderFilePath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,
                                                    shotInfos = shotInfos,projStyle = projStyle)
        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'

        baseShotInfo = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType == 3:
            baseShotInfo = '%s_%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
        if projStyle not in [1]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfos,projStyle = projStyle)
            baseShotInfo = fileDict['shotID']
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFile = renderFilePath + baseShotInfo + fileGrpType + fileFomat
        print('--------otc|set_Step001')
        print(otcFile)
        root = mc.ls(assemblies=True)
        if root and (fileGRP + '_GRP') in root:
            mc.select(fileGRP + '_GRP')
            #file -force -options "v=0;" -typ "mayaAscii" -pr -es "E:/testError.ma";
            #mc.file(otcFile, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
            mel.eval('file -force -options "v=0;" -typ "%s" -pr -es "%s"'%(fileTypeFull,otcFile))
        mc.select(cl=1)
        print('--------otc|set_Step002')
        # 对set进行参考处理
        if fileGRP == 'SET':
            # ma模式处理
            animRefInfos = sk_infoConfig.sk_infoConfig().checkFileRead(otcFile)
            renderRefInfos = []
            for num in range(len(animRefInfos)):
                lineInfo = animRefInfos[num]
                checkKey = '_l_ms_'
                if checkKey in lineInfo:
                    lineInfo = lineInfo.replace(checkKey,'_h_ms_')
                checkKey = '_ms_anim.m'
                if checkKey in lineInfo:
                    lineInfo = lineInfo.replace(checkKey,'_ms_render.m')
                checkKey = '_ms_gpu.m'
                if checkKey in lineInfo and shotInfos[0] == u'mi':#=========add by zhangben for minitiger  set gpu.mb file ==== 2016.3.8===========
                    lineInfo = lineInfo.replace(checkKey,u'_ms_render.m')
                checkKey = '_gpu_'
                if checkKey in lineInfo and shotInfos[0] == u'mi':#=========add by shenkang for mi set gpu 2017.2.27===========
                    lineInfo = lineInfo.replace(checkKey,'_')
                checkKey = '_GPU_'
                if checkKey in lineInfo:
                    lineInfo = lineInfo.replace(checkKey,'_')
                # 屏蔽源文件错误
                # 当前行
                if self.refEditCheck(lineInfo):
                    continue
                # 上一行没结束
                if num>0 and self.refEditCheck(animRefInfos[num-1]) and ';' not in animRefInfos[num-1]:
                    continue
                renderRefInfos.append(lineInfo)
            sk_infoConfig.sk_infoConfig().checkFileWrite(otcFile,renderRefInfos,lineKey = '')
        # 对otc进行转参考处理
        if fileGRP == 'OTC':
            # ma模式处理
            animRefInfos = sk_infoConfig.sk_infoConfig().checkFileRead(otcFile)
            renderRefInfos = []
            for num in range(len(animRefInfos)):
                lineInfo = animRefInfos[num]
                # 屏蔽源文件错误
                # 当前行
                if self.refEditCheck(lineInfo):
                    continue
                # 上一行没结束
                if num>0 and self.refEditCheck(animRefInfos[num-1]) and ';' not in animRefInfos[num-1]:
                    continue
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
            sk_infoConfig.sk_infoConfig().checkFileWrite(otcFile,renderRefInfos,lineKey = '')
        print('--------target')
        print( otcFile)
        # 传至服务器
        if server:
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15,
                                                    shotInfos = shotInfos,projStyle = projStyle)

            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            print('------------otcFile')
            print(otcFile)
            print(otcFileServer)
            cmd = 'zwSysFile("copy","' + otcFile + '","' + otcFileServer + '",1)'
            mel.eval(cmd)

    #------------------------------#
    # OTC结构处理：导入
    def sk_sceneGRPImport(self, fileGRP='OTC' ,server = 1, shotType = 2,projStyle = 0):
        # ma文件利于文本读取改参考
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        # oldRule
        #renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)
        #if server:
        #    renderFilePathServer = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)

        renderFilePath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15,
                                            shotInfos = shotInfo,projStyle = projStyle)

        fileFomat = '.ma'
        fileTypeFull = 'mayaAscii'
        baseShotInfo = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType == 3:
            baseShotInfo = '%s_%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2],shotInfo[3])
        if projStyle not in [1]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfo,projStyle = projStyle)
            baseShotInfo = fileDict['shotID']
        fileGrpType = '_' + fileGRP.lower() + '_render'
        otcFileServer = renderFilePath + baseShotInfo + fileGrpType + fileFomat
        print(otcFileServer)
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
            timeNow += str(msTime / 100000)
            #timeMsec = datetime.datetime.now().microsecond
            #timeNow = timeNow + '_' + str(timeMsec)
            ns = 'food' + timeNow
            if fileGRP == 'SET':
                # 导入,必须这里清理
                print('---')
                print(otcFileServer)
                mc.file(otcFileServer, i=1 , loadReferenceDepth="none", namespace = ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            if fileGRP == 'OTC':
                # VFX文件采用tx文件做参考，可以直接用于渲染，无需切换参考
                mc.file(otcFileServer, i=1 , namespace=ns , type=fileTypeFull , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))


    #------------------------------#
    #------------------------------#
    # 处理OTC的SET文件
    def sk_sceneSETRefShaderReset(self , shotInfo , serverModify = 1 , shotType = 2,projStyle = 0):

        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileGrpType = '_set_render'

        # oldRule
        #if serverModify:
        #    needFilePath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        #else:
        #    needFilePath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(shotType)

        needFilePath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = serverModify,infoMode = 15,
                                                    shotInfos = shotInfo,projStyle = projStyle)

        baseShotInfo = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType == 3:
            baseShotInfo = '%s_%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2],shotInfo[3])
        if projStyle not in [1]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos = shotInfo,projStyle = projStyle)
            baseShotInfo = fileDict['shotID']
        needSetFile = needFilePath + baseShotInfo + fileGrpType + fileFomat
        print(needSetFile)
        import os
        if os.path.exists(needSetFile):
            # 不加载参考导入
            mc.file(needSetFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            print(u'====================开始处理SET_GRP文件====================')
            # 处理好文件
            # 在importOTC之前处理好anim中材质更改的情况
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            mc.file(save = 1, force = 1)

        if serverModify == 1:
            # 传至服务器
            renderFilePathServer = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,
                                                    shotInfos = shotInfo,projStyle = projStyle)
            otcFileServer = renderFilePathServer + baseShotInfo + fileGrpType + fileFomat
            print(otcFileServer)
            sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',needSetFile,otcFileServer)
            #mc.sysFile(needSetFile,copy=otcFileServer)
#            cmd = 'zwSysFile(\"copy\",\"' + needSetFile + '\",\"' + otcFileServer + '\",1)'
#            mel.eval(cmd)
        print(u'====================SET_GRP更新完毕====================')

    #------------------------------#

    # 特殊错误排查
    def refEditCheck(self,checkInfo,mode = 1):
        errorState = 0
        if mode in [1]:
            if 'connectAttr' in checkInfo and ('"modelPanel' in checkInfo and 'ViewSelectedSet.d' in checkInfo):
                errorState = 1
        return errorState

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
        for objSet in objsSet:
            ctrls = mc.sets(objSet, q=1)
            if not ctrls:
                continue
            for ctrl in ctrls:
                # 排除otc组信息
                if otcGrp not in [1]:
                    continue
                if 'OTC_GRP' not in mc.ls(ctrl,l=1)[0] and 'SET_GRP' not in mc.ls(ctrl,l=1)[0]:
                    print(ctrl)
                    objsAnim.append(ctrl)
        if objsAnim:
            print(u'[Anim  Object]    ' + str(len(objsAnim)))
        else:
            print(u'[Anim  Object]    0')
        return objsAnim

   #------------------------------#
    # 【核心】【动画数据导入导出PYTHON版】
    # 0.动画
    # Author : 沈  康
    # 参考             : 万寿龙
    # Data   : 2013_05_24 - 2013_05_28
    #------------------------------#
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = '' , shotType = 2,projStyle = 0):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.5   (Author: shenkang)')
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
            for checkObj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(checkObj, k=1)
                if not keys:
                    continue
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(checkObj, cb=1)
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        objAttr = '%s.%s'%(checkObj,attr)
                        if mc.objExists(objAttr):
                            # 获取属性的动画曲线 添加character连接处理
                            #animCurve = mc.listConnections(objAttr, s=1, d=0)
                            animCurve = self.skGetAnimCurvs(objAttr)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' +objAttr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0])
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(objAttr):
                                if 'double3' not in mc.getAttr(objAttr, type=1) :
                                    value = mc.getAttr(objAttr)
                                    AnimsInfo.append('non-anim ' + objAttr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(checkObj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if allAttr:
                                for attr in allAttr:
                                    objAttr = '%s.%s'%(expShapes[0],attr)
                                    # 获取属性的动画曲线 添加character连接处理
                                    #animCurve = mc.listConnections(objAttr, type='animCurve', s=1, d=0)
                                    animCurve = self.skGetAnimCurvs(objAttr)
                                    if animCurve:
                                        if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                            AnimsInfo.append('anim ' + objAttr + '\n{')
                                            # 更新信息
                                            infoAll = (self.checkAnimCurveInfoGet(animCurve[0]))
                                            for info in infoAll:
                                                AnimsInfo.append(info)
                                            AnimsInfo.append('}')
                                    else:
                                        # 无动画的信息，不过对于点来说基本用不到
                                        if 'double3' not in mc.getAttr(objAttr, type=1) :
                                            value = mc.getAttr(objAttr)
                                            AnimsInfo.append('non-anim ' + objAttr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            #localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType)
            localPathAnim = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,shotInfos = [],projStyle = projStyle)
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
                self.checkAnimInfoUpdate(infoFile = infoFile,projStyle = projStyle)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)

    #------------------------------#
    # 导入信息
    # 加入从服务器端读取功能
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = '' , shotType = 2,projStyle = 0):
        # 考虑下清理动画
        # 错误信息
        errorInfo = []
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        # fsMode，指定路径读取
        if not targetPath:
            # 本地获取
            needPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = serverFile,infoMode = 15,shotInfos = [],projStyle = projStyle)
            personalAmimFile = needPath + infoFile + '.sla'
            personalObjFile = needPath + infoFile + '_objs.txt'
        else:
            # 自定义读取路径
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        # 动画信息
        AnimsInfo = self.checkFileRead(personalAmimFile)
        # 获取objct信息，检测obj
        nsObjs = self.checkFileRead(personalObjFile)
        print(nsObjs)
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

    #------------------------------#
    # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile , projStyle = 0):
        import os
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        # 本地路径转mel用
        #localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath(shotType).replace('\\', '/')
        localPathAnim = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,shotInfos = [],projStyle = projStyle)
        # 服务器端路径转mel用
        #serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath(shotType).replace('\\', '/')
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,shotInfos = [],projStyle = projStyle)
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
        #print('-----------------')
        #print(animCurve)
        # 帧的时间值
        time = mc.keyframe(animCurve, q=1, tc=1)
        #print(time)
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
                    infoW += ' ' + str(inputAngle[i]) + ' ' + str(outputAngle[i])
                else:
                    if inputType[i] in specialFix  or outputType[i] in specialFix  and weightLock[i] != 'True':
                        infoW += ' ' + str(inputAngle[i]) + ' ' + str(inputWeight[i]) + ' ' + str(outputAngle[i]) + ' ' + str(outputWeight[i])
                infoAll.append(infoW + ';')
        return infoAll

    #------------------------------#
    # 获取物体上游真正的animCurve
    def skGetAnimCurvs(self,checkObj):
        needObj = []
        inputAttr = mc.listConnections(checkObj,s=1,d=0,plugs=1)
        findState = 1
        if inputAttr:
            inputAttr = inputAttr[0]
            checkType = mc.nodeType(inputAttr)
            while 'animCurve' not in checkType:
                if checkType in ['addDoubleLinear']:
                    inputAttr = inputAttr.replace('.output','.input1')
                inputTemp = mc.listConnections(inputAttr,s=1,d=0,plugs=1)

                if inputTemp:
                    inputAttr = inputTemp[0]
                    checkType = mc.nodeType(inputAttr)
                else:
                    checkType = 'animCurve'
                    findState = 0
            if findState:
                needObj = [inputAttr.split('.')[0]]
            else:
                needObj = []
        return needObj

    #------------------------------#
    # 处理数据，并输出
    def checkCacheVStateExport(self ,cacheObjs= [], shotType = 2 ,server = 1,rootMode = 0 , projStyle = 0 ,renderGrp = 'MODEL'):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        if projStyle in [2]:
            renderGrp = 'MODEL'
        if not cacheObjs:
            modelGrps = mc.ls('*:%s*'%renderGrp,type = 'transform',l=1)
            # 排除多个MODEL组的
            needModeGrps = []
            for checkGrp in modelGrps:
                tempInfos = checkGrp.split(renderGrp)
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
        ObjsVDataLocalPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,projStyle = projStyle)
        fileName = 'cacheObjVInfo.txt'
        self.checkFileWrite((ObjsVDataLocalPath + fileName ), resultData)
        if server:
            ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,projStyle = projStyle)
            runCmd = 'zwSysFile("copy","' + (ObjsVDataLocalPath + fileName) + '","' + (ObjsVDataServerPath + fileName) + '",1)'
            mel.eval(runCmd)
            print(u'\n')
            print(u'=====================【cacheObjVInfo】【服务器端】【输出】完毕=====================')
            print(u'\n')
        return  resultData

    #------------------------------#
    # v信息导入
    def checkCacheVStateImport(self , shotType = 2,server = 1,projStyle = 0):
        vData = self.checkObjsVData(shotType,server,projStyle = projStyle)
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
                lockState = mc.getAttr(objAttr,l=1)
                if lockState:
                    continue
                mc.setAttr(objAttr,vState)
            # 多帧
            else:
                for i in range(len(keyInfo)):
                    vState = keyInfo[i][0]
                    frame = keyInfo[i][1]
                    mc.currentTime(frame)
                    lockState = mc.getAttr(objAttr,l=1)
                    if lockState:
                        continue
                    mc.setAttr(objAttr,vState)
                    mc.setKeyframe(objAttr)

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
        '''
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
        '''
        import maya.api.OpenMaya as OpenMaya
        objList = OpenMaya.MGlobal.getSelectionListByName(checkObj)
        result = int(objList.getDagPath(0).isVisible())
        return result

    #------------------------------#
    #------------------------------#
    # 写文件
    def checkFileWrite(self, path , info , addtion=0):
        print(u'>>>>>>[write]')
        print(path)
        if addtion == 1:
            info = self.checkFileRead(path) + info
        #txt = open(path, 'w')
        try:
            txt = open(path,'w')
        except:
            print('----------')
            print(path)
            txt = open(path,'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()

    #------------------------------#
    # 读文件
    def checkFileRead(self, path):
        print(u'>>>>>>[read]')
        print(path)
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
                            mc.disconnectAttr('%s'% (connectAttr[0]), '%s'% (ctrl + attr))
                        mc.setAttr((ctrl + attr),0)
            else:
                self.checkAnimCurveInfoExport([], serverFile = serverFile, infoFile = 'moveInfo',shotType = shotType)

    #-------------------------------------#
    # 新建参考
    def sk_FLRefRebuild(self,refInfos,noNeedRefNodeInfo,projStyle = 0):
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]

        print('[Ref Info]')
        print(refInfos[0][0])
        print('[NoNeedRef Info]')
        print(noNeedRefNodeInfo)
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
                    print(u'\n')
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print(u'\n')
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print(u'\n')
            else:
                if '_' not in refNode:
                    continue
                setState = 0
                if projStyle in [1]:
                    if refNode.split('_')[1][0] in ['s', 'S']:
                        setState = 1
                if projStyle in [2]:
                    if 'BG_' in refNode:
                        setState = 1
                if not setState:
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
                    print(u'\n')
                    print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                    print(u'\n')

    #------------------------------#
    # 【辅助】【备份材质】
    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,faceMode = 1,cacheMode = 1 ,shotType = 3,projStyle = 0):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if not mc.ls(obj):
                    errorObjs.append(obj)
            if errorObjs:
                print(u'------------------------以下物体不存在------------------------')
                for info in errorObjs:
                    print(info)
                print(u'------------------------以上物体不存在------------------------')
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
            self.checkCacheRecordMaterialExport(MatLists,shotType,projStyle = projStyle)
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
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0,shotType = 2,forceMode = 1):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport(shotType)
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
    def checkCacheRecordMaterialExport(self,MatLists,shotType = 2,projStyle = 0):
        localShaderInfoPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=0,infoMode=15,projStyle = projStyle)
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
        serverDataPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=1,infoMode=15,projStyle = projStyle)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print(serverDataPath)
        print(u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo)

    #------------------------------#
    # 【核心】回到原点cache处理，导入信息
    #------------------------------#
    def checkCacheResetPositionImport(self,serverFile = 1, shotType = 2,projStyle = 0):
        if not projStyle:
            projStyle = sk_infoConfig.sk_infoConfig().checkProjStyle()
        # 读控制器
        infoFile = 'moveInfo'
        path = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = serverFile,infoMode = 15,shotInfos = [],projStyle = projStyle)
        print('---pathInfo')
        print(path + infoFile + '_objs.txt')
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
    # 【辅助】【材质信息导入】【拆分用】
    #------------------------------#
    # 输出材质信息
    def checkCacheRecordMaterialImport(self,shotType,server = 1):
        serverDataPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server=server,infoMode=15)
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
            checkAdd += 1
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
    # 【辅助】【传递file动画】
    #------------------------------#
    # bake并导出动画信息
    def sk_checkTextureAnimationExport(self,server,projStyle = 0):
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
            ObjsVDataLocalPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 15,projStyle = projStyle)
            fileInfo = 'txAnimation'
            self.checkAnimCurveInfoExport(needNodes,infoFile = fileInfo,targetPath = ObjsVDataLocalPath)
            if server:
                ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 15,projStyle = projStyle)
                fileName = '%s.sla'%fileInfo
                runCmd = 'zwSysFile("copy","' + (ObjsVDataLocalPath + fileName ) + '","' + (ObjsVDataServerPath + fileName) + '",1)'
                mel.eval(runCmd)
                print(ObjsVDataServerPath + fileName)
                fileName = '%s_objs.txt'%fileInfo
                runCmd = 'zwSysFile("copy","' + (ObjsVDataLocalPath + fileName ) + '","' + (ObjsVDataServerPath + fileName) + '",1)'
                mel.eval(runCmd)
                print(ObjsVDataServerPath + fileName)
                print(u'\n')
                print(u'=====================【txNodesAnimation】【服务器端】【输出】完毕=====================')
                print(u'\n')

    # txFile动画导入
    def sk_checkTextureAnimationImport(self,server):
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15)
        fileInfo = 'txAnimation'
        checkFileA = '%s%s.sla'%(ObjsVDataServerPath,fileInfo)
        checkFileB = '%s%s_objs.txt'%(ObjsVDataServerPath,fileInfo)
        if os.path.exists(checkFileA) and os.path.exists(checkFileB):
            self.checkAnimCurveInfoImport(infoFile = fileInfo,targetPath = ObjsVDataServerPath)
            print(u'=====================【txNodesAnimation】【还原】完毕=====================')

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
    def checkObjsVData(self, shotType = 2,server = 1,projStyle = 0):
        #ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType)
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = server,infoMode = 15,projStyle = projStyle)
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
                print(u'====已经删除【%s】参考===' % setinfoList[2][i].split('_')[1])

            refRNnew='csl_'+ID+'RN'
            refNamespaceN='csl_'+ID+'_h'
            refoldfile=setinfoList[1][0]
            refoldinfo=setinfoList[1][0].split('_')[1]
            refFileN=refoldfile.replace(refoldinfo,ID)
            mc.file(refFileN, r=1, namespace=refNamespaceN , referenceNode = refRNnew)
            mc.file(rename=(temppath+fileshort))
            mc.file(save=1,type ='mayaBinary',f = 1)
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
            print(u'====【%s】场景已经替换===' %    fileshort)
            print(u'====文件路径【%s】===' %    temppath)
        else:
            print(u'===【%s】没有需要替换的场景===='  %    fileshort)


    # test
    def testDef(self,numInfo):
        print('------[test]-%s'%numInfo)

    # 清理OTC_GRP里非VFX_GRP和Cluster_GRP的非参考物体
    def sceneNotRefMeshClean(self,keepObjs = []):
        otcGrp = '|OTC_GRP'
        if not mc.ls(otcGrp):
            return
        childGrps = mc.listRelatives(otcGrp,c=1,f=1)
        if not childGrps:
            return
        for checkGrp in childGrps:
            if checkGrp in keepObjs:
                continue
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

    # 获取otc里参考物体列表
    def otcRefCheck(self):
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

