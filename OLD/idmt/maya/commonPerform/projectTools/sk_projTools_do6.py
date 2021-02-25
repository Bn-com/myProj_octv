# -*- coding: utf-8 -*-
# 【通用】【do6项目工具】
#  Author : 沈康
#  Data   : 2017
import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_projTools_do6(object):
    def __init__(self):
        self.errorSet = 'ErrorTemp_Set'

    '''
            【UI篇】【前期】【check工具集】
    '''
    # 前期check工具集
    def sk_sceneUICheckTools(self):
        # 窗口
        uiName = 'sk_checkUIMain'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title="Check Tools", widthHeight=(400, 450), menuBar=0)
        # 主界面
        mc.columnLayout()
        
        # 模块
        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        
        # 选取栏
        mc.rowLayout(numberOfColumns=2, columnWidth2=(255, 100))
        mc.textField('sk_sceneUICheckName', w=250 , h=30 , en=1 , text=(unicode('输入整行然后按【提取选择】按钮', 'utf8')))
        mc.button(w=100 , h=30 , bgc=[0, 0.5, 0.8], label=(unicode('【提取选择】', 'utf8')) , c='reload(sk_checkTools);sk_checkTools.sk_checkTools().sk_sceneDetailsSelectObject()')
        mc.setParent("..")
        
        # 行按钮
        mc.rowLayout(numberOfColumns=2, columnWidth2=(100, 250))
        # 全自动
        mc.button(w=100 , h=350 , bgc=[0.1, 0.1, 0.1], label=(unicode('【全自动】【Check】', 'utf8')), c='from idmt.maya.commonPerform.projectTools import sk_projTools_do6;reload(sk_projTools_do6);sk_projTools_do6.sk_projTools_do6().checkDetailsWarning(UIShow= 1)')
        mc.columnLayout()
        # 分割按钮
        # 第1排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【参考】          ', 'utf8')), c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"refCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动更新标记Set>>', 'utf8')),c = 'reload(sk_checkTools);sk_checkTools.sk_checkTools().checkCacheSetAdd()')
        mc.setParent("..")
        # 第2排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【namespace】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"nsCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<namespace工具>>', 'utf8')),c = 'mel.eval(\"common_namespaceTools\")')
        mc.setParent("..")
        # 第3排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【命名】          ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"MSHCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<添加_后缀>>', 'utf8')),c ='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkRenameMSHPosfix()')
        mc.setParent("..")
        # 第4排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【面数】          ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"faceCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动处理重命名>>', 'utf8')),c ='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkSameRename()\nsk_checkCommon.sk_checkTools().checkSameRename(\"mesh\")\nsk_checkCommon.sk_checkTools().checkSameRename(\"nurbsCurve\")\nsk_checkCommon.sk_checkTools().checkMSHKeepOneRename(\"MSH\")')
        mc.setParent("..")
        # 第5排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【instance】    ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"insCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<displaceLayer清理>>', 'utf8')),c = 'reload(sk_checkTools);sk_checkTools.sk_checkTools().checkCleanDisplayLayers()')
        mc.setParent("..")
        # 第6排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【smooth】     ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"smoothCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<renderLayer清理>>', 'utf8')), c = 'reload(sk_checkTools);sk_checkTools.sk_checkTools().checkCleanRenderLayers()')
        mc.setParent("..")        
        # 第7排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【标记】         ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"signCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动清理空组>>', 'utf8')),c = 'mel.eval(\"deleteEmptyGroups()\")')
        mc.setParent("..")
        # 第8排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【物体重名】  ', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameTransformCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<显示|隐藏骨骼>>', 'utf8')),c = 'reload(sk_checkTools);sk_checkTools.sk_checkTools().checkJointViewHide()')
        mc.setParent("..")      
        
        # 第9排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【shape重名】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameShapeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.1, 0.1, 0.1], label=(unicode('<<添加|ABC属性>>', 'utf8')), c ='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="alembic")')
        mc.setParent("..")        
        
        # 第10排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【Mesh同名】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"sameShapeNodeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【proxy位移】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning(\"proxyInfo\")')
        mc.setParent("..")   
        
        # 第11排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【smoothSet】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning("smoothSet")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【renderState】', 'utf8')),c='reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning("renderState")')
        mc.setParent("..")     
        mc.setParent("..")
        mc.setParent("..")

        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'【Check】【模型命名】'),c='execfile(r\'//file-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/edo_modelNameCheckinList.py\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'【Check】【顶点检查】'),c='mel.eval("source kcCheckVertex.mel;kcCheckVertex()")')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'【Check】【重合物体检查】'),c='mel.eval("source zjCheckDup.mel;zjCheckDup()")')
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<清除点位移信息>>'),c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/wxIIOptimize4PreClearLocal4Vtx.mel";wxIIOptimize4PreClearLocal4Vtx()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<选择transfer节点>>'),c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreTransfer()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<选择灰色shape节点>>'),c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreSpilthShape()\')')
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<勾上所有大于2k的贴图Use BOT选项>>'),c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreUseBot()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<重新命名材质相关节点>>'),c='from idmt.maya.ShunLiu_common import csl_RenameMatNode\nreload(csl_RenameMatNode)\ncsl_RenameMatNode.csl_RenameMatNode().csl_RenameMatNode(nodeName=[])')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<非法层检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_LayerCheck()')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<非法模型检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_geocheck()')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<模型freez检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_nofrezzeCheck()')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<文件结构检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().yd_checkGeo()')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<面赋材质检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_faceAssignments()')
        #mc.setParent('..')
        # mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<非法模型检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_geocheck()')
        # mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=(u'<<模型freez检测>>'),c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_nofrezzeCheck()')

        mc.setParent("..")
        mc.setParent("..")
        # 行按钮
        # mc.rowLayout()
        # 单独导入音轨
        # mc.button(w = 150 , h = 30 ,bgc = [0,0.7,0.2],label = (unicode('【动画】只导入音频', 'utf8')) , c = 'sk_sceneConfig.sk_sceneConfig().sk_sceneImportAudio()' )
        # mc.setParent("..")
        
        
        mc.setParent("..")
        mc.showWindow(uiName)
        
    # 提取选择物体
    def sk_sceneDetailsSelectObject(self):
        pathInfo = mc.textField('sk_sceneUICheckName', q=1, text=1)
        objPath = pathInfo.split('\t')[-1]
        mc.select(objPath)

    #--------------------------------------------------------#
    # 前期检测工具
    #--------------------------------------------------------#
    def checkDetailsWarning(self, checkType = '',UIShow = 0,printMode = 1,errorMode = 0):
        infoWrong = []
        errorPrint = 0

        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)

        import time
        startTime = time.strftime("%Y-%m-%d %H:%M:%S")

        # 文件名检测，判断环节
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        # 代理模式检测
        highMode = shotInfo[2]
        if highMode in ['l']:
            return
        
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
        self.checkErrorSetCreate()

        setState = 0
        if shotInfo[1][0] in sk_infoConfig.sk_infoConfig().setKeys:
            setState = 1

        stepSimp = shotInfo[3]
        if '.' in stepSimp:
            stepSimp = stepSimp.split('.')[0]

        # 点线面豁免
        errorEdgeIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'errorEdgeIgnore')
        errorFaceIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'errorFaceShaderIgnore')
        error4EdgesIgnoreState = sk_checkTools.sk_checkTools().checkErrorIgnoreState(shotInfo[0],shotInfo[1], 'error4EdgesIgnore')

        # 点线面server豁免
        projFullName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        dataCmd = "SELECT isnull(A.vefcheck,'0') as vefcheckNew FROM idmtPlex_%s.dbo.[TB_Asset] A WHERE A.asset_name ='%s'"%(projFullName,shotInfo[1])
        vefCheckIgnoreState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)
        errorEdgeIgnoreState = vefCheckIgnoreState
        errorFaceIgnoreState = vefCheckIgnoreState
        error4EdgesIgnoreState = vefCheckIgnoreState
        dataCmd = u"SELECT case when isnull(edite1,\'否\')=\'否\' then \'0\' else \'1\' end as txSize from idmtPlex_%s.dbo.View_SsomAssetModel VSAM where VSAM.asset_name=\'%s\'"%(projFullName,shotInfo[1])
        txSizeState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)

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
                errorPrint += 1

            # 检测文件名
            fileName = mc.file(exn=1,q=1).split('/')[-1]
            lenNum = len(fileName.split('.'))
            if lenNum != 2:
                infoWrong.append(u'【错误存在】\t\t%s' % ('文件名错误!请仔细看命名规范!'))
                errorPrint += 1

            # 检测MODEL组重系列
            model = mc.ls('MODEL',l=1)
            if not model:
                infoWrong.append(u'【 错 误 】\t\tMODEL组不存在!!')
                errorPrint += 1
            else:
                # MODEL组唯一
                if len(model) > 1 and not setState:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不止一个!')
                    errorPrint += 1
                else:
                    # MODEL组必须第二层级
                    if len(model[0].split('|')) !=3:
                        infoWrong.append(u'【 错 误 】\t\tMODEL组不在第二层级!')
                        errorPrint += 1
            # 检测大组数目
            rootGrps = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()
            if rootGrps:
                # 根目录大组数目。特殊项目特殊情况
                if len(rootGrps) != 1:
                    infoWrong.append(u'【 错 误 】\t\t大组不止一个!%s\t'%(rootGrps))
                    errorPrint += 1
            else:
                infoWrong.append(u'【 错 误 】\t\t文件是空的!!')
                errorPrint += 1
            #rootGrpCheck = sk_checkTools.sk_checkTools().checkRootGrpName()
            #if rootGrpCheck:
            #    infoWrong.append(u'【 错 误 】\t\tAsset大组名字错误！角色应为CHR，道具应为PRO，场景应为SET')
            #    errorPrint += 1
            #print '\n'

            if printMode:print '-----c_001'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 忽略l模型的检测
            if highMode in ['l'] and stepSimp not in ['tx']:
                if errorPrint == 0:
                    mc.delete(self.errorSet)
                # 输出错误消息
                print UIShow
                print(u'=============================【文件中错误如下】=============================')
                for info in infoWrong:
                    print info
                print(u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
                mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrint)

                # 解锁
                sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
                sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo(0)
                return errorPrint

            if printMode:print '-----c_002'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 检测空Mesh错误
            if checkType == '' or checkType == 'meshError':
                errorNames = sk_checkTools.sk_checkTools().checkMeshError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【空白Mesh】\t\t%s' % (str(name)))
                        errorPrint += 1
            print '\n'

            if printMode:print '-----c_003'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
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
            print '\n'

            if printMode:print '-----c_004'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测namespace，对于rg和set允许有参考  | 不同项目不同处理
            if checkType == '' or checkType == 'nsCheck':
                # 对set类和rg特殊处理
                if not setState and stepSimp not in ['rg']:
                    errorNs = sk_checkTools.sk_checkTools().checkNamespace(setState)
                    if errorNs:
                        for ns in errorNs:
                            infoWrong.append(u'【 错 误 】\t\t%s'%ns)
                            errorPrint += 1
            print '\n'

            if printMode:print '-----c_005'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 非polygon检测，只允许polygon建模
            if checkType == '' or checkType == 'polyCheck':
                errorSet = 'Error_polyError'
                if not setState:
                    errorNames = sk_checkTools.sk_checkTools().checkNotPoly()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【非poly】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_006'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # transform异常数值检测
            if checkType == '' or checkType in ['nanCheck']:
                errorSet = 'Error_nanValues'
                errorNames = sk_checkTools.sk_checkTools().checkAttrNaNValue()
                # do6暂时不更新检测,下个项目开始应用
                errorNames = []
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【NaN数值】\t\t%s' % (str(name)))
                        errorPrint += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            #-----------------------------#
            # model环节检测
            #-----------------------------#
            # 检测intermediate object
            if checkType == '' or checkType == 'imoCheck':
                errorSet = 'Error_imoError'
                if not setState and stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkIntermediateObjectError()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【临时shape】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_006a'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 非法模型检测
            if checkType == '' or checkType == 'nonManifoldVertices':
                errorSet = 'Error_nonManifoldVertices'
                if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldVertices')
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【未缝合点】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_006b'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            if checkType == '' or checkType == 'nonManifoldEdges':
                errorSet = 'Error_nonManifoldEdges'
                if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldEdges')
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【未缝合边】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_006c'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            if checkType == '' or checkType == 'laminaFaces':
                errorSet = 'Error_laminaFaces'
                if not errorEdgeIgnoreState and stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkErrorObjects('laminaFaces')
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【未缝合面】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_007'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # texture环节检测
            #-----------------------------#
            # 选面物体检测
            if checkType == '' or checkType == 'faceShader':
                errorSet = 'Error_faceShader'
                if not errorFaceIgnoreState:
                    if not setState and stepSimp in ['tx']:
                        errorNames = sk_checkTools.sk_checkTools().checkFaceShaderDetails()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【选面物体】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement=errorSet)
                        else:
                            mc.delete(errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_007a'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 尺寸超标
            if checkType == '' or checkType == 'Error_txFileSize':
                errorSet = 'Error_txFileSize'
                if not txSizeState and stepSimp in ['tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkTextureFileSize(returnMode = 1,sizeMax = 8)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【尺寸超标】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_007b'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 透明贴图检测
            if checkType == '' or checkType == 'transprancyNodes':
                errorSet = 'Error_transprancyNodes'
                if stepSimp in ['tx']:
                    #from idmt.maya.py_common import GDC_TransInfoProce
                    #reload(GDC_TransInfoProce)
                    #errorNames = GDC_TransInfoProce.GDC_TransInfoProce().gdc_TrShadeInfo(returnMode = 1)
                    errorNames = []
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【透明贴图】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            # 贴图路径检测
            if checkType == '' or checkType == 'txFilePath':
                errorSet = 'Error_txFilePath'
                if stepSimp in ['tx','rg']:
                    errorNames = sk_checkTools.sk_checkTools().checkFileTexture()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【贴图路径】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_007c'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # rigging环节检测
            #-----------------------------#
            # 检测MODEL层级
            if checkType == '' or checkType == 'modelRg':
                # 对rg检测
                errorSet = 'Error_modelRG'
                if stepSimp in ['rg']:
                    errorNames = sk_checkTools.sk_checkTools().checkRGModel()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【MODEL层级】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            if printMode:print '-----c_009'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 通用环节检测
            #-----------------------------#
            # 渲染属性检测
            if checkType == '' or checkType == 'renderState':
                errorSet = 'Error_RenderState'
                errorNames = sk_checkTools.sk_checkTools().checkMeshRenderStates()
                if errorNames:
                    if errorNames == ['No Model']:
                        infoWrong.append(u'【MODEL】\t\t%s' % (str(errorNames)))
                        errorPrint += 1
                    else:
                        for name in errorNames:
                            infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_010'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 多边面错误
            if checkType == '' or checkType == 'faceCheck':
                error4Set = 'Error_N4Edges'
                error3Set = 'Error_N3Edges'
                if not error4EdgesIgnoreState:
                    errorNames = [[],[]]
                    if not setState:
                        errorNames = sk_checkTools.sk_checkTools().checkFaceVertexs(smoothSkip = 0,triangleNum = 1)
                    check4Name = errorNames[0]
                    print errorNames
                    if check4Name:
                        for name in check4Name:
                            if '.f[' in name:
                                infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                            else:
                                infoWrong.append(u'【蒙皮错误】\t\t%s' % (str(name)))
                            errorPrint += 1
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
            print '\n'

            if printMode:print '-----c_011'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # instance检测
            # 对场景不检测
            if checkType == '' or checkType == 'insCheck':
                errorSet = 'Error_Instance'
                if not setState:
                    errorNames = sk_checkTools.sk_checkTools().checkInstance()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【instance】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_012'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                errorSet = 'Error_SmoothLost'
                if stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkModelSmoothSet(shotInfo[0])
                    if errorNames:
                        if errorNames == [u'未发现正版SMOOTH_SET']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                            errorPrint += 1
                        if errorNames == [u'未发现有效SMOOTH物体']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                            errorPrint += 1
                        if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                            for name in errorNames:
                                infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            print '\n'

            if printMode:print '-----c_013'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测重名错误
            if checkType == ''  or checkType == 'sameTransformCheck':
                errorSet = 'Error_SameNameNode'
                errorNames = []
                if not setState:
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName(skipGrp = 'MODEL')
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            #if '|MODEL|' in name:
                            errorNames.append(name)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_014'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测重名错误|shape节点检测
            if checkType == '' or checkType == 'sameShapeCheck':
                errorSet = 'Error_SameNameShape'
                errorNames = []
                if not setState:
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName('mesh',skipGrp = 'MODEL')
                    errorNamesTemp = errorNamesTemp + sk_checkTools.sk_checkTools().checkSameName('nurbsCurve',skipGrp = 'MODEL')
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            #if '|MODEL|' in name:
                            errorNames.append(name)
                    passList = []
                    if errorNames and (shotInfo[0] + '_' + shotInfo[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_015'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测mesh同名节点
            if checkType == '' or checkType == 'sameShapeNodeCheck':
                errorSet = 'Error_SameShapeNode'
                if not setState:
                    errorNames = []
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkMeshSameNameNodes()
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
                                errorPrint += 1
                            mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_016'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 归零检测
            if checkType == '' or checkType == 'zeroAttrCheck':
                errorSet = 'Error_zeroAttrCheck'
                if not setState:
                    errorObjs  = sk_checkTools.sk_checkTools().checkZeroMeshAttrs()
                    errorCtrls = []
                    if stepSimp in ['rg']:
                        errorCtrls = sk_checkTools.sk_checkTools().checkZeroCtrlAttrs(checkType = 1)
                    errorNames = errorObjs + errorCtrls
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【没有归零】\t\t%s' % (str(name)))
                            errorPrint += 1
                        if mc.ls(errorCtrls):
                            mc.sets(errorNames , e=1 , addElement=errorSet)
                        else:
                            if mc.ls(errorObjs):
                                mc.sets(errorObjs , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_017'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # polygon父子检测
            if checkType == '' or checkType == 'polyCPoly':
                errorSet = 'Error_polyCPoly'
                if not setState and stepSimp in ['mo','tx']:
                    errorNames = sk_checkTools.sk_checkTools().checkPolyParents()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【父子Polyon】\t\t%s' % (str(name)))
                            errorPrint += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_018'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 无用表达式检测
            if checkType == '' or checkType == 'noneedexp':
                errorSet = 'Error_noneedexp'
                errorNames = sk_checkTools.sk_checkTools().checkNoNeedExpression()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【无用表达式】\t\t%s' % (str(name)))
                        errorPrint += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print '\n'

            if printMode:print '-----c_019'
            if printMode:print time.strftime("%Y-%m-%d %H:%M:%S")
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # tx文件参考检测
            if checkType == '' or checkType == 'txRndRef':
                if stepSimp in ['tx'] :
                    errorNames = sk_checkTools.sk_checkTools().checkTXRefRnd()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【参考错误】\t\t%s' % (str(name)))
                            errorPrint += 1

            # tx文件检测材质赋予
            if checkType == '' or checkType == 'txRLCheck':
                errorSet = 'Error_txRLCk'

                if stepSimp in ['tx'] :
                    errorNames = sk_checkTools.sk_checkTools().checkTextureModelShader(returnMode = 1)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【分层测试】\t\t%s' % (str(name)))
                            errorPrint += 1
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

        else:
            print '\n'
            infoWrong.append(u'【 错 误 】\t\t文件名错误! ')
            errorPrint += 1

        # 删除ErrorSet
        if errorPrint == 0:
            try:
                mc.delete(self.errorSet)
            except:
                pass

        for i in range(len(timeInfos)):
            print '[%s]:\t%s'%(str(i+1),timeInfos[i])

        # 输出DetailsUI
        if UIShow:
            sk_checkTools.sk_checkTools().checkDetailsUI(infoWrong)
            sk_checkTools.sk_checkTools().checkConfigHelpUI()

        # 输出错误消息
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            print info
        errorInfo = (u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
        mc.warning(errorInfo)
        if errorMode and errorPrint:
            print errorInfo
            mc.error()

        print 'start time:%s'%startTime
        print 'end   time:%s'%(time.strftime("%Y-%m-%d %H:%M:%S"))

        # 解锁
        sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
        sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo(0)
        return errorPrint

    #------------------------------#
    # ErrorSet
    def checkErrorSetCreate(self):
        # 文件名检测，判断环节
        if mc.objExists(self.errorSet):
            pass
        else:
            mc.createNode('objectSet', n=self.errorSet)

        # 贴图检测
        setName = 'Error_txFilePath'
        self.errorSetConfig(setName)

        # 尺寸超标
        setName = 'Error_txFileSize'
        self.errorSetConfig(setName)

        # poly检测
        setName = 'Error_polyError'
        self.errorSetConfig(setName)

        # Error_imoError
        setName = 'Error_imoError'
        self.errorSetConfig(setName)

        # 选面物体
        setName = 'Error_faceShader'
        self.errorSetConfig(setName)

        # 三角面过多
        setName = 'Error_N3Edges'
        self.errorSetConfig(setName)

        # 非四边形
        setName = 'Error_N4Edges'
        self.errorSetConfig(setName)

        # instance
        setName = 'Error_Instance'
        self.errorSetConfig(setName)

        # smoothSet
        setName = 'Error_SmoothLost'
        self.errorSetConfig(setName)

        # RenderState
        setName = 'Error_RenderState'
        self.errorSetConfig(setName)

        # SameName Transform
        setName = 'Error_SameNameNode'
        self.errorSetConfig(setName)

        # SameName Shape
        setName = 'Error_SameNameShape'
        self.errorSetConfig(setName)

        # Error_SameShapeNode
        setName = 'Error_SameShapeNode'
        self.errorSetConfig(setName)

        # 归零检测
        setName = 'Error_zeroAttrCheck'
        self.errorSetConfig(setName)

        # MODEL层级
        setName = 'Error_modelRG'
        self.errorSetConfig(setName)

        # polygon父子
        setName = 'Error_polyCPoly'
        self.errorSetConfig(setName)

        # txRLcheck
        setName = 'Error_txRLCk'
        self.errorSetConfig(setName)

        # rg丢材质
        setName = 'Error_rgShader'
        self.errorSetConfig(setName)

        # 无用表达式
        setName = 'Error_noneedexp'
        self.errorSetConfig(setName)

        # 透明贴图检测
        setName = 'Error_transprancyNodes'
        self.errorSetConfig(setName)

        # nonManifoldEdges
        setName = 'Error_nonManifoldEdges'
        self.errorSetConfig(setName)

        # nonManifoldVertices
        setName = 'Error_nonManifoldVertices'
        self.errorSetConfig(setName)

        # laminaFaces
        setName = 'Error_laminaFaces'
        self.errorSetConfig(setName)

        # nanValues
        setName = 'Error_nanValues'
        self.errorSetConfig(setName)

    # 创建error set
    def errorSetConfig(self,setName):
        if mc.objExists(setName):
            mc.sets(cl=setName)
        else:
            mc.createNode('objectSet', n=setName)
            mc.sets(setName, e=1, addElement=self.errorSet)

    #--------------------------------------------------------#
    # 动画检测工具 [anMode] :0 ly,1 an,2 sd
    #--------------------------------------------------------#
    def checkShotDetails(self, backMode=1, returnMode=0 , printErrorMode = 1 ,preCheck = 0,anMode = 1,testMode = 0):
        import os
        # 开始处理.
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
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

        if testMode:self.testDef('001')

        # 转参考
        from idmt.maya.commonPerform.projectTools import sk_projTools_base
        reload(sk_projTools_base)
        sk_projTools_base.sk_projTools_base().refReplacePerform(saveMode = 0)

        if testMode:self.testDef('002')

        # 处理参考,ly可能使用rg参考
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
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
            if tempPath != path:
                mc.file(tempPath, loadReference = refNodes[i])

        if testMode:self.testDef('002')

        errorInfoList = []

        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1,shotMode=anMode)
        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

        if testMode:self.testDef('003')

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

        if testMode:self.testDef('005')

        if anMode in [0,1]:
            checkState = 1
            if shotInfo[0] in sk_infoConfig.sk_infoConfig().camNMFProjList:
                nmfCamList = sk_animFileCheck.sk_animFileCheck().steCamesGetShotCamList()
                if nmfCamList != ['base']:
                    checkState = 0
                print nmfCamList
            if checkState:
                errorList = sk_animFileCheck.sk_animFileCheck().shotCameraCheck()
                if not errorList:
                    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    shotType = sk_infoConfig.sk_infoConfig().checkShotType()
                    camSourceName = 'cam_' + str(shotInfo[1]) + '_' + str(shotInfo[2])
                    if shotType == 3:
                        camSourceName += '_' + str(shotInfo[3])
                    errorInfoList += [u'[Error CamName|相机名错误]cam should be %s'%camSourceName]

        if testMode:self.testDef('006')

        print u'=====================Cam Name Check Done====================='

        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate=backMode)

        if testMode:self.testDef('007')

        print u'=====================Camera Config Done====================='

        # 检测ref
        if anMode in [1]:
            errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(
                'an', 1, returnMode=returnMode)
            if errorList:
                errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('008')

        # 检测非server参考
        errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(
            returnMode=returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('009')

        # 参考加载检测
        errorList = sk_animFileCheck.sk_animFileCheck().shotReferenceLoadCheck()
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('010')

        print u'=====================Reference List Check Done====================='

        # 清理层和渲染层
        if anMode in [0,1]:
            sk_animFileCheck.sk_animFileCheck().shotDisplayLayerCheck(returnMode=returnMode,deleteMode =1 )

        if testMode:self.testDef('011')

        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        if testMode:self.testDef('012')

        print u'=====================DisplayLayer & RenderLayer Check Done====================='

        # 必须先检测
        if anMode in [1]:
            errorList = sk_animFileCheck.sk_animFileCheck().shotNoRefNodesCheck()
            if errorList[0]:
                errorInfoList = errorInfoList + errorList[0]

        if testMode:self.testDef('015')

        # asset 改材质球
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetShaderCheck(returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016')

        # asset 贴图检测
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(
            assetMode = 0 ,returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016a')

        # 场景非法破坏
        errorList = sk_animFileCheck.sk_animFileCheck().shotRefEditCheck(returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016b')

        # transform异常数值检测 do6先不检测,下个项目开启检测
        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        #errorList = sk_checkTools.sk_checkTools().checkAttrNaNValue(mode = 1,returnMode = returnMode)
        errorList = []
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('017')

        print u'=====================File Nodes Check Done====================='

        if errorInfoList and printErrorMode:
            errorInfo = u'\n--------请处理好这些错误--------'
            print errorInfo
            for errorLine in errorInfoList:
                print errorLine
            errorInfo = u'--------请处理好这些错误--------\n'
            print errorInfo
            mc.error()

        if testMode:self.testDef('018')

        if preCheck:
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
            newPath = ''
            if '_c_h_ms_anim.mb' in path:
                newPath = path.replace('_c_h_ms_anim.mb','_h_ms_anim.mb')
            # _ng_参考
            if '_ng_h_ms_anim.mb' in path:
                newPath = path.replace('_ng_h_ms_anim.mb','_h_ms_anim.mb')
            # l->h
            if anMode not in [0] and '_l_ms_' in path:
                newPath = path.replace('_l_ms_','_h_ms_')
            # 替换参考
            if newPath != path:
                mc.file(newPath, loadReference = refNodes[i])

        if testMode:self.testDef('019')

        print u'=====================参考修正完毕====================='
        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        if anMode in [2]:
            # 修正相机namespace
            from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
            reload(sk_renderLayerCore)
            sk_renderLayerCore.sk_renderLayerCore().camRefFix()

        if testMode:self.testDef('020')

        # print u'=====================Ref Namespace Info Fix Done====================='

        print mc.ls(type='unknown')
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')

        if testMode:self.testDef('021')

        print u'=====================No Need Nodes Clean Done====================='

        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)

        norenderL = ['norender','VFX_REF']
        for checkL in norenderL:
            if mc.ls(checkL):
                mc.setAttr(checkL+'.v',0)

        # 多相机信息导出
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout;reload(sk_cacheFinalLayout)
        sk_cacheFinalLayout.sk_cacheFinalLayout().displayLayerInfoExport()

        if testMode:self.testDef('022')

        print u'=====================OutLiner ReGroup Done====================='

        mc.file(s=1, f=1)

        return errorInfoList

    # test
    def testDef(self,num):
        print '-----test_%s'%(str(num))
        print mc.editDisplayLayerMembers('near',q=1)

    #----------------------------------#
    # smallTools
    def sk_projSmallTools(self,showDict = {'mo':0,'rg':0,'an':0,'fx':0,'lr':0}):
        stepKeys = showDict.keys()
        wideValue = 260
        heightValue = 350
        bgcColor = [0,0,0]
        bH = 22.6
        # 窗口
        uiName = 'sk_projSmallTools_do6'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title="Small Tools", widthHeight=(wideValue, heightValue), menuBar=0)
        # 主界面
        mc.scrollLayout( '%s_scrollLayout'%uiName )

        # finalLayout
        for stepKey in stepKeys:
            mc.frameLayout( label=u'===[%s] Tools==='%stepKey, collapse = 1-showDict[stepKey],
                            collapsable = 1,borderStyle='etchedIn',width = wideValue,bgc = bgcColor)
            projBaseKey = 'from idmt.maya.commonPerform.projectTools import sk_projTools_do6;reload(sk_projTools_do6);sk_projTools_do6.sk_projTools_do6()'
            renderBaseKey = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_do6;reload(sk_renderLayer_do6);sk_renderLayer_do6.sk_renderLayer_do6()'
            if stepKey in ['mo']:
                rowNum = 4
                rowHight = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHight)
                # row1
                mc.rowLayout(numberOfColumns = 3,columnWidth2=(130 , 130))
                mc.button(l=u'动态海草选取',w=84,bgc = [0.15,0.55,0.65],h=bH,c = 'reload(sk_projTools_do6);sk_projTools_do6.sk_projTools_do6().animatedPlaneSelect()')
                mc.button(l=u'海草abc导入',w=84,bgc = [0.15,0.65,0.15],h=bH,c = 'from idmt.maya.py_common import GA_Effectalembic;reload(GA_Effectalembic);GA_Effectalembic.GA_Effectalembic().shotSdAbcImport()')
                mc.button(l=u'选删[abc]',w=85,bgc = [0.2,0.2,0.2],h=bH,c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().cleanSelObjAbcCons()')
                mc.setParent( '..' )
                # row2
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'[SD]选[取]物体显示层',w=130,bgc = [0.15,0.55,0.65],h=bH,c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sdSelHideObjs()')
                mc.button(l=u'[SD]选[面]物体Set组',w=130,bgc = [0.15,0.65,0.15],h=bH,c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sdSelHideSets()')
                mc.setParent( '..' )
                #  row3
                baseKey = projBaseKey
                mc.button(l=u'[运行前]<=备份=> SD导入参考删除',w=260,bgc = [0.68,0.22,0.22],c = '%s.runUI(1)'%baseKey)
                # row4
                mc.button(l=u'【多相机工具】激活',w=260,bgc = [0.1,0.1,0.1],c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_mi;reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamUI()')
                #  end
                mc.setParent( '..' )

            if stepKey in ['an']:
                rowNum = 3
                rowHight = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHight)
                baseKey = projBaseKey
                # row1
                mc.button(l=u'=====【ly】动画检测=====',w=260,bgc = [0.15,0.45,0.65],c = '%s.checkShotDetails(anMode = 0,preCheck = 1,returnMode = 1)'%baseKey)
                # row2
                mc.button(l=u'=====【an】动画检测=====',w=260,bgc = [0.15,0.65,0.15],c = '%s.checkShotDetails(anMode = 1,preCheck = 1,returnMode = 1)'%baseKey)
                # row3
                mc.button(l=u'=====【sd】动画检测=====',w=260,bgc = [0.25,0.55,0.35],c = '%s.checkShotDetails(anMode = 2,preCheck = 1,returnMode = 1)'%baseKey)
                #  end
                mc.setParent( '..' )

            if stepKey in ['lr']:
                rowNum = 17
                bH = 22.1
                rowHight = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHight)
                baseKey = renderBaseKey
                suColr = [0.18,0.18,0.18]
                # row1
                fixCmd = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().sk_sceneReorganize();'
                fixCmd += 'sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig();'
                fixCmd += 'from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam;reload(sk_hbExportCam);'
                fixCmd += 'sk_hbExportCam.sk_hbExportCam().camServerReference();print "----------All Done----------"'
                mc.button(l=u'=====[运行后保存]MS镜头文件模拟=====',w=260,bgc = [0.18,0.18,0.18],c = fixCmd)
                # row2
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===选取[开启]matte===',w=130,bgc = [0.15,0.65,0.15],c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().arnoldMatteConfig(1)')
                mc.button(l=u'===选取[关闭]matte===',w=130,bgc = [0.15,0.15,0.35],c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().arnoldMatteConfig(0)')
                mc.setParent( '..' )
                # row3:selSms
                mc.rowLayout(numberOfColumns = 3,columnWidth2=(130 , 130))
                smsKey = 'from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet;reload(sk_smoothSet);sk_smoothSet.sk_smoothSet()'
                mc.button(l=u'<=选sms[0]=>',w=83,bgc = [0.15,0.65,0.15],c = '%s.doSmoothSelObjs(smsLev= 0,disModify =0)'%smsKey)
                mc.button(l=u'<=选sms[1]=>',w=84,bgc = [0.15,0.45,0.65],c = '%s.doSmoothSelObjs(smsLev= 1,disModify =0)'%smsKey)
                mc.button(l=u'<=选sms[2]=>',w=83,bgc = [0.15,0.55,0.85],c = '%s.doSmoothSelObjs(smsLev= 2,disModify =0)'%smsKey)
                mc.setParent( '..' )
                # row3.5
                mc.button(l=u'>>>--[sky]加载相机并配置--<<<',w=130,bgc = [0.05,0.05,0.05],c = '%s.skyFix()'%baseKey)
                # row4:masterLayer素模
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'[SurfaceShader素模]',w=130,bgc = [0.12,0.12,0.12],c = 'from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType="surfaceShader")')
                mc.button(l=u'[aiStandard素模]',w=130,bgc = [0.12,0.12,0.12],c = 'from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType="ar")')
                mc.setParent( '..' )
                # row5
                mc.button(l=u'======【全自动分层】======',w=130,bgc = [0.12,0.65,0.12],c = '%s.do6AutoCreateRenderLayers()'%baseKey)
                # row6
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===CHRCLR===',w=130,bgc = [0.15,0.45,0.65],c = '%s.rlCHR(printMode = 1)'%baseKey)
                mc.button(l=u'===BGCLR===',w=130,bgc = [0.15,0.45,0.65],c = '%s.rlBG(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row7
                mc.button(l=u'(下面的层创建后不得使用CHRCLR|BGCLR分层)',w=130,bgc = [0.12,0.12,0.12])
                # row8
                mc.button(l=u'===ALLIDP===',w=130,bgc = suColr,c = '%s.rlAllIdp(printMode = 1)'%baseKey)
                # row9
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'===CHRFOG===',w=85,bgc = suColr,c = '%s.rlCHR_FOG(printMode = 1)'%baseKey)
                mc.button(l=u'===CHRENV===',w=85,bgc = suColr,c = '%s.rlCHR_ENV(printMode = 1)'%baseKey)
                mc.button(l=u'===CHRHOLO===',w=85,bgc = suColr,c = '%s.rlCHR_HOLO(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row10
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'===CHRRGB===',w=85,bgc = suColr,c = '%s.rlCHR_RGB(printMode = 1)'%baseKey)
                mc.button(l=u'===CHRSHD===',w=85,bgc = suColr,c = '%s.rlCHR_SHD(printMode = 1)'%baseKey)
                mc.button(l=u'===CHRCAU===',w=85,bgc = suColr,c = '%s.rlCHR_CAU(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row11
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'===BGRGB===',w=85,bgc = suColr,c = '%s.rlBG_RGB(printMode = 1)'%baseKey)
                mc.button(l=u'===BGFOG===',w=85,bgc = suColr,c = '%s.rlBG_FOG(printMode = 1)'%baseKey)
                mc.button(l=u'===BGCAU===',w=85,bgc = suColr,c = '%s.rlBG_CAU(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row12
                mc.button(l=u'===BGVFX===',w=130,bgc = suColr,c = '%s.rlBG_VFX(printMode = 1)'%baseKey)
                # row13
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130,130))
                mc.button(l=u'===SKY(跳过已有)===',w=130,bgc = suColr,c='%s.rlSkyEnv()'%baseKey)
                mc.button(l=u'===SKY(全部制作)===',w=130,bgc = suColr,c='%s.rlSkyEnv(forceBuild = 1)'%baseKey)
                mc.setParent( '..' )
                # row14
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===[chr_Light]更新===',w=130,bgc = [0.35,0.25,0.65],c = '%s.lgtImport("chr",1)'%baseKey)
                mc.button(l=u'===[set_Light]更新===',w=130,bgc = [0.35,0.25,0.65],c = '%s.lgtImport("bg",1)'%baseKey)
                mc.setParent( '..' )
                # row15
                mc.button(l=u'===【使用帮助】===',w=130,bgc = [0.25,0.65,0.25],c='%s.openHelp()'%projBaseKey)
                # row16
                mc.button(l=u'===lightDataUpdate===',w=130,bgc = [0.05,0.05,0.05],c='from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore().lgtUpdateUI()')
                # end
                mc.setParent( '..' )

            mc.setParent( '..' )

        mc.setParent("..")
        mc.showWindow(uiName)

    def openHelp(self):
        filePath = 'Z:/Projects/DiveollyDive6/Project/data/lighting/do6_help.txt'.replace('/','\\')
        runCmd = 'notePad.exe \"%s\"'%filePath
        import threading
        threadNew = threading.Thread(target = self.missionRunCmd,args = (runCmd,''))
        threadNew.setDaemon(True)
        threadNew.start()

    def missionRunCmd(self,cmd,temp = ''):
        import subprocess
        subprocess.check_output(cmd)

    def runUI(self,checkMode = 1):
        if checkMode in [1]:
            showInfo = u'做此操作前务必备份文件;此操作用于观察该清理的结果是否正确;'
            showInfo +=u'\n本操作是不可逆的,先执行要删除的物体参考导入(maya不可逆)'
            showInfo +=u'\n再删除sd环节的显示层和set组里的物体。上传请用之前备份文件'
            runCmd = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sdDelConfig()'
            result = mc.confirmDialog(title = 'CheckConfirm',message = showInfo,button=[u'执行',u'返回'],defaultButton = runCmd)
            if result in [u'执行']:
                from idmt.maya.commonPerform.projectTools import sk_projTools_base
                reload(sk_projTools_base)
                sk_projTools_base.sk_projTools_base().sdDelConfig()

    #------------------------------------------------------------#
    #------------------------------------------------------------#

    # animated plant
    def animatedPlaneSelect(self):
        import os
        mc.select(cl=1)
        assetList = []
        checkRoot = 'Z:/Projects/DiveollyDive6/Project/data/alembic/ef'
        for root,dirs,files in os.walk(checkRoot):
            checkFolder = root.split('\\')[-1]
            if not checkFolder:
                continue
            if checkFolder[0] not in ['p','P']:
                continue
            assetList.append(checkFolder)
        if not assetList:
            return
        ctrlGrps = []
        print '---------AssetList'
        print assetList
        for checkNs in assetList:
            checkGrps = mc.ls('*:*%s_*_ctrl*'%checkNs,type = 'transform',l=1)
            checkGrps += mc.ls('%s_*_ctrl*'%checkNs,type = 'transform',l=1)
            if not checkGrps:
                continue
            for checkGrp in checkGrps:
                curvShape = mc.listRelatives(checkGrp,s=1,ni=1,type = 'nurbsCurve',f=1)
                if not curvShape:
                    continue
                ctrlGrps += [checkGrp]
        if ctrlGrps:
            mc.select(ctrlGrps)


    # do5特殊处理
    def refImportFix(self):
        refNodes = mc.ls(type = 'reference')
        for checkRef in refNodes:
            if '_c505004' in checkRef:
                continue
            if '_p531001' in checkRef:
                continue
            try:
                mc.file(rfn=checkRef , removeReference=1)
            except:
                pass
        mc.file(s=1,f=1)