# -*- coding: utf-8 -*-

# import sys
# sys.path.append('D:\\food\pyp\common')

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式
# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)

class sk_sceneTools(object):
    def __init__(self):
        # namespace清理
        pass

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 【camera工具集】
    # ------------------------------#
    def sk_sceneUICameraTools(self):
        # 窗口
        if mc.window("sk_sceneUICameraTools", ex=1):
            mc.deleteUI("sk_sceneUICameraTools", window=True)
        mc.window("sk_sceneUICameraTools", title="Camera Tools", widthHeight=(150, 170), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        # 文件asset
        mc.button(w=150, h=30, bgc=[0.1, 0.1, 0.1], label=(unicode('【动画】打开文件系统', 'utf8')),
                  c='mel.eval(\"zwAssetFile\")')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        # 我的规则是，import了scene类，于是这里可以直接用起来
        mc.button(w=150, h=30, bgc=[0, 0.5, 1], label=(unicode('【动画】导入音频及相机', 'utf8')),
                  c='reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().sk_sceneImportCameraAudioFrame()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=(unicode('【动画】导出最终相机', 'utf8')),
                  c='reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate()')
        mc.setParent("..")
        # newCmd = r"zwSysFile  \"copy\" \"" + camTempPath + r"\" \"" + camServerPath + r"\" 1"

        mc.rowLayout()
        # mc.button(w=150 , h=30 , bgc=[0, 0.5, 1], label=(unicode('【通用】参考最终相机', 'utf8'))  , c='mel.eval(\'source zwCameraImportExport.mel; zwGetCameraUI;\')')
        mc.button(w=150, h=30, bgc=[0, 1, 0.2], label=(unicode('【通用】参考最终相机', 'utf8')),
                  c='from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam;reload(sk_hbExportCam);sk_hbExportCam.sk_hbExportCam().camServerReference()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.7, 0.2], label=(unicode('【动画】导出abc相机', 'utf8')),
                  c='reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().LY_CameraABC()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0, 0.55, 0.15], label=u'【AN】激活视窗再拍屏' ,
                  c='reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().ste3CamPlayblast(mode="an")')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0, 0.55, 0.15], label=u'【FS】激活视窗再拍屏' ,
                  c='reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().ste3CamPlayblast(mode="fs")')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.6, 0.15], label=u'【动画】前台批量拍屏',
                  c='from idmt.maya.commonPerform.projectTools import sk_multiPlayblast;reload(sk_multiPlayblast);sk_multiPlayblast.sk_multiPlayblast().sk_multiPlayblastUI()')
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow("sk_sceneUICameraTools")

    # ------------------------------#
    # 立体相机拍屏
    # ------------------------------#
    def ste3CamPlayblast(self,bgColors = [],mode = 'an'):
        fileName = mc.file(q=1,exn=1).split('/')[-1]
        # sl,sa 1 | sd fs 2
        playBlastState = 1
        if '_sd_' in fileName:
            playBlastState = 2
        if '_fs_' in fileName:
            playBlastState = 2
        import os
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        shotID = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfo[3])
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        localPath = '%s%s/'%(localPath,shotID.replace('_','/'))
        if not os.path.exists(localPath):
            mc.sysFile(localPath,makeDir=1)
        camSourceName = shotID.replace(shotInfo[0],'cam')
        needCamList = []
        #导入相机
        #if playBlastState == 2:
        #    self.shotRefCamImport()
        if mode in ['an']:
            camList = mc.ls('*%s*'%camSourceName,type = 'camera',l=1)
        if mode in ['fs']:
            camList = mc.ls('*:*%s*'%camSourceName,type = 'camera',l=1)
        for cam in camList:
            camGrp = mc.listRelatives(cam,p=1,type = 'transform',f=1)[0]
            needCamList.append(camGrp)
        # 配置
        mc.optionVar(intValue = ('playblastViewe',0))
        mc.optionVar(intValue = ('playblastViewerOn',0))
        mc.optionVar(intValue = ('playblastMultiCamera',1))
        mc.optionVar(stringValue = ('playblastFormat','avi'))
        mc.optionVar(stringValue= ('playblastCompression','PVMJPG40'))
        mc.optionVar(intValue = ('playblastSaveToFile',1))
        mc.optionVar(floatValue = ('playblastScale',0.5))
        # 关系所有layer
        disLayers = mc.ls('near',type = 'displayLayer')
        disLayers += mc.ls('mid',type = 'displayLayer')
        disLayers += mc.ls('far',type = 'displayLayer')
        for checkLayer in disLayers:
            mc.setAttr('%s.v'%checkLayer,0)
        camKeyList = sk_infoConfig.sk_infoConfig().checkReadShotCamData()
        # 拍屏 背景色 换改立体背景色模式
        #if bgColors:
        #    mc.displayRGBColor('background',bgColors[0],bgColors[1],bgColors[2])
        # 拍屏
        oldFileList = []
        for needCam in needCamList:
            needLayer = needCam.split('_')[-1]
            if mode in ['fs']:
                camKey = needCam.split(':')[-1].replace('cam',shotInfo[0])
            if mode in ['an']:
                camKey = needCam.split('|')[-1].replace('cam',shotInfo[0])
            movFile = '%s%s'%(localPath,camKey)
            mc.optionVar(stringValue = ('playblastFile',movFile))
            for info in ['left','right']:
                oldFile = '%s_%s.avi'%(movFile,info)
                if not os.path.exists(oldFile):
                    continue
                os.remove(oldFile)
            oldFile = '%s.avi'%(movFile)
            if os.path.exists(oldFile):
                os.remove(oldFile)
            editor = mel.eval('playblast -ae')
            panel = mc.editor(editor, q = True, panel = True)
            mel.eval('stereoCameraSwitchToCamera %s %s'%(needCam, panel))
            # 背景色去掉
            if bgColors:
                #mc.stereoCameraView( editor, edit=True,useCustomBackground = 0 )
                mc.stereoCameraView( editor, edit=True,viewColor= [bgColors[0],bgColors[1],bgColors[2],1],useCustomBackground = True )
            # 清理显示
            mc.modelEditor(editor,e=1,allObjects = 0)
            mc.modelEditor(editor,e=1,polymeshes = 1)
            mc.modelEditor(editor,e=1,pluginShapes = 1)
            mc.modelEditor(editor,e=1,strokes = 1)
            mel.eval('modelEditor -e -pluginObjects gpuCacheDisplayFilter true %s;'%editor)
            mel.eval('modelEditor -e -displayAppearance "smoothShaded" -displayTextures off -displayLights "default" %s;'%editor)
            # 开启layer
            if camKeyList:
                mc.setAttr('%s.v'%needLayer,1)
            mel.eval('performPlayblast 8001')
            # 背景色恢复
            if bgColors:
                #mc.stereoCameraView( editor, edit=True,useCustomBackground = 1 )
                mc.stereoCameraView( editor, edit=True,viewColor= [0,0,0,1],useCustomBackground = True )
            # 关闭layer
            if camKeyList:
                mc.setAttr('%s.v'%needLayer,0)
            # 改名
            for info in ['left','right']:
                oldFile = '%s.avi_%s.avi'%(movFile,info)
                if not os.path.exists(oldFile):
                    continue
                if oldFile in oldFileList:
                    continue
                oldFileList.append(oldFile)
        # 删相机
        #if bgColors:
        #    mc.displayRGBColor('background',0.651,0.651,0.651)
        if playBlastState in [2]:
            mc.delete(needCamList)
        for checkLayer in disLayers:
            mc.setAttr('%s.v'%checkLayer,1)
        for oldFile in oldFileList:
            newFile = oldFile.replace('.avi_','_')
            if os.path.exists(newFile):
                os.remove(newFile)
            os.rename(oldFile,newFile)
        print '------------outPut'
        print bgColors
        print needCamList
        print localPath

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 【Camera Bake及Update】
    # ------------------------------#
    # camera导出更新
    # info 2 为 cl_xxx_xxx模式 | 3 为 yd_xxx_xxx_xxx模式
    def sk_sceneCameraUpdate(self, batchUpadate=0, shotType=0,abcToggle=0,testMode = 0):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        # 顺溜临时处理
        if shotType == 3:
            shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        proStartFrame = int(anim.frmStart)

        # 清理unknown节点
        if batchUpadate:
            self.checkDonotNodeCleanBase(0)
        camFileTestKey = shotInfo[1] + '_' + shotInfo[2]
        # 本地临时目录
        camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + \
                      shotInfo[1] + "/" + 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked.ma'
        # serve目录
        camServerBasePath = "//file-cluster/GDC/Projects/" + projectInfo + "/Project/scenes/Animation/episode_" + \
                            shotInfo[1] + "/episode_camera/"
        # 需要创建目录
        # 更新server文件路径
        camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.ma'
        if shotType == 3:
            camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + \
                          shotInfo[1] + "/" + 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_baked.ma'
            camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[
                3] + '_cam.ma'
            camFileTestKey = shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        mc.sysFile(camTempPath, makeDir=True)
        # 先删除cam参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            if camServerPath in refPaths:
                id = refPaths.index(camServerPath)
                refNode = refNodes[id]
                if batchUpadate:
                    mc.file(rfn=refNode, removeReference=1)
        # 立体模式
        import sk_pyCommon
        reload(sk_pyCommon)
        # baked camera
        stereoState = sk_infoConfig.sk_infoConfig().checkStereoProj()
        # 获取相机
        needCamList = self.sk_getProjNeedCamera(shotInfo,shotType)
        print '------u'
        print needCamList
        import os
        for needCam in needCamList:
            # 修正pivot
            mc.xform(needCam,rp=[0,0,0])
            mc.xform(needCam,sp=[0,0,0])
            # 检测相机模式
            camShapes = mc.listRelatives(needCam,s=1,f=1)
            stereoStateCheck = 0
            tempType = mc.nodeType(camShapes[0])
            print tempType
            if stereoState and 'stereo' not in tempType:
                stereoStateCheck = 1
            if not stereoState and 'stereo' in tempType:
                stereoStateCheck = 1
            if stereoStateCheck:
                print u'---[Cam Type Error]Cam类型不对,请检查是否立体项目---'
                print u'---[Cam Type Error]或者查询是否有多的非法相机---'
                mc.error()
            # camBakeName = camSourceName + '_baked'
            camBakeName = needCam.split('|')[-1] + '_baked'
            camSelect = 0
            shotInfos = shotInfo
            # calimero camera
            if shotInfo[0] == 'cl':
                # 清理CAMERAnamespace
                if mc.ls('CAMERA:*'):
                    sk_pyCommon.sk_pyCommon().sk_deleteNamespace('CAMERA')
                camBakeName = 'grp' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '|CAMERA'
                camSelect = 1
                shotInfos = [str(shotInfo[1]), str(shotInfo[2]), str(shotInfo[0])]
            # bakeCame
            if mc.ls(camBakeName):
                mc.delete(camBakeName)
            if needCam:
                mc.select(needCam)
            else:
                print(u'=============找不到对应镜头的CAM=============')
                mc.error(u'=============找不到对应镜头的CAM=============')
            #mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
            #mel.eval('zwBakeCamera')
            from idmt.maya.commonCore.core_finalLayout import sk_bkCore
            reload(sk_bkCore)
            sk_bkCore.sk_bkCore().sk_sceneCameraBK(stereoMode = stereoState,shotInfos = shotInfo,bkCam = needCam)
            mc.lockNode("defaultRenderGlobals", lock = 0)
            mc.select(camBakeName)
            print '-------needCam'
            print camBakeName
            print shotInfos
            if testMode in [0.1]:
                return
            # 相机Export
            import sk_hbExportCam
            reload(sk_hbExportCam)
            exportPath = sk_hbExportCam.sk_hbExportCam().HbExceptSelectReCam(projectInfo = projectInfo, all = 0,
                scrFrame = str(proStartFrame),batchUpadate = batchUpadate, camSelect = camSelect, shotInfo = shotInfos)
            # 输出相机
            print '--------exportCamPath'
            print exportPath
            if testMode in [0.2]:
                return
            needInfo = exportPath[0].split('/')[-1]
            if '_baked' in needInfo:
                needInfo = needInfo.replace('_baked', '_cam')
            needInfo = needInfo.split(camFileTestKey)[-1]
            resultServerPath = '%s%s' % (camServerBasePath, '%s_%s%s' % (shotInfo[0], camFileTestKey, needInfo))
            camDataPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 11,shotInfos = shotInfo)
            if not os.path.exists(camDataPath):
                #os.makedirs(ThePath)
                mc.sysFile(camDataPath,makeDir = 1)
            print resultServerPath
            mel.eval('zwSysFile \"copy\" \"' + exportPath[0] + '\" \"' + resultServerPath + '\" 1')
            mel.eval('zwSysFile \"copy\" \"' + exportPath[0] + '\" \"' + '%s%s'%(camDataPath,needInfo) + '\" 1')
            if testMode in [0.3]:
                return
            print u'====================成功更新camera到服务器端===================='
            #========add by zhangben 20160603   export camera abc cache 2 server ==============================
            if abcToggle:
                import Other.minitiger.mi_pipelineProcs as mpplp;reload(mpplp)
                ins_mpplp = mpplp.mi_pipelineProcs()
                cam_abc_gener_path = exportPath[0].replace(u'.ma',u'.abc')
                cam_abc_exp2 = u'%s%s_%s%s'%(camServerBasePath,shotInfo[0],camFileTestKey,needInfo.replace(u'.ma',u'.abc'))
                ins_mpplp.mi_export_camAbc2Server(camBakeName,cam_abc_gener_path)
                mel.eval('zwSysFile \"copy\" \"' + cam_abc_gener_path + '\" \"' + cam_abc_exp2 + '\" 1')
                print u'================ copied camera abc file  2 server ============================'
            # 删除bake后的相机
            mc.delete(camBakeName)
            mc.select(cl=1)

        # 成功代码
        return 0

    # test
    def testDef(self,num):
        print '-----test_%s'%(str(num))

    # 获取项目需要的camera
    def sk_getProjNeedCamera(self,shotInfo = [],shotType = 0):
        if not shotInfo:
            shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 检查bake相机
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        # 顺溜临时处理
        print '=' * 20 + str(shotType)
        if shotType == 3:
            camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3])
            # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
        # 增加fs之后环节处理
        refState = 0
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        for infoKey in ['_fs_','_dy_','_sd_','_lr_']:
            if infoKey in fileName:
                refState = 1
        if refState:
            camSourceName = 'CAM:%s_baked'%camSourceName
        print '----------CamSource'
        print camSourceName
        needCamList = []
        camList = []
        tempList = mc.ls('*%s*' % camSourceName, type='transform', l=1)
        for checkGrp in tempList:
            shapeList = mc.listRelatives(checkGrp,s=1,type = 'camera',f=1)
            if not shapeList:
                continue
            camList = camList + shapeList
        # mi专用
        extraKeyList = ['near', 'mid', 'far']
        if camList:
            for cam in camList:
                camGrp = mc.listRelatives(cam, p=1, type='transform', f=1)[0]
                if camGrp.split('|')[-1] != camSourceName:
                    if shotInfo[0] in sk_infoConfig.sk_infoConfig().camNMFProjList:
                        for extraKey in extraKeyList:
                            newCamGrp = '%s_%s' % (camSourceName, extraKey)
                            if camGrp.split('|')[-1] == newCamGrp:
                                needCamList.append(camGrp)
                else:
                    needCamList.append(camGrp)
                if cam.split('|')[-1] == camGrp.split('|')[-1]:
                    mc.rename(cam, (cam + 'Shape'))
            if not needCamList:
                print u'=============找不到对应镜头的CAM============='
                mc.error(u'=============找不到对应镜头的CAM=============')
        else:
            print u'=============正确相机命名应该是【%s】,请检查camera名字及shape节点==============' % camSourceName
            mc.error(u'=============找不到对应镜头的CAM=============')
        '''
        # 传统单相机获取
        camList = mc.ls(camSourceName,l=1)
        needCam = ''
        if camList:
            for cam in camList:
                if mc.listRelatives(cam,s=1,ni=1,type = 'camera'):
                    needCam = cam
                if mc.nodeType(cam) == 'camera':
                    mc.rename(mc.ls(cam,l=1)[0],(cam+'Shape'))
        else:
            print(u'=============找不到对应镜头的CAM=============')
            mc.error(u'=============找不到对应镜头的CAM=============')
        '''
        # 无near,mid,far的检测
        if len(needCamList) > 1:
            steoState = 0
            for checkCam in needCamList:
                for checkKey in extraKeyList:
                    if checkKey in checkCam.split('|')[-1]:
                        steoState = 1
            if not steoState:
                errorInfo = u'------本文件不应该有多个相机,请处理掉不需要的相机------'
                print '\n' + errorInfo
                for checkCam in needCamList:
                    print checkCam
                print errorInfo + '\n'
                mc.error()
        return needCamList

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # camera 检测/修正 缩放参数
    # ------------------------------#
    def sk_sceneCameraScaleCheck(self,fixMode = 0):
        allCamGrps = self.sk_getProjNeedCamera()
        attrList = ['sx','sy','sz']
        errorList = []
        minValue = 0.0001
        for checkCam in allCamGrps:
            camInfos = []
            for checkAttr in attrList:
                checkValue = mc.getAttr('%s.%s'%(checkCam,checkAttr))
                if fixMode:
                    self.sk_sceneCameraScaleFix(checkCam,checkAttr)
                    continue
                if (checkValue - 1.0) < minValue:
                    continue
                if not camInfos:
                    camInfos += [checkCam,'[%s]:%s'%(checkAttr,checkValue)]
                else:
                    camInfos += ['----------------',checkCam,'[%s]:%s'%(checkAttr,checkValue)]
            errorList += camInfos
        if not fixMode and errorList:
            for info in errorList:
                print info
            errorInfo = u'------请处理以上缩放值------\n------上面的值哪怕"显示"是1.0也请手动打1\n'
            print errorInfo
            mc.error()

    # 修正camera scale
    def sk_sceneCameraScaleFix(self,cam,attr):
        checkAttr = '%s.%s'%(cam,attr)
        # 连接
        cons = mc.listConnections(checkAttr,s=1,d=0,plugs = 1)
        # 锁
        if mc.getAttr(checkAttr,l=1):
            mc.setAttr(checkAttr,l=0)
        if cons:
            mc.disconnectAttr(cons[0],checkAttr)
        # 参考
        inr = mc.referenceQuery(cam,inr = 1)
        if inr:
            errorInfo = u'%s\n这是参考相机,不该出现在镜头文件里，请处理'%cam
            print errorInfo
            mc.error()
        # 处理
        mc.setAttr(checkAttr,1)

    #-----------------------------------------------------#
    # 批量参考cam
    #-------------------------#
    def sk_sceneCameraReferenceUI(self):
        # 窗口
        UIName = 'sk_ScenecamRefUI'
        width = 470
        height = 230

        leftwidth = 260

        listWidth = 150
        listHeight = 170

        defaultText = 'mi_030'

        if mc.window (UIName, ex=1):
            mc.deleteUI(UIName, window=True)
        mc.window(UIName, title="Scene Cam Reference", widthHeight=(width,height), menuBar=0)

        rowLayout = mc.rowColumnLayout(numberOfColumns=2)
        #------------#
        # 中路
        columnLayout = mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])
        # 选取
        mc.frameLayout(l = u'[ 请选取_模式 | Select Mode ]' ,collapse = 0,collapsable = 0,borderStyle = 'etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',15])
        mc.text(label = '' , height = 2)
        mc.radioButtonGrp('sk_stereoMode',numberOfRadioButtons  = 2,columnWidth2 = [120,120],labelArray2 = [u'标准模式 | Standard',u'立体项目 | Stereo'] ,select = 2)
        mc.text(label = '' , height = 2)
        mc.setParent()
        mc.setParent(columnLayout)

        mc.frameLayout(l = u'[ 请输入项目和场 | Input proj and Seq info ]' ,collapse = 0,collapsable = 0,borderStyle = 'etchedIn')
        # 项目场信息
        mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',15])
        mc.text(label = '' , height = 3)
        mc.textField('sk_camSceneInfo',text = defaultText ,width = leftwidth,height = 25)
        mc.text(label = '' , height = 2)
        mc.setParent()
        mc.setParent(columnLayout)

        # assetID
        mc.frameLayout(l = u'[ 请输入AssetID | AssetID ]' ,collapse = 0,collapsable = 0,borderStyle = 'etchedIn')
        mc.columnLayout(adjustableColumn = 0 , columnOffset = ['both',15])
        mc.text(label = '' , height = 2)
        mc.textField('sk_camAssetIDInfo',text = '',width = leftwidth,height = 25)
        mc.text(label = '' , height = 2)
        mc.setParent()
        mc.setParent(columnLayout)

        # 查询
        mc.frameLayout(l = u'[ 查询镜头列表 | Search Shot List ]' ,collapse = 0,collapsable = 0,borderStyle = 'etchedIn')
        mc.columnLayout(adjustableColumn = 0,columnOffset = ['both',15])
        mc.button(l = u'查询需要的镜头列表 | Search Shot List',bgc = [0,0,0],width = leftwidth,height = 25,
                  c = 'reload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneCameraReferenceUIButton()')
        mc.text(label = '' , height = 8)
        mc.setParent()
        mc.setParent(columnLayout)
        mc.setParent(rowLayout)

        #------------#
        # 右路
        mc.columnLayout(adjustableColumn= 1)
        mc.textScrollList('sk_assetSeqShotList',width = listWidth,height = listHeight +20,numberOfRows = 20,allowMultiSelection = 1)
        mc.button(l = u'选取导入 | Sel Import',bgc = [0.1,0.1,0.1],
                  c = 'reload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneCameraImport()')
        mc.setParent()
        mc.setParent(rowLayout)

        mc.setParent()
        mc.showWindow(UIName)

    # 连接button
    def sk_sceneCameraReferenceUIButton(self):
        # 获取数据
        shotInfos = mc.textField('sk_camSceneInfo',q = 1,text = 1)
        assetID =  mc.textField('sk_camAssetIDInfo',q = 1 , text = 1)
        if not shotInfos:
            shotInfos = []
        else:
            shotInfos = shotInfos.split('_')

        projFull = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        shotType = sk_infoConfig.sk_infoConfig().checkShotType(shotInfos[0])
        if shotType == 2:
            shotID = '_%s'%shotInfos[1]
        if shotType == 3:
            shotID = '%s_%s'%(shotInfos[1],shotInfos[2])
        needShots = []

        cmd_name = "exec idmtplex.dbo.usp_AssetFileInAnimGetByAssetNameAndAnimEpTag '%s','%s','%s'"%(shotInfos[0],assetID,shotID)
        cnxn = sk_infoConfig.sk_infoConfig().checkServerConnect(projFull)
        cursor = cnxn.cursor()
        try:
            data = cursor.execute(cmd_name).fetchall()
            if data:
                needShots = int(str(data).split('\'')[1].split('\'')[0])
        finally:
            cursor.close()
            cnxn.close()

        if not needShots:
            return

        mc.textScrollList('sk_assetSeqShotList',e=1,removeAll=1)
        for checkItem in needShots:
            mc.textScrollList('sk_assetSeqShotList',e=1,append = checkItem)

    def sk_sceneCameraImport(self):
        needShots = mc.textScrollList('sk_assetSeqShotList',q=1,selectItem=1)

        if not needShots:
            return
        shotInfos = mc.textField('sk_camSceneInfo',q = 1,text = 1)
        if not shotInfos:
            shotInfos = []
        else:
            shotInfos = shotInfos.split('_')
        fileDictInfo = sk_infoConfig.sk_infoConfig().checkGetShotDict(shotInfos)
        sceneID = fileDictInfo['sequence']
        if fileDictInfo['reel']:
            sceneID = '%s_%s'%(fileDictInfo['reel'],fileDictInfo['sequence'])
        stereoMode = mc.radioButtonGrp('sk_stereoMode',q=1,select=1) - 1
        # 执行参考
        for info in needShots:
            if not info:
                continue
            ns = '%s_%s_%s'%(fileDictInfo['showShortname'],sceneID,info)
            needShot = ns.split('_')
            camServerPath = sk_infoConfig.sk_infoConfig().checkServerCamPath(1,1,shotInfos = needShot)
            try:
                mc.file(camServerPath,r = 1,namespace = ':%s'%(ns))
            except:
                pass

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 【CAM,AUDIO】       动画用导cam及音频
    # ------------------------------#
    # 导入项目的音频及cam及帧信息
    def sk_sceneImportCameraAudioFrame(self):
        # camera
        self.sk_sceneImportCamera()
        # FPS
        self.sk_sceneImportFrame('FPS')
        # frame
        self.sk_sceneImportFrame('frame')
        # audio
        self.sk_sceneImportAudio()
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理组
        grpCList = []
        if shotInfo[0] not in grpCList:
            self.sk_sceneReorganize()

    # ------------------------------#
    # 导入项目的cam
    def sk_sceneImportCamera(self, shotType=0):
        import os
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        projectPathBase = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        camPathBase = projectPathBase.replace('/Project/',( '/' + projectFullName + '_Scratch/TD/SetCam/'))
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 开始cam部分
        camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        # 判断摄像机在不在
        if mc.ls(camName):
            # print (unicode('==============================!!!已存在相机【%s】!!!==============================' % (str(camName)), 'utf8'))
            print (u'==============================!!!已存在相机【%s】!!!==============================' % camName)
        else:
            camPath = camPathBase + shotInfo[1] + "/"
            if shotType == 2:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '.ma'
            if shotType == 3 and shotInfo[0] not in ['yd','nj','Xyj']:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '.ma'
            if shotType == 3 and shotInfo[0] in ['yd','nj','Xyj']:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_baked.ma'
            # 判断是否存在
            if os.path.exists(camPath):
                # 导入相机，清除namespace
                mc.file(camPath, i=1)
                cambake = camName + '_baked'
                mc.rename(cambake, camName)
                # print (unicode('==============================成功【导入】【%s】==============================' % (str(camName)), 'utf8'))
                print (u'==============================成功【导入】【%s】==============================' % camName)
            else:
                # 创建相机
                camTemp = mc.camera()
                mc.rename(camTemp[1], (camName + 'Shape'))
                mc.rename(camTemp[0], camName)
                # print (unicode('==============================成功【创建】【%s】==============================' % (str(camName)), 'utf8'))
                print (u'==============================成功【创建】【%s】==============================' % camName)
            # 处理安全框
            camShape = mc.listRelatives(camName, s=1)[0]
            mc.setAttr((camShape + '.displayResolution'), 1)
            mc.setAttr((camShape + '.displayGateMask'), 1)
            mc.setAttr((camShape + '.displaySafeAction'), 1)
            mc.setAttr((camShape + '.displaySafeTitle'), 0)
            # 处理其他信息
            mc.setAttr((camShape + '.nearClipPlane'), 0.1)
            mc.setAttr((camShape + '.farClipPlane'), 1000000)

    # ------------------------------#
    # ------------------------------#
    # 导入项目的cam
    def sk_sceneImportCameraF(self, shotType=0):
        import os
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        projectFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        projectPathBase = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        camPathBase = projectPathBase.replace('/Project/',('/' + projectFullName +'_Scratch/TD/SetCam/'))
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 开始cam部分
        camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        # 判断摄像机在不在
        if mc.ls(camName):
            # print (unicode('==============================!!!已存在相机【%s】!!!==============================' % (str(camName)), 'utf8'))
            print (u'==============================!!!已存在相机【%s】!!!==============================' % camName)
        else:
            camPath = camPathBase + shotInfo[1] + "/"
            if shotType == 2:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '.ma'
            if shotType == 3 and shotInfo[0] not in  ['yd','nj','Xyj']:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '.ma'
            if shotType == 3 and shotInfo[0] in ['yd','nj','Xyj']:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_baked.ma'
            # 判断是否存在
            if os.path.exists(camPath):
                # 导入相机，清除namespace
                mc.file(camPath, i=1)
                if mc.ls(camName + '_baked'):
                    cambake = camName + '_baked'
                if mc.ls(camName + '_baked') == [] and mc.ls(camName + '_baked_' + camName + '_baked'):
                    cambake = camName + '_baked_' + camName + '_baked'
                print cambake
                mc.rename(cambake, camName)
                # print (unicode('==============================成功【导入】【%s】==============================' % (str(camName)), 'utf8'))
                print (u'==============================成功【导入】【%s】==============================' % camName)
            else:
                mc.warning(u'====================文件中缺少正确相机【%s】，请检查文件==================' % camName)
                # print (unicode('==============================成功【创建】【%s】==============================' % (str(camName)), 'utf8'))
                mc.error(u'====================文件中缺少正确相机【%s】，请检查文件==================' % camName)
            # 处理安全框
            camShape = mc.listRelatives(camName, s=1)[0]
            mc.setAttr((camShape + '.displayResolution'), 1)
            mc.setAttr((camShape + '.displayGateMask'), 1)
            mc.setAttr((camShape + '.displaySafeAction'), 1)
            mc.setAttr((camShape + '.displaySafeTitle'), 0)
            # 处理其他信息
            mc.setAttr((camShape + '.nearClipPlane'), 0.1)
            mc.setAttr((camShape + '.farClipPlane'), 1000000)

    # 导入Audio
    def sk_sceneImportAudio(self):
        import os
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 处理清单
        audioIList = []
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        projectPathBase = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        audioPathBase = projectPathBase.replace('/Project/','/Reference/') + 'Animation_production/' + audioProjectInfos + '/'
        # 开始audio部分
        audios = mc.ls(type='audio')
        if audios:
            mc.delete(audios)
        audioPath = audioPathBase + str(shotInfo[1]) + '/Audio files/wav/'
        audioPath += shotInfo[2] + '.wav'
        if shotType == 3:
            audioPath += shotInfo[2]+'_'+shotInfo[3]+'.wav'
        print '-----------audioPath'
        print audioPath
        # 判断是否存在
        if os.path.exists(audioPath):
            # 导入audio
            cmd = "doSoundImportArgList (\"1\",{\"" + audioPath + "\",\"0\"});"
            mel.eval(cmd)
            # 处理Offset
            audios = mc.ls(type='audio')
            offsetFrame = mc.playbackOptions(min=1, q=1)
            mc.setAttr((audios[0] + '.offset'), offsetFrame)
            # print (unicode('==============================【成功】本镜头【音频】【导入】==============================', 'utf8'))
            print (u'==============================【成功】本镜头【音频】【导入】==============================')
        else:
            # mc.warning(unicode('==============================【！！！错误！！！】本镜头【音频】不存在==============================', 'utf8'))
            mc.warning(u'==============================【！！！错误！！！】本镜头【音频】不存在==============================')

    # ------------------------------#
    # 导入起始|结束帧
    def sk_sceneImportFrame(self, configType='FPS', shotType=0,pre = 10 , checkMode = 0,returnMode = 0):
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        errorList = []
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        # 命令
        shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            shot = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
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
        ratio = resW / (resH + float('.0'))
        mc.setAttr(('defaultResolution.deviceAspectRatio'), ratio)
        mc.evalDeferred('import maya.cmds as mc\nmc.setAttr((\'defaultResolution.pixelAspect\'),1)', lowestPriority=1)
        # FPS
        if configType == 'FPS':
            timeName = ['game','film','pal','ntsc','show','palf','ntscf']
            timeSpeed= [15,     24,    25,   30,    48,    50,   60]
            fpsFrameName = timeName[timeSpeed.index(fpsFrame)]
            if checkMode:
                speedMode = mc.currentUnit(time = 1,q=1)
                if  speedMode != fpsFrameName:
                    if not returnMode:
                        errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(100)
                        print errorInfo
                        sk_infoConfig.errorCode = errorInfo
                        mc.error()
                    else:
                        errorList.append('[Error FPS]')
            if fpsFrame:
                mc.currentUnit(time = fpsFrameName)
            else:
                errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(101)
                mc.warning(errorInfo)
        # frame
        if configType == 'frame':
            if startFrame and endFrame:
                if checkMode:
                    fileStartFrame = int(mc.playbackOptions(min=1,q=1))
                    fileEndFrame   = int(mc.playbackOptions(max=1,q=1))
                    if fileStartFrame != startFrame or fileEndFrame != endFrame:
                        if not returnMode:
                            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(102)
                            print errorInfo
                            sk_infoConfig.errorCode = errorInfo
                            mc.error()
                        else:
                            errorList.append('[Error Frame Range]')
                # 起始帧
                mc.playbackOptions(min=startFrame)
                # 起始预留
                preStartFrame = startFrame - pre
                mc.playbackOptions(animationStartTime=preStartFrame)
                # 结束帧
                mc.playbackOptions(max=endFrame)
                # 结束预留
                posEndFrame = endFrame + pre
                mc.playbackOptions(animationEndTime=posEndFrame)
            else:
                errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(103)
                mc.warning(errorInfo)
        mc.playbackOptions(playbackSpeed=1)
        # 允许undo
        mc.undoInfo(state=True, infinity=True)

    # ----------------------------------------------------------------------------------------------#

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 【场景文件整理】
    # ------------------------------#
    # 根据参考整理文件 0 不删除多余物体，保留在OTC | 1 删除多余物体 |  anMode 启动时无视OTC,参考类型打组
    # finalLayout环节先清理约束再处理分组
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
        if mc.ls('|VFX_GRP') or mc.ls('|OTC_GRP|VFX_GRP'):
            if mc.ls('|VFX_GRP'):
                vfxGrp = '|VFX_GRP'
            if mc.ls('|OTC_GRP|VFX_GRP'):
                vfxGrp = '|OTC_GRP|VFX_GRP'
        else:
            vfxGrp = mc.group(em=1, name='VFX_GRP')
        if vfxGrp[0] not in ['|']:
            vfxGrp = '|' + vfxGrp
        # 鱼群集群
        if mc.ls('|Cluster_GRP') or mc.ls('|OTC_GRP|Cluster_GRP'):
            if mc.ls('|Cluster_GRP'):
                clusterFlowGrp = '|Cluster_GRP'
            if mc.ls('|OTC_GRP|Cluster_GRP'):
                clusterFlowGrp = '|OTC_GRP|Cluster_GRP'
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
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
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
                if '/characters/' in path or '/crowd/' in path:
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
            import sk_pyCommon
            reload(sk_pyCommon)
            for ns in ogNsGrp:
                sk_pyCommon.sk_pyCommon().sk_deleteNamespace(ns)

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
            inr = mc.referenceQuery(checkGrp,inr=1)
            if inr:
                continue
            childNodes = mc.listRelatives(checkGrp,ad=1,type = 'transform',f=1)
            if childNodes:
                for childGrp in childNodes:
                    deleteState = 0
                    mesh = mc.listRelatives(childGrp,s=1,type= 'mesh',f=1)
                    if mesh:
                        deleteState = 1
                    cam = mc.listRelatives(childGrp,s=1,type= 'camera',f=1)
                    if cam:
                        deleteState = 1
                    shape = mc.listRelatives(childGrp,s=1)
                    if not shape:
                        deleteState = 1
                    if deleteState:
                        mc.lockNode(childGrp,l=0)
                        mc.delete(childGrp)
            deleteState = 0
            mesh = mc.listRelatives(checkGrp,s=1,type= 'mesh',f=1)
            if mesh:
                deleteState = 1
            cam = mc.listRelatives(checkGrp,s=1,type= 'camera',f=1)
            if cam:
                deleteState = 1
            if not childNodes:
                deleteState = 1
            if deleteState:
                mc.lockNode(checkGrp,l=0)
                mc.delete(checkGrp)

    # ------------------------------#
    # 【核心】 【asset 参考 namespace校正】
    # ------------------------------#
    # reference namespace 处理
    def sk_sceneAssetNamespaceConfig(self):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        import sk_pyCommon
        reload(sk_pyCommon)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        refNamespace = refInfos[2][0]

        allRefPaths = list(set(refPaths))

        for refPath in allRefPaths:
            if '_cam.' in refPath:
                continue
            assetInfo = refPath.split('/')[-1].split('_')
            if len(assetInfo) < 4:
                continue
            assetName = assetInfo[0] + '_' + assetInfo[1]
            # 只有一个时
            if refPaths.count(refPath) == 1:
                refIndex = refPaths.index(refPath)
                realRefPath = mc.referenceQuery(refNodes[refIndex], filename=1)
                newNamespace = assetName + '_' + assetInfo[2]
                # 是否加载
                isRefLoad = mc.referenceQuery(refNodes[refIndex], isLoaded=1)
                if isRefLoad:
                    # 只处理非法名字
                    print '-------'
                    print newNamespace
                    print refNamespace[refIndex]
                    print realRefPath
                    if newNamespace != refNamespace[refIndex]:
                        try:
                            print '---nsFix'
                            print realRefPath
                            mc.file(realRefPath, e=1, ns=newNamespace)
                        except:
                            print '\n'
                            print u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex])
                            print u'======有重复的namespace，重复编号往大处理======'
                            mc.error(u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex]))
            # 多个asset时
            else:
                allIndex = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(refPaths, refPath)
                for i in range(len(allIndex)):
                    refIndex = allIndex[i]
                    realRefPath = mc.referenceQuery(refNodes[refIndex], filename=1)
                    newNamespace = assetName + '_' + assetInfo[2] + '_' + str(i + 1)
                    if i == 0:
                        newNamespace = assetName + '_' + assetInfo[2]
                    # 是否加载
                    isRefLoad = mc.referenceQuery(refNodes[refIndex], isLoaded=1)
                    if isRefLoad:
                        # 只处理非法名字
                        if newNamespace != refNamespace[refIndex]:
                            try:
                                print '---001'
                                print realRefPath
                                mc.file(realRefPath, e=1, ns=newNamespace)
                            except:
                                print '\n'
                                print u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex])
                                print u'======有重复的namespace，重复编号往大处理======'
                                mc.error(u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex]))

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

    # ----------------------------------------------------------------------------------------------#

    # ------------------------------#
    # 【辅助】 文件清理相关
    # ------------------------------#

    # ------------------------------#
    # 【通用：清理unUsed及unknown节点及turtle节点】
    # 0.通用
    # Author  : 沈  康
    # Data    : 2013_05_19
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
        refExist = ''
        try:
            refExist = mc.referenceQuery(
                '//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/QSK_lib/QSK_model.ma',
                rfn=1)
        except:
            pass
        if refExist:
            mc.file(rfn=refExist, removeReference=1)
        # 清理无用SG节点
        if shotMode in [1]:
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
        if shotMode in [1]:
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
        # 清理无用ref节点
        refNodes = mc.ls(type = 'reference')
        for checkRefNode in refNodes:
            refState = mc.referenceQuery(checkRefNode,inr = 1)
            if refState:
                continue
            try:
                isLoaded = mc.referenceQuery(checkRefNode,isLoaded = 1)
            except:
                mc.lockNode(checkRefNode,l = 0)
                mc.delete(checkRefNode)
        # unkown plugin清理
        vInfo = mc.about(v=1)
        vNum = 0
        if len(vInfo)>=4 and '20' in vInfo[:2]:
            vNum = int(vInfo[:4])
        if vNum >= 2016:
            unknownPlugins = mc.unknownPlugin(list = 1, q=1)
            if unknownPlugins:
                for up in unknownPlugins :
                    try:
                        mc.unknownPlugin(up,remove = 1)
                    except:
                        pass

    # ------------------------------#
    # 清理displayLayer，delete0时打印，1时删除，3时只拦截不显示非donotLayers层。
    def checkCleanDisplayLayers(self, layers=[], donotLayers=[], delete=1):
        if not layers:
            layers = mc.listConnections('layerManager.displayLayerId')
        if not layers:
            layers = []
        errorDelete = []
        for layer in layers:
            if 'defaultLayer' in layer:
                continue
            if layer.lower() in donotLayers:
                continue
            # 判断是否参考
            refInfo = mc.referenceQuery(layer, isNodeReferenced=1)
            if refInfo:
                mc.warning(u'============【参考层】【%s】无法清理============' % (layer))
            else:
                # 断开连接模式
                if delete:
                    if delete == 1:
                        # 断开layerManager和其连接再删除
                        layerManager = mc.connectionInfo((layer + '.identification'), sourceFromDestination=1)
                        if layerManager:
                            if 'layerManager' in layerManager:
                                mc.disconnectAttr(layerManager, (layer + '.identification'))
                        # 断开输出链接
                        outputs = mc.connectionInfo((layer + '.drawInfo'), destinationFromSource=1)
                        if outputs:
                            for out in outputs:
                                mc.disconnectAttr((layer + '.drawInfo'), out)
                    if delete == 3:
                        if layer.lower() not in donotLayers:
                            errorDelete.append(layer)
                else:
                    if layer.lower() not in donotLayers:
                        errorDelete.append(layer)
        if delete == 1:
            for layer in layers:
                if 'defaultLayer' not in layer:
                    if donotLayers:
                        if layer not in donotLayers:
                            mc.delete(layer)
                    else:
                        mc.delete(layer)
        return errorDelete

    #------------------------------#
    # 不显示的显示层物体继承到norender OK
    def checkHideObjs2Norender(self,targetLayer = 'norender',skipList = []):
        hideObjs = []
        checkLayers = mc.ls(type='displayLayer')
        checkLayers.remove('defaultLayer')
        for checkLayer in checkLayers:
            inr = mc.referenceQuery(checkLayer,inr = 1)
            if inr:
                continue
            if checkLayer in skipList:
                continue
            if mc.getAttr(checkLayer + '.v'):
                continue
            layerObjs = mc.editDisplayLayerMembers(checkLayer,q=1,fullNames = 1)
            if layerObjs:
                hideObjs += layerObjs
        if not hideObjs:
            return
        hideObjs = list(set(hideObjs))
        if not mc.ls(targetLayer,type = 'displayLayer'):
            mc.createDisplayLayer(name = targetLayer)
        mc.setAttr(targetLayer + '.v',0)
        for hideObj in hideObjs:
            mc.editDisplayLayerMembers(targetLayer,hideObj,noRecurse = 1)

    # ------------------------------#
    # 清理renderLayer
    def checkCleanRenderLayers(self):
        # 回到masterLayer
        #mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        #layers = mc.ls(type='renderLayer')
        #layers.remove('defaultRenderLayer')
        # 黄仲维将这3行改成以下写法，20170426
        layers = mc.listConnections("renderLayerManager.renderLayerId");
        mel.eval('editRenderLayerGlobals -currentRenderLayer %s' % layers[0])
        layers.pop(0)
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

    # 删除|加载 未勾选的参考
    def sk_sceneUnloadRefDel(self, deleteMode=1, reloadMode=0):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
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
    # 删除不需要的层(除了norender)
    def sk_sceneCleanDislayLayers(self):
        displayLayers = mc.listConnections('layerManager.displayLayerId')
        if displayLayers:
            for layer in displayLayers:
                if layer.lower() == 'norender':
                    displayLayers.remove(layer)
            self.checkCleanDisplayLayers(displayLayers)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 通用：锁lock/解锁unlock工具】
    # 0.阶段通用
    # 1.对指定节点及其下属子节点及其本身进行lock处理
    # 2.将显示属性解锁
    # 3.MODEL组不锁
    # Author  : 沈  康
    # Data    : 2013_03_29
    # Data    : 2013_05_10 处理重名物体带来的问题。解锁和锁合并函数
    #------------------------------#
    # 对控制器不锁
    def checkLockObjs(self , objs , typeNum , lockTop = 1 ,justModel = 1):
        if not objs:
            return
        doNotLock = ['drawOverride','visibility','lodVisibility','message','enable','active']
        lockAttrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz',]
        allObjs = mc.listRelatives(objs,ad =1,type ='transform',f = 1)
        if allObjs:
            allObjs = allObjs + objs
        else:
            allObjs = objs
        nurbsCurvs = mc.listRelatives(objs,ad =1,ni = 1,type ='nurbsCurve',f = 1)
        nurbsCurvsGrps = []
        if nurbsCurvs:
            nurbsCurvsGrps  = mc.listRelatives(nurbsCurvs,p =1,type ='transform',f = 1)
        nurbsShapes = mc.listRelatives(objs,ad =1,ni = 1,type ='nurbsSurface',f = 1)
        nurbsShapeGrps = []
        if nurbsShapes:
            nurbsShapeGrps = mc.listRelatives(nurbsShapes,p =1,type ='transform',f = 1)
        nurbsObjs = nurbsCurvsGrps + nurbsShapeGrps
        for obj in allObjs:
            # 参考不处理
            isRef = mc.referenceQuery(obj,isNodeReferenced = 1)
            if isRef:
                continue
            if justModel and '|MODEL|' not in obj:
                continue
            # 忽略骨骼 和 解算节点
            if mc.nodeType(obj) in ['joint','nucleus']:
                continue
            # 忽略特殊Loc
            if '__reference' in obj.split('|')[-1].lower() and typeNum:
                continue
            if obj in nurbsObjs:
                continue
            for attr in lockAttrList:
                mc.setAttr((obj+attr),l=int(typeNum))
            mc.setAttr((obj + '.visibility'), l=0)
            mc.setAttr((obj + '.lodVisibility'), l=0)

        if not lockTop:
            obj = objs[0]
            # 参考不处理
            isRef = mc.referenceQuery(obj,isNodeReferenced = 1)
            if not isRef:
                for attr in lockAttrList:
                    mc.setAttr((obj + attr),l=int(0))
                mc.setAttr((obj + '.visibility'), l=0)
                mc.setAttr((obj + '.lodVisibility'), l=0)

    # ------------------------------#
    # 解锁所有V
    # 解锁所有lodV
    def checkUnlockMSHV(self,justModel = 1):
        meshes = mc.ls(type='mesh', l=1)
        if justModel:
            meshes = mc.listRelatives('MODEL',ad = 1, type = 'mesh',f = 1)
        if not meshes:
            return
        for mesh in meshes:
            grp = mc.listRelatives(mesh, p=1, type='transform', f=1)
            if not grp:
                continue
            isRef = mc.referenceQuery(mesh,inr = 1)
            if isRef:
                continue
            grp = grp[0]
            checkAttr = (grp + '.v')
            tempAttr = mc.connectionInfo(checkAttr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)
            checkAttr = (grp + '.lodVisibility')
            tempAttr = mc.connectionInfo(checkAttr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)

    #------------------------------#
    # 补充，解锁道具的geo组 ,需要下面的文件支持
    def checkUnlockMSHGeo(self , MODELUnlock = 1):
        # MODEL解锁
        if not MODELUnlock:
            return
        unlockList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v','.lodVisibility']
        unlockObjs = mc.ls('MODEL',l=1)
        for unlockObj in unlockObjs:
            isRef = mc.referenceQuery(unlockObj,inr = 1)
            if isRef:
                continue
            if not mc.ls(unlockObj):
                continue
            for attr in unlockList:
                tempAttr = mc.connectionInfo(unlockObj + attr,gla=1)
                if tempAttr:
                    mc.setAttr(tempAttr,l=0)

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 相关Set处理
    # ------------------------------#

    # ------------------------------#
    # 【通用：cacheSet自动创建】
    #  0.仅在model,rig,texture通用
    #  1.含创建、更新cacheSet
    #  Author  : 沈  康
    #  Data    : 2013_05_16
    # ------------------------------#

    # ------------------------------#
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
            # mc.sets(cl='MESHES')

    # ------------------------------#
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
            # mc.sets(cl='CTRLS')

    # 批量清理多余Set组
    def checkNoNeedSetClean(self):
        cleanSets = mc.ls('*CACHE_OBJS*',type= 'objectSet')
        for cleanSet in cleanSets:
            self.checkTargetSetClean(cleanSet)
        cleanSets = mc.ls('*TRANSANIM_OBJS*',type= 'objectSet')
        for cleanSet in cleanSets:
            self.checkTargetSetClean(cleanSet)

    # 清理多余Set组
    def checkTargetSetClean(self,cleanRoot = 'CACHE_OBJS'):
        if not mc.ls(cleanRoot):
            return
        childSets = mc.sets(cleanRoot, q=1)
        if not childSets:
            return
        for checkObj in childSets:
            if mc.nodeType(checkObj) in ['objectSet']:
                mc.delete(checkObj)
        if mc.ls(cleanRoot):
            mc.delete(cleanRoot)

    # ------------------------------#
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
                if '|MODEL|' in mc.ls(node, l=1)[0]:
                    if node[-1] == '_':
                        needNodes.append(node)
                    shape = mc.listRelatives(node, c=1, type='mesh')
                    if shape:
                        if node not in needNodes:
                            needNodes.append(node)
            if needNodes:
                mc.sets(needNodes, e=1, addElement='MESHES')
            print u'---'
        print (u'CacheList    ' + str(len(needNodes)))

    # ------------------------------#
    # 更新AnimSet列表 ，这个不会在mo阶段处理
    # 传递动画用nurbs曲线 要求：
    # 　1.必须有属性ct_an 2.必须在MODEL组内 3.不得使用形变绑定
    def checkTransAnimSetAdd(self):
        self.checkCacheSetCreate()
        self.checkTransAnimSetCreate()
        mc.sets(cl='CTRLS')
        nodes = []
        # 属性上的
        nurbsCurves = mc.ls(type='nurbsCurve', l=1)
        if nurbsCurves:
            for shape in nurbsCurves:
                curveNode = mc.listRelatives(shape, p=1, typ='transform', f=1)
                if not curveNode:
                    continue
                curveNode = curveNode[0]
                attrCurveNode = mc.listAttr(curveNode)
                if 'ct_an' in attrCurveNode:
                    nodes.append(curveNode)
        # 名字上的
        nodes = nodes + mc.ls('*_ct_an*', type='transform')
        if nodes:
            needNodes = []
            # 支持组传递信息，可以考虑隐藏hide组,控制器 的显示|隐藏 约束 隐藏专用grp
            for node in nodes:
                if '|MODEL|' in mc.ls(node, l=1)[0] and node[-1] != '_':
                    if '_nr_' not in node and '_si_' not in node and '_proxy_' not in node and '_ca_' not in node:
                        needNodes.append(node)
            if needNodes:
                mc.sets(needNodes, e=1, addElement='CTRLS')
            print (u'AnimList    ' + str(len(needNodes)))

    # ------------------------------#
    # cacheSet,animSet,Proxy_Set合并处理
    # 获取所有MESHES或CTRLS级别的objectSet，甄别出非正版的"CacheSetx"或"AnimSetx"，将盗版物体绑架到正版Set去
    def checkCacheAnimSetCombine(self, setType, proType=''):
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
                        mc.sets(meshes, e=1, addElement=keyWords)
                    try:
                        # 对于参考，pass
                        mc.delete(objSet)
                    except:
                        pass
        else:
            print u'=========未发现有效的[%s]Set组=========' % setType

    # ------------------------------#
    # 获取标记nodes    #同一物体，_ca_与_an_无法共存;_si_与_nr_
    def checkGetSignNodes(self, sign, noNeed):
        nodes = mc.ls(type='transform')
        signNodes = []
        for node in nodes:
            # 排除非nurbs及mesh类
            shape = mc.listRelatives(node, s=1, f=1)
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

    # ------------------------------#
    # 获取场景中所有cacheSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkCacheSetObjects(self, otcGrp=1):
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
                            if '|OTC_GRP|' in mc.ls(mesh, l=1)[0] or '|SET_GRP|' in mc.ls(mesh, l=1)[0] or \
                                            mc.ls(mesh, l=1)[0].split('|')[-1][3] in ['s', 'S']:
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
    # 贴图,cache环境变量
    #------------------------------#
    def sk_setPathEnv(self,oldPre = '' , newPre = '${IDMT_PROJECTS}',skipType = [],justType = []):
        if not oldPre:
            oldPre = sk_infoConfig.sk_infoConfig().serverPre
        # 每个镜头运行次
        typeDict = sk_infoConfig.sk_infoConfig().nodeDict
        fileNodes = []
        for checkType in typeDict.keys():
            if checkType in skipType:
                continue
            if justType and checkType not in justType:
                continue
            fileNodes += mc.ls(type = checkType)
        for checkNode in fileNodes:
            checkType = mc.nodeType(checkNode)
            checkAttr = typeDict[checkType]
            oldPath = mc.getAttr(checkNode + checkAttr)
            if oldPre not in oldPath:
                continue
            newPath = oldPath.replace(oldPre,newPre)
            mc.setAttr(checkNode + checkAttr,newPath,type = 'string')

        yetiNodes = mc.ls(type = 'pgYetiMaya')
        for yetiNode in yetiNodes:
            txNodes = mc.pgYetiGraph(yetiNode,listNodes= 1, type = 'texture')
            if not txNodes:
                continue
            for checkTxNode in txNodes:
                oldPath = mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name',getParamValue = 1)
                if newPre in ['${IDMT_PROJECTS}']:
                    newPre = 'Z:/Projects'
                    oldPre = oldPre.replace('//file-cluster/GDC/Projects',newPre)
                if oldPre not in oldPath:
                    continue
                newPath = oldPath.replace(oldPre,newPre)
                mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name',setParamValueString = newPath)

    #-------------------------------#
    # 贴图统一切换盘符
    def checkTextureSwitch(self,target = 'Z:'):
        oldPathes = ['//file-cluster/GDC/Projects','L:','Z:','${IDMT_PROJECTS}']
        for oldPath in oldPathes:
            if oldPath in ['//file-cluster/GDC/Projects','${IDMT_PROJECTS}']:
                self.sk_setPathEnv(oldPath,(target + '/Projects'))
            if oldPath in ['L:','Z:']:
                self.sk_setPathEnv(oldPath,target)

    # ------------------------------#
    # 【cacheSet合并处理】
    # 白海豚用，其他项目或可通用
    # 获取所有MESHES或CTRLS级别的objectSet，甄别出非正版的"CacheSetx"或"AnimSetx"，将盗版物体绑架到正版Set去
    # 加入proxy_Set处理
    # ------------------------------#
    def sk_sceneCacheAnimSetConfig(self, setType, proType):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
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
            # 获取盗版Set
            if keyWords in temp and temp != keyWords:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                if not mc.ls(objSet):
                    continue
                # 获取盗版mesh
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    mc.sets(meshes, e=1, addElement=keyWords)
                try:
                    # 对于参考，pass
                    mc.delete(objSet)
                except:
                    pass

    # ------------------------------#
    # 直接全部处理好所有的set合并
    def sk_sceneSetCombineConfig(self, proType='ZM'):
        import sk_smoothSet
        reload(sk_smoothSet)
        self.sk_sceneCacheAnimSetConfig('Anim', proType)
        self.sk_sceneCacheAnimSetConfig('Cache', proType)
        sk_smoothSet.sk_smoothSet().smoothSetCombine('Smooth', proType)

    # ---------------------------------------------------#
    # 删除mr节点
    def checkMrNodesDel(self):
        fileName = mc.file(exn=1, q=1)
        localPath = sk_infoConfig.sk_infoConfig().checkTexLocalPath()

        # 清理mr节点
        nodeTypes = mel.eval("pluginInfo -q -dependNode \"Mayatomr\"")
        nodes = []
        for nodeType in nodeTypes:
            nodes = nodes + mc.ls(type=nodeType)
        for node in nodes:
            if mc.ls(node):
                mc.lockNode(node, l=0)
                mc.delete(node)

        # 存ma
        maName = localPath + fileName.split('.')[0].split('/')[-1] + '.ma'
        print maName
        mc.file(rename=maName)
        mc.file(force=1, options="v=0", type='mayaAscii', save=1)

        # 读ma文件
        fileInfos = sk_infoConfig.sk_infoConfig().checkFileRead(maName)
        newFileInfos = []
        for line in fileInfos:
            if 'requires' in line and 'Mayatomr' in line:
                continue
            newFileInfos.append(line)

        # 保存文件
        sk_infoConfig.sk_infoConfig().checkFileWrite(maName, newFileInfos)

        # 重开文件
        mc.file(f=1, new=1)
        try:
            mel.eval('unloadPlugin "Mayatomr"')
        except:
            pass
        mc.file(maName, open=1, force=1)
        # 另存mb
        mbName = localPath + fileName.split('.')[0].split('/')[-1] + '.mb'
        mc.file(rename=mbName)
        mc.file(force=1, options="v=0", type='mayaBinary', save=1)

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用：model命名检测工具】
    # 非anim转anim
    # Author  : 沈  康
    # ------------------------------#
    def sk_sceneNotAnim2Anim(self):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]

        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 最优先
            # 非标准参考转标准参考
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb', '_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 非标准参考转标准参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb', '_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 转换参考，model文件
            if '_mo.' in path:
                newPath = path.replace('/model/', '/master/')
                newPath = newPath.replace('_mo.', '_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 转换参考，rigging文件
            if '_rg.' in path:
                newPath = path.replace('/rigging/', '/master/')
                newPath = newPath.replace('_rg.', '_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 转换参考，tx文件
            if '_tx.' in path:
                newPath = path.replace('/texture/', '/master/')
                newPath = newPath.replace('_tx.', '_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 转换参考，notex和tex
            if '_ms_notex.' in path:
                newPath = path.replace('_ms_notex.', '_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])
            # 转换参考，notex和tex
            if '_ms_tex.' in path:
                newPath = path.replace('_ms_tex.', '_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])

    # ------------------------------#
    # anim转render  1 anim->render | 2 anim->tx
    def sk_sceneNotAnim2Render(self, transType=1):
        import sk_referenceConfig

        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        # 处理参考
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            path = refPath.lower()
            # 转换参考
            if transType == 1:
                oldKey = '_ms_anim.'
                newKey = '_ms_render.'
                if oldKey in path:
                    newPath = path.replace(oldKey, newKey)
                    # 替换参考
                    mc.file(newPath, loadReference=refNodes[i])
            if transType == 2:
                oldKey = '_ms_anim.'
                newKey = '_tx.'
                if oldKey in path:
                    newPath = path.replace(oldKey, newKey)
                tempPath = newPath
                oldKey = 'master'
                newKey = 'texture'
                if oldKey in tempPath:
                    newPath = tempPath.replace(oldKey, newKey)
                # 替换参考
                mc.file(newPath, loadReference=refNodes[i])

    #-------------------------------#
    # 读取ma文件,修改文件参考加载状态 loadType 1 要加载 | 0 不要加载 |
    def checkMaFileRefLoad(self,maFile,loadType = 0 , skipAssetKey = 'sets'):
        readlines  = sk_infoConfig.sk_infoConfig().checkFileRead(maFile)
        for num in range(len(readlines)):
            lineInfo = readlines[num]
            if 'file -rdi ' not in lineInfo:
                continue
            if skipAssetKey and '/%s/'%skipAssetKey in lineInfo.lower():
                continue
            # -dr 1 不加载 | 无-dr或者-dr 0加载
            if loadType:
                if '-dr ' in lineInfo:
                    # 获取dr的参数
                    drValue = lineInfo.split('-dr ')[-1].split('-')[0].replace(' ','')
                    allInfos = lineInfo.split('-dr %s '%drValue)
                    lineInfo = allInfos[0] + allInfos[1]
                else:
                    continue
            else:
                if '-dr ' in lineInfo:
                    # 获取dr的参数
                    drValue = lineInfo.split('-dr ')[-1].split('-')[0].replace(' ','')
                    if int(drValue):
                        allInfos = lineInfo.split('-dr %s '%drValue)
                        lineInfo = allInfos[0] + allInfos[1]
                    else:
                        allInfos = lineInfo.split('-dr %s '%drValue)
                        lineInfo = allInfos[0] + '-dr 1 ' + allInfos[1]
                else:
                    allInfos = lineInfo.split('-rfn ')
                    lineInfo = allInfos[0] + '-dr 1 -rfn ' + allInfos[1]
            readlines[num] = lineInfo
        sk_infoConfig.sk_infoConfig().checkFileWrite(maFile,readlines,lineKey = '')

    # ----------------------------------------------------------------------------------------------#

    # ------------------------------#
    # 【通用：model命名检测工具】
    # 0.仅在model,rig,texture通用
    # 1.检测只有一个大组
    # 2.所有带'_'的物体是否有shape节点
    # Author  : 沈  康
    # Data    : 2013_05_16
    # ------------------------------#
    # 检测大纲内大组数
    def checkOutlinerGroup(self):
        grps = mc.ls(type='transform', l=1)
        grps.remove('|persp')
        grps.remove('|top')
        grps.remove('|front')
        grps.remove('|side')
        rootGrp = []
        for grp in grps:
            setpGrp = grp.split('|')
            if len(setpGrp) == 2:
                rootGrp.append(grp)
        return rootGrp

    # ------------------------------#
    # 【通用：检测v属性】
    #  参考老赵思路：没有现成的函数，只能自己写
    # Author  : 沈  康
    # Data    :2014_02_10
    # ------------------------------#

    # 核心处理物体
    def checkObjVState(self, checkObj):
        # 物体不存在则返回0
        if not mc.objExists(checkObj):
            return 0
        # 物体v属性是否存在
        if not mc.attributeQuery('visibility', node=checkObj, exists=1):
            return 0
        result = mc.getAttr(checkObj + '.visibility')
        # intermediate mesh
        if mc.attributeQuery('intermediateObject', node=checkObj, exists=1):
            checkValue = mc.getAttr(checkObj + '.intermediateObject')
            result = result and (not checkValue)
        # displayLayer
        if mc.attributeQuery('overrideEnabled', node=checkObj, exists=1) and mc.getAttr(checkObj + '.overrideEnabled'):
            checkValue = mc.getAttr(checkObj + '.overrideVisibility')
            result = result and checkValue
        # 层级
        if result:
            parentNodes = mc.listRelatives(checkObj, p=1, f=1)
            if parentNodes:
                result = result and self.checkObjVState(parentNodes[0])

        return result

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【导出camera ABC格式】
    # ------------------------------#
    # info 2 为 cl_xxx_xxx模式 | 3 为 yd_xxx_xxx_xxx模式
    def LY_CameraABC(self, batchUpadate=0, shotType=0):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig

        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig

        reload(sk_referenceConfig)
        if not mc.pluginInfo('AbcExport', loaded=1, q=1):
            mc.loadPlugin('AbcExport')

        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if not shotType:
            shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        if shotType == 3:
            shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]

        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd

        ProjectsPath = '//file-cluster/GDC/Projects/'
        camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + \
                      shotInfo[1] + "/"
        camServerBasePath = "//file-cluster/GDC/Projects/" + projectInfo + "/Project/scenes/Animation/episode_" + \
                            shotInfo[1] + "/episode_camera/"

        camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.abc'
        camInfo = camTempPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.abc'

        if shotType == 3:
            camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + \
                          shotInfo[1] + "/"
            camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[
                3] + '_cam.abc'
            camInfo = camTempPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + shotInfo[3] + '_cam.abc'
        mc.sysFile(camTempPath, makeDir=True)
        # 先删除cam参考
        print u'=================ready to remove camera reference=================='
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            if camServerPath in refPaths:
                id = refPaths.index(camServerPath)
                refNode = refNodes[id]
                if batchUpadate:
                    mc.file(rfn=refNode, removeReference=1)
        print u'===============removed camera reference============================'

        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        if shotType == 3:
            camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3])

        # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
        needCamList = self.sk_getProjNeedCamera(shotInfo,shotType)
        preFrame = 20
        if needCamList:
            for needCam in needCamList:
                abcFile = needCam.split('|')[-1].replace('cam_', (shotInfo[0] + '_')) + '_cam.abc'
                InfoCam = "-fr" + " " + str(startFrame-preFrame) + " " + str(endFrame+preFrame) + " " + "-root " + needCam + " -file " + (
                camTempPath + abcFile)
                mc.AbcExport(j=InfoCam)
                # 输出相机
                mel.eval('zwSysFile \"copy\" \"' + (camTempPath + abcFile) + '\" \"' + (camServerBasePath + abcFile) + '\" 1')
                print camTempPath + abcFile
                print camServerBasePath + abcFile
        print u'====================成功更新camera到服务器端===================='
        # 成功代码
        return 0

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 动画曲线偏移系列
    #  keyframe无-r标签即出错
    # ------------------------------#
    # UI
    def checkSceneAnOffsetUI(self):
        # 窗口
        if mc.window("sk_frameOffsetTools", ex=1):
            mc.deleteUI("sk_frameOffsetTools", window=True)
        mc.window("sk_frameOffsetTools", title="Frame Offset Tools", widthHeight=(300, 400), menuBar=0, sizeable=0)
        columnLayout = mc.columnLayout(adjustableColumn=1, columnOffset=['both', 0])
        # 项目选取区域
        mc.frameLayout(l=u'物体选取模式', collapse=0, collapsable=0, borderStyle='etchedIn')
        # 输入
        mc.columnLayout(adjustableColumn=1, columnOffset=['both', 0])
        mc.radioButtonGrp('sk_frameOffsetObjectMode', numberOfRadioButtons=3, labelArray3=[u'所有物体', u'Root组', u'选取物体'],
                          width=300, columnWidth3=[100, 100, 100], select=1)
        mc.setParent()
        mc.setParent(columnLayout)

        # assetImput
        mc.frameLayout(l=u'帧范围选取模式', collapse=0, collapsable=0, borderStyle='etchedIn')
        # 清单
        mc.columnLayout(adjustableColumn=1, columnOffset=['both', 0])
        mc.radioButtonGrp('sk_frameOffsetFrameMode', numberOfRadioButtons=3, labelArray3=[u'所有曲线', u'当前帧开始', u'选取范围'],
                          width=300, columnWidth3=[100, 100, 100], select=2)
        mc.setParent()
        mc.setParent(columnLayout)

        # 偏移值
        mc.frameLayout(l=u'偏移值', collapse=0, collapsable=0, borderStyle='etchedIn')
        # 清单
        mc.columnLayout(adjustableColumn=1, columnOffset=['both', 0])
        mc.floatField('sk_frameOffsetField', value=0)
        mc.setParent()
        mc.setParent(columnLayout)

        # 按钮区
        mc.button(l=u'执行', bgc=[0, 0.8, 0.1], height=30,
                  c='from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().checkSceneOffsetButton()')
        mc.setParent()
        mc.setParent()

        mc.showWindow("sk_frameOffsetTools")

    # button cmd
    def checkSceneOffsetButton(self):
        # animCurvs
        objMode = mc.radioButtonGrp('sk_frameOffsetObjectMode', q=1, select=1)
        animCurves = []
        if objMode == 1:
            animCurves = mc.ls(type='animCurve')
            temps = []
            for animCurve in animCurves:
                isRef = mc.referenceQuery(animCurve, inr=1)
                if isRef:
                    continue
                temps.append(animCurve)
            animCurves = temps
        if objMode in [2, 3]:
            allGrps = mc.ls(sl=1, l=1)
            if objMode == 2:
                tempGrps = mc.listRelatives(allGrps, ad=1, type='transform', f=1)
                if tempGrps:
                    allGrps = tempGrps + allGrps
            for grp in allGrps:
                animCurveList = mc.listConnections(grp, s=1, t=0, type='animCurve')
                if not animCurveList:
                    continue
                for animNode in animCurveList:
                    isRef = mc.referenceQuery(animNode, inr=1)
                    if isRef:
                        continue
                    if animNode in animCurves:
                        continue
                    animCurves.append(animNode)
        # frameRanges
        frameMode = mc.radioButtonGrp('sk_frameOffsetFrameMode', q=1, select=1)
        frameEnd = mc.playbackOptions(max=1, q=1)
        if frameMode == 1:
            frameStart = mc.playbackOptions(min=1, q=1)
        if frameMode == 2:
            frameStart = mc.currentTime(q=1)
            frameStart = frameStart + 1
        if frameMode == 3:
            infos = self.checkSceneGetTimeSelRange()
            frameStart = infos[0]
            frameEnd = infos[1]
        frameRange = (frameStart, frameEnd)
        # offsetValue
        offsetValue = mc.floatField('sk_frameOffsetField', value=1, q=1)
        # 执行
        self.checkSceneAnimOffsetPerform(animCurves, offsetValue, frameRange)

    def checkSceneGetTimeSelRange(self):
        playbackslider = mel.eval('$temp = $gPlayBackSlider;')
        timeRange = mc.timeControl(playbackslider, q=1, rng=1)
        rangeList = [float(timeRange.split(':')[0].split('"')[-1]), float(timeRange.split(':')[1].split('"')[0])]
        return rangeList

    def checkSceneAnimOffsetPerform(self, animCurves, offsetValue=0, frameRange=(0, 0)):
        mc.keyframe(animCurves, e=1, iub=True, o='over', time=frameRange, r=1, tc=offsetValue)
        '''
        for animCurve in animCurves:
            if mc.listConnections('%s.input' % animCurve):
                continue
            animkeyscount = mc.keyframe(animCurve, q=1, iv=1)
            mc.keyframe(animCurve, e=1, iub=True, r=1, o='over', tc=offsetValue, index=(0, len(animkeyscount)-1))
        '''

    #---------------------#
    # 镜头文件显示层记录/恢复
    def checkShotDisLRecord(self):
        localDisPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 0,infoMode = 10)
        serverDisPath= sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 10)
        localFile = '%s/ShotDisInfo.json'%localDisPath
        serverFile= '%s/ShotDisInfo.json'%serverDisPath
        # 查询所有非参考显示层
        disLayers = mc.ls(type = 'displayLayer')
        temp = []
        for checkLayer in disLayers:
            inr = mc.referenceQuery(checkLayer,inr = 1)
            if inr:
                continue
            if checkLayer in ['defaultLayer']:
                continue
            temp.append(checkLayer)
        disLayers = temp
        # 记录
        disDict = dict()
        for checkLayer in disLayers:
            objs = mc.editDisplayLayerMembers(checkLayer,q=1,fullNames = 1)
            state = mc.getAttr('%s.v'%checkLayer)
            disDict[checkLayer] = [state,objs]
        # 备份上传
        sk_infoConfig.sk_infoConfig().writeDict(localFile,disDict)
        cmd = r'zwSysFile  "copy" "' + localFile + '" "' + serverFile + '" 1'
        mel.eval(cmd)

    def checkShotDisLLoad(self):
        serverDisPath= sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,infoMode = 10)
        serverFile= '%s/ShotDisInfo.json'%serverDisPath
        disDict = sk_infoConfig.sk_infoConfig().readDict(serverFile)
        disLayers = disDict.keys()
        if not disLayers:
            return
        lostObjs = []
        for checkLayer in disLayers:
            state = disDict[checkLayer][0]
            if not mc.ls(checkLayer):
                mc.createDisplayLayer(name = checkLayer)
            mc.setAttr('%s.v'%checkLayer,state)
            objs= disDict[checkLayer][1]
            if not objs:
                continue
            needObjs = []
            for checkObj in objs:
                if mc.ls(checkObj):
                    needObjs.append(checkObj)
                else:
                    shortName = checkObj.split('|')[-1]
                    newName = mc.ls(shortName,l=1)
                    if newName:
                        needObjs = needObjs + newName
                    else:
                        lostObjs.append(shortName)
            if not needObjs:
                continue
            mc.editDisplayLayerMembers(checkLayer,needObjs , nr = 1)

        if lostObjs:
            print '---------------------'
            for lostObj in lostObjs:
                print lostObj
            print '---------------------'
            print u'===注意，以上物体，有变动，不在文件里==='
            print '---------------------'
            mc.error()

    # 视图清理
    def sk_viewConfig(self):
        cameras = mc.ls(type = 'camera')
        cameraGrps = mc.listRelatives(cameras,p=1,type = 'transform')
        for camGrp in cameraGrps:
            mc.lookThru( camGrp )
            viewPanel = mc.getPanel(withFocus = 1)
            mc.modelEditor(viewPanel,e=1,allObjects = 0)
            mc.modelEditor(viewPanel,e=1,polymeshes = 1)
            mc.modelEditor(viewPanel,e=1,lights = 1)
            mc.modelEditor(viewPanel,e=1,cameras = 1)

    # 查询一个节点的所有下游节点
    def sk_getConsNodes(self,checkNodes,st = 0,dt = 1):
        targetList = []
        if not checkNodes:
            return targetList
        consD = mc.listConnections(checkNodes,s=st,d=dt)
        while consD:
            targetList += consD
            tempConsD = mc.listConnections(consD,s=st,d=dt)
            if not tempConsD:
                tempConsD = []
            consD = []
            for checkNode in tempConsD:
                if checkNode not in targetList:
                    consD.append(checkNode)
        if targetList:
            targetList = list(set(targetList))
        return targetList

    # 修正arnold ies bug
    def checkArnoldShotFix(self):
        oldInfo = '${IDMT_PROJECTS}'
        newInfo = 'Z:/Projects'
        checkNodes = mc.ls(type = 'aiPhotometricLight',l=1)
        for checkNode in checkNodes:
            checkAttr = checkNode + '.aiFilename'
            pathNow = mc.getAttr(checkAttr)
            pathNow = pathNow.replace('\\','/')
            if oldInfo not in pathNow:
                continue
            newPath = pathNow.replace(oldInfo,newInfo)
            mc.setAttr(checkAttr,newPath,type = 'string')
