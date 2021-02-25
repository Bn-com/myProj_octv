# -*- coding: utf-8 -*-
# 【通用】【mi项目工具】
#  Author : 沈康
#  Data   : 2016

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json


from functools import partial

import tiBase as tiBase
reload(tiBase)

import tiFile as tiFile
reload(tiFile)


errorSet = 'ErrorTemp_Set'

#--------------------------------------------------------#
# 前期检测 UI
#--------------------------------------------------------#
# 前期check工具集
def sk_sceneUICheckTools():
    # 窗口
    if mc.window ("sk_sceneUICheckTools", ex=1):
        mc.deleteUI("sk_sceneUICheckTools", window=True)
    mc.window("sk_sceneUICheckTools", title="Check Tools", widthHeight=(360, 420), menuBar=0)
    # 主界面
    mc.columnLayout()

    # 选取栏
    # mc.rowLayout(numberOfColumns=2, columnWidth2=(230, 100))
    # mc.textField('sk_sceneUICheckName', w=230 , h=30 , en=1 , text=(unicode('输入整行然后按【提取选择】按钮', 'utf8')))
    # mc.button(w=100 , h=30 , bgc=[0, 0.5, 0.8], label=(unicode('【提取选择】', 'utf8')) , c='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().sk_sceneDetailsSelectObject()')
    # mc.setParent("..")

    # 行按钮
    mc.rowLayout(numberOfColumns=2, columnWidth2=(80, 250))
    # 全自动
    mc.button(w=80 , h=350 , bgc=[0.1, 0.1, 0.1], label=(unicode('【全自动】\n【Check】', 'utf8')), c=partial(checkDetailsWarning, ''))
    mc.columnLayout()
    # 分割按钮
    # 第1排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【参考】          ', 'utf8')), c=partial(checkDetailsWarning, 'refCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('命名:MASTER', 'utf8')), c='import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.renameSelectObj("MASTER")')
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动更新标记Set>>', 'utf8')),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().checkCacheSetAdd()')
    mc.setParent("..")
    # 第2排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【namespace】', 'utf8')),c=partial(checkDetailsWarning, 'nsCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('命名:CHARACTER', 'utf8')), c='import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.renameSelectObj("CHARACTER")')
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<namespace工具>>', 'utf8')),c = 'mel.eval(\"common_namespaceTools\")')
    mc.setParent("..")
    # 第3排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【命名】          ', 'utf8')),c=partial(checkDetailsWarning, 'MSHCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('命名:MOVE_CTRL', 'utf8')), c='import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.renameSelectObj("MOVE_CTRL")')
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<添加_后缀>>', 'utf8')),c ='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkRenameMSHPosfix()')
    mc.setParent("..")
    # 第4排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【面数】          ', 'utf8')),c=partial(checkDetailsWarning, 'faceCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('命名:PRO_CTRL', 'utf8')), c='import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.renameSelectObj("PRO_CTRL")')
    # tempCmd = 'from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkSameRename();sk_checkTools.sk_checkTools().checkSameRename("mesh");'
    # tempCmd += 'sk_checkTools.sk_checkTools().checkSameRename("nurbsCurve");sk_checkTools.sk_checkTools().checkMSHKeepOneRename("MSH")'
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动处理重命名>>', 'utf8')),c = tempCmd)
    mc.setParent("..")
    # 第5排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【instance】    ', 'utf8')),c=partial(checkDetailsWarning, 'insCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('1.文件对比', 'utf8')), c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.compareFile()')
    mc.setParent("..")
    # 第6排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【smooth】     ', 'utf8')),c=partial(checkDetailsWarning, 'smoothCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('2.对比点信息', 'utf8')),c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.compareVtxInfo()')

    mc.setParent("..")
    # 第7排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【标记】         ', 'utf8')),c=partial(checkDetailsWarning, 'signCheck'))
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动清理空组>>', 'utf8')),c = 'import maya.mel as mel;mel.eval(\"deleteEmptyGroups()\")')
    mc.setParent("..")
    # 第8排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【物体重名】  ', 'utf8')),c=partial(checkDetailsWarning, 'sameTransformCheck'))
    # mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<显示|隐藏骨骼>>', 'utf8')),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkJointViewHide()')
    mc.setParent("..")

    # 第9排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【shape重名】', 'utf8')),c=partial(checkDetailsWarning, 'sameShapeCheck'))
    # mc.button(w=125 , h=30 , bgc=[0.1, 0.1, 0.1], label=(unicode('<<添加|ABC属性>>', 'utf8')), c ='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="alembic")')
    mc.setParent("..")

    # 第10排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【Mesh同名】', 'utf8')),c=partial(checkDetailsWarning, 'sameShapeNodeCheck'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【proxy位移】', 'utf8')),c=partial(checkDetailsWarning, 'proxyInfo'))
    mc.setParent("..")

    # 第11排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【smoothSet】', 'utf8')),c= partial(checkDetailsWarning, 'smoothSet'))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【renderState】', 'utf8')),c= partial(checkDetailsWarning, 'renderState'))
    mc.setParent("..")

    # 第12排
    mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【SETIDP】', 'utf8')),c= partial(checkDetailsWarning, 'arnoldSHDAndIDP'))  
    mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【VTX】', 'utf8')), c = 'import idmt.maya.titanium.tiPre as tiPre;reload(tiPre);tiPre.compareVtxInfo()')
    mc.setParent("..")


    mc.setParent("..")

    mc.setParent("..")
    mc.showWindow("sk_sceneUICheckTools")

# 提取选择物体
def sk_sceneDetailsSelectObject():
    pathInfo = mc.textField('sk_sceneUICheckName', q=1, text=1)
    objPath = pathInfo.split('\t')[-1]
    mc.select(objPath)

#--------------------------------------------------------#
# 前期检测工具
#--------------------------------------------------------#
def checkDetailsWarning( checkType = '',UIShow = 0,printMode = 1,errorMode = 0):
    infoWrong = []
    errorPrintNum = 0

    import time
    startTime = time.strftime("%Y-%m-%d %H:%M:%S")

    tf = tiFile.tiAssetFile()
    # 文件名检测，判断环节
    shotInfo = checkShotInfo()
    
    # 代理模式检测
    highMode = tf.mode
    proxyMode = 0
    if highMode in ['p']:
        proxyMode = 1
    needSets = [u'defaultLightSet', u'defaultObjectSet', u'initialParticleSE', u'initialShadingGroup']
    if proxyMode:
        setGrps = mc.ls(type = 'objectSet')
        for setGrp in setGrps:
            if setGrp in needSets:
                continue
            if mc.ls(setGrp):
                mc.delete(setGrp)
        return

    # 创建ErrorSet
    checkErrorSetCreate()

    setState = 0 # set ?
    if tf.assetType == 'set' : #shotInfo[1][0] in sk_infoConfig.sk_infoConfig().setKeys:
        setState = 1

    stepSimp = tf.type
    # stepSimp = shotInfo[3]
    # if '.' in stepSimp:
    #     stepSimp = stepSimp.split('.')[0]

    
    # 点线面豁免
    #errorEdgeIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'errorEdgeIgnore')
    #errorFaceIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'errorFaceShaderIgnore')
    #error4EdgesIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'error4EdgesIgnore')

    errorEdgeIgnoreState = 0
    errorFaceIgnoreState = 0
    error4EdgesIgnoreState = 0
    txSizeState = 0

    try:
        # 点线面server豁免
        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])

        dataCmd = "SELECT isnull(A.vefcheck,'0') as vefcheckNew FROM idmtPlex_%s.dbo.[TB_Asset] A WHERE A.asset_name ='%s'"%(projFullName,shotInfo[1])
        

        vefCheckIgnoreState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)
        
        errorEdgeIgnoreState = vefCheckIgnoreState
        errorFaceIgnoreState = vefCheckIgnoreState
        error4EdgesIgnoreState = vefCheckIgnoreState
        dataCmd = u"SELECT case when isnull(edite1,\'否\')=\'否\' then \'0\' else \'1\' end as txSize from idmtPlex_%s.dbo.View_SsomAssetModel VSAM where VSAM.asset_name=\'%s\'"%(projFullName,shotInfo[1])
        txSizeState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)

    except:
        pass

    timeInfos = []
    import time
    if len(shotInfo) > 3:
        # 错误检测，根据阶段不同而不同
        # 检测是否有非法MODEL组
        for i in range(0, 9):
            grps = mc.ls('MODEL' + str(i) + '*')
            if not grps:
                continue
            infoWrong.append(u'【错误存在】\t\t%s' % (grps))
            errorPrintNum += 1

        # 检测文件名
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        lenNum = len(fileName.split('.'))

        if lenNum != 2:
            infoWrong.append(u'【错误存在】\t\t%s' % ('文件名错误!请仔细看命名规范!'))
            errorPrintNum += 1

        # 检测MODEL组重系列
        model = mc.ls('MODEL',l=1)
        if not model:
            infoWrong.append(u'【 错 误 】\t\tMODEL组不存在!!')
            errorPrintNum += 1
        else:
            # MODEL组唯一
            if len(model) > 1 and not setState:
                infoWrong.append(u'【 错 误 】\t\tMODEL组不止一个!')
                errorPrintNum += 1
            else:
                # MODEL组必须第二层级
                if len(model[0].split('|')) !=3:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不在第二层级!')
                    errorPrintNum += 1
        # 检测大组数目
        rootGrps = outlineGrps() #sk_sceneTools.sk_sceneTools().checkOutlinerGroup()
        
        if rootGrps:
            # 根目录大组数目。特殊项目特殊情况
            if len(rootGrps) == 1:
                if rootGrps[0] not in ['CHR','PRO','SET']:
                    infoWrong.append(u'【 错 误 】\t\tAsset大组名字错误！角色应为CHR，道具应为PRO，场景应为SET')
                    errorPrintNum += 1
            else:
                infoWrong.append(u'【 错 误 】\t\t大组不止一个!%s\t'%(rootGrps))
                errorPrintNum += 1
        else:
            infoWrong.append(u'【 错 误 】\t\t文件是空的!!')
            errorPrintNum += 1

        # rootGrpCheck = sk_checkTools.sk_checkTools().checkRootGrpName()
        
        # print rootGrpCheck
        # print outlineGrps()
        # return


        # if rootGrpCheck:
        #     infoWrong.append(u'【 错 误 】\t\tAsset大组名字错误！角色应为CHR，道具应为PRO，场景应为SET')
        #     errorPrintNum += 1
        print(u'\n')

        if printMode:print('-----c_001')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        #-----------------------------#
        # 忽略l模型的检测
        if highMode in ['l'] and stepSimp not in ['tx']:
            if errorPrintNum == 0:
                mc.delete(errorSet)
            # 输出错误消息
            print(UIShow)
            print(u'=============================【文件中错误如下】=============================')
            for info in infoWrong:
                print(info)
            print(u'===========================【目前】共计【%s】处错误===========================' %errorPrintNum)
            mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrintNum)

            # 解锁
            checkUnlockMSHV()
            checkUnlockMSHGeo(0)
            return errorPrintNum

        if printMode:print('-----c_002')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        
        #-----------------------------#
        # 检测空Mesh错误
        if checkType == '' or checkType == 'meshError':
            
            
            errorNames = checkMeshError() #sk_checkTools.sk_checkTools().checkMeshError()
            if errorNames:
                for name in errorNames:
                    infoWrong.append(u'【空白Mesh】\t\t%s' % (str(name)))
                    errorPrintNum += 1
        print(u'\n')

        if printMode:print('-----c_003')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))


        #-----------------------------#
        # 预先检测
        #-----------------------------#
        # 参考检测，对于rg和set允许有参考 | 不同项目不同处理
        if checkType == '' or checkType == 'refCheck':
            # 对set类不检测
            if not setState and stepSimp not in ['rg']:
                # 获取参考数
                rfnNods = mc.file(q=1, reference=1)
                # 有参考时
                if rfnNods:
                    infoWrong.append(u'【 警告 】\t\t有参考存在，请注意核查!!')
        print(u'\n')

        if printMode:print('-----c_004')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测namespace，对于rg和set允许有参考  | 不同项目不同处理
        if checkType == '' or checkType == 'nsCheck':
            # 对set类和rg特殊处理
            if not setState and stepSimp not in ['rg']:
                errorNs = checkNamespace(setState) #sk_checkTools.sk_checkTools().checkNamespace(setState)
                if errorNs:
                    for ns in errorNs:
                        infoWrong.append(u'【 错 误 】\t\t%s'%ns)
                        errorPrintNum += 1
        print(u'\n')

        if printMode:print('-----c_005')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 非polygon检测，只允许polygon建模
        if checkType == '' or checkType == 'polyCheck':
            errorSet = 'Error_polyError'
            if not setState:
                errorNames = checkNotPoly() #sk_checkTools.sk_checkTools().checkNotPoly()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【非poly】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_006')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        #-----------------------------#
        # model环节检测
        #-----------------------------#
        #　检测intermediate object
        if checkType == '' or checkType == 'imoCheck':
            errorSet = 'Error_imoError'
            if not setState and stepSimp in ['mo','tx']:
                errorNames = checkIntermediateObjectError() #sk_checkTools.sk_checkTools().checkIntermediateObjectError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【临时shape】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_006a')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 非法模型检测
        if checkType == '' or checkType == 'nonManifoldVertices':
            errorSet = 'Error_nonManifoldVertices'
            if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                errorNames = checkErrorObjects('nonManifoldVertices') #sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldVertices')
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【未缝合点】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_006b')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        if checkType == '' or checkType == 'nonManifoldEdges':
            errorSet = 'Error_nonManifoldEdges'
            if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                errorNames = checkErrorObjects('nonManifoldEdges') # sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldEdges')
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【未缝合边】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_006c')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        if checkType == '' or checkType == 'laminaFaces':
            errorSet = 'Error_laminaFaces'
            if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                errorNames = checkErrorObjects('laminaFaces') # sk_checkTools.sk_checkTools().checkErrorObjects('laminaFaces')
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【未缝合面】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_007')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        #-----------------------------#
        # texture环节检测
        #-----------------------------#
        # 选面物体检测
        if checkType == '' or checkType == 'faceShader':
            errorSet = 'Error_faceShader'
            if not errorFaceIgnoreState:
                if not setState and stepSimp in ['tx']:
                    errorNames = checkFaceShaderDetails() #sk_checkTools.sk_checkTools().checkFaceShaderDetails()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【选面物体】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_007a')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 尺寸超标
        if checkType == '' or checkType == 'Error_txFileSize':
            errorSet = 'Error_txFileSize'
            if not txSizeState and stepSimp in ['tx']:
                errorNames = checkTextureFileSize(returnMode = 1,sizeMax=4) # sk_checkTools.sk_checkTools().checkTextureFileSize(returnMode = 1,sizeMax=4)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【尺寸超标】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_007b')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 透明贴图检测
        if checkType == '' or checkType == 'transprancyNodes':
            errorSet = 'Error_transprancyNodes'
            if stepSimp in ['tx']:
                # from idmt.maya.py_common import GDC_TransInfoProce
                # reload(GDC_TransInfoProce)
                errorNames = gdc_TrShadeInfo(returnMode = 1) #GDC_TransInfoProce.GDC_TransInfoProce().gdc_TrShadeInfo(returnMode = 1)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【透明贴图】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_007c')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        #-----------------------------#
        # rigging环节检测
        #-----------------------------#
        # 检测MODEL层级
        if checkType == '' or checkType == 'modelRg':
            # 对rg检测
            errorSet = 'Error_modelRG'
            if stepSimp in ['rg']:
                errorNames = checkRGModel() # sk_checkTools.sk_checkTools().checkRGModel()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【MODEL层级】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_009')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        if printMode:print('-----c_009a')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测约束到物体级别
        if checkType == '' or checkType == 'constraint2Grps':
            # 对rg检测
            errorSet = 'Error_Constraint2Grps'
            if stepSimp in ['rg'] and not setState:
                errorNames = checkconstraintObjs() #sk_checkTools.sk_checkTools().checkconstraintObjs()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【约束到物】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)

        if printMode:print('-----c_009b')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        #-----------------------------#
        # 通用环节检测
        #-----------------------------#
        # 渲染属性检测
        if checkType == '' or checkType == 'renderState':
            errorSet = 'Error_RenderState'
            errorNames = checkMeshRenderStates() #sk_checkTools.sk_checkTools().checkMeshRenderStates()
            if errorNames:
                if errorNames == ['No Model']:
                    infoWrong.append(u'【MODEL】\t\t%s' % (str(errorNames)))
                    errorPrintNum += 1
                else:
                    for name in errorNames:
                        infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_010')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 多边面错误
        if checkType == '' or checkType == 'faceCheck':
            error4Set = 'Error_N4Edges'
            error3Set = 'Error_N3Edges'
            if not error4EdgesIgnoreState:
                errorNames = [[],[]]
                if not setState:
                    errorNames = checkFaceVertexs(smoothSkip = 0,triangleNum = 1) # sk_checkTools.sk_checkTools().checkFaceVertexs(smoothSkip = 0,triangleNum = 1)
                check4Name = errorNames[0]
                print(errorNames)
                if check4Name:
                    for name in check4Name:
                        if '.f[' in name:
                            infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                        else:
                            infoWrong.append(u'【蒙皮错误】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(check4Name , e=1 , addElement=error4Set)
                else:
                    mc.delete(error4Set)
                check3Name = errorNames[1]
                if check3Name:
                    for name in check3Name:
                        infoWrong.append(u'【三角面过多】\t\t%s' % (str(name)))
                    mc.sets(check3Name , e=1 , addElement=error3Set)
                else:
                    mc.delete(error3Set)
            else:
                mc.delete(error3Set)
                mc.delete(error4Set)
        print(u'\n')

        if printMode:print('-----c_011')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # instance检测
        # 对场景不检测
        if checkType == '' or checkType == 'insCheck':
            errorSet = 'Error_Instance'
            if not setState:
                errorNames = checkInstance() # sk_checkTools.sk_checkTools().checkInstance()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【instance】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_012')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测SmoothSet
        # 只对model，tx，render进行检测
        # if checkType == '' or checkType == 'smoothSet':
        #     errorSet = 'Error_SmoothLost'
        #     if stepSimp in ['mo','tx']:
        #         errorNames = sk_checkTools.sk_checkTools().checkModelSmoothSet(shotInfo[0])
        #         if errorNames:
        #             if errorNames == [u'未发现正版SMOOTH_SET']:
        #                 infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
        #                 errorPrintNum += 1
        #             if errorNames == [u'未发现有效SMOOTH物体']:
        #                 infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
        #                 errorPrintNum += 1
        #             if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
        #                 for name in errorNames:
        #                     infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
        #                     errorPrintNum += 1
        #                 mc.sets(errorNames , e=1 , addElement=errorSet)
        #         else:
        #             mc.delete(errorSet)
        #     else:
        #         mc.delete(errorSet)

        # 检测SmoothSet
        # 只对model，tx，render进行检测

        if checkType == '' or checkType == 'smoothSet':
            

            errorSet = 'Error_SmoothLost'
            smoothSetError = False
            if stepSimp in ['mo','tx']:
                
                smSet = mc.ls('SMOOTH_SET*', type = 'objectSet')
                
                if len(smSet) == 0:
                    smoothSetError = True
                    infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                    errorPrintNum += 1

                if len(smSet) > 1:
                    smoothSetError = True
                    infoWrong.append(u'【SmoothSet】\t\t存在多余的 SMOOTH_SET')
                    errorPrintNum += 1

                if len(smSet) == 1:
                    childSet = mc.sets(smSet[0], q = True)
                    hadObj = False
                    for cs in childSet:
                        if cs in ['smooth_0', 'smooth_1', 'smooth_2']:
                            objsInChildSet = mc.sets(cs, q = True)
                            if objsInChildSet:
                                hadObj = True
                        else:
                            smoothSetError = True
                            infoWrong.append(u'【SmoothSet】\t\tSMOOTH_SET名字不正确： %s' % cs)
                            errorPrintNum += 1

                    if not hadObj:
                        smoothSetError = True
                        infoWrong.append(u'【SmoothSet】\t\tSMOOTH_SET中没有物体')
                        errorPrintNum += 1

            if not smoothSetError:
                mc.delete(errorSet)

                # if errorNames:
                #     if errorNames == [u'未发现正版SMOOTH_SET']:
                #         infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                #         errorPrintNum += 1
                #     if errorNames == [u'未发现有效SMOOTH物体']:
                #         infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                #         errorPrintNum += 1
                #     if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                #         for name in errorNames:
                #             infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                #             errorPrintNum += 1
                #         mc.sets(errorNames , e=1 , addElement=errorSet)
                # else:
                #     mc.delete(errorSet)
            else:
                mc.delete(errorSet)


        # CacheSet
        #sk_sceneTools.sk_sceneTools().checkCacheSetAdd()
        # AnimSet
        #sk_sceneTools.sk_sceneTools().checkTransAnimSetAdd()
        #sk_sceneTools.sk_sceneTools().sk_sceneSetCombineConfig(shotInfo[0])
        print(u'\n')


        if printMode:print('-----c_013')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测重名错误
        if checkType == ''  or checkType == 'sameTransformCheck':
            errorSet = 'Error_SameNameNode'
            errorNames = []
            if not setState:
                errorNamesTemp = checkSameName() #sk_checkTools.sk_checkTools().checkSameName()
                if errorNamesTemp:
                    for name in errorNamesTemp:
                        #if '|MODEL|' in name:
                        errorNames.append(name)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_014')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测重名错误|shape节点检测
        if checkType == '' or checkType == 'sameShapeCheck':
            errorSet = 'Error_SameNameShape'
            errorNames = []
            if not setState:
                errorNamesTemp = checkSameName('mesh') # sk_checkTools.sk_checkTools().checkSameName('mesh')
                errorNamesTemp = errorNamesTemp + checkSameName('nurbsCurve') #sk_checkTools.sk_checkTools().checkSameName('nurbsCurve')
                if errorNamesTemp:
                    for name in errorNamesTemp:
                        #if '|MODEL|' in name:
                        errorNames.append(name)
                passList = []
                if errorNames and (tf.proj + '_' + tf.id) not in passList:
                    for name in errorNames:
                        infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_015')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 检测mesh同名节点
        if checkType == '' or checkType == 'sameShapeNodeCheck':
            errorSet = 'Error_SameShapeNode'
            if not setState:
                errorNames = []
                errorNamesTemp = checkMeshSameNameNodes() #sk_checkTools.sk_checkTools().checkMeshSameNameNodes()
                if errorNamesTemp:
                    for name in errorNamesTemp:
                        #if '|MODEL|' in name:
                        errorNames.append(name)
                if errorNames:
                    if errorNames == [u'有同名mesh!!!']:
                        infoWrong.append(u'【shape重名】\t\t%s' % (str('有同名mesh!!!')))
                    else:
                        for name in errorNames:
                            infoWrong.append(u'【shape同名】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_016')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 归零检测
        if checkType == '' or checkType == 'zeroAttrCheck':
            errorSet = 'Error_zeroAttrCheck'
            if not setState:
                errorObjs  = checkZeroMeshAttrs() #sk_checkTools.sk_checkTools().checkZeroMeshAttrs()
                errorCtrls = []
                if stepSimp in ['rg']:
                    errorCtrls = checkZeroCtrlAttrs(checkType = 1) # sk_checkTools.sk_checkTools().checkZeroCtrlAttrs(checkType = 1)
                errorNames = errorObjs + errorCtrls
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【没有归零】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    if mc.ls(errorCtrls):
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        if mc.ls(errorObjs):
                            mc.sets(errorObjs , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_017')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # polygon父子检测
        if checkType == '' or checkType == 'polyCPoly':
            errorSet = 'Error_polyCPoly'
            if not setState and stepSimp in ['mo','tx']:
                errorNames = checkPolyParents() #sk_checkTools.sk_checkTools().checkPolyParents()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【父子Polyon】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_018')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 无用表达式检测
        if checkType == '' or checkType == 'noneedexp':
            errorSet = 'Error_noneedexp'
            errorNames = checkNoNeedExpression() #sk_checkTools.sk_checkTools().checkNoNeedExpression()
            if errorNames:
                for name in errorNames:
                    infoWrong.append(u'【无用表达式】\t\t%s' % (str(name)))
                    errorPrintNum += 1
                mc.sets(errorNames , e=1 , addElement=errorSet)
            else:
                mc.delete(errorSet)
        print(u'\n')

        if printMode:print('-----c_019')
        if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
        timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

        # tx文件参考检测
        if checkType == '' or checkType == 'txRndRef':
            if stepSimp in ['tx'] :
                errorNames = checkTXRefRnd() #sk_checkTools.sk_checkTools().checkTXRefRnd()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【参考错误】\t\t%s' % (str(name)))
                        errorPrintNum += 1

        # tx文件检测材质赋予
        if checkType == '' or checkType == 'txRLCheck':
            errorSet = 'Error_txRLCk'
            if stepSimp in ['tx'] :
                errorNames = checkTextureModelShader(returnMode = 1) #sk_checkTools.sk_checkTools().checkTextureModelShader(returnMode = 1)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【分层测试】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                else:
                    mc.delete(errorSet)
            else:
                mc.delete(errorSet)


        if checkType == '' or checkType == 'arnoldSHDAndIDP':
            # 对tx检测
            if stepSimp in ['tx']:
                mats = mc.ls(materials = True)
                for mat in mats:
                    if mat not in ['lambert1', 'particleCloud1', 'shaderGlow1']:
                        if mc.nodeType(mat) not in ['aiStandardSurface', 'aiTwoSided']:
                            infoWrong.append(u'【非aiStandardSurface材质球】\t\t%s' % (str(mat)))
                            errorPrintNum += 1

                        endName = mat.split('_')[-1]
                        if endName not in tiBase.nameRulesArray():
                            infoWrong.append(u'【材质球名字后缀不符合规范】\t\t%s' % (str(mat)))
                            errorPrintNum += 1


        if checkType == '' and mc.about(batch = True) == False:

            if stepSimp in ['mo', 'tx', 'rg']:

                if not mc.objExists( '__OA__'):
                    infoWrong.append(u'【似乎没用OA工具打开过文件，请用OA工具打开文件】')
                    errorPrintNum += 1
           
            if mc.attributeQuery( '__OA__', node='layerManager', ex = True):
                mc.deleteAttr('layerManager.__OA__')

        if checkType == '':
            if stepSimp in ['mo', 'rg']:
                tiBase.autoRenameMaterials()
    else:
        print(u'\n')
        infoWrong.append(u'【 错 误 】\t\t文件名错误! ')
        errorPrintNum += 1

    # 删除ErrorSet
    if errorPrintNum == 0:
        try:
            mc.delete('ErrorTemp_Set')
        except:
            pass

    # for i in range(len(timeInfos)):
    #     print('[%s]:\t%s'%(str(i+1),timeInfos[i]))

    # 输出DetailsUI
    # if UIShow:
    #     sk_checkTools.sk_checkTools().checkDetailsUI(infoWrong)
    #     sk_checkTools.sk_checkTools().checkConfigHelpUI()

    # 输出错误消息
    print(u'=============================【文件中错误如下】=============================')
    for info in infoWrong:
        print(info)
    errorInfo = (u'===========================【目前】共计【%s】处错误===========================' %errorPrintNum)
    mc.warning(errorInfo)
    if errorMode and errorPrintNum:
        print(errorInfo)
        mc.error()

    print('start time:%s'%startTime)
    print('end   time:%s'%(time.strftime("%Y-%m-%d %H:%M:%S")))

    # 解锁
    checkUnlockMSHV()
    checkUnlockMSHGeo(0)
    return errorPrintNum


# tx文件测试，所有模型重新赋予材质，失败则报错
def checkTextureModelShader(returnMode = 0,MODELSkipState = 0,renderGrp = 'MODEL'):
    meshes = mc.ls(type='mesh', l=1)
    if not meshes:
        return
    return
    # 创建新渲染层
    testLayer = 'food_shaderLayer_test'
    if mc.ls(testLayer):
        mc.delete(testLayer)
    modelKey = renderGrp
    if MODELSkipState:
        modelKey = self.tempRGrp
    # 获取MODEL下的
    needObjs = []
    noCheckGrps = ['hairSys_Grp','vfxGrp'] # sk_infoConfig.sk_infoConfig().dyMoGrps
    for mesh in meshes:
        checkState = 1
        for checkGrp in noCheckGrps:
            if '|%s|'%modelKey in mesh:
                checkState = 0
        if not checkState:
            continue
        if '|%s|'%modelKey in mesh:
            needObjs.append(mc.listRelatives(mesh, p=1, f=1)[0])
    needObjs = list(set(needObjs))
    # 创建层
    if not needObjs:
        return
    # 首先备份材质球信息
    # from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout
    # reload(sk_cacheFinalLayout)
    MatLists = tiBase.sgAndMeshsInfo() #sk_cacheFinalLayout.sk_cacheFinalLayout().checkCacheRecordMaterial(checkObjs = needObjs , finalLayout = 0 ,faceMode = 1,shotType = sk_infoConfig.sk_infoConfig().checkShotType(), server = 0)
    errorObjs = []
    mc.createRenderLayer(needObjs , name='food_shaderLayer_test' , noRecurse=1 , makeCurrent=1)
    # 创建材质
    shaderMain = mc.shadingNode ('lambert', asShader=True, name='food_shader_test')
    shaderMianSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name='food_shader_test_SG')
    mc.connectAttr((shaderMain + '.outColor'), (shaderMianSG + '.surfaceShader'))
    for obj in needObjs:
        mesh = mc.listRelatives(obj, ni=1, s=1)
        if not mesh:
            continue
        mesh = mesh[0]
        try:
            mc.sets(obj, e=1, forceElement=shaderMianSG)
        except:
            errorObjs.append(mesh)
    # 删除层，清理垃圾节点
    # Back To MasterLayer
    mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
    mc.delete(testLayer)
    mc.delete(shaderMain)
    mc.delete(shaderMianSG)
    SGInfos = MatLists.keys()
    print('----------------')
    print(MatLists)

    for checkSGNode in SGInfos:
        shapes = MatLists[checkSGNode]
        for mesh in shapes:
            checkMesh = mesh
            if '.f[' in mesh:
                checkMesh = mc.listRelatives(mesh.split('.f[')[0],s=1,ni=1,type = 'mesh',f=1)[0]
            SGNode = mc.listConnections(checkMesh,d=1,type = 'shadingEngine')
            if not SGNode:
                errorObjs.append(mesh)
            else:
                if checkSGNode not in SGNode:
                    errorObjs.append(mesh)

    if returnMode:
        if errorObjs:
            errorObjs = list(set(errorObjs))
        return errorObjs
    if errorObjs:
        errorObjs = list(set(errorObjs))
        for errorObj in errorObjs:
            print(u'-------------')
            print(errorObj)
            print(errorObj.split('|')[-1])
        #errorInfo = sk_infoCore.sk_infoCore().sk_infoCore(39)
        errorInfo= u'-------------[着色]某些物体无法赋予材质，请处理好它们-------------'
        print(errorInfo)
        
        mc.error()

# 获取referenceList
def checkReferenceListInfo():
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
        refPaths.append(checkReferencePathConfig(refInfo))
        #refPaths.append(checkReferencePathConfig(str(refInfo.path)))
        refPath = mc.referenceQuery(refInfo , filename = 1)
        refNamespace.append(checkReferenceGetNamespaceInfoByPath(refPath))
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
                    refPathsDown.append(checkReferencePathConfig(mc.referenceQuery(refNodeD, f=1)))
                    # 记录namespace
                    refNamespaceDown.append(checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNodeD, f=1)))
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


