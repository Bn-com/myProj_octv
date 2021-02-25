# -*- coding: utf-8 -*-
#  Author : 沈康
#  Data   : 2016
import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_baseCommon import sk_infoCore
reload(sk_infoCore)

class sk_projTools_base(object):
    def __init__(self):
        pass

    def justCheck(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotInfos[-1] = shotInfos[-1].split('.')[0]
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        asset_type = ''
        assetTypeShort = shotInfos[1][0].lower()
        shortList = sk_infoConfig.sk_infoConfig().assetInfos
        if assetTypeShort in shortList:
            indexNum = sk_infoConfig.sk_infoConfig().assetInfos.index(assetTypeShort)
            asset_type = sk_infoConfig.sk_infoConfig().assetFullInfos[indexNum]
        print '---------[CheckPre]assetType'
        print asset_type
        project = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        print '---------[CheckPre]project'
        print project
        if asset_type:
            filename = '%s_%s_%s_%s.mb'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
        else:
            filename = '%s_%s_%s_%s_c001.mb'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3])
            if shotType == 3:
                filename = '%s_%s_%s_%s_%s_c001.mb'%(shotInfos[0],shotInfos[1],shotInfos[2],shotInfos[3],shotInfos[4])
        print '---------[CheckPre]filename'
        print filename
        if shotInfos[-1][0] in ['c'] and shotInfos[-1][0:2] not in sk_infoConfig.sk_infoConfig().cVStep:
            stepIndex = -2
        else:
            stepIndex = -1
        stepShort = shotInfos[stepIndex]
        shortList = sk_infoConfig.sk_infoConfig().simInfos
        if stepShort not in shortList:
            errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(62)
            print errorInfo
            raise
        mode = sk_infoConfig.sk_infoConfig().fullInfos[shortList.index(stepShort)]
        if mode in ['animation']:
            mode = 'anim'
        if mode in ['setdress']:
            mode = 'setDressing'
        if mode in ['finish']:
            mode = 'finishing'
        print '---------[CheckPre]mode'
        print mode
        '''
        $project            = $args[0];
        $filename           = $args[1];
        $destFolder         = $args[2];
        $copyMaps           = $args[3];
        $convert2iff        = $args[4];
        $copyHaircache      = $args[5];
        $optimizeImagePlane = $args[6];
        $progress           = $args[7];
        $optimize           = $args[8];
        $mode               = $args[9];
        $asset_type         = $args[10];
        $optimizeTx         = $args[11];
        '''
        argsList = [project,filename,'//file-cluster/GDC/Projects',0,0,0,0,100,0,mode,asset_type,0]

        argCmd = 'zjCheckinClean("5",{'
        for idNum in range(len(argsList)):
            info = argsList[idNum]
            argCmd = argCmd + '"' + str(info) + '"'
            if idNum != (len(argsList)-1):
                argCmd+=','
        argCmd += '})'

        mel.eval('putenv "IDMT_CHECKIN_TEST" "IDMT_CHECKIN_TEST";')
        mel.eval('source "//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/GDC/MEL/zjCheckinClean.mel"')
        print '----------[CheckPre]Cmd'
        print argCmd
        mel.eval(argCmd)

    #--------------------------------#
    # 修正渲染层问题
    def fixRenderLayerSwitch(self):
        mel.eval('fixRenderLayerOutAdjustmentErrors')
        sourceFileName = mc.file(exn=1,q=1).split('/')[-1]
        localPath = '%s/rlSwitchFixed'%sk_infoConfig.sk_infoConfig().localBase
        import os
        if not os.path.exists(localPath):
            mc.sysFile(localPath,makeDir = 1)
        outputPath = '%s/%s'%(localPath,sourceFileName)
        mc.file(rename = outputPath)
        mc.file(s=1,f=1)
        print '--------outputPath'
        print outputPath

    #------------------------------------#
    # 替换执行
    #---------------------------#
    # 替换参考
    def refReplacePerform(self,saveMode = 0,stepMode = 'an'):
        import os
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotID = sk_infoConfig.sk_infoConfig().checkShotID()
        projSimp = shotID.split('_')[0]
        sceneID = shotID.split('_')[1]
        shotNum = shotID.split('_')[-1]
        if projSimp in ['mi']:
            # 纠正history错误
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfos[0][0]
            refPaths = refInfos[1][0]
            needState = 0
            for idNum in range(len(refPaths)):
                checkPath  = refPaths[idNum]
                moreKey = '_gpu_'
                if moreKey not in checkPath:
                    continue
                needState = 1
                newPath = checkPath.replace(moreKey,'_')
                mc.file(newPath, loadReference = refNodes[idNum])

            if needState and saveMode:
                try:
                    mel.eval('fixRenderLayerOutAdjustmentErrors')
                except:
                    pass
                sourceFileName = mc.file(exn=1,q=1).split('/')[-1]
                localPath = '%s/refReplace'%sk_infoConfig.sk_infoConfig().localBase
                import os
                if not os.path.exists(localPath):
                    mc.sysFile(localPath,makeDir = 1)
                outputPath = '%s/%s'%(localPath,sourceFileName)
                mc.file(rename = outputPath)
                mc.file(s=1,f=1)
                print '--------outputPath'
                print outputPath
                return
        if projSimp in ['csl']:
            if sceneID in ['208','209']:
                from TEST import csl_switchAssets
                reload(csl_switchAssets)
                csl_switchAssets.switchAssetsPerform()
            if sceneID in ['213']:
                from TEST import csl_switchAssets
                reload(csl_switchAssets)
                csl_switchAssets.switchAssetsPerform({'c2903AniuCityFin':'c2904AniuFin'})
        if projSimp in ['mtd']:
            from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
            reload(sk_referenceConfig)
            refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            refNodes = refInfo[0][0]
            needState = 0
            for i in range(len(refNodes)):
                refNode = refNodes[i]
                refPath = mc.referenceQuery(refNode, f=1)
                path = refPath.lower()
                tempPath = path
                if '/rigging/' in tempPath and '_rg.m' in tempPath:
                    tempPath = tempPath.replace('/rigging/','/master/')
                    tempPath = tempPath.replace('_rg.m','_ms_anim.m')
                if '/model/' in tempPath and '_mo.m' in tempPath:
                    tempPath = tempPath.replace('/model/','/master/')
                    tempPath = tempPath.replace('_mo.m','_ms_anim.m')
                if tempPath != path and os.path.exists(tempPath):
                    needState = 1
                    mc.file(tempPath, loadReference = refNodes[i])
            if needState and saveMode:
                sourceFileName = mc.file(exn=1,q=1).split('/')[-1]
                localPath = '%s/refReplace'%sk_infoConfig.sk_infoConfig().localBase
                if not os.path.exists(localPath):
                    mc.sysFile(localPath,makeDir = 1)
                outputPath = '%s/%s'%(localPath,sourceFileName)
                mc.file(rename = outputPath)
                mc.file(s=1,f=1)
                print '--------outputPath'
                print outputPath
                return
        # 导入相机cam
        if projSimp in ['mk']:
            camRef = mc.ls('DY_CameraRig_*:*',type = 'camera')
            if camRef:
                camRef = camRef[0]
                inr = mc.referenceQuery(camRef,inr=1)
                if inr:
                    refPath = mc.referenceQuery(camRef,filename=1)
                    mc.file(refPath,importReference = 1, f = 1)
            # 开启解算
            if stepMode in ['fs']:
                controls = mc.ls('*:Master_Ctrl',type = 'transform')
                attrDict = {'.DynamicCtrlCloak':'.StartFrame','.necklaceDynamicCtrlCloak':'.necklaceStartFrame','.pantsDynamicCtrlCloak':'.pantsStartFrame'}
                for checkGrp in controls:
                    for checkKey in attrDict.keys():
                        checkAttr = checkGrp + checkKey
                        if mc.ls(checkAttr):
                            cons = mc.listConnections(checkAttr,s=1,d=0,plugs=1)
                            if cons:
                                mc.disconnectAttr(cons[0],checkAttr)
                            mc.setAttr(checkAttr,1)
                            startframeAttr = checkGrp+attrDict[checkKey]
                            cons = mc.listConnections(startframeAttr,s=1,d=0,plugs=1)
                            if cons:
                                mc.disconnectAttr(cons[0],startframeAttr)
                            mc.setAttr(startframeAttr,950)

    #------------------------------------#
    # 指定镜头ref替换
    def refReplaceCore(self,oldID = '',newID = '',changeVersion = 0,saveMode = 0):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        sourceFileName = mc.file(exn=1,q=1).split('/')[-1]
        # assetID鉴别
        if not oldID or not newID:
            return
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        refDict = {}
        newPathDict = {}
        for idNum in range(len(refPaths)):
            checkPath = refPaths[idNum]
            if '/%s/'%oldID.lower() in checkPath.lower():
                refDict[refNodes[idNum]] = checkPath
                # newPath
                newPath = checkPath.lower().replace(oldID.lower(),newID.lower())
                if changeVersion:
                    fileFolder = newPath[:-1*len(newPath.split('/')[-1])]
                    fileName = newPath.split('/')[-1].split('.')[0]
                    fileFormat = newPath.split('/')[-1].split('.')[-1]
                    newPath = '%shistory/%s_c%s.%s'%(fileFolder,fileName,self.getVersionFromNum(changeVersion),fileFormat)
                newPathDict[refNodes[idNum]] = newPath
        # replace
        for refNode in refDict.keys():
            print '--------targetRef'
            print newPathDict[refNode]
            mc.file(newPathDict[refNode], loadReference = refNode)

        if saveMode:
            localPath = '%s/refReplace'%sk_infoConfig.sk_infoConfig().localBase
            import os
            if not os.path.exists(localPath):
                mc.sysFile(localPath,makeDir = 1)
            outputPath = '%s/%s'%(localPath,sourceFileName)
            mc.file(rename = outputPath)
            mc.file(s=1,f=1)
            print '--------outputPath'
            print outputPath

    def getVersionFromNum(self,checkNum,limit=3):
        needID = ''
        for i in range(limit):
            needID += str(int(checkNum/pow(10,limit-i-1))%10)
        return needID

    #----------------------------------------#
    # 查询exr转成的png有没有丢帧 UI
    def checkLostFramesInFolderUI(self):
        # 窗口
        uiName = 'exrCheckUI'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title="Exr2PngCheck", widthHeight=(400, 300), menuBar=0 , sizeable = 0)

        mc.frameLayout(l = u'选取模式|SelectMode' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        mc.text(label = '',height = 2)
        mc.radioButtonGrp('sk_exr2pngMode',columnWidth2 = [180,180],numberOfRadioButtons  = 2,labelArray2 = [u'Exr转Png模式 |Exr To Png Mode',u'Png检测模式 |Png Check Mode'] ,select = 1,cc = 'reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sk_exr2pngSwitchPerform()')
        mc.text(label = '',height = 2)
        mc.setParent("..")

        # 源目录
        mc.frameLayout(l = u'Exr目录|Exr Folder Root' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        mc.text(label = '',height = 3)
        mc.textFieldButtonGrp('sk_exr2pngSourceFolder',columnWidth2 = [315,1],buttonCommand = 'reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sk_exr2pngFolderButton(1)',buttonLabel = u'Select  Path')
        mc.text(label = '',height = 3)
        mc.setParent("..")

        # 输出目录
        mc.frameLayout(l = u'Png目录|Png Folder Root' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        mc.text(label = '',height = 3)
        mc.textFieldButtonGrp('sk_exr2pngTargetFolder',columnWidth2 = [315,1],buttonCommand = 'reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sk_exr2pngFolderButton(2)',buttonLabel = u'Select  Path')
        mc.text(label = '',height = 3)
        mc.setParent("..")

        # 执行button
        mc.frameLayout(l = u'执行' ,collapse = 0,collapsable = 1,borderStyle = 'etchedIn')
        mc.text(label = '',height = 2)
        mc.button(label = u'======【先转后测 | 运行】【记得看信息】======',height = 35,bgc = [0.3,0.5,0.7],c = 'reload(sk_projTools_base)\nsk_projTools_base.sk_projTools_base().sk_exr2pngPerformButton()')
        mc.text(label = '',height = 2)
        mc.setParent("..")

        mc.setParent("..")

        mc.showWindow(uiName)

    # 输出路径
    def sk_exr2pngFolderButton(self,textID = 0):
        folder = mc.fileDialog2(fileMode = 3)
        if not folder:
            return
        if textID == 1:
            mc.textFieldButtonGrp('sk_exr2pngSourceFolder',e=1,text = folder[0])
        if textID == 2:
            mc.textFieldButtonGrp('sk_exr2pngTargetFolder',e=1,text = folder[0])

    # 切换运行
    def sk_exr2pngSwitchPerform(self):
        chooseMode = mc.radioButtonGrp('sk_exr2pngMode',select = 1, q = 1)
        if chooseMode == 2:
            mc.textFieldButtonGrp('sk_exr2pngSourceFolder',e=1,text = '')

    # 执行
    def sk_exr2pngPerformButton(self):
        chooseMode = mc.radioButtonGrp('sk_exr2pngMode',select = 1, q = 1)
        sourceFolder = mc.textFieldButtonGrp('sk_exr2pngSourceFolder',q=1,text = 1)
        targetFolder = mc.textFieldButtonGrp('sk_exr2pngTargetFolder',q=1,text = 1)
        convertTool = 'D:/Alias/Maya2014x64/mentalrayForMaya2014/bin/imf_copy.exe'
        # 转
        import os
        if chooseMode == 1:
            if not os.path.exists(sourceFolder):
                info = u'\n---Exr Source Path error'
                print info
                mc.error()
            batInfo = ['@echo off\n\n']
            batInfo.append('set SOURCE_DIR=%s\n'%(sourceFolder.replace('/','\\')))
            batInfo.append('set TARGET_DIR=%s\n'%(targetFolder.replace('/','\\')))
            batInfo.append('set CONVERT_TOOL=%s\n'%(convertTool.replace('/','\\')))
            batInfo.append('\nfor /r %SOURCE_DIR% %%i in (*) do if not exist %TARGET_DIR%%%~pi mkdir %TARGET_DIR%%%~pi')
            batInfo.append('\nfor /r %SOURCE_DIR% %%i in (*) do %CONVERT_TOOL% %%i %TARGET_DIR%%%~pni.png')
            batInfo.append('\npause')
            batFile = 'D:/exr2Png_Perform.bat'
            sk_infoConfig.sk_infoConfig().checkFileWrite(batFile,batInfo)
            print '\n-------------Done!'
            print batFile
            print u'少年|少女们，运行这个bat转序列吧，转完再检测！\n'
            print u'序列帧多的话，晚上或者中午休息的时候挂机转吧!!!\n'
        # 测
        if chooseMode == 2:
            self.checkLostFramesInFolder(targetFolder)

    #----------------------------------------#
    # 查询exr转成的png有没有丢帧
    def checkLostFramesInFolder(self,targetFolder):
        import  os
        searchPath = targetFolder.replace('/','\\')
        dataGet = os.popen('DIR /d %s /b /s'%(searchPath))
        getInfo = dataGet.read()
        allInfos = getInfo.split('\n')
        imgFiles = []
        allDict = {}
        for info in allInfos:
            if '.' not in info:
                continue
            if '.txt' in info:
                continue
            imgPath = info.replace('\\','/')
            imgFiles.append(imgPath)
            key = imgPath.split('/')[-1].split('.')[0]
            frameNum = int(imgPath.split('/')[-1].split('.')[1])
            imgFolder = imgPath[:-1*(len(imgPath.split('/')[-1]))]
            if key not in allDict.keys():
                allDict[key] = {'file':[imgPath],'folder':imgFolder,'frame':[frameNum]}
            else:
                allDict[key]['file'].append(imgPath)
                allDict[key]['frame'].append(frameNum)
        # 开始检测
        errorDict = {}
        for checkKey in allDict.keys():
            frameList = allDict[checkKey]['frame']
            errorList = []
            for checkNum in range(min(frameList),max(frameList)+1):
                if checkNum in frameList:
                    continue
                errorList.append(checkNum)
            if errorList:
                errorDict[checkKey] = {'lost':errorList,'folder':allDict[key]['folder']}
        errorInfos = []
        for key in errorDict.keys():
            print '\n--------------------LostInfo'
            print errorDict[key]['folder']
            print key
            print errorDict[key]['lost']
            errorInfos.append('\n--------------------LostInfo')
            errorInfos.append(errorDict[key]['folder'])
            errorInfos.append(key)
            tempInfo = ''
            for info in errorDict[key]['lost']:
                if not tempInfo:
                    tempInfo = str(info)
                else:
                    tempInfo += (','+str(info))
            errorInfos.append(str(tempInfo))
        lostInfoFile = 'D:/pngCheckLost.txt'
        sk_infoConfig.sk_infoConfig().checkFileWrite(lostInfoFile,errorInfos)
        print '\n------------------checkLostInfoFile'
        print lostInfoFile

    #-----------------------------------------------#
    # 相机外物体隐藏
    def outCamConfig(self):
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        camName = 'CAM:cam_%s_%s_baked'%(shotInfo[1],shotInfo[2])
        if shotType == 3:
            camName = 'CAM:cam_%s_%s_%s_baked'%(shotInfo[1],shotInfo[2],shotInfo[3])
        # 添加分层
        from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
        reload(sk_renderLayerCore)
        sk_renderLayerCore.sk_renderLayerCore().getObjsNotInCamera(camName)
        # 保存
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        localPath = '%sOutCamConfig'%localPath
        import os
        if not os.path.exists(localPath):
            os.makedirs(localPath)
        localFile = '%s/%s'%(localPath,fileName)
        mc.file(rename = localFile)
        mc.file(s=1,f=1)
        print '---------SaveFilePath'
        print localFile

    #-----------------------------------------------#
    # 相机小工具---临时相机
    def camSmallToolsUI(self):
        uiName = 'camSmallToolsUI'
        # 窗口
        if mc.window(uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title=u"相机小工具 | Camera Small Tools", widthHeight=(150, 120), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        # 我的规则是，import了scene类，于是这里可以直接用起来
        mc.button(w=150, h=30, bgc=[0, 0.65, 0.1], label=u'【创建】临时检测相机',
                  c='sk_projTools_base.sk_projTools_base().camTemCamCreate()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0, 0], label=u'【清理】临时检测相机',
                  c='sk_projTools_base.sk_projTools_base().camTemCamCreate(justDelete = 1)')
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow(uiName)


    # 临时相机
    def camTemCamCreate(self,justDelete = 0):
        camTemp = 'cam_temp'
        if mc.ls(camTemp):
            mc.delete(camTemp)
        if justDelete:
            return
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        # 寻找
        camList = sk_sceneTools.sk_sceneTools().sk_getProjNeedCamera()
        if not camList:
            print u'-----未找到合法相机名-----'
            mc.error()
        checkCam = camList[0]
        # 创建
        camNew = mc.duplicate(checkCam,returnRootsOnly = 1,inputConnections = 1)
        camTemp = mc.rename(camNew[0],camTemp)
        attrList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz']
        for attr in attrList:
            tempAttr = mc.connectionInfo(camTemp+attr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)
        for attr in attrList:
            tempAttr = mc.connectionInfo(camTemp+attr,gla=1)
            if tempAttr:
                mc.setAttr(tempAttr,l=0)
        mc.lookThru(camTemp)

    #-----------------------------------------------#
    # yeti补丁
    def yetiRenderFix(self):
        loadState = mc.pluginInfo('pgYetiMaya.mll',q=1,loaded=1)
        if loadState:
            addKey = 'pgYetiPreRender'
            checkAttr = 'defaultRenderGlobals.preMel'
            nowInfo = mc.getAttr(checkAttr)
            if addKey not in nowInfo:
                newInfo = '%s;%s'%(nowInfo,addKey)
                if not nowInfo:
                    newInfo = addKey
                mc.setAttr(checkAttr,newInfo,type = 'string')
        else:
            addKeys = ['pgYetiPrerender','pgYetiVRayPreRender','pgYetiVRayPostRender']
            checkAttrs = ['defaultRenderGlobals.preMel','defaultRenderGlobals.preMel','defaultRenderGlobals.postMel']
            for i in range(len(addKeys)):
                addKey = addKeys[i]
                checkAttr = checkAttrs[i]
                nowInfo = mc.getAttr(checkAttr)
                if addKey in nowInfo:
                    newInfo = '%s%s'%(nowInfo.split(addKey)[0],nowInfo.split(addKey)[-1])
                    if newInfo:
                        if newInfo[0] in [';']:
                            newInfo = newInfo[1:]
                        if newInfo[-1] in [';']:
                            newInfo = newInfo[:-1]
                    mc.setAttr(checkAttr,newInfo,type = 'string')

    #----------------------------#
    # ass配套工具
    #----------------------------#
    def projAssProxyToolsUI(self):
        # 窗口
        uiName = 'projAssProxyToolsUI'
        if mc.window(uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title="Proxy Tools", widthHeight=(150, 320), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout()
        mc.button(w=150, h=20, bgc=[0.1, 0.1, 0.1], label=u'Ass代理工具集')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'自动创建',
                  c='from idmt.maya.py_common  import GDC_proxyTools;reload(GDC_proxyTools);GDC_proxyTools.GDC_proxyTools().proxyCreatGeoAuto()')
        mc.setParent("..")

        # 行按钮
        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'重命名',
                  c='from idmt.maya.py_common  import GDC_proxyTools;reload(GDC_proxyTools);GDC_proxyTools.GDC_proxyTools().proxyRenameProxy()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'高低模切换',
                  c='from idmt.maya.py_common import GA_modSwitch;reload(GA_modSwitch);GA_modSwitch.GA_modSwitch().GA_switchModeWin()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'显示切换',
                  c='from idmt.maya.py_common import Yak_ArnoldDis;reload(Yak_ArnoldDis);Yak_ArnoldDis.Yak_ArnoldDis().Yak_ArnoldDisWin()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'动态abc替换',
                  c='from idmt.maya.py_common import GA_Effectalembic;reload(GA_Effectalembic);GA_Effectalembic.GA_Effectalembic().GA_EffectalembicUI()')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'关闭读取',
                  c='from idmt.maya.py_common import GDC_VariablePathSwitch;reload(GDC_VariablePathSwitch);GDC_VariablePathSwitch.GDC_VariablePathSwitch().YAK_aiStandSwitch(0)')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'转绝对路径',
                  c='from idmt.maya.py_common import GDC_VariablePathSwitch;reload(GDC_VariablePathSwitch);GDC_VariablePathSwitch.GDC_VariablePathSwitch().YAK_aiStandSwitch(1)')
        mc.setParent("..")

        mc.rowLayout()
        mc.button(w=150, h=30, bgc=[0, 0.4, 0.8], label=u'转变量路径',
                  c='from idmt.maya.py_common import GDC_VariablePathSwitch;reload(GDC_VariablePathSwitch);GDC_VariablePathSwitch.GDC_VariablePathSwitch().GDC_VariableSwitch(cacheFile=0,mip=0,aiStandIn=1,fileTex=0,ref=0,abc=0,aiimage=0)')
        mc.setParent("..")

        mc.setParent("..")
        mc.showWindow(uiName)

    # arnoldMatte切换
    def arnoldMatteConfig(self,value):
        objs = mc.ls(sl=1,l=1)
        meshes = []
        for checkObj in objs:
            checkType = mc.nodeType(checkObj)
            if checkType in ['mesh']:
                meshes.append(checkObj)
            else:
                checkMesh = mc.listRelatives(checkObj,s=1,ni=1,type = 'mesh',f=1)
                if checkMesh:
                    meshes.append(checkMesh[0])
        if not meshes:
            return
        # 当前渲染层
        overState = 0
        rlNow = mc.editRenderLayerGlobals( query=True, currentRenderLayer=True )
        if rlNow not in ['defaultRenderLayer']:
            overState = 1
        for checkMesh in meshes:
            meshAttr = '%s.aiMatte'%checkMesh
            if not mc.ls(meshAttr):
                continue
            if overState:
                mc.editRenderLayerAdjustment(meshAttr)
            mc.setAttr(meshAttr,value)

    # xgen渲染熟悉切换
    def selXgenPrSetting(self,value):
        selObjs = mc.ls(sl=1,l=1)
        xgenShapes = mc.listRelatives(selObjs,ad=1,type= 'xgmDescription',f=1)
        if not xgenShapes:
            return
        for checkXgen in xgenShapes:
            xgenAttr = checkXgen + '.primaryVisibility'
            mc.editRenderLayerAdjustment(xgenAttr)
            mc.setAttr(xgenAttr,value)


    #-----------------------#
    # SD文件处理
    #-----------------------#
    # 隐藏物体进层
    def sdSelHideObjs(self):
        sdLayer = 'sd_hideLayer'
        selObjs = mc.ls(sl=1)
        if not selObjs:
            return
        # 获取层
        if not mc.ls(sdLayer):
            mc.createDisplayLayer(name = sdLayer,empty=1)
        mc.setAttr(sdLayer+'.visibility',0)
        # 添加
        oldObjs = mc.editDisplayLayerMembers(sdLayer,fullNames = 1,q=1)
        if oldObjs:
            oldObjs = mc.ls(oldObjs,l=1)
        else:
            oldObjs = []
        needObjs = oldObjs
        for checkObj in selObjs:
            if checkObj not in oldObjs:
                needObjs.append(checkObj)

        mc.editDisplayLayerMembers(sdLayer,needObjs , nr = 1)

    #-----------------------#
    # 隐藏物体进set组
    def sdSelHideSets(self):
        sdSet = 'sd_hideSet'
        selFaces = mc.ls(sl=1,l=1)
        if not selFaces:
            return
        # 获取set
        oldFaces = []
        if not mc.ls(sdSet):
            mc.sets(name = sdSet,em = 1)
        else:
            oldFaces = mc.sets(sdSet,q=1)
            if oldFaces:
                oldFaces = mc.ls(oldFaces,l=1)
            else:
                oldFaces = []
        needInfos = {}
        for checkInfo in oldFaces:
            checkObj = checkInfo.split('.f[')[0]
            if checkObj not in needInfos.keys():
                needInfos[checkObj] = []
            if '.f[' not in checkInfo:
                continue
            faceNum = checkInfo.split('.f[')[-1].split(']')[0]
            if ':' in faceNum:
                minNum = int(faceNum.split(':')[0])
                maxNum = int(faceNum.split(':')[-1])
                for num in range(minNum,maxNum+1):
                    needInfos[checkObj].append(num)
            else:
                needInfos[checkObj].append(int(faceNum))
        # add new
        for selInfo in selFaces:
            checkObj = selInfo.split('.f[')[0]
            if checkObj not in needInfos.keys():
                needInfos[checkObj] = []
            if '.f[' not in selInfo:
                continue
            faceNum = selInfo.split('.f[')[-1].split(']')[0]
            if ':' in faceNum:
                minNum = int(faceNum.split(':')[0])
                maxNum = int(faceNum.split(':')[-1])
                for num in range(minNum,maxNum+1):
                    if num not in needInfos[checkObj]:
                        needInfos[checkObj].append(num)
            else:
                if faceNum not in needInfos[checkObj]:
                    needInfos[checkObj].append(faceNum)
        # 更新
        mc.sets(clear = sdSet)
        for checkObj in needInfos.keys():
            if not needInfos[checkObj]:
                mc.sets([checkObj], e=1, addElement=sdSet)
            else:
                for num in needInfos[checkObj]:
                    mc.sets(['%s.f[%s]'%(checkObj,num)],e=1,addElement=sdSet)


    #-----------------------#
    def sdDelConfig(self):
        # face
        delFaces = []
        sdSet = 'sd_hideSet'
        if mc.ls(sdSet):
            delFaces = mc.sets(sdSet,q=1)
        if delFaces:
            delFaces = mc.ls(delFaces,l=1)
        else:
            delFaces = []
        # obj
        delObjs = []
        sdLayer = 'sd_hideLayer'
        if mc.ls(sdLayer):
            delObjs = mc.editDisplayLayerMembers(sdLayer,fullNames = 1,q=1)
        if delObjs:
            delObjs = mc.ls(delObjs,l=1)
        else:
            delObjs = []
        # checkRef
        refNodes = {}
        # face
        notRefFaces = []
        refFaces = []
        for checkFace in delFaces:
            inr = mc.referenceQuery(checkFace,inr = 1)
            if not inr:
                notRefFaces.append(checkFace)
            else:
                refNode = mc.referenceQuery(checkFace,referenceNode=1)
                refFile = mc.referenceQuery(checkFace,filename=1)
                if refNode not in refNodes.keys():
                    refNodes[refNode] = refFile
                refFaces.append(checkFace)
        # obj
        notRefObjs = []
        refObjs = []
        for checkObj in delObjs:
            inr = mc.referenceQuery(checkObj,inr = 1)
            if not inr:
                notRefObjs.append(checkObj)
            else:
                refNode = mc.referenceQuery(checkObj,referenceNode=1)
                if 'CAM' in refNode[:3]:
                    continue
                refFile = mc.referenceQuery(checkObj,filename=1)
                if refNode not in refNodes.keys():
                    refNodes[refNode] = refFile
                refObjs.append(checkObj)
        # import
        for checkRef in refNodes.keys():
            refPath = refNodes[checkRef]
            mc.file(refPath,importReference = 1, f = 1)
        # del
        if notRefFaces:
            mc.select(notRefFaces)
            mc.delete()
        if refFaces:
            mc.select(refFaces)
            mc.delete()
        if notRefObjs:
            mc.delete(notRefObjs)
        if refObjs:
            mc.delete(refObjs)

    #-------------------------#
    # 删除选取物体的abc链接
    def cleanSelObjAbcCons(self):
        selObjs = mc.ls(sl=1,l=1)
        meshes = mc.listRelatives(selObjs,ad=1,type='mesh',f=1)
        if not meshes:
            meshes = []
        for checkMesh in meshes:
            cons = mc.listConnections(checkMesh,s=1,d=0,type = 'AlembicNode',plugs=1)
            if cons:
                mc.disconnectAttr(cons[0],checkMesh+'.inMesh')

    #-------------------------#
    # 多景别相机系列工具
    #-------------------------#
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


    # 相机开启 mode:0 都开启,1左眼开启,2右眼开启,-1 左右眼分割
    def stereoCamFix(self,mode = 0,testMode = 0):
        oldPreInfo = mc.getAttr('defaultRenderGlobals.imageFilePrefix')
        doneInfo = u'--------Modify Cam Done!--------'
        skipInfo = u'--------Do not need to modify--------'
        if mode in [0]:
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
            newInfo = oldPreInfo
            checkKey = 'CAM_stereoCameraLeft/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            checkKey = 'CAM_stereoCameraRight/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            if newInfo != oldPreInfo:
                mc.setAttr('defaultRenderGlobals.imageFilePrefix',newInfo,type='string')
                if not testMode:
                    mc.file(s=1,f=1)
                    print doneInfo
            else:
                print skipInfo
        if mode in [1]:
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',0)
            newInfo = oldPreInfo
            checkKey = 'CAM_stereoCameraLeft/'
            if checkKey not in newInfo:
                newInfo = checkKey + oldPreInfo
            checkKey = 'CAM_stereoCameraRight/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            if newInfo != oldPreInfo:
                mc.setAttr('defaultRenderGlobals.imageFilePrefix',newInfo,type='string')
                if not testMode:
                    mc.file(s=1,f=1)
                    print doneInfo
            else:
                print skipInfo
        if mode in [2]:
            print 111
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',0)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
            newInfo = oldPreInfo
            checkKey = 'CAM_stereoCameraLeft/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            checkKey = 'CAM_stereoCameraRight/'
            if checkKey not in newInfo:
                newInfo = checkKey + oldPreInfo
            if newInfo != oldPreInfo:
                mc.setAttr('defaultRenderGlobals.imageFilePrefix',newInfo,type='string')
                if not testMode:
                    mc.file(s=1,f=1)
                    print doneInfo
            else:
                print skipInfo
        if mode in [-1]:
            import os
            fileNow = mc.file(exn=1,q=1)
            fileName = fileNow.split('/')[-1]
            filePath = fileNow[:-1*(1+len(fileName))]
            # 左眼
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',1)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',0)
            newInfo = oldPreInfo
            checkKey = 'CAM_stereoCameraLeft/'
            if checkKey not in newInfo:
                newInfo = checkKey + oldPreInfo
            checkKey = 'CAM_stereoCameraRight/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            if newInfo != oldPreInfo:
                mc.setAttr('defaultRenderGlobals.imageFilePrefix',newInfo,type='string')
                if not testMode:
                    leftFolder = '%s/Just_Left'%filePath
                    if not os.path.exists(leftFolder):
                        os.makedirs(leftFolder)
                    newName = '%s/%s'%(leftFolder,fileName)
                    mc.file(rename = newName)
                    mc.file(s=1,f=1)
                    print doneInfo
            else:
                print skipInfo
            # 右眼
            mc.setAttr('CAM:stereoCameraLeftShape.renderable',0)
            mc.setAttr('CAM:stereoCameraRightShape.renderable',1)
            newInfo = oldPreInfo
            checkKey = 'CAM_stereoCameraLeft/'
            if checkKey in newInfo:
                newInfo = newInfo.replace(checkKey,'')
            checkKey = 'CAM_stereoCameraRight/'
            if checkKey not in newInfo:
                newInfo = checkKey + oldPreInfo
            if newInfo != oldPreInfo:
                mc.setAttr('defaultRenderGlobals.imageFilePrefix',newInfo,type='string')
                if not testMode:
                    rightFolder = '%s/Just_Right'%filePath
                    if not os.path.exists(rightFolder):
                        os.makedirs(rightFolder)
                    newName = '%s/%s'%(rightFolder,fileName)
                    mc.file(rename = newName)
                    mc.file(s=1,f=1)
                    print doneInfo
            else:
                print skipInfo