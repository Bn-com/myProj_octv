# -*- coding: utf-8 -*-

'''
Created on 2016-08-29

@author: 陈嘉伟
'''
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import shutil
import os
import math
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.TF import TF_renderTools
reload(TF_renderTools)
from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
reload(sk_smoothSet)
class TF_AutoRenderLayerClass(object):
    def __init__(self):
        pass
    # 读文件名得到镜头信息
    def CJW_ShotInfoData(self, fileName):
        # 读文件名全路径  'E:/Scripts/TF/Render/tf_act01_001_001_an_c001.ma'
        # ThisFileNamePath = mc.file(query=1, exn=1)
        # 读文件名 'tf_act01_001_001_an_c001.ma'
        # ThisFileNameAll = ThisFileNamePath.split('/')[-1]
        if '_' in fileName:
            shotInfo = fileName.split('_')
            return shotInfo
        else:
            mc.warning(u'========================【！！！文件名不规范！！！】========================')

    def TF_localRenderLayerPath(self, fileName, shotType=3):
        shotInfo = self.CJW_ShotInfoData(fileName)
        localRenderLayerPath = []
        if shotType == 2:
            localRenderLayerPath = ('E:/Info_Temp/renderLayerFile/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/')
        if shotType == 3:
            localRenderLayerPath = ('E:/Info_Temp/renderLayerFile/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/' + str(shotInfo[3]) + '/')
        # 如无路径文件，建立
        mc.sysFile(localRenderLayerPath, makeDir=True)
        return localRenderLayerPath

    def TF_SaveSceneAsAscii(self,fileName, type='_Base.ma'):
        # <mayaBinary> <mayaAscii>
        # u'E:/Scripts/TF/Render/tf_act01_001_001_an_c001.ma'
        if '.mb' in fileName:
            maBaseFileName = fileName.replace('.mb',type)
        elif '.ma' in fileName:
            maBaseFileName = fileName.replace('.ma',type)
        else:
            maBaseFileName =[]
            mc.warning(u'========================【！！！请用maya格式文件！！！】========================')
            mc.error(u'========================【！！！非maya文件！！！】========================')
        # mc.file(rename = maRgFile)
        # 本地分层文件保存路径
        localRenderLayerPath = self.TF_localRenderLayerPath(fileName, shotType=3)
        # 本地base文件路径
        baseFileNamePath = localRenderLayerPath + maBaseFileName
        # 再次打组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        mc.select(cl=1)
        baseGrps = ['CAM_GRP','CHR_GRP','PRP_GRP','SET_GRP','OTC_GRP']
        # 选组,选objeceSet物体节点 ======选中导出会丢失动画啊，尼玛逼的~
        '''
        mc.select(baseGrps,r=1)
        quickSets = mc.ls(type = 'objectSet')
        if quickSets:
            for obj in quickSets:
                if 'smooth' in obj:
                    mc.select(obj,add = 1,ne = 1)
        mc.file(baseFileNamePath,f=1,es=1, pr=1, type = 'mayaAscii')
        '''
        mc.file(rename = baseFileNamePath)
        mc.file(save=1,type = 'mayaAscii',f = 1)
        print (u'====================成功保存Base的ma文件====================')
        mc.select(cl=1)
        return baseFileNamePath

    # 替换参考路径，并把替换写入，清理一遍废插件
    def TF_SwitchReferencePath(self, path, oldName, newName):
        # oldName = '_h_ms_anim.mb'
        # newName = '_h_ms_render.mb'
        # path = 'D:/Info_Temp/renderLayerFile/tf/act01/001/tf_act01_001_001_an_c002_Base.ma'
        txt = open(path, 'r')
        try:
            fileContents = txt.readlines()
            for i in range(len(fileContents)):
                # 先替换参考
                if oldName in fileContents[i]:
                    newPath = fileContents[i].replace(oldName,newName)
                    fileContents[i] = newPath
                # 再清理插件
                if 'requires "' in fileContents[i] and 'requires maya "2014"; ' not in fileContents[i]:
                    newPath = fileContents[i].replace(fileContents[i],'')
                    fileContents[i] = newPath
        finally:
            txt.close()
        txt = open(path, 'w')
        try:
            txt.writelines(fileContents)
        finally:
            txt.close()

    # 读取数据库信息 1 fetchone单行 | 2 fetchall全行
    def TF_ReadServerData(self, shotInfo, cmd_name = '', returnAll = 1):
        import pyodbc
        # 连接数据库 不用改
        cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=192.168.168.16;DATABASE=idmtPlex_ToothFairies;UID=EWAUser;PWD=hk#$G#324f')
        # 数据库连接状态
        cursor = cnxn.cursor()
        # episode 集  scene 场  shot 镜头
        Episode = shotInfo[1]
        Scene = shotInfo[2]
        Shot = shotInfo[3]
        if not cmd_name:
            cmd_name = 'select VSGC.anim_ep,VSGC.Tag,VSGC.anim_sc,VSGC.unfixed5 as Locations, VSGC.unfixed6 as TimeOfDay, VSGC.unfixed7 as TypeOfSky,VSGC.unfixed8 as Sky from idmtPlex_ToothFairies.dbo.View_SsomAnimationCG_CompositeLoad VSGC where VSGC.anim_ep=\'%s\' and VSGC.Tag=\'%s\' and VSGC.anim_sc=\'%s\''%(str(Episode),str(Scene),str(Shot))
        needInfo=''
        data = []
        # 数据库返回数据
        try:
            if returnAll in [0,1]:
                data = cursor.execute(cmd_name).fetchone()
            if returnAll in [2]:
                data = cursor.execute(cmd_name).fetchall()
            if returnAll:
                return data
            # 处理数据
            if data:
                needInfo = int(str(data).split('\'')[1].split('\'')[0])
        # 关闭连接
        finally:
            cursor.close()
            cnxn.close()
        return needInfo

    def TFRenderLayerAutoCreate(self):
        print (u'=================================================================')
        print (u'====================!!!开始自动分层!!!====================')
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)
        from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
        reload(sk_animCurveCore)
        # 不加入自动分层的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        # 回到masterLayer层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # 分组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
        # tf_act01_001_001_an_c002_Base.ma
        ThisFileName = (mc.file(query=1, exn=1)).split('/')[-1]
        # u'tf', u'act01', u'001', u'019', u'an', u'c004.mb']
        shotInfo = self.CJW_ShotInfoData(ThisFileName)
        # 读取数据库信息
        # ('act01', u'000', '001', 'l024001FloatingIslandPathway', 'Day', 'fairyworld_CLOUDS', '')
        # ('act01', u'000', '002', 'l022001FloatingIslandEXT', 'Day', 'fairyworld_CLOUDS', 'Y')
        # ('act01', u'002', '001', 'l002001AirliesBedroomINT', 'Night\nStormy', 'realworld_NIGHT', 'Y')
        # ('act01', u'004', '001', 'l002001AirliesBedroomINT', 'Dawn', 'realworld_DAWN', 'Y')
        # ('act01', u'004', '024', 'l007001AirliesHouseEXT', 'Autumn Day', 'realworld_AUTUMN', 'Y')
        ServerInfoData = self.TF_ReadServerData(shotInfo,returnAll=1)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        # 记录动画文件内隐藏或放入norender层的物体,返回为正确的shape节点
        AllHideObjShapes = self.CJW_checkHideObj()
        self.checkNorenderInfoExport(AllHideObjShapes)
        # 保存Base文件为ma格式,返回本机base文件路径
        baseFileNamePath = self.TF_SaveSceneAsAscii(ThisFileName, type='_Base.ma')
        # 首先把所有_ms_anim参考全转成_ms_render
        self.TF_SwitchReferencePath(baseFileNamePath, '_ms_anim.mb','_ms_render.mb')
        if not ServerInfoData[3] == '':
            print (u'====此镜头场景为%s氛围===='%ServerInfoData[4])
            # 由于尼玛沟通问题，以下只支持一个场景分层
            # 分层种类
            SceneColor = '_l1ScClr'
            SceneDepth = '_l1ScDepth'
            SceneOCC = '_l1ScOcc'
            SceneLGTDay = '_l2SclgtDay'
            SceneLGTDawn = '_l2SclgtDawn'
            SceneLGTNight = '_l3SclgtNight'
            SceneIdp = '_l4ScIdp'
            SceneIDP = '_l1IDP'
            SceneRG = '_l1RG'
            #####秋天########
            SceneColorAutumn = '_l1ScClrAutumnDay'
            SceneDepthAutumn = '_l1ScDepthAutumnDay'
            SceneOCCAutumn = '_l1ScOccAutumnDay'
            SceneLGTAutumn = '_l2SclgtAutumnDay'
            SceneIdpAutumn = '_l4ScIdpAutumnDay'
            SceneIDPAutumn = '_l1IDPAutumnDay'
            SceneRGAutumn = '_l1RGAutumnDay'
            if ServerInfoData[3] in ['l007001AirliesHouseEXT','l002001AirliesBedroomINT']:
                if ServerInfoData[4] in ['Day']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDay,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Day'
                elif ServerInfoData[4] in ['Dawn']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDawn,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Dawn'
                elif ServerInfoData[4] in ['Night','Stormy']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTNight,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Night'
                elif ServerInfoData[4] in ['Autumn Day']:
                    AllLayerFile = [SceneColorAutumn,SceneDepthAutumn,SceneOCCAutumn,SceneLGTAutumn,SceneIdpAutumn,SceneIDPAutumn]
                    SceneRigFile = SceneRGAutumn
                    keyLight = 'Key_Light_Autumn'
                else:
                    mc.warning(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                    mc.error(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                print (u'====此镜头场景属于"l007001AirliesHouseEXT",为%s氛围'%ServerInfoData[4])
            else:
                keyLight = 'Key_Light_Day'
                '''
                # 以下为支持其他场景分层
                print (u'====此镜头场景为%s氛围'%ServerInfoData[4])
                if ServerInfoData[4] in ['Day']:
                    keyLight = 'Key_Light_Day'
                elif ServerInfoData[4] in ['Dawn']:
                    keyLight = 'Key_Light_Dawn'
                elif ServerInfoData[4] in ['Night','Storm']:
                    keyLight = 'Key_Light_Night'
                elif ServerInfoData[4] in ['Autumn Day']:
                    keyLight = 'Key_Light_Autumn'
                else:
                    mc.warning(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                    mc.error(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                '''
            # bake 动画曲线
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
            # cam bake 相机
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,3)
            # 分组
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(0)
            # 记得记录set的namespace ！！！#
            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            for ns in refNamespaces:
                if '_' not in ns:
                    continue
                # 记录场景nameSpace
                if ServerInfoData[3][0:7] in ns:
                    TheNamespace = ns
                    print (u'====================!!!得到场景nameSpace!!!====================%s'%TheNamespace)
            # 导出 SET_GRP 内场景参考的动画，保存到一个我还不想知道的位置
            shotLoaclPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server =0,infoMode = 6)
            shotSetAnimFile = shotLoaclPath + 'shotSet_'
            ctrlShapes = mc.listRelatives('SET_GRP',ad = 1, type = 'nurbsCurve',f=1)
            ctrlGrps = []
            if ctrlShapes:
                ctrlGrps = mc.listRelatives(ctrlShapes,p=1,f=1,type = 'transform')
            startFrame = mc.playbackOptions(min=1,q=1)
            endFrame = mc.playbackOptions(max=1,q=1)
            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoExport( ctrlGrps, serverFile = 0, infoFile='anim' , targetPath = shotSetAnimFile , shotType = 3,frameRange = [startFrame,endFrame])
            # 读取MaserLighting路径下所有文件，
            if ServerInfoData[3]:
                checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/MasterLighting/'
                # 路径下有可能不止 mb文件，有可能有iff文件
                MaserLightingFiles = mc.getFileList(folder = checkFileExists)
                if MaserLightingFiles:
                    for MaserLightingFile in MaserLightingFiles:
                        if MaserLightingFile.split('.')[-1] == 'mb' and '_h_ms_l1rg' not in MaserLightingFile and '_h_ms_l1idp' not in MaserLightingFile:
                            MaserLightingFilePath = checkFileExists + MaserLightingFile
                            # 打开网上分好层的场景文件
                            print '-----------info'
                            print MaserLightingFilePath
                            mc.file(MaserLightingFilePath,open = 1 , f = 1)
                            # 添加NameSpace 公子牛叉啊~
                            # 先清理非参考的namespace
                            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
                            reload(sk_sceneTools)
                            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
                            # 再赋予namespace
                            mc.namespace(add = TheNamespace)
                            mc.namespace(set = ':')
                            # 这里应该都是SET的名字
                            rootGrps = ['SET']
                            allGrps = mc.listRelatives(rootGrps,pa=1,ad=1,f = 1)
                            allGrps += rootGrps
                            for checkObj in allGrps:
                                mc.rename(checkObj,(TheNamespace + ':' + checkObj.split('|')[-1]))
                            # 本地分层文件保存路径
                            # ThisFileName = 'tf_act01_001_001_an_c001.mb'
                            localRenderLayerPath = self.TF_localRenderLayerPath(ThisFileName, shotType=3)
                            # 分层名称
                            # MaserLightingFile = u'tf_l007001AirliesHouseEXT_h_ms_l1idpautumnday.mb'
                            layerFileName = MaserLightingFile.split('.')[0].split('_')[4]
                            # 最后分层文件重命名  FileName = 'tf_act02_019_006_l1idp_lr_c001.mb'
                            fileName = ThisFileName.replace('_an_', '_'+layerFileName+'_lr_')
                            # c00*版本号改c001
                            fileName2 = fileName.replace(fileName.split('_')[-1].split('.')[0], 'c001')
                            # 保存本地分层文件
                            FileNamePath = localRenderLayerPath + fileName2
                            # shutil.copy(MaserLightingFilePath, FileNamePath)
                            mc.file(rename=FileNamePath)
                            mc.file(save=True)
                            #-----------------------------------------------------------------#
                            print (u'=================================================================')
                            print (u'====================!!!开始导入动画!!!====================')
                            # 打开刚才的文件
                            mc.file(FileNamePath,open = 1 , f = 1)
                            # 参考相机
                            from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
                            reload(sk_hbExportCam)
                            sk_hbExportCam.sk_hbExportCam().camServerReference(3)
                            # 导入 | 记得打开文件后把文件名改成镜头名字！！！
                            from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
                            reload(sk_infoConfig)
                            shotLoaclPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server =0,infoMode = 6)
                            shotSetAnimFile = shotLoaclPath + 'shotSet_'
                            from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
                            reload(sk_animCurveCore)
                            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoImport( serverFile = 0, infoFile='anim' , targetPath = shotSetAnimFile , shotType = 3,missStop = 0,simpleGrpMode = 1)
                            # 尝试隐藏动画文件里的物体
                            for hideObjShape in AllHideObjShapes:
                                try:
                                    mc.setAttr(hideObjShape+'.visibility',0)
                                except:
                                    pass
                            # 再次保存文件,是这样吧，公子~
                            mc.file(save=1,type = 'mayaBinary',f = 1)
                            print (u'====================!!!导入动画完成并成功保存文件!!!====================%s'%fileName2)
                        if MaserLightingFile.split('.')[-1] == 'mb' and '_h_ms_l1idp' in MaserLightingFile:
                            renderLayer = 'IDP'
                            # 另存文件
                            layerFileName = MaserLightingFile.split('.')[0].split('_')[4]
                            SceneFileNamePath = baseFileNamePath.replace('_an_', '_'+layerFileName+'_lr_')
                            SceneFileNamePath2 = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
                            shutil.copy(baseFileNamePath, SceneFileNamePath2)
                            print (u'====成功保存分层文件%s'%SceneFileNamePath2)
                            # 替换参考
                            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
                            newName = 'MasterLighting/'+ MaserLightingFile
                            self.TF_SwitchReferencePath(SceneFileNamePath2,oldName,newName)
                            # 注意，替换参考是不用保存文件的，是以文本方式修改的。
                            print (u'====成功替换文件场景参考成MasterLighting路径下的====')
                            # 打开文件
                            mc.file(SceneFileNamePath2,open = 1 , f = 1)
                            print (u'====打开分层文件，准备建层===%s'%SceneFileNamePath2)
                            # 读取文件内参考物体
                            CHRAllShapes = []
                            SETAllShapes = []
                            PRPAllShapes = []
                            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
                            for ns in refNamespaces:
                                if 'tf_' not in ns or 'c009001' in ns or 'c013001' in ns or 'c014001' in ns or 'c019001' in ns or 'c020001' in ns or 'c022001' in ns or 'c023001' in ns or 'c021001' in ns:
                                    continue
                                if ns.split('_')[1][0] in ['c'] and mc.objExists(ns + ':MSH_all'):
                                    needMeshFulls = mc.ls((ns + ':MSH_all'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in CHRAllShapes:
                                        CHRAllShapes.append(taskAllShapes2)
                                # 场景只读取表格里面有的做idp，其他灯光层场景不用处理，已经手动分好层的。
                                if ns.split('_')[1][0] in ['l'] and ServerInfoData[3] in ns and mc.objExists(ns + ':MSH_all'):
                                    needMeshFulls = mc.ls((ns + ':MSH_all'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in SETAllShapes:
                                        SETAllShapes.append(taskAllShapes2)
                                if ns.split('_')[1][0] in ['p'] and mc.objExists(ns + ':MSH_all'):
                                    needMeshFulls = mc.ls((ns + ':MSH_all'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in PRPAllShapes:
                                        PRPAllShapes.append(taskAllShapes2)
                            # 清理大组为['a','b','c']形式
                            CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
                            SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
                            PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
                            # 建层
                            AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
                            for item in AllRenderLayers:
                                if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                                    mc.setAttr(item+'.renderable', 0)
                            if 'IDP' not in AllRenderLayers:
                                renderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='IDP')
                                mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
                                # 设置渲染属性
                                TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                            # 把角色道具场景放入渲染层，加遮罩材质，场景不用加，已经添加好蓝色了.
                            mc.editRenderLayerMembers(renderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
                            mc.select(cl=1)
                            if CHRAllShapesClear:
                                mc.select(CHRAllShapesClear,r=1)
                                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                                mc.select(cl=1)
                            if PRPAllShapesClear:
                                mc.select(PRPAllShapesClear,r=1)
                                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                                mc.select(cl=1)
                            # 由于建层名称不统一，已令渲染在master上材质，插件自动建层加入。
                            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                            # 尝试隐藏动画文件里的物体
                            for hideObjShape in AllHideObjShapes:
                                try:
                                    mc.setAttr(hideObjShape+'.visibility',0)
                                except:
                                    pass
                            # 转存mb文件，删除ma文件
                            mc.file(save=1,type = 'mayaBinary',f = 1)
                            print (u'====成功保存%s渲染层mb文件==='%layerFileName)
                            os.remove(SceneFileNamePath2)
                            print (u'====场景角色道具互动Idp渲染层完成===')
            else:
                mc.warning(u'========================【！！！表格场景读取失败！！！】%s========================'%ServerInfoData[3])
                mc.error(u'========================【！！！表格场景读取失败！！！】%s========================'%ServerInfoData[3])
            # 马勒戈壁的再加个rg场景文件读取
            SceneRigFile = '_l1rg'
            '''
            # 由于尼玛沟通问题，以下只支持一个场景分层
            if ServerInfoData[3] == 'l007001AirliesHouseEXT':
                if ServerInfoData[4] == 'Day':
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDay,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Day'
                elif ServerInfoData[4] == 'Dawn':
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDawn,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Dawn'
                elif ServerInfoData[4] == 'Night\nStormy':
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTNight,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Night'
                elif ServerInfoData[4] == 'Autumn Day':
                    AllLayerFile = [SceneColorAutumn,SceneDepthAutumn,SceneOCCAutumn,SceneLGTAutumn,SceneIdpAutumn,SceneIDPAutumn]
                    SceneRigFile = SceneRGAutumn
                    keyLight = 'Key_Light_Autumn'
                else:
                    mc.warning(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                    mc.error(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                print (u'====此镜头场景属于"l007001AirliesHouseEXT",为%s氛围'%ServerInfoData[4])
                # 先复制文件并根据功能重命名
                for LayerFile in AllLayerFile:
                    if '_an_' in baseFileNamePath:
                        # tf_act01_001_001_an_c001_Base.ma
                        # tf_act01_001_001_l1IDP_lr_c001.ma
                        SceneFileNamePath = baseFileNamePath.replace('_an_', LayerFile+'_lr_')
                        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
                        # 另存新文件
                        shutil.copy(baseFileNamePath, SceneFileNamePath)
                        print (u'====成功保存分层文件%s'%SceneFileNamePath)
                        # 替换参考 /master/tf_c003001Twinkle_h_ms_render.mb   /MasterLighting/tf_c003001Twinkle_h_ms_render.mb
                        oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render'
                        newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ LayerFile
                        checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName + '.mb'
                        # 先检测下替换的参考文件是否存在
                        if os.path.exists(checkFileExists):
                            self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                            print (u'====成功修改文件参考成MasterLighting路径下的====%s'%checkFileExists)
                            # 打开文件，建立渲染层，赋材质球，导入参考，保存mb文件，删除ma文件, 是否建立渲染层 type = 0
                            if 'IDP' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='IDP', type=1)
                            if 'ScClr' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='amb', type=0)
                            if 'ScDepth' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='depth', type=0)
                            if 'ScOcc' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='AO', type=0)
                            if 'Sclgt' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='lgt01', type=0)
                            if 'ScIdp' in LayerFile:
                                self.TF_OpenLRfileCreateLayer(SceneFileNamePath, renderlayer='id01', type=0)
                            # 由于ma文件无法不打开直接转存mb，所以还是要打开一次
                            # else:
                            #     print (u'====渲染层%s完成==='%LayerFile)
                            #     # 转存mb文件，删除ma文件
                            #     mc.file(save=1,type = 'mayaBinary',f = 1)
                            #     os.remove(SceneFileNamePath)
                        else:
                            mc.warning(u'========================【！！！此路径下无相关文件！！！%s】========================'%checkFileExists)
                            mc.error(u'========================【！！！此路径下无相关文件！！！%s】========================'%checkFileExists)
                    else:
                        mc.warning(u'========================【！！！请用动画文件！！！】========================')
                        mc.error(u'========================【！！！非an动画镜头文件！！！】========================')
            else:
                # 以下为支持其他场景分层
                print (u'====此镜头场景为%s氛围'%ServerInfoData[4])
                if ServerInfoData[4] == 'Day':
                    keyLight = 'Key_Light_Day'
                elif ServerInfoData[4] == 'Dawn':
                    keyLight = 'Key_Light_Dawn'
                elif ServerInfoData[4] == 'Night\nStormy':
                    keyLight = 'Key_Light_Night'
                elif ServerInfoData[4] == 'Autumn Day':
                    keyLight = 'Key_Light_Autumn'
                else:
                    mc.warning(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                    mc.error(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                # 读取MaserLighting路径下所有文件，
                if ServerInfoData[3]:
                    checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/MasterLighting/'
                    # 路径下有可能不止 mb文件，有可能有iff文件
                    MaserLightingFiles = mc.getFileList(folder = checkFileExists)
                    if MaserLightingFiles:
                        for MaserLightingFile in MaserLightingFiles:
                            # MaserLightingFile = u'tf_l007001AirliesHouseEXT_h_ms_l1idp.mb',
                            # MaserLightingFile = u'tf_l007001AirliesHouseEXT_h_ms_l1idpautumnday.mb',
                            if MaserLightingFile.split('.')[-1] == 'mb' and '_h_ms_l1rg' not in MaserLightingFile:
                                layerFileName = MaserLightingFile.split('.')[0].split('_')[4]
                                # 另存文件
                                SceneFileNamePath = baseFileNamePath.replace('_an_', '_'+layerFileName+'_lr_')
                                SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
                                shutil.copy(baseFileNamePath, SceneFileNamePath)
                                print (u'====成功保存分层文件%s'%SceneFileNamePath)
                                # 替换参考
                                oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
                                newName = 'MasterLighting/'+ MaserLightingFile
                                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                                print (u'====成功替换文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
                                # 如果是IDP文件才需要打开文件
                                # 不打开文件保存不了mb格式啊贱人
                                mc.file(SceneFileNamePath,open = 1 , f = 1)
                                print (u'====打开分层文件，准备建层===%s'%SceneFileNamePath)
                                # 参考物体
                                # 多个角色会出现 [['A','B','C'],['A','B','C'],['A','B','C']]这种情况
                                CHRAllShapes = []
                                SETAllShapes = []
                                PRPAllShapes = []
                                refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
                                for TheNamespace in refNamespaces:
                                    if '_' not in TheNamespace:
                                        continue
                                    for noRenderChr in noRenderCharacters:
                                        if noRenderChr in TheNamespace:
                                            continue
                                    if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                                        needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                                        taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                        taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                        if taskAllShapes2 not in CHRAllShapes:
                                            CHRAllShapes.append(taskAllShapes2)
                                    # 场景只读取表格里面有的做idp，其他灯光层场景不用处理，已经手动分好层的。
                                    if TheNamespace.split('_')[1][0] in ['l'] and ServerInfoData[3] in TheNamespace and mc.objExists(TheNamespace + ':MSH_all'):
                                        needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                                        taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                        taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                        if taskAllShapes2 not in SETAllShapes:
                                            SETAllShapes.append(taskAllShapes2)
                                    if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                                        needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                                        taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                        taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                        if taskAllShapes2 not in PRPAllShapes:
                                            PRPAllShapes.append(taskAllShapes2)
                                # 清理大组为['a','b','c']形式
                                CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
                                SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
                                PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
                                # 创建渲染层
                                if '_h_ms_l1idp' in MaserLightingFile:
                                    renderLayer = 'IDP'
                                    AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
                                    for item in AllRenderLayers:
                                        if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                                            mc.setAttr(item+'.renderable', 0)
                                    if 'IDP' not in AllRenderLayers:
                                        renderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='IDP')
                                        mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
                                        # 设置渲染属性
                                        TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                                    # 把角色道具场景放入渲染层，加遮罩材质，场景不用加，已经添加好蓝色了.
                                    mc.editRenderLayerMembers(renderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
                                    mc.select(cl=1)
                                    if CHRAllShapesClear:
                                        mc.select(CHRAllShapesClear,r=1)
                                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                                        mc.select(cl=1)
                                    if PRPAllShapesClear:
                                        mc.select(PRPAllShapesClear,r=1)
                                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                                        mc.select(cl=1)
                                        # 由于建层名称不统一，已令渲染在master上材质，插件自动建层加入。
                                    print (u'====场景角色道具互动Idp渲染层完成===')
                                    # 场景灯光都已建好层，删除角色道具参考即可
                                    # 已沟通，选择不删除角色参考
                                    # rfPaths = mc.file(q = 1,reference =1)
                                    # for rfPath in rfPaths:
                                    #     if rfPath.split('/')[-1].split('_')[1][0] == 'c' or rfPath.split('/')[-1].split('_')[1][0] == 'p':
                                    #         reNode = mc.referenceQuery(rfPath, referenceNode=1)
                                    #         mc.file(rfn = reNode , removeReference=1)
                                # 扫描文件中每个渲染层，设置渲染属性
                                AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
                                for item in AllRenderLayers:
                                    if not item == 'defaultRenderLayer' and not item == '*:defaultRenderLayer':
                                        mc.editRenderLayerGlobals(currentRenderLayer = item)
                                        TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                                mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
                                sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                                # 转存mb文件，删除ma文件
                                mc.file(save=1,type = 'mayaBinary',f = 1)
                                print (u'====成功保存%s渲染层mb文件==='%layerFileName)
                                os.remove(SceneFileNamePath)
                    else:
                        mc.warning(u'========================【！！！无此路径存在！！！%s】========================'%checkFileExists)
                        mc.error(u'========================【！！！无此路径存在！！！%s】========================'%checkFileExists)
            '''
        else:
            print (u'=================================================================')
            print (u'====================!!!此镜头无场景，跳过场景分层!!!%s===================='%ThisFileName)
            pass
        print (u'=================================================================')
        print (u'====================!!!场景分层完成，下面进入角色分层!!!====================')
        print (u'---------')
        # 上面主要是针对场景分层，下面是角色道具分层
        # 角色灯光颜文件分层---------ChClr------------
        print (u'---------')
        print (u'-------------------------开始角色ChClr文件分层-----------------------------')
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l4ChClr_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        if not ServerInfoData[3] == '':
            # 开始替换rg场景文件参考
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile+'.mb'
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
        else:
            print (u'====此镜头无场景文件====%s'%ThisFileName)
        # 开文件建层,调用面板插件
        mc.file(SceneFileNamePath,open = 1 , f = 1)
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrColor')
        mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        print (u'====渲染层ChrColor完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrAmb')
        print (u'====渲染层ChrAmb完成===')
        ChrWingMeshs = []
        for wingMesh in ChrAndPropsClean:
            if TF_renderTools.TF_renderToolsClass().CJW_readTansformAttr(wingMesh,'wing') and wingMesh not in ChrWingMeshs:
                ChrWingMeshs.append(wingMesh)
        if ChrWingMeshs:
            mc.select(cl=1)
            mc.select(ChrAndPropsClean,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrWingAmb')
            print (u'====渲染层ChrWingAmb完成===')
        else:
            print (u'====ChrWingAmb层无wing物体，不创建层===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderLGTLayer(transparency=0)
        print (u'====渲染层ChrLGT完成===')
        # 导入所有参考
        # sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 再次清理废节点
        # self.CJW_CleanUselesNodes(SceneFileNamePath)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        self.CJW_chrRenderSettings(type=0)
        # 尝试隐藏动画文件里的物体
        for hideObjShape in AllHideObjShapes:
            try:
                mc.setAttr(hideObjShape+'.visibility',0)
            except:
                pass
        # 转存mb文件，删除ma文件
        mc.file(save=1,type = 'mayaBinary',f = 1)
        os.remove(SceneFileNamePath)
        print (u'-------------------------角色ChClr文件分层完成-----------------------------')
        print (u'---------')
        # 开始角色非灯光层分层
        print (u'---------')
        print (u'-------------------------开始角色ChOcc文件分层-----------------------------')
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l3ChOcc_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        if not ServerInfoData[3] == '':
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile+'.mb'
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
        else:
            print (u'====此镜头无场景文件====%s'%ThisFileName)
        # 把所有参考再全转成_ms_anim文件
        self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render.mb','_ms_anim.mb')
        # 开文件建层,调用面板插件
        mc.file(SceneFileNamePath,open = 1 , f = 1)
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderOCCLayer(layer='ChrOCC',transparency=0)
        print (u'====渲染层ChrOCC完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderNormalLayer(transparency=0)
        print (u'====渲染层ChrNormal完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderFresnelLayer(transparency=0)
        print (u'====渲染层ChrFresnel完成===')
        # 导入所有参考
        # sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 再次清理废节点
        # self.CJW_CleanUselesNodes(SceneFileNamePath)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        self.CJW_chrRenderSettings(type=0)
        # 尝试隐藏动画文件里的物体
        for hideObjShape in AllHideObjShapes:
            try:
                mc.setAttr(hideObjShape+'.visibility',0)
            except:
                pass
        # 转存mb文件，删除ma文件
        mc.file(save=1,type = 'mayaBinary',f = 1)
        os.remove(SceneFileNamePath)
        print (u'-------------------------角色ChOcc文件分层完成-----------------------------')
        print (u'---------')
        # 追加角色wing层 ---------------------------
        print (u'---------')
        print (u'-------------------------wing 角色文件分层开始-----------------------------')
        wingCharacters13 = ['c006001Triana','c008001LadySirona','c030001BloomFairyRose','c031001BloomFairyLily','c004001Avalanne','c007001Brigida','c011001Bree','c011002BreewithComicalHairdo','c011002BreewithComicalHairdo','c026001Clarissa','c027001Rochelle','c029001GenericPixie02','c028001GenericPixie01']
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l2wing_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        if not ServerInfoData[3] == '':
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile+'.mb'
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
        else:
            print (u'====此镜头无场景文件====%s'%ThisFileName)
        # 开文件建层
        mc.file(SceneFileNamePath,open = 1 , f = 1)
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        XX = 0
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            for wingCharacter in wingCharacters13:
                if wingCharacter in TheNamespace:
                    XX = 1
            if XX==1 and TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if XX==1 and TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFull = mc.ls((TheNamespace + ':MSH_all'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        if ChrAndProps:
            ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        if XX ==1:
            mc.select(cl=1)
            mc.select(ChrAndPropsClean,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrWingColor')
            print (u'====渲染层ChrColor完成===')
            mc.select(cl=1)
            mc.select(ChrAndPropsClean,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderOCCLayer(layer='ChrWingOCC',transparency=0)
            print (u'====渲染层ChrOCC完成===')
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
            self.CJW_chrRenderSettings(type=0)
            # 尝试隐藏动画文件里的物体
            for hideObjShape in AllHideObjShapes:
                try:
                    mc.setAttr(hideObjShape+'.visibility',0)
                except:
                    pass
            # 转存mb文件，删除ma文件
            mc.file(save=1,type = 'mayaBinary',f = 1)
            os.remove(SceneFileNamePath)
            print (u'-------------------------wing 角色文件分层完成-----------------------------')
        else:
            os.remove(SceneFileNamePath)
            print (u'====无wing类角色，删除wing分层文件====%s')
        print (u'---------')
        # 角色IDP层
        '''
        if '_an_' in baseFileNamePath:
            SceneFileNamePath = baseFileNamePath.replace('_an_', '_l4ChIdp_lr_')
            SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
            shutil.copy(baseFileNamePath, SceneFileNamePath)
            print (u'====成功保存分层文件%s'%SceneFileNamePath)
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName + '.mb'
            print '------------'
            print checkFileExists
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
                # 项目组-把所有参考再全转成_ms_anim文件
                self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render','_ms_anim')
                # 开文件建层,调用面板插件
                mc.file(SceneFileNamePath,open = 1 , f = 1)
                # 清除材质
                #mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteShadingGroupsAndMaterials");hyperShadePanelMenuCommand("hyperShadePanel1", "deleteTextures");hyperShade -assign lambert1;SelectAll;hyperShade -assign initialShadingGroup;select -cl;')
                # 清理无用节点，这个好用啊啊啊啊 啊
                # mel.eval('MLdeleteUnused')
                TF_renderTools.TF_renderToolsClass().TF_RGBMAInfoLayerCreat()
                sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                self.()
                print (u'====渲染层ChrIDP完成===')
                mc.file(save=1,type = 'mayaBinary',f = 1)
                os.remove(SceneFileNamePath)
            else:
                mc.warning(u'========================【！！！无成功替换参考！！！】========================%s'%checkFileExists)
                mc.error(u'========================【！！！无成功替换参考！！！】========================%s'%checkFileExists)
        else:
            mc.warning(u'========================【！！！请用动画文件！！！】========================')
            mc.error(u'========================【！！！非an动画镜头文件！！！】========================')
        '''
        # 角色、场景、道具。conSHD 接触阴影层。 conOcc 接触occ层。
        # 这两个场景移出建层文件 'l014001' 'l021001'
        print (u'---------')
        print (u'-------------------------角色场景接触阴影和Occ接触层开始-----------------------------')
        if not ServerInfoData[3] == '' and 'l014001' not in ServerInfoData[3] and 'l021001' not in ServerInfoData[3]:
            SceneFileNamePath = baseFileNamePath.replace('_an_', '_l2con_lr_')
            SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
            shutil.copy(baseFileNamePath, SceneFileNamePath)
            print (u'====成功保存分层文件%s'%SceneFileNamePath)
            # 把所有参考再全转成_ms_anim文件
            self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render.mb','_ms_anim.mb')
            # 开文件,
            mc.file(SceneFileNamePath,open = 1 , f = 1)
            # 通过参考得到角色场景信息
            CHRAllShapes = []
            SETAllShapes = []
            PRPAllShapes = []
            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            for TheNamespace in refNamespaces:
                if '_' not in TheNamespace:
                    continue
                #for noRenderChr in noRenderCharacters:
                #    if noRenderChr in TheNamespace:
                #        continue
                if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                    needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in CHRAllShapes:
                        CHRAllShapes.append(taskAllShapes2)
                if TheNamespace.split('_')[1][0] in ['l'] and mc.objExists(TheNamespace + ':MSH_all'):
                    needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in SETAllShapes:
                        SETAllShapes.append(taskAllShapes2)
                if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                    needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in PRPAllShapes:
                        PRPAllShapes.append(taskAllShapes2)
            # 清理大组为['a','b','c']形式
            CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
            SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
            PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
            # 导入所有参考
            sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
            #reset SG
            mel.eval('zwResetShadingEnginesN')
            # 清理无用节点,删除其他层，自建材质球删除所有材质球。
            self.CJW_ClearUnusedNode(deleteLayer=1, cleanType=1)
            #
            mel.eval('zwResetShadingEnginesN')
            # 再次保存此ma文件
            # mc.file(save=1,type = 'mayaAscii',f = 1)
            # 以文本清理插件
            # self.CJW_CleanUselesNodes(SceneFileNamePath)
            # 再次打开此文件,预计应该比较快了
            # mc.file(SceneFileNamePath,open = 1 , f = 1)
            # 创建材质球，添加所有模型shape
            materialsNodes =mc.ls(mat=1)
            shaderNode = 'conShadow_shader'
            if shaderNode not in materialsNodes:
                shadowShader = mc.shadingNode('useBackground', asShader=1, name = shaderNode)
                mc.setAttr(shadowShader+'.specularColor', 0, 0, 0, type='double3')
                mc.setAttr(shadowShader+'.reflectivity', 0)
                mc.setAttr(shadowShader+'.reflectionLimit', 0)
                shadowShaderSG = mc.sets(renderable =1, noSurfaceShader =1, empty=1, name =(shadowShader+'SG'))
                mc.connectAttr((shadowShader +'.outColor'),(shadowShaderSG +'.surfaceShader'),f=1)
            else:
                shadowShader = shaderNode
                shadowShaderSG = shadowShader+'SG'
            # 创建渲染层
            AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
            for item in AllRenderLayers:
                if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                    mc.setAttr(item+'.renderable', 0)
            conSHDrenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='conSHD')
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            # 设置渲染属性
            TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
            # 把物体加入渲染层
            mc.editRenderLayerMembers(conSHDrenderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
            # 物体添加材质球
            mc.sets(CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear,e=1, forceElement = shadowShaderSG)
            # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
            ChrAndProps = CHRAllShapesClear+PRPAllShapesClear
            for shape in ChrAndProps:
                mc.setAttr(shape+'.primaryVisibility', 0)
            # 场景物体关闭投射属性 setAttr "pSphereShape1.castsShadows" 0;
            for shape in SETAllShapesClear:
                mc.setAttr(shape+'.castsShadows', 0)
            # 添加场景主灯
            FuckingLights = mc.ls(type = 'light')
            for FuckingLight in FuckingLights:
                if '*:'+keyLight or keyLight:
                    if keyLight in FuckingLight or '*:'+keyLight in FuckingLight:
                        mc.editRenderLayerMembers(conSHDrenderLayer,FuckingLight, noRecurse=0)
                        print (u'====成功添加阴影主灯====')
                else:
                    print (u'====注意！！！无发现阴影层主灯====')
            print (u'====渲染层%s完成==='%conSHDrenderLayer)
            ## =======================================创建conOcc接触occ层========================================== ##
            # 创建材质球
            materialsNodes =mc.ls(mat=1)
            shaderName = 'conOCC_shader'
            OCCTextureName = 'conOCC_texture'
            if (mc.pluginInfo('Mayatomr.mll',query=1,loaded=1) == False):
                mc.loadPlugin('Mayatomr.mll')
            if shaderName not in materialsNodes:
                OCCTexture = mc.shadingNode('mib_amb_occlusion',asTexture=1,name = OCCTextureName)
                mc.setAttr(OCCTexture+'.samples',136)
                mc.setAttr(OCCTexture+'.spread',0.8)
                mc.setAttr(OCCTexture+'.max_distance',2)
                mc.setAttr(OCCTexture+'.output_mode',0)
                mc.setAttr(OCCTexture+'.falloff',1)
                mc.setAttr(OCCTexture+'.id_inclexcl',0)
                mc.setAttr(OCCTexture+'.id_nonself',1)
                OCCShader = mc.shadingNode('surfaceShader',asShader=1,name = shaderName)
                mc.connectAttr((OCCTexture +'.outValue'),(OCCShader +'.outColor'),f=1)
                OCCShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(OCCShader+'SG'))
                mc.connectAttr((OCCShader +'.outColor'),(OCCShaderSG +'.surfaceShader'),f=1)
            else:
                OCCShader = shaderName
                OCCShaderSG = OCCShader+'SG'
                OCCTexture = OCCTextureName
            # 创建渲染层
            conOccrenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='conOcc')
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            # 设置渲染属性
            TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
            # 把所有物体加入渲染层
            mc.editRenderLayerMembers(conOccrenderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
            # 物体添加材质球
            mc.sets(CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear,e=1, forceElement = OCCShaderSG)
            # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
            ChrAndProps = CHRAllShapesClear+PRPAllShapesClear
            for shape in ChrAndProps:
                mc.setAttr(shape+'.primaryVisibility', 0)
            # 场景物体添加miLabel属性
            for SETAllShape in SETAllShapesClear:
                transform = mc.listRelatives(SETAllShape, p=1, f=1, type='transform')[0]
                if not mc.objExists(transform+'.miLabel'):
                    mc.addAttr(transform, shortName='miLabel',longName='miLabel',defaultValue=1.0, minValue=0.0, maxValue=1.0, attributeType='double',k=1)
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
            self.CJW_chrRenderSettings(type=0)
            # 尝试隐藏动画文件里的物体
            for hideObjShape in AllHideObjShapes:
                try:
                    mc.setAttr(hideObjShape+'.visibility',0)
                except:
                    pass
            # 转存mb文件
            mc.file(save=1,type = 'mayaBinary',f = 1)
            # 删除之前ma文件
            os.remove(SceneFileNamePath)
            print (u'---------')
            print (u'-------------------------角色场景接触阴影和Occ接触层完成-----------------------------')
            print (u'---------')
        else:
            print (u'====此镜头文件无表格内场景，或为l014001,l021001号场景，无需做阴影层和接触层===%s'%ThisFileName)
        '''
        # 角色之间的整体遮罩，如果一个镜头里有大量角色，互相直接的遮罩
        print (u'---------')
        print (u'-------------------------角色Ch All IDP 文件分层开始-----------------------------')
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l3ChAllIdp_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        if not ServerInfoData[3] == '':
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName + '.mb'
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
        else:
             print (u'====此镜头无场景文件====%s'%ThisFileName)
        # 把所有参考再全转成_ms_anim文件
        self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render','_ms_anim')
        # 开文件,建层
        mc.file(SceneFileNamePath,open = 1 , f = 1)
        # 下组为查几个角色，为MSH_all 组长名
        Characters = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if '_' not in TheNamespace:
                continue
            for noRenderChr in noRenderCharacters:
                if noRenderChr in TheNamespace:
                    continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace+':CHR|'+TheNamespace+':MODEL|'+TheNamespace+':MSH_all'):
                needMeshFull = mc.ls((TheNamespace+':CHR|'+TheNamespace+':MODEL|'+TheNamespace+':MSH_all'), l=1)[0]
                if needMeshFull not in Characters:
                    Characters.append(needMeshFull)
        # 导入所有参考
        sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 清理无用节点,删除其他层，自建材质球删除所有材质球。
        self.CJW_ClearUnusedNode(deleteLayer=1, cleanType=1)
        print (u'====清理无用节点，强制删除材质球和层，成功====')
        # 开始计算角色与层
        layerCount = int(math.ceil(len(Characters)/3.0))
        for i in range(layerCount):
            Id = i+1
            # 建层,把全部角色放入层内，先赋予黑遮罩
            mc.select(cl=1)
            if len(Characters) > 1:
                mc.select(Characters,r=1)
                IdpRenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name=('chrAllID0'+str(Id)))
                print (u'====成功建立%s渲染层===='%IdpRenderLayer)
                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'M', transparency=0)
                print (u'====成功添加M遮罩了====')
                mc.select(cl=1)
                # 设置渲染属性
                TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                print (u'====成功设置了渲染属性了哇====')
                # 给相关3角色添加 红、绿、蓝遮罩
                if Id*3 <= len(Characters):
                    needChrs = Characters[0:Id*3]
                    print (u'====不打印一下不行了，搞不掂啊%s%s===='%(needChrs,[needChrs[-3]]))
                    taskAllShapes01 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-3]])
                    CHRAllShapesClear01 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes01)
                    mc.select(cl=1)
                    if CHRAllShapesClear01:
                        mc.select(CHRAllShapesClear01,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes02 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-2]])
                    CHRAllShapesClear02 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes02)
                    mc.select(cl=1)
                    if CHRAllShapesClear02:
                        mc.select(CHRAllShapesClear02,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes03 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-1]])
                    CHRAllShapesClear03 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes03)
                    mc.select(cl=1)
                    if CHRAllShapesClear03:
                        mc.select(CHRAllShapesClear03,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'B', transparency=0)
                        mc.select(cl=1)
                else:
                    print (u'====不打印一下不行了，搞不掂啊啊啊啊%s===='%[Characters[-2]])
                    taskAllShapes04 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([Characters[-2]])
                    CHRAllShapesClear04 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes04)
                    mc.select(cl=1)
                    if CHRAllShapesClear04:
                        mc.select(CHRAllShapesClear04,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes05 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([Characters[-1]])
                    CHRAllShapesClear05 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes05)
                    mc.select(cl=1)
                    if CHRAllShapesClear05:
                        mc.select(CHRAllShapesClear05,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                        mc.select(cl=1)
                print (u'====角色相互遮罩渲染层创建完成===')
                sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                self.()
                mc.file(save=1,type = 'mayaBinary',f = 1)
                print (u'====角色相互遮罩渲染mb文件保存成功===')
                os.remove(SceneFileNamePath)
            else:
                mc.warning(u'========================【！！！此镜头文件内角色不超过一个，无需做角色互动分层文件！！！】========================%s'%baseFileNamePath)
                os.remove(SceneFileNamePath)
        print (u'-------------------------角色Ch All IDP 文件分层完成-----------------------------')
        print (u'---------')
        '''
    # 打开一个文件，建立渲染层, 赋材质球，导入参考，保存mb文件，删除ma文件,type=0为不建层，1为建层。
    def TF_OpenLRfileCreateLayer(self,SceneFileNamePath, renderlayer, type=1):
        # 不加入RGB层里的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        #
        mc.file(SceneFileNamePath,open = 1 , f = 1)
        print (u'====打开分层文件，准备建层===%s'%SceneFileNamePath)
        # 读所有渲染层
        renderLayer = renderlayer
        AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
        for item in AllRenderLayers:
            if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                mc.setAttr(item+'.renderable', 0)
        if type==1 and renderlayer not in AllRenderLayers:
            renderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name=renderlayer)
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
        # 设置渲染属性
        TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
        # 参考物体
        # 多个角色会出现 [['A','B','C'],['A','B','C'],['A','B','C']]这种情况
        CHRAllShapes = []
        SETAllShapes = []
        PRPAllShapes = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in CHRAllShapes:
                    CHRAllShapes.append(taskAllShapes2)
            # 此命令只针对那个特殊场景
            if TheNamespace.split('_')[1][0] in ['l'] and 'l007001AirliesHouseEXT' in TheNamespace and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in SETAllShapes:
                    SETAllShapes.append(taskAllShapes2)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in PRPAllShapes:
                    PRPAllShapes.append(taskAllShapes2)
        # 清理大组为['a','b','c']形式
        CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
        SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
        PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
        # 确定渲染层，判断相关哪些Shape加入渲染层，并上材质
        self.TF_assignMeterialShader(CHRAllShapesClear,SETAllShapesClear,PRPAllShapesClear,renderlayer)
        print (u'====渲染层%s完成==='%renderLayer)
        # 导入所有参考
        #sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 再次清理废节点
        #self.CJW_CleanUselesNodes(SceneFileNamePath)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        self.CJW_chrRenderSettings(type=0)
        # 转存mb文件，删除ma文件
        mc.file(save=1,type = 'mayaBinary',f = 1)
        print (u'====成功保存%s渲染层mb文件==='%renderlayer)
        os.remove(SceneFileNamePath)

    # 确定渲染层，判断相关Shape加入渲染层，并上材质
    def TF_assignMeterialShader(self, CHRAllShapes, SETAllShapes, PRPAllShapes, renderlayer):
        if renderlayer == 'IDP':
            mc.editRenderLayerMembers(renderlayer, CHRAllShapes+SETAllShapes+PRPAllShapes, noRecurse=0)
            mc.select(cl=1)
            if CHRAllShapes:
                mc.select(CHRAllShapes,r=1)
                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                mc.select(cl=1)
            if PRPAllShapes:
                mc.select(PRPAllShapes,r=1)
                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                mc.select(cl=1)
        '''
        # 安全考虑，不删除角色道具参考了
        if renderlayer == 'amb' or renderlayer == 'depth' or renderlayer == 'AO' or renderlayer == 'lgt01' or renderlayer == 'id01':
            # 场景灯光都已建好层，删除角色道具参考即可
            rfPaths = mc.file(q = 1,reference =1)
            for rfPath in rfPaths:
                if rfPath.split('/')[-1].split('_')[1][0] == 'c' or rfPath.split('/')[-1].split('_')[1][0] == 'p':
                    reNode = mc.referenceQuery(rfPath, referenceNode=1)
                    mc.file(rfn = reNode , removeReference=1)
        '''

    # 清理ma 文件内废插件、节点
    def CJW_CleanUselesNodes(self,path):
        txt = open(path, 'r')
        try:
            fileContents = txt.readlines()
            for i in range(len(fileContents)):
                if 'requires "' in fileContents[i] and 'requires maya "2014"; ' not in fileContents[i]:
                    newPath = fileContents[i].replace(fileContents[i],'')
                    fileContents[i] = newPath
        finally:
            txt.close()
        txt = open(path, 'w')
        try:
            txt.writelines(fileContents)
        finally:
            txt.close()

    # 返回默认渲染层，建立tempLambertShader，连接所有模型，然后删除所有材质球。——主要功能为在不破坏原有材质的基础上清理无用材质球
    # deleteLayer=0时为不删除非默认渲染层，deleteLayer=1时为删除所有非默认渲染层。
    # cleanType=0时为删除无连接、无用材质及节点，cleanType=1时为删除无用节点，并强制删除所有材质信息。
    def CJW_ClearUnusedNode(self, deleteLayer=0, cleanType=0):
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        materialsNodes =mc.ls(mat=1)
        shaderName = 'tempLambertShader'
        tempLambertShaderSG = 'tempLambertShaderSG'
        if shaderName not in materialsNodes:
            tempLambertShader = mc.shadingNode('lambert', asShader=1, name='tempLambertShader')
            tempLambertShaderSG = mc.sets(renderable=1, noSurfaceShader=1, empty=1, name=(tempLambertShader+'SG'))
            mc.connectAttr((tempLambertShader + '.outColor'), (tempLambertShaderSG + '.surfaceShader'), f=1)
        AllMeshShapes = mc.ls(type = 'mesh',l=1)
        for MeshShape in AllMeshShapes:
            if 'MSH_all|' in MeshShape:
                try:
                    mc.sets(MeshShape, e=1, forceElement=tempLambertShaderSG)
                except:
                    pass
        if deleteLayer == 1:
            AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
            for renderLayer in AllRenderLayers:
                if 'defaultRenderLayer' not in renderLayer:
                    mc.delete(renderLayer)
        if cleanType == 0:
            # 清理无用节点，这个好用啊啊啊啊 啊
            mel.eval('MLdeleteUnused')
        if cleanType == 1:
            # 清理无用节点，这个好用啊啊啊啊 啊
            mel.eval('MLdeleteUnused')
            # 删除所有材质
            try:
                mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1");')
            except:
                pass
            try:
                mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteShadingGroupsAndMaterials");hyperShadePanelMenuCommand("hyperShadePanel1", "deleteTextures");hyperShade -assign lambert1;SelectAll;hyperShade -assign initialShadingGroup;select -cl;')
            except:
                pass
        try:
            # 由于强制删除命令会把这个也删掉，所以要try下
            mc.delete(shaderName,tempLambertShaderSG)
        except:
            pass

    # 自读参考
    def CJW_taskAllShapes(self,CHR,SET,PRPA):
        # 不加入RGB层里的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        #
        CHRAllShapes = []
        SETAllShapes = []
        PRPAllShapes = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in CHRAllShapes:
                    CHRAllShapes.append(taskAllShapes2)
            # 场景只读取表格里面有的做idp，其他灯光层场景不用处理，已经手动分好层的。
            if TheNamespace.split('_')[1][0] in ['l'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in SETAllShapes:
                    SETAllShapes.append(taskAllShapes2)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MSH_all'):
                needMeshFulls = mc.ls((TheNamespace + ':MSH_all'), l=1)
                taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                if taskAllShapes2 not in PRPAllShapes:
                    PRPAllShapes.append(taskAllShapes2)
        # 清理大组为['a','b','c']形式
        CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
        SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
        PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
        taskShapeInfos = [CHRAllShapesClear,SETAllShapesClear,PRPAllShapesClear]
        return taskShapeInfos

    # 设置摄像机可渲染属性  # ('act01', u'004', '024', 'l007001AirliesHouseEXT', 'Autumn Day', 'realworld_AUTUMN', 'Y')
    def CJW_settingCameraAttr(self,  shotInfo):
        localCam = 'cam_'+ shotInfo[1]+'_'+shotInfo[2]
        AllCameras = mc.ls(type='camera')
        for Camera in AllCameras:
            mc.setAttr(Camera+'.renderable', 0)
            transformGrp = mc.listRelatives(Camera,parent=1,type='transform')[0]
            if localCam in transformGrp:
                mc.setAttr(Camera+'.renderable', 1)
    # 角色渲染设置
    # type = 0为角色，type=1为场景
    def CJW_chrRenderSettings(self,type=0):
        mc.setAttr('miDefaultOptions.miRenderUsing',2)
        try:
            mel.eval('optionMenuGrp -e -select 3 miSampleModeCtrl')
            mel.eval('attrControlGrp -edit -enable 1 miMinSampleCtrl')
        except:
            pass
        mc.setAttr('miDefaultOptions.maxSamples',2)
        mc.setAttr('miDefaultOptions.minSamples',0)
        if type == 0:
            mc.setAttr('miDefaultOptions.contrastR',0.01)
            mc.setAttr('miDefaultOptions.contrastG',0.01)
            mc.setAttr('miDefaultOptions.contrastB',0.01)
            mc.setAttr('miDefaultOptions.contrastA',0.01)
        if type == 1:
            mc.setAttr('miDefaultOptions.contrastR',0.1)
            mc.setAttr('miDefaultOptions.contrastG',0.1)
            mc.setAttr('miDefaultOptions.contrastB',0.1)
            mc.setAttr('miDefaultOptions.contrastA',0.1)
    # 角色之间的整体遮罩，如果一个镜头里有大量角色，互相直接的遮罩
    def TF_ChrAllIdpCreateLayer(self):
        print (u'---------')
        print (u'-------------------------角色Ch All IDP 文件分层开始-----------------------------')
        # 下组为查几个角色，为MSH_all 组长名
        Characters = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if '_' not in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace+':CHR|'+TheNamespace+':MODEL|'+TheNamespace+':MSH_all'):
                needMeshFull = mc.ls((TheNamespace+':CHR|'+TheNamespace+':MODEL|'+TheNamespace+':MSH_all'), l=1)[0]
                if needMeshFull not in Characters:
                    Characters.append(needMeshFull)
        # 导入所有参考
        # sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 清理无用节点,删除其他层，自建材质球。
        self.CJW_ClearUnusedNode(deleteLayer=1, cleanType=0)
        print (u'====清理无用节点，强制删除材质球和层，成功====')
        print (u'====开始计算角色与层====')
        layerCount = int(math.ceil(len(Characters)/3.0))
        for i in range(layerCount):
            Id = i+1
            # 建层,把全部角色放入层内，先赋予黑遮罩
            mc.select(cl=1)
            if len(Characters) > 1:
                mc.select(Characters,r=1)
                IdpRenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name=('chrAllID0'+str(Id)))
                print (u'====成功建立%s渲染层===='%IdpRenderLayer)
                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'M', transparency=0)
                print (u'====成功添加M遮罩了====')
                mc.select(cl=1)
                # 设置渲染属性
                TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                print (u'====成功设置了渲染属性了哇====')
                # 给相关3角色添加 红、绿、蓝遮罩
                if Id*3 <= len(Characters):
                    needChrs = Characters[0:Id*3]
                    print (u'====不打印一下不行了，搞不掂啊%s%s===='%(needChrs,[needChrs[-3]]))
                    taskAllShapes01 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-3]])
                    CHRAllShapesClear01 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes01)
                    mc.select(cl=1)
                    if CHRAllShapesClear01:
                        mc.select(CHRAllShapesClear01,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes02 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-2]])
                    CHRAllShapesClear02 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes02)
                    mc.select(cl=1)
                    if CHRAllShapesClear02:
                        mc.select(CHRAllShapesClear02,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes03 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([needChrs[-1]])
                    CHRAllShapesClear03 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes03)
                    mc.select(cl=1)
                    if CHRAllShapesClear03:
                        mc.select(CHRAllShapesClear03,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'B', transparency=0)
                        mc.select(cl=1)
                else:
                    print (u'====不打印一下不行了，搞不掂啊啊啊啊%s===='%[Characters[-2]])
                    taskAllShapes04 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([Characters[-2]])
                    CHRAllShapesClear04 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes04)
                    mc.select(cl=1)
                    if CHRAllShapesClear04:
                        mc.select(CHRAllShapesClear04,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                        mc.select(cl=1)
                    taskAllShapes05 = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes([Characters[-1]])
                    CHRAllShapesClear05 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes05)
                    mc.select(cl=1)
                    if CHRAllShapesClear05:
                        mc.select(CHRAllShapesClear05,r=1)
                        TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                        mc.select(cl=1)
                sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                self.CJW_chrRenderSettings(type=0)
                print (u'====角色相互遮罩渲染层创建完成===')
            else:
                mc.warning(u'========================【！！！此镜头文件内角色不超过一个，无需做角色互动分层文件！！！】========================%s'%baseFileNamePath)
        print (u'-------------------------角色Ch All IDP 文件分层完成-----------------------------')
        print (u'---------')

    def TF_RenderLayerAutoCreate_Set(self):
        print (u'=================================================================')
        print (u'====================!!!开始自动分层——场景!!!====================')
        # 不加入自动分层的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        #
        # 回到masterLayer层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # tf_act01_001_001_an_c002_Base.ma
        ThisFileName = (mc.file(query=1, exn=1)).split('/')[-1]
        # u'tf', u'act01', u'001', u'019', u'an', u'c004.mb']
        shotInfo = self.CJW_ShotInfoData(ThisFileName)
        # 读取数据库信息
        # ('act01', u'000', '001', 'l024001FloatingIslandPathway', 'Day', 'fairyworld_CLOUDS', '')
        # ('act01', u'000', '002', 'l022001FloatingIslandEXT', 'Day', 'fairyworld_CLOUDS', 'Y')
        # ('act01', u'002', '001', 'l002001AirliesBedroomINT', 'Night\nStormy', 'realworld_NIGHT', 'Y')
        # ('act01', u'004', '001', 'l002001AirliesBedroomINT', 'Dawn', 'realworld_DAWN', 'Y')
        # ('act01', u'004', '024', 'l007001AirliesHouseEXT', 'Autumn Day', 'realworld_AUTUMN', 'Y')
        ServerInfoData = self.TF_ReadServerData(shotInfo,returnAll=1)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        # 修复文件内参考nameSpace
        from idmt.maya.TF import TF_sceneTools
        reload(TF_sceneTools)
        TF_sceneTools.TF_sceneTools().sk_sceneAssetNamespaceConfig()
        # 重置布料cache名称
        from idmt.maya.TF import TF_checkinClean
        reload(TF_checkinClean)
        TF_checkinClean.CJW_renovateNCache()
        # 清除非参考nameSpace
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # 再次打组 ，为参考
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        # 记录动画文件内隐藏或放入norender层的物体,返回为正确的shape节点----要在打组后运行
        AllHideObjShapes = self.CJW_checkHideObj()
        # 保存Base文件为ma格式,返回本机base文件路径
        baseFileNamePath = self.TF_SaveSceneAsAscii(ThisFileName, type='_Base.ma')
        # 首先把所有_ms_anim参考全转成_ms_render
        self.TF_SwitchReferencePath(baseFileNamePath, '_ms_anim.mb','_ms_render.mb')
        if not ServerInfoData[3] == '':
            print (u'====此镜头场景为%s氛围===='%ServerInfoData[4])
            # 由于尼玛沟通问题，以下只支持一个场景分层
            # 分层种类
            SceneColor = '_l1ScClr'
            SceneDepth = '_l1ScDepth'
            SceneOCC = '_l1ScOcc'
            SceneLGTDay = '_l2SclgtDay'
            SceneLGTDawn = '_l2SclgtDawn'
            SceneLGTNight = '_l3SclgtNight'
            SceneIdp = '_l4ScIdp'
            SceneIDP = '_l1IDP'
            SceneRG = '_l1RG'
            #####秋天########
            SceneColorAutumn = '_l1ScClrAutumnDay'
            SceneDepthAutumn = '_l1ScDepthAutumnDay'
            SceneOCCAutumn = '_l1ScOccAutumnDay'
            SceneLGTAutumn = '_l2SclgtAutumnDay'
            SceneIdpAutumn = '_l4ScIdpAutumnDay'
            SceneIDPAutumn = '_l1IDPAutumnDay'
            SceneRGAutumn = '_l1RGAutumnDay'
            if ServerInfoData[3] in ['l007001AirliesHouseEXT','l002001AirliesBedroomINT']:
                if ServerInfoData[4] in ['Day']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDay,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Day'
                elif ServerInfoData[4] in ['Dawn']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTDawn,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Dawn'
                elif ServerInfoData[4] in ['Night','Stormy']:
                    AllLayerFile = [SceneColor,SceneDepth,SceneOCC,SceneLGTNight,SceneIdp,SceneIDP]
                    SceneRigFile = SceneRG
                    keyLight = 'Key_Light_Night'
                elif ServerInfoData[4] in ['Autumn Day']:
                    AllLayerFile = [SceneColorAutumn,SceneDepthAutumn,SceneOCCAutumn,SceneLGTAutumn,SceneIdpAutumn,SceneIDPAutumn]
                    SceneRigFile = SceneRGAutumn
                    keyLight = 'Key_Light_Autumn'
                else:
                    mc.warning(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                    mc.error(u'========================【！！！表格出现非四种预定氛围！！！】========================')
                print (u'====此镜头场景属于"l007001AirliesHouseEXT",为%s氛围'%ServerInfoData[4])
            else:
                keyLight = 'Key_Light_Day'
            # bake 动画曲线
            from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
            reload(sk_cacheFinalLayout)
            sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()
            # cam bake 相机
            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
            reload(sk_sceneTools)
            #sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1,3)
            # 记得记录set的namespace ！！！#
            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            for ns in refNamespaces:
                if '_' not in ns:
                    continue
                # 记录场景nameSpace
                if ServerInfoData[3][0:7] in ns:
                    TheNamespace = ns
            if not TheNamespace == '':
                print (u'====================!!!得到场景nameSpace!!!====================%s'%TheNamespace)
            else:
                mc.warning(u'========================【！！！表格场景读取失败！！！】========================')
                mc.error(u'========================【！！！表格场景读取失败-此镜头内无表格标注的场景】========================')
            # 导出 SET_GRP 内场景参考的动画，保存到一个我还不想知道的位置
            from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
            reload(sk_infoConfig)
            shotLoaclPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server =0,infoMode = 6)
            shotSetAnimFile = shotLoaclPath + 'shotSet_'
            ctrlShapes = mc.listRelatives('SET_GRP',ad = 1, type = 'nurbsCurve',f=1)
            ctrlGrps = []
            if ctrlShapes:
                ctrlGrps = mc.listRelatives(ctrlShapes,p=1,f=1,type = 'transform')
            startFrame = mc.playbackOptions(min=1,q=1)
            endFrame = mc.playbackOptions(max=1,q=1)
            from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
            reload(sk_animCurveCore)
            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoExport( ctrlGrps, serverFile = 0, infoFile='anim' , targetPath = shotSetAnimFile , shotType = 3,frameRange = [startFrame,endFrame])
            # 读取MaserLighting路径下所有文件，
            if ServerInfoData[3]:
                checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/MasterLighting/'
                # 路径下有可能不止 mb文件，有可能有iff文件
                MaserLightingFiles = mc.getFileList(folder = checkFileExists)
                if MaserLightingFiles:
                    for MaserLightingFile in MaserLightingFiles:
                        if MaserLightingFile.split('.')[-1] == 'mb' and '_h_ms_l1rg' not in MaserLightingFile and '_h_ms_l1idp' not in MaserLightingFile:
                            MaserLightingFilePath = checkFileExists + MaserLightingFile
                            # 打开网上分好层的场景文件
                            print '-----------info'
                            print MaserLightingFilePath
                            mc.file(MaserLightingFilePath,open = 1 , f = 1)
                            # 先回到默认渲染层
                            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
                            # 设置摄像机渲染属性，此处场景文件内无相机
                            self.CJW_settingCameraAttr(shotInfo)
                            # 添加NameSpace 公子牛叉啊~
                            # 先清理非参考的namespace
                            from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
                            reload(sk_sceneTools)
                            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
                            # 再赋予namespace
                            mc.namespace(add = TheNamespace)
                            mc.namespace(set = ':')
                            # 这里应该都是SET的名字
                            rootGrps = ['SET']
                            allGrps = mc.listRelatives(rootGrps,pa=1,ad=1,f = 1)
                            allGrps += rootGrps
                            for checkObj in allGrps:
                                mc.rename(checkObj,(TheNamespace + ':' + checkObj.split('|')[-1]))
                            # 再次打组，场景为非参考状态，所以场景是自动放入了OTC_GRP组里，没放入SET_GRP里
                            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
                            mc.select(cl=1)
                            # 把场景SET组放入整理大组，此处如果是在渲染层处理的话，会把无关物体也放入到当前渲染层
                            try:
                                mc.parent(TheNamespace+':SET','SET_GRP')
                            except:
                                pass
                            # 本地分层文件保存路径
                            # ThisFileName = 'tf_act01_001_001_an_c001.mb'
                            # localRenderLayerPath = 'E:/Info_Temp/renderLayerFile/tf/act01/001/001/'
                            localRenderLayerPath = self.TF_localRenderLayerPath(ThisFileName, shotType=3)
                            # 分层名称
                            # MaserLightingFile = u'tf_l007001AirliesHouseEXT_h_ms_l1idpautumnday.mb'
                            layerFileName = MaserLightingFile.split('.')[0].split('_')[4]
                            # 最后分层文件重命名  FileName = 'tf_act02_019_006_l1idp_lr_c001.mb'
                            fileName = ThisFileName.replace('_an_', '_'+layerFileName+'_lr_')
                            # c00*版本号改c001
                            fileName2 = fileName.replace(fileName.split('_')[-1].split('.')[0], 'c001')
                            # 保存本地分层文件
                            FileNamePath = localRenderLayerPath + fileName2
                            # shutil.copy(MaserLightingFilePath, FileNamePath)
                            mc.file(rename=FileNamePath)
                            # 打开的是网上的masterLighting文件，保存的是本机场景分层文件
                            mc.file(save=True)
                            #-----------------------------------------------------------------#
                            print (u'=================================================================')
                            print (u'====================!!!开始导入动画!!!====================')
                            # 打开刚才的文件
                            mc.file(FileNamePath,open = 1 , f = 1)
                            # 参考相机
                            from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam
                            reload(sk_hbExportCam)
                            sk_hbExportCam.sk_hbExportCam().camServerReference(3)
                            # 导入 | 记得打开文件后把文件名改成镜头名字！！！
                            from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
                            reload(sk_infoConfig)
                            shotLoaclPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server =0,infoMode = 6)
                            shotSetAnimFile = shotLoaclPath + 'shotSet_'
                            from idmt.maya.commonCore.core_finalLayout import sk_animCurveCore
                            reload(sk_animCurveCore)
                            sk_animCurveCore.sk_animCurveCore().checkAnimCurveInfoImport( serverFile = 0, infoFile='anim' , targetPath = shotSetAnimFile , shotType = 3,missStop = 0,simpleGrpMode = 1)
                            # 尝试隐藏动画文件里的物体
                            for hideObjShape in AllHideObjShapes:
                                try:
                                    mc.setAttr(hideObjShape+'.visibility',0)
                                    print (u'====================!!!成功隐藏%s物体!!!===================='%hideObjShape)
                                except:
                                    print (u'====================!!!没成功隐藏%s物体!!!===================='%hideObjShape)
                            # 设置摄像机渲染属性
                            self.CJW_settingCameraAttr(shotInfo)
                            # 再次保存文件,是这样吧，公子~
                            mc.file(save=1,type = 'mayaBinary',f = 1)
                            print (u'====================!!!导入动画完成并成功保存文件!!!====================%s'%fileName2)
                        if MaserLightingFile.split('.')[-1] == 'mb' and '_h_ms_l1idp' in MaserLightingFile:
                            renderLayer = 'IDP'
                            # 另存文件
                            layerFileName = MaserLightingFile.split('.')[0].split('_')[4]
                            SceneFileNamePath = baseFileNamePath.replace('_an_', '_'+layerFileName+'_lr_')
                            SceneFileNamePath2 = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_Base', 'c001')
                            shutil.copy(baseFileNamePath, SceneFileNamePath2)
                            print (u'====成功保存分层文件%s'%SceneFileNamePath2)
                            # 替换参考,非灯光层，先把角色场景道具全换成anim
                            self.TF_SwitchReferencePath(SceneFileNamePath2, '_ms_render.mb', '_ms_anim.mb')
                            # 再把场景anim换成场景IDP
                            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_anim.mb'
                            newName = 'MasterLighting/'+ MaserLightingFile
                            self.TF_SwitchReferencePath(SceneFileNamePath2,oldName,newName)
                            # 注意，替换参考是不用保存文件的，是以文本方式修改的。
                            print (u'====成功替换文件场景参考成MasterLighting路径下的场景idp参考====')
                            # 打开文件
                            mc.file(SceneFileNamePath2,open = 1 , f = 1)
                            print (u'====打开分层文件，准备建层===%s'%SceneFileNamePath2)
                            # 设置摄像机渲染属性
                            self.CJW_settingCameraAttr(shotInfo)
                            # 读取文件内参考物体
                            CHRAllShapes = []
                            SETAllShapes = []
                            PRPAllShapes = []
                            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
                            for ns in refNamespaces:
                                if 'tf_' not in ns or 'c009001' in ns or 'c013001' in ns or 'c014001' in ns or 'c019001' in ns or 'c020001' in ns or 'c022001' in ns or 'c023001' in ns or 'c021001' in ns:
                                    continue
                                if ns.split('_')[1][0] in ['c'] and mc.objExists(ns + ':MODEL'):
                                    needMeshFulls = mc.ls((ns + ':MODEL'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in CHRAllShapes:
                                        CHRAllShapes.append(taskAllShapes2)
                                # 场景只读取表格里面有的做idp，其他灯光层场景不用处理，已经手动分好层的。
                                if ns.split('_')[1][0] in ['l'] and ServerInfoData[3] in ns and mc.objExists(ns + ':MODEL'):
                                    needMeshFulls = mc.ls((ns + ':MODEL'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in SETAllShapes:
                                        SETAllShapes.append(taskAllShapes2)
                                if ns.split('_')[1][0] in ['p'] and mc.objExists(ns + ':MODEL'):
                                    needMeshFulls = mc.ls((ns + ':MODEL'), l=1)
                                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                                    if taskAllShapes2 not in PRPAllShapes:
                                        PRPAllShapes.append(taskAllShapes2)
                            # 清理大组为['a','b','c']形式
                            CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
                            SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
                            PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
                            # 建层
                            AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
                            for item in AllRenderLayers:
                                if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                                    mc.setAttr(item+'.renderable', 0)
                            if 'IDP' not in AllRenderLayers:
                                renderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='IDP')
                                mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
                                # 设置渲染属性
                                TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                            # 把角色道具场景放入渲染层，加遮罩材质，场景不用加，已经添加好蓝色了.
                            mc.editRenderLayerMembers(renderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
                            mc.select(cl=1)
                            if CHRAllShapesClear:
                                mc.select(CHRAllShapesClear,r=1)
                                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'R', transparency=0)
                                mc.select(cl=1)
                            if PRPAllShapesClear:
                                mc.select(PRPAllShapesClear,r=1)
                                TF_renderTools.TF_renderToolsClass().TF_RBGMApass(type = 'G', transparency=0)
                                mc.select(cl=1)
                            # 由于建层名称不统一，已令渲染在master上材质，插件自动建层加入。
                            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
                            # 尝试隐藏动画文件里的物体
                            for hideObjShape in AllHideObjShapes:
                                try:
                                    mc.setAttr(hideObjShape+'.visibility',0)
                                except:
                                    pass
                            # 转存mb文件，删除ma文件
                            mc.file(save=1,type = 'mayaBinary',f = 1)
                            print (u'====成功保存%s渲染层mb文件==='%layerFileName)
                            os.remove(SceneFileNamePath2)
                            print (u'====场景角色道具互动Idp渲染层完成===')
            else:
                mc.warning(u'========================【！！！表格场景读取失败！！！】%s========================'%ServerInfoData[3])
                mc.error(u'========================【！！！表格场景读取失败！！！】%s========================'%ServerInfoData[3])
        else:
            print (u'=================================================================')
            print (u'====================!!!此镜头无场景，跳过场景分层!!!%s===================='%ThisFileName)
            pass
        print (u'=================================================================')
        print (u'====================!!!场景分层完成!!!====================')

    def TF_RenderLayerAutoCreate_Chr(self):
        print (u'=================================================================')
        print (u'====================!!!开始角色层自动分层!!!====================')
        # 不加入自动分层的角色
        noRenderCharacters = ['c009001Toothmouse','c013001PixelPixieFemale','c014001PixelPixieMale','c019001ReffieLion','c020001TambiKitten','c022001RosieSkunk','c023001RainbowBunny','c021001SnowettePoodle']
        # 所有有翅膀的角色
        wingCharacters = ['c002001Stacey','c003001Twinkle','c003002LittleTwinkle','c005001Gwendolyn','c006001Triana','c008001LadySirona','c030001BloomFairyRose','c031001BloomFairyLily','c032001BloomFairyGerberDaisy','c004001Avalanne','c007001Brigida','c011001Bree','c011002BreewithComicalHairdo','c024001Adriana','c025001Giselle','c026001Clarissa','c027001Rochelle','c028001GenericPixie01','c029001GenericPixie02']
        # 回到masterLayer层
        mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        # tf_act01_001_001_an_c002_Base.ma
        ThisFileName = (mc.file(query=1, exn=1)).split('/')[-1]
        # u'tf', u'act01', u'001', u'019', u'an', u'c004.mb']
        shotInfo = self.CJW_ShotInfoData(ThisFileName)
        # 读取数据库信息
        # ('act01', u'000', '001', 'l024001FloatingIslandPathway', 'Day', 'fairyworld_CLOUDS', '')
        # ('act01', u'000', '002', 'l022001FloatingIslandEXT', 'Day', 'fairyworld_CLOUDS', 'Y')
        # ('act01', u'002', '001', 'l002001AirliesBedroomINT', 'Night\nStormy', 'realworld_NIGHT', 'Y')
        # ('act01', u'004', '001', 'l002001AirliesBedroomINT', 'Dawn', 'realworld_DAWN', 'Y')
        # ('act01', u'004', '024', 'l007001AirliesHouseEXT', 'Autumn Day', 'realworld_AUTUMN', 'Y')
        ServerInfoData = self.TF_ReadServerData(shotInfo,returnAll=1)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        # 记录动画文件内隐藏或放入norender层的物体,返回为正确的shape节点
        AllHideObjShapes = self.CJW_checkHideObj()
        # 修复文件内参考nameSpace名称
        from idmt.maya.TF import TF_sceneTools
        reload(TF_sceneTools)
        TF_sceneTools.TF_sceneTools().sk_sceneAssetNamespaceConfig()
        # 重置布料cache名称
        from idmt.maya.TF import TF_checkinClean
        reload(TF_checkinClean)
        TF_checkinClean.CJW_renovateNCache()
        # 清除非参考nameSpace
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # 再次打组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        mc.select(cl=1)
        # 保存Base文件为ma格式,返回本机base文件路径
        baseFileNamePath = self.TF_SaveSceneAsAscii(ThisFileName, type='_ChrBase.ma')
        # 首先把所有_ms_anim参考全转成_ms_render
        self.TF_SwitchReferencePath(baseFileNamePath, '_ms_anim.mb','_ms_render.mb')
        # 角色类分层先把CHrBase文件的场景替换成rg文件
        SceneRigFile = '_l1rg'
        if not ServerInfoData[3] == '':
            print (u'====此镜头场景为%s氛围===='%ServerInfoData[4])
            if ServerInfoData[4] in ['Day','Storm']:
                keyLight = 'Key_Light_Day'
            elif ServerInfoData[4] in ['Dawn']:
                keyLight = 'Key_Light_Dawn'
            elif 'Night' in ServerInfoData[4]:
                keyLight = 'Key_Light_Night'
            elif ServerInfoData[4] in ['Autumn Day']:
                keyLight = 'Key_Light_Autumn'
            oldName = 'master/tf_'+ServerInfoData[3]+'_h_ms_render.mb'
            newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms'+ SceneRigFile+'.mb'
            checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName
            if os.path.exists(checkFileExists):
                self.TF_SwitchReferencePath(baseFileNamePath,oldName,newName)
                print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
            else:
                print (u'====请检查此镜头的场景，无发现l1rg文件====%s'%checkFileExists)
        else:
            keyLight = 'Key_Light_Day'
            print (u'====此镜头无场景文件====%s'%ThisFileName)
        # 角色灯光颜文件分层---------ChClr------------
        print (u'---------')
        print (u'-------------------------开始角色ChClr文件分层-----------------------------')
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l4ChClr_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_ChrBase', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        # 开文件建层,调用面板插件
        # mc.file(SceneFileNamePath,open = 1 , f = 1)
        # 修改为先打开壳文件，再导入动画文件
        RenderShellV001 = 'Z:/Projects/ToothFairies/Reference/Product manager/Render/RenderShell/RenderShellV001.mb'
        RenderShellV01 = 'Z:/Projects/ToothFairies/Reference/Product manager/Render/RenderShell/RenderShellV01.mb'
        mc.file(RenderShellV001,open = 1 , f = 1)
        mc.file(SceneFileNamePath,i = 1, f = 1)
        mc.file(rename = SceneFileNamePath)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        # ChrAndPropsClean = [u'|CHR_GRP|tf_c001001Airlie:CHR|tf_c001001Airlie:MODEL|tf_c001001Airlie:MSH_all','|CHR_GRP|tf_c002001Stacey:CHR|tf_c002001Stacey:MODEL|tf_c002001Stacey:MSH_all']
        ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrColor')
        mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        print (u'====渲染层ChrColor完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrAmb')
        print (u'====渲染层ChrAmb完成===')
        ChrWing_MSH_all = []
        for wingMesh in ChrAndPropsClean:
            for wingCharacter in wingCharacters:
                if wingCharacter in wingMesh and wingMesh not in ChrWing_MSH_all:
                    ChrWing_MSH_all.append(wingMesh)
        if ChrWing_MSH_all:
            mc.select(cl=1)
            mc.select(ChrWing_MSH_all,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrWingAmb')
            print (u'====渲染层ChrWingAmb完成===')
        else:
            print (u'====ChrWingAmb层无wing物体，不创建层===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderLGTLayer(transparency=0)
        print (u'====渲染层ChrLGT完成===')
        # 导入所有参考
        # sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 再次清理废节点
        # self.CJW_CleanUselesNodes(SceneFileNamePath)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        self.CJW_chrRenderSettings(type=0)
        # 尝试隐藏动画文件里的物体
        for hideObjShape in AllHideObjShapes:
            try:
                mc.setAttr(hideObjShape+'.visibility',0)
            except:
                pass
        # 转存mb文件，删除ma文件
        mc.file(save=1,type = 'mayaBinary',f = 1)
        os.remove(SceneFileNamePath)
        print (u'-------------------------角色ChClr文件分层完成-----------------------------')
        print (u'---------')
        # 开始角色非灯光层分层
        print (u'---------')
        print (u'-------------------------开始角色ChOcc文件分层-----------------------------')
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l3ChOcc_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_ChrBase', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        # 把所有参考再全转成_ms_anim文件
        self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render.mb','_ms_anim.mb')
        # 开文件建层,调用面板插件
        # mc.file(SceneFileNamePath,open = 1 , f = 1)
        # 修改为先打开壳文件，再导入动画文件
        mc.file(RenderShellV001,open = 1 , f = 1)
        mc.file(SceneFileNamePath,i = 1, f = 1)
        mc.file(rename = SceneFileNamePath)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        mel.eval('zwResetShadingEnginesN')
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderOCCLayer(layer='ChrOCC',transparency=0)
        print (u'====渲染层ChrOCC完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderNormalLayer(transparency=0)
        print (u'====渲染层ChrNormal完成===')
        mc.select(cl=1)
        mc.select(ChrAndPropsClean,r=1)
        TF_renderTools.TF_renderToolsClass().TF_RenderFresnelLayer(transparency=0)
        print (u'====渲染层ChrFresnel完成===')
        # 导入所有参考
        # sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
        # 再次清理废节点
        # self.CJW_CleanUselesNodes(SceneFileNamePath)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
        self.CJW_chrRenderSettings(type=0)
        # 尝试隐藏动画文件里的物体
        for hideObjShape in AllHideObjShapes:
            try:
                mc.setAttr(hideObjShape+'.visibility',0)
            except:
                pass
        # 转存mb文件，删除ma文件
        mc.file(save=1,type = 'mayaBinary',f = 1)
        os.remove(SceneFileNamePath)
        print (u'-------------------------角色ChOcc文件分层完成-----------------------------')
        print (u'---------')
        # 追加角色wing层 ---------------------------
        print (u'---------')
        print (u'-------------------------wing 角色文件分层开始-----------------------------')
        # 以下角色需要单独加翅膀层
        wingCharacters13 = ['c006001Triana','c008001LadySirona','c030001BloomFairyRose','c031001BloomFairyLily','c004001Avalanne','c007001Brigida','c011001Bree','c011002BreewithComicalHairdo','c011002BreewithComicalHairdo','c026001Clarissa','c027001Rochelle','c029001GenericPixie02','c028001GenericPixie01']
        SceneFileNamePath = baseFileNamePath.replace('_an_', '_l2wing_lr_')
        SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_ChrBase', 'c001')
        shutil.copy(baseFileNamePath, SceneFileNamePath)
        print (u'====成功保存分层文件%s'%SceneFileNamePath)
        # 开文件建层
        # mc.file(SceneFileNamePath,open = 1 , f = 1)
        # 修改为先打开壳文件，再导入动画文件
        mc.file(RenderShellV001,open = 1 , f = 1)
        mc.file(SceneFileNamePath,i = 1, f = 1)
        mc.file(rename = SceneFileNamePath)
        # 设置摄像机渲染属性
        self.CJW_settingCameraAttr(shotInfo)
        ChrAndProps = []
        refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        XX = 0
        for TheNamespace in refNamespaces:
            if 'tf_' not in TheNamespace or 'c009001' in TheNamespace or 'c013001' in TheNamespace or 'c014001' in TheNamespace or 'c019001' in TheNamespace or 'c020001' in TheNamespace or 'c022001' in TheNamespace or 'c023001' in TheNamespace or 'c021001' in TheNamespace:
                continue
            for wingCharacter in wingCharacters13:
                if wingCharacter in TheNamespace:
                    XX = 1
            if XX==1 and TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
            if XX==1 and TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MODEL'):
                needMeshFull = mc.ls((TheNamespace + ':MODEL'), l=1)
                if needMeshFull not in ChrAndProps:
                    ChrAndProps.append(needMeshFull)
        if ChrAndProps:
            ChrAndPropsClean = TF_renderTools.TF_renderToolsClass().TF_switchGroup(ChrAndProps)
        if XX ==1:
            mc.select(cl=1)
            mc.select(ChrAndPropsClean,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderColorLayer(layer='ChrWingColor')
            print (u'====渲染层ChrColor完成===')
            mc.select(cl=1)
            mc.select(ChrAndPropsClean,r=1)
            TF_renderTools.TF_renderToolsClass().TF_RenderOCCLayer(layer='ChrWingOCC',transparency=0)
            print (u'====渲染层ChrOCC完成===')
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
            self.CJW_chrRenderSettings(type=0)
            # 尝试隐藏动画文件里的物体
            for hideObjShape in AllHideObjShapes:
                try:
                    mc.setAttr(hideObjShape+'.visibility',0)
                except:
                    pass
            # 转存mb文件，删除ma文件
            mc.file(save=1,type = 'mayaBinary',f = 1)
            os.remove(SceneFileNamePath)
            print (u'-------------------------wing 角色文件分层完成-----------------------------')
        else:
            os.remove(SceneFileNamePath)
            print (u'====无wing类角色，删除wing分层文件====%s')
        print (u'---------')
        # 角色、场景、道具。conSHD 接触阴影层。 conOcc 接触occ层。
        # 这两个场景移出建层文件 'l014001' 'l021001'
        print (u'---------')
        print (u'-------------------------角色场景接触阴影和Occ接触层开始-----------------------------')
        if not ServerInfoData[3] == '':
            SceneFileNamePath = baseFileNamePath.replace('_an_', '_l2con_lr_')
            SceneFileNamePath = SceneFileNamePath.replace(shotInfo[5].split('.')[0]+'_ChrBase', 'c001')
            shutil.copy(baseFileNamePath, SceneFileNamePath)
            print (u'====成功保存分层文件%s'%SceneFileNamePath)
            # 把所有参考再全转成_ms_anim文件,后改为专成l1idp文件
            if not ServerInfoData[3] == '':
                oldName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms_l1rg.mb'
                newName = 'MasterLighting/tf_'+ServerInfoData[3]+'_h_ms_l1idp.mb'
                checkFileExists = '//file-cluster/GDC/Projects/ToothFairies/Project/scenes/locations/'+ ServerInfoData[3]+'/'+ newName
                if os.path.exists(checkFileExists):
                    self.TF_SwitchReferencePath(SceneFileNamePath,oldName,newName)
                    print (u'====成功修改文件场景参考成MasterLighting路径下的====%s'%checkFileExists)
                else:
                    print (u'====请检查此镜头的场景，无发现l1idp文件====%s'%checkFileExists)
            else:
                print (u'====此镜头无场景文件====%s'%ThisFileName)
            # 继续把场景内角色道具render参考转成anim参考
            self.TF_SwitchReferencePath(SceneFileNamePath, '_ms_render.mb','_ms_anim.mb')
            # 开文件,
            # mc.file(SceneFileNamePath,open = 1 , f = 1)
            # 修改为先打开壳文件，再导入动画文件
            mc.file(RenderShellV01,open = 1 , f = 1)
            mc.file(SceneFileNamePath,i = 1, f = 1)
            mc.file(rename = SceneFileNamePath)
            # 设置摄像机渲染属性
            self.CJW_settingCameraAttr(shotInfo)
            # 通过参考得到角色场景信息
            CHRAllShapes = []
            SETAllShapes = []
            PRPAllShapes = []
            refNamespaces = mc.namespaceInfo(listOnlyNamespaces=1)
            for TheNamespace in refNamespaces:
                if 'tf_' not in TheNamespace:
                    continue
                #for noRenderChr in noRenderCharacters:
                #    if noRenderChr in TheNamespace:
                #        continue
                if TheNamespace.split('_')[1][0] in ['c'] and mc.objExists(TheNamespace + ':MODEL'):
                    needMeshFulls = mc.ls((TheNamespace + ':MODEL'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in CHRAllShapes:
                        CHRAllShapes.append(taskAllShapes2)
                if TheNamespace.split('_')[1][0] in ['l'] and mc.objExists(TheNamespace + ':MODEL'):
                    needMeshFulls = mc.ls((TheNamespace + ':MODEL'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in SETAllShapes:
                        SETAllShapes.append(taskAllShapes2)
                if TheNamespace.split('_')[1][0] in ['p'] and mc.objExists(TheNamespace + ':MODEL'):
                    needMeshFulls = mc.ls((TheNamespace + ':MODEL'), l=1)
                    taskAllShapes = TF_renderTools.TF_renderToolsClass().TF_CleanNoIntermediateShapeNodes(needMeshFulls)
                    taskAllShapes2 = TF_renderTools.TF_renderToolsClass().TF_switchGroup(taskAllShapes)
                    if taskAllShapes2 not in PRPAllShapes:
                        PRPAllShapes.append(taskAllShapes2)
            # 清理大组为['a','b','c']形式
            CHRAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(CHRAllShapes)
            SETAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(SETAllShapes)
            PRPAllShapesClear = TF_renderTools.TF_renderToolsClass().TF_switchGroup(PRPAllShapes)
            # 导入所有参考
            sk_referenceConfig.sk_referenceConfig().checkRefAllImport()
            # 清理无用节点,删除其他层，自建材质球删除所有材质球。
            self.CJW_ClearUnusedNode(deleteLayer=1, cleanType=1)
            mel.eval('zwResetShadingEnginesN')
            # 再次保存此ma文件
            # mc.file(save=1,type = 'mayaAscii',f = 1)
            # 以文本清理插件
            # self.CJW_CleanUselesNodes(SceneFileNamePath)
            # 再次打开此文件,预计应该比较快了
            # mc.file(SceneFileNamePath,open = 1 , f = 1)
            if 'l014001' not in ServerInfoData[3] and 'l021001' not in ServerInfoData[3] and 'l004001' not in ServerInfoData[3]:
                print (u'------开始建立阴影材质球------')
                # 创建材质球，添加所有模型shape
                materialsNodes =mc.ls(mat=1)
                shaderNode = 'conShadow_shader'
                if shaderNode not in materialsNodes:
                    shadowShader = mc.shadingNode('useBackground', asShader=1, name = shaderNode)
                    mc.setAttr(shadowShader+'.specularColor', 0, 0, 0, type='double3')
                    mc.setAttr(shadowShader+'.reflectivity', 0)
                    mc.setAttr(shadowShader+'.reflectionLimit', 0)
                    shadowShaderSG = mc.sets(renderable =1, noSurfaceShader =1, empty=1, name =(shadowShader+'SG'))
                    mc.connectAttr((shadowShader +'.outColor'),(shadowShaderSG +'.surfaceShader'),f=1)
                else:
                    shadowShader = shaderNode
                    shadowShaderSG = shadowShader+'SG'
                # 创建渲染层
                AllRenderLayers = mc.listConnections('renderLayerManager.renderLayerId')
                for item in AllRenderLayers:
                    if item in "*:*defaultRenderLayer*" or item in "*defaultRenderLayer*":
                        mc.setAttr(item+'.renderable', 0)
                conSHDrenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='conSHD')
                mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
                # 设置渲染属性
                TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
                # 把物体加入渲染层
                mc.editRenderLayerMembers(conSHDrenderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
                # 物体添加材质球
                AA = CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear
                for aa in AA:
                    mc.sets(aa,e=1, forceElement = shadowShaderSG)
                # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
                ChrAndProps = CHRAllShapesClear+PRPAllShapesClear
                for shape in ChrAndProps:
                    mc.setAttr(shape+'.primaryVisibility', 0)
                # 场景物体关闭投射属性 setAttr "pSphereShape1.castsShadows" 0;
                for shape in SETAllShapesClear:
                    mc.setAttr(shape+'.castsShadows', 0)
                # 添加场景主灯
                FuckingLights = mc.ls(type = 'light')
                for FuckingLight in FuckingLights:
                    if '*:'+keyLight or keyLight:
                        if keyLight in FuckingLight or '*:'+keyLight in FuckingLight:
                            mc.editRenderLayerMembers(conSHDrenderLayer,FuckingLight, noRecurse=0)
                            print (u'====成功添加阴影主灯====')
                    else:
                        print (u'====注意！！！无发现阴影层主灯====')
                print (u'====渲染层%s完成==='%conSHDrenderLayer)
            else:
                print (u'====此镜头文件场景为l014001,l021001,l004001号场景，无需做阴影层====')
            ## =======================================创建conOcc接触occ层========================================== ##
            # 创建材质球
            materialsNodes =mc.ls(mat=1)
            shaderName = 'conOCC_shader'
            OCCTextureName = 'conOCC_texture'
            if (mc.pluginInfo('Mayatomr.mll',query=1,loaded=1) == False):
                mc.loadPlugin('Mayatomr.mll')
            if shaderName not in materialsNodes:
                OCCTexture = mc.shadingNode('mib_amb_occlusion',asTexture=1,name = OCCTextureName)
                mc.setAttr(OCCTexture+'.samples',136)
                mc.setAttr(OCCTexture+'.spread',0.8)
                mc.setAttr(OCCTexture+'.max_distance',2)
                mc.setAttr(OCCTexture+'.output_mode',0)
                mc.setAttr(OCCTexture+'.falloff',1)
                mc.setAttr(OCCTexture+'.id_inclexcl',0)
                mc.setAttr(OCCTexture+'.id_nonself',1)
                OCCShader = mc.shadingNode('surfaceShader',asShader=1,name = shaderName)
                mc.connectAttr((OCCTexture +'.outValue'),(OCCShader +'.outColor'),f=1)
                OCCShaderSG = mc.sets(renderable =1,noSurfaceShader =1,empty=1,name =(OCCShader+'SG'))
                mc.connectAttr((OCCShader +'.outColor'),(OCCShaderSG +'.surfaceShader'),f=1)
            else:
                OCCShader = shaderName
                OCCShaderSG = OCCShader+'SG'
                OCCTexture = OCCTextureName
            # 创建渲染层
            conOccrenderLayer = mc.createRenderLayer(noRecurse=1, makeCurrent=1, name='conOcc')
            mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
            # 设置渲染属性
            TF_renderTools.TF_renderToolsClass().CJW_setRenderSetting(renderUsing='mentalRay',type=1, imageFormatValue='iff')
            # 把所有物体加入渲染层
            mc.editRenderLayerMembers(conOccrenderLayer, CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear, noRecurse=0)
            # 物体添加材质球
            AA = CHRAllShapesClear+SETAllShapesClear+PRPAllShapesClear
            for aa in AA:
                mc.sets(aa,e=1, forceElement = OCCShaderSG)
            # 关闭角色道具shape节点的pSphereShape1.primaryVisibility渲染属性
            ChrAndProps = CHRAllShapesClear+PRPAllShapesClear
            for shape in ChrAndProps:
                mc.setAttr(shape+'.primaryVisibility', 0)
            # 场景物体添加miLabel属性
            for SETAllShape in SETAllShapesClear:
                transform = mc.listRelatives(SETAllShape, p=1, f=1, type='transform')[0]
                if not mc.objExists(transform+'.miLabel'):
                    mc.addAttr(transform, shortName='miLabel',longName='miLabel',defaultValue=1.0, minValue=0.0, maxValue=1.0, attributeType='double',k=1)
            sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)
            self.CJW_chrRenderSettings(type=1)
            # 尝试隐藏动画文件里的物体
            for hideObjShape in AllHideObjShapes:
                try:
                    mc.setAttr(hideObjShape+'.visibility',0)
                except:
                    pass
            # 转存mb文件
            mc.file(save=1,type = 'mayaBinary',f = 1)
            # 删除之前ma文件
            os.remove(SceneFileNamePath)
            print (u'---------')
            print (u'-------------------------角色场景接触阴影和Occ接触层完成-----------------------------')
            print (u'---------')
        else:
            print (u'====此镜头文件无表格内场景，无需做阴影层和接触层===%s'%ThisFileName)

    # 扫描Moderl组下隐藏物体
    # 返回mesh节点
    def CJW_checkHideObj(self):
        transNodes = mc.ls(type = 'transform',l=1)
        hideObjs = []
        for checkNode in transNodes:
            inr = mc.referenceQuery(checkNode,inr=1)
            if not inr:
                continue
            if ':%s|'%(sk_infoConfig.sk_infoConfig().renderGrp) not in checkNode:
                continue
            if not mc.getAttr(checkNode+'.v'):
                hideObjs.append(checkNode)
        # 加入layer显示层的判断
        layerNames = ['norender','noRender','NoRender','NORENDER']
        for layerName in layerNames:
            try:
                noRenderLayerObjs = mc.editDisplayLayerMembers(layerName, query=True,fullNames=1)
                if noRenderLayerObjs:
                    for noRenderLayerObj in noRenderLayerObjs:
                        if noRenderLayerObj not in hideObjs:
                            hideObjs.append(noRenderLayerObj)
            except:
                pass
        # 扫描下面正确的shape节点
        AllHideObjShapes = []
        for hideObj in hideObjs:
            hideObjShapes = mc.listRelatives(hideObj, ad=1, f=1, type='mesh')
            if hideObjShapes:
                for hideObjShape in hideObjShapes:
                    hideObjTransform = mc.listRelatives(hideObjShape, p=1, f=1, type='transform')[0]
                    try:
                        hideObjNoIntermediateShape = mc.listRelatives(hideObjTransform, s=1, f=1, ni=1, type='mesh')[0]
                        if hideObjNoIntermediateShape not in AllHideObjShapes:
                            AllHideObjShapes.append(hideObjNoIntermediateShape)
                    except:
                        pass
        return AllHideObjShapes

    '''
    创建渲染层 mc.createRenderLayer(noRecurse=1, makeCurrent=1, name=renderlayer)1
    加入渲染层 mc.editRenderLayerMembers(renderlayer, ChrModelMeshs, noRecurse=0)
    移出渲染层 mc.editRenderLayerMembers(renderlayer, ChrModelMesh, noRecurse=0, remove=1)
    所有渲染层 mc.listConnections('renderLayerManager.renderLayerId')
    选择渲染层 mc.editRenderLayerGlobals(currentRenderLayer = 'layer1')
    属性覆盖渲染层 mc.editRenderLayerAdjustment('defaultRenderGlobals.currentRenderer')
    删除渲染层 mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer') 先回到默认层
               mc.delete('layer1') 再删除指定层
    刷新渲染面板 mel.eval('changeMentalRayImageFormat')格式属性
    导入参考后要再清理一遍废插件，参考文件里有插件

    from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
    reload(sk_smoothSet)
    sk_smoothSet.sk_smoothSet().smoothSetDoSmooth(disModify = 0)

    文件改名字后，才能保存，
    读取文件名 ThisFileNamePath = mc.file(query=1, exn=1)

    mc.file(rename = baseFileName)
    mc.file(save = 1 , f = 1)
    '''

    # norender信息导出
    def checkNorenderInfoExport(self,nrObjs):
        key = 'norender'
        localPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(0,1)
        serverPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(1,1)
        serverPath = serverPath.replace('EyeLight',key)
        fileInfo = 'norender.txt'
        sk_infoConfig.sk_infoConfig().checkFileWrite((localPath + fileInfo),nrObjs)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath + fileInfo) + '"' + ' ' + '"' + (serverPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