# 通过refPath 获取refNode的namespace
def checkReferenceGetNamespaceInfoByPath(refPth):
    namespace = mc.file( refPth ,namespace = 1 ,q = 1 )
    # 判断是不是子参考
    parentRef = mc.referenceQuery( refPth , referenceNode=True, parent = True )
    if parentRef:
        namespace = parentRef[:-2] + ':' + namespace 
    return namespace


# 处理reference路径，清楚后面可能存在的{}
def checkReferencePathConfig(path):
    if '{' in path:
        path = path.split('{')[0]
    return path
#-------------------------------#
# tx文件参考rnd文件
def checkTXRefRnd():
    fileName = mc.file(exn = 1, q= 1).split('/')[-1]
    if '_' not in fileName:
        return []
    errorInfos = []
    # import sk_referenceConfig
    # reload(sk_referenceConfig)
    refInfos = checkReferenceListInfo() #sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
    rfnPathLv1 = refInfos[1][0]
    for refPath in rfnPathLv1:
        needInfo = refPath.split('/')[-1]
        if len(needInfo.split('_')) < 4:
            errorInfos.append(refPath.split('/')[-1])
        else:
            if '_ms_render.' not in needInfo.split('_')[3]:
                errorInfos.append(refPath.split('/')[-1])
    return errorInfos

