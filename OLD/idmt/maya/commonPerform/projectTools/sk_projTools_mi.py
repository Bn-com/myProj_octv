# -*- coding: utf-8 -*-
# 【通用】【mi项目工具】
#  Author : 沈康
#  Data   : 2016

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_projTools_mi(object):
    def __init__(self):
        pass

    #--------------------------------------------------------#
    # 动画检测工具 anMode : 0-ly;1-an;2-sd
    #--------------------------------------------------------#
    def checkShotDetails(self, backMode=1, returnMode=0 , printErrorMode = 1 ,preCheck = 0 , anMode = 1):
        import os
        # 参考修正
        from idmt.maya.commonPerform.projectTools import sk_projTools_base
        reload(sk_projTools_base)
        sk_projTools_base.sk_projTools_base().refReplacePerform()
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        if anMode in [0,1]:
            sk_referenceConfig.sk_referenceConfig().checkRefReplace(old = ['_ms_render.',''],replace = ['_ms_anim.',''])
        # 获取ref信息
        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 另存本地
        if not preCheck:
            localTempPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(
                server=0, infoMode=6, shotInfos=shotInfo)
            if not os.path.exists(localTempPath):
                mc.sysFile(localTempPath, makeDir=1)
            mc.file(rename=(localTempPath + mc.file(exn=1, q=1).split('/')[-1]))
            mc.file(s=1, f=1)

        errorInfoList = []

        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1,shotMode=1)
            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

        # near,mid,far 修改
        layerDict = {'near':'n','mid':'m','far':'f'}
        for checkKey in layerDict.keys():
            if mc.ls(checkKey,type = 'displayLayer'):
                continue
            if mc.ls(layerDict[checkKey],type = 'displayLayer'):
                inr = mc.referenceQuery(layerDict[checkKey],inr = 1)
                if not inr:
                    mc.rename(layerDict[checkKey],checkKey)

        print u'=====================Wrong Namespace Clean Done====================='

        # FPS
        errorList = sk_sceneTools.sk_sceneTools().sk_sceneImportFrame(
            'FPS', checkMode=1, returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList
        # frame
        if anMode:
            errorList = sk_sceneTools.sk_sceneTools().sk_sceneImportFrame(
                'frame', checkMode=1, returnMode=returnMode)
            if errorList:
                errorInfoList = errorInfoList + errorList

        print u'=====================Camera Config Done====================='

        # 检测ref
        if anMode in [1]:
            errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(
                'an', 1, returnMode=returnMode)
            if errorList:
                errorInfoList = errorInfoList + errorList

        # 检测非server参考
        errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(
            returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        print u'=====================Reference List Check Done====================='

        # 清理层和渲染层
        if anMode in [1]:
            sk_animFileCheck.sk_animFileCheck().shotDisplayLayerCheck(returnMode=returnMode,deleteMode =1 )

        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        print u'=====================DisplayLayer & RenderLayer Check Done====================='

        # 必须先检测
        #errorList = sk_animFileCheck.sk_animFileCheck().shotNoRefNodesCheck()
        #if errorList[0]:
        #    errorInfoList = errorInfoList + errorList[0]

        #print u'=====================Not Ref Check Done====================='

        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetShaderCheck(returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(assetMode = 0 ,returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        print u'=====================File Nodes Check Done====================='

        if errorInfoList and printErrorMode:
            errorInfo = u'\n--------请处理好这些错误--------'
            print errorInfo
            for errorLine in errorInfoList:
                print errorLine
            errorInfo = u'--------请处理好这些错误--------\n'
            print errorInfo
            #mc.error()

        if preCheck or (not anMode):
            return

        #-------------------------#
        #以下是处理阶段

        # display fix
        displayLayers = mc.ls(type ='displayLayer')
        for checkLayer in displayLayers:
            if checkLayer in ['defaultLayer']:
                continue
            inr = mc.referenceQuery(checkLayer,inr=1)
            if inr:
                continue
            mc.setAttr(checkLayer+'.displayType',0)

        # 处理参考
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 最优先
            # 非标准参考转标准参考
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考

                mc.file(newPath, loadReference = refNodes[i])
            # _ng_参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])

        print u'=====================参考修正完毕====================='

        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()

        print u'=====================Ref Namespace Info Fix Done====================='

        print mc.ls(type='unknown')
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')

        print u'=====================No Need Nodes Clean Done====================='
        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate=backMode,abcToggle = 1)

        print u'=====================Camera Update Done====================='

        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

        print u'=====================OutLiner ReGroup Done====================='

        mc.file(s=1, f=1)

        return errorInfoList

    #---------------------------#
    # 三景别界面 UI 系列
    #---------------------------#
    def ste3CamUI(self):
        # 窗口
        uiName = 'sk_ste3CamUi'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title=u"3 Camera Tools", widthHeight=(180, 200), menuBar=0)
        # 主界面
        mc.columnLayout()
        widthValue = 150
        heightValue = 25

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0, 0.5, 1], label=(unicode('【临时】导入景别信息', 'utf8')) , c='from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout;reload(sk_cacheFinalLayout);sk_cacheFinalLayout.sk_cacheFinalLayout().displayLayerInfoImport()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0, 0.4, 0.8], label=(unicode('【参考】转换景别相机', 'utf8')), c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().steCamesSwitchUI()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0, 1, 0.2], label=(unicode('【SD】拍屏前加载相机', 'utf8')) , c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().shotRefCamImport()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0, 0.7, 0.2], label=(unicode('【立体】激活视窗再拍屏', 'utf8')) , c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamPlayblast()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=10 , bgc=[0.1, 0.1, 0.1],label = '')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0.6, 0.2, 0.1], label=(unicode('【红背】激活视窗再拍屏', 'utf8')) , c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamPlayblast([1,0,0])')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0.2, 0.8, 0.3], label=(unicode('【绿背】激活视窗再拍屏', 'utf8')) , c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamPlayblast([0,1,0])')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=heightValue , bgc=[0.1, 0.4, 0.8], label=(unicode('【蓝背】激活视窗再拍屏', 'utf8')) , c='reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamPlayblast([0,0,1])')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=widthValue , h=10 , bgc=[0.1, 0.1, 0.1],label = '')
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow(uiName)

    # 立体相机拍屏 sd和fs要先导入非参考的相机
    def ste3CamPlayblast(self,bgColors = []):
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
        # 收集导入的相机
        camList = mc.ls('*%s*'%camSourceName,type = 'camera',l=1)
        print camList
        extraKeyList = ['near','mid','far']
        for cam in camList:
            camGrp = mc.listRelatives(cam,p=1,type = 'transform',f=1)[0]
            if camGrp.split('|')[-1] != camSourceName:
                for extraKey in extraKeyList:
                    newCamGrp = '%s_%s'%(camSourceName,extraKey)
                    if camGrp.split('|')[-1] == newCamGrp:
                        needCamList.append(camGrp)
            else:
                needCamList.append(camGrp)
        print '---CamList'
        print needCamList
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
        nmfState = 0
        for needCam in needCamList:
            needLayer = needCam.split('_')[-1]
            if needLayer in ['near','mid','far']:
                nmfState = 1
                if not mc.ls(needLayer):
                    errorInfo = u'-----没找到对应显示层:[%s]'%needLayer
                    print errorInfo
                    mc.error()
            movFile = '%s%s'%(localPath,needCam.split('|')[-1].replace('cam',shotInfo[0]))
            mc.optionVar(stringValue = ('playblastFile',movFile))
            for info in ['left','right']:
                oldFile = '%s_%s.avi'%(movFile,info)
                if not os.path.exists(oldFile):
                    continue
                os.remove(oldFile)
            oldFile = '%s.avi'%movFile
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
        print '---outputFiles'
        print oldFileList
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
        print '------------'
        print bgColors
        print needCamList
        print localPath
        if nmfState and not camKeyList:
            warningInfo = u'-----------本镜头没有发现数据库前中后信息,请核对！！！-----------'
            mc.warning(warningInfo)

    # 避免no active 预先导入相机
    def shotRefCamImport(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        shotID = '%s_%s_%s'%(shotInfo[0],shotInfo[1],shotInfo[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfo[3])
        oldCams = mc.ls('%s_near'%(shotID.replace(shotInfo[0],'cam')))
        oldCams += mc.ls('%s_mid'%(shotID.replace(shotInfo[0],'cam')))
        oldCams += mc.ls('%s_far'%(shotID.replace(shotInfo[0],'cam')))
        if oldCams:
            mc.delete(oldCams)
        camServerBase = sk_infoConfig.sk_infoConfig().checkCameraServerPath()
        camKeyList = sk_infoConfig.sk_infoConfig().checkReadShotCamData()
        if camKeyList:
            camKeyList = camKeyList.split(';')
        else:
            camKeyList = ['base']
        for camKey in camKeyList:
            if camKey == 'base':
                camServerFile = '%s%s_cam.ma'%(camServerBase,shotID)
                camTemp = '%s_baked'%(shotID.replace(shotInfo[0],'cam'))
            else:
                camServerFile = '%s%s_%s_cam.ma'%(camServerBase,shotID,camKey)
                camTemp = '%s_%s_baked'%(shotID.replace(shotInfo[0],'cam'),camKey)
            ns = 'foodTemp'
            print '-----CamServerFile'
            print camServerFile
            mc.file(camServerFile, i=1 , namespace=ns , type='mayaAscii' , preserveReferences=1 , options="v=0")
            # 删除namespace
            mc.namespace(force=1 , moveNamespace=[(':' + ns) , ':'])
            mc.namespace(removeNamespace=(':' + ns))
            if camKey == 'base':
                mc.rename(camTemp,'%s_near'%camTemp.replace('_baked',''))
            else:
                mc.rename(camTemp,camTemp.replace('_baked',''))

    #---------------------------#
    # 多景别相机切换 UI系列
    #---------------------------#
    def steCamesSwitchUI(self):
        # 窗口
        uiName = 'sk_ste3CamSwichUI'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title=u"3 Camera Tools", widthHeight=(180, 240), menuBar=0)
        # 主界面
        widthInfo = 160
        buttonH = 30
        mc.columnLayout()

        mc.rowLayout()
        mc.text(label = u'请输入镜头信息',width = widthInfo)
        mc.setParent("..")

        mc.rowLayout()
        mc.text(label = u'如mi_010_0010',width = widthInfo)
        mc.setParent("..")

        mc.rowLayout()
        mc.textField('sk_ste3CamSwichShotInfo',text = '',width = widthInfo)
        mc.setParent("..")

        mc.rowLayout()
        mc.text(label = u'空值默认取文件名',width = widthInfo)
        mc.setParent("..")

        mc.rowLayout()
        mc.button(label = u'查询服务器端Cam',bgc=[0, 0.4, 0.9],width = widthInfo,height = buttonH,c = 'reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().steCamesGetShotCamList()')
        mc.setParent("..")

        mc.rowLayout()
        mc.textScrollList('sk_ste3CamSwichList',width = widthInfo,height = 70)
        mc.setParent("..")

        mc.rowLayout()
        mc.button(label = u'选取景别切换',bgc=[0.1, .1, 0.1],width = widthInfo,height = buttonH,c = 'reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().steCamesSwitchPerform()')
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow(uiName)

    # 获取list
    def steCamesGetShotCamList(self):
        shotID = mc.textField('sk_ste3CamSwichShotInfo',q=1,text=1)
        if not shotID:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        else:
            shotInfos = shotID.split('_')
        camInfos = sk_infoConfig.sk_infoConfig().checkReadShotCamData(shotInfos)
        if not camInfos:
            camList = ['base']
        else:
            camList = camInfos.split(';')
        scrollList = 'sk_ste3CamSwichList'
        mc.textScrollList(scrollList,e=1,removeAll=1)
        for checkItem in camList:
            mc.textScrollList(scrollList,e=1,append = checkItem)

    # 更改路径
    def steCamesSwitchPerform(self):
        shotID = mc.textField('sk_ste3CamSwichShotInfo',q=1,text=1)
        if not shotID:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        else:
            shotInfos = shotID.split('_')

        scrollList = 'sk_ste3CamSwichList'
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()

        shotID = '%s_%s_%s'%(shotInfos[0],shotInfos[1],shotInfos[2])
        if shotType == 3:
            shotID = '%s_%s'%(shotID,shotInfos[3])

        camNeed = mc.textScrollList(scrollList,q=1,selectItem = 1)
        if not camNeed:
            print  u'\n------请选取需要切换的景别------'
            mc.error()
        else:
            camNeed = camNeed[0]
        camServerBase = sk_infoConfig.sk_infoConfig().checkCameraServerPath(shotInfos)
        if camNeed == 'base':
            camServerFile = '%s%s_cam.ma'%(camServerBase,shotID)
        else:
            camServerFile = '%s%s_%s_cam.ma'%(camServerBase,shotID,camNeed)
        print '----ServerCam'
        print camServerFile

        import os
        if not os.path.exists(camServerFile):
            print  u'\n------服务器端该景别文件不存在，请和立体环节沟通------'
            print camServerFile
            print camNeed
            print  u'------服务器端该景别文件不存在，请和立体环节沟通------\n'

        camRefNode = 'CAMRN'
        if not mc.ls(camRefNode,type='reference'):
            print '-----001'
            mc.file(camServerFile,reference = 1,ignoreVersion=1,namespace='CAM')
        else:
            print '-----002'
            mc.file(camServerFile, loadReference = camRefNode)

        if camNeed in ['far']:
            msCam = 'CAM:cam_010_0010_far_baked'
            camShape = mc.listRelatives(msCam,s=1,type = 'camera')[0]
            mc.setAttr('%s.farClipPlane'%camShape,80000)

        print u'\n====================切换景别成功====================\n'


    #--------------------------------#
    # fs外挂
    #--------------------------------#
    # 检测ns
    def miAssetLightMeshAbcConfig(self,ex = 0,im =0):
        refNodes = mc.ls(type = 'reference')
        needNsList = []
        for checkRefNode in refNodes:
            if ':' in checkRefNode:
                continue
            needState = 0
            if 'p001001Aerocraft' in checkRefNode:
                needState = 1
            if 'p001002AerocraftB' in checkRefNode:
                needState = 1
            if 'p001003AerocraftBroken' in checkRefNode:
                needState = 1
            if 'c024001MechanicalBeast' in checkRefNode:
                needState = 1
            if not needState:
                continue
            try:
                checkNs = mc.referenceQuery(checkRefNode,namespace=1).split(':')[-1]
                needNsList.append(checkNs)
            except:
                pass
        if not needNsList:
            return
        for ns in needNsList:
            if ex:
                self.miAssetExtraAbcExport(ns)
            if im:
                self.miAssetExtraAbcImport(ns)

    # 导出
    def miAssetExtraAbcExport(self,ns):
        if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
            mc.loadPlugin('AbcExport')
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        frame_min = mc.playbackOptions(min=True,q=True)-50
        frame_max = mc.playbackOptions(max=True,q=True) +10
        localPath = sk_infoConfig.sk_infoConfig().alembicLocalPath(2)
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(2)
        # 额外cache物体
        checkAbcGrp = self.miAssetGetExtraObjs(ns)
        if not checkAbcGrp:
            return
        # 输出abc
        abcFile = '%s_%s_extra.abc'%(shotID,ns)
        localFile = '%s%s'%(localPath,abcFile)
        serverFile = '%s%s'%(serverPath,abcFile)
        rootObjs = u' -root %s' %( u' -root '.join([checkGrp for checkGrp in checkAbcGrp]))
        mc.AbcExport(j="-frameRange %s %s -uvWrite -worldSpace -writeVisibility  %s -file %s"%(frame_min,frame_max,rootObjs,localFile))
        copyCmd = u'zwSysFile "copy" "%s" "%s" true' % (localFile,serverFile)
        mel.eval(copyCmd)
        print u'\n=========================[ABC]: [%s] Up To Server ================================\n'%abcFile

    # 导入
    def miAssetExtraAbcImport(self,ns):
        if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
            mc.loadPlugin('AbcImport')
        from idmt.maya.norch import north_alembicCommon
        reload(north_alembicCommon)
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        serverPath = sk_infoConfig.sk_infoConfig().alembicServerPath(2)
        abcFile = '%s_%s_extra.abc'%(shotID,ns)
        abcNode = '%s_%s_extra_AlembicNode'%(shotID,ns)
        # clean
        self.cleanAbcNodeInfo(abcNode)
        mc.AbcImport((serverPath + abcFile),mode='replace')
        # 赋予namespace
        self.abcMeshAddNs(ns)
        errorList = self.replaceRebuildPerform(abcNode,'extra',ns)

    # 清理以前的
    def cleanAbcNodeInfo(self,abcNode):
        if mc.ls(abcNode):
            mc.delete(abcNode)
        unitNodes = mc.ls(type = 'unitConversion')
        for checkNode in unitNodes:
            cons = mc.listConnections(checkNode,s=1,d=0)
            if not cons:
                mc.delete(checkNode)

    # ns extra objects
    def miAssetGetExtraObjs(self,ns):
        # 额外cache物体
        needNodes = []
        keyList = ['MSH_MeshLGT','MSH_Emission','LIGHTING','MSH_LIGHTING']
        for key in keyList:
            rootGrp = '%s:%s'%(ns,key)
            if mc.ls(rootGrp):
                tempNodes = mc.listRelatives(rootGrp,ad =1,type = 'mesh',f=1)
                if not tempNodes:
                    tempNodes = []
                needNodes += tempNodes
                tempNodes = mc.listRelatives(rootGrp,ad=1,type = 'aiAreaLight',f=1)
                if not tempNodes:
                    tempNodes = []
                needNodes += tempNodes
                tempNodes = mc.listRelatives(rootGrp,ad=1,type = 'light',f=1)
                if not tempNodes:
                    tempNodes = []
                needNodes += tempNodes
        checkAbcGrp = mc.listRelatives(needNodes,p=1,type = 'transform',f=1)
        return checkAbcGrp

    # 重连模式
    def replaceRebuildPerform(self,checkAbcNode = '',checkType= 'mesh',checkNs = ''):
        testMode = 1
        from idmt.maya.norch import north_alembicCommon
        reload(north_alembicCommon)
        # all transform
        sourceObjs = self.getShotAssetAbcObj(checkType,checkNs)
        # all transform
        abcObjs    = self.getReplaceAbcObj(checkType,checkNs)

        errorList = []
        # 检测不匹配情况,视情况做blendShape
        if len(sourceObjs) != len(abcObjs):
            for checkObjS in abcObjs:
                checkKeyS = checkObjS.split('|')[-1]
                checkState = 0
                for checkObjT in sourceObjs:
                    checkKeyT = checkObjT.split('|')[-1]
                    if checkKeyS == checkKeyT:
                        checkState = 1
                        break
                if checkState:
                    break
                else:
                    errorList.append(checkObjS)
            for checkObjS in sourceObjs:
                checkKeyS = checkObjS.split('|')[-1]
                checkState = 0
                for checkObjT in abcObjs:
                    checkKeyT = checkObjT.split('|')[-1]
                    if checkKeyS == checkKeyT:
                        checkState = 1
                        break
                if checkState:
                    break
                else:
                    errorList.append(checkObjS)
            if errorList:
                errorList = list(set(errorList))

        # attrlist
        abcConsObjs= mc.listConnections(checkAbcNode,d=1,plugs=1)
        abcConsObjs.remove('time1.outTime')
        tempList = []
        for abcObjAttr in abcConsObjs:
            if 'hyperLayout' in abcObjAttr:
                continue
            tempList.append(abcObjAttr)
        abcConsObjs = tempList

        if checkType in ['mesh','curve']:
            if len(abcObjs) != len(abcConsObjs):
                for checkObjS in abcObjs:
                    checkState = 0
                    checkType = mc.nodeType(checkObjS)
                    if checkType not in ['transform']:
                        checkKeyS = mc.listRelatives(checkObjS,p=1,type='transform',f=1)[0].split('|')[-1]
                    else:
                        checkKeyS = checkObjS.split('|')[-1]
                    for checkObjT in abcConsObjs:
                        checkObjT = checkObjT.split('.')[0]
                        checkType = mc.nodeType(checkObjT)
                        if checkType not in ['transform']:
                            checkKeyT = mc.listRelatives(checkObjT,p=1,type='transform',f=1)[0].split('|')[-1]
                        else:
                            checkKeyT = checkObjT.split('|')[-1]
                        if checkKeyS == checkKeyT:
                            checkState = 1
                        if checkState:
                            break
                    if not checkState and checkObjS not in errorList:
                        errorList.append(checkObjS)

        if errorList:
            print '--------------x'
            print len(sourceObjs)
            print len(abcObjs)
            print len(abcConsObjs)
            print '---------------------uTestGrpsCheck'
            print len(errorList)
            for errorObj in errorList:
                print errorObj
            if not testMode:
                mc.error()

        # 正式处理
        fixedObjs  = []
        # 变形情况
        deformInfos = []
        # 位移直接连接情况
        transInfos  = []
        # 只断,不连(rebuild使用)
        unitInfos   = []
        usedNodes   = ['unitConversion']
        for abcObjAttr in abcConsObjs:
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
            needCheckObj = ''
            for checkObj in sourceObjs:
                if abcObj in checkObj:
                    needCheckObj = checkObj
                if needCheckObj:
                    break
            if not needCheckObj:
                print '[Error]Need Check-------'
                errorInfo =  '[%s] not in render file'%abcObj
                print errorInfo
                if not testMode:
                    mc.error()
                else:
                    continue
            # 对polygon物体而言,shape节点已经不同名
            # 需要处理既有.inMesh也有属性连接的状况
            if '.inMesh' in abcObjAttr or '.create' in abcObjAttr:
                targetShape = mc.listRelatives(needCheckObj,s=1,ni=1,f=1)[0]
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

        # 处理 unitInfos
        for infos in unitInfos:
            abcSAttr = infos[0]
            abcObjAttr = infos[1]
            mc.disconnectAttr(abcSAttr,abcObjAttr)
            #mc.connectAttr(abcSAttr,abcObjAttr,f=1)
            unitNode = abcObjAttr.split('.')[0]
            if mc.ls(unitNode):
                mc.delete(unitNode)

        # blend弥补
        errorObjs = []
        if checkType in ['mesh','curve']:
            for checkObj in abcObjs:
                shape = mc.listRelatives(checkObj,s=1,f=1)
                if not shape:
                    continue
                shape = shape[0]
                cons = mc.listConnections(shape,s=1,d=0)
                if cons:
                    continue
                # target obj
                checkKey = checkObj.split('|')[-1]
                checkList = mc.ls('*%s*'%checkKey,l=1,type = 'transform')
                if len(checkList) == 1:
                    continue
                needObj = ''
                for cObj in checkList:
                    if mc.referenceQuery(cObj,inr=1):
                        needObj = cObj
                if not needObj:
                    continue
                # 若有blend连接，删除
                needShape = mc.listRelatives(needObj,s=1,ni=1,type='mesh',f=1)[0]
                blendCons = mc.listConnections(needShape,s=1,d=0,type='blendShape')
                if blendCons:
                    mc.delete(blendCons)
                #continue
                # blend
                mc.select(checkObj)
                mc.select(needObj,add= 1)
                try:
                    blendNode = mc.blendShape(frontOfChain=1)
                    if ':' in checkObj:
                        attr = checkObj.split(':')[-1]
                    else:
                        attr = checkObj.split('|')[-1]
                    mc.setAttr((blendNode[0] + '.' + attr),1)
                    #mc.select(needObj)
                    #mel.eval('DeleteHistory')
                    #mc.select(cl=1)
                except:
                    errorObjs.append(checkObj)
                    errorObjs.append(needObj)

        mc.delete(abcObjs)

        return errorObjs

    # 非参考replace物体赋予namespace
    def abcMeshAddNs(self,ns):
        checkObjs = mc.ls(type = 'mesh',l=1) + mc.ls(type = 'nurbsCurve',l=1)
        for checkObj in checkObjs:
            inr = mc.referenceQuery(checkObj,inr=1)
            if inr:
                continue
            transNode = mc.listRelatives(checkObj,p=1,type='transform',f=1)
            if not transNode:
                continue
            transNode = transNode[0]
            splitNum = len(transNode.split('|'))
            if splitNum != 2:
                continue
            if ':' in transNode:
                continue
            mc.rename(transNode,'%s:%s'%(ns,transNode.split('|')[-1]))

    # 获取指定asset的abc属性物体
    def getShotAssetAbcObj(self,checkType = 'mesh',checkNs=''):
        needObjs = []
        if checkType in ['mesh','curve']:
            if checkNs:
                checkObjs = mc.ls('%s:*'%checkNs,type = checkType,l=1)
            else:
                checkObjs = mc.ls('*:*',type = checkType,l=1)
            checkObjs = mc.listRelatives(checkObjs,p=1,type='transform',f=1)
            for checkObj in checkObjs:
                inr = mc.referenceQuery(checkObj,inr=1)
                if not inr:
                    continue
                if not mc.ls('%s.alembic'%checkObj):
                    continue
                if checkObj in needObjs:
                    continue
                needObjs.append(checkObj)
        if checkType in ['extra']:
            needObjs = self.miAssetGetExtraObjs(checkNs)
        return needObjs

    # replace模式的abc物体
    def getReplaceAbcObj(self,checkType = 'mesh',checkNs = ''):
        needObjs = []
        if checkType in ['mesh','curve']:
            if checkNs:
                checkObjs = mc.ls('%s:*'%checkNs,type = checkType,l=1)
            else:
                checkObjs = mc.ls('*:*',type = checkType,l=1)
            checkObjs = mc.listRelatives(checkObjs,p=1,type='transform',f=1)
            for checkObj in checkObjs:
                inr = mc.referenceQuery(checkObj,inr=1)
                if inr:
                    continue
                if mc.ls('%s.alembic'%checkObj):
                    continue
                if len(checkObj.split('|')) !=2:
                    continue
                if checkObj in needObjs:
                    continue
                needObjs.append(checkObj)
        if checkType in ['extra']:
            grps = mc.ls('%s:*'%checkNs,type = 'transform',l=1)
            for checkGrp in grps:
                inr = mc.referenceQuery(checkGrp,inr=1)
                if inr:
                    continue
                if len(checkGrp.split('|')) !=2:
                    continue
                needObjs.append(checkGrp)
        return needObjs


    #-----------------------------------------#
    # 处理材质球恢复
    def deformerAfterObjectSetMod(self,printState = 0):
        meshes = mc.ls(type='mesh', l=1)
        needObjs = []
        # cleanup ref
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        for refNode in refNodes:
            mc.file(cr = refNode)
        for mesh in meshes:
            if 'MODEL|' not in mesh:
                continue
            needObjs.append(mc.listRelatives(mesh, p=1, type='transform', f=1)[0])
        needObjs = list(set(needObjs))
        for obj in needObjs:
            shapes = mc.listRelatives(obj, s=1, f=1)
            if printState:
                print '--------00a'
                print shapes
            referenceShapes = [k for k in shapes if (mc.referenceQuery(k, inr=1) and mc.listConnections(k))]
            if printState:
                print '--------00b'
                print referenceShapes
            destShapes = [k for k in shapes if (not mc.referenceQuery(k, inr=1))]
            if printState:
                print destShapes
            if not referenceShapes:
                continue
            referenceShape = referenceShapes[0]
            RefShapeSG = mc.listConnections(referenceShape,d = 1, type = 'shadingEngine')
            if not RefShapeSG:
                continue
            RefShapeSG = RefShapeSG[0]
            isRef = mc.referenceQuery(RefShapeSG,isNodeReferenced = 1)
            if printState:
                print '-----00c'
                print isRef
                print RefShapeSG
            if not isRef:
                continue
            if printState:
                print '--------------00d'
                print destShapes
            for destShape in destShapes:
                #mc.sets(destShape, e=1, forceElement=RefShapeSG)
                if printState:
                    print '------00e'
                    print referenceShapes[0]
                    print destShape
                try:
                    mel.eval("deformerAfterObjectSetMod \"%s\" \"%s\";" % (referenceShapes[0], destShape))
                except Exception, e:
                    mc.sets(destShape, e=1, forceElement=RefShapeSG)
                    e

    #选中组改属性
    def modifySelAttrAiOpaque(self,turnOn = 1):
        grps = mc.ls(sl=1,l=1)
        if not grps:
            return
        meshes = mc.listRelatives(grps,ad=1,type='mesh',f=1)
        if not meshes:
            return
        checkAttr = '.intermediateObject'
        for checkMesh in meshes:
            if mc.getAttr(checkMesh+checkAttr):
                continue
            mc.setAttr((checkMesh+'.aiOpaque'),turnOn)

    #---------------------------------------------#
    # 表格处理系列
    #-------------------#
    # LYT 制作者进度
    def renderInfoGet(self,timedate = '20161212',userMode = 1,printMode = 0):
        userInfo = mel.eval('getenv "USERNAME"')
        happpInfo = 0
        if userInfo in ['shenkang']:
            happpInfo = 1
        if happpInfo:
            info = u'\n------[专用]------\n------准备开始收集啦~\n'
            print info
            info = u'\n------[燃烧工作ing...轰隆隆轰隆隆..]~\n'
            print info
        else:
            info = u'\n------[检测到非法用户...退出...开始销毁所有记录...]\n'
            print info
            return

        readData = self.readServerDailyExcel(timedate,userMode)
        renderInfoDict = readData[0]
        userInfoDict   = readData[1]

        import xlrd
        import xlwt
        from xlutils.copy import copy
        # write
        dateDict = {'201612':'_2016_Dec_Now','201701':'_2017_Jan_Now','201702':'_2017_Feb_Now','201703':'_2017_Mar_Now','201704':'_2017_Apr_Now','201705':'_2017_May_Now'}
        targetPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Sylvain/DOCS/Compo/Artists/'
        for key in dateDict.keys():
            if key in timedate:
                targetFile = targetPath + 'Follow-up_Artists' + dateDict[key] + '.xls'
        #targetFile = 'E:/Follow-up_Artists_2016_Dec_Test_old.xls'
        print targetFile
        import os
        print os.path.exists(targetFile)
        newData = xlrd.open_workbook(targetFile,formatting_info=True)
        writeData = copy(newData)
        atistList = newData.sheet_names()
        # lock num
        # artist
        writeUserDict = {}
        for num in range(len(atistList)):
            user = atistList[num]
            readInfos = newData.sheets()[num]
            writeInfos = writeData.get_sheet(num)
            if user.lower() not in userInfoDict.keys():
                continue
            infoList = userInfoDict[user.lower()]
            rlWipInfo     = [[3]]
            rlOutSideInfo = [[4]]
            rlInsideInfo  = [[5]]
            pubOKInfo     = [[6]]
            pubRenderInfo = [[7]]
            comWipInfo    = [[8]]
            comDoneInfo   = [[9]]
            comPassInfo   = [[10]]
            comRetakeInfo = [[11]]
            # dict config
            for infoDict in infoList:
                shotID = infoDict['shotID']
                checkList = ['render status bg','render status chr','fur','vol','glass']
                for checkKey in checkList:
                    if checkKey in infoDict.keys():
                        if 'outside' in infoDict[checkKey].lower():
                            if len(rlOutSideInfo) == 1:
                                rlOutSideInfo.append(shotID)
                            else:
                                rlOutSideInfo[1] += '|%s'%shotID
                        if 'inside' in infoDict[checkKey].lower():
                            if len(rlInsideInfo) == 1:
                                rlInsideInfo.append(shotID)
                            else:
                                rlInsideInfo[1] += '|%s'%shotID
                        if 'wip' in infoDict[checkKey].lower():
                            if len(rlWipInfo) == 1:
                                rlWipInfo.append(shotID)
                            else:
                                rlWipInfo[1] += '|%s'%shotID
                        if 'ok' in infoDict[checkKey].lower():
                            if len(pubOKInfo) == 1:
                                pubOKInfo.append(shotID)
                            else:
                                pubOKInfo[1] += '|%s'%shotID
                        if 'rendered' in infoDict[checkKey].lower():
                            if len(pubRenderInfo) == 1:
                                pubRenderInfo.append(shotID)
                            else:
                                pubRenderInfo[1] += '|%s'%shotID
                checkList = ['compo status']
                for checkKey in checkList:
                    if checkKey in infoDict.keys():
                        if 'wip' in infoDict[checkKey].lower():
                            if len(comWipInfo) == 1:
                                comWipInfo.append(shotID)
                            else:
                                comWipInfo[1] += '|%s'%shotID
                        if 'retake' in infoDict[checkKey].lower():
                            if len(comRetakeInfo) == 1:
                                comRetakeInfo.append(shotID)
                            else:
                                comRetakeInfo[1] += '|%s'%shotID
                        if 'ok' in infoDict[checkKey].lower():
                            if len(comPassInfo) == 1:
                                comPassInfo.append(shotID)
                            else:
                                comPassInfo[1] += '|%s'%shotID
                        if 'c' in infoDict[checkKey].lower() and 'retake' not in infoDict[checkKey].lower():
                            if len(comDoneInfo) == 1:
                                comDoneInfo.append(shotID)
                            else:
                                comDoneInfo[1] += '|%s'%shotID
            allInfoList = [rlWipInfo,rlOutSideInfo,rlInsideInfo,pubOKInfo,pubRenderInfo,comWipInfo,comDoneInfo,comPassInfo,comRetakeInfo]
            if printMode:
                print '----------userInfos'
                print user.lower()
                for info in allInfoList:
                    print info
            tempUserDict = {}
            tempUserDict['rlWipInfo'] = rlWipInfo
            tempUserDict['rlOutSideInfo'] = rlOutSideInfo
            tempUserDict['rlInsideInfo'] = rlInsideInfo
            tempUserDict['pubOKInfo'] = pubOKInfo
            tempUserDict['pubRenderInfo'] = pubRenderInfo
            tempUserDict['comWipInfo'] = comWipInfo
            tempUserDict['comRetakeInfo'] = comRetakeInfo
            tempUserDict['comPassInfo'] = comPassInfo
            tempUserDict['comDoneInfo'] = comDoneInfo
            writeUserDict[user.lower()] = tempUserDict
            # write
            timeInfos = readInfos.col_values(0)
            timeRNum = len(timeInfos)
            # 需要行数
            maxRows = []
            for checkInfo in allInfoList:
                if len(checkInfo) == 1:
                    maxRows.append(0)
                else:
                    maxRows.append(len(list(set(checkInfo[1].split('|')))))
            maxRowsNum = max(maxRows)
            # 最底层开始
            bottomRow = self.getLatestBlankLine(readInfos,timeRNum)
            # 起点行数
            if timedate in timeInfos:
                startRow = timeInfos.index(timedate)
                valueRowIndex = 0
                for checkNum in range(startRow+1,len(timeInfos)):
                    checkValue = readInfos.cell(checkNum,0).value
                    #if checkValue and checkValue not in ['N/A']:
                    if checkValue:
                        valueRowIndex = checkNum
                        break
                if not valueRowIndex:
                    valueRowIndex = bottomRow
                nowRowNums = valueRowIndex - startRow
                goAwayRows = maxRowsNum - nowRowNums
                # 覆盖原数据,并处理好偏移
                self.excelGoAway(readInfos,writeInfos,bottomRow,startRow,nowRowNums,maxRowsNum,goAwayRows)
            else:
                # 最底层开始
                startRow = bottomRow
            writeInfos.write(startRow, 0, timedate)
            for checkInfo in allInfoList:
                if len(checkInfo) == 1:
                    continue
                self.shotListToRecord(writeInfos,checkInfo,startRow)
        # save
        writeData.save(targetFile)
        if happpInfo:
            info = u'\n------[专用]------\n------(运行中...)\n------恭喜~【Artists】收集成功啦~愿你开心哈~\n'
            print '\n[File Path]:'
            print targetFile
            print info
        #return userInfoDict

    #-------------------#
    # 录入总表
    def record2Main(self,timedate,userMode=1,printMode = 0):
        userInfo = mel.eval('getenv "USERNAME"')
        happpInfo = 0
        if userInfo in ['shenkang']:
            happpInfo = 1
        if happpInfo:
            info = u'\n------[专用]------\n------准备开始收集啦~\n'
            print info
            info = u'\n------[叮叮铛铛...嗷呜...(运行中...)]~\n'
            print info
        else:
            info = u'\n------[检测到非法用户...退出...开始销毁所有记录...]\n'
            print info
            return
        readData = self.readServerDailyExcel(timedate,userMode)
        renderInfoDict = readData[0]
        userInfoDict   = readData[1]

        import xlrd
        import xlwt
        from xlutils.copy import copy
        # baseFile
        baseFile = 'Z:\Projects\MiniTiger\MiniTiger_Scratch\Sylvain\DOCS\Compo\Artists\Old\Compo MI_base.xls'
        baseFile2 = 'Z:\Projects\MiniTiger\MiniTiger_Scratch\Sylvain\DOCS\Compo\Artists\Old\Compo MI_Lost_base.xls'
        renderStateKeys = ['maya rl','maya publish','compo']
        rlKeys = ['wip','outside','inside']
        publishKeys = ['ok','rendered']
        comKeys = ['wip','c**','ok','retake']
        detailKeys = ['num','shots']
        newData = xlrd.open_workbook(baseFile,formatting_info=True)
        writeData = copy(newData)
        newData2 = xlrd.open_workbook(baseFile2,formatting_info=True)
        writeData2 = copy(newData2)
        # newData
        sheetNames = newData.sheet_names()
        for shotID in renderInfoDict.keys():
            sceneID = shotID.split('_')[0]
            shotNum = shotID.split('_')[1]
            if sceneID not in sheetNames:
                continue
            needSheetNum = 0
            for sheetNum in range(len(sheetNames)):
                if sceneID == sheetNames[sheetNum]:
                    needSheetNum = sheetNum
            readInfos = newData.sheet_by_name(sceneID)
            writeInfos = writeData.get_sheet(needSheetNum)
            titiles = readInfos.row_values(0)
            # 记录列数数据
            calDict = {}
            for checkNum in range(len(titiles)):
                checkInfo = titiles[checkNum]
                if 'shot' in checkInfo.lower():
                    calDict['shot'] = checkNum
                for checkKey in renderInfoDict[shotID].keys():
                    if checkKey in ['shotID']:
                        continue
                    if checkKey in checkInfo.lower():
                        calDict[checkKey] = checkNum
            if printMode:
                print '------'
                print shotID
                print calDict
            # row
            needRowNum = 0
            checkColInfos = readInfos.col_values(calDict['shot'])
            for iNum in range(len(checkColInfos)):
                checkColInfo = str(checkColInfos[iNum]).split('.')[0]
                if checkColInfo == shotNum:
                    needRowNum = iNum
                    break
            # write
            if not needRowNum:
                print '\n-----can not find shot info in excel'
                print shotID
                mc.error()
            for checkKey in renderInfoDict[shotID].keys():
                if checkKey in ['shotID']:
                    continue
                if checkKey not in calDict.keys():
                    continue
                writeInfos.write(needRowNum,calDict[checkKey],renderInfoDict[shotID][checkKey])
        # newData2
        needDict = {}
        for shotID in renderInfoDict.keys():
            checkDict = renderInfoDict[shotID]
            needState = 0
            for checkKey in ['render status bg','render status chr','fur','vol','glass']:
                if checkKey not in checkDict.keys():
                    continue
                checkInfo = checkDict[checkKey].lower()
                if 'ok' in checkInfo:
                    needState = 1
                if 'render' in checkInfo:
                    needState = 1
                if 'inside' in checkInfo:
                    needState = 1
                if 'outside' in checkInfo:
                    needState = 1
            if 'render missing' in checkDict.keys():
                needState = 1
            if needState:
                needDict[shotID] = checkDict
        # 填写
        titileList = newData2.sheets()[0].row_values(0)
        writeInfos2 = writeData2.get_sheet(0)
        needTitiles = ['screen','shot','artist','render status bg','render status chr','fur','vol','glass','render missing']
        titileDict = {}
        for checkNum in range(len(titileList)):
            keyInfo =  titileList[checkNum].lower()
            if keyInfo in needTitiles:
                titileDict[keyInfo] = checkNum
        shotList = needDict.keys()
        for checkIndex in range(len(shotList)):
            shotID = shotList[checkIndex]
            screenNum = shotID.split('_')[0]
            writeInfos2.write(checkIndex+1,titileDict['screen'],screenNum)
            shotNum = shotID.split('_')[1]
            writeInfos2.write(checkIndex+1,titileDict['shot'],shotNum)
            for checkKey in needTitiles:
                if checkKey in ['screen','shot']:
                    continue
                if checkKey not in needDict[shotID].keys():
                    continue
                tempInfo = needDict[shotID][checkKey]
                if not tempInfo or tempInfo.lower() in ['n/a']:
                    continue
                writeInfos2.write(checkIndex+1,titileDict[checkKey],needDict[shotID][checkKey])
        # save
        saveFile = 'Z:\Projects\MiniTiger\MiniTiger_Scratch\Sylvain\DOCS\Compo\Artists\Compo MI_%s_L.xls'%timedate
        saveFile2 = 'Z:\Projects\MiniTiger\MiniTiger_Scratch\Sylvain\DOCS\Compo\Artists\Compo MI_%s_Lost_L.xls'%timedate
        writeData.save(saveFile)
        writeData2.save(saveFile2)
        if happpInfo:
            info = u'\n------[专用]------\n------(运行中...)\n------恭喜~【日期表】收集成功啦~愿你开心哈~\n'
            print '\n[File Path]:'
            print saveFile
            print info

    #-------------------#
    # 获取信息
    def readServerDailyExcel(self,timedate,userMode = 0):
        sceneIDlist = ['010','020','030','050','080','100','110','120','125','130','135','140']
        sceneIDlist+= ['150','170','180','185','190','200','210','220','230','240','250','260','800']
        renderInfoDict = {}
        userInfoDict = {}
        serverPath = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Sylvain/DOCS/Compo'
        import os
        import xlrd
        import xlwt
        from xlutils.copy import copy
        renderStateKeys = ['render status bg','render status chr','fur','vol','glass','render missing','compo status','colorgrade status']
        renderKeyDict = {}
        baseInfoKeys = ['shot','artist']
        baseInfoDict = {}
        errorFiles = []
        # collect
        for sceneID in sceneIDlist:
            sceneFolder = serverPath+'/'+sceneID
            if not os.path.exists(sceneFolder):
                continue
            dateFolder = ''
            tempFolder = sceneFolder+'/'+ timedate
            if os.path.exists(tempFolder):
                dateFolder = tempFolder
            tempFolder = sceneFolder+'/'+ timedate[-4:]
            if os.path.exists(tempFolder):
                dateFolder = tempFolder
            if not dateFolder:
                continue
            # file list
            filelist = mc.getFileList(folder = dateFolder+'/',filespec = '*.xls')
            for checkFile in filelist:
                fileFullPath = dateFolder+'/'+checkFile
                if '~' in checkFile:
                    continue
                if '.xlsx' in checkFile:
                    errorFiles.append(fileFullPath)
                    continue
                fileData = xlrd.open_workbook(fileFullPath)
                sheetNames = fileData.sheet_names()
                needSheetNum = -1
                for sheetNum in range(len(sheetNames)):
                    if sceneID == sheetNames[sheetNum]:
                        needSheetNum = sheetNum
                if needSheetNum == -1:
                    print '\n-----Excel Sheet Info Error'
                    print fileFullPath
                    mc.error()
                writeInfos = fileData.sheets()[needSheetNum]
                titleList = writeInfos.row_values(needSheetNum)
                # keyList
                for checkInfo in titleList:
                    inState = 0
                    for checkKey in renderStateKeys:
                        if checkKey in checkInfo.lower():
                            inState = 1
                            break
                    if inState:
                        renderKeyDict[checkInfo.lower()] = titleList.index(checkInfo)
                for checkInfo in titleList:
                    if checkInfo.lower() not in baseInfoKeys:
                        continue
                    baseInfoDict[checkInfo.lower()] = titleList.index(checkInfo)
                # record
                if 'shot' not in baseInfoDict.keys():
                    print '\n-----Excel Shot Info Error'
                    print fileFullPath
                    mc.error()
                rowNums = writeInfos.nrows
                for rowID in range(1,rowNums):
                    shotNum = str(writeInfos.cell(rowID,baseInfoDict['shot']).value).split('.')[0]
                    shotID = '%s_%s'%(sceneID,shotNum)
                    tempDict = {}
                    for checkKey in renderKeyDict.keys():
                        tempInfo = writeInfos.cell(rowID,renderKeyDict[checkKey]).value
                        #if tempInfo and tempInfo != 'N/A':
                        if tempInfo:
                            tempDict[checkKey] = tempInfo
                    #artistNewDict = copy.deepcopy(tempDict)
                    if tempDict.keys():
                        artistName = writeInfos.cell(rowID,baseInfoDict['artist']).value.lower()
                        # ID
                        tempDict['artist'] = checkFile.lower().split('.')[0].split('_')[-1]
                        if userMode:
                            if artistName.lower() in checkFile.lower():
                                renderInfoDict[shotID] = tempDict
                        else:
                            renderInfoDict[shotID] = tempDict
        # artist
        for shotID in renderInfoDict.keys():
            checkInfo = renderInfoDict[shotID]
            artist = checkInfo['artist']
            checkInfo['shotID'] = shotID
            if artist not in userInfoDict.keys():
                userInfoDict[artist] = [checkInfo]
            else:
                userInfoDict[artist].append(checkInfo)
        # error
        if errorFiles:
            print u'\n------------下列excel不是2003文档，请通知制作人更改格式并移除非2003文档------------'
            for checkFile in errorFiles:
                print checkFile
                mc.error()
        return [renderInfoDict,userInfoDict]

    # 获取近的空档
    def getLatestBlankLine(self,readInfos,maxRows = 10,maxLines = 12):
        blankList = []
        for rowNum in range(maxRows):
            lastRowNum = maxRows-rowNum-1
            valueState = 0
            for lineNum in range(maxLines):
                value = readInfos.cell(lastRowNum,lineNum).value
                if not value and value not in ['N/A']:
                    valueState += 1
            if valueState == maxLines:
                blankList.append(0)
            else:
                blankList.append(1)
        needNum = 2
        for indexNum in range(len(blankList)):
            if blankList[indexNum] == 1:
                needNum = maxRows-indexNum
                break
        return needNum

    # 整体偏移
    def excelGoAway(self,readInfos,writeInfos,bottomRow,startRow,nowRowNums,maxRowsNum,goAwayRows,maxLines = 12):
        # 偏移记录
        printMode = 0
        if printMode:
            print '-------------goAwayInfo'
            print startRow
            print bottomRow
            print nowRowNums
            print maxRowsNum
            print goAwayRows
        oldDict = {}
        for rowNum in range(startRow+nowRowNums,bottomRow):
            tempDict = {}
            for lineNum in range(maxLines):
                cellValue = readInfos.cell(rowNum,lineNum).value
                tempDict[lineNum] = cellValue
            oldDict[rowNum] = tempDict
        # 覆盖
        for rowNum in range(startRow,startRow+maxRowsNum):
            for lineNum in range(maxLines):
                cellValue = readInfos.cell(rowNum,lineNum).value
                #if cellValue and cellValue not in ['N/A']:
                if cellValue:
                    writeInfos.write(rowNum, lineNum,'')
        # 偏移覆盖
        for rowNum in range(startRow+maxRowsNum,bottomRow+goAwayRows):
            for lineNum in range(maxLines):
                try:
                    writeInfos.write(rowNum, lineNum,oldDict[rowNum-goAwayRows][lineNum])
                except:
                    writeInfos.write(rowNum, lineNum,'')

    # 按镜头列表填充
    def shotListToRecord(self,writeInfos,checkInfo,startRow,addPre=0):
        shotList = checkInfo[1].split('|')
        shotList = list(set(shotList))
        for num in range(len(shotList)):
            writeInfos.write(startRow+num, addPre+checkInfo[0][0],shotList[num])

    # 特殊情况处理
    def tempShotFixA(self):
        # 开始执行
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        for i in range(len(refPaths)):
            refPath = refPaths[i]
            checkKey = 'minitiger/project/scenes/sets/s026005collapsecastledsky/texture/mi_s026005collapsecastledsky_h_tx.mb'
            if checkKey in refPath.lower():
                newKey = 'minitiger/project/scenes/sets/s026005collapsecastledsky/master/mi_s026005collapsecastledsky_h_ms_render.mb'
                newPath = refPath.lower().replace(checkKey,newKey)
                mc.file(newPath, loadReference = refNodes[i])
            checkKey = 'minitiger/minitiger_scratch/sylvain/assets/mi_s026006collapsecastleelight_h_tx.mb'
            if checkKey in refPath.lower():
                newKey = 'minitiger/project/scenes/sets/s026006collapsecastleelight/master/mi_s026006collapsecastleelight_h_ms_render.mb'
                newPath = refPath.lower().replace(checkKey,newKey)
                mc.file(newPath, loadReference = refNodes[i])
        renderLayers = mc.ls(type = 'renderLayer')
        for checkLayer in renderLayers:
            inr = mc.referenceQuery(checkLayer,inr=1)
            if inr:
                continue
            if checkLayer in ['ZDEPTH','BGTECH']:
                mc.setAttr(checkLayer+'.renderable',0)
        # 保存
        fileName = mc.file(q=1,exn=1).split('/')[-1]
        version = fileName.split('.')[0].split('_')[-1]
        versionNum = int(version[1:])
        newNum = versionNum+1
        newVersion = 'c%s'%(self.checkNum2Version(newNum,3))

        newFileName = mc.file(q=1,exn=1).replace('_%s.'%version,'_%s.'%newVersion)
        mc.file(rename = newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print newFileName
        localPath = 'D:/transferTemp/REFPATH_FIX/'
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        newFileName = fileName.replace('_%s.'%version,'_%s.'%newVersion)
        newFileName = '%s%s'%(localPath,newFileName)
        mc.file(rename = newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print newFileName

    # 特殊情况处理
    def tempShotFixB(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        sceneID = shotInfos[1]

        saveState = 1
        # 关闭渲染层
        renderLayers = mc.ls(type = 'renderLayer')
        if 'CHRCOLOR' not in renderLayers:
            saveState = 0

        if not saveState:
            return

        for checkLayer in renderLayers:
            inr = mc.referenceQuery(checkLayer,inr=1)
            if inr:
                continue
            if checkLayer in ['defaultRenderLayer','CHRCOLOR']:
                continue
            mc.setAttr(checkLayer+'.renderable',0)
        mc.setAttr('CHRCOLOR.renderable',1)

        if sceneID in ['200','210','220','230','250']:
            try:
                mel.eval('fixRenderLayerOutAdjustmentErrors')
            except:
                pass
            mel.eval('editRenderLayerGlobals -currentRenderLayer "CHRCOLOR"')
            #CAMERA (AA)
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.AASamples')
            mc.setAttr('defaultArnoldRenderOptions.AASamples', 5)
            #DIFFUSE
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIDiffuseSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples', 3)
            #GLOSSY
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIGlossySamples')
            mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples', 2)
            #REFRACTION
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIRefractionSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples', 2)
            #SSS
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GISssSamples')
            mc.setAttr('defaultArnoldRenderOptions.GISssSamples', 3)
            #VOLUME INDIRECT
            mc.editRenderLayerAdjustment('defaultArnoldRenderOptions.GIVolumeSamples')
            mc.setAttr('defaultArnoldRenderOptions.GIVolumeSamples', 2)

            # needAov
            import mtoa.aovs as aovs
            needAovName = 'msk_PLANE*'
            planeAovList = mc.ls(needAovName)
            checkKey = 'msk_PLANEMT'
            if checkKey in planeAovList:
                planeAovList.remove(checkKey)
            checkKey = 'msk_PLANETL'
            if checkKey in planeAovList:
                planeAovList.remove(checkKey)
            if planeAovList:
                planeAovNum = len(planeAovList)
                needAovName = 'msk_PLANE%s'%(planeAovNum)
            else:
                needAovName = 'msk_PLANE'
            aovs.AOVInterface().addAOV(needAovName)
            if mc.ls(needAovName):
                needAovName = aovs.AOVInterface().addAOV(needAovName)
            # SG fix
            checkAttr = 'mi_p077003LittleairplaneA_h:p077003LittleairplaneA_body14_aiStandardSG.aiCustomAOVs'
            if mc.ls(checkAttr):
                attrNumList = mc.getAttr(checkAttr,mi=1)
                for i in attrNumList:
                    aovAttr =  '%s[%s].aovName'%(checkAttr,i)
                    aovName =  mc.getAttr(aovAttr)
                    consAttr = '%s[%s].aovInput'%(checkAttr,i)
                    if aovName in [needAovName]:
                        cons = mc.listConnections(consAttr,s=1,d=0,plugs=1)
                        if cons:
                            mc.disconnectAttr(cons[0],consAttr)
                        mc.connectAttr('AAA_BLUE.outColor',consAttr,f=1)

        fileName = mc.file(q=1,exn=1).split('/')[-1]
        version = fileName.split('.')[0].split('_')[-1]
        versionNum = int(version[1:])
        newNum = versionNum+1
        newVersion = 'c%s'%(self.checkNum2Version(newNum,3))

        newFileName = mc.file(q=1,exn=1).replace('_%s.'%version,'_%s.'%newVersion)
        mc.file(rename = newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print newFileName
        localPath = 'D:/transferTemp/MT_FIX/'
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        newFileName = fileName.replace('_%s.'%version,'_%s.'%newVersion)
        newFileName = '%s%s'%(localPath,newFileName)
        mc.file(rename = newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print newFileName

    def checkNum2Version(self,vNum,rangeNum):
        version = ''
        for idNum in range(rangeNum):
            version += str(int(vNum/pow(10,(rangeNum-idNum-1))))[-1]
        return version

    # TL fur
    def fixTLFur(self):
        # rl onff
        renderLayers = mc.ls(type = 'renderLayer')
        for checkLayer in renderLayers:
            inr = mc.referenceQuery(checkLayer,inr=1)
            if inr:
                continue
            if checkLayer in ['CHRFUR']:
                value = 1
            else:
                value = 0
            mc.setAttr(checkLayer+'.renderable',value)
        # fur
        furTxFile = mc.ls('mi_c002002Teethless*:c002001Teethless_pgYetiMaya1Shape_aiHair_file2')
        if not furTxFile:
            return
        for checkNode in furTxFile:
            nodeAttr = checkNode + '.fileTextureName'
            imgPath = mc.getAttr(nodeAttr)
            if '_burned.' not in imgPath:
                newPath = imgPath.replace('.jpg','_burned.png')
                mc.setAttr(nodeAttr,newPath,type = 'string')
        # addVersion
        fileName = mc.file(q=1,exn=1).split('/')[-1]
        version = fileName.split('.')[0].split('_')[-1]
        versionNum = int(version[1:])
        newNum = versionNum+1
        newVersion = 'c%s'%(self.checkNum2Version(newNum,3))

        localPath = 'D:/transferTemp/MT_FIX/'
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        newFileName = fileName.replace('_%s.'%version,'_%s.'%newVersion)
        newFileName = '%s%s'%(localPath,newFileName)
        mc.file(rename = newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print newFileName
        print '-------------Done-------------'

    # GPS config
    def fixGPSTool(self,rlType = 'off'):
        try:
            mel.eval('loadPlugin "mtoa"')
        except:
            pass
        try:
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        except:
            pass
        mc.setAttr('defaultRenderGlobals.currentRenderer', 'arnold', type='string')
        # 下来所需的节点提前创建
        import mtoa
        mtoa.core.createOptions()
        import mtoa.cmds.registerArnoldRenderer
        mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()
        # ref
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPathes= refInfo[1][0]
        refNsList= refInfo[2][0]
        for num in range(len(refNodes)):
            refNode = refNodes[num]
            refPath = refPathes[num]
            needLoad = 0
            if '/episode_camera/' in refPath:
                needLoad = 1
            if '/p013001PositionIndicator/' in refPath:
                needLoad = 1
            if needLoad:
                mc.file(refPath, loadReference = refNode)
            else:
                mc.file(rfn=refNode , unloadReference=1)

        # smoothSetApply
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        sk_smoothSet.sk_smoothSet().smoothSetDoSmooth()

        # arnold Settings
        mc.setAttr('defaultArnoldRenderOptions.AASamples',4)
        mc.setAttr('defaultArnoldRenderOptions.GIDiffuseSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIGlossySamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GIRefractionSamples',0)
        mc.setAttr('defaultArnoldRenderOptions.GISssSamples',0)
        mc.setAttr ('defaultArnoldRenderOptions.motion_blur_enable', 1)
        #LOCK SAMPLING NOISE ARNOLD
        mc.setAttr('defaultArnoldRenderOptions.lock_sampling_noise', 1)
        #TURN OFF Abord On Error ARNOLD
        mc.setAttr('defaultArnoldRenderOptions.abortOnError', 0)
        #USE TX
        mc.setAttr('defaultArnoldRenderOptions.use_existing_tiled_textures', 1)
        # setup EXR
        mc.setAttr('defaultArnoldDriver.ai_translator', 'exr', type = 'string')
        #Half precision
        #mc.editRenderLayerAdjustment('defaultArnoldDriver.halfPrecision')
        mc.setAttr('defaultArnoldDriver.halfPrecision', 1)
        #COnfig camera renderable
        if mc.objExists('CAM*:stereoCamera*LeftShape'):
            mc.setAttr('CAM*:stereoCamera*LeftShape.renderable', 1)
            mc.setAttr('CAM*:stereoCamera*RightShape.renderable', 1)
        else:
            pass
        mc.setAttr('persp.renderable', 0)
        #SETUP MOTIONBLUR
        mc.setAttr ('CAM*:stereoCamera*LeftShape.aiShutterStart', 0.5)
        mc.setAttr ('CAM*:stereoCamera*LeftShape.aiShutterEnd', 0.5)
        mc.setAttr ('CAM*:stereoCamera*RightShape.aiShutterStart', 0.5)
        mc.setAttr ('CAM*:stereoCamera*RightShape.aiShutterEnd', 0.5)
        mc.setAttr ('defaultArnoldRenderOptions.motion_steps', 3)
        mc.setAttr ('perspShape.aiShutterStart', 0.5)
        mc.setAttr ('perspShape.aiShutterEnd', 0.5)
        #Config Clip Plane
        Camera = mc.ls('*:*baked', type = "stereoRigTransform")
        if Camera:
            for Cam in Camera:
                mc.setAttr ((Cam + '.nearClipPlane'), 0.1)
                mc.setAttr ((Cam + '.farClipPlane'), 10000)

        #Switch to L
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().checkTextureSwitch('L:')

        # turnOff RL
        renderLayers = mc.ls(type ='renderLayer')
        for checkLayer in renderLayers:
            inr = mc.referenceQuery(checkLayer,inr=1)
            if inr:
                continue
            mc.setAttr(checkLayer+'.renderable',0)

        # RL create
        gpsMeshes = mc.ls('mi_p013001PositionIndicator_*:*',type=  'mesh',l=1)
        gpsGrps = []
        if gpsMeshes:
            gpsGrps = mc.listRelatives(gpsMeshes,p=1,f=1)
        if gpsGrps:
            gpsGrps = list(set(gpsGrps))
        if not gpsGrps:
            return
        GPSRL = 'GPSOFF'
        if rlType in ['on']:
            GPSRL = 'GPSRGB'
        if mc.ls(GPSRL):
            mc.delete(GPSRL)
        mc.createRenderLayer(gpsGrps , name=GPSRL , noRecurse=1 , makeCurrent=1)

        # import shader
        if not mc.ls('ai_BLUE'):
            shaderFile = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Sylvain/ASSETS/GPS_FIX/GPS_SHADERS.mb'
            mc.file(shaderFile,i=1)

        # mesh fix
        for checkGrp in gpsGrps:
            if 'cator2_' in checkGrp:
                mc.setAttr(checkGrp+'.v',0)
            for checkNum in range(28,45):
                if 'cator%s_'%checkNum in checkGrp:
                    mc.setAttr(checkGrp+'.v',0)
            checkMesh = mc.listRelatives(checkGrp,s=1,ni=1,type = 'mesh',f=1)[0]
            checkKey = 'cator18_'
            if rlType in ['on']:
                checkKey = 'cator6_'
            if checkKey in checkGrp:
                mc.sets(checkMesh, e=1, forceElement='ai_RGBSG')
            else:
                mc.sets(checkMesh, e=1, forceElement='ai_BLACKSG')

        # save
        fileName = mc.file(q=1,exn=1).split('/')[-1]
        oldFilePath = mc.file(q=1,exn=1)[:-1*(len(fileName)+1)]
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileKey = 'GPSOFF'
        if rlType in ['on']:
            fileKey = 'GPSRGB'
        newFileName = '%s_%s_%s_%s_c001.mb'%(shotInfos[0],shotInfos[1],shotInfos[2],fileKey)
        #mc.file(rename = oldFilePath+newFileName)
        #mc.file(s=1,f=1)
        #print '--------------------'
        #print oldFilePath+newFileName
        localPath = 'D:/transferTemp/GPS_FIX/'
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        mc.file(rename = localPath + newFileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print localPath + newFileName

    def tlFurBurnedFix(self):

        #Create AOVFUR
        if mc.objExists('*Teethless_h*:CHR') or mc.objExists('*Minitiger_h*:CHR'):
            from idmt.maya.commonPerform.renderLayers import zb_renderLayer_mi
            reload(zb_renderLayer_mi)
            zb_renderLayer_mi.zb_renderLayer_mi().mi_MTXFurCreate()

        if mc.objExists('*Teethless_h*:CHR'):
            asset4KList = ['mi_c002']
            fileNodes = mc.ls('mi_c002*:c002001Teethless_pgYetiMaya1Shape_aiHair_file2')
            for checkNode in fileNodes:
                needState = 0
                for checkAsset in asset4KList:
                    if checkAsset in checkNode:
                        needState = 1
                if not needState:
                    continue
                checkAttr = '.fileTextureName'
                checkType = mc.nodeType(checkNode)
                if checkType in ['aiImage']:
                    checkAttr = '.filename'
                checkPath = mc.getAttr(checkNode+checkAttr)
                keyInfo = '_2k.jpg'
                replaceInfo = '_2k_burned.png'
                if keyInfo in checkPath:
                    newPath = checkPath.replace(keyInfo,replaceInfo)
                    mc.setAttr(checkNode+checkAttr,newPath,type = 'string')
                keyInfo = '_2k.jpg'
                replaceInfo = '_2k_burned.png'
                if keyInfo in checkPath:
                    newPath = checkPath.replace(keyInfo,replaceInfo)
                    mc.setAttr(checkNode+checkAttr,newPath,type = 'string')

    def check2kSwitch4kFix(self,rlFix = 0,aovFix = 0):
        fileNodes = mc.ls(type = 'file') + mc.ls(type = 'aiImage')
        asset4KList = ['mi_c','mi_p']
        for checkNode in fileNodes:
            needState = 0
            for checkAsset in asset4KList:
                if checkAsset in checkNode:
                    needState = 1
            if not needState:
                continue
            checkAttr = '.fileTextureName'
            checkType = mc.nodeType(checkNode)
            if checkType in ['aiImage']:
                checkAttr = '.filename'
            checkPath = mc.getAttr(checkNode+checkAttr)
            keyInfo = '_4k_half'
            replaceInfo = '_4k'
            if keyInfo in checkPath:
                newPath = checkPath.replace(keyInfo,replaceInfo)
                mc.setAttr(checkNode+checkAttr,newPath,type = 'string')
        if rlFix:
            renderLayers = mc.ls(type = 'renderLayer')
            for checkRL in renderLayers:
                inrState = mc.referenceQuery(checkRL,inr=1)
                if inrState:
                    continue
                checkAttr = '%s.renderable'%checkRL
                if checkRL in ['CHRCOLOR']:
                    mc.setAttr(checkAttr,1)
                else:
                    mc.setAttr(checkAttr,0)
        if aovFix:
            if mc.ls('CHRCOLOR'):
                aovList = mc.ls(type = 'aiAOV')
                try:
                    mel.eval('fixRenderLayerOutAdjustmentErrors')
                except:
                    pass
                mc.editRenderLayerGlobals(currentRenderLayer = 'CHRCOLOR')
                keepList = ['aiAOV_direct_specular','aiAOV_indirect_specular']
                for checkAov in aovList:
                    inrState = mc.referenceQuery(checkAov,inr=1)
                    if inrState:
                        continue
                    if checkAov not in keepList:
                        mc.setAttr('%s.enabled'%checkAov,0)
        fileName = mc.file(q=1,exn=1).split('/')[-1]
        localPath = 'D:/transferTemp/fix4K/'
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        mc.file(rename = localPath + fileName)
        mc.file(s=1,f=1)
        print '--------------------'
        print localPath + fileName

    #改木刀
    def woodBlade(self,saveMode = 1 ):
        shaderRoot = 'Z:/Projects/MiniTiger/MiniTiger_Scratch/Render/ToS/180'
        assetShaderDict = {'p063001':'ChangDao_shader.mb','p064001':'DuanDao_shader.mb','p065001':'HuixuanDao_shader.mb'}
        modifyState = 0
        # 回到masterLayer
        try:
            mel.eval('fixRenderLayerOutAdjustmentErrors')
        except:
            pass
        mc.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
        # yeti处理
        yetiNodes = mc.ls(type = 'pgYetiMaya')
        oldKey = 'Y:/WOQB/Projects'
        newKey = 'Z:/Projects/MiniTiger/Project/External/WOQB'
        for yetiNode in yetiNodes:
            txNodes = mc.pgYetiGraph(yetiNode,listNodes= 1, type = 'texture')
            if not txNodes:
                continue
            for checkTxNode in txNodes:
                oldPath = mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name', getParamValue = 1)
                if oldKey in oldPath:
                    modifyState = 1
                    newPath = oldPath.replace(oldKey,newKey)
                    mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name', setParamValueString = newPath)
        renderMeshes = []
        # p063001
        assetKey = 'MSH_c_hi_p063001Sword6_'
        transGrp = mc.ls('*:%s'%assetKey,type = 'transform',l=1)
        if not transGrp:
            transGrp = mc.ls('*%s'%assetKey,type = 'transform',l=1)
        if transGrp:
            modifyState = 1
            needMeshes = mc.listRelatives(transGrp,ad = 1,type = 'mesh',f=1)
            if needMeshes:
                # 清理
                needShader = 'ChangDao_temp_Shader'
                needSG = 'ChangDao_temp_ShaderSG'
                checkShader = mc.ls(needShader,type = 'aiStandard')
                if checkShader:
                    mc.delete(checkShader)
                checkSGNode = mc.ls(needSG,type = 'shadingEngine')
                if checkSGNode:
                    mc.delete(checkSGNode)
                # 导入
                shaderFile = '%s/%s'%(shaderRoot,assetShaderDict['p063001'])
                mc.file(shaderFile,i=1)
                # 赋予材质
                mc.sets(needMeshes,e=1,forceElement=needSG)
                renderMeshes += needMeshes
        # p064001
        assetKey = 'MSH_c_hi_p064001BroadSword2_'
        transGrp = mc.ls('*:%s'%assetKey,type = 'transform',l=1)
        if not transGrp:
            transGrp = mc.ls('*%s'%assetKey,type = 'transform',l=1)
        if transGrp:
            modifyState = 1
            needMeshes = mc.listRelatives(transGrp,ad = 1,type = 'mesh',f=1)
            if needMeshes:
                # 清理
                needShader = 'DuanDao_temp_Shader'
                needSG = 'DuanDao_temp_ShaderSG'
                checkShader = mc.ls(needShader,type = 'aiStandard')
                if checkShader:
                    mc.delete(checkShader)
                checkSGNode = mc.ls(needSG,type = 'shadingEngine')
                if checkSGNode:
                    mc.delete(checkSGNode)
                # 导入
                shaderFile = '%s/%s'%(shaderRoot,assetShaderDict['p064001'])
                mc.file(shaderFile,i=1)
                # 赋予材质
                mc.sets(needMeshes,e=1,forceElement=needSG)
                renderMeshes += needMeshes
        # p065001
        transGrp = []
        keyListA = ['3','4','5','6']
        keyListB = ['12','13','14','15']
        numList = ['0','1','2','3','4','5','6','7','8','9']
        tempGrps = mc.ls('*MSH_c_hi_*Dart*',type = 'transform',l=1)
        if tempGrps:
            for checkGrp in tempGrps:
                maxL = len(checkGrp)
                offsetNum = 0
                if checkGrp[-1] in ['_']:
                    offsetNum = 1
                if checkGrp[maxL-(2+offsetNum)] in numList:
                    if checkGrp[maxL-(2+offsetNum):maxL-(offsetNum)] in keyListB:
                        transGrp.append(checkGrp)
                else:
                    if checkGrp[maxL-(1+offsetNum):maxL-(offsetNum)] in keyListA:
                        transGrp.append(checkGrp)
        if transGrp:
            modifyState = 1
            needMeshes = mc.listRelatives(transGrp,ad = 1,type = 'mesh',f=1)
            if needMeshes:
                # 清理
                needShader = 'HuixuanDao_temp_Shader'
                needSG = 'HuixuanDao_temp_ShaderSG'
                checkShader = mc.ls(needShader,type = 'aiStandard')
                if checkShader:
                    mc.delete(checkShader)
                checkSGNode = mc.ls(needSG,type = 'shadingEngine')
                if checkSGNode:
                    mc.delete(checkSGNode)
                # 导入
                shaderFile = '%s/%s'%(shaderRoot,assetShaderDict['p065001'])
                mc.file(shaderFile,i=1)
                # 赋予材质
                mc.sets(needMeshes,e=1,forceElement=needSG)
                renderMeshes += needMeshes
        # 其他物体matte
        allMeshes = mc.ls(type = 'mesh',l=1)
        for checkMesh in allMeshes:
            if checkMesh in renderMeshes:
                continue
            meshAttr = checkMesh + '.aiMatte'
            if mc.ls(meshAttr):
                mc.setAttr(meshAttr,1)
        if modifyState:
            fileName = mc.file(q=1,exn=1).split('/')[-1]
            localPath = 'D:/transferTemp/woodBlade/'
            import os
            if not os.path.exists(localPath):
                os.makedirs(localPath)
            mc.file(rename = localPath + fileName)
            mc.file(s=1,f=1)
            print '--------------------'
            print localPath + fileName


