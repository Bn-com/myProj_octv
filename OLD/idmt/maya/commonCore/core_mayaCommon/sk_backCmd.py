# -*- coding: utf-8 -*-

# import sys
# sys.path.append('D:\\food\pyp\common')


# Q:an标记是_an_还是_ca_
# A:_ct_an

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式
# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import re
import maya.cmds as mc
import maya.mel as mel
import sk_infoConfig
reload(sk_infoConfig)

class sk_backCmd(object):

    def __init__(self):
        # namespace清理
        self.pointLimit = -3

    #------------------------------------------------#
    # rg,tx输出anim系列 rg参考mo版
    #-------------------------------#
    #-------------------------------#
    # render系列之
    # rg -> anim
    # chr,prp,有tx的set用
    # modclear 为0时不清理双重MODEL组，为1时清理双重MODEL组
    #-------------------------------#
    def checkRg2Anim(self,checkIn = 1,backMode = 1,setMode = 1,assetSpecial = 0,modclear=0,abcByns = 1):
        # 参考处理
        rgMode = sk_infoConfig.sk_infoConfig().checkRgMode()
        if rgMode:
            self.checkRgRefConfig()
        # 生成处理
        self.checkAniRndCore(checkIn=checkIn,returnOpen=backMode,setMode=setMode,assetSpecial=assetSpecial,exMode = 'anim',imMode = 'rg',modclear=modclear,abcByns = abcByns)

    #-------------------------------#
    # render系列之
    # tx -> anim
    # 无rg的set使用
    #-------------------------------#
    def checkTx2Anim(self,checkIn = 1,backMode = 1,setMode = 1,assetSpecial = 0,abcByns = 1):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        rgMode = 0
        cleanShader = 0
        if setMode:
            rgMode = 1
            if shotInfos[0] in ['csl']:
                cleanShader = 1
        # 生成处理
        if rgMode:
            self.checkAniRndCore(checkIn=checkIn,returnOpen=backMode,setMode=setMode,assetSpecial=assetSpecial,exMode = 'anim',imMode = 'tx',cleanShader = cleanShader,abcByns = abcByns)

    #-------------------------------#
    # render系列之
    # rg -> render
    # 有rg的set使用
    #-------------------------------#
    def checkRg2Render(self,checkIn = 1,backMode = 1,setMode = 1,assetSpecial = 0,abcByns = 1):
        # 参考处理
        self.checkRgRefConfig()
        rgMode = sk_infoConfig.sk_infoConfig().checkRgMode()
        if rgMode:
            # 处理
            self.checkAniRndCore(checkIn=checkIn,returnOpen=backMode,setMode=setMode,assetSpecial=assetSpecial,exMode = 'render',imMode = 'rg',abcByns = abcByns)

    #-------------------------------#
    # render系列之
    # tx -> render
    # chr,prp,无rg的set使用
    #-------------------------------#
    def checkTx2Render(self,checkIn = 1,backMode = 1,setMode = 0,assetSpecial = 0,abcByns = 1):
        # 生成处理
        self.checkAniRndCore(checkIn=checkIn,returnOpen=backMode,setMode=setMode,assetSpecial=assetSpecial,exMode = 'render',imMode = 'tx',abcByns = abcByns )

    #-------------------------------#
    # reference 转向
    #-------------------------------#
    def checkRgRefConfig(self):
        import sk_checkTools
        reload(sk_checkTools)
        # check
        sk_checkTools.sk_checkTools().checkMeshRenderStates(errorMode=1)
        # 参考指向tx
        refNodes = mc.ls(type = 'reference')
        import os
        if not refNodes:
            return
        # 参考转向
        for rfNode in refNodes:
            try:
                refPath = mc.referenceQuery(rfNode,filename = 1)
                # 有则替换
                if '/texture/' not in refPath and '_tx.' not in refPath:
                    targetPath = refPath.replace('/model/','/texture/')
                    targetPath = targetPath.replace('_mo.','_tx.')
                    if os.path.exists(targetPath):
                        mc.file(targetPath,loadReference = rfNode)
            except:
                mc.lockNode(rfNode,l=0)
                mc.delete(rfNode)
        # 刷新材质球
        self.deformerAfterObjectSetMod()
        # 参考导入
        refNodes = mc.ls(type = 'reference')
        errorRefs = []
        for rfNode in refNodes:
            try:
                refPath = mc.referenceQuery(rfNode,filename = 1)
                # 参考导入
                mc.file(refPath,importReference = 1, f = 1)
            except:
                if '_UNKNOWN_' in rfNode:
                    errorRefs.append(rfNode)
        for errorRef in errorRefs:
            mc.lockNode(errorRef, l=0)
            mc.delete(errorRef)

    #-------------------------------#
    # 传UV~
    #-------------------------------#
    def checkRgUvTransfer(self):
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        shotInfo = fileName.split('_')
        assetID = fileName.split('_')[1]
        assetType = 'characters'
        if assetID[0] in ['p','P']:
            assetType = 'props'
        if assetID[0] in ['s','S']:
            return
        if shotInfo[0] in ['csl']:
            if assetID in ['c3404JunjieChildren']:
                return
        assetOtherFolder = '/texture/'
        assetOtherKey = '_tx'
        masterFolderPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        masterFolderPath = masterFolderPath + 'scenes/' + assetType + '/' + assetID + assetOtherFolder
        # 首先查询是否存在另一半文件,不存在则pass
        fileOther = masterFolderPath + shotInfo[0] + '_' + assetID + '_' + shotInfo[2] + assetOtherKey + '.' + fileName.split('.')[-1]
        mel.eval('source "//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/GDC/MEL/zjApplyMaterial.mel"')
        cmd = 'TransferUVMatBackgroundMode "%s" 1;'%fileOther
        print cmd
        mel.eval(cmd)
        localPath = sk_infoConfig.sk_infoConfig().localBase
        mc.sysFile(localPath, makeDir=True)
        localFile = '%s/%s'%(localPath,fileName)
        mc.file(rename = localFile)
        mc.file(s=1,f=1)

    #-------------------------------#
    # anim render生成核心函数
    #-------------------------------#
    def checkAniRndCore(self,checkIn = 1,returnOpen = 1,setMode = 0,assetSpecial = 0,exMode = 'render',imMode = 'tx',cleanShader = 0,modclear=0,abcByns = 1,printMode = 0):
        fileNow = mc.file(exn=1,q=1)
        localPath = sk_infoConfig.sk_infoConfig().checkTexLocalPath()
        if localPath not in fileNow:
            fileNow = '%s%s'%(localPath,fileNow.split('/')[-1])
            mc.file(rename = fileNow)
        mc.file(s=1,f=1)
        import sk_smoothSet
        reload(sk_smoothSet)
        import sk_sceneTools
        reload(sk_sceneTools)
        printMode = 1
        import time
        if printMode:self.testDef('---[Trans]:[%s]---001'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 临时测试处理
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfos[0] in ['mtd']:
            if 'cTest' in shotInfos[1]:
                abcByns = 2
            if 'pTest' in shotInfos[1]:
                abcByns = 2
            if 'sTest' in shotInfos[1]:
                abcByns = 2
        # 额外非MODEL组abc物体
        notModelAbcObjs = []
        meshes = mc.ls(type = 'mesh',l=1)
        for checkMesh in meshes:
            if '|MODEL' in checkMesh:
                continue
            objGrp = mc.listRelatives(checkMesh,p=1,f=1)
            if not objGrp:
                continue
            objGrp = objGrp[0]
            if not mc.ls(objGrp+'.alembic'):
                continue
            if objGrp not in notModelAbcObjs:
                notModelAbcObjs.append(objGrp)

        # MODEL物体清理历史

        if exMode in ['render'] and not setMode:
            self.checkMODELUnlock()
            if abcByns in [2]:
                mc.select('MODEL')
                if notModelAbcObjs:
                    mc.select(notModelAbcObjs,add=1)
                import maya.mel as mel
                # 归零
                self.transformNodeGoZero()
                mel.eval('FreezeTransformations')
                mel.eval('ResetTransformations')
            # 清理非归零点
            self.sk_meshLocalPoints(notModelAbcObjs)
            # 清理历史
            mc.select('MODEL')
            if notModelAbcObjs:
                mc.select(notModelAbcObjs,add=1)
            import maya.mel as mel
            mel.eval('DeleteHistory')
            # 归零
            if abcByns in [2]:
                # 多余mesh清理
                meshes = mc.ls(type = 'mesh',l=1)
                for checkMesh in meshes:
                    if mc.getAttr(checkMesh+'.intermediateObject'):
                        mc.delete(checkMesh)

        if printMode:self.testDef('---[Trans]:[%s]---002'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if joints:
            for joint in joints:
                if mc.getAttr(joint + '.drawStyle', l=1):
                    continue
                mc.setAttr((joint + '.drawStyle'), 2)
        # 隐藏晶格
        lattices = mc.ls(type='lattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                cons = mc.listConnections((grp[0] + '.v'),s=1,d=0)
                if cons:
                    continue
                mc.setAttr((grp[0] + '.v'),l=0)
                mc.setAttr((grp[0] + '.v'), 0)
        lattices = mc.ls(type='baseLattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                try:
                    mc.setAttr((grp[0] + '.v'), l=0)
                except:
                    pass
                mc.setAttr((grp[0] + '.v'), 0)
        rootGrp = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()[0]

        if printMode:self.testDef('---[Trans]:[%s]---003'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        if setMode and exMode in ['anim']:
            from idmt.maya.Lion import Lion_checkData
            reload(Lion_checkData)
            Lion_checkData.Lion_meshData().Lion_SetMeshData()

        if printMode:self.testDef('---[Trans]:[%s]---005'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        self.checkAssetSmoothSetUpdate()

        if printMode:self.testDef('---[Trans]:[%s]---006'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 清理，导出
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        tagetPath = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileNamePre = shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2]
        if shotInfo[2] in ['gpu','GPU']:
            fileNamePre = fileNamePre + '_' + shotInfo[3]
        fileName = tagetPath + fileNamePre + '_ms_%s'%exMode + fileFomat

        skipAssetList = ['']

        if not setMode and shotInfo[1] not in skipAssetList:
            # 选取物体
            mc.select(rootGrp)
            # set组加选
            quickSets = mc.ls(type='objectSet')
            rootSets = []
            for checkSet in quickSets:
                if 'skinCluster' in checkSet:
                    continue
                if 'tweak' in checkSet:
                    continue
                if 'SG' in checkSet:
                    continue
                if checkSet in ['initialParticleSE','initialShadingGroup']:
                    continue
                info = mc.listConnections(checkSet,s=0, d=1)
                if not info:
                    rootSets.append(checkSet)
                else:
                    checkChild = mc.listConnections((checkSet + '.message'),s=0, d=1, type='objectSet')
                    if mc.nodeType(info[0]) in ['hyperLayout'] and (not checkChild):
                        rootSets.append(checkSet)
            if rootSets:
                mc.select(rootSets,add=1,ne=1)

            # 显示层
            if setMode:
                displayLayers = mc.ls(type = 'displayLayer')
                needLayers = []
                for checkLayer in displayLayers:
                    if checkLayer in ['displayLayer']:
                        continue
                    inr = mc.referenceQuery(checkLayer,inr=1)
                    if inr:
                        continue
                    needLayers.append(checkLayer)
                if needLayers:
                    mc.select(needLayers,add=1)

            if exMode in ['anim']:
                #应YAK项目设置要求导出该脚本表达式
                if shotInfo[0] in ['Yak']:
                    expNodes = mc.ls('SV_DagMenuProc',type='script')
                    if expNodes:
                        mc.select(expNodes,add=1)

                # 设置专用保留
                if shotInfo[0] in ['mk']:
                    expNodes = mc.ls(type='script') + mc.ls(type='network')
                    if expNodes:
                        mc.select(expNodes,add=1)
                else:
                    expNodes = mc.ls('rgNeed_*',type='script') + mc.ls('rgNeed_*',type='network')
                    if expNodes:
                        mc.select(expNodes,add=1)

            if printMode:self.testDef('---[Trans]:[%s]---007'%exMode)
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

            # 处理导出
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
            mc.file(fileName, force=1, options="v=0", type=fileTypeFull, preserveReferences=1, exportSelected=1)

            if printMode:self.testDef('---[Trans]:[%s]---008'%exMode)
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

            print '\n------Export Clean-------\n'
            # 打开CacheMODEL新文件
            mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)

            if printMode:self.testDef('---[Trans]:[%s]---009'%exMode)
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
        else:
            mc.file(rename = fileName)
            mc.file(s=1,f=1)

        # 清理ShapeOrig
        if (not setMode) and exMode in ['render']:
            shapes = mc.ls(type='mesh',l=1)
            for mesh in shapes:
                if '|%s|'%sk_infoConfig.sk_infoConfig().renderGrp not in mesh:
                    continue
                if mc.getAttr(mesh + '.intermediateObject'):
                    mc.delete(mesh)
        if printMode:self.testDef('---[Trans]:[%s]---010'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 重建smoothSet
        serverSmoothSetInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server = 1,infoMode=3)
        print '------------PathPre'
        print serverSmoothSetInfoPath

        import os
        removeList = ['SMOOTH_SET','smooth_0','smooth_1','smooth_2']
        for checkSet in removeList:
            if not mc.ls(checkSet,type = 'objectSet'):
                continue
            mc.delete(checkSet)
        for num in range(3):
            smoothFile = serverSmoothSetInfoPath + 'smooth_%s.txt'%(str(num))
            if not os.path.exists(smoothFile):
                continue
            objsSmoothSet_lvNum = sk_infoConfig.sk_infoConfig().checkFileRead(smoothFile)
            if objsSmoothSet_lvNum:
                needObjs = []
                for obj in objsSmoothSet_lvNum:
                    if mc.ls(obj):
                        objName = mc.ls(obj, l=1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lvNum = needObjs
                    mc.select(objsSmoothSet_lvNum)
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(smoothLevel = num,previewFix = 0)

        if printMode:self.testDef('---[Trans]:[%s]---011'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        mc.select(cl=1)

        # aov 清理
        aovNodes = mc.ls(type = 'aiAOV')
        for checkNode in aovNodes:
            inr = mc.referenceQuery(checkNode,inr=1)
            if not inr:
                mc.delete(checkNode)

        if printMode:self.testDef('---[Trans]:[%s]---012'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 清理shader
        if cleanShader and shotInfo[1]!='s5410RuinsCounty':
            baseShader = 'idmt_baseColorShader'
            if not mc.ls(baseShader):
                baseShader = mc.shadingNode('lambert', asShader = True, name = baseShader)
            baseSG = 'idmt_baseColorShaderSG'
            if not mc.ls(baseSG):
                baseSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = baseSG)
            baseSGAttr = baseSG+'.surfaceShader'
            cons = mc.listConnections(baseSG+'.surfaceShader',s=1,d=0,plugs=1)
            if cons:
                if baseShader not in cons[0]:
                    mc.disConnectAttr(cons[0],baseSGAttr)
                    mc.connectAttr(baseShader+ '.outColor',baseSGAttr)
            else:
                mc.connectAttr(baseShader+ '.outColor',baseSGAttr)
            meshes = mc.ls(type = 'mesh',l=1)
            try:
                mc.sets(meshes,e = 1 , forceElement = baseSG)
            except:
                print '---------error'
                print "------Some Objs can't modify shader"
                mc.error()

        if printMode:self.testDef('---[Trans]:[%s]---015'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 清理
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean()

        # displayeLayer及renderPlayer删除
        # 对set不清理显示层
        if shotInfo[1][assetSpecial] not in ['s', 'S']:
            sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        # 清理多余SET
        sk_sceneTools.sk_sceneTools().checkNoNeedSetClean()

        # 清理非参考namespace #
        print '---nsClean'
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()

        if printMode:self.testDef('---[Trans]:[%s]---016'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 清理无用ref
        refNodes = mc.ls(type = 'reference')
        for refNode in refNodes:
            if ':' in refNode:
                continue
            if '_UNKNOWN_' not in refNode:
                continue
            mc.lockNode(refNode, l=0)
            mc.delete(refNode)

        # 贴图隐藏
        if exMode in ['anim']:
            self.checkAssetAniFileNodesBackup()
        #整理文件
        if modclear==1:
            self.checkCleanMOD()

        #锁物体
        if exMode in ['anim'] and (not setMode):
            objs = [rootGrp]
            sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 1)
            sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
            sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()

        if printMode:self.testDef('---[Trans]:[%s]---017'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        # 环境变量
        sk_sceneTools.sk_sceneTools().sk_setPathEnv()

        # 关闭代理自动读取
        self.checkArnoldProxyLoadOff()

        # 更新asset信息
        if exMode in ['render']:
            self.checkAssetMetailUpdate()
            self.checkMODELUnlock()

        if modclear==1:
            sk_smoothSet.sk_smoothSet().smoothSetCombine("Smooth",remove = 1)
            self.checkCleanMOD()
        mc.file(s=1,f=1)

        if printMode:self.testDef('---[Trans]:[%s]---018'%exMode)
        if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")

        print '-----msFilePath'
        print mc.file(exn=1,q=1)

        if checkIn:
            # 用户名
            import os
            userName = os.environ['USERNAME']
            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
            tempInfo = projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2]
            if 'GPU' in newInfo:
                tempInfo = projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3]
            fileInfo = '1|' + tempInfo + '_ms_%s.mb'%exMode + '|' + userName
            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
            #print checkOutCmd
            import maya.mel as mel
            mel.eval(checkOutCmd)
            # checkIn
            #mel.eval('idmtProject -checkin -description \" ' + u'由%s文件清理完成'%imMode + '\"')
            result = mc.idmtProject(checkin = True, description = u'由%s文件清理完成'%imMode)
            if not result:
                print '--------Error:Checkin Failed'
                print u'-------Checkin失败,请通知TD核查-------'
                mc.error()
            print '\n==============Sucess CheckIn [%s] File=============='%exMode

        if returnOpen:
            mc.file(fileNow,o=1,f=1)

    # test
    def testDef(self,numInfo):
        print '----------%s'%numInfo

    # 处理非归位点
    def sk_meshLocalPoints(self,notModelAbcObjs = []):
        modelMeshes = mc.listRelatives('MODEL',ad=1,type='mesh',f=1)
        meshGrps = mc.listRelatives(modelMeshes,p=1,f=1)
        if notModelAbcObjs:
            meshGrps += notModelAbcObjs
        needFixList = []
        for checkGrp in meshGrps:
            checkMesh = mc.listRelatives(checkGrp,s=1,ni=1,type='mesh',f=1)[0]
            addState = 1
            cons = mc.listConnections(checkMesh,s=1,d=0)
            if cons:
                for checkNode in cons:
                    nodeType = mc.nodeType(checkNode)
                    if nodeType not in ['shadingEngine','groupId']:
                        addState = 0
            if addState:
                needFixList.append(checkGrp)
        # 加簇清理
        errorObjs = []
        for checkGrp in needFixList:
            try:
                tempNodes = mc.nonLinear(checkGrp,type = 'bend')
                mc.delete(tempNodes)
            except:
                errorObjs.append(checkGrp)
        if errorObjs:
            print '------errorObjList'
            for errorObj in errorObjs:
                print errorObj
            mc.error()

    #------------------------------#
    # asset贴图转Arnold.tx
    #------------------------------#
    def assetImage2Tx(self,checkMode = 1):
        sequenceLenth = 3
        fileNodes = mc.ls(type = 'file') + mc.ls(type = 'aiImage')
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        # arnoldPath..
        arnoldPath = ''
        import sys
        for checkPath in sys.path:
            if 'arnold' in checkPath.lower() and '2013' in checkPath:
                arnoldPath = checkPath.replace('2013','bin').replace('\\','/')
        if not arnoldPath:
            if "mtoa" in mc.moduleInfo(listModules = True):
                arnoldPath = "%s/bin" % mc.moduleInfo(path = True, moduleName = "mtoa")
        if not arnoldPath:
            print '-----No Arnold-----'
            return
        arnoldPath = '%s/maketx.exe'%arnoldPath
        serverPath = sk_infoConfig.sk_infoConfig().checkAssetSourceImagesPath()
        errorMissionList = []
        import os
        import shutil
        txTempPath = '%stxTransTemp'%localPath
        if os.path.exists(txTempPath):
            shutil.rmtree(txTempPath)
        os.makedirs(txTempPath)
        txFilePath = '%stxFileTemp'%localPath
        if os.path.exists(txFilePath):
            shutil.rmtree(txFilePath)
        os.makedirs(txFilePath)
        # 统计已转化的贴图
        transDoneFiles = []
        for checkNode in fileNodes:
            # 路径获取
            checkType = mc.nodeType(checkNode)
            checkAttr = '.fileTextureName'
            if checkType in ['aiImage']:
                checkAttr = '.filename'
            nodeAttr = checkNode + checkAttr
            imagePath = mc.getAttr(nodeAttr,x=1)
            if '\\' in imagePath:
                imagePath = imagePath.replace('\\','/')
            # 特殊情况处理
            if checkType in ['file'] and mc.getAttr(checkNode+'.useFrameExtension'):
                imgName = imagePath.split('/')[-1]
                searchPath = imagePath[:-1*(len(imagePath.split('/')[-1])+1)].replace('/','\\')
                dataGet = os.popen('DIR /d %s /b /s'%searchPath)
                getInfo = dataGet.read()
                allInfos = getInfo.split('\n')
                for checkInfo in allInfos:
                    newImgPath = checkInfo.replace('\\','/')
                    if newImgPath not in transDoneFiles:
                        infoName = newImgPath.split('/')[-1]
                        if (len(infoName) == len(imgName)) and (infoName.split('.')[0][:-1*sequenceLenth] == imgName.split('.')[0][:-1*sequenceLenth]):
                            errorMissionList += self.txCreatePerform(newImgPath,serverPath,txTempPath,txFilePath,arnoldPath,checkMode)
                            transDoneFiles.append(newImgPath)
            else:
                if imagePath not in transDoneFiles:
                    errorMissionList += self.txCreatePerform(imagePath,serverPath,txTempPath,txFilePath,arnoldPath,checkMode)
                    transDoneFiles.append(imagePath)
        if errorMissionList:
            print u'\n---[Trans To Arnold Tx][转.tx失败]---'
            for errorFile in errorMissionList:
                print errorFile
            print u'---[Trans To Arnold Tx][转.tx失败]---\n'
            mc.error()
        updateAnimCMD = 'zwSysFile "xcopy" "%s" "%s" true' % (txTempPath, re.sub(r"[/\\]$", "", serverPath))
        mel.eval(updateAnimCMD)
        shutil.rmtree(txTempPath)
        shutil.rmtree(txFilePath)

    # 执行转换
    def txCreatePerform(self,imagePath,serverPath,txTempPath,txFilePath,arnoldPath,checkMode = 1):
        import os
        errorMissionList = []
        # 检测
        imgTxFile = '%stx'%(imagePath.split('/')[-1][:-1*len(imagePath.split('.')[-1])])
        exportState = 1
        serverKey = '/Projects/'
        if checkMode:
            txServerFile = '%s%s'%(serverPath,imgTxFile)
            if serverPath.split(serverKey)[-1].lower() in imagePath.split(serverKey)[-1].lower() and os.path.exists(txServerFile):
                exportState = 0
        # 执行
        if exportState:
            finalFile = '%s/%s'%(txTempPath,imgTxFile)
            localFile = '%s/%s'%(txFilePath,imagePath.split('/')[-1])
            mc.sysFile(imagePath,copy=localFile)
            runCmd = '\""%s" -o "%s" -u --oiio "%s"\"'%(arnoldPath ,finalFile , localFile)
            print runCmd
            os.popen(runCmd)
            if not os.path.exists(finalFile):
                errorMissionList.append(imagePath)
        return errorMissionList

    #------------------------------#
    # render属性归零
    #---------------------------------------------------------#
    # transformNode归零
    def transformNodeGoZero(self,minCheck = -3):
        transNode = mc.ls(type = 'transform')
        attrDict = {'.tx':0,'.ty':0,'.tz':0,'.rx':0,'.ry':0,'.rz':0,'.sx':1,'.sy':1,'.sz':1}
        for checkNode in transNode:
            inr = mc.referenceQuery(checkNode,inr = 1)
            if inr:
                continue
            shape = mc.listRelatives(checkNode,s=1)
            if shape:
                continue
            for attr in attrDict.keys():
                checkAttr = checkNode + attr
                valueNow = mc.getAttr(checkAttr)
                if abs(valueNow-attrDict[attr]) > 5*pow(10,minCheck):
                    cons = mc.listConnections(checkAttr,s=1,d=0,plugs = 1)
                    if cons:
                        mc.disConnectAttr(cons[0],checkAttr)
                    mc.setAttr(checkAttr,attrDict[attr])

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 所有代理节点关闭load
    def checkArnoldProxyLoadOff(self):
        checkNodes = mc.ls(type = 'aiStandIn')
        for checkNode in checkNodes:
            checkAttr = checkNode + '.standInDrawOverride'
            mc.setAttr(checkAttr,4)

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】File节点路径清理，备份
    #  Author  : 沈  康
    #  Data    : 2013_08_21
    #------------------------------#
    # 清理，备份
    def checkAssetAniFileNodesBackup(self, selectMode=0 , keyDonot = '',justOff = 0):
        if selectMode:
            objsSel = mc.ls(sl=1, l=1)
            fileNodes = self.checkGetObjFileNodes(objsSel)
        else:
            fileNodes = mc.ls(type='file') + mc.ls(type='aiImage') + mc.ls(type = 'aiStandIn')
        for node in fileNodes:
            if keyDonot:
                ns = node[:(len(node.split(':')[-1])*-1)]
                if keyDonot not in ns.lower():
                    continue
            if mc.nodeType(node) in ['file']:
                keyAttr = '.fileTextureName'
            if mc.nodeType(node) in ['aiImage']:
                keyAttr = '.filename'
            if mc.nodeType(node) in ['aiStandIn']:
                keyAttr = '.dso'
            attr = sk_infoConfig.sk_infoConfig().bkImgAttr
            if not mc.ls(node + '.' + attr):
                mc.addAttr(node, ln=attr , dt='string')
            imagePath = mc.getAttr((node + keyAttr))
            mc.setAttr((node + keyAttr), '', type='string')
            if imagePath and not justOff:
                mc.setAttr((node + '.' + attr), imagePath, type='string')

    #------------------------------#
    # 还原
    def checkAssetAniFileNodesReturn(self, selectMode=0 ,showType = []):
        if selectMode:
            objsSel = mc.ls(sl=1, l=1)
            fileNodes = self.checkGetObjFileNodes(objsSel)
        else:
            fileNodes = mc.ls(type='file') + mc.ls(type='aiImage') + mc.ls(type = 'aiStandIn')

        for node in fileNodes:
            attr = sk_infoConfig.sk_infoConfig().bkImgAttr
            if mc.nodeType(node) in ['file']:
                keyAttr = '.fileTextureName'
            if mc.nodeType(node) in ['aiImage']:
                keyAttr = '.filename'
            if mc.nodeType(node) in ['aiStandIn']:
                keyAttr = '.dso'
            if showType and mc.nodeType(node) not in showType:
                continue
            oldImagePath = mc.getAttr(node + keyAttr)
            if not oldImagePath and mc.ls(node + '.' + attr):
                imagePath = mc.getAttr((node + '.' + attr))
                mc.setAttr((node + keyAttr), imagePath, type='string')

    #------------------------------#
    # 选取物体获取file节点
    def checkGetObjFileNodes(self, objs):
        meshes = mc.listRelatives(objs, s=1, ni=1, type='mesh', f=1)
        sgNodes = mc.listConnections(meshes, s=1, type='shadingEngine')

        temp = mc.listConnections(sgNodes , s=1 , type='file')
        if not temp:
            temp = []
        baseFileNodes = temp
        temp = mc.listConnections(sgNodes , s=1 , type='aiImage')
        if not temp:
            temp = []
        baseFileNodes = baseFileNodes + temp

        if not baseFileNodes:
            baseFileNodes = []

        if not sgNodes:
            return []

        shaders = []
        sgAttrs = ['surfaceShader', 'volumeShader', 'displacementShader', 'aiSurfaceShader', 'aiVolumeShader', 'miMaterialShader', 'miShadowShader', 'miVolumeShader', 'miDisplacementShader']
        for sgNode in sgNodes:
            for attr in sgAttrs:
                try:
                    shaderTemp = mc.listConnections((sgNode + '.%s' % attr) , s=1)
                    if shaderTemp:
                        shaders.append(shaderTemp[0])
                except:
                    pass

        shaderFiles = self.getShaderAllFileNodes(shaders,['file','aiImage','aiStandIn'])
        shaderFiles = shaderFiles + baseFileNodes

        return shaderFiles

    #------------------------------#
    # shader下所有file或aiImage,aiStandIn
    def getShaderAllFileNodes(self,shaders,fileType):
        nodes = []
        needNodes = []
        haveNodes = []
        for shader in shaders:
            temp = mc.listConnections(shader,s=1,d=0)
            if not temp:
                continue
            nodes = nodes + temp
        if nodes:
            nodes = list(set(nodes))
        while nodes:
            checkNodes = []
            for node in nodes:
                if mc.nodeType(node) not in ['materialInfo','defaultShaderList','defaultTextureList','shadingEngine'] and node not in haveNodes:
                    checkNodes.append(node)
                    haveNodes.append(node)
                if mc.nodeType(node) not in fileType:
                    continue
                needNodes.append(node)
            nodes = self.getShaderAllFileNodes(checkNodes,fileType)
        return needNodes

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用：cache测试管理】
    # 0.仅在rig阶段使用
    # 1.cache测试
    # Author　　: 沈  康
    #　Data    :　2013_05_19 - 2013_05_20
    # ------------------------------#
    # 设置cache测试,rgCache
    def checkCacheRigTest(self):
        import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)

        #shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localFilePath = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
        fileName = mc.file(exn=1, q=1)
        rgFileName = fileName.split('/')[-1]
        # 本地另存
        mc.file(rename=(localFilePath + rgFileName))
        mc.file(save=1, force=1)
        # 获取控制器
        ctrl = mc.ls('Master', type='transform') + mc.ls('Master_ct_an', type='transform') + mc.ls('master', type='transform') + mc.ls('master_ct_an', type='transform')
        if ctrl:
            if mc.ls('Master'):
                ctrl = 'Master'
            if mc.ls('Master_ct_an'):
                ctrl = 'Master_ct_an'
            if mc.ls('master'):
                ctrl = 'master'
            if mc.ls('master_ct_an'):
                ctrl = 'master_ct_an'
            # 获取时间轴
            mc.select(ctrl)
            frameStart = mc.playbackOptions(q=1, min=1)
            frameEnd = mc.playbackOptions(max=frameStart + 20)
            # 第一帧K帧
            mc.currentTime(frameStart)
            mc.setKeyframe(v=0, at='translateZ')
            mc.setKeyframe(v=0, at='rotateY')
            # 最后一帧K帧
            mc.currentTime(frameEnd)
            mc.setKeyframe(v=50, at='translateZ')
            mc.setKeyframe(v=360, at='rotateY')
            mc.select(cl=1)

            # 隐藏不渲染的物体
            grps = mc.ls(type='transform', l=1)
            for grp in grps:
                if grp[-1] == '_':
                    if '_si' in grp or '_nr_' in grp:
                        try:
                            mc.setAttr((grp + '.v'), 0)
                        except:
                            print grp
                            pass

            # 更新cache列表，测试rig用时不需要祛除隐藏物体
            sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
            sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
            cacheObjs = mc.sets('MESHES', q=1)
            animObjs = mc.sets('CTRLS', q=1)

            if cacheObjs:
                # 执行缓存创建,local,不偏移,非ref模式,不连接模式
                # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, 0, 0, 0, 0)

                # 本地anim信息
                if animObjs:
                    # 判断animObjs有没有约束
                    isCons = 0
                    for animObj in animObjs:
                        historyObjs = mc.listHistory(animObj)
                        if historyObjs:
                            for objOne in historyObjs:
                                if 'Constraint' in mc.nodeType(objOne):
                                    isCons = 1
                                    break
                    if isCons:
                        sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

                    # 执行约束导出,local,非ref模式
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 0)

                # 转render文件
                mc.file((localFilePath + rgFileName), open=1, force=1)
                self.checkTexMo2CacheMo(checkin=0)

                # 导入cache
                sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, 0)

                # 导入anim信息
                if animObjs:
                    sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(0)

                print u'\n'
                print u'=====================Rg Cache创建完毕====================='
                print u'>>>>>当前文件为您的rg文件模拟出的render文件'
                print u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'
                print u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'
                print u'>>>>>如果涉及到_ct_an标记，请检测与Master环约束的_ct_an是否运动'
                print u'\n'

            else:
                mc.warning(u'=====================【错误】未发现cache物体 ！！！】=====================')

        else:
            #mc.warning(unicode('=====================【错误】 未发现Master控制器！！！】=====================', "utf8"))
            mc.warning(u'=====================【错误】 未发现Master控制器！！！】=====================')

    # ------------------------------#
    # 【通用：cache测试管理】
    # 0.仅在texture阶段使用
    # 1.cache测试
    # Author: 沈  康
    # Data    :2013_12_18
    # ------------------------------#
    # txcache
    def checkCacheTxTest(self):
        import os
        import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)

        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 判断是否tx文件
        if 'tx.' in shotInfo[3]:
            txFileName = mc.file(exn=1, q=1)
            # 寻找服务器端rg文件
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            assetType = ''
            if shotInfo[1][0] == 'c':
                assetType = 'characters'
            if shotInfo[1][0] == 'p':
                assetType = 'props'

            if assetType:
                needFolder = '/rigging/'
                fileKeyInfo = shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) + '_rg.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + str(shotInfo[1]) + needFolder

                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder=assetServerPath)
                    if assetFiles:
                        rgCheck = 0
                        for fileName in assetFiles:
                            if fileKeyInfo in fileName:
                                rgCheck = 1
                                # 打开rg文件
                                mc.file((assetServerPath + fileName), open=1, force=1)
                                # rg文件cache检测
                                # 获取控制器
                                ctrl = mc.ls('Master', type='transform') + mc.ls('Master_ct_an', type='transform') + mc.ls('master', type='transform') + mc.ls('master_ct_an', type='transform')
                                if ctrl:
                                    if mc.ls('Master'):
                                        ctrl = 'Master'
                                    if mc.ls('Master_ct_an'):
                                        ctrl = 'Master_ct_an'
                                    if mc.ls('master'):
                                        ctrl = 'master'
                                    if mc.ls('master_ct_an'):
                                        ctrl = 'master_ct_an'
                                    # 获取时间轴
                                    mc.select(ctrl)
                                    frameStart = mc.playbackOptions(q=1, min=1)
                                    frameEnd = mc.playbackOptions(max=frameStart + 20)
                                    # 第一帧K帧
                                    mc.currentTime(frameStart)
                                    mc.setKeyframe(v=0, at='translateZ')
                                    mc.setKeyframe(v=0, at='rotateY')
                                    # 最后一帧K帧
                                    mc.currentTime(frameEnd)
                                    mc.setKeyframe(v=50, at='translateZ')
                                    mc.setKeyframe(v=360, at='rotateY')
                                    mc.select(cl=1)

                                    # 更新cache列表，测试rig用时不需要祛除隐藏物体
                                    sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                                    sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                                    cacheObjs = mc.sets('MESHES', q=1)
                                    animObjs = mc.sets('CTRLS', q=1)
                                    if cacheObjs:
                                        # 执行缓存创建,local,非ref模式
                                        # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                                        sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheExport(cacheObjs, 0, 0, 0, 0)

                                        # 本地anim信息
                                        if animObjs:
                                            # 判断animObjs有没有约束
                                            isCons = 0
                                            for animObj in animObjs:
                                                historyObjs = mc.listHistory(animObj)
                                                if historyObjs:
                                                    for objOne in historyObjs:
                                                        if 'Constraint' in mc.nodeType(objOne):
                                                            isCons = 1
                                                            break
                                            if isCons:
                                                sk_cacheFinalLayout.sk_cacheFinalLayout().sk_checkBakeConstraints()

                                            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 0)

                                        # 回到tx文件检测
                                        mc.file(txFileName, open=1, force=1)

                                        # 清理历史
                                        mc.select(cacheObjs)
                                        mel.eval('DeleteAllHistory')

                                        # 导入cache
                                        sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheSetCacheImport(cacheObjs, 0)

                                        # 导入anim信息
                                        if animObjs:
                                            sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoImport(0)

                                        print u'\n'
                                        print u'=====================Tx Cache创建完毕====================='
                                        print u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'
                                        print u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'
                                        print u'\n'

                                    else:
                                        # 回到tx文件检测
                                        mc.file(txFileName, open=1, force=1)

                                        print u'\n'
                                        print u'=====================Tx Cache创建完毕====================='
                                        print u'>>>>>rg文件没有cache物体'
                                        print u'>>>>>请和rg确定，该asset rg文件是否cache测试正确'
                                        print u'\n'
                                else:
                                    # 回到tx文件检测
                                    mc.file(txFileName, open=1, force=1)
                                    print u'\n'
                                    print u'=====================Tx Cache创建完毕====================='
                                    print u'>>>>>rg文件找不到大环控制器'
                                    print u'>>>>>请和rg确定，该asset rg文件是否cache测试正确'
                                    print u'\n'
                        if rgCheck == 0:
                            print u'\n'
                            print u'=====================Tx Cache创建完毕====================='
                            print u'>>>>>服务器端没有对应版本的rg文件'
                            print u'\n'

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【杂项】 后台处理相关
    # ------------------------------#

    # ------------------------------#
    # 【an镜头】shot 文件 asset信息输出
    # ------------------------------#
    # needType : 0 需要所有asset，chr,prop,set |  1 只要chr ,prop
    def sk_assetInfoUpdate(self, reorganize=[0, 0], needType=1, assetSpecial=0):
        import sk_sceneTools
        reload(sk_sceneTools)
        import sk_referenceConfig
        reload(sk_referenceConfig)

        # 处理大组
        if reorganize[0]:
            sk_sceneTools.sk_sceneTools().sk_sceneReorganize(reorganize[1])

        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

        # 处理大组
        noNeedRefNodeInfo = []
        if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
            allGrps = []
            if mc.listRelatives('OTC_GRP', ad=1, f=1):
                allGrps = allGrps + mc.listRelatives('OTC_GRP', ad=1, f=1)
            if needType == 1:
                if mc.listRelatives('SET_GRP', ad=1, f=1):
                    allGrps = allGrps + mc.listRelatives('SET_GRP', ad=1, f=1)
            if allGrps:
                for grp in allGrps:
                    if mc.referenceQuery(grp, isNodeReferenced=1):
                        refNode = mc.referenceQuery(grp, referenceNode=1)
                        noNeedRefNodeInfo.append(refNode)
                if noNeedRefNodeInfo:
                    noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
        # 输出数据
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
                if refNode.split('_')[1][assetSpecial] not in ['s', 'S']:
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    assetNeedOutputInfo.append(newPath)
                    assetNeedOutputInfo.append(ns)
        assetLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath()
        print assetNeedServerPath
        # 写
        sk_infoConfig.sk_infoConfig().checkFileWrite((assetLocalPath + 'assetReference.txt'), assetNeedOutputInfo)
        # 传递
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (assetLocalPath + 'assetReference.txt') + '"' + ' ' + '"' + (assetNeedServerPath + 'assetReference.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'\n'
        print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
        print u'\n'

    # ------------------------------#
    # 【通用：文件中透明贴图物体信息输出】
    # 0.仅在model,rig,texture通用
    # Author  : 沈  康
    # Data    : 2013_05_16
    # ------------------------------#
    # 获取有透明贴图的物体 assetTrans
    def checkTransparencyObjsInfoExport(self):
        transparencySG = []
        # 获取file节点
        SGNodes = mc.ls(type='shadingEngine')
        for SGNode in SGNodes:
            transLayerShaderCheckState = 0
            transRampShaderCheckState = 0
            # 判断是否有透明值
            transValueState = 0
            # 获取shader
            shaderNode = mc.listConnections(SGNode + '.surfaceShader')
            if shaderNode:
                # 获取提供透明属性的上级连接的节点
                transpancyNode = ''
                needTranparencyAttr = ''
                if mc.nodeType(shaderNode[0]) != 'surfaceShader':
                    # 判断是否层纹理
                    # 对于层纹理，一旦发现有透明贴图，立即将本节点的outTransparency输出给新layer shader
                    if mc.nodeType(shaderNode[0]) == 'layeredShader':
                        # 获取层纹理的input
                        layerInputs = mc.getAttr((shaderNode[0] + '.inputs'), mi=1)
                        if layerInputs:
                            for inputNum in layerInputs:
                                transpancyNode = ''
                                transpancyAttr = mc.ls(shaderNode[0] + '.inputs[' + str(inputNum) + ']' + '.transparency')
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                                if transpancyNode:
                                    transLayerShaderCheckState = 1
                            if transLayerShaderCheckState:
                                transpancyNode = [shaderNode[0]]
                            else:
                                # 判断有没有值
                                needTranparencyAttr = shaderNode[0] + '.outTransparency'
                                transValue = mc.getAttr(needTranparencyAttr)
                                if transValue[0][0] != 0:
                                    transpancyNode = [shaderNode[0]]
                                else:
                                    transpancyNode = ''
                    else:
                        # 判断是否 rampShader
                        # 对于判断是否rampShader，一旦发现有透明贴图，立即将本节点的outTransparency输出给新layer shader
                        if mc.nodeType(shaderNode[0]) == 'rampShader':
                            transList = mc.getAttr((shaderNode[0] + '.transparency'), mi=1)
                            for inputNum in transList:
                                transpancyNode = ''
                                transpancyAttr = mc.ls(shaderNode[0] + '.transparency[' + str(inputNum) + ']' + '.transparency_Color')
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                                if transpancyNode:
                                    transRampShaderCheckState = 1
                            if transRampShaderCheckState:
                                transpancyNode = [shaderNode[0]]
                            else:
                                # 判断有没有值
                                needTranparencyAttr = shaderNode[0] + '.outTransparency'
                                transValue = mc.getAttr(needTranparencyAttr)
                                if transValue[0][0] != 0:
                                    transpancyNode = [shaderNode[0]]
                                else:
                                    transpancyNode = ''
                        else:
                            if mc.objExists(shaderNode[0] + '.transparency'):
                                transpancyAttr = mc.ls(shaderNode[0] + '.transparency')
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                                # 获取值
                                if not transpancyNode:
                                    transValue = mc.getAttr(transpancyAttr[0])
                                    if transValue[0][0] != 0:
                                        transValueState = 1
                                        transpancyNode = '[food]' + str(transValue[0][0])
                else:
                    transpancyAttr = mc.ls(shaderNode[0] + '.outTransparency')
                    transpancyNode = mc.listConnections(transpancyAttr[0], plugs=1, connections=1, destination=0)
                    # 获取值
                    if not transpancyNode:
                        transValue = mc.getAttr(transpancyAttr[0])
                        if transValue[0][0] != 0:
                            transValueState = 1
                            transpancyNode = '[food]' + str(transValue[0][0])
                # 存在透明通道，则保存
                if transpancyNode:
                    if transpancyAttr[0] in transpancyNode:
                        transpancyNode.remove(transpancyAttr[0])
                if transpancyNode:
                    '''
                    if transLayerShaderCheckState == 0 and transRampShaderCheckState == 0 and transValueState == 0 :
                        transpancyNode = mc.listConnections(transpancyAttr[0] , plugs = 1)
                    else:
                        transpancyNode = transpancyNode
                    '''
                    needTransNode = ''
                    if transpancyNode[0] == '[':
                        needTransNode = transpancyNode
                    else:
                        needTransNode = transpancyNode[0]

                    # SG节点命名判断
                    # 遵循'SHD_..._keyInfo_SG'
                    if ':' in SGNode:
                        #meshes = mc.listConnections(SGNode,type = 'mesh')
                        meshes = mc.sets(SGNode, q=1)
                        # 记录信息
                        transparencySG.append([SGNode, meshes, needTransNode])
                    else:
                        #meshes = mc.listConnections(SGNode,type = 'mesh')
                        meshes = mc.sets(SGNode, q=1)
                        # print u'------------------'
                        # print meshes
                        # print transpancyNode
                        # 记录信息
                        if transValueState == 1:
                            transparencySG.append([SGNode, meshes, needTransNode])
                        else:
                            transparencySG.append([SGNode, meshes, needTransNode])
        # 输出信息
        # 必须全部输出，避免由有内容到无内容的不更新bug更新
        # if transparencySG:
        # 整理信息
        transpancySGNodes = []
        transpancyMeshes = []
        transpancyNode = []
        for transGrp in transparencySG:
            transpancySGNodes.append(transGrp[0])
            transpancyMeshes.append(transGrp[1])
            transpancyNode.append(transGrp[2])

        # 本地及服务器端路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localTransPath = localPath + 'transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        mc.sysFile(localTransPath, makeDir=1)
        serverTransPath = serverPath + 'data/AssetInfos/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
        mel.eval(makeDirCMD)

        # 本地输出及更新
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'transSGNodes.txt'), transpancySGNodes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transSGNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transSGNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'transMeshes.txt'), transpancyMeshes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transMeshes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath + 'transNodes.txt'), transpancyNode)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    # 全流程用，禁用arnold
    def checkAssetforbidenNodes(self, arnoldCheck=1):
        if arnoldCheck:
            arnoldNodes = mc.ls(type='aiAOVDriver') + mc.ls(type='aiAOVFilter') + mc.ls(type='aiOptions')
            if arnoldNodes:
                print(u'=====Asset 存在 Arnold 节点，请Export清理=====')
                mc.error(u'=====Asset 存在 Arnold 节点，请Export清理=====')

    #-------------------------------#
    # 收集文件内所有贴图，cache路径
    def checkNodeFilePaths(self):
        pathDict = {}
        # file 节点
        nodeType = 'file'
        checkAttr = '.fileTextureName'
        fileNodes = mc.ls(type = nodeType)
        nodeList = []
        pathList = []
        for checkNode in fileNodes:
            targetPath = mc.getAttr((checkNode + checkAttr),x=1)
            nodeList.append(checkNode)
            pathList.append(targetPath)
        pathDict[nodeType] = {'node':nodeList,'path':pathList,'attr':checkAttr}
        # aiImage 节点
        nodeType = 'aiImage'
        checkAttr = '.filename'
        fileNodes = mc.ls(type = nodeType)
        nodeList = []
        pathList = []
        for checkNode in fileNodes:
            targetPath = mc.getAttr((checkNode + checkAttr),x=1)
            nodeList.append(checkNode)
            pathList.append(targetPath)
        pathDict[nodeType] = {'node':nodeList,'path':pathList,'attr':checkAttr}
        # cache 节点
        nodeType = 'cacheFile'
        checkAttr = '.cachePath'
        fileNodes = mc.ls(type = nodeType)
        nodeList = []
        pathList = []
        for checkNode in fileNodes:
            targetPath = mc.getAttr((checkNode + checkAttr),x=1)
            nodeList.append(checkNode)
            pathList.append(targetPath)
        pathDict[nodeType] = {'node':nodeList,'path':pathList,'attr':checkAttr}
        # abc 节点
        nodeType = 'AlembicNode'
        checkAttr = '.abc_File'
        fileNodes = mc.ls(type = nodeType)
        nodeList = []
        pathList = []
        for checkNode in fileNodes:
            targetPath = mc.getAttr((checkNode + checkAttr),x=1)
            nodeList.append(checkNode)
            pathList.append(targetPath)
        pathDict[nodeType] = {'node':nodeList,'path':pathList,'attr':checkAttr}
        # yeti texture
        nodeType = 'pgYetiMaya'
        checkAttr = 'file_name'
        fileNodes = mc.ls(type = nodeType)
        for checkNode in fileNodes:
            txNodes = mc.pgYetiGraph(checkNode,listNodes= 1, type = 'texture')
            if not txNodes:
                continue
            for checkTxNode in txNodes:
                targetPath = mc.pgYetiGraph(checkNode,node = checkTxNode,param= checkAttr, getParamValue = 1)
                targetPath = sk_infoConfig.sk_infoConfig().checkEnvPath2FullPath(targetPath)
                nodeList.append('%s|%s'%(checkNode,checkTxNode))
                pathList.append(targetPath)
        pathDict[nodeType] = {'node':nodeList,'path':pathList,'attr':checkAttr}

        return pathDict

    #-------------------------------#
    # camera name check
    # 全流程用
    def checkShotCameraName(self):
        fileName = mc.file(exn=1, q=1)
        shotInfo = fileName .split('/')[-1].split('.')[0].split('_')
        needCam = ''
        cameras = mc.ls(type='camera', l=1)
        if cameras:
            for cam in cameras:
                isRef = mc.referenceQuery(cam, isNodeReferenced=1)
                if isRef:
                    continue
                camGrp = mc.listRelatives(cam, p=1, f=1)
                if not camGrp:
                    continue
                camGrp = camGrp[0]
                if ('_' + str(shotInfo[1]) + '_').lower() in camGrp.split('|')[-1].lower() and ('_' + str(shotInfo[2])).lower() in camGrp.split('|')[-1].lower():
                    if '_baked' in camGrp:
                        bkCam = camGrp
                    else:
                        needCam = camGrp
        if not needCam:
            mc.error(u'=============找不到对应镜头的CAM=============')

    # ------------------------------#
    # 前期角色道具tx文件检测选面
    def checkFaceShaderDetails(self):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        check = 1
        if shotInfo[0] == 'zm':
            # 特殊内部任务ID
            strangeID = sk_infoConfig.sk_infoConfig().checkStrangeIDInfo()
            if shotInfo[1] not in strangeID:
                if shotInfo[1][0] == 'p' and int(shotInfo[1][1:7]) < 100:
                    check = 0
        # 检测SG节点
        if check:
            errorAssetMeshes = []
            SGNodes = mc.ls(type='shadingEngine')
            if SGNodes:
                for node in SGNodes:
                    meshes = mc.sets(node, q=1)
                    if meshes:
                        for mesh in meshes:
                            meshFull = mc.ls(mesh, l=1)[0]
                            if '|MODEL|' in meshFull and '.f[' in mesh:
                                errorAssetMeshes.append(meshFull)
            if errorAssetMeshes:
                for info in errorAssetMeshes:
                    print info
                mc.error(u'------------请处理好以上选面赋予材质的物体------------')

    # ------------------------------#
    # cache path 环境变量恢复
    def checkCacheEnvPath(self):
        cacheFiles = mc.ls(type='cacheFile')
        if cacheFiles:
            for node in cacheFiles:
                cachePath = mc.getAttr(node + '.cachePath')
                cachePathNew = cachePath.replace('//file-cluster/GDC/Projects', '${IDMT_PROJECTS}')
                mc.setAttr((node + '.cachePath'), cachePathNew, type='string')

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用：后台检测anim和render版本是否一致】
    # 0.阶段通用
    # Author　　: 沈  康
    #　Data    :2013_11_27
    # ------------------------------#
    # UI篇前台篇
    def checkAnim2RenderSetUI(self):
        # 窗口
        if mc.window("sk_checkAnim2RenderSetUI", ex=1):
            mc.deleteUI("sk_checkAnim2RenderSetUI", window=True)
        mc.window("sk_checkAnim2RenderSetUI", title="Check Anim Render Cache List", widthHeight=(175, 100), menuBar=0)
        # 主界面
        mc.columnLayout()

        # Asset范围
        mc.frameLayout(label=u'检测Anim及Render版本', borderStyle='etchedOut', width=175)
        mc.rowLayout()

        mc.columnLayout()
        mc.optionMenuGrp('sk_checkAnim2RenderCheckType', label=(unicode('检测Asset范围', 'utf8')), bgc=[0.1, 0.6, 0.3], w=175, adjustableColumn=1)
        mc.menuItem(label=u'[0]项目全局')
        mc.menuItem(label=u'[1]所有角色')
        mc.menuItem(label=u'[2]所有道具')
        mc.menuItem(label=u'[3]所有场景')
        mc.menuItem(label=u'[4]当前Asset')
        mc.setParent("..")

        mc.setParent("..")

        mc.rowLayout()

        # 模型类别
        mc.columnLayout()
        mc.optionMenuGrp('checkAnim2RenderModelType', label=(unicode('检测模型类别', 'utf8')), bgc=[0.1, 0.7, 0.8], w=175, adjustableColumn=1)
        mc.menuItem(l=u'[0]   低模      ')
        mc.menuItem(l=u'[1]   中模      ')
        mc.menuItem(l=u'[2]   高模      ')
        mc.menuItem(l=u'[3]   所有      ')
        mc.setParent("..")

        mc.setParent("..")

        mc.optionMenuGrp('sk_checkAnim2RenderCheckType', e=1, select=5)
        mc.optionMenuGrp('checkAnim2RenderModelType', e=1, select=3)

        mc.rowLayout()
        mc.button(w=180, h=50, bgc=[0.3, 0.6, 0.3], label=(unicode('执行检测', 'utf8')), c='import maya.cmds as mc\ncheckType = mc.optionMenuGrp(\"sk_checkAnim2RenderCheckType\",q=1, value=1)[1]\nmodelType = mc.optionMenuGrp(\"checkAnim2RenderModelType\",q=1, value=1)[1]\nsk_checkCommon.sk_checkTools().checkAnim2RenderSetInfo(checkType,modelType)')
        mc.setParent("..")

        mc.setParent("..")
        mc.setParent("..")
        mc.showWindow("sk_checkAnim2RenderSetUI")

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【核心】 anim 和 render 版本差异
    # ------------------------------#

    # ------------------------------#
    # check in时检测Anim和Render版本差异
    # cacheType: 1 cacheList检测 | 0 设置流程控制器List检测
    # 增加豁免列表| keys: anim render 差异 | anim render 一致性
    # assetSpecial  默认是文件名第二个字段的第一个字符，某些特殊情况除外，如SK是第二个字符
    # [注意]物体点线面异常对比，是在物体列表数量一致后进行的
    def checkAssetAnim2RenderCheckInConfig(self, cacheType=1,UVCheck = 1, assetSpecial=0,ignoreMode = 1,saveMode = 1):
        import sk_sceneTools
        reload(sk_sceneTools)
        import os
        # 豁免判断
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()

        # 文本豁免列表
        doNotCheckTxtPath = projectPath + 'data/rgtxIgnore.txt'
        notTxtProj = ['csl']
        # 有文件，且本文件在文件列表里，则判断return跳出
        if shotInfo[0] not in notTxtProj and os.path.exists(doNotCheckTxtPath) and ignoreMode:
            fileInfo = sk_infoConfig.sk_infoConfig().checkFileRead(doNotCheckTxtPath)
            if fileInfo:
                if shotInfo[1] in fileInfo:
                    print u'==========[一致性]本Asset处于豁免检测状态=========='
                    return 'ok'

        # 数据库豁免版本
        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        dataCmd = "SELECT isnull(A.rgtxIgnore,'0') as rgtxIgnoreNew FROM idmtPlex_%s.dbo.[TB_Asset] A WHERE A.asset_name ='%s'"%(projFullName,shotInfo[1])
        checkState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)

        if shotInfo[1] in ['p999999Ttest']:
            checkState = 1

        if checkState and ignoreMode:
            print u'=======rgrg===[一致性]本Asset处于豁免检测状态=========='
            return 'ok'
        import time
        print '-------------[rgCtx]Start-------------'
        print time.strftime("%Y-%m-%d %H:%M:%S")
        # 非豁免状态，全部强制检测
        # 记录文件名
        if saveMode:
            mc.file(save=1, force=1)
        fileName = mc.file(query=1, exn=1)
        print '-------------[rgCtx]001-------------'
        print time.strftime("%Y-%m-%d %H:%M:%S")
        # 记录非渲染的标记
        noNeedSign = ['_si_', '_nr_']
        # 开始检测
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        mayaType = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        cpState = 0
        if len(shotInfo) >= 4:
            # 检测是否为有效asset
            assetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
            assetName = shotInfo[1]
            checkState = 0
            for assetList in assetInfo:
                if shotInfo[1] in assetList:
                    checkState = 1
            if not checkState:
                return 0
            # 获取assetType
            if assetName in assetInfo[1] or shotInfo[1][assetSpecial] == 'c':
                assetType = 'characters'
                cpState = 1
            if assetName in assetInfo[2] or shotInfo[1][assetSpecial] == 'p':
                assetType = 'props'
                cpState = 1
            if assetName in assetInfo[3] or shotInfo[1][assetSpecial] in ['s', 'S']:
                assetType = 'sets'
            modelHML = ['l', 'm', 'h']
            errorInfos = []
            if shotInfo[2] in modelHML and shotInfo[3].split('.')[0] in ['rg', 'tx']:
                #animSetNum = [0, 0]
                #cacheSetNum = [0, 0]
                difInfo = ''
                if shotInfo[3].split('.')[0] == 'tx':
                    assetOtherFolder = '/rigging/'
                    assetOtherKey = '_rg'
                if shotInfo[3].split('.')[0] == 'rg':
                    assetOtherFolder = '/texture/'
                    assetOtherKey = '_tx'
                masterFolderPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
                masterFolderPath = masterFolderPath + 'scenes/' + assetType + '/' + assetName + assetOtherFolder
                # 首先查询是否存在另一半文件,不存在则pass
                fileOther = masterFolderPath + shotInfo[0] + '_' + assetName + '_' + shotInfo[2] + assetOtherKey + mayaType
                if os.path.exists(fileOther):
                    # 先检测本文件
                    sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                    if shotInfo[0] == u'mi':
                        import Other.minitiger.mi_checkCommon as micc
                        reload(micc)
                        INS_miCT = micc.sk_checkTools()
                        INS_miCT.checkCacheSetAdd()
                    else:
                        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                    localModelObjs = []
                    localFaceNum = []
                    localVertexNum = []
                    localUVsNum = {}
                    localUInfo = {}
                    localVInfo = {}
                    anotherModelObjs = []
                    anotherFaceNum = []
                    anotherVertexNum = []
                    anotherUVsNum = {}
                    anotherUInfo = {}
                    anotherVInfo = {}
                    # 无论做不做Cache，都要检测MODEL组下的物体
                    localModelGrps = mc.listRelatives('MODEL', ad=1, type='transform', f=1)
                    if not localModelGrps:
                        localModelGrps = []
                    localModelMeshes = mc.listRelatives('MODEL', ad=1 ,type='mesh', f=1)
                    if localModelMeshes:
                        for mesh in localModelMeshes:
                            if mc.getAttr(mesh + '.intermediateObject'):
                                continue
                            obj = mc.listRelatives(mesh, p=1, type='transform', f=1)
                            if not obj:
                                continue
                            obj = obj[0]
                            if noNeedSign:
                                checkSign = 0
                                for sign in noNeedSign:
                                    if sign not in obj:
                                        checkSign +=  1
                                if checkSign == len(noNeedSign):
                                    localModelObjs.append(obj)
                    if localModelObjs:
                        localModelObjs = list(set(localModelObjs))
                    localCacheObjs = localModelObjs
                    # 记录faceNum，vertex，uvs
                    if localCacheObjs:
                        for checkObj in localCacheObjs:
                            localFaceNum.append(mc.polyEvaluate(checkObj, face=1))
                            localVertexNum.append(mc.polyEvaluate(checkObj, vertex=1))
                            if UVCheck:
                                localUVsNum[checkObj] = mc.polyEvaluate(checkObj, uvcoord=1)
                                UVInfo =self.getObjUVInfos(checkObj,targetType = 'now')
                                localUInfo[checkObj] = UVInfo[0]
                                localVInfo[checkObj] = UVInfo[1]
                    # 对比位移和pivot信息
                    localTransInfors = self.getObjsTransInfos(localModelGrps)
                    # 打开另一半文件并检测
                    print '----------otherFile'
                    print fileOther
                    mc.file(fileOther, open=1, f=1)
                    sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                    if shotInfo[0] == u'mi':
                        import Other.minitiger.mi_checkCommon as micc
                        reload(micc)
                        INS_miCT = micc.sk_checkTools()
                        INS_miCT.checkCacheSetAdd()
                    else: sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                    # 无论做不做Cache，都要检测MODEL组下的物体
                    anotherModelGrps = mc.listRelatives('MODEL', ad=1, type='transform', f=1)
                    if not anotherModelGrps:
                        anotherModelGrps = []
                    anotherModelMeshes = mc.listRelatives('MODEL', ad=1 , type='mesh', f=1)
                    if anotherModelMeshes:
                        for mesh in anotherModelMeshes:
                            if mc.getAttr(mesh + '.intermediateObject'):
                                continue
                            obj = mc.listRelatives(mesh, p=1, type='transform', f=1)
                            if not obj:
                                continue
                            obj = obj[0]
                            if noNeedSign:
                                checkSign = 0
                                for sign in noNeedSign:
                                    if sign not in obj:
                                        checkSign +=  1
                                if checkSign == len(noNeedSign):
                                    anotherModelObjs.append(obj)
                    if anotherModelObjs:
                        anotherModelObjs = list(set(anotherModelObjs))
                    anotherCacheObjs = anotherModelObjs
                    # 记录faceNum，vertex，uvs
                    if anotherCacheObjs:
                        for checkObj in anotherCacheObjs:
                            anotherFaceNum.append(mc.polyEvaluate(checkObj, face=1))
                            anotherVertexNum.append(mc.polyEvaluate(checkObj, vertex=1))
                            if UVCheck:
                                anotherUVsNum[checkObj] = mc.polyEvaluate(checkObj, uvcoord=1)
                                UVInfo =self.getObjUVInfos(checkObj,targetType = 'other')
                                anotherUInfo[checkObj] = UVInfo[0]
                                anotherVInfo[checkObj] = UVInfo[1]
                    # 对比位移和pivot信息
                    otherTransInfos = self.getObjsTransInfos(anotherModelGrps)
                    # 返回文件
                    if saveMode:
                        mc.file(fileName, open=1, f=1)
                    # 检测阶段
                    # 第一阶段|数量对比处理
                    checkObjNum = 0
                    if len(localModelObjs) != len(anotherModelObjs):
                        difInfo = difInfo + u'MoldeMeshNum_Dif' + '\n'
                        checkObjNum = 1
                    if checkObjNum:
                        print '---------------------------------------'
                        print difInfo
                        errorInfos = [difInfo]
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                        #mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                    # 第二阶段尝试
                    # 此时数量都相等,开始第二阶段检测
                    checkNameDif = 0
                    # 第二阶段|cache处理异常名字
                    difLocalCacheNameInfo = []
                    difAnotherCacheNameInfo = []
                    if cacheType:
                        if localCacheObjs:
                            for cacheObj in localCacheObjs:
                                if cacheObj not in anotherCacheObjs:
                                    difLocalCacheNameInfo.append(cacheObj)
                            for cacheObj in anotherCacheObjs:
                                if cacheObj not in localCacheObjs:
                                    difAnotherCacheNameInfo.append(cacheObj)
                    # 第二阶段|anim处理异常ili d 名字
                    difLocalAnimNameInfo = []
                    if difLocalCacheNameInfo or difLocalAnimNameInfo:
                        if difLocalCacheNameInfo:
                            tempInfo = u'------------------[cache][本文件][异常不同名字][如下]------------------'
                            print tempInfo
                            errorInfos.append(tempInfo)
                            for info in difLocalCacheNameInfo:
                                print info
                                errorInfos.append(info)
                            tempInfo = u'------------------[cache][另文件][异常不同名字][如上]------------------'
                            print tempInfo
                            errorInfos.append(tempInfo)
                            for info in difAnotherCacheNameInfo:
                                print info
                                errorInfos.append(info)
                        checkNameDif = 1
                    # 第二阶段|Model处理异常名字
                    difLocalModelNameInfo = []
                    difAnotherModelNameInfo = []
                    if localModelObjs:
                        for localObj in localModelObjs:
                            if localObj not in anotherModelObjs:
                                difLocalModelNameInfo.append(localObj)
                        for anotherObj in anotherModelObjs:
                            if anotherObj not in localModelObjs:
                                difAnotherModelNameInfo.append(anotherObj)
                    if difLocalModelNameInfo or difAnotherModelNameInfo:
                        tempInfo = u'------------------[Model][本文件][异常不同名字][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in difLocalModelNameInfo:
                            print info
                            errorInfos.append(info)
                        tempInfo = u'------------------[Model][另文件][异常不同名字][如上]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in difAnotherModelNameInfo:
                            print info
                            errorInfos.append(info)
                        checkNameDif = 1
                    if checkNameDif:
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                        #mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                    # 第三阶段|cache物体和anim物体 faceNum，vertexNum，UV对比
                    faceEList = []
                    vertexEList = []
                    uvEList = []
                    uvInfoEList = []
                    checkIIState = 0
                    # [注意]物体点线面异常对比，是在物体列表数量一致后进行的
                    if cacheType and (not difLocalCacheNameInfo) and localCacheObjs:
                        for j in range(len(localCacheObjs)):
                            localID = j
                            anotherID = anotherCacheObjs.index(localCacheObjs[j])
                            if localFaceNum[localID] != anotherFaceNum[anotherID]:
                                faceEList.append(localCacheObjs[localID])
                                checkIIState = 1
                            if localVertexNum[localID] != anotherVertexNum[anotherID]:
                                vertexEList.append(localCacheObjs[localID])
                                checkIIState = 1
                    if UVCheck and localUVsNum.keys():
                        for checkKey in localUVsNum.keys():
                            if checkKey not in anotherUVsNum.keys():
                                continue
                            if localUVsNum[checkKey] != anotherUVsNum[checkKey]:
                                uvEList.append(checkKey)
                                checkIIState = 1
                            else:
                                UVError = 0
                                if (localUInfo[checkKey] != anotherUInfo[checkKey]) or (localVInfo[checkKey] != anotherVInfo[checkKey]):
                                    for checkNum in range(len(localUInfo[checkKey])):
                                        UDif = abs(localUInfo[checkKey][checkNum] - anotherUInfo[checkKey][checkNum])
                                        VDif = abs(localVInfo[checkKey][checkNum] - anotherVInfo[checkKey][checkNum])
                                        if UDif > 1 or VDif > 1:
                                            UVError = 1
                                            break
                                if UVError:
                                    uvInfoEList.append(checkKey)
                                    checkIIState = 1
                    if faceEList and cpState:
                        tempInfo = u'------------------[cache][异常Face][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in faceEList:
                            print info
                            errorInfos.append(info)
                        print u'------------------[cache][异常Face][如上]------------------'
                    if vertexEList and cpState:
                        tempInfo = u'------------------[cache][Vertext][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in vertexEList:
                            print info
                            errorInfos.append(info)
                        print u'------------------[cache][Vertext][如上]------------------'
                    if uvEList and cpState:
                        tempInfo = u'------------------[cache][UV point num][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in uvEList:
                            print info
                            errorInfos.append(info)
                        print u'------------------[cache][UV point num][如上]------------------'
                    if uvInfoEList and cpState:
                        tempInfo = u'------------------[cache][UV posistion][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in uvInfoEList:
                            print info
                            errorInfos.append(info)
                        print u'------------------[cache][UV posistion][如上]------------------'
                    if checkIIState:
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                        #mc.error(u'\n======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                    # 第四阶段位移pivot出入
                    difTransInfo = []
                    #print '-------TransInfo'
                    #print localTransInfors
                    #print otherTransInfos
                    localObjKeys = localTransInfors.keys()
                    otherObjKeys = otherTransInfos.keys()
                    limitValue = pow(10,self.pointLimit)
                    rangeNum = 9
                    # 不检测显示隐藏
                    if shotInfo[0] in ['mi']:
                        rangeNum = 9
                    for checkKey in localObjKeys:
                        if checkKey not in otherObjKeys:
                            continue
                        localInfos = localTransInfors[checkKey]
                        otherInfos = otherTransInfos[checkKey]
                        errorState = 0
                        #for num in range(len(localInfos)):
                        for num in range(rangeNum):
                            if abs(localInfos[num] - otherInfos[num]) < limitValue:
                                continue
                            print '------------transValueInfo'
                            print localInfos[num]
                            print otherInfos[num]
                            errorState = 1
                        if errorState:
                            difTransInfo.append(checkKey)
                    if difTransInfo :
                        tempInfo = u'------------------[位移|轴心对比异常][如下]------------------'
                        print tempInfo
                        errorInfos.append(tempInfo)
                        for info in difTransInfo:
                            print info
                            errorInfos.append(info)
                        print u'------------------[位移|轴心对比异常][如上]------------------'
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                    if errorInfos:
                        print '\n\n==========================================\n'
                        for info in errorInfos:
                            print info
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作=========\n'
                        mc.error(u'\n======本素材rg和tx版本有出入，请前期和设置协商共同处理======\n')
                    print u'=====================AnimRender版本检测完毕====================='
                else:
                    pass
            else:
                mc.error(u'==============================找不到对应Asset,请检查文件名==============================')
        else:
            mc.error(u'==============================找不到对应Asset,请检查文件名==============================')
        print '-------------[rgCtx]end-------------'
        print time.strftime("%Y-%m-%d %H:%M:%S")

    # ------------------------------#
    # 记录清单的transform和pivot属性
    def getObjsTransInfos(self,objList):
        transInfos = dict()
        for checkObj in objList:
            transInfos[checkObj] = [0,0,0,0,0,0,0,0,0]
            if not mc.ls(checkObj):
                continue
            tx = mc.getAttr(checkObj + '.tx')
            ty = mc.getAttr(checkObj + '.ty')
            tz = mc.getAttr(checkObj + '.tz')
            rx = mc.getAttr(checkObj + '.rx')
            ry = mc.getAttr(checkObj + '.ry')
            rz = mc.getAttr(checkObj + '.rz')
            sx = mc.getAttr(checkObj + '.sx')
            sy = mc.getAttr(checkObj + '.sy')
            sz = mc.getAttr(checkObj + '.sz')
            v = mc.getAttr(checkObj + '.v')
            localP = mc.xform(checkObj,rotatePivot = 1, q = 1)
            localS = mc.xform(checkObj,scalePivot = 1, q = 1)
            transInfos[checkObj] = [tx,ty,tz,rx,ry,rz,sx,sy,sz,v,localP[0],localP[1],localP[2],localS[0],localS[1],localS[2]]
        return transInfos

    #------------------------------#
    # 记录UV点信息
    def getObjUVInfos(self,checkObj,underLevel = 2,targetType = 'now'):
        UList = []
        VList = []
        UVNumList = mc.polyEvaluate(checkObj, uvcoord=1)
        if not UVNumList:
            return [0,0]
        import math
        try:
            for idNum in range(UVNumList):
                uvP = '%s.uv[%s]'%(checkObj,str(idNum))
                uvInfo = mc.getAttr(uvP)[0]
                uInfo = int(uvInfo[0] * math.pow(10,underLevel))
                vInfo = int(uvInfo[1] * math.pow(10,underLevel))
                UList.append(uInfo)
                VList.append(vInfo)
            return [UList,VList]
        except:
            print '-------[UVInfo]Get Error'
            if targetType in ['now']:
                print '[file]:Now'
            if targetType in ['other']:
                print '[file]:Other'
            print checkObj
            mc.error

    #------------------------------#
    # 移除豁免
    def removeNoCheckState(self,checkType = ''):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projSimp = shotInfos[0]
        if checkType in ['rgtxIgnore']:
            assetID = shotInfos[1]
            if shotInfos[0] in ['csl']:
                projFull = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(projSimp)
                #exCmd = "SELECT isnull(A.rgtxIgnore,'0') as rgtxIgnoreNew FROM idmtPlex_%s.dbo.[TB_Asset] A WHERE A.asset_name ='%s'"%(projFull,assetID)
                exCmd = "update TA set TA.rgtxIgnore=0 from idmtPlex_%s.dbo.tb_asset TA where TA.asset_name ='%s'"%(projFull,assetID)
                #exCmd = "\nselect '01' as resultText"
                cnxn = sk_infoConfig.sk_infoConfig().checkServerConnect(projFull)
                cursor = cnxn.cursor()
                errorState = 1
                try:
                    cursor.execute(exCmd)
                    cnxn.commit()
                    errorState = 0
                finally:
                    cursor.close()
                    cnxn.close()
                if errorState:
                    errorInfo = u'\n-------数据库状态更新失败，请联系TD-------\n'
                    print errorInfo
                    mc.error()
            else:
                dataPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server = 1,infoMode = 1).split('EyeLight/')[0]
                localPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server = 0,infoMode = 1)
                serverTxt = dataPath + checkType + '.txt'
                localTxt = localPath + checkType + '.txt'
                import os
                if os.path.exists(serverTxt):
                    self.removeTxtInfos(serverTxt,localTxt,assetID)

    # 更新服务器端清单
    def removeTxtInfos(self,serverTxt,localTxt,removeInfo):
        readLines = sk_infoConfig.sk_infoConfig().checkFileRead(serverTxt)
        removeState = 0
        needInfos = []
        for info in readLines:
            if info == removeInfo:
                removeState = 1
                continue
            needInfos.append(info)
        if not removeState:
            return
        sk_infoConfig.sk_infoConfig().checkFileWrite(localTxt,needInfos)
        updateCMD = 'zwSysFile "copy" ' + '"' + (localTxt) + '"' + ' ' + '"' + (serverTxt) + '"' + ' true'
        mel.eval(updateCMD)

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用：自动生成animModel及masterMode】
    # 0.仅在texture阶段使用
    # Author  : 沈  康
    # Data    : 2013_05_20 - 2013_05_
    # ------------------------------#
    # ------------------------------#
    # 主函数，处理切换
    #　CHR PROP  rg -> arnoldNodesnim     (sys copy)
    #　CHR PROP  tx -> render    (清理历史)
    # SET       tx -> anim      (脚本处理，给个普通贴图)
    # SET       tx -> render    (sys copy)
    # cacheMode    0 tx另存 render | 1 tx清历史存为render
    # assetSpecial    0 默认是文件名第二个字段的第一个字符为asset类型 |1 默认是文件名第二个字段的第二个字符为asset类型
    def checkTexTransformtMo(self, checkIn=0, backTx=1, cacheMode=1, assetSpecial=0):
        # 用户名
        import os
        import sk_sceneTools
        reload(sk_sceneTools)
        import sk_checkTools
        reload(sk_checkTools)
        userName = os.environ['USERNAME']
        # 项目名
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 处理文件内ca模型渲染开启属性
        self.checkCacheObjRenderState()

        self.checkRenderObjRenderState(1, 0, 0)
        # 另存到temp文件夹
        pathLocal = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        mc.file(rename=fileLocal)
        mc.file(save=1, force=1)
        # 仅允许tx阶段使用
        # 先输出smoothSet信息
        self.checkAssetSmoothSetUpdate()
        # info = self.checkShotInfo()
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(info[0])
        fileName = mc.file(query=1, exn=1)
        # rootGrp检测
        rootGrp = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()[0]
        if info[3].split('.')[0] == 'tx'and 'MODEL' not in rootGrp:
            # 检测 材质着色
            self.checkTextureModelShader()
            # 【规定】有an的，保留MODEL组；没an的，保留MODEL组并清历史
            # 角色类全cache处理
            # 对道具类可能存在的超大型物体，部分cache部分anim，根据情况处理
            if info[1][assetSpecial] not in ['s', 'S']:
                # set检测
                setType = sk_checkTools.sk_checkTools().checkSetsType()
                # setType 有4种情况 [0,0];[0,1];[1,0];[1,1]
                # 无_ct_an标记的cache文件
                if setType == [1, 0]:
                    for i in range(2):
                        mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                        # 转 animModel
                        if i == 0:
                            pass
                            '''
                            self.checkTexNoAC2AnimMo('anim',assetSpecial)
                            if checkIn == 1:
                                print(u'=====================[Check in] Start=====================')
                                # checkOut
                                newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                                #print checkOutCmd
                                mel.eval(checkOutCmd)
                                # checkIn
                                mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                            print(u'=====================创建【AnimFile】完毕=====================')
                            '''
                        # 转 cacheModel
                        else:
                            if cacheMode:
                                print '----------------001CacheMode----------------'
                                self.checkTexMo2CacheMo(checkIn, assetSpecial)
                            else:
                                print '----------------002AnimMode----------------'
                                self.checkTexNoAC2AnimMo('render', assetSpecial)
                            if checkIn == 1:
                                print(u'=====================[Check in] Start=====================')
                                # checkOut
                                newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                                # print checkOutCmd
                                mel.eval(checkOutCmd)
                                # checkIn
                                mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                            print(u'=====================创建【RenderFile】完毕=====================')
                # 有an的文件，以及什么都无的文件
                if setType[1] == 1 or setType == [0, 0]:
                    '''
                    # 另存anim
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                    self.checkTexNoAC2AnimMo('anim',assetSpecial)
                    if checkIn == 1:
                        print(u'=====================[Check in] Start=====================')
                        # checkOut
                        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        mel.eval(checkOutCmd)
                        # checkIn
                        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                    print(u'=========【非cache文件，直接输出anim文件。复制到render文件】=========')
                    print(u'=====================创建【AnimFile】完毕=====================')
                    '''
                    # 另存render
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                    self.checkTexNoAC2AnimMo('render', assetSpecial)
                    if checkIn == 1:
                        print(u'=====================[Check in] Start=====================')
                        # checkOut
                        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        # print checkOutCmd
                        mel.eval(checkOutCmd)
                        # checkIn
                        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                    print(u'=========【非cache文件，清理ca的history。复制到render文件】=========')
                    print(u'=====================创建【RenderFile】完毕=====================')
            # 对set组不做cache处理
            # 对set组，判断参考在时进行参考替换
            else:
                # 另存anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                print(u'=====================创建【RenderFile】完毕=====================')
            # 返回tx文件
            if backTx == 1:
                print fileName
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
            print(u'=====================【返回 tx 文件】=====================')
        else:
            # 要报错处理,check in 用
            print(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')
            print(u'=====================【！！！【tx】【MODEL】处于第二层！！！】=====================')
            mc.error(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')

    # ------------------------------#
    # 【特殊 】:  SK版本
    # 【角色】 rg -> anim | tx -> render
    # 【设置】rg -> anim render
    # 【场景】rx -> anim render
    # 【注意】将参考还原
    # ------------------------------#
    def checkSKTransformtMo(self, checkIn=0, backTx=1, cacheMode=1, assetSpecial=1):
        # 用户名
        import os
        import sk_sceneTools
        reload(sk_sceneTools)
        import sk_checkTools
        reload(sk_checkTools)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        userName = os.environ['USERNAME']
        # 项目名
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 处理文件内ca模型渲染开启属性
        self.checkCacheObjRenderState()
        self.checkRenderObjRenderState(1, 0, 0)
        # 另存到temp文件夹
        pathLocal = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        mc.file(rename=fileLocal)
        mc.file(save=1, force=1)
        # 仅允许tx阶段使用
        # 先输出smoothSet信息
        self.checkAssetSmoothSetUpdate()
        # info = self.checkShotInfo()
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(info[0])
        fileName = mc.file(query=1, exn=1)
        # rootGrp检测
        rootGrp = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()[0]
        # 角色类
        if info[1][assetSpecial] == 'c' and 'MODEL' not in rootGrp:
            # 只对tx处理
            if info[3].split('.')[0] == 'rg':
                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                print(u'=====================创建【RenderFile】完毕=====================')

                # 处理anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                # 处理贴图文件
                fileNodes = mc.ls(type='file')
                for node in fileNodes:
                    mc.setAttr((node + '.fileTextureName'), '', type='string')
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=====================创建【AnimFile】完毕=====================')

                # 返回tx参考
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                sk_referenceConfig.sk_referenceConfig().checkRefReplace(['/master/', '_ms_render.'], ['/texture/', '_tx.'])
        # 道具类
        if info[1][assetSpecial] == 'p' and 'MODEL' not in rootGrp:
            # 只对tx处理
            if info[3].split('.')[0] == 'rg':
                # 另存anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By RG File\"')
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By RG File\"')
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                print(u'=====================创建【RenderFile】完毕=====================')
                # 返回rg参考
                sk_referenceConfig.sk_referenceConfig().checkRefReplace(['/master/', '_ms_render.'], ['/rigging/', '_rg.'])
        # 场景类
        if info[1][assetSpecial] in ['s', 'S'] and 'MODEL' not in rootGrp:
            # 只对tx处理
            if info[3].split('.')[0] == 'tx':
                # 另存anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                # check in
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(u'=====================[Check in] Start=====================')
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                print(u'=====================创建【RenderFile】完毕=====================')
                # 返回rg参考
                sk_referenceConfig.sk_referenceConfig().checkRefReplace(['/master/', '_ms_render.'], ['/texture/', '_tx.'])

    # ------------------------------#
    # 【执行 】:  texModel - > animModel
    # ------------------------------#
    # 执行：单独另存导出清理
    # assetSpecial 默认文件名第二个字段的第一个字符，某些项目除外，如SK，用第二个字符
    def checkTexNoAC2AnimMo(self, fileType, assetSpecial=0):
        import sk_sceneTools
        reload(sk_sceneTools)
        '''
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        if fileType == 'anim':
            fileName = path + info[0] + '_' + info[1] + '_' + info[2] + '_ms_anim' + fileFormat
        if fileType == 'render':
            fileName = path + info[0] + '_' + info[1] + '_' + info[2] + '_ms_render' + fileFormat
        # 文件清理开始
        mc.file(rename=fileName)
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(info[0])
        mc.file(force=1, options="v=0" , type=fileTypeFull , save=1)
        '''
        #rootGrp = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()[0]
        # 取MODEL组上一级物体导出
        rootGrp = []
        MODELGrp = ''
        if mc.ls('MODEL'):
            MODELGrp = 'MODEL'
            upGrp = mc.listRelatives(MODELGrp, p=1, type='transform')
            if upGrp:
                rootGrp = upGrp
            else:
                rootGrp = ['MODEL']

        '''
        if not rootGrp:
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
        '''
        # 清理，导出
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_' + fileType + fileFomat

        if not rootGrp:
            print '\n'
            print u'---'
            print u'===没发现MODEL组，请检查文件==='
            mc.error(u'===没发现MODEL组，请检查文件===')

        mc.select(rootGrp)
        # 场景文件加选显示层
        if shotInfo[1][assetSpecial] in ['s', 'S']:
            # 显示层
            displayLayers = mc.listConnections('layerManager.displayLayerId')
            needLayer = []
            if displayLayers:
                for layer in displayLayers:
                    if 'defaultLayer' not in layer:
                        needLayer.append(layer)
            if needLayer:
                mc.select(needLayer, add=1)
        # set组
        quickSets = mc.ls(type='objectSet')
        if quickSets:
            for obj in quickSets:
                #info = mc.listConnections((obj + '.message'), d=1)
                info = mc.listConnections((obj + '.message'), d=1, type='objectSet')
                if not info and mc.nodeType(obj) == 'objectSet':
                    mc.select(obj, add=1, ne=1)
        # 导出
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        mc.file(fileName, force=1, options="v=0", type=fileTypeFull, preserveReferences=1, exportSelected=1)

        # 打开CacheMODEL新文件
        mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)

        # CacheSet
        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()

        # AnimSet
        sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()

        # 合并Set
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache", "ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim", "ZM")

        # 处理cache环境变量
        self.checkCacheEnvPath()

        import sk_referenceConfig
        reload(sk_referenceConfig)

        # anim着色
        if fileType == 'anim':
            # set类
            if shotInfo[1][assetSpecial] in ['s', 'S']:
                # 参考替换
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                rfnNodeLv1 = refInfos[0][0]
                rfnPathLv1 = refInfos[1][0]
                # 导入参考，注意将_ms_anim替换成_ms_render
                # OTC内的参考不参与处理
                # shareNode只能对第一级reference处理。。。
                if rfnNodeLv1:
                    for i in range(len(rfnNodeLv1)):
                        pathLower = rfnPathLv1[i].lower()
                        newPath = pathLower.replace('texture', 'master')
                        newPath = newPath.replace('_tx.', '_ms_anim.')
                        mc.file(newPath, loadReference=rfnNodeLv1[i])
            # 基本着色
            if shotInfo[1][assetSpecial] != 'c':
                self.checkDefaultShader()

        # render删除不参与渲染物体
        # 这里算法可以加速
        if fileType == 'render':
            # set类
            if shotInfo[1][assetSpecial] in ['s', 'S']:
                # 参考替换
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                rfnNodeLv1 = refInfos[0][0]
                rfnPathLv1 = refInfos[1][0]
                # 导入参考，注意将_ms_anim替换成_ms_render
                # OTC内的参考不参与处理
                # shareNode只能对第一级reference处理。。。
                if rfnNodeLv1:
                    for i in range(len(rfnNodeLv1)):
                        pathLower = rfnPathLv1[i].lower()
                        newPath = pathLower.replace('texture', 'master')
                        newPath = newPath.replace('_tx.', '_ms_render.')
                        mc.file(newPath, loadReference=rfnNodeLv1[i])
            # 删除_si_和_nr_物体
            grps = mc.ls(type='transform')
            for grp in grps:
                if '_si_' in grp or '_nr_' in grp:
                    # 对参考进行pass
                    try:
                        mc.delete(grp)
                    except:
                        pass

        # 整理文件
        # self.checkAddColorShader(assetSpecial)

        # displayeLayer及renderPlayer删除
        # 对set不清理显示层
        if shotInfo[1][assetSpecial] not in ['s', 'S']:
            sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        # 清理节点
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean()

        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if joints:
            for joint in joints:
                if mc.getAttr(joint + '.drawStyle', l=1):
                    pass
                else:
                    mc.setAttr((joint + '.drawStyle'), 2)

        # 隐藏晶格
        lattices = mc.ls(type='lattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                mc.setAttr((grp[0] + '.v'), 0)
        lattices = mc.ls(type='baseLattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                try:
                    mc.setAttr((grp[0] + '.v'), l=0)
                except:
                    pass
                mc.setAttr((grp[0] + '.v'), 0)

        # 锁,但SET类不处理
        if u'%s_%s' % (shotInfo[0], shotInfo[1]) != u'do5_p003001Vegetation1' and shotInfo[1][assetSpecial] not in ['s', 'S']:
            objs = ['MODEL']
            sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 1)
            sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
            sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()

        # 保存anim
        mc.file(force=1, save=1)

    # ------------------------------#
    # 执行 :  texModel - > cacheModel
    # ------------------------------#
    # assetSpecial 默认文件名第二个字段的第一个字符，某些项目除外，如SK，用第二个字符
    def checkTexMo2CacheMo(self, checkin=1, assetSpecial=0):
        import sk_smoothSet
        reload(sk_smoothSet)
        # MODEL物体清理历史
        import sk_sceneTools
        reload(sk_sceneTools)
        # CacheSet
        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
        meshes = mc.sets('MESHES', q=1)

        mc.select(meshes)
        mel.eval('DeleteAllHistory')
        mc.select(cl=1)

        # 删除非MODEL
        rootGrp = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()[0]
        grps = mc.listRelatives(rootGrp, c=1, f=1)
        for grp in grps:
            if '|MODEL' not in grp:
                mc.delete(grp)

        # 删除_si_和_nr_物体
        grps = mc.ls(type='transform')
        for grp in grps:
            if '_si_' in grp or '_nr_' in grp:
                mc.delete(grp)

        # 清理，导出
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_render' + fileFomat
        # 选取物体
        mc.select(rootGrp)
        # set组加选
        quickSets = mc.ls(type='objectSet')
        if quickSets:
            for obj in quickSets:
                #info = mc.listConnections((obj + '.message'), d=1)
                info = mc.listConnections((obj + '.message'), d=1, type='objectSet')
                if not info and mc.nodeType(obj) == 'objectSet':
                    mc.select(obj, add=1, ne=1)
        # 处理导出
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        mc.file(fileName, force=1, options="v=0", type=fileTypeFull, preserveReferences=1, exportSelected=1)

        # 打开CacheMODEL新文件
        mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)

        # 清理ShapeOrig
        shapes = mc.ls(type='mesh')
        for mesh in shapes:
            if mc.getAttr(mesh + '.intermediateObject'):
                mc.delete(mesh)

        # 重建cacheSet
        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()

        # 重建AnimSet
        sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()

        # 重建smoothSet
        if checkin:
            serverSmoothSetInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=1,infoMode=3)
            objsSmoothSet_lv0 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_0.txt')
            if objsSmoothSet_lv0:
                needObjs = []
                for obj in objsSmoothSet_lv0:
                    if mc.ls(obj):
                        objName = mc.ls(obj, l=1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv0 = needObjs
                    mc.select(objsSmoothSet_lv0)
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(smoothLevel = 0)
            objsSmoothSet_lv1 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_1.txt')
            if objsSmoothSet_lv1:
                needObjs = []
                for obj in objsSmoothSet_lv1:
                    if mc.ls(obj):
                        objName = mc.ls(obj, l=1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv1 = needObjs
                    mc.select(objsSmoothSet_lv1)
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(smoothLevel = 1)
            objsSmoothSet_lv2 = sk_infoConfig.sk_infoConfig().checkFileRead(serverSmoothSetInfoPath + 'smooth_2.txt')
            if objsSmoothSet_lv2:
                needObjs = []
                for obj in objsSmoothSet_lv2:
                    if mc.ls(obj):
                        objName = mc.ls(obj, l=1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv2 = needObjs
                    mc.select(objsSmoothSet_lv2)
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(smoothLevel = 2)
            mc.select(cl=1)

        # 清理
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean()

        # displayeLayer及renderPlayer删除
        # 对set不清理显示层
        if shotInfo[1][assetSpecial] not in ['s', 'S']:
            sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        # 合并Set
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache", "ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim", "ZM")

        # 锁物体
        if u'%s_%s' % (shotInfo[0], shotInfo[1]) != u'do5_p003001Vegetation1' and shotInfo[1][assetSpecial] not in ['s', 'S']:
            objs = [rootGrp]
            sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 1)
            sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
            sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()

    #------------------------------------------------#
    # mo,tx MODEL组解锁
    def checkMODELUnlock(self):
        ModelGrp = mc.ls('MODEL',l=1)
        objs = mc.listRelatives(ModelGrp, p=1 , type='transform', f=1)
        if not objs:
            return
        import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 0)
        sk_sceneTools.sk_sceneTools().checkUnlockMSHV()

    # 刷新材质球
    def deformerAfterObjectSetMod(self,printState = 0):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        meshes = mc.ls(type='mesh', l=1)
        needObjs = []
        # cleanup ref
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

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【Asset 材质信息上传】
    #  Author  : 沈  康
    #  Data    : 2015_07_30
    #------------------------------#
    def checkAssetMetailUpdate(self):
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        fileInfo = fileName.split('_')
        # MaterialInfos
        checkObjs = mc.ls(type = 'mesh',l=1)
        if not checkObjs:
            return
        checkObjs = mc.listRelatives(checkObjs,p=1,type = 'transform',f=1)
        checkObjs = list(set(checkObjs))
        MatLists = self.checkCacheRecordMaterial(checkObjs)
        # update
        localDataPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=0,shotInfos=fileInfo,infoMode=4)[:-1]
        serverDataPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=1,shotInfos=fileInfo,infoMode=4)[:-1]

        SGKeys = MatLists.keys()
        allInfo = []

        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        recordFile = 'assetShaderInfo.txt'
        mc.sysFile(localDataPath, makeDir=True)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localDataPath + '/'+ recordFile),allInfo)

        # 上传
        sk_infoConfig.sk_infoConfig().checkServerFileSystem('copy',(localDataPath + '/'+ recordFile),(serverDataPath + '/'+ recordFile))
        print serverDataPath
        print u'=====================[Updating Info To Server] [%s] Done====================='%fileInfo[1]

    #------------------------------#
    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] ,cacheMode = 1 ):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            for obj in checkObjs:
                mesh = mc.listRelatives(obj,ni=1,type = 'mesh',c =1,f=1 )[0]
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
                connectObjsSG = self.checkFaceMode(connectObjsSG)
                MatLists[node] = connectObjsSG
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

    # ------------------------------#
    # 执行 :  默认着色标准lambert
    # ------------------------------#
    def checkDefaultShader(self):
        # 默认着色
        shapes = mc.ls(type='mesh', l=1)
        shapeNeed = []
        for shape in shapes:
            if '|MODEL|' in mc.ls(shape, l=1)[0]:
                # 参考物体不着色
                ifRef = mc.referenceQuery(shape, isNodeReferenced=1)
                if not ifRef:
                    shapeNeed.append(shape)
        shapes = shapeNeed
        if shapes:
            shader = mc.shadingNode('lambert', asShader=True, name='IDMT_Shader_Base')
            shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(shader + '_SG'))
            mc.connectAttr(('%s.%s') % (shader, 'outColor'), ('%s.%s') % ((shaderSG), 'surfaceShader'), f=True)
            try:
                mc.sets(shapes, e=1, forceElement=shaderSG)
            except:
                print u'===注意，进入此环节意味着有物体无法着色==='
                print u'===最下端的物体即为无法成功着色的物体==='
                for mesh in shapes:
                    print mesh.split('|')[-1]
                    mc.sets(mesh, e=1, forceElement=shaderSG)
            # 清理节点
            import sk_sceneTools
            reload(sk_sceneTools)
            sk_sceneTools.sk_sceneTools().checkDonotNodeClean()

    # ------------------------------#
    # 执行 :  整理asset文件内信息规范
    # ------------------------------#
    # assetSpecial 默认是文件名第二段的第一个字符，特殊情况可以用别的字符，如SK项目
    def checkAddColorShader(self, assetSpecial=0):
        import sk_sceneTools
        reload(sk_sceneTools)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        # CacheSet
        sk_sceneTools.sk_sceneTools().checkCacheSetAdd()

        # AnimSet
        sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()

        # 合并Set
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache", "ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim", "ZM")

        # 隐藏瞳孔
        noNeedObjs = mc.ls('*_si_*', type='transform')
        if noNeedObjs:
            for obj in noNeedObjs:
                mc.setAttr((obj + '.v'), 0)

        # 新版本
        # self.checkShaderColorImport()

        # displayeLayer及renderPlayer删除
        if shotInfo[1][assetSpecial] not in ['s', 'S']:
            sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if joints:
            for joint in joints:
                if mc.getAttr(joint + '.drawStyle', l=1):
                    pass
                else:
                    mc.setAttr((joint + '.drawStyle'), 2)

        # 隐藏晶格
        lattices = mc.ls(type='lattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                mc.setAttr((grp[0] + '.v'), 0)
        lattices = mc.ls(type='baseLattice', l=1)
        if lattices:
            for lattice in lattices:
                grp = mc.listRelatives(lattice, p=1, f=1)
                mc.setAttr((grp[0] + '.v'), 0)

        # 锁,但对参考物体不使用
        if shotInfo[1][assetSpecial] not in ['s', 'S']:
            if mc.ls('MODEL', type='transform'):
                objs = ['MODEL']
                sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 1)
                sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()

    # ------------------------------#
    # tx check in shader
    # tx文件测试，所有模型重新赋予材质，失败则报错
    def checkTextureModelShader(self):
        meshes = mc.ls(type='mesh', l=1)
        if meshes:
            # 创建新渲染层
            if mc.ls('food_shaderLayer_test'):
                mc.delete('food_shaderLayer_test')
            # 获取MODEL下的
            needObjs = []
            for mesh in meshes:
                if '|MODEL|' in mesh:
                    needObjs.append(mc.listRelatives(mesh, p=1, f=1)[0])
            needObjs = list(set(needObjs))
            # 创建层
            if needObjs:
                errorObjs = []
                mc.createRenderLayer(needObjs, name='food_shaderLayer_test', noRecurse=1, makeCurrent=1)
                # 创建材质
                shaderMain = mc.shadingNode('lambert', asShader=True, name='food_shader_test')
                shaderMianSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='food_shader_test_SG')
                mc.connectAttr((shaderMain + '.outColor'), (shaderMianSG + '.surfaceShader'))
                for obj in needObjs:
                    mesh = mc.listRelatives(obj, ni=1, s=1)
                    if not mesh:
                        continue
                    mesh = mesh[0]
                    # print u'-------------'
                    # print mesh
                    try:
                        mc.sets(obj, e=1, forceElement=shaderMianSG)
                    except:
                        errorObjs.append(mesh)

                if errorObjs:
                    for errorObj in errorObjs:
                        print u'-------------'
                        print errorObj
                        print errorObj.split('|')[-1]
                    mc.error(u'>>>>>>------------以上mesh无法正常赋予材质，请回到原tx文件进行处理！！！')
                # 删除层，清理垃圾节点
                # Back To MasterLayer
                mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
                mc.delete('food_shaderLayer_test')
                # mel.eval('MLdeleteUnused')

    # ------------------------------#
    # 强行将所有SG和shader打断，并重新连接
    def checkShaderSGReConnection(self):
        # 获取有效的mesh及shader及SG节点
        SGNodes = mc.ls(type='shadingEngine')
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
                    if mc.listConnections((sgNode + '.surfaceShader'), source=1, plugs=1):
                        shaderAttr = mc.listConnections((sgNode + '.surfaceShader'), source=1, plugs=1)[0]
                    if mc.listConnections(sgNode, source=1, type='mesh'):
                        meshes = mc.listConnections(sgNode, source=1, type='mesh')
                    if shaderAttr and meshes:
                        # 删除SG节点
                        mc.delete(sgNode)
                        # 重连物体
                        newSGNode = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(sgNode))
                        mc.connectAttr((shaderAttr), (newSGNode + '.surfaceShader'))
                        mc.sets(meshes, e=1, forceElement=newSGNode)

    # ------------------------------#
    # 记录tx文件中的smoothSet  角色道具不允许重名，场景。。随遇而安
    def checkAssetSmoothSetUpdate(self):
        # 本地路径
        localInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=0,infoMode=3)
        mc.sysFile(localInfoPath, makeDir=1)
        serverInfoPath = sk_infoConfig.sk_infoConfig().checkAssetInfoPath(server=1,infoMode=3)
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 记录信息
        smoothSetNode = 'smooth_0'
        smoothObjs_lv0 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv0 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv0:
                smoothObjs_lv0 = []
        smoothSetNode = 'smooth_1'
        smoothObjs_lv1 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv1 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv1:
                smoothObjs_lv1 = []
        smoothSetNode = 'smooth_2'
        smoothObjs_lv2 = []
        if mc.ls(smoothSetNode):
            smoothObjs_lv2 = mc.sets(smoothSetNode, q=1)
            if not smoothObjs_lv2 :
                smoothObjs_lv2 = []
        # 输出信息
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_0.txt'), smoothObjs_lv0)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_0.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_0.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_1.txt'), smoothObjs_lv1)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_1.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_1.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localInfoPath + 'smooth_2.txt'), smoothObjs_lv2)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_2.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_2.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    # ------------------------------#
    # 将所有用于cache的模型render state开启
    def checkCacheObjRenderState(self):
        import sk_sceneTools
        reload(sk_sceneTools)
        cacheObjs = sk_sceneTools.sk_sceneTools().checkCacheSetObjects()
        if cacheObjs:
            for obj in cacheObjs:
                if mc.objExists(obj+'.MoA')==None:
                    shape = mc.listRelatives(obj, c=1, type='mesh', f=1)
                    if not shape:
                        return 0
                    shape = shape[0]
                    mc.setAttr((shape + '.castsShadows'), 1)
                    mc.setAttr((shape + '.receiveShadows'), 1)
                    mc.setAttr((shape + '.motionBlur'), 1)
                    mc.setAttr((shape + '.primaryVisibility'), 1)
                    mc.setAttr((shape + '.smoothShading'), 1)
                    mc.setAttr((shape + '.visibleInReflections'), 1)
                    mc.setAttr((shape + '.visibleInRefractions'), 1)
                    mc.setAttr((shape + '.doubleSided'), 1)

    # ------------------------------#
    # 将所有用于渲染的模型render state开启
    def checkRenderObjRenderState(self, pv=1, cs=0, rs=0):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if not mc.ls('MODEL'):
            return 0
        objs = mc.listRelatives('MODEL', ad=1, type='transform', f=1)
        if not objs:
            return 0
        for obj in objs:
            if '_nr_' in obj or '_si_' in obj:
                continue
            if shotInfo[0] in ['csl'] and '_p_' in obj:
                continue
            if shotInfo[0] in ['csl'] and mc.objExists(obj+'.MoA'):
                continue

            if shotInfo[0] in ['sk']:
                if 'newadd' in obj:
                    continue
            shape = mc.listRelatives(obj, s=1, ni=1, type='mesh', f=1)
            if not shape:
                continue
            shape = shape[0]
            if pv:
                mc.setAttr((shape + '.primaryVisibility'), 1)
            if cs:
                mc.setAttr((shape + '.castsShadows'), 1)
            if rs:
                mc.setAttr((shape + '.receiveShadows'), 1)

    #------------------------------#
    # 查询贴图尺寸
    def checkTextureFileSize(self,imgPath):
        import maya.OpenMaya
        img = maya.OpenMaya.MImage()
        # 读取文件
        img.readFromFile(imgPath)
        # 获取尺寸
        width = maya.OpenMaya.uIntPtr()
        height = maya.OpenMaya.uIntPtr()
        img.getSize(width, height)
        # 处理
        return width.value()

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【通用】【dy环节文件上传】
    #  Author  : 沈  康
    #  Data    : 2016_06
    #------------------------------#
    def checkDyCacheUpdate(self):
        fileName  = mc.file(exn = 1, q=1).split('/')[-1]
        shotInfos = fileName.split('_')
        shotType = sk_infoConfig.sk_infoConfig().checkShotType(fileName)
        # 路径获取
        import os
        fileNodes  = mc.ls(type = 'cacheFile') + mc.ls(type = 'AlembicNode')
        needPaths  = []
        errorPaths = []
        for node in fileNodes:
            nodeType = mc.nodeType(node)
            attrKey = ''
            if nodeType in ['cacheFile']:
                attrKey = '.cachePath'
            if nodeType in ['AlembicNode']:
                attrKey = '.abc_File'
            cachePath = mc.getAttr(node + attrKey)
            if not cachePath:
                continue
            if cachePath[-1] in ['/']:
                cachePath = cachePath[:-1]
            # 检测文件在不在
            filePath = cachePath
            if nodeType in ['cacheFile']:
                filePath += '/' + mc.getAttr('%s.cacheName'%node) +'.xml'
            if not os.path.exists(filePath):
                errorPaths.append(node)
                errorPaths.append(cachePath)
            else:
                needPaths.append(cachePath)
        if needPaths:
            needPaths = list(set(needPaths))
        if errorPaths:
            errorInfo = u'-------------[上传cache] cache路径错误,请确定目标文件是否存在,请检查-------------\n'
            print '\n--------------------'
            for node in errorPaths:
                print node
            print errorInfo
            mc.error()
        if not needPaths:
            return
        # 上传
        sourcePaths = []
        serverPaths = []
        serverPath  = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(server = 1,shotInfos = shotInfos,infoMode = 3)
        for localPath in needPaths:
            if serverPath in localPath:
                continue
            # 此处why?
            #if os.path.exists(localPath):
            #    continue
            localFolder = localPath.split('/')[-1]
            resultPath = '%s/%s'%(serverPath,localFolder)
            sourcePaths.append(localPath)
            serverPaths.append(resultPath)
            if '.' in localPath:
                updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath) + '"' + ' ' + '"' + (resultPath) + '"' + ' true'
            else:
                updateAnimCMD = 'zwSysFile "xcopy" ' + '"' + (localPath) + '"' + ' ' + '"' + (resultPath) + '"' + ' true'
            mel.eval(updateAnimCMD)
        if sourcePaths and serverPaths:
            # 整理cache节点名字
            for node in fileNodes:
                nodeType = mc.nodeType(node)
                attrKey = ''
                if nodeType in ['cacheFile']:
                    attrKey = '.cachePath'
                if nodeType in ['AlembicNode']:
                    attrKey = '.abc_File'
                cachePath = mc.getAttr(node + attrKey)
                if not cachePath:
                    continue
                if cachePath[-1] in ['/']:
                    cachePath = cachePath[:-1]
                if cachePath not in sourcePaths:
                    continue
                index = sourcePaths.index(cachePath)
                mc.setAttr((node + attrKey),serverPaths[index],type = 'string')

    #-------------------------------#
    # 重新处理rg文件
    def checkRgGrpsRebuild(self,stepType = 'rg',refMode = 0):
        # 大组摘出
        rootGrp = sk_infoConfig.sk_infoConfig().checkAssetRootGrp()
        if not mc.ls(rootGrp):
            mc.group(em = 1,name = rootGrp)
        else:
            rootGrp = mc.ls(rootGrp,l=1)[0]
            if len(rootGrp.split('|')) != 2:
                rootGrp = mc.parent(rootGrp,world = 1)[0]
        if '|' in rootGrp:
            rootGrp = rootGrp.split('|')[1]
        # MODEL组
        modelKey = 'MODEL'
        from idmt.maya.commonCore.core_baseCommon import sk_infoCore
        reload(sk_infoCore)
        errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(37)
        if not refMode:
            if not mc.ls(modelKey):
                print errorInfo
                mc.error()
            self.checkTurnRootGrpDown(modelKey,rootGrp)
        else:
            #print mc.ls('*:%s'%modelKey)
            if not mc.ls(modelKey) and not mc.ls('*:%s'%modelKey):
                print errorInfo
                mc.error()
            self.checkRefModelRootDown(modelKey,rootGrp)
        # 设置处理
        if stepType in ['rg']:
            # RIG组
            rigKey = 'RIG'
            self.checkTurnRootGrpDown(rigKey,rootGrp)
            # DEFORMERS组
            defKey = 'DEFORMERS'
            self.checkTurnRootGrpDown(defKey,rootGrp)
            # FX组
            fxKey = 'FX'
            self.checkTurnRootGrpDown(fxKey,rootGrp)

    # 指定组放到大组下
    def checkTurnRootGrpDown(self,checkKey,rootGrp):
        needGrp = checkKey
        if checkKey in ['DEFORMERS']:
            if mc.ls('DEFROMERS'):
                mc.rename('DEFROMERS','DEFORMERS')
        if not mc.ls(needGrp):
            mc.group(em = 1,name = needGrp)
            mc.parent(needGrp,rootGrp)
        else:
            needGrp = mc.ls(needGrp,l=1)[0]
            if '|%s|'%rootGrp not in needGrp:
                needGrp = mc.parent(needGrp,rootGrp)[0]
            needGrp = mc.ls(needGrp,l=1)[0]
            #print len(needGrp.split(checkKey)[0].split('|'))
            if len(needGrp.split(checkKey)[0].split('|')) != 3:
                mc.parent(needGrp,rootGrp)

    # 参考模式放大组下
    def checkRefModelRootDown(self,modelKey,rootGrp):
        checkKey = ':%s'%modelKey
        modeGrp = mc.ls('*:%s'%modelKey,l=1)[0]
        refRoot = ''
        deleteGrps = []
        for checkInfo in modeGrp.split(checkKey)[0].split('|'):
            if not checkInfo:
                continue
            checkGrp = modeGrp.split(checkInfo)[0] + checkInfo
            inr = mc.referenceQuery(checkGrp,inr = 1)
            if not inr:
                if checkGrp != '|%s'%rootGrp and '|RIG' not in checkGrp:
                    deleteGrps.append(checkGrp)
                continue
            refRoot = checkGrp
            break
        #for delGrp in deleteGrps:
        #    if mc.ls(delGrp):
        #        print delGrp
        #        mc.delete(delGrp)
        self.checkTurnRootGrpDown(refRoot.split('|')[-1],rootGrp)

    #-----------------------#
    # deformer处理属性传递连接
    #-----------------------#
    def transAttrUpdate(self,checkObj):
        nowMesh = mc.listRelatives(checkObj,s=1,ni=1,type= 'mesh',f=1)[0]
        needKey = 'Deformed'
        if needKey not in nowMesh:
            return
        oldMesh = nowMesh.split(needKey)[0]
        if not mc.ls(oldMesh):
            return
        #--------------------#
        # attr 处理
        # base
        baseAttrList = ['.castsShadows','.castsShadows','.motionBlur','.primaryVisibility','.smoothShading',
                    '.visibleInReflections','.visibleInRefractions','.doubleSided','.geometryAntialiasingOverride',
                    '.antialiasingLevel','.shadingSamplesOverride','.shadingSamples','.maxShadingSamples',
                    '.visibility','.lodVisibility']
        self.attrA2B(oldMesh,nowMesh,baseAttrList)
        #print '-------MayaBase Transfer Done!-------'
        # arnold
        arAttrList = ['.aiTranslator:string','.aiSelfShadows','.aiOpaque','.aiVisibleInDiffuse',
                      '.aiVisibleInGlossy','.aiMatte','.aiExportTangents','.aiExportColors','.aiExportRefPoints',
                      '.aiExportRefNormals','.aiExportRefTangents',
                      '.color:double3','.intensity','.aiExposure','.aiUseColorTemperature:bool','.aiColorTemperature',
                      '.emitDiffuse','.emitSpecular','.aiDecayType','.lightVisible','.aiSamples','.aiNormalize','.aiCastShadows',
                      '.aiShadowDensity','.aiShadowColor:double3','.aiAffectVolumetrics','.aiCastVolumetricShadows',
                      '.aiDiffuse','.aiSpecular','.aiSss','.aiIndirect','.aiVolume','.aiMaxBounces','.aiAov:string','.aiSssSetname:string'
                      '.aiTraceSets:string','.aiUserOptions:string','.data:string','.dso:string',
                      '.aiSubdivType','.aiSubdivIterations','.aiSubdivAdaptiveMetric','.aiSubdivPixelError','.aiSubdivAdaptiveSpace',
                      '.aiSubdivDicingCamera:cons','.aiSubdivUvSmoothing','.aiSubdivSmoothDerivs',
                      '.aiDispHeight','.aiDispPadding','.aiDispZeroValue','.aiDispAutobump','.aiStepSize']
        self.attrA2B(oldMesh,nowMesh,arAttrList)
        #print '-------Arnold Transfer Done!-------'
        # mr
        mrAttrList = ['.miTransparencyCast','.miTransparencyReceive','.miReflectionReceive','.miRefractionReceive','.miFinalGatherCast',
                      '.miFinalGatherReceive','.miProxyFile:string','.miUpdateProxyBoundingBoxMode','.miOverrideSamples',
                      '.miMinSamples','.miMaxSamples','.miShadingSamplesOverride','.miShadingSamples','.miFinalGatherRays',
                      '.miFinalGatherMinRadius','.miFinalGatherMaxRadius','.miFinalGatherView','.miFinalGatherFilter',
                      '.miOverrideGlobalIllumination','.miGlobillumAccuracy','.miGlobillumRadius','.miCausticAccuracy',
                      '.miMaxDisplaceOverride','.miCausticRadius','.miMaxDisplace']
        self.attrA2B(oldMesh,nowMesh,mrAttrList)
        #print '-------Mr Transfer Done!-------'
        # redShift
        rsAttrList=['.rsObjectId','.rsEnableSubdivision','.rsSubdivisionRule','.rsScreenSpaceAdaptive','.rsDoSmoothSubdivision',
                    '.rsMinTessellationLength','.rsMaxTessellationSubdivs','.rsOutOfFrustumTessellationFactor','.rsEnableDisplacement',
                    '.rsMaxDisplacement','.rsDisplacementScale','.rsAutoBumpMap"']
        self.attrA2B(oldMesh,nowMesh,rsAttrList)
        rsVAttrList=['.rsEnableVisibilityOverrides','.rsPrimaryRayVisible','.rsSecondaryRayVisible','.rsShadowCaster',
                     '.rsShadowCaster','.rsSelfShadow','.rsAOCaster','.rsReflectionVisible','.rsRefractionVisible',
                     '.rsReflectionCaster','.rsRefractionCaster','.rsFgVisible','.rsGiVisible','.rsCausticVisible',
                     '.rsFgCaster','.rsForceBruteForceGI','.rsGiCaster','.rsCausticCaster','.rsFgCaster','.rsForceBruteForceGI',
                     '.rsGiCaster','.rsCausticCaster','.rsFgCaster','.rsForceBruteForceGI','.rsGiCaster','.rsCausticCaster',
                     '.rsGiReceiver','.rsCausticReceiver']
        self.attrA2B(oldMesh,nowMesh,rsVAttrList)
        rsMAttrList=['.rsMatteEnable','.rsMatteShowBackground','.rsMatteApplyToSecondaryRays','.rsMatteAffectedByMatteLights',
                     '.rsMatteAlpha','.rsMatteReflectionScale','.rsMatteRefractionScale','.rsMatteDiffuseScale']
        self.attrA2B(oldMesh,nowMesh,rsMAttrList)
        rsSAttrList=['.rsMatteShadowEnable','.rsMatteShadowAffectsAlpha','.rsMatteShadowColor:double3','.rsMatteShadowTransparency']
        self.attrA2B(oldMesh,nowMesh,rsSAttrList)
        #print '-------Redshift Transfer Done!-------'
        #--------------------#
        # SG 处理
        needSGNodesCons = mc.listConnections(oldMesh,s=0,d=1,type = 'shadingEngine',plugs=1,connections = 1)
        needSgNodeList = mc.listConnections(oldMesh,s=0,d=1,type = 'shadingEngine')
        if not needSgNodeList:
            return
        needSgNodeList = list(set(needSgNodeList))
        tempSGNode = needSGNodesCons[1].split('.')[0]
        mc.sets(nowMesh,e=1,forceElement = tempSGNode)
        # 断开
        for sgNode in needSgNodeList:
            sgTAttr = sgNode + '.dagSetMembers'
            allList = mc.getAttr(sgTAttr,mi=1)
            newKey = nowMesh.split('|')[-1]
            for index in allList:
                targetAttr = '%s[%s]'%(sgTAttr,allList[index])
                sourceAttr = mc.listConnections(targetAttr,s=1,d=0,plugs = 1)
                if sourceAttr and newKey in sourceAttr[0]:
                    mc.disconnectAttr(sourceAttr[0],targetAttr)
        # 清单
        sgDict = {}
        for sgNode in needSgNodeList:
            meshes = mc.sets(sgNode,q=1)
            for checkMesh in meshes:
                if '|' in checkMesh:
                    checkKey = oldMesh
                    newKey = nowMesh
                else:
                    checkKey = oldMesh.split('|')[-1]
                    newKey = nowMesh.split('|')[-1]
                if checkKey not in checkMesh:
                    continue
                needMesh = checkMesh.replace(checkKey,newKey)
                if sgNode not in sgDict.keys():
                    sgDict[sgNode] = [needMesh]
                else:
                    sgDict[sgNode] += [needMesh]
                mc.sets(needMesh,e=1,forceElement = sgNode)

    #-----------------------#
    # attr 传递
    def attrA2B(self,oldMesh,nowMesh,attrList):
        errorList = []
        for checkAttr in attrList:
            checkKey = ''
            if ':' in checkAttr:
                checkKey = checkAttr.split(':')[-1]
                needAttr = checkAttr.split(':')[0]
            else:
                needAttr = checkAttr
            oldAttr = oldMesh+needAttr
            nowAttr = nowMesh+needAttr
            if not mc.ls(oldAttr):
                continue
            # 需要一步old的自建属性传给now
            needTransfer = 0
            if checkKey in ['double3','cons']:
                oldCons = mc.listConnections(oldAttr,s=1,d=0,plugs=1,c=1)
                nowCons = mc.listConnections(nowAttr,s=1,d=0,plugs=1,c=1)
                if (not oldCons) and nowCons:
                    mc.disconnectAttr(nowCons[1],nowCons[0])
                if oldCons and (not nowCons):
                    needTransfer = 1
                if oldCons and nowCons and oldCons[1] != nowCons[1]:
                    needTransfer = 1
                if checkKey in ['double3']:
                    oldValue = mc.getAttr(oldAttr)
                    nowValue = mc.getAttr(nowAttr)
                    if oldValue != nowValue:
                        needTransfer = 1
            else:
                oldValue = mc.getAttr(oldAttr)
                nowValue = mc.getAttr(nowAttr)
                if oldValue != nowValue:
                    needTransfer = 1
            if not needTransfer:
                continue
            # 传输
            try:
                if checkKey:
                    if checkKey in ['string']:
                        mc.setAttr(nowAttr,oldValue,type = 'string')
                    if checkKey in ['bool']:
                        if oldValue:
                            mc.setAttr(nowAttr,1)
                        else:
                            mc.setAttr(nowAttr,0)
                    if checkKey in ['double3']:
                        if oldCons:
                            mc.connectAttr(oldCons[1],nowMesh+'.%s'%oldCons[0].split('.')[-1])
                        else:
                            mc.setAttr(nowAttr,oldValue[0][0],oldValue[0][1],oldValue[0][2],type = 'double3')
                    if checkKey in ['cons']:
                        mc.connectAttr(oldCons[1],nowMesh+'.%s'%oldCons[0].split('.')[-1])
                else:
                    mc.setAttr(nowAttr,oldValue)
            except:
                errorList.append(needAttr)
        if errorList:
            print '--------Attr_A2B_Error:'
            for info in errorList:
                print '-----------'
                print oldMesh
                print nowMesh
                print info
            mc.error()

    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用】【清理工具系列】
    #  0.阶段通用
    #  Author  : 沈  康
    #  Data    : 2013_05_16
    # ------------------------------#

    # ------------------------------#
    # 清理asset文件persp里的动画
    def checkCleanPerspAnimation(self):
        attrs = ['translateX', 'translateY', 'translateZ', 'rotateX', 'rotateY', 'rotateZ', 'scaleX', 'scaleY', 'scaleZ', 'visibility']
        for attr in attrs:
            if mc.ls('persp' + '_' + attr):
                mc.delete('persp' + '_' + attr)
    # ----------------------------------------------------------------------------------------------#
    # ------------------------------#
    # 【通用】【清理工具系列】
    #  0.阶段通用
    #  Author  : hanhong
    #  Data    : 2017_2_7
    # ------------------------------#

    # ------------------------------#
    # 清理设置文件中双重MODEL组
    def checkCleanMOD(self):
        MODEL=mc.ls('MODEL',l=1)
        if len(MODEL)==2 :
            mod=''
            errmod=''
            nums=[]
            for i in range(2):
                num=len(MODEL[i].split('|'))
                nums.append(num)
            if nums[0]>nums[1]:
                mod=MODEL[1]
                errmod=MODEL[0]
            else:
                mod=MODEL[0]
                errmod=MODEL[1]
            all=mc.ls('MSH_all',l=1)
            if len(all)<1:
                mc.error(u'文件中缺少【MSH_all】组，请检查文件')
            elif len(all)>1:
                mc.error(u'文件中有多个【MSH_all】组，请检查文件')
            else:
                mc.parent(all[0],mod)
                grs=errmod.split('|')
                gr='|'+grs[1]+'|'+grs[2]+'|'+grs[3]
                try:
                    mc.delete(gr)
                    print u'==========已经清【双重MODEL组】'
                except:
                    mc.error(u'无法删除【%s】组，请检查文件'%gr)
        return 0