# 无用表达式筛选
def checkNoNeedExpression():
    # 检测SG节点
    expNodes = mc.ls(type = 'expression')
    noNeedList = []
    for checkNode in expNodes:
        cons = mc.listConnections(checkNode,s=0,d=1)
        if not cons:
            noNeedList.append(checkNode)
    return noNeedList


#------------------------------#
# 检测polygon是polygon的父体
def checkPolyParents(renderGrp = 'MODEL'):
    meshes = mc.listRelatives(renderGrp,ad = 1, type = 'mesh',f=1)
    errorObjs = []
    extraInfo = ['eye']
    extraAttrs =  ['_hair_']
    if not meshes:
        return errorObjs
    for mesh in meshes:
        objGrp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
        if not objGrp:
            continue
        objGrp = objGrp[0]
        if mc.ls(objGrp + '._nr_'):
            continue
        checkMode = 1
        # 屏蔽特殊类型物体
        for attr in extraAttrs:
            if mc.ls(objGrp + '.' + attr):
                checkMode = 0
                break
        if not checkMode:
            continue
        # 检测
        childMeshes = mc.listRelatives(objGrp,ad = 1,type = 'mesh',f=1)
        lenCheck = 2
        for info in extraInfo:
            if info in mesh.split('|')[-1].lower():
                lenCheck = 3
                break
        if len(childMeshes) >= lenCheck:
            errorObjs.append(objGrp)
    if errorObjs:
        return list(set(errorObjs))
    else:
        return errorObjs



