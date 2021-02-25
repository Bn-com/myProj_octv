# -*- coding: utf-8 -*-

import sys
sys.path.append('Z:/Resource/Development/Maya/GDC/Plug/Python/GDC/COMMON/pre')


# Q:an标记是_an_还是_ca_
# A:_ct_an

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式
# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import maya.cmds as mc
import maya.mel as mel
import GDC_ProjectInfo
reload(GDC_ProjectInfo)

#
class sk_backCmd(object):

    def __init__(self):
        # namespace清理
        pass

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
        assetLocalPath = GDC_ProjectInfo.GDC_ProjectInfo().checkCacheLocalPath()
        assetNeedServerPath = GDC_ProjectInfo.GDC_ProjectInfo().checkCacheServerPath()
        print assetNeedServerPath
        # 写
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((assetLocalPath + 'assetReference.txt'), assetNeedOutputInfo)
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
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        localPath = GDC_ProjectInfo.GDC_ProjectInfo().checkLocalInfoPath()
        serverPath = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectServerPath()
        localTransPath = localPath + 'transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        mc.sysFile(localTransPath, makeDir=1)
        serverTransPath = serverPath + 'data/AssetInfos/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
        mel.eval(makeDirCMD)

        # 本地输出及更新
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localTransPath + 'transSGNodes.txt'), transpancySGNodes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transSGNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transSGNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localTransPath + 'transMeshes.txt'), transpancyMeshes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transMeshes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localTransPath + 'transNodes.txt'), transpancyNode)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    # 全流程用，禁用arnold
    def checkAssetforbidenNodes(self, arnoldCheck=1):
        if arnoldCheck:
            arnoldNodes = mc.ls(type='aiAOVDriver') + mc.ls(type='aiAOVFilter') + mc.ls(type='aiOptions')
            if arnoldNodes:
                print(u'=====Asset 存在 Arnold 节点，请Export清理=====')
                mc.error(u'=====Asset 存在 Arnold 节点，请Export清理=====')

    # ------------------------------#
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
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        check = 1
        if shotInfo[0] == 'zm':
            # 特殊内部任务ID
            strangeID = GDC_ProjectInfo.GDC_ProjectInfo().checkStrangeIDInfo()
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
    def checkAssetAnim2RenderCheckInConfig(self, cacheType=1, assetSpecial=0):
        import sk_sceneTools
        reload(sk_sceneTools)
        import os
        # 豁免判断
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        projectName = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectNameSimple2Full(shotInfo[0])
        projectPath = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectServerPath()
        scenesInfo = projectPath.split('/')[-2]

        # 文本豁免列表
        doNotCheckTxtPath = projectPath + 'data/rgtxIgnore.txt'
        # 有文件，且本文件在文件列表里，则判断return跳出
        if os.path.exists(doNotCheckTxtPath):
            fileInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkFileRead(doNotCheckTxtPath)
            if fileInfo:
                if shotInfo[1] in fileInfo:
                    print u'==========[一致性]本Asset处于豁免检测状态=========='
                    return 'ok'

        # 数据库豁免版本
        checkState = GDC_ProjectInfo.GDC_ProjectInfo().checkReadServerData()
        if checkState:
            print u'==========[一致性]本Asset处于豁免检测状态=========='
            return 'ok'

        # zm项目部分植物豁免检测
        if shotInfo[0] == 'zm' and shotInfo[1][:4] == 'p000':
            print u'==========[一致性]本Asset处于豁免检测状态=========='
            return 'ok'
        # 非豁免状态，全部强制检测
        # 记录文件名
        mc.file(save=1, force=1)
        fileName = mc.file(query=1, exn=1)
        # 记录非渲染的标记
        noNeedSign = ['_si_', '_nr_']
        # 开始检测
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        projectName = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectNameSimple2Full(shotInfo[0])
        mayaType = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormat(shotInfo[0])
        if len(shotInfo) >= 4:
            # 检测是否为有效asset
            assetInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectAssetNames()
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
            if assetName in assetInfo[2] or shotInfo[1][assetSpecial] == 'p':
                assetType = 'props'
            if assetName in assetInfo[3] or shotInfo[1][assetSpecial] in ['s', 'S']:
                assetType = 'sets'
            modelHML = ['l', 'm', 'h']
            print u'---------------'
            print shotInfo[3].split('.')[0]
            print shotInfo[2]
            if shotInfo[2] in modelHML and shotInfo[3].split('.')[0] in ['rg', 'tx']:
                animSetNum = [0, 0]
                cacheSetNum = [0, 0]
                difInfo = ''
                masterFolderPath = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectServerPath()
                masterFolderPath = masterFolderPath + 'scenes/' + assetType + '/' + assetName + '/master/'
                # 首先查询是否存在另一半文件,不存在则pass
                if shotInfo[3].split('.')[0] == 'tx':
                    assetOther = '_ms_anim'
                if shotInfo[3].split('.')[0] == 'rg':
                    assetOther = '_ms_render'
                fileOther = masterFolderPath + shotInfo[0] + '_' + assetName + '_' + shotInfo[2] + assetOther + mayaType
                print u'------'
                print fileOther
                if os.path.exists(fileOther):
                    # 先检测本文件
                    sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                    sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                    localAnimObjs = []
                    localCacheObjs = []
                    localModelObjs = []
                    localFaceNum = []
                    localVertexNum = []
                    localUVsNum = []
                    anotherAnimObjs = []
                    anotherCacheObjs = []
                    anotherModelObjs = []
                    anotherFaceNum = []
                    anotherVertexNum = []
                    anotherUVsNum = []
                    # cache模式
                    if cacheType:
                        if mc.sets('CTRLS', q=1):
                            localAnimObjs = mc.sets('CTRLS', q=1)
                            if localAnimObjs:
                                localAnimObjs = mc.ls(localAnimObjs, l=1)
                            animSetNum[0] = len(mc.sets('CTRLS', q=1))
                        if mc.sets('MESHES', q=1):
                            localCacheObjs = mc.sets('MESHES', q=1)
                            if localCacheObjs:
                                localCacheObjs = mc.ls(localCacheObjs, l=1)
                            cacheSetNum[0] = len(mc.sets('MESHES', q=1))
                    # anim模式
                    else:
                        controlCurves = mc.ls(type='nurbsCurve', l=1)
                        if controlCurves:
                            localAnimObjs = mc.listRelatives(controlCurves, p=1, type='transform', f=1)
                            if localAnimObjs:
                                localAnimObjs = mc.ls(localAnimObjs, l=1)
                                localAnimObjs = list(set(localAnimObjs))
                                animSetNum[0] = len(localAnimObjs)
                    # 无论做不做Cache，都要检测MODEL组下的物体
                    localModelMeshes = mc.listRelatives('MODEL', ad=1, type='mesh', f=1)
                    if localModelMeshes:
                        for mesh in localModelMeshes:
                            obj = mc.listRelatives(mesh, p=1, type='transform', f=1)
                            if not obj:
                                continue
                            obj = obj[0]
                            if noNeedSign:
                                checkSign = 0
                                for sign in noNeedSign:
                                    if sign not in obj:
                                        checkSign = checkSign + 1
                                if checkSign == len(noNeedSign):
                                    localModelObjs.append(obj)
                    if localModelObjs:
                        localModelObjs = list(set(localModelObjs))
                    # 记录faceNum，vertex，uvs
                    if localCacheObjs:
                        for checkObj in localCacheObjs:
                            localFaceNum.append(mc.polyEvaluate(checkObj, face=1))
                            localVertexNum.append(mc.polyEvaluate(checkObj, vertex=1))
                            localUVsNum.append(mc.polyEvaluate(checkObj, uvcoord=1))
                    # 打开另一半文件并检测
                    mc.file(fileOther, open=1, f=1)
                    sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
                    sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
                    # cache模式
                    if cacheType:
                        if mc.sets('CTRLS', q=1):
                            anotherAnimObjs = mc.sets('CTRLS', q=1)
                            if anotherAnimObjs:
                                anotherAnimObjs = mc.ls(anotherAnimObjs, l=1)
                            animSetNum[1] = len(mc.sets('CTRLS', q=1))
                        if mc.sets('MESHES', q=1):
                            anotherCacheObjs = mc.sets('MESHES', q=1)
                            if anotherCacheObjs:
                                anotherCacheObjs = mc.ls(anotherCacheObjs, l=1)
                            cacheSetNum[1] = len(mc.sets('MESHES', q=1))
                    # anim模式
                    else:
                        controlCurves = mc.ls(type='nurbsCurve', l=1)
                        if controlCurves:
                            anotherAnimObjs = mc.listRelatives(controlCurves, p=1, type='transform', f=1)
                            if anotherAnimObjs:
                                anotherAnimObjs = mc.ls(anotherAnimObjs, l=1)
                                anotherAnimObjs = list(set(anotherAnimObjs))
                                animSetNum[1] = len(anotherAnimObjs)
                    # 无论做不做Cache，都要检测MODEL组下的物体
                    anotherModelMeshes = mc.listRelatives('MODEL', ad=1, type='mesh', f=1)
                    if anotherModelMeshes:
                        for mesh in anotherModelMeshes:
                            obj = mc.listRelatives(mesh, p=1, type='transform', f=1)
                            if not obj:
                                continue
                            obj = obj[0]
                            if noNeedSign:
                                checkSign = 0
                                for sign in noNeedSign:
                                    if sign not in obj:
                                        checkSign = checkSign + 1
                                if checkSign == len(noNeedSign):
                                    anotherModelObjs.append(obj)
                    if anotherModelObjs:
                        anotherModelObjs = list(set(anotherModelObjs))
                    # 记录faceNum，vertex，uvs
                    if anotherCacheObjs:
                        for checkObj in anotherCacheObjs:
                            anotherFaceNum.append(mc.polyEvaluate(checkObj, face=1))
                            anotherVertexNum.append(mc.polyEvaluate(checkObj, vertex=1))
                            anotherUVsNum.append(mc.polyEvaluate(checkObj, uvcoord=1))
                    # 返回文件
                    mc.file(fileName, open=1, f=1)
                    # 检测阶段
                    # 第一阶段|数量对比处理
                    checkObjNum = 0
                    if animSetNum[0] != animSetNum[1]:
                        difInfo = difInfo + (u'AnimSetNum_Dif') + '\n'
                        checkObjNum = 1
                    if cacheSetNum[0] != cacheSetNum[1]:
                        difInfo = difInfo + (u'CacheSetNum_Dif') + '\n'
                        checkObjNum = 1
                    if len(localModelObjs) != len(anotherModelObjs):
                        difInfo = difInfo + (u'MoldeMeshNum_Dif') + '\n'
                        checkObjNum = 1
                    print animSetNum
                    print '++++++++++++++++++++++++++++++++'
                    print cacheSetNum
                    print '++++++++++++++++++++++++++++++++'
                    print[len(localModelObjs), len(anotherModelObjs)]
                    print '++++++++++++++++++++++++++++++++'
                    if checkObjNum:
                        print '---------------------------------------'
                        print difInfo
                        print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                        print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                        mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                    else:
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
                        # 第二阶段|anim处理异常名字
                        difLocalAnimNameInfo = []
                        difAnotherAnimNameInfo = []
                        if localAnimObjs:
                            for animObj in localAnimObjs:
                                if animObj not in anotherAnimObjs:
                                    difLocalAnimNameInfo.append(animObj)
                            for animObj in anotherAnimObjs:
                                if animObj not in localAnimObjs:
                                    difAnotherAnimNameInfo.append(animObj)
                        if difLocalCacheNameInfo or difLocalAnimNameInfo:
                            if difLocalCacheNameInfo:
                                print u'------------------[cache][本文件][异常不同名字][如下]------------------'
                                for info in difLocalCacheNameInfo:
                                    print info
                                print u'------------------[cache][另文件][异常不同名字][如下]------------------'
                                for info in difAnotherCacheNameInfo:
                                    print info
                            if difLocalAnimNameInfo:
                                print u'------------------[anim][本文件][异常不同名字][如下]------------------'
                                for info in difLocalAnimNameInfo:
                                    print info
                                print u'------------------[anim][另文件][异常不同名字][如下]------------------'
                                for info in difAnotherAnimNameInfo:
                                    print info
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
                            print u'------------------[Model][本文件][异常不同名字][如下]------------------'
                            for info in difLocalModelNameInfo:
                                print info
                            print u'------------------[Model][另文件][异常不同名字][如下]------------------'
                            for info in difAnotherModelNameInfo:
                                print info
                            checkNameDif = 1
                        if checkNameDif:
                            print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                            print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                            mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                        # 第三阶段|cache物体和anim物体 faceNum，vertexNum，UV对比
                        difObjInfo = []
                        if cacheType:
                            if not difLocalCacheNameInfo and localCacheObjs:
                                for j in range(len(localCacheObjs)):
                                    checkFNum = 0
                                    checkVNum = 0
                                    checkUNum = 0
                                    localID = j
                                    anotherID = anotherCacheObjs.index(localCacheObjs[j])
                                    if localFaceNum[localID] != anotherFaceNum[anotherID]:
                                        checkFNum = 1
                                    if localVertexNum[localID] != anotherVertexNum[anotherID]:
                                        checkVNum = 1
                                    if localUVsNum[localID] != anotherUVsNum[anotherID]:
                                        checkUNum = 1
                                    if checkFNum or checkVNum:
                                        difObjInfo.append('---------------')
                                        difObjInfo.append(localCacheObjs[localID])
                        if difObjInfo:
                            print u'------------------[cache][异常Face|Vertext|UV模型][如下]------------------'
                            for info in difObjInfo:
                                print info
                            print u'------------------[cache][异常Face|Vertext|UV模型][如上]------------------'
                            print u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======'
                            print u'=========请视情况使用豁免处理，但严禁非法豁免操作========='
                            mc.error(u'\n======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                        print u'=====================AnimRender版本检测完毕====================='
                else:
                    pass
            else:
                mc.error(u'==============================找不到对应Asset,请检查文件名==============================')
        else:
            mc.error(u'==============================找不到对应Asset,请检查文件名==============================')

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
        info = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        projectInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 处理文件内ca模型渲染开启属性
        self.checkCacheObjRenderState()

        self.checkRenderObjRenderState(1, 0, 0)
        # 另存到temp文件夹
        pathLocal = GDC_ProjectInfo.GDC_ProjectInfo().checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        mc.file(rename=fileLocal)
        mc.file(save=1, force=1)
        # 仅允许tx阶段使用
        # 先输出smoothSet信息
        self.checkAssetSmoothSetUpdate()
        # info = self.checkShotInfo()
        fileTypeFull = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormatFull(info[0])
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
                                print(unicode('=====================[Check in] Start=====================', "utf8"))
                                # checkOut
                                newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                                #print checkOutCmd
                                mel.eval(checkOutCmd)
                                # checkIn
                                mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                            #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
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
                                print(unicode('=====================[Check in] Start=====================', "utf8"))
                                # checkOut
                                newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                                # print checkOutCmd
                                mel.eval(checkOutCmd)
                                # checkIn
                                mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                            #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
                            print(u'=====================创建【RenderFile】完毕=====================')
                # 有an的文件，以及什么都无的文件
                if setType[1] == 1 or setType == [0, 0]:
                    '''
                    # 另存anim
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                    self.checkTexNoAC2AnimMo('anim',assetSpecial)
                    if checkIn == 1:
                        print(unicode('=====================[Check in] Start=====================', "utf8"))
                        # checkOut
                        newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        mel.eval(checkOutCmd)
                        # checkIn
                        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                    #print(unicode('=========【非cache文件，直接输出anim文件。复制到render文件】=========', "utf8"))
                    print(u'=========【非cache文件，直接输出anim文件。复制到render文件】=========')
                    #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
                    print(u'=====================创建【AnimFile】完毕=====================')
                    '''
                    # 另存render
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                    self.checkTexNoAC2AnimMo('render', assetSpecial)
                    if checkIn == 1:
                        print(unicode('=====================[Check in] Start=====================', "utf8"))
                        # checkOut
                        newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        # print checkOutCmd
                        mel.eval(checkOutCmd)
                        # checkIn
                        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                    #print(unicode('=========【非cache文件，清理ca的history。复制到render文件】=========', "utf8"))
                    print(u'=========【非cache文件，清理ca的history。复制到render文件】=========')
                    #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
                    print(u'=====================创建【RenderFile】完毕=====================')
            # 对set组不做cache处理
            # 对set组，判断参考在时进行参考替换
            else:
                # 另存anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                if checkIn == 1:
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=========【非cache文件，直接输出anim文件。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=========【非cache文件，清理ca的history。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
                print(u'=====================创建【RenderFile】完毕=====================')
            # 返回tx文件
            if backTx == 1:
                print fileName
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
            #print(unicode('=====================【返回 tx 文件】=====================', "utf8"))
            print(u'=====================【返回 tx 文件】=====================')
        else:
            # 要报错处理,check in 用
            #print(unicode('=====================【！！！您所用的不是【tx】阶段文件！！！】=====================', "utf8"))
            print(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')
            #print(unicode('=====================【！！！【tx】【MODEL】处于第二层！！！】=====================', "utf8"))
            print(u'=====================【！！！【tx】【MODEL】处于第二层！！！】=====================')
            #mc.error(unicode('=====================【！！！您所用的不是【tx】阶段文件！！！】=====================', "utf8"))
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
        info = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        projectInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 处理文件内ca模型渲染开启属性
        self.checkCacheObjRenderState()
        self.checkRenderObjRenderState(1, 0, 0)
        # 另存到temp文件夹
        pathLocal = GDC_ProjectInfo.GDC_ProjectInfo().checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        mc.file(rename=fileLocal)
        mc.file(save=1, force=1)
        # 仅允许tx阶段使用
        # 先输出smoothSet信息
        self.checkAssetSmoothSetUpdate()
        # info = self.checkShotInfo()
        fileTypeFull = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormatFull(info[0])
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
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=========【非cache文件，清理ca的history。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
                print(u'=====================创建【RenderFile】完毕=====================')

                # 处理anim
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('anim', assetSpecial)
                # 处理贴图文件
                fileNodes = mc.ls(type='file')
                for node in fileNodes:
                    mc.setAttr((node + '.fileTextureName'), '', type='string')
                if checkIn == 1:
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
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
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By RG File\"')
                #print(unicode('=========【非cache文件，直接输出anim文件。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By RG File\"')
                #print(unicode('=========【非cache文件，清理ca的history。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
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
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=========【非cache文件，直接输出anim文件。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
                print(u'=====================创建【AnimFile】完毕=====================')

                # 另存render
                mc.file(fileName, force=1, options="v=0", type=fileTypeFull, open=1)
                self.checkTexNoAC2AnimMo('render', assetSpecial)
                if checkIn == 1:
                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                    # 全部显示层显示
                    layerInfos = mc.ls(type='displayLayer')
                    for layer in layerInfos:
                        a = layer.lower()
                        if 'defaultlayer' not in a and u'norender' not in a:
                            mc.setAttr((layer + '.visibility'), 1)
                    # checkOut
                    newInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                    # print checkOutCmd
                    mel.eval(checkOutCmd)
                    # checkIn
                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                #print(unicode('=========【非cache文件，清理ca的history。复制到render文件】=========', "utf8"))
                print(u'=========【Set_Asset，清理ca的history。复制到render文件】=========')
                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
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
        path = GDC_ProjectInfo.GDC_ProjectInfo().checkPCFilePath()
        info = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        fileFormat = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormat(info[0])
        if fileType == 'anim':
            fileName = path + info[0] + '_' + info[1] + '_' + info[2] + '_ms_anim' + fileFormat
        if fileType == 'render':
            fileName = path + info[0] + '_' + info[1] + '_' + info[2] + '_ms_render' + fileFormat
        # 文件清理开始
        mc.file(rename=fileName)
        fileTypeFull = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormatFull(info[0])
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
        path = GDC_ProjectInfo.GDC_ProjectInfo().checkPCFilePath()
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        fileFomat = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormat(shotInfo[0])
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
                info = mc.listConnections((obj + '.message'), d=1)
                if not info:
                    mc.select(obj, add=1, ne=1)
        # 导出
        fileTypeFull = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormatFull(shotInfo[0])
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
        path = GDC_ProjectInfo.GDC_ProjectInfo().checkPCFilePath()
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        fileFomat = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_render' + fileFomat
        # 选取物体
        mc.select(rootGrp)
        # set组加选
        quickSets = mc.ls(type='objectSet')
        if quickSets:
            for obj in quickSets:
                info = mc.listConnections((obj + '.message'), d=1)
                if not info:
                    mc.select(obj, add=1, ne=1)
        # 处理导出
        fileTypeFull = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectFileFormatFull(shotInfo[0])
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
            serverPath = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectServerPath()
            serverSmoothSetInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
            objsSmoothSet_lv0 = GDC_ProjectInfo.GDC_ProjectInfo().checkFileRead(serverSmoothSetInfoPath + 'smooth_0.txt')
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
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(1, 0)
            objsSmoothSet_lv1 = GDC_ProjectInfo.GDC_ProjectInfo().checkFileRead(serverSmoothSetInfoPath + 'smooth_1.txt')
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
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(1, 1)
            objsSmoothSet_lv2 = GDC_ProjectInfo.GDC_ProjectInfo().checkFileRead(serverSmoothSetInfoPath + 'smooth_2.txt')
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
                    sk_smoothSet.sk_smoothSet().smoothSetAdd(1, 2)
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
            objs = []
            objs.append(rootGrp)
            sk_sceneTools.sk_sceneTools().checkLockObjs(objs, 1)
            sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
            sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()

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
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()

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
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
        localPath = GDC_ProjectInfo.GDC_ProjectInfo().checkLocalInfoPath()
        serverPath = GDC_ProjectInfo.GDC_ProjectInfo().checkProjectServerPath()
        localInfoPath = localPath + 'smoothSetInfoTemp/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
        mc.sysFile(localInfoPath, makeDir=1)
        serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 记录信息
        smoothObjs_lv0 = mc.sets('smooth_0', q=1)
        if smoothObjs_lv0 == None:
            smoothObjs_lv0 = []
        smoothObjs_lv1 = mc.sets('smooth_1', q=1)
        if smoothObjs_lv1 == None:
            smoothObjs_lv1 = []
        smoothObjs_lv2 = mc.sets('smooth_2', q=1)
        if smoothObjs_lv2 == None:
            smoothObjs_lv2 = []
        # 输出信息
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localInfoPath + 'smooth_0.txt'), smoothObjs_lv0)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_0.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_0.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localInfoPath + 'smooth_1.txt'), smoothObjs_lv1)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_1.txt') + '"' + ' ' + '"' + (serverInfoPath + 'smooth_1.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        GDC_ProjectInfo.GDC_ProjectInfo().checkFileWrite((localInfoPath + 'smooth_2.txt'), smoothObjs_lv2)
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
        shotInfo = GDC_ProjectInfo.GDC_ProjectInfo().checkShotInfo()
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
            #mc.setAttr((shape + '.motionBlur'),1)
            #mc.setAttr((shape + '.smoothShading'),1)
            #mc.setAttr((shape + '.visibleInReflections'),1)
            #mc.setAttr((shape + '.visibleInRefractions'),1)
            #mc.setAttr((shape + '.doubleSided'),1)

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
