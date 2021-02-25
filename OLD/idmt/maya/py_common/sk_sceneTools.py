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

class sk_sceneTools(object):
    def __init__(self):
        # namespace清理
        # test
        pass
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 【camera工具集】
    #------------------------------#
    def sk_sceneUICameraTools(self):
        # 窗口
        if mc.window ("sk_sceneUICameraTools", ex=1):
            mc.deleteUI("sk_sceneUICameraTools", window=True)
        mc.window("sk_sceneUICameraTools", title="Camera Tools", widthHeight=(150, 120), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        # 文件asset
        mc.button(w=150 , h=30 , bgc=[0, 1, 0.2], label=(unicode('【动画】打开文件系统', 'utf8')) , c='mel.eval(\"zwAssetFile\")')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        # 我的规则是，import了scene类，于是这里可以直接用起来
        mc.button(w=150 , h=30 , bgc=[0, 1, 0.2], label=(unicode('【动画】导入音频及相机', 'utf8')) , c='sk_sceneTools.sk_sceneTools().sk_sceneImportCameraAudioFrame()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0.6, 0.2, 0.2], label=(unicode('【动画】导出最终相机', 'utf8')), c='sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate()')
        mc.setParent("..")
        # newCmd = r"zwSysFile  \"copy\" \"" + camTempPath + r"\" \"" + camServerPath + r"\" 1"

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0, 0.5, 1], label=(unicode('【通用】参考最终相机', 'utf8'))  , c='mel.eval(\'source zwCameraImportExport.mel; zwGetCameraUI;\')')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150 , h=30 , bgc=[0.6, 0.5, 0.1], label=(unicode('【动画】导出abc相机', 'utf8')), c='sk_sceneTools.sk_sceneTools().LY_CameraABC()')
        mc.setParent("..")
                
        mc.setParent("..")
        mc.showWindow("sk_sceneUICameraTools")
    
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 【Camera Bake及Update】
    #------------------------------#
    # camera导出更新
    # info 2 为 cl_xxx_xxx模式 | 3 为 yd_xxx_xxx_xxx模式 
    def sk_sceneCameraUpdate(self,batchUpadate = 0 , shotType = 2):
        import sk_referenceConfig
        reload(sk_referenceConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
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
        
        # 本地临时目录
        camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" + 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_baked.ma'
        # serve目录
        camServerBasePath = "//file-cluster/GDC/Projects/" + projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/" 
        # 需要创建目录
        # 更新server文件路径
        camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.ma'
        if shotType == 3:
            camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" + 'cam_' + shotInfo[1] + '_'+ shotInfo[2] + '_' + shotInfo[3] + '_baked.ma'
            camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_cam.ma'
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
                    mc.file(rfn=refNode , removeReference=1)
        # 检查bake相机
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        # 顺溜临时处理
        print '=' * 20 + str(shotType)
        if shotType == 3:
            camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])  + '_' + str(shotInfo[3]) 
        # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
        print '=' * 20 + camSourceName
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
        # baked camera
        camBakeName = camSourceName + '_baked'
        camSelect = 0
        shotInfos = []
        # calimero camera
        if shotInfo[0] == 'cl':
            # 清理CAMERAnamespace
            if mc.ls('CAMERA:*'):
                import sk_pyCommon
                reload(sk_pyCommon)
                sk_pyCommon.sk_pyCommon().sk_deleteNamespace('CAMERA')
            camBakeName = 'grp' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '|CAMERA'
            camSelect = 1
            shotInfos = [str(shotInfo[1]),str(shotInfo[2]),str(shotInfo[0])]
        print camBakeName
        # bakeCame
        if mc.ls(camBakeName):
            mc.delete(camBakeName)
        if needCam:
            mc.select(needCam)
        else:
            print(u'=============找不到对应镜头的CAM=============')
            mc.error(u'=============找不到对应镜头的CAM=============')
        mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
        mel.eval('zwBakeCamera')
        mc.select(camBakeName)
        # 相机Export
        import sk_hbExportCam
        reload(sk_hbExportCam)
        sk_hbExportCam.sk_hbExportCam().HbExceptSelectReCam(projectInfo , 0 , str(proStartFrame),batchUpadate,camSelect,shotInfos)
        # 输出相机
        mel.eval('zwSysFile \"copy\" \"' + camTempPath + '\" \"' + camServerPath + '\" 1')
        print u'====================成功更新camera到服务器端===================='
        # 删除bake后的相机
        mc.delete(camBakeName)
        mc.select(cl=1)
        
        # 成功代码
        return 0
    
    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【核心】 【CAM,AUDIO】       动画用导cam及音频
    #------------------------------#
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
        
    #------------------------------#    
    # 导入项目的cam
    def sk_sceneImportCamera(self,shotType = 2):
        import os
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        camProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        # 开始cam部分
        if shotType == 2:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2] +  '_' + shotInfo[3]
        # 判断摄像机在不在
        if mc.ls(camName):
            # print (unicode('==============================!!!已存在相机【%s】!!!==============================' % (str(camName)), 'utf8'))
            print (u'==============================!!!已存在相机【%s】!!!==============================' % camName)
        else:
            camPath = "//file-cluster/GDC/Projects/" + camProjectInfos + "/" + camProjectInfos + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" 
            if shotType == 2:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '.ma'
            if shotType == 3 and shotInfo[0]!='yd':
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] +'.ma'
            if shotType == 3 and shotInfo[0]=='yd':
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] +'_baked.ma'
            # 判断是否存在
            file = os.path.exists(camPath)
            if file:
                # 导入相机，清除namespace
                mc.file(camPath , i=1)
                cambake=camName+'_baked'
                mc.rename(cambake,camName)
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
                
    #------------------------------#
    #------------------------------#    
    # 导入项目的cam
    def sk_sceneImportCameraF(self,shotType = 2):
        import os
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 处理清单
        camProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        # 开始cam部分
        if shotType == 2:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            camName = 'cam_' + shotInfo[1] + '_' + shotInfo[2] +  '_' + shotInfo[3]
        # 判断摄像机在不在
        if mc.ls(camName):
            # print (unicode('==============================!!!已存在相机【%s】!!!==============================' % (str(camName)), 'utf8'))
            print (u'==============================!!!已存在相机【%s】!!!==============================' % camName)
        else:
            camPath = "//file-cluster/GDC/Projects/" + camProjectInfos + "/" + camProjectInfos + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" 
            if shotType == 2:
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '.ma'
            if shotType == 3 and shotInfo[0]!='yd':
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] +'.ma'
            if shotType == 3 and shotInfo[0]=='yd':
                camPath += 'cam_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] +'_baked.ma'
            # 判断是否存在
            file = os.path.exists(camPath)
            if file:
                # 导入相机，清除namespace
                mc.file(camPath , i=1)
                if camName+'_baked':
                    cambake=camName+'_baked'
                if mc.ls(camName+'_baked')==[] and mc.ls(camName+'_baked_'+camName+'_baked'):
                    cambake=camName+'_baked_'+camName+'_baked'
                print cambake
                mc.rename(cambake,camName)
                # print (unicode('==============================成功【导入】【%s】==============================' % (str(camName)), 'utf8'))
                print (u'==============================成功【导入】【%s】==============================' % camName)
            else:
                mc.warning(u'====================文件中缺少正确相机，请检查文件=================='% camName)
                # print (unicode('==============================成功【创建】【%s】==============================' % (str(camName)), 'utf8'))
                mc.error(u'====================文件中缺少正确相机，请检查文件=================='% camName)
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
        # 处理清单
        audioIList = []
        camProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        audioProjectInfos = sk_infoConfig.sk_infoConfig().checkProjectAudioPath(shotInfo[0])
        # 开始audio部分
        if shotInfo[0] not in audioIList:
            audios = mc.ls(type='audio')
            if audios:
                mc.delete(audios)
            audioPath = "//file-cluster/GDC/Projects/" + camProjectInfos + "/Reference/Animation_production/" + audioProjectInfos + str(shotInfo[1]) + '/Audio files/wav/'
            audioPath += shotInfo[2] + '.wav'
            # 判断是否存在
            file = os.path.exists(audioPath)
            if file:
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
    
    #------------------------------#
    # 导入起始|结束帧
    def sk_sceneImportFrame(self, configType='FPS',shotType = 2):
        # 开始镜头信息
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 命令
        if shotType == 2:
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
            if fpsFrame:
                if fpsFrame == 25:
                    mc.currentUnit(time='pal')
                if fpsFrame == 24:
                    mc.currentUnit(time='film')
                if fpsFrame == 30:
                    mc.currentUnit(time='ntsc')
            else:
                # mc.warning(unicode('==============================!!!【错误】本镜头【帧速率】【不存在】!!!==============================', 'utf8'))
                mc.warning(u'==============================!!!【错误】本镜头【帧速率】【不存在】!!!==============================')
        # frame
        if configType == 'frame':
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
            else:
                # mc.warning(unicode('==============================!!!【错误】本镜头【帧信息】【不存在】!!!==============================', 'utf8'))
                mc.warning(u'==============================!!!【错误】本镜头【帧信息】【不存在】!!!==============================')
        # 设置帧播放模式
            mc.playbackOptions(playbackSpeed=1)
        # 允许undo
            mc.undoInfo(state=True, infinity=True)
 
    #----------------------------------------------------------------------------------------------#

    #----------------------------------------------------------------------------------------------#            
    #------------------------------#
    # 【核心】 【场景文件整理】
    #------------------------------#
    # 根据参考整理文件 0 不删除多余物体，保留在OTC | 1 删除多余物体
    # finalLayout环节先清理约束再处理分组
    def sk_sceneReorganize(self, finalLayout=0):
        import sk_referenceConfig
        reload(sk_referenceConfig)
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
                        upGrp = mc.listRelatives(root,p=1,f=1)
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
                        upGrp = mc.listRelatives(root,p=1,f=1)
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
                        upGrp = mc.listRelatives(root,p=1,f=1)
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
        if mc.ls(ogNsGrp):
            import sk_pyCommon
            reload(sk_pyCommon)
            for ns in ogNsGrp:
                try:
                    sk_pyCommon.sk_pyCommon().sk_deleteNamespace(ns)
                except:
                    mc.warning(ns)
                    pass
    
    #------------------------------#
    # 【核心】 【asset 参考 namespace校正】
    #------------------------------#
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
            assetInfo = refPath.split('/')[-1].split('_')
            if len(assetInfo) < 4:
                continue
            assetName = assetInfo[0] + '_' + assetInfo[1]
            # 只有一个时
            if refPaths.count(refPath) == 1:
                refIndex = refPaths.index(refPath)
                realRefPath = mc.referenceQuery(refNodes[refIndex],filename = 1)
                newNamespace = assetName + '_' + assetInfo[2]
                # 是否加载
                isRefLoad = mc.referenceQuery(refNodes[refIndex],isLoaded = 1)
                if isRefLoad:
                    # 只处理非法名字
                    print '-------'
                    print newNamespace
                    print refNamespace[refIndex]
                    print realRefPath
                    if newNamespace != refNamespace[refIndex]:
                        try:
                            print '---000'
                            print realRefPath
                            mc.file(realRefPath,e = 1 ,ns = newNamespace)
                        except:
                            print '\n'
                            print u'======参考[%s]无法被编辑，请打开文件处理======'%(refNamespace[refIndex])
                            print u'======有重复的namespace，重复编号往大处理======'%(refNamespace[refIndex])
                            mc.error(u'======参考[%s]无法被编辑，请打开文件处理======'%(refNamespace[refIndex]))
            # 多个asset时
            else:
                allIndex = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(refPaths,refPath)
                for i in range(len(allIndex)):
                    refIndex = allIndex[i]
                    realRefPath = mc.referenceQuery(refNodes[refIndex],filename = 1)
                    newNamespace = assetName + '_' + assetInfo[2] + '_' + str(i+1)
                    if i == 0:
                        newNamespace = assetName + '_' + assetInfo[2]
                    # 是否加载
                    isRefLoad = mc.referenceQuery(refNodes[refIndex],isLoaded = 1)
                    if isRefLoad:
                        # 只处理非法名字
                        if newNamespace != refNamespace[refIndex]:
                            try:
                                print '---001'
                                print realRefPath
                                mc.file(realRefPath,e = 1 ,ns = newNamespace)
                            except:
                                print '\n'
                                print u'======参考[%s]无法被编辑，请打开文件处理======'%(refNamespace[refIndex])
                                print u'======有重复的namespace，重复编号往大处理======'%(refNamespace[refIndex])
                                mc.error(u'======参考[%s]无法被编辑，请打开文件处理======'%(refNamespace[refIndex]))
    
    #------------------------------#
    # 【核心】 【非参考 namespace 清理】
    #------------------------------#
    # 文件内非参考的namespace清理，必须在参考都加载的时候处理
    def sk_sceneNoRefNamespaceClean(self):                        
        namespaces = mc.namespaceInfo(listOnlyNamespaces = 1)  
        namespaces.remove('UI')
        namespaces.remove('shared')
        refNamespace = []
        while namespaces:
            # 备份当前默认ns
            nsNow = mc.namespaceInfo(currentNamespace = 1)
            if nsNow != ':':
                nsNow = ':' + nsNow
            # 处理所有namespace
            for ns in namespaces:
                mc.namespace(set = ':')
                ns = ':' + ns
                checkNs = ns
                objs = mc.ls(checkNs + ':*')
                if objs:
                    for obj in objs:
                        if mc.objExists(obj):
                            if not mc.referenceQuery(obj,isNodeReferenced = 1):
                                newName = obj.split(checkNs + ':')[-1]
                                mc.lockNode( obj, lock=False )
                                mc.rename(obj,newName)
                try:
                    mc.namespace(moveNamespace = [ns,':'],f = 1)
                    mc.namespace(removeNamespace = ns)
                except:
                    refNamespace.append(ns.split(':')[-1])
            # 还原ns
            mc.namespace(set = nsNow)
            namespaces = mc.namespaceInfo(listOnlyNamespaces = 1)  
            namespaces.remove('UI')
            namespaces.remove('shared')
            if refNamespace:
                for info in refNamespace:
                    if info in namespaces:
                        namespaces.remove(info)
    
    #----------------------------------------------------------------------------------------------#  

    #------------------------------#
    # 【辅助】 文件清理相关
    #------------------------------#
    
    #------------------------------#
    #【通用：清理unUsed及unknown节点及turtle节点】
    #0.通用
    #Author  : 沈  康
    #Data    : 2013_05_19
    #------------------------------#
    # 全流程用
    def checkDonotNodeCleanBase(self, unuse=1 , turtle=1):
        # 清理unusedNodes
        if unuse == 1:
            mel.eval('MLdeleteUnused')
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer') + mc.ls(type = 'ilrUIOptionsNode') +  mc.ls(type = 'ilrOptionsNode') + mc.ls(type = 'ilrBakeLayerManager')
        if turtle and turtleNodes:
            for node in turtleNodes:
                # 非参考才执行删除
                if mc.referenceQuery(node,inr = 1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)

    #------------------------------#
    # 清理无用节点
    def checkDonotNodeClean(self, unuse=1 , turtle=1):
        
        # 清理finalRender插件
        try:
            mel.eval('unloadPlugin "finalRender"')
        except:
            pass      
        
        # 清理孙望参考
        refExist = ''
        try:
            refExist = mc.referenceQuery('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/QSK_lib/QSK_model.ma',rfn=1)
        except:
            pass
        if refExist:
            mc.file(rfn=refExist , removeReference=1)
        
        # 清理unusedNodes
        if unuse == 1:
            mel.eval('MLdeleteUnused')
        # 清理未知节点
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        # 清理海龟节点
        turtleNodes = mc.ls(type='ilrBakeLayer') + mc.ls(type = 'ilrUIOptionsNode') +  mc.ls(type = 'ilrOptionsNode') + mc.ls(type = 'ilrBakeLayerManager')
        if turtle:
            if turtleNodes:
                for node in turtleNodes:
                    # 非参考才执行删除
                    if mc.referenceQuery(node,inr = 1):
                        pass
                    else:
                        if mc.ls(node):
                            mc.lockNode(node, l=0)
                            mc.delete(node)

    #------------------------------#              
    # 清理displayLayer
    def checkCleanDisplayLayers(self,layers = [],donotLayers = [],delete = 1):
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
                        # 断开连接模式
                        if delete == 1:
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
                        else:
                            if layer.lower() != 'norender':
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
    
    # 删除|加载 未勾选的参考
    def sk_sceneUnloadRefDel(self,deleteMode = 1 , reloadMode = 0):
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
                        mc.file(rfn=refInfos[0][0][i] , removeReference=1)
                        mc.warning(u'===============【清理警告】未勾选的【%s】参考被清理完毕！===============' % (refInfos[0][0][i]))
                    if reloadMode:
                        mc.file(refInfos[1][0][i], loadReference = refInfos[0][0][i])
    
    #------------------------------#
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
    def checkLockObjs(self , objs , typeNum):
        doNotLock = ['drawOverride','visibility','lodVisibility']
        allObjs = mc.listRelatives(objs,ad =1,type ='transform',f = 1)
        if allObjs:
            allObjs = allObjs + objs
        else:
            allObjs = objs
        nurbsCurvs = mc.listRelatives(objs,ad =1,ni = 1,type ='nurbsCurve',f = 1)
        nurbsObjs  = mc.listRelatives(nurbsCurvs,p =1,type ='transform',f = 1)
        if not nurbsObjs:
            nurbsObjs = []
        
        for obj in allObjs:
            if obj not in nurbsObjs:
                attrs = mc.listAttr(obj)
                for attr in attrs:
                    if attr not in doNotLock:
                        try:
                            mc.setAttr((obj+'.'+attr),l=int(typeNum))
                        except:
                            pass
                    mc.setAttr((obj + '.visibility'), l=0)
            if obj.split('|')[-1] in ['MODEL']:
                attrs = mc.listAttr(obj)
                for attr in attrs:
                    if attr not in doNotLock:
                        try:
                            mc.setAttr((obj+'.'+attr),l=int(0))
                        except:
                            pass
                    mc.setAttr((obj + '.visibility'), l=0)
    
    #------------------------------#
    # 解锁所有V
    # 解锁所有lodV
    def checkUnlockMSHV(self):
        meshes = mc.ls(type = 'mesh',l=1)
        if meshes:
            for mesh in meshes:
                grp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
                if not grp:
                    continue
                grp = grp[0]
                if mc.getAttr((grp+'.v'),l=1):
                    try:
                        mc.setAttr((grp+'.v'), l=0)
                    except:
                        pass
                if mc.getAttr((grp+'.lodVisibility'),l=1):
                    try:
                        mc.setAttr((grp+'.lodVisibility'), l=0)
                    except:
                        pass
                        
    #------------------------------#
    # 补充，解锁道具的geo组 ,需要下面的文件支持
    def checkUnlockMSHGeo(self):
        import sk_infoConfig
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        typeGeo = info[1]
        if typeGeo[0] == 'p':
            ctrls = mc.ls('*_ct_an*',type = 'transform')
            unlockObjs = ['MSH_geo', 'MSH_c_hi_proxy_','Master'] + ctrls
            for unlock in unlockObjs:
                ok = 0
                if unlock != 'MSH_c_hi_proxy_':
                    if mc.ls(unlock):
                        attrs = mc.listAttr(unlock)
                        for attr in attrs:
                            try:
                                mc.setAttr((unlock + '.' + attr), l=0)
                                ok = 1
                            except:
                                if '.' not in attr:
                                    #print(unicode('========================【%.%s】解锁失败========================' % (str(unlock), str(attr)), 'utf8'))
                                    print u'========================【%.%s】解锁失败========================' % (unlock, attr)
                                     
                                pass
                if unlock == 'MSH_c_hi_proxy_' and info[3].split('.')[0] != 'ms':
                    # 只对植物进行代理处理
                    # 加入部分set
                    if info[1][0:4] == 'p000' or info[1][0] in ['s', 'S']:
                        attrs = mc.listAttr(unlock)
                        for attr in attrs:
                            try:
                                mc.setAttr((unlock + '.' + attr), l=0)
                                ok = 1
                            except:
                                if '.' not in attr:
                                    #print(unicode('========================【%.%s】解锁失败========================' % (str(unlock), str(attr)), 'utf8'))
                                    print u'========================【%.%s】解锁失败========================' % (unlock, attr)
                                     
                                pass
                if ok == 1:
                    #print(unicode('========================【%s】解锁【成功】========================' % (str(unlock)), 'utf8'))
                    print u'========================【%s】解锁【成功】========================' % (unlock)
                     

    #----------------------------------------------------------------------------------------------#            
    #------------------------------# 
    # 【核心】 相关Set处理
    #------------------------------# 

    #------------------------------#
    # 【通用：cacheSet自动创建】
    #  0.仅在model,rig,texture通用
    #  1.含创建、更新cacheSet
    #  Author  : 沈  康
    #  Data    : 2013_05_16
    #------------------------------#


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

    #------------------------------#
    # 更新AnimSet列表 ，这个不会在mo阶段处理
    # 传递动画用nurbs曲线 要求：
    #　1.必须有属性ct_an 2.必须在MODEL组内 3.不得使用形变绑定
    def checkTransAnimSetAdd(self):
        self.checkCacheSetCreate()
        self.checkTransAnimSetCreate()
        mc.sets(cl='CTRLS')
        nodes = []
        # 属性上的
        nurbsCurves = mc.ls(type = 'nurbsCurve',l = 1)
        if nurbsCurves:
            for shape in nurbsCurves:
                curveNode = mc.listRelatives(shape,p = 1,typ = 'transform',f = 1)
                if not curveNode:
                    continue
                curveNode = curveNode[0]
                attrCurveNode = mc.listAttr(curveNode)
                if 'ct_an' in attrCurveNode:
                    nodes.append(curveNode)
        # 名字上的
        nodes = nodes + mc.ls('*_ct_an*',type = 'transform')
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
    # 【cacheSet合并处理】
    # 白海豚用，其他项目或可通用
    # 获取所有MESHES或CTRLS级别的objectSet，甄别出非正版的"CacheSetx"或"AnimSetx"，将盗版物体绑架到正版Set去
    # 加入proxy_Set处理
    #------------------------------# 
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
                # 获取盗版mesh
                meshes = mc.sets(objSet, q=1)
                if meshes:
                    mc.sets(meshes , e=1 , addElement=keyWords)
                try:
                    # 对于参考，pass
                    mc.delete(objSet)
                except:
                    pass
                
    #------------------------------# 
    # 直接全部处理好所有的set合并
    def sk_sceneSetCombineConfig(self,proType):
        import sk_smoothSet
        reload(sk_smoothSet)
        self.sk_sceneCacheAnimSetConfig('Anim',proType)
        self.sk_sceneCacheAnimSetConfig('Cache',proType)
        sk_smoothSet.sk_smoothSet().smoothSetCombine('Smooth',proType)
                
    #---------------------------------------------------#
    # 删除mr节点
    def checkMrNodesDel(self):
        fileName = mc.file(exn=1,q = 1)
        localPath = sk_infoConfig.sk_infoConfig().checkTexLocalPath()
        
        # 清理mr节点
        nodeTypes = mel.eval("pluginInfo -q -dependNode \"Mayatomr\"")
        nodes = []
        for nodeType in nodeTypes:
            nodes = nodes + mc.ls(type = nodeType)
        for node in nodes:
            if mc.ls(node):
                mc.lockNode(node,l=0)
                mc.delete(node)
                
        # 存ma
        maName = localPath + fileName.split('.')[0].split('/')[-1] + '.ma'
        print maName
        mc.file(rename = maName)
        mc.file(force=1, options="v=0", type='mayaAscii' , save=1)
        
        # 读ma文件
        fileInfos = sk_infoConfig.sk_infoConfig().checkFileRead(maName)
        newFileInfos = []
        for line in fileInfos:
            if 'requires' in line and 'Mayatomr' in line:
                continue
            newFileInfos.append(line)
        
        # 保存文件
        sk_infoConfig.sk_infoConfig().checkFileWrite(maName,newFileInfos)
        
        # 重开文件
        mc.file(f=1, new=1)
        try:
            mel.eval('unloadPlugin "Mayatomr"')
        except:
            pass
        mc.file(maName,open = 1 ,force = 1)
        # 另存mb
        mbName = localPath + fileName.split('.')[0].split('/')[-1] + '.mb'
        mc.file(rename = mbName)
        mc.file(force=1, options="v=0", type='mayaBinary' , save=1)
                
                
    #----------------------------------------------------------------------------------------------#            
    #------------------------------# 
    # 【通用：model命名检测工具】
    # 非anim转anim
    # Author  : 沈  康
    #------------------------------#
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
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 非标准参考转标准参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，model文件
            if '_mo.' in path:
                newPath = path.replace('/model/','/master/')
                newPath = newPath.replace('_mo.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，rigging文件
            if '_rg.' in path:
                newPath = path.replace('/rigging/','/master/')
                newPath = newPath.replace('_rg.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，tx文件
            if '_tx.' in path:
                newPath = path.replace('/texture/','/master/')
                newPath = newPath.replace('_tx.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，notex和tex
            if '_ms_notex.' in path:
                newPath = path.replace('_ms_notex.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
            # 转换参考，notex和tex
            if '_ms_tex.' in path:
                newPath = path.replace('_ms_tex.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
    #------------------------------#
    # anim转render  1 anim->render | 2 anim->tx
    def sk_sceneNotAnim2Render(self,transType = 1):
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
            if transType== 1:
                oldKey = '_ms_anim.'
                newKey = '_ms_render.'
                if oldKey in path:
                    newPath = path.replace(oldKey,newKey)
                    # 替换参考
                    mc.file(newPath, loadReference = refNodes[i])
            if transType== 2:
                oldKey = '_ms_anim.'
                newKey = '_tx.'
                if oldKey in path:
                    newPath = path.replace(oldKey,newKey)
                tempPath = newPath
                oldKey = 'master'
                newKey = 'texture'
                if oldKey in tempPath:
                    newPath = tempPath.replace(oldKey,newKey)
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
                
    #----------------------------------------------------------------------------------------------#            
   
    #------------------------------# 
    # 【通用：model命名检测工具】
    # 0.仅在model,rig,texture通用
    # 1.检测只有一个大组
    # 2.所有带'_'的物体是否有shape节点
    # Author  : 沈  康
    # Data    : 2013_05_16
    #------------------------------# 
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


    #------------------------------# 
    # 【通用：检测v属性】
    #  参考老赵思路：没有现成的函数，只能自己写
    # Author  : 沈  康
    # Data    :2014_02_10
    #------------------------------# 

    # 核心处理物体
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

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    #【导出camera ABC格式】
    #------------------------------#
    # info 2 为 cl_xxx_xxx模式 | 3 为 yd_xxx_xxx_xxx模式 
    def LY_CameraABC(self,batchUpadate = 0 , shotType = 2):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)       
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport') 
                     
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])       
        shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotType == 3:
            shotID = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3]
        
        anim = idmt.pipeline.db.GetAnimByFilename(shotID)
        startFrame = anim.frmStart
        endFrame = anim.frmEnd
        
        ProjectsPath = '//file-cluster/GDC/Projects/'
        camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + shotInfo[1] + "/"
        camServerBasePath =  "//file-cluster/GDC/Projects/" + projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/"
   
        camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.abc'
        camInfo=camTempPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_cam.abc'
        if shotType == 3: 
            camTempPath = "//file-cluster/GDC/Projects/" + projectInfo + "/" + projectInfo + "_Scratch/TD/SetCam/" + shotInfo[1] + "/" 
            camServerPath = camServerBasePath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_' + shotInfo[3] + '_cam.abc'
            camInfo=camTempPath + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + shotInfo[3] + '_cam.abc'
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
                    mc.file(rfn=refNode , removeReference=1)
        print u'===============removed camera reference============================'
        
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        if shotType == 3: 
            camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_' + str(shotInfo[3])
        
        # 获取真正cam 居然有|cam_102_001|cam_102_001的情况
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
        
        #ABC CAMERA开始
        if camList:           
            InfoCam="-fr" +" " + str(startFrame)+" "+str(endFrame)+" " + "-root " + camList[0] + " -file " + camInfo
            mc.AbcExport(j=InfoCam)
        # 输出相机
        mel.eval('zwSysFile \"copy\" \"' + camInfo + '\" \"' + camServerPath + '\" 1')
        print camInfo
        print camServerPath
        print u'====================成功更新camera到服务器端===================='      
        # 成功代码
        return 0