# ctrls
def checkZeroCtrlAttrs(checkType = 0,minCheck = -5,ctrlSetList = ['All_BodySet']):
    errorObjs = []
    checkAttrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
    scaleAttrs = ['.sx','.sy','.sz']
    skipKey = ['_noZero_','_nozero_']
    # 控制器
    ctrlShapes = []
    if checkType == 0:
        ctrlShapes = mc.ls(type = 'nurbsCurve',l = 1)
    if checkType == 1:
        for ctrlSet in ctrlSetList:
            if not mc.ls(ctrlSet):
                continue
            ctrlTemp = mc.sets(ctrlSet, q=1)
            ctrlTemp = mc.listRelatives(ctrlTemp,s = 1,type = 'nurbsCurve',f = 1)
            ctrlShapes += ctrlTemp
    if not ctrlShapes:
        return errorObjs
    for ctrlShape in ctrlShapes:
        ctrl = mc.listRelatives(ctrlShape,p = 1,f=1)
        if not mc.ls(ctrl):
            continue
        ctrl = ctrl[0]
        skipState = 0
        for checkInfo in skipKey:
            if mc.ls('%s.%s'%(ctrl,checkInfo)):
                skipState = 1
        if skipState:
            continue
        errorState = 0
        for attr in checkAttrs:
            if not mc.getAttr((ctrl + attr),keyable = 1):
                continue
            if abs(mc.getAttr(ctrl + attr)) > pow(10,minCheck):
                errorState = 1
                break
        for attr in scaleAttrs:
            if not mc.getAttr((ctrl + attr),keyable = 1):
                continue
            if abs(mc.getAttr(ctrl + attr)-1) > pow(10,minCheck):
                errorState = 1
                break
        if errorState:
            errorObjs.append(ctrl)
    return errorObjs


