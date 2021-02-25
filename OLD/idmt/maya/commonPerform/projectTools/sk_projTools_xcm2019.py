# -*- coding: utf-8 -*-
# 【通用】【xcm2019项目工具】
#  Author : 沈康
#  Data   : 2018
import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_projTools_xcm2019(object):
    def __init__(self):
        self.errorSet = 'ErrorTemp_Set'
        self.oldAttr = '.hqOld'
        self.insideKeyList = ['.f[','.vtx[','.v[']

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
        mc.button(w=100 , h=350 , bgc=[0.1, 0.1, 0.1], label=(unicode('【全自动】【Check】', 'utf8')), c='from idmt.maya.commonPerform.projectTools import sk_projTools_xcm2019;reload(sk_projTools_xcm2019);sk_projTools_xcm2019.sk_projTools_xcm2019().checkDetailsWarning(UIShow= 1)')
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
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'【Check】【模型命名】',c='execfile(r\'//file-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/edo_modelNameCheckinList.py\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'【Check】【顶点检查】',c='mel.eval("source kcCheckVertex.mel;kcCheckVertex()")')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'【Check】【重合物体检查】',c='mel.eval("source zjCheckDup.mel;zjCheckDup()")')
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<清除点位移信息>>',c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/wxIIOptimize4PreClearLocal4Vtx.mel";wxIIOptimize4PreClearLocal4Vtx()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<选择transfer节点>>',c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreTransfer()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<选择灰色shape节点>>',c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreSpilthShape()\')')
        mc.setParent("..")
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<勾上所有大于2k的贴图Use BOT选项>>',c='mel.eval(\'source "Z:/Resource/Support/Maya/projects/ShunLiu/csl_ModeOptimize.mel";wxIIOptimize4PreUseBot()\')')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<重新命名材质相关节点>>',c='from idmt.maya.ShunLiu_common import csl_RenameMatNode\nreload(csl_RenameMatNode)\ncsl_RenameMatNode.csl_RenameMatNode().csl_RenameMatNode(nodeName=[])')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<非法层检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_LayerCheck()')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<非法模型检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_geocheck()')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<模型freez检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_nofrezzeCheck()')
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<文件结构检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().yd_checkGeo()')
        mc.setParent('..')
        mc.rowLayout(numberOfColumns=3, columnWidth2=(125, 125))
        mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<面赋材质检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().GDC_faceAssignments()')
        #mc.setParent('..')
        # mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<非法模型检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_geocheck()')
        # mc.button(w=134,h=30,bgc=[0.13, 0.15, 0.1],label=u'<<模型freez检测>>',c='from idmt.maya.py_common import GDC_checkin\nreload(GDC_checkin)\nGDC_checkin.GDC_checkin().gdc_nofrezzeCheck()')

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
    # 获取文件dict
    def getFileDict(self,shotInfos = []):
        if not shotInfos:
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if 'seq' in shotInfos[2].lower()[:3]:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetShotDict()
        else:
            fileDict = sk_infoConfig.sk_infoConfig().checkGetAssetDict()
        return fileDict

    #--------------------------------------------------------#
    # 前期检测工具
    #--------------------------------------------------------#
    def checkDetailsWarning(self, checkType = '',UIShow = 0,printMode = 1,errorMode = 0):
        infoWrong = []
        errorPrintNum = 0

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
        fileDitc = sk_infoConfig.sk_infoConfig().checkGetAssetDict()

        # 代理模式检测
        highMode = fileDitc['highMode']
        if highMode in ['L']:
            print(u'------------Error:此项目没有L文件')
            mc.error()
        projStyle  = 2

        skipKeyList = ['_PA126','_PA129','_qingtai_']
        skipState = 0
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        for skipKey in skipKeyList:
            if skipKey in fileName:
                skipState = 1
        if skipState:
            return

        # 渲染集中营
        renderGrp = sk_infoConfig.sk_infoConfig().checkProjMODELGrp(projStyle = projStyle)

        # 创建ErrorSet
        self.checkErrorSetCreate()

        setState = 0
        if shotInfo[2] in ['BG']:
            setState = 1

        stepSimp = fileDitc['stepSimp']

        # 点线面server豁免
        projFullName = fileDitc['projFull']
        dataCmd = "SELECT isnull(A.vefcheck,'0') as vefcheckNew FROM idmtPlex_%s.dbo.[TB_Asset] A WHERE A.asset_name ='%s'"%(projFullName,shotInfo[3])
        vefCheckIgnoreState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)
        # vefCheckIgnoreState = 0
        errorEdgeIgnoreState = vefCheckIgnoreState
        errorFaceIgnoreState = vefCheckIgnoreState
        error4EdgesIgnoreState = vefCheckIgnoreState
        #dataCmd = u"SELECT case when isnull(edite1,\'否\')=\'否\' then \'0\' else \'1\' end as txSize from idmtPlex_%s.dbo.View_SsomAssetModel VSAM where VSAM.asset_name=\'%s\'"%(projFullName,shotInfo[1])
        #txSizeState = sk_infoConfig.sk_infoConfig().checkReadServerData(cmd_name = dataCmd,returnAll= 0)

        timeInfos = []
        import time
        if len(shotInfo) > 3:
            #----------------------------------#
            # 错误检测，根据阶段不同而不同
            # 检测是否有非法MODEL组
            for i in range(0, 9):
                grps = mc.ls(renderGrp + str(i) + '*')
                if not grps:
                    continue
                infoWrong.append(u'【错误存在】\t\t%s' %grps)
                errorPrintNum += 1

            # 检测文件名
            fileName = mc.file(exn=1,q=1).split('/')[-1]
            lenNum = len(fileName.split('.'))
            if lenNum != 2:
                infoWrong.append(u'【错误存在】\t\t%s' %'文件名错误!请仔细看命名规范!')
                errorPrintNum += 1

            # 检测MODEL组重系列
            model = mc.ls(renderGrp,l=1)
            if not model:
                infoWrong.append(u'【 错 误 】\t\t%s组不存在!!'%renderGrp)
                errorPrintNum += 1
            else:
                # MODEL组唯一
                if len(model) > 1 and not setState:
                    infoWrong.append(u'【 错 误 】\t\t%s组不止一个!'%renderGrp)
                    errorPrintNum += 1
                else:
                    # MODEL组必须第二层级
                    levNum = 3
                    if fileDitc['category'] in ['character']:
                        levNum = 5
                    if len(model[0].split('|')) != levNum:
                        infoWrong.append(u'【 错 误 】\t\t%s组不在正确层级!'%renderGrp)
                        errorPrintNum += 1

            if fileDitc['category'] in ['character'] and mc.ls(renderGrp,l=1):
                if '|MODEL|' not in mc.ls(renderGrp,l=1)[0]:
                    infoWrong.append(u'【 错 误 】\t\t高模组不在MODEL组!')
                    errorPrintNum += 1

            # 检测大组数目
            rootGrps = sk_sceneTools.sk_sceneTools().checkOutlinerGroup()
            if rootGrps:
                # 根目录大组数目。特殊项目特殊情况
                if len(rootGrps) != 1:
                    infoWrong.append(u'【 错 误 】\t\t大组不止一个!%s\t'%rootGrps)
                    errorPrintNum += 1
            else:
                infoWrong.append(u'【 错 误 】\t\t文件是空的!!')
                errorPrintNum += 1

            # needModify
            rootDict = {'character':'CHR','prop':'PRO','background':'BG','proxy':'PX'}
            rootGrpCheck = sk_checkTools.sk_checkTools().checkRootGrpName(rightRootGrp = rootDict[fileDitc['category']])
            if rootGrpCheck:
                infoWrong.append(u'【 错 误 】\t\tAsset大组名字错误！角色应为CHR，道具应为PRO，场景应为SET')
                errorPrintNum += 1
            print('\n')

            if printMode:print('-----c_001')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 忽略l模型的检测
            if highMode in ['L'] and stepSimp not in ['tex']:
                if errorPrintNum == 0:
                    mc.delete(self.errorSet)
                # 输出错误消息
                print(UIShow)
                print(u'=============================【文件中错误如下】=============================')
                for info in infoWrong:
                    print(info)
                print(u'===========================【目前】共计【%s】处错误===========================' %errorPrintNum)
                mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrintNum)

                # 解锁
                sk_sceneTools.sk_sceneTools().checkUnlockMSHV(renderGrp = renderGrp)
                sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo(0,renderGrp = renderGrp)
                return errorPrintNum

            if printMode:print('-----c_002')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 检测空Mesh错误
            if checkType == '' or checkType == 'meshError':
                errorNames = sk_checkTools.sk_checkTools().checkMeshError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【空白Mesh】\t\t%s' % (str(name)))
                        errorPrintNum += 1
            print('\n')

            if printMode:print('-----c_003')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            #-----------------------------#
            # 预先检测
            #-----------------------------#
            # 参考检测，对于rg和set允许有参考 | 不同项目不同处理
            if checkType == '' or checkType == 'refCheck':
                # 对set类不检测
                if not setState and stepSimp not in ['rig']:
                    # 获取参考数
                    rfnNods = mc.file(q=1, reference=1)
                    # 有参考时
                    if rfnNods:
                        infoWrong.append(u'【 警告 】\t\t有参考存在，请注意核查!!')
            print('\n')

            if printMode:print('-----c_004')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测namespace， 不同项目不同处理
            if checkType == '' or checkType == 'nsCheck':
                errorNs = sk_checkTools.sk_checkTools().checkNamespace(setState)
                if errorNs:
                    for ns in errorNs:
                        infoWrong.append(u'【 错 误 】\t\t%s'%ns)
                        errorPrintNum += 1
            print('\n')

            if printMode:print('-----c_005')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 非polygon检测，只允许polygon建模
            if checkType == '' or checkType == 'polyCheck':
                errorSet = 'Error_polyError'
                if not setState:
                    errorNames = sk_checkTools.sk_checkTools().checkNotPoly(renderGrp = renderGrp)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【非poly】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            if printMode:print('-----c_006')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # transform异常数值检测
            if checkType == '' or checkType in ['nanCheck']:
                errorSet = 'Error_nanValues'
                errorNames = sk_checkTools.sk_checkTools().checkAttrNaNValue(renderGrp = renderGrp)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【NaN数值】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            #-----------------------------#
            # model环节检测
            #-----------------------------#
            # 检测intermediate object
            if checkType == '' or checkType == 'imoCheck':
                errorSet = 'Error_imoError'
                tempSkipState = 0
                if '_CA011001tzs' in fileName:
                    tempSkipState = 1
                if not setState and stepSimp in ['mo','tex'] and not tempSkipState:
                    errorNames = sk_checkTools.sk_checkTools().checkIntermediateObjectError(renderGrp = renderGrp)
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
                if not errorEdgeIgnoreState and stepSimp in ['mo','tex']:
                    tempNames = sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldVertices',renderGrp = renderGrp)
                    errorNames = []
                    for name in tempNames:
                        checkName = self.checkGetTransformNode(name)
                        if mc.ls(checkName + self.oldAttr):
                            continue
                        infoWrong.append(u'【未缝合点】\t\t%s' % (str(name)))
                        errorNames.append(name)
                        errorPrintNum += 1
                    if errorNames:
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
                if not errorEdgeIgnoreState and stepSimp in ['mo','tex']:
                    tempNames = sk_checkTools.sk_checkTools().checkErrorObjects('nonManifoldEdges',renderGrp = renderGrp)
                    errorNames = []
                    for name in tempNames:
                        checkName = ''
                        for checkKey in  self.insideKeyList:
                            if checkKey in name:
                                checkName = name.split(checkKey)[0]
                        if mc.ls(checkName + self.oldAttr):
                            continue
                        infoWrong.append(u'【未缝合边】\t\t%s' % (str(name)))
                        errorNames.append(name)
                        errorPrintNum += 1
                    if errorNames:
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
                if not errorEdgeIgnoreState and stepSimp in ['mo','tex']:
                    tempNames = sk_checkTools.sk_checkTools().checkErrorObjects('laminaFaces',renderGrp = renderGrp)
                    errorNames = []
                    for name in tempNames:
                        checkName = self.checkGetTransformNode(name)
                        if mc.ls(checkName + self.oldAttr):
                            continue
                        infoWrong.append(u'【未缝合面】\t\t%s' % (str(name)))
                        errorNames.append(name)
                        errorPrintNum += 1
                    if errorNames:
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
                    if not setState and stepSimp in ['tex','rig']:
                        tempNames = sk_checkTools.sk_checkTools().checkFaceShaderDetails(renderGrp = renderGrp)
                        errorNames = []
                        for name in tempNames:
                            checkName = self.checkGetTransformNode(name)
                            if mc.ls(checkName + self.oldAttr):
                                continue
                            infoWrong.append(u'【选面物体】\t\t%s' % (str(name)))
                            errorNames.append(name)
                            errorPrintNum += 1
                        if errorNames:
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

            # 透明贴图检测
            if checkType == '' or checkType == 'transprancyNodes':
                errorSet = 'Error_transprancyNodes'
                if stepSimp in ['tex']:
                    #from idmt.maya.py_common import GDC_TransInfoProce
                    #reload(GDC_TransInfoProce)
                    #errorNames = GDC_TransInfoProce.GDC_TransInfoProce().gdc_TrShadeInfo(returnMode = 1)
                    errorNames = []
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【透明贴图】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            # 贴图路径检测
            if checkType == '' or checkType == 'txFilePath':
                errorSet = 'Error_txFilePath'
                if stepSimp in ['tex','rig']:
                    errorNames = self.checkFileTexture(assetID = fileDitc['assetID']
                                        ,assetTypeFolder = fileDitc['assetType'],seqFolder = fileDitc['sequence'])
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【贴图路径】\t\t%s' % (str(name)))
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
                if stepSimp in ['rig']:
                    errorNames = sk_checkTools.sk_checkTools().checkRGModel()
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

            #-----------------------------#
            # 通用环节检测
            #-----------------------------#
            # 渲染属性检测
            if checkType == '' or checkType == 'renderState':
                errorSet = 'Error_RenderState'
                errorNames = sk_checkTools.sk_checkTools().checkMeshRenderStates(renderGrp = renderGrp)
                print(errorNames)
                if errorNames:
                    if errorNames == ['No %s'%renderGrp]:
                        infoWrong.append(u'【MODEL】\t\t%s' % (str(errorNames)))
                        errorPrintNum += 1
                    else:
                        for name in errorNames:
                            infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

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
                        errorNames = sk_checkTools.sk_checkTools().checkFaceVertexs(renderGrp = renderGrp,
                                        smoothSkip = 0,triangleNum = 1)
                    check4Name = errorNames[0]
                    if check4Name:
                        needNames = []
                        for name in check4Name:
                            nodeName = name
                            if '.' in name:
                                nodeName = name.split('.')[0]
                            if mc.nodeType(nodeName) in ['mesh']:
                                nodeName = mc.listRelatives(nodeName,p=1,f=1,type = 'transform')
                            if mc.ls(nodeName + self.oldAttr):
                                continue
                            if '.f[' in name:
                                infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                            else:
                                infoWrong.append(u'【蒙皮错误】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                            needNames.append(name)
                        if needNames:
                            mc.sets(needNames , e=1 , addElement=error4Set)
                        else:
                            mc.delete(error4Set)
                    else:
                        mc.delete(error4Set)
                    check3Name = errorNames[1]
                    if check3Name:
                        needNames = []
                        for name in check3Name:
                            if mc.ls(name + self.oldAttr):
                                continue
                            infoWrong.append(u'【三角面过多】\t\t%s' % (str(name)))
                            needNames.append(name)
                        if needNames:
                            mc.sets(check3Name , e=1 , addElement=error3Set)
                        else:
                            mc.delete(error3Set)
                    else:
                        mc.delete(error3Set)
                else:
                    mc.delete(error3Set)
                    mc.delete(error4Set)
            print('\n')

            if printMode:print('-----c_011')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # instance检测
            # 对场景不检测
            if checkType == '' or checkType == 'insCheck':
                errorSet = 'Error_Instance'
                if not setState:
                    errorNames = sk_checkTools.sk_checkTools().checkInstance(renderGrp = renderGrp)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【instance】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            if printMode:print('-----c_012')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                errorSet = 'Error_SmoothLost'
                if stepSimp in ['mo','rig','tex'] and not setState:
                    errorNames = sk_checkTools.sk_checkTools().checkModelSmoothSet('%s_%s'%(shotInfo[0],shotInfo[1]),projStyle = projStyle)
                    if errorNames:
                        if errorNames == [u'未发现正版SMOOTH_SET']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                            errorPrintNum += 1
                        if errorNames == [u'未发现有效SMOOTH物体']:
                            infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                            errorPrintNum += 1
                        if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                            for name in errorNames:
                                infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                                errorPrintNum += 1
                            mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

            print('\n')

            if printMode:print('-----c_013')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测重名错误
            if checkType == ''  or checkType == 'sameTransformCheck':
                errorSet = 'Error_SameNameNode'
                errorNames = []
                if not setState:
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName(justCheck = renderGrp)
                    if errorNamesTemp:
                        for name in errorNamesTemp:
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
            print('\n')

            if printMode:print('-----c_014')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测重名错误|shape节点检测
            if checkType == '' or checkType == 'sameShapeCheck':
                errorSet = 'Error_SameNameShape'
                errorNames = []
                if not setState:
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName('mesh',justCheck = renderGrp)
                    errorNamesTemp = errorNamesTemp + sk_checkTools.sk_checkTools().checkSameName('nurbsCurve',justCheck = renderGrp)
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            errorNames.append(name)
                    passList = []
                    if errorNames and (shotInfo[0] + '_' + shotInfo[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            if printMode:print('-----c_015')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 检测mesh同名节点
            if checkType == '' or checkType == 'sameShapeNodeCheck':
                errorSet = 'Error_SameShapeNode'
                if not setState:
                    errorNames = []
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkMeshSameNameNodes()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
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
            print('\n')

            if printMode:print('-----c_016')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 归零检测 needModify
            if checkType == '' or checkType == 'zeroAttrCheck':
                errorSet = 'Error_zeroAttrCheck'
                if not setState:
                    errorObjs  = sk_checkTools.sk_checkTools().checkZeroMeshAttrs(renderGrp = renderGrp)
                    errorCtrls = []
                    if stepSimp in ['rig']:
                        errorCtrls = sk_checkTools.sk_checkTools().checkZeroCtrlAttrs(checkType = 1,ctrlSetList = ['All_BodySet'])
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
            print('\n')

            if printMode:print('-----c_017')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # polygon父子检测
            if checkType == '' or checkType == 'polyCPoly':
                errorSet = 'Error_polyCPoly'
                tempSkipState = 0
                if '_CA011001tzs' in fileName:
                    tempSkipState = 1
                if not setState and stepSimp in ['mo','tex'] and not tempSkipState:
                    errorNames = sk_checkTools.sk_checkTools().checkPolyParents(renderGrp = renderGrp)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【父子Polyon】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                        mc.sets(errorNames , e=1 , addElement=errorSet)
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            if printMode:print('-----c_018')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # 无用表达式检测
            if checkType == '' or checkType == 'noneedexp':
                errorSet = 'Error_noneedexp'
                errorNames = sk_checkTools.sk_checkTools().checkNoNeedExpression()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【无用表达式】\t\t%s' % (str(name)))
                        errorPrintNum += 1
                    mc.sets(errorNames , e=1 , addElement=errorSet)
                else:
                    mc.delete(errorSet)
            print('\n')

            if printMode:print('-----c_019')
            if printMode:print(time.strftime("%Y-%m-%d %H:%M:%S"))
            timeInfos.append(time.strftime("%Y-%m-%d %H:%M:%S"))

            # tx文件参考检测
            if checkType == '' or checkType == 'txRndRef':
                if stepSimp in ['tex'] :
                    errorNames = sk_checkTools.sk_checkTools().checkTXRefRnd()
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【参考错误】\t\t%s' % (str(name)))
                            errorPrintNum += 1

            # tx文件检测材质赋予
            if checkType == '' or checkType == 'txRLCheck':
                errorSet = 'Error_txRLCk'
                if stepSimp in ['tex'] :
                    errorNames = sk_checkTools.sk_checkTools().checkTextureModelShader(returnMode = 1,renderGrp = renderGrp)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【分层测试】\t\t%s' % (str(name)))
                            errorPrintNum += 1
                    else:
                        mc.delete(errorSet)
                else:
                    mc.delete(errorSet)

        else:
            print('\n')
            infoWrong.append(u'【 错 误 】\t\t文件名错误! ')
            errorPrintNum += 1

        # 删除ErrorSet
        if errorPrintNum == 0:
            try:
                mc.delete(self.errorSet)
            except:
                pass

        for i in range(len(timeInfos)):
            print('[%s]:\t%s'%(str(i+1),timeInfos[i]))

        # 输出DetailsUI
        if UIShow:
            sk_checkTools.sk_checkTools().checkDetailsUI(infoWrong)
            sk_checkTools.sk_checkTools().checkConfigHelpUI()

        # 输出错误消息
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            print(info)
        errorInfo = (u'===========================【目前】共计【%s】处错误===========================' % (errorPrintNum))
        mc.warning(errorInfo)
        if errorMode and errorPrintNum:
            print(errorInfo)
            mc.error()

        print('start time:%s'%startTime)
        print('end   time:%s'%(time.strftime("%Y-%m-%d %H:%M:%S")))

        # 解锁
        sk_sceneTools.sk_sceneTools().checkUnlockMSHV(renderGrp = renderGrp)
        sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo(0,renderGrp = renderGrp)
        return errorPrintNum

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
        # 外包风格
        projStyle = 2
        # 另存本地
        if not preCheck:
            localTempPath = sk_infoConfig.sk_infoConfig().checkShotDataInfoPath(
                server=0, infoMode=6, shotInfos=shotInfo,projStyle = projStyle)
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

        errorInfoList = []

        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1,shotMode=anMode)
        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        # 避免非server参考被算进OTC组，检测成功后再分组
        #sk_sceneTools.sk_sceneTools().sk_sceneReorganize(finalLayout = 2,projStyle = projStyle)

        if testMode:self.testDef('003')

        print(u'=====================Wrong Namespace Clean Done=====================')

        # FPS
        errorList = sk_sceneTools.sk_sceneTools().sk_sceneImportFrame(
            'FPS', checkMode=1, returnMode=returnMode ,projStyle = projStyle)

        if errorList:
            errorInfoList = errorInfoList + errorList
        # frame
        if anMode:
            errorList = sk_sceneTools.sk_sceneTools().sk_sceneImportFrame(
                'frame', checkMode=1, returnMode=returnMode ,projStyle = projStyle)
            if errorList:
                errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('005')

        if anMode in [0,1]:
            checkState = 1
            if shotInfo[0] in sk_infoConfig.sk_infoConfig().camNMFProjList:
                nmfCamList = sk_animFileCheck.sk_animFileCheck().steCamesGetShotCamList(projStyle = projStyle)
                if nmfCamList != ['base']:
                    checkState = 0
                print(nmfCamList)
            if checkState:
                errorList = sk_animFileCheck.sk_animFileCheck().shotCameraCheck(projStyle = projStyle)
                if not errorList:
                    shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                    shotType = sk_infoConfig.sk_infoConfig().checkShotType()
                    camSourceName = 'cam_%s_%s'%(shotInfo[1],shotInfo[2])
                    if shotType == 3:
                        camSourceName = 'cam_%s_%s_%s'%(shotInfo[1],shotInfo[2],shotInfo[3])
                    if projStyle in [2]:
                        camSourceName = 'An_%s_%s_StereoCam'%(shotInfo[2],shotInfo[3])
                    errorInfoList += [u'[Error CamName|相机名错误]cam should be %s'%camSourceName]

        if testMode:self.testDef('006')

        print(u'=====================Cam Name Check Done=====================')

        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(batchUpadate=backMode,projStyle = projStyle)

        if testMode:self.testDef('007')

        print(u'=====================Camera Config Done=====================')

        # 检测ref
        if anMode in [1]:
            errorList = sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck(
                'an', 1, returnMode=returnMode,projStyle = projStyle)
            if errorList:
                errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('008')

        # 检测非server参考
        errorList = sk_animFileCheck.sk_animFileCheck().checkNotServerAssetRef(
            returnMode=returnMode,projStyle = projStyle)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('009')

        # 参考加载检测
        errorList = sk_animFileCheck.sk_animFileCheck().shotReferenceLoadCheck()
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('010')

        print(u'=====================Reference List Check Done=====================')

        # 清理层和渲染层
        if anMode in [0,1]:
            sk_animFileCheck.sk_animFileCheck().shotDisplayLayerCheck(returnMode=returnMode,deleteMode =1,projStyle = projStyle )


        if testMode:self.testDef('011')

        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()

        if testMode:self.testDef('012')

        print(u'=====================DisplayLayer & RenderLayer Check Done=====================')

        # 必须先检测
        if anMode in [1]:
            errorList = sk_animFileCheck.sk_animFileCheck().shotNoRefNodesCheck(norenderL = ['noRender'])
            if errorList[0]:
                errorInfoList = errorInfoList + errorList[0]

        if testMode:self.testDef('015')

        # asset 改材质球
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetShaderCheck(
            returnMode = returnMode,norenderL = ['NoRender'])
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016')

        # asset 贴图检测
        errorList = sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck(
            assetMode = 0 ,returnMode = returnMode,projStyle = projStyle)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016a')

        # 场景非法破坏
        errorList = sk_animFileCheck.sk_animFileCheck().shotRefEditCheck(
            returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('016b')

        # transform异常数值检测
        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        errorList = sk_checkTools.sk_checkTools().checkAttrNaNValue(mode = 1,returnMode = returnMode)
        if errorList:
            errorInfoList = errorInfoList + errorList

        if testMode:self.testDef('017')

        print(u'=====================File Nodes Check Done=====================')

        if errorInfoList and printErrorMode:
            errorInfo = u'\n--------请处理好这些错误--------'
            print(errorInfo)
            for errorLine in errorInfoList:
                print(errorLine)
            errorInfo = u'--------请处理好这些错误--------\n'
            print(errorInfo)
            mc.error()

        if testMode:self.testDef('018')

        if preCheck:
            return

        #-------------------------#)
        #以下是处理阶段

        if testMode:self.testDef('019')

        print(u'=====================参考修正完毕=====================')
        if anMode in [0,1]:
            sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig(projStyle = projStyle)
        if anMode in [2]:
            # 修正相机namespace
            from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore
            reload(sk_renderLayerCore)
            sk_renderLayerCore.sk_renderLayerCore().camRefFix()

        if testMode:self.testDef('020')

        # print(u'=====================Ref Namespace Info Fix Done=====================')

        print(mc.ls(type='unknown'))
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print(mc.ls(type='unknown'))

        if testMode:self.testDef('021')

        print(u'=====================No Need Nodes Clean Done=====================')

        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(finalLayout = 2,projStyle = projStyle)

        norenderL = ['norender','noRender','VFX_REF']
        for checkL in norenderL:
            if mc.ls(checkL):
                mc.setAttr(checkL+'.v',0)

        # 多相机信息导出
        from idmt.maya.commonCore.core_finalLayout import sk_cacheFinalLayout;reload(sk_cacheFinalLayout)
        sk_cacheFinalLayout.sk_cacheFinalLayout().displayLayerInfoExport(projStyle = projStyle)

        if testMode:self.testDef('022')

        print(u'=====================OutLiner ReGroup Done=====================')

        mc.file(s=1, f=1)

        return errorInfoList

    # test
    def testDef(self,num):
        print('-----test_%s'%(str(num)))
        print(mc.editDisplayLayerMembers('near',q=1))

    #----------------------------------#
    # smallTools
    def sk_projSmallTools(self,showDict = {'mo':0,'rig':0,'an':0,'fx':0,'lr':0}):
        stepKeys = showDict.keys()
        wideValue = 260
        heightValue = 350
        bgcColor = [0,0,0]
        bH = 22.6
        # 窗口
        uiName = 'sk_projSmallTools_xcm2019'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title="Small Tools", widthHeight=(wideValue, heightValue), menuBar=0)
        # 主界面
        mc.scrollLayout( '%s_scrollLayout'%uiName )

        # finalLayout
        for stepKey in stepKeys:
            mc.frameLayout( label=u'===[%s] Tools==='%stepKey, collapse = 1-showDict[stepKey],
                            collapsable = 1,borderStyle='etchedIn',width = wideValue,bgc = bgcColor)
            projBaseKey = 'from idmt.maya.commonPerform.projectTools import sk_projTools_xcm2019;reload(sk_projTools_xcm2019);sk_projTools_xcm2019.sk_projTools_xcm2019()'
            renderBaseKey = 'from idmt.maya.commonPerform.renderLayers import sk_renderLayer_xcm2019;reload(sk_renderLayer_xcm2019);sk_renderLayer_xcm2019.sk_renderLayer_xcm2019()'
            if stepKey in ['mo']:
                rowNum = 5
                rowHigh = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHigh)
                # row1
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'[Ass] 选切polyware',w=130,bgc = [0.15,0.15,0.15],h=bH,c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().assModeSwitch(selMode = 0 ,switchMode = 2)')
                mc.button(l=u'[Ass] 选切bbox模式',w=130,bgc = [0.15,0.15,0.15],h=bH,c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().assModeSwitch(selMode = 0 ,switchMode = 1)')
                mc.setParent( '..' )
                # row2
                mc.rowLayout(numberOfColumns = 3,columnWidth2=(130 , 130))
                mc.button(l=u'选物体加[OldAttr]',w=260,bgc = [0.1,0.1,0.1],c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_xcm2019;reload(sk_projTools_xcm2019);sk_projTools_xcm2019.sk_projTools_xcm2019().addOldSkipAttr()')
                mc.setParent( '..' )
                # row3
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'[SD]选[取]物体显示层',w=130,bgc = [0.15,0.55,0.65],h=bH,c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sdSelHideObjs()')
                mc.button(l=u'[SD]选[面]物体Set组',w=130,bgc = [0.15,0.65,0.15],h=bH,c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_base;reload(sk_projTools_base);sk_projTools_base.sk_projTools_base().sdSelHideSets()')
                mc.setParent( '..' )
                #  row4
                baseKey = projBaseKey
                mc.button(l=u'[运行前]<=备份=> SD导入参考删除',w=260,bgc = [0.68,0.22,0.22],c = '%s.runUI(1)'%baseKey)
                # row5
                mc.button(l=u'【多相机工具】激活',w=260,bgc = [0.1,0.1,0.1],c = 'from idmt.maya.commonPerform.projectTools import sk_projTools_mi;reload(sk_projTools_mi);sk_projTools_mi.sk_projTools_mi().ste3CamUI()')
                #  end
                mc.setParent( '..' )

            if stepKey in ['an']:
                rowNum = 4
                rowHigh = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHigh)
                baseKey = projBaseKey
                # row1
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===动作库===',w=130,bgc = [0.12,0.12,0.12],c = '%s.cmdSwitch(mode = 1)'%baseKey)
                mc.button(l=u'===表情库===',w=130,bgc = [0.12,0.12,0.12],c = '%s.cmdSwitch(mode = 2)'%baseKey)
                mc.setParent( '..' )
                # row2
                mc.button(l=u'=====【ly】动画检测=====',w=260,bgc = [0.15,0.45,0.65],c = '%s.checkShotDetails(anMode = 0,preCheck = 1,returnMode = 1)'%baseKey)
                # row3
                mc.button(l=u'=====【an】动画检测=====',w=260,bgc = [0.15,0.65,0.15],c = '%s.checkShotDetails(anMode = 1,preCheck = 1,returnMode = 1)'%baseKey)
                # row4
                mc.button(l=u'=====【sd】动画检测=====',w=260,bgc = [0.25,0.55,0.35],c = '%s.checkShotDetails(anMode = 2,preCheck = 1,returnMode = 1)'%baseKey)
                #  end
                mc.setParent( '..' )

            if stepKey in ['lr']:
                rowNum = 17
                bH = 22.1
                rowHigh = bH*rowNum + 2*(rowNum-1)
                mc.rowColumnLayout(numberOfRows=rowNum,height = rowHigh)
                baseKey = renderBaseKey
                suColr = [0.18,0.18,0.18]
                # row1
                fixCmd = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools;reload(sk_sceneTools);sk_sceneTools.sk_sceneTools().sk_sceneReorganize();'
                fixCmd += 'sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig();'
                fixCmd += 'from idmt.maya.commonCore.core_mayaCommon import sk_hbExportCam;reload(sk_hbExportCam);'
                fixCmd += 'sk_hbExportCam.sk_hbExportCam().camServerReference();print("----------All Done----------")'
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
                mc.button(l=u'>>>Coming Soon...<<<',w=130,bgc = [0.05,0.05,0.05],c = 'print("Coming Soon...")')
                # row4:masterLayer素模
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'[SurfaceShader素模]',w=130,bgc = [0.12,0.12,0.12],c = 'from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType="surfaceShader")')
                mc.button(l=u'[aiStandard素模]',w=130,bgc = [0.12,0.12,0.12],c = 'from idmt.maya.commonCore.core_renderLayer import sk_renderLayerCore;reload(sk_renderLayerCore);sk_renderLayerCore.sk_renderLayerCore().masterLayerLambertShader(shaderType="ar")')
                mc.setParent( '..' )
                # row5
                mc.button(l=u'======【全自动分层】======',w=130,bgc = [0.12,0.65,0.12],c = '%s.xcm2019AutoCreateRenderLayers()'%baseKey)
                # row6
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===CHRCLR===',w=130,bgc = [0.15,0.45,0.65],c = '%s.rlCHR_CO(printMode = 1)'%baseKey)
                mc.button(l=u'===BGCLR===',w=130,bgc = [0.15,0.45,0.65],c = '%s.rlBG_CO(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row7
                mc.button(l=u'(下面的层创建后不得使用CHRCLR|BGCLR分层)',w=130,bgc = [0.12,0.12,0.12])
                # row8
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'===BGfzc===',w=130,bgc = [0.15,0.35,0.65],c = '%s.rlBG_fzc(printMode = 1)'%baseKey)
                mc.button(l=u'===ALLIdp===',w=130,bgc = [0.15,0.35,0.65],c = '%s.rlAll_Idp(printMode = 1)'%baseKey)
                mc.setParent( '..' )
                # row9
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.setParent( '..' )
                # row10
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.setParent( '..' )
                # row11
                mc.button(l=u'Coming Soon...',w=130,bgc = suColr,c = 'print("Coming Soon...")')
                # row12
                mc.rowLayout(numberOfColumns = 3,columnWidth3=(85,85,85))
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=85,bgc = suColr,c = 'print("Coming Soon...")')
                mc.setParent( '..' )
                # row13
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130,130))
                mc.button(l=u'...',w=130,bgc = suColr,c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=130,bgc = suColr,c = 'print("Coming Soon...")')
                mc.setParent( '..' )
                # row14
                mc.rowLayout(numberOfColumns = 2,columnWidth2=(130 , 130))
                mc.button(l=u'...',w=130,bgc = [0.35,0.25,0.65],c = 'print("Coming Soon...")')
                mc.button(l=u'...',w=130,bgc = [0.35,0.25,0.65],c = 'print("Coming Soon...")')
                mc.setParent( '..' )
                # row15
                mc.button(l=u'===【使用帮助】===',w=130,bgc = [0.25,0.65,0.25],c = 'print("Coming Soon...")')
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

    def cmdSwitch(self,mode = 0):
        if mode in [1]:
            import maya.mel as mel
            mel.eval('source "slAnimPoseLibrary.mel"; slAnimPoseLibrary("XCM_2019")')
        if mode in [2]:
            faceToolPath = u'Y:/XCM_2019DY/XCM_2019DY_交换空间/Animation/表情库/PoseMAN_10_XXGL_fixed.mel'
            import maya.mel as mel
            mel.eval('source "%s"'%faceToolPath)

    #------------------------------------------------------------#
    # 配套小工具
    #------------------------------------------------------------#
    # 华强旧asset屏蔽检测
    def addOldSkipAttr(self):
        objs = mc.ls(sl=1,l=1)
        needObjs = []
        for checkObj in objs:
            insideKey = ''
            insideState = 0
            for checkKey in self.insideKeyList:
                if checkKey in checkObj:
                    insideState = 1
                    insideKey = checkKey
            if insideState:
                needObjs.append(checkObj.split(insideKey)[0])
            else:
                needObjs.append(checkObj)
        tempObjs = []
        for checkObj in needObjs:
            checkType = mc.nodeType(checkObj)
            if checkType in ['transform']:
                tempObjs.append(checkObj)
            else:
                tempObjs.append(mc.listRelatives(checkObj,p=1,f=1)[0])
        needObjs = tempObjs
        if needObjs:
            needObjs = list(set(needObjs))
        attrName = self.oldAttr.split('.')[-1]
        for checkObj in needObjs:
            objAttr = checkObj + self.oldAttr
            if mc.ls(objAttr):
                continue
            mc.addAttr(checkObj,sn=attrName,longName=attrName,nn=attrName,attributeType='double')
            mc.setAttr(objAttr,e=1,keyable = 1)

    #-------------------------#
    # asset贴图路径检测
    def checkFileTexture(self,assetID,assetTypeFolder,seqFolder):
        import os
        errorObjs = []
        # 获取贴图信息
        txDict = {'file':'.fileTextureName','aiImage':'.filename','aiStandIn':'.dso','gpuCache':'.cacheFileName'}
        #rootPath = 'Y:/XCM_2019DY/Asset/%s/%s/%s'%(seqFolder,assetTypeFolder,assetID)
        #sourceImageFolder = '%s/sourceimages'%rootPath
        seqKeyList = ['.###.','.####.']
        for fileType in txDict.keys():
            checkNodes = mc.ls(type = fileType)
            keyAttr = txDict[fileType]
            for fileNode in checkNodes:
                inr = mc.referenceQuery(fileNode,inr=1)
                if inr:
                    continue
                imagePath = mc.getAttr(fileNode + keyAttr,x=1)
                if '<udim>' in imagePath:
                    errorObjs.append(fileNode)
                    continue
                seqState = 0
                for checkKey in seqKeyList:
                    if checkKey in imagePath:
                        seqState = 1
                if not os.path.exists(imagePath) and not seqState:
                    errorObjs.append(fileNode)
                    continue
        yetiNodes = mc.ls(type = 'pgYetiMaya')
        for yetiNode in yetiNodes:
            txNodes = mc.pgYetiGraph(yetiNode,listNodes= 1, type = 'texture')
            if not txNodes:
                continue
            for checkTxNode in txNodes:
                txFile = mc.pgYetiGraph(yetiNode,node = checkTxNode,param= 'file_name', getParamValue = 1)
                seqState = 0
                for checkKey in seqKeyList:
                    if checkKey in txFile:
                        seqState = 1
                if not os.path.exists(txFile) and not seqState and '<udim>' not in txFile.lower():
                    errorObjs.append(yetiNode)
        return errorObjs

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
        print('---------AssetList')
        print(assetList)
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

    #------------------------------#
    # 获取指定物体的transform节点
    def checkGetTransformNode(self,checkNode):
        needInfo = ''
        if '.' in checkNode:
            checkType = mc.nodeType(checkNode.split('.')[0])
        else:
            checkType = mc.nodeType(checkNode)
        if checkType in ['transform']:
            needInfo = checkNode.split('.')[0]
        else:
            tempGrp = mc.listRelatives(checkNode,p=1,f=1)
            while tempGrp and mc.nodeType(tempGrp) not in ['transform']:
                tempGrp = mc.listRelatives(tempGrp,p=1,f=1)
            if tempGrp:
                needInfo = tempGrp[0]
        return needInfo

    #-------------------------------#
    # 参考转向 fixed
    def updateNewAssetByReference(self,saveMode = 0):
        assetDict = self.getAssetDict()
        print(assetDict)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        needState = 0
        errorAssetList = []
        for idNum in range(len(refPaths)):
            checkPath  = refPaths[idNum]
            newPath = checkPath
            modifyState = 0
            for checkKey in assetDict.keys():
                if '/%s/'%checkKey not in checkPath:
                    continue
                if checkKey.lower() not in newPath.lower():
                    continue
                if assetDict[checkKey][0].lower() in checkPath.lower():
                    continue
                modifyState = 1
                if ('/%s/'%assetDict[checkKey][0]).lower() in checkPath.lower():
                    modifyState = 0
                if modifyState:
                    for addKey in ['_','/']:
                        oldAssetKey = '%s%s%s'%(addKey,checkKey,addKey)
                        oldAssetKey = oldAssetKey.lower()
                        newAssetKey = '%s%s%s'%(addKey,assetDict[checkKey][0],addKey)
                        if oldAssetKey != newAssetKey.lower() and oldAssetKey in newPath.lower():
                            newPath = newPath.lower().replace(oldAssetKey,newAssetKey)
                        oldSeqKey = '%s%s%s'%(addKey,assetDict[checkKey][1],addKey)
                        oldSeqKey = oldSeqKey.lower()
                        newSeqKey = '%s%s%s'%(addKey,assetDict[checkKey][2],addKey)
                        if oldSeqKey != newSeqKey.lower() and oldSeqKey in newPath.lower():
                            newPath = newPath.lower().replace(oldSeqKey,newSeqKey)
            if modifyState:
                newPath = newPath.replace('y:/','Y:/')
                newPath = newPath.replace('xcm_2019dy','XCM_2019DY')
                newPath = newPath.replace('_ch_','_CH_')
                newPath = newPath.replace('_pro_','_PRO_')
                newPath = newPath.replace('_bg_','_BG_')
                newPath = newPath.replace('_h_','_H_')
                newPath = newPath.replace('/asset/','/Asset/')
                newPath = newPath.replace('/seq002a/','/seq002A/')
                newPath = newPath.replace('_seq002a_','_seq002A_')
            if not modifyState:
                continue
            print('----------ModifyRef')
            print(checkPath)
            print(newPath)
            print(modifyState)
            if checkPath == newPath and modifyState:
                errorAssetList.append(checkPath)
                errorAssetList.append(newPath)
            if checkPath != newPath:
                needState = 1
                mc.file(newPath, loadReference = refNodes[idNum])
        if errorAssetList:
            print('\n\n\n----------Replace Error:[Failed]')
            for num in range(len(errorAssetList)/2):
                print('----------')
                print(errorAssetList[num])
                print(errorAssetList[num+1])
            print('---------Please Check Asset ID and Old Reference Info\n\n\n')
            mc.error()
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig(projStyle = 2)
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
            print('--------outputPath')
            print(outputPath)
            return

    #-------------------------------#
    # 文本替换新旧参考
    def updateNewAssetByTxt(self,rootPath):
        import os
        checkPath = rootPath.replace('/','\\')
        dataGet = os.popen('DIR /d /b %s /s'%checkPath)
        getInfo = dataGet.read()
        allInfos = getInfo.split('\n')
        assetDict = self.getAssetDict()
        for info in allInfos:
            if not info:
                continue
            filePath = info.replace('\\','/')
            readInfo = sk_infoConfig.sk_infoConfig().checkFileRead(filePath)
            newInfos = []
            for num in range(len(readInfo)):
                lineInfo = readInfo[num]
                if 'file -r' in lineInfo or '-typ "mayaBinary"' in lineInfo:
                    for checkKey in assetDict.keys():
                        for addKey in ['_','/']:
                            oldAssetKey = '%s%s%s'%(addKey,checkKey,addKey)
                            newAssetKey = '%s%s%s'%(addKey,assetDict[checkKey],addKey)
                            lineInfo = lineInfo.replace(oldAssetKey,newAssetKey)
                newInfos.append(lineInfo)
            if readInfo != newInfos:
                sk_infoConfig.sk_infoConfig().checkFileWrite(path = filePath,info = newInfos,lineKey='')

    #-------------------------------#
    # refRetarget
    def getAssetDict(self):
        import xlrd
        idDict = {}
        xlsFile = 'Y:/XCM_2019DY/Reference/Preproduction_Reference/XCM2019DY_seq002A_Asset_List.xls'
        fileData = xlrd.open_workbook(xlsFile)
        sheetData = fileData.sheets()[0]
        oldIdList = sheetData.col_values(0)
        newIdList = sheetData.col_values(2)
        oldSeqList = sheetData.col_values(3)
        newSeqList = sheetData.col_values(4)
        for num in range(len(oldIdList)):
            if num in [0]:
                continue
            idDict[oldIdList[num]] = [newIdList[num],oldSeqList[num],newSeqList[num]]
        return idDict