def checkZeroMeshAttrs(minCheck = -3,MODELSkipState = 0,renderGrp = 'MODEL'):
    errorObjs = []
    checkAttrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
    scaleAttrs = ['.sx','.sy','.sz']
    extraInfo = ['_eye','_nozero']
    extraAttrs = ['_noZero','_nozero_','_noZero_']
    modelKey = renderGrp
    if MODELSkipState:
        modelKey = self.tempRGrp
    modelGrp = mc.ls(modelKey)
    if not modelGrp:
        modelGrp = mc.ls('*:%s'%modelKey)
    if modelGrp:
        rootGrp = mc.ls(assemblies=True,l=1)
        removelist = ['|persp','|top','|front','|side']
        for removGrp in removelist:
            if removGrp in rootGrp:
                rootGrp.remove(removGrp)
        # mesh
        objs = mc.listRelatives(modelGrp,ad = 1 ,type = 'transform',f= 1)
        if not objs:
            return errorObjs
        objs = objs + rootGrp
        for checkObj in objs:
            errorState = 0
            extraState = 0
            # 判断是否例外
            for info in extraInfo:
                if info in checkObj.split('|')[-1].lower():
                    extraState = 1
            for exAttr in extraAttrs:
                if mc.ls('%s.%s'%(checkObj,exAttr)):
                    extraState = 1
            if extraState:
                continue
            # tx,rotate
            for attr in checkAttrs:
                if not mc.getAttr((checkObj + attr),keyable = 1):
                    continue
                if abs(mc.getAttr(checkObj + attr)) > 5*pow(10,minCheck):
                    if extraState == 0:
                        errorState = 1
                        break
            # scale
            for attr in scaleAttrs:
                if abs(mc.getAttr(checkObj + attr)-1) > 5*pow(10,minCheck):
                    if extraState == 0:
                        errorState = 1
                        break
            if errorState:
                errorObjs.append(checkObj)
    return errorObjs

# 检测mesh同名物体（包括）
def checkMeshSameNameNodes():
    # 获取mesh
    meshes = mc.ls(type = 'mesh')
    allMeshes = list(set(meshes))
    errorInfo = []
    if len(meshes) == len(allMeshes):
        for mesh in meshes:
            shapeName = mesh
            if '|' in mesh:
                shapeName = mesh.split('|')[-1]
            meshSame = mc.ls(shapeName,l=1)
            if len(meshSame) > 1:
                for obj in meshSame:
                    if mc.nodeType(obj) != 'mesh':
                        errorInfo.append(obj)
    else:
        errorInfo = [u'有同名mesh!!!']
    return errorInfo


# 获取重名
def checkSameName(nodeType='transform',justCheck = '',needShape = 0):
    # translate处理
    errorInfo = []
    if nodeType in ['transform']:
        grps = mc.ls(type=nodeType, l=1)
        simpleGrps = []
        simpleSetGrps = []
        check = 0
        skipNum = 0
        for grp in grps:
            if justCheck :
                if not (':%s|'%justCheck in grp or '|%s|'%justCheck in grp):
                    skipNum += 1
                    continue
            if needShape:
                shape = mc.listRelatives(grp,s=1)
                if not shape:
                    skipNum += 1
                    continue
            simple = grp.split('|')[-1]
            simpleGrps.append(simple)
            simpleSetGrps.append(simple)
            if (len(list(set(simpleSetGrps))) + check) != len(simpleGrps):
                check += 1
                tempGrps = simpleGrps[:]
                tempAdd = 0
                while tempGrps.count(simple) > 0:
                    errorInfo.append(grps[int(tempGrps.index(simple) + tempAdd + skipNum)])
                    tempAdd += 1
                    tempGrps.remove(simple)
    # mesh|shape处理
    if nodeType in ['mesh','nurbsCurve']:
        grps = mc.ls(type=nodeType, l=1)
        simpleGrps = []
        simpleSetGrps = []
        check = 0
        skipNum = 0
        for grp in grps:
            if justCheck and '%s|'%justCheck not in grp:
                skipNum += 1
                continue
            simple = grp.split('|')[-1]
            simpleGrps.append(simple)
            simpleSetGrps.append(simple)
            if (len(list(set(simpleSetGrps))) + check) != len(simpleGrps):
                check += 1
                tempGrps = simpleGrps[:]
                tempAdd = 0
                while tempGrps.count(simple) > 0:
                    errorInfo.append(grps[int(tempGrps.index(simple) + tempAdd + skipNum)])
                    tempAdd += 1
                    tempGrps.remove(simple)
    return list(set(errorInfo))


# MODEL或者其他阶段的instance检测
def checkInstance(model = 0,renderGrp = 'MODEL'):
    if model == 1:
        grps = mc.ls(type='transform', l=1)
        grps.remove('|persp')
        grps.remove('|top')
        grps.remove('|front')
        grps.remove('|side')
    else:
        model = mc.ls(renderGrp)
        try:
            grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
        except:
            grps = []
    errorInfo = []
    newGrps = []
    if grps:
        for grp in grps:
            shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
            if shape:
                newGrps.append(shape[0].split('|')[-1])
                lenOld = len(newGrps)
                newGrps = list(set(newGrps))
                lenNew = len(newGrps)
                if lenOld != lenNew:
                    errorInfo.append(grp)

# 多边面检测
def checkFaceVertexs(outInfo = 0,smoothSkip = 0 , triangleNum = 1,doNotCheckGrp = ['hairSys_Grp'],MODELSkipState = 0,renderGrp = 'MODEL'):
    errorInfo = []
    irInfo = '_ir_'
    nrAttr = '_nr_'
    modelKey = renderGrp
    if MODELSkipState:
        modelKey = self.tempRGrp
    model = mc.ls(modelKey)
    if not model:
        model = mc.ls('*:%s'%modelKey)
        if not model:
            return [[],[]]
    doNotCheckGrp = ['hairSys_Grp','vfxGrp'] # doNotCheckGrp + sk_infoConfig.sk_infoConfig().dyMoGrps
    # smoothSkip处理
    smoothCheckObjs = []
    if smoothSkip:
        checkObjs = []
        if mc.ls('smooth_0'):
            smoothCheckObjs = mc.sets('smooth_0', q=1)
            smoothCheckObjs = mc.ls(smoothCheckObjs,l=1)
            checkObjs = checkObjs + smoothCheckObjs
        if mc.ls('*:smooth_0'):
            smsSetNode = mc.ls('*:smooth_0')
            smoothCheckObjs = mc.sets(smsSetNode, q=1)
            smoothCheckObjs = mc.ls(smoothCheckObjs,l=1)
            checkObjs = checkObjs + smoothCheckObjs
        smoothCheckObjs = checkObjs
    grps = mc.listRelatives(model[0], type='transform', ad=1, f=1)
    if not grps:
        return [[],[]]
    triangleErrorObjs = []
    for grp in grps:
        shape = mc.listRelatives(grp, ni=1 , s=1 , type='mesh' , f=1)
        triangleCheckNum = 0
        doNotCheckState = 0
        for checkGrp in doNotCheckGrp:
            if '%s|'%checkGrp in grp:
                doNotCheckState = 1
            break
        if doNotCheckState:
            continue
        if not shape:
            continue
        if smoothSkip and grp in smoothCheckObjs:
            continue
        try:
            faceNum = mc.polyEvaluate(grp, f=1)
            # 这里有时候会出错,尤其是命名中加了"_ca_"和"_"后缀的时候
            if faceNum:
                for i in range(faceNum):
                    # 获取面的点
                    pointInfo = list(set(mc.polyInfo((grp + '.f[' + str(i) + ']'), faceToVertex=1)[0].split(':')[1].split(' ')))
                    if outInfo:
                        # 检测模式，查询所有非四边形
                        if len(pointInfo) not in [6]:
                            addState = 1
                            if irInfo in grp.split('|')[-1].lower():
                                addState = 0
                            if mc.ls(grp + '.' + nrAttr):
                                addState = 0
                            if addState:
                                errorInfo.append(grp + '.f[' + str(i) + ']')
                        else:
                            if len(pointInfo) in [5]:
                                triangleCheckNum += 1
                    else:
                        # checkin模式，拦截非三角形、四边形、五边形
                        if len(pointInfo) not in [5,6,7]:
                            addState = 1
                            if irInfo in grp.split('|')[-1].lower():
                                addState = 0
                            if mc.ls(grp + '.' + nrAttr):
                                addState = 0
                            if addState:
                                errorInfo.append(grp + '.f[' + str(i) + ']')
                        else:
                            if len(pointInfo) in [5]:
                                triangleCheckNum += 1
            else:
                addState = 1
                if irInfo in grp.split('|')[-1].lower():
                    addState = 0
                if mc.ls(grp + '.' + nrAttr):
                    addState = 0
                if addState:
                    errorInfo.append(grp)
            if triangleCheckNum / faceNum > triangleNum:
                triangleErrorObjs.append(grp)
        # 对残留的shape节点进行处理，某些组有shape节点，但不是polygon
        except:
            addState = 1
            if irInfo in grp.split('|')[-1].lower():
                addState = 0
            if mc.ls(grp + '.' + nrAttr):
                addState = 0
            if addState:
                errorInfo.append(grp)
    return [list(set(errorInfo)),triangleErrorObjs]




# MODEL组下，模型基本渲染属性开启检测
def checkMeshRenderStates(errorMode = 0,renderGrp = 'MODEL'):
    errorObjs = []
    nrKeyList = ['_si_','_nr_','_proxy_']
    modelGrps = mc.ls(renderGrp,l=1) + mc.ls('*:'+renderGrp,l=1)
    attrs = ['.castsShadows','.receiveShadows','.motionBlur','.primaryVisibility','.smoothShading']
    attrs += ['.aiVisibleInDiffuse','.aiVisibleInGlossy']
    shotInfo = checkShotInfo()
    Eyes=[]
    if modelGrps:
        objs = mc.listRelatives(modelGrps,ad = 1 ,type = 'transform',f= 1)
        if objs:
            for mod in objs:
                if mc.objExists(mod+'.eye') and mod not in Eyes:
                    Eyes.append(mod)
    print(Eyes)
    attrsN=['.motionBlur','.primaryVisibility','.smoothShading','.aiVisibleInDiffuse','.aiVisibleInGlossy']
    if shotInfo[0] in ['ddz']:
        attrsN=['.motionBlur']
    if modelGrps:
        objs = mc.listRelatives(modelGrps,ad = 1 ,type = 'transform',f= 1)
        if not objs:
            return []
        for obj in objs:
            if obj not in Eyes:
                attrs=attrs
            else:
                attrs=attrsN
            mesh = mc.listRelatives(obj,s=1,ni=1,type = 'mesh',f=1)
            if mesh:
                mesh = mesh[0]
                checkState = 0
                for attr in attrs:
                    if not mc.ls(mesh + attr):
                        continue
                    state = mc.getAttr(mesh + attr)
                    if state == 0:
                        checkState = 1
                        break
                if '_si_' in obj or '_nr_' in obj or '_proxy_' in obj  or '_p_' in obj or '_ctrl' in obj:
                    checkState = 0
                for nrKey in nrKeyList:
                    if mc.ls('%s.%s'%(obj,nrKey)):
                        checkState = 0
                if checkState:
                    errorObjs.append(obj)
    else:
        errorObjs = ['No %s'%renderGrp]
    if errorMode and errorObjs:
        print('----------------------')
        for errorInfo in errorObjs:
            print(errorInfo)
        print(u'-----渲染shape属性没开启-----')
        mc.error()
    return errorObjs


def checkShotInfo(noFormat = 0):
    temp = (mc.file(query=1, exn=1)).split('/')
    info = []
    if '_' in temp[len(temp) - 1]:
        info = temp[len(temp) - 1].split('_')
        if noFormat and '.' in info[-1]:
            info[-1] = info[-1].split('.')[0]
    else:
        mc.warning(u'========================【！！！文件名不规范！！！】========================')
    return info

def checkProjMODELGrp(fileInfos = [] ,projStyle = 0):
    modelGrp = 'MODEL'
    if not fileInfos:
        fileInfos = checkShotInfo()
    if projStyle in [2]:
        if fileInfos[2] in ['CH']:
            modelGrp = 'Model_Hight'
        if fileInfos[2] in ['PRO']:
            modelGrp = 'MODEL'
        if fileInfos[2] in ['BG']:
            modelGrp = 'SCENES'
    return modelGrp

# 设置，约束必须放到灯光或者物体层级
def checkconstraintObjs(returnMode = 1,projStyle = 0):
    constraintNodes = mc.ls(type = 'constraint')
    skipTypes = ['mesh','joint','light','baselattice','lattice','constraint']
    renderGrp = checkProjMODELGrp(projStyle = projStyle)
    errorGrps = []
    for checkNode in constraintNodes:
        targetGrps = mc.listConnections(checkNode,s=0,d=1,type = 'transform')
        if not targetGrps:
            continue
        targetGrps = list(set(targetGrps))
        for checkGrp in targetGrps:
            if 'constraint' in checkGrp.lower():
                continue
            fullNode = mc.ls(checkGrp,l=1)[0]
            if '%s|'%renderGrp not in fullNode:
                continue
            if not ('|%s|'%renderGrp in fullNode or ':%s|'%renderGrp in fullNode):
                continue
            childNode = mc.listRelatives(fullNode,s=1,ni=1)
            if not childNode:
                errorGrps.append(fullNode)
            else:
                childType = mc.nodeType(childNode)
                skipState = 0
                for skipType in skipTypes:
                    if skipType in childType.lower():
                        skipState = 1
                if not skipState:
                    errorGrps.append(fullNode)
    # 进一步判断,下面的mesh有没有蒙皮
    tempGrps = []
    for checkGrp in errorGrps:
        meshes = mc.listRelatives(checkGrp,ad = 1, type = 'mesh',f = 1)
        if not meshes:
            continue
        grps = mc.listRelatives(meshes,p=1,type = 'transform',f=1)
        grps = list(set(grps))
        for grp in grps:
            childMeshes = mc.listRelatives(grp,ad=1,type = 'mesh',f=1)
            if len(childMeshes) == 1:
                tempGrps.append(checkGrp)
    errorGrps = tempGrps
    # 返回
    if returnMode:
        return errorGrps
    else:
        if errorGrps:
            print(u'--------------[角色道具]请把约束放到物体级别，别放组上--------------')
            for errorGrp in errorGrps:
                print(errorGrp)
            print(u'--------------[角色道具]请把约束放到物体级别，别放组上--------------')

def gdc_TrShadeInfo(returnMode = 0):
    SGS=mc.ls(type='shadingEngine',l=1)
    if not SGS:
        pass
    shadeTrs=[]
    shadetrerror=[]
    for sg in SGS:
        cons=mc.listConnections( (sg+'.surfaceShader'), d=False, s=True,c=False )
        if cons:
            shade=cons[0]
            if mc.objExists(shade+'.transparency'):
                trs=mc.listConnections((shade+'.transparency'),d=0,s=1,p=1 )
            elif mc.objExists(shade+'.outTransparency'):
                trs=mc.listConnections((shade+'.outTransparency'),d=0,s=1,p=1 )
            else:
                pass
            if mc.ls(trs) and '.outTransparency' in trs[0] and trs[0] not in shadetrerror:
                shadetrerror.append(shade)
            if mc.ls(trs) and mc.nodeType(trs[0])!='file' and trs[0] not in shadetrerror:
                shadetrerror.append(shade)
            if trs and '.outColor' in trs[0] and mc.nodeType(trs[0])=='file' and trs[0] not in shadeTrs:
                shadeTrs.append(shade)
    result=[shadeTrs,shadetrerror]
    if not returnMode:
        return result
    else:
        return shadeTrs


# 检测贴图尺寸
def checkTextureFileSize(returnMode = 1,sizeMax = 2):
    checkTxFiles = []
    checkNodes = []
    # 收集
    fileNodes = mc.ls(type = 'file') + mc.ls(type = 'aiImage')
    for checkNode in fileNodes:
        checkType = mc.nodeType(checkNode)
        checkAttr = '.fileTextureName'
        if checkType in ['aiImage']:
            checkAttr = '.filename'
        txFile = mc.getAttr(checkNode + checkAttr)
        checkTxFiles.append(txFile)
        checkNodes.append(checkNode)
    yetiNodes = mc.ls(type = 'pgYetiMaya')
    for yetiNode in yetiNodes:
        txNodes = mc.pgYetiGraph(yetiNode,listNodes= 1, type = 'texture')
        if not txNodes:
            continue
        for checkTxNode in txNodes:
            txFile = mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name', getParamValue = 1)
            checkTxFiles.append(txFile)
            checkNodes.append(checkTxNode)
    # 检测
    maxSize = 1024*sizeMax
    import maya.OpenMaya
    img = maya.OpenMaya.MImage()
    errorFiles = []
    for num in range(len(checkTxFiles)):
        txFile = checkTxFiles[num]
        if not txFile:
            continue
        #img.readFromFile(txFile)
        #width = maya.OpenMaya.uIntPtr()
        #height = maya.OpenMaya.uIntPtr()
        #img.getSize(width, height)
        #if width.value() > maxSize:
        # 这一段有两问题，一来txFile带环境变量时会报错，二来很慢，暂时用这个旧的mel函数代替，黄仲维，20161115
        wh = mel.eval('zwImageSize "%s"' % (txFile.replace("\\", "/")))
        if not wh:
            print(u'------------TxFile Path Error')
            print(txFile)
            mc.error()
        if wh[0] > maxSize:
            indexNum = checkTxFiles.index(txFile)
            errorFiles.append(checkNodes[indexNum])
    if returnMode:
        return errorFiles



def checkRGModel(MODELSkipState = 0,renderGrp = 'MODEL'):
    if MODELSkipState:
        modelKey = self.tempRGrp
    if not mc.ls('*:%s'%renderGrp):
        return []
    ModelGrp = mc.ls('*:%s'%renderGrp)
    checkGrp = mc.listRelatives(ModelGrp,p=1,f= 1)
    meshes = []
    temp = mc.listRelatives(checkGrp,ad = 1, type = 'mesh',f=1)
    if not temp:
        temp = []
    meshes = meshes + temp
    temp = mc.listRelatives(checkGrp,ad = 1,type = 'baseLattice',f = 1)
    if not temp:
        temp = []
    meshes = meshes + temp
    errorList = []
    for mesh in meshes:
        ifRef = mc.referenceQuery(mesh,isNodeReferenced = 1)
        if ifRef:
            continue
        grp = mc.listRelatives(mesh,p=1,f=1,type = 'transform')
        if not grp:
            continue
        ifRef = mc.referenceQuery(grp,isNodeReferenced = 1)
        if ifRef:
            continue
        errorList.append(mesh)
    return errorList
# 前期角色道具tx文件检测选面
def checkFaceShaderDetails(MODELSkipState = 0,renderGrp = 'MODEL'):
    # 检测SG节点
    errorAssetMeshes = []
    SGNodes = mc.ls(type='shadingEngine')
    modelKey = renderGrp
    if MODELSkipState:
        modelKey = self.tempRGrp
    for node in SGNodes:
        meshes = mc.sets(node, q=1)
        print meshes
        print node
        if not meshes:
            continue
        for mesh in meshes:
            meshLong = mc.ls(mesh,l=1)[0]
            if '|%s|'%modelKey not in meshLong:
                continue
            if '.' in mesh:
                checkType = mc.nodeType(mesh.split('.')[0])
            else:
                checkType = mc.nodeType(mesh)
            if checkType in ['mesh']:
                meshFull = mc.ls(mesh,l = 1)[0]
                if '.f[' in mesh:
                    errorAssetMeshes.append(meshFull)
            else:
                meshGrp = mesh.split('.')[0]
                if meshGrp not in errorAssetMeshes:
                    errorAssetMeshes.append(meshGrp)
    return errorAssetMeshes

def checkErrorObjects(checkType = '',renderGrp = 'MODEL'):
    checkMeshes = mc.listRelatives(renderGrp,ad=1,ni=1,type = 'mesh',f=1)
    if not checkMeshes:
        return []
    checkObjs = mc.listRelatives(checkMeshes,p=1,f=1)
    errorObjs = []
    if checkType in ['nonManifoldEdges']:
        errorObjs= mc.polyInfo(checkObjs,nonManifoldEdges=True)

    if checkType in ['nonManifoldVertices']:
        errorObjs= mc.polyInfo(checkObjs,nonManifoldVertices=True)

    if checkType in ['laminaFaces']:
        errorObjs= mc.polyInfo(checkObjs,laminaFaces=True)

    needObjs = []
    if not errorObjs:
        errorObjs = []
    for checkObj in errorObjs:
        checkNode = checkObj
        if '.' in checkNode:
            checkNode = checkNode.split('.')[0]
        if mc.ls(checkNode + '._plfIg_'):
            continue
        needObjs.append(checkObj)

    return needObjs

def checkIntermediateObjectError(MODELSkipState = 0,renderGrp = 'MODEL'):
    errorInfo = []
    extraInfo = ['eye']
    model = mc.ls(renderGrp,l = 1)
    if MODELSkipState:
        model = mc.ls(renderGrp,l = 1)
    if not model:
        return []
    meshes = mc.listRelatives(model,ad = 1,type = 'mesh',f = 1)
    if not meshes:
        return []
    extraAttrs = ['_hair_']
    for mesh in meshes:
        value = mc.getAttr(mesh + '.intermediateObject')
        if not value:
            continue
        grp = mc.listRelatives(mesh,ap = 1,type = 'transform',f = 1)
        if not grp:
            continue
        grp = grp[0]
        if mc.ls(grp + '._nr_'):
            continue
        # 屏蔽特殊属性物体
        checkMode = 1
        for attr in extraAttrs:
            if mc.ls(grp + '.' + attr):
                checkMode = 0
        if not checkMode:
            continue
        # 开始检测
        checkState = 1
        for info in extraInfo:
            if info in grp.split('|')[-1].lower():
                checkState = 0
        if checkState:
            errorInfo.append(mesh)
    return errorInfo


def checkNotPoly(MODELSkipState = 0,renderGrp = 'MODEL'):
    nodeTypes = ['nurbsSurface','nurbsCurve','subdiv']
    noCheckGrps = ['hairSys_Grp','vfxGrp']
    errorNames = []
    model = renderGrp
    if MODELSkipState:
        model = mc.ls(self.tempRGrp)
    for nodeType in nodeTypes:
        if not mc.ls(model):
            continue
        objs = mc.listRelatives(model,ad = 1,type = nodeType,f=1)
        if not objs:
            continue
        errorNames = errorNames + objs
    errorObjs = []
    for checkObj in errorNames:
        checkState = 1
        for noCheckGrp in noCheckGrps:
            if '|%s|'%noCheckGrp in checkObj:
                checkState = 0
        if not checkState:
            continue
        errorObjs.append(checkObj)
    return errorObjs


def checkNamespace(setMode = 0):
    infoWrong = []
    namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
    namespace.remove('UI')
    namespace.remove('shared')
    if len(namespace) != 0:
        if not setMode:
            for ns in namespace:
                infoWrong.append(u'存在namespace [%s],请清理掉'%ns)
        else:
            for ns in namespace:
                objs = mc.ls(ns + ':*',l=1)
                if not objs:
                    # 空的
                    infoWrong.append(u'存在非参考namespace [%s],请清理掉'%ns)
                else:
                    # 检查是否参考
                    isRef = mc.referenceQuery(objs[0], isNodeReferenced = 1)
                    if not isRef:
                        infoWrong.append(u'存在非参考namespace [%s],请清理掉'%ns)
    return infoWrong


def outlineGrps():
    grps = mc.ls(assemblies = True)
    grps.remove('persp') 
    grps.remove('top')
    grps.remove('front')
    grps.remove('side')
    return grps

def checkUnlockMSHV(justModel = 1,renderGrp = 'MODEL'):
    meshes = mc.ls(type='mesh', l=1)
    if justModel:
        meshes = mc.listRelatives(renderGrp,ad = 1, type = 'mesh',f = 1)
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

def checkUnlockMSHGeo(MODELUnlock = 1,renderGrp = 'MODEL'):
    # MODEL解锁
    if not MODELUnlock:
        return
    unlockList = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v','.lodVisibility']
    unlockObjs = mc.ls(renderGrp,l=1)
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


def checkMeshError():
    shaderSGList = tiBase.sgAndMeshsInfo()
    errorInfo = []
    if shaderSGList:
        keys = shaderSGList.keys()
        for key in keys:
            objs = shaderSGList[key]
            if objs:
                for obj in objs:
                    if mc.ls(obj):
                        pass
                    else:
                        errorInfo.append(obj) 
    return errorInfo


#------------------------------#
# ErrorSet
def checkErrorSetCreate():
    # 文件名检测，判断环节
    if mc.objExists(errorSet):
        pass
    else:
        mc.createNode('objectSet', n=errorSet)

    # 约束物体
    setName = 'Error_Constraint2Grps'
    errorSetConfig(setName)

    # 尺寸超标
    setName = 'Error_txFileSize'
    errorSetConfig(setName)

    # poly检测
    setName = 'Error_polyError'
    errorSetConfig(setName)

    # Error_imoError
    setName = 'Error_imoError'
    errorSetConfig(setName)

    # 选面物体
    setName = 'Error_faceShader'
    errorSetConfig(setName)

    # 三角面过多
    setName = 'Error_N3Edges'
    errorSetConfig(setName)

    # 非四边形
    setName = 'Error_N4Edges'
    errorSetConfig(setName)

    # instance
    setName = 'Error_Instance'
    errorSetConfig(setName)

    # smoothSet
    setName = 'Error_SmoothLost'
    errorSetConfig(setName)

    # RenderState
    setName = 'Error_RenderState'
    errorSetConfig(setName)

    # SameName Transform
    setName = 'Error_SameNameNode'
    errorSetConfig(setName)

    # SameName Shape
    setName = 'Error_SameNameShape'
    errorSetConfig(setName)

    # Error_SameShapeNode
    setName = 'Error_SameShapeNode'
    errorSetConfig(setName)

    # 归零检测
    setName = 'Error_zeroAttrCheck'
    errorSetConfig(setName)

    # MODEL层级
    setName = 'Error_modelRG'
    errorSetConfig(setName)

    # polygon父子
    setName = 'Error_polyCPoly'
    errorSetConfig(setName)

    # txRLcheck
    setName = 'Error_txRLCk'
    errorSetConfig(setName)

    # rg丢材质
    setName = 'Error_rgShader'
    errorSetConfig(setName)

    # 无用表达式
    setName = 'Error_noneedexp'
    errorSetConfig(setName)

    # 透明贴图检测
    setName = 'Error_transprancyNodes'
    errorSetConfig(setName)

    # nonManifoldEdges
    setName = 'Error_nonManifoldEdges'
    errorSetConfig(setName)

    # nonManifoldVertices
    setName = 'Error_nonManifoldVertices'
    errorSetConfig(setName)

    # laminaFaces
    setName = 'Error_laminaFaces'
    errorSetConfig(setName)

# 创建error set
def errorSetConfig(setName):
    if mc.objExists(setName):
        mc.sets(cl=setName)
    else:
        mc.createNode('objectSet', n=setName)
        mc.sets(setName, e=1, addElement=errorSet)

#--------------------------------------------------------#
# 动画检测工具
#--------------------------------------------------------#
def checkShotDetails( backMode=1, returnMode=0 , printErrorMode = 1 ,preCheck = 0,printMode = 0,anMode = 1):
    import os
    # 开始处理
    from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
    reload(sk_infoConfig)
    from idmt.maya.py_common import GDC_proxyTools
    reload(GDC_proxyTools)

    from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
    reload(sk_sceneTools)
    from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
    reload(sk_referenceConfig)
    from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
    reload(sk_animFileCheck)
    shotInfo = checkShotInfo()
    # 另存本地
    if not preCheck:
        localTempPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(
            server=0, infoMode=6, shotInfos=shotInfo)
        if not os.path.exists(localTempPath):
            mc.sysFile(localTempPath, makeDir=1)
        mc.file(rename=(localTempPath + mc.file(exn=1, q=1).split('/')[-1]))
        mc.file(s=1, f=1)

    # 转参考
    from idmt.maya.commonPerform.projectTools import sk_projTools_base
    reload(sk_projTools_base)
    sk_projTools_base.sk_projTools_base().refReplacePerform(saveMode = 0)

    errorInfoList = []

    if printMode:print('-------------001')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1,shotMode=anMode)
    sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
    sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

    print(u'=====================Wrong Namespace Clean Done=====================')

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

    if printMode:print('-------------002')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    errorList = sk_animFileCheck.sk_animFileCheck().shotCameraCheck()
    if not errorList:
        shotInfo = checkShotInfo()
        shotType = sk_infoConfig.sk_infoConfig().checkShotType()
        camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
        if shotType == 3:
            camSourceName += '_' + str(shotInfo[3])
        errorInfoList += ['[Error CamName]cam should be %s'%camSourceName]

    print(u'=====================Cam Name Check Done=====================')

    sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate=backMode)

    print(u'=====================Camera Config Done=====================')

    # 检测ref
    if anMode:
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(
            'an', 1, returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

    # 检测非server参考
    errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(
        returnMode=returnMode)
    if errorList:
        errorInfoList = errorInfoList + errorList

    # 参考加载检测
    errorList = sk_animFileCheck.sk_animFileCheck().shotReferenceLoadCheck()
    if errorList:
        errorInfoList = errorInfoList + errorList

    if printMode:print('-------------003')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================Reference List Check Done=====================')

    # 清理层和渲染层
    if anMode:
        sk_animFileCheck.sk_animFileCheck().shotDisplayLayerCheck(returnMode=returnMode,deleteMode =1 )

    sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

    if printMode:print('-------------005')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================DisplayLayer & RenderLayer Check Done=====================')

    # 必须先检测
    #if anMode:
    #    errorList = sk_animFileCheck.sk_animFileCheck().shotNoRefNodesCheck()
    #    if errorList[0]:
    #        errorInfoList = errorInfoList + errorList[0]

    if printMode:print('-------------006')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    #print(u'=====================Not Ref Check Done=====================')

    errorList = sk_animFileCheck.sk_animFileCheck().shotAssetShaderCheck(returnMode = returnMode)
    if errorList:
        errorInfoList = errorInfoList + errorList

    errorList = sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(
        assetMode = 0 ,returnMode = returnMode)
    if errorList:
        errorInfoList = errorInfoList + errorList

    if printMode:print('-------------007')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================File Nodes Check Done=====================')

    if errorInfoList and printErrorMode:
        errorInfo = u'\n--------请处理好这些错误--------'
        print(errorInfo)
        for errorLine in errorInfoList:
            print(errorLine)
        errorInfo = u'--------请处理好这些错误--------\n'
        print(errorInfo)
        mc.error()

    if printMode:print('-------------008')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    if preCheck or (not anMode):
        return

    #-------------------------#
    #以下是处理阶段

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

    if printMode:print('-------------009')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================参考修正完毕=====================')

    sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()

    if printMode:print('-------------010')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    # print(u'=====================Ref Namespace Info Fix Done=====================')

    print(mc.ls(type='unknown'))
    unknownNodes = mc.ls(type='unknown')
    if unknownNodes:
        for node in unknownNodes:
            if mc.ls(node):
                mc.lockNode(node, l=0)
                mc.delete(node)
    print(mc.ls(type='unknown'))

    if printMode:print('-------------011')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================No Need Nodes Clean Done=====================')

    if printMode:print('-------------012')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================Camera Update Done=====================')

    # 处理组
    sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

    if printMode:print('-------------013')
    if printMode:print(mc.editDisplayLayerMembers('norender',q=1))

    print(u'=====================OutLiner ReGroup Done=====================')

    mc.file(s=1, f=1)

    return errorInfoList

# 临时用：参考路径处理
def bkReferencePathConfig():
    from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
    reload(sk_referenceConfig)
    refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
    refNodes = refInfos[0][0]
    refPaths = refInfos[1][0]
    for i in range(len(refPaths)):
        refPath = refPaths[i]
        refNode = refNodes[i]
        oldKey = u'//192.168.1.100/项目/Y盘/'
        newKey = u'Y:/'
        newPath = refPath.replace(oldKey, newKey)
        try:
            mc.file(newPath, loadReference=refNode)
        except:
            pass
    fileInfo = mc.file(exn=1, q=1)
    fileName = fileInfo.split('/')[-1]
    filePath = fileInfo[:-1*(len(fileName))]
    newFilePath = filePath + 'done/'
    mc.sysFile(newFilePath, makeDir=1)
    mc.file(rename=(newFilePath + fileName))
    mc.file(s=1, f=1)

# --------------------------#
# 工具架检测
# --------------------------#
def animCheckTools( selectIndex=1):
    # 窗口
    widthValue = 235
    if mc.window("sk_animationCheckTools", ex=1):
        mc.deleteUI("sk_animationCheckTools", window=True)
    mc.window("sk_animationCheckTools", title="Animation Check Tools", widthHeight=(
        widthValue, 235), menuBar=0)

    # 主界面
    mc.columnLayout()

    # 模型类
    mc.rowLayout()
    mc.button(w=widthValue, h=30, bgc=[
              0, 0, 0.0], label=(unicode('===动画检测工具===', 'utf8')))
    mc.setParent("..")

    # FPS检测
    mc.rowLayout()
    mc.button(w=widthValue, h=30, bgc=[
              0, 0.1, 0.45], label=u'FPS检测 | FPS Check', c='from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneImportFrame(\'FPS\',checkMode = 1)')
    mc.setParent("..")

    # frame检测
    mc.rowLayout()
    mc.button(
        w=widthValue, h=30, bgc=[0, 0.1, 0.45], label=u'帧范围检测 | Frame Range Check',
        c='from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneImportFrame(\'frame\',checkMode = 1)')
    mc.setParent("..")

    # Asset List检测
    mc.rowLayout()
    mc.button(
        w=widthValue, h=30, bgc=[0, 0.1, 0.45], label=u'[An]Asset List检测 | Asset List Check',
        c='from commonCore.core_mayaCommon import sk_animFileCheck\nreload(sk_animFileCheck)\nsk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(\'an\',1)')
    mc.setParent("..")

    # camera Update检测
    mc.rowLayout()
    mc.button(
        w=widthValue, h=30, bgc=[0, 0.1, 0.45], label=u'Camera 上传检测  | Camera Update Check',
        c='from commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate()')
    mc.setParent("..")

    # Asset Texture检测
    mc.rowLayout()
    mc.button(
        w=widthValue, h=30, bgc=[0, 0.1, 0.45], label=u'Asset Texture检测  | Asset Texture Check',
        c='from commonCore.core_mayaCommon import sk_animFileCheck\nreload(sk_animFileCheck)\nsk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(assetMode = 0)')
    mc.setParent("..")

    # Server Asset检测
    mc.rowLayout()
    mc.button(
        w=widthValue, h=30, bgc=[0, 0.1, 0.45], label=u'Server Asset检测  | Server Asset Check',
        c='from commonCore.core_mayaCommon import sk_animFileCheck\nreload(sk_animFileCheck)\nsk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef()')
    mc.setParent("..")

    '''
    # l and h
    mc.rowLayout()
    mc.button(w = widthValue , h = 30 ,bgc = [0,0.1,0.45],label = u'h模替换l模检测 | h and l model Check',c = 'from commonCore.core_mayaCommon import sk_animFileCheck\nreload(sk_animFileCheck)\nsk_animFileCheck.sk_animFileCheck().checklmState()')
    mc.setParent("..")

    # 显示层检测
    mc.rowLayout()
    mc.button(w = widt-.-hValue , h = 30 ,bgc = [0,0.1,0.45],label = u'显示层检测  | Display Layer Check 'c = 'from commonCore.core_mayaCommon import sk_animFileCheck\nreload(sk_animFileCheck)\nsk_animFileCheck.sk_animFileCheck().checkDisplayLayers(norenderConfig = 0,donotKeys = [\'norender\',\'nodisplay\'])')
    mc.setParent("..")
    '''

    mc.setParent("..")

    mc.setParent("..")
    mc.showWindow("sk_animationCheckTools")

