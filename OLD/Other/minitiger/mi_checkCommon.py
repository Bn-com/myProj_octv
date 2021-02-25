# -*- coding: utf-8 -*-

# import sys
# sys.path.append('D:\\food\pyp\common')


# Q:an标记是_an_还是_ca_
# A:_ct_an

# 关于proxy代理物体
# 原则就是，有高低模的，在材质没有做好的时候拼场景的，满足这两者任意一个条件的，必须做proxy.
# 其他的在场景里，你可以import，而不要用specialRef模式
# 缺少一个脚本，在设置上传之前自动将proxy层级关系设置正确

import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_checkTools(object):
    def __init__(self):
        # namespace清理
        pass
        
        
    '''
            【UI篇】【前期】【check工具集】
    '''
    # 前期check工具集
    def sk_sceneUICheckTools(self):
        # 窗口
        if mc.window ("sk_sceneUICheckTools", ex=1):
            mc.deleteUI("sk_sceneUICheckTools", window=True)
        mc.window("sk_sceneUICheckTools", title="Check Tools", widthHeight=(400, 450), menuBar=0)
        # 主界面
        mc.columnLayout()
        
        # 模块
        # from idmt.maya.py_common import sk_checkCommon
        # import sk_checkCommon
        # reload(sk_checkCommon)
        
        # 选取栏
        mc.rowLayout(numberOfColumns=2, columnWidth2=(255, 100))
        mc.textField('sk_sceneUICheckName', w=250 , h=30 , en=1 , text=(unicode('输入整行然后按【提取选择】按钮', 'utf8')))
        mc.button(w=100 , h=30 , bgc=[0, 0.5, 0.8], label=(unicode('【提取选择】', 'utf8')) , c='mi_checkCommon.sk_checkTools().sk_sceneDetailsSelectObject()')
        mc.setParent("..")
        
        # 行按钮
        mc.rowLayout(numberOfColumns=2, columnWidth2=(100, 250))
        # 全自动
        mc.button(w=100 , h=350 , bgc=[0.1, 0.1, 0.1], label=(unicode('【全自动】【Check】', 'utf8')), c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning()')
        mc.columnLayout()
        # 分割按钮
        # 第1排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【参考】          ', 'utf8')), c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"refCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动更新标记Set>>', 'utf8')),c = 'mi_checkCommon.sk_checkTools().checkCacheSetAdd()')
        mc.setParent("..")
        # 第2排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【namespace】', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"nsCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<namespace工具>>', 'utf8')),c = 'mel.eval(\"common_namespaceTools\")')
        mc.setParent("..")
        # 第3排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【命名】          ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"MSHCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<添加_后缀>>', 'utf8')),c ='mi_checkCommon.sk_checkTools().checkRenameMSHPosfix()')
        mc.setParent("..")
        # 第4排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【面数】          ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"faceCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动处理重命名>>', 'utf8')),c ='mi_checkCommon.sk_checkTools().checkSameRename()\nsk_checkCommon.sk_checkTools().checkSameRename(\"mesh\")\nsk_checkCommon.sk_checkTools().checkSameRename(\"nurbsCurve\")\nsk_checkCommon.sk_checkTools().checkMSHKeepOneRename(\"MSH\")')
        mc.setParent("..")
        # 第5排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【instance】    ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"insCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<displaceLayer清理>>', 'utf8')),c = 'mi_checkCommon.sk_checkTools().checkCleanDisplayLayers()')
        mc.setParent("..")
        # 第6排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【smooth】     ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"smoothCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<renderLayer清理>>', 'utf8')), c = 'mi_checkCommon.sk_checkTools().checkCleanRenderLayers()')
        mc.setParent("..")        
        # 第7排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【标记】         ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"signCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动清理空组>>', 'utf8')),c = 'mel.eval(\"deleteEmptyGroups()\")')
        mc.setParent("..")
        # 第8排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【物体重名】  ', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"sameTransformCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<显示|隐藏骨骼>>', 'utf8')),c = 'mi_checkCommon.sk_checkTools().checkJointViewHide()')
        mc.setParent("..")      
        
        # 第9排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【shape重名】', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"sameShapeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.1, 0.1, 0.1], label=(unicode('<<添加|ABC属性>>', 'utf8')), c ='from idmt.maya.norch import norch_toolCommons\nreload(norch_toolCommons)\nnorch_toolCommons.norch_toolComnnons().norch_AttrAction(line="add",attrtype="alembic")')
        mc.setParent("..")        
        
        # 第10排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【Mesh同名】', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"sameShapeNodeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【proxy位移】', 'utf8')),c='mi_checkCommon.sk_checkTools().checkModelDetailsWarning(\"proxyInfo\")')
        mc.setParent("..")   
        
        # 第11排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【smoothSet】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning("smoothSet")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.3], label=(unicode('【Check】【renderState】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools;reload(sk_checkTools);sk_checkTools.sk_checkTools().checkModelDetailsWarning("renderState")')
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
        mc.showWindow("sk_sceneUICheckTools")
        
    # 提取选择物体
    def sk_sceneDetailsSelectObject(self):
        pathInfo = mc.textField('sk_sceneUICheckName', q=1, text=1)
        objPath = pathInfo.split('\t')[-1]
        mc.select(objPath)
        
    '''
    【通用：获取checkList内所有相同元素的编号】
    0.通用
    Author: 沈  康
    Data    :2013_05_20
    '''
    # 获取list内所有相同元素的编号 ，index number
    def checkListSameAllIndex(self, checkList, checkObj):
        tempList = checkList[:]
        checkAdd = 0
        allIndex = []
        while tempList.count(checkObj) > 0:
            indexNow = tempList.index(checkObj)
            allIndex.append(checkAdd + indexNow)
            tempList.remove(checkObj)
            checkAdd = checkAdd + 1
        return allIndex


    '''
    【通用：核心处理-层级归类，最深到最高层级】
    0.通用
    Author: 沈  康
    Data    :2013_10_30
    '''
    # 重新排序
    def sk_checkObjOutlinerReorder(self,objList):
        # 记录长度
        lenInfoList = []
        for obj in objList:
            lenInfoList.append(len(mc.ls(obj,l=1)[0].split('|'))-1)
        # 重新排序
        # 最大值最小为1，最小值最小为1
        reorderList = []
        lenInfo = lenInfoList[:]
        maxDeep = max(lenInfo)
        minDeep = min(lenInfo)
        while maxDeep >= minDeep:
            allIndex = self.checkListSameAllIndex(lenInfo, maxDeep)
            maxObj = []
            for index in allIndex:
                maxObj.append(mc.ls(objList[index],l=1)[0])
                # 更新lenInfo
                lenInfo[index] = 0
            # 存储信息
            reorderList.append(maxObj)
            # 更新max
            maxDeep = max(lenInfo)
        return reorderList

    '''
    【通用：model命名检测工具】
    0.仅在model,rig,texture通用
    1.检测只有一个大组
    2.所有带'_'的物体是否有shape节点
    Author: 沈  康
    Data    :2013_05_16
    '''
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

    # 仅检测MODEL及其下的节点    
    # 检测MSH前缀,'_'后缀的检测：有'_'必须有shape，无'_'必须无shape    
    # 检测最后后缀多重'_'的检测，如'MSH_c_hi_mouth__'进行报错处理
    # 对于MSH命名，必须是MSH_c_hi_XX这样的命名，除了MSH_all及MSH_geo
    # 允许nurbs控制器在MODEL组
    def checkMSHName(self, model):
        import types
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        '''
        if grps:
            for grp in grps:
                # 检测命名后缀    
                # MSH前缀判断，MODEL除外
                setpGrp = grp.split('|')
                grpConfig = setpGrp[-1]

                # 长度问题.只对mesh检测
                exName = ['MSH_all', 'MSH_geo', 'Master', 'WORLD']
                if grpConfig[-1] == '_':
                    num=''
                    split = grpConfig.split('_')
                    if split[0][0]=='p':
                        num=split[0][1:7]                    
                    if split[0][0]=='p' and int(num)>=1000 and len(split) < 4:
                        errorInfo.append(grp)
                    if split[0][0]!='p' and len(split) < 4:
                        errorInfo.append(grp)
                # mesh'_'后缀判断
                if grpConfig[-1] == '_':
                    split = grpConfig.split('_')
                    # '__'的处理
                    if split[-2] == '':
                        errorInfo.append(grp)
                    # 模型的子物体必须有shape,且为mesh
                    shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                    if shape :
                        continue
                    else:
                        errorInfo.append(grp)
                # 无'_'后缀的判断，除了nurbsCurve，必须没有Shape
                else:
                    shape = mc.listRelatives(grp, s=1, ni = 1,f=1)
                    if shape:
                        needNodes = ['nurbsCurve','directionalLight','ambientLight','pointLight','spotLight','areaLight','volumeLight','aiStandIn','aiSkyDomeLight','aiAreaLight']
                        num=''
                        split = grpConfig.split('_')
                        if split[0][0]=='p':
                            num=split[0][1:7]  
                        if type(num)!=int:
                            mc.error(u'==========================【%s】文件命名错误==========================' % grpConfig )                                                
                        if split[0][0]=='p' and type(num)==int and int(num)>=1000 and mc.nodeType(shape[0]) not in needNodes:
                            errorInfo.append(grp)
                        if split[0][0]!='p' and mc.nodeType(shape[0]) not in needNodes:
                            errorInfo.append(grp)    
        ''' 
        return list(set(errorInfo))
        
    # 仅检测MODEL及其下的节点    
    # 检测每个有mesh节点的物体是否有.MaxSmooth属性
    def checkModelSmooth(self, model):
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        if grps:
            for grp in grps:
                # 只支持mesh
                shape = mc.listRelatives(grp , pa=1 , ni=1 , s=1 , type='mesh' , f=1)
                if shape:
                    if mc.nodeType(shape[0]) == 'mesh':
                        # 判断是否有MaxSmooth属性
                        attr = mc.ls(grp + '.MaxSmooth')
                        if attr == []:
                            errorInfo.append(grp)
        return errorInfo
    
    # 所有重命名检测    #需要优化，太卡，双重循环

    '''
    【通用：重命名检测及修正工具】
    0.所有环节通用
    1.对多边形,nurbs曲面和细分曲面后缀加'_'
    Author: 沈  康
    Data    :2013_05_29-2013_05_30
    2.修正顺序：
    checkSameRename('MSH')
    checkSameRename('mesh')
    checkSameRename('nurbsCurve')
    checkTransformShapeSameNameConfig()
    checkMeshSameNameNodesConfig()
    '''
    # 新版重名，只有一个循环、while还可以优化
    # 获取重名
    def checkSameName(self, nodeType='transform',skipGrp = '',needShape = 0 ):
        # translate处理
        if nodeType == 'transform':
            grps = mc.ls(type=nodeType, l=1)
            errorInfo = []
            simpleGrps = []
            simpleSetGrps = []
            check = 0
            skipNum = 0
            for grp in grps:
                if skipGrp :
                    if not (':%s|'%skipGrp in grp or '|%s|'%skipGrp in grp):
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
        if nodeType == 'mesh' or nodeType == 'nurbsCurve':
            grps = mc.ls(type=nodeType, l=1)
            errorInfo = []
            simpleGrps = []
            simpleSetGrps = []
            check = 0
            for grp in grps:
                simple = grp.split('|')[-1]
                simpleGrps.append(simple)
                simpleSetGrps.append(simple)
                if (len(list(set(simpleSetGrps))) + check) != len(simpleGrps):
                    check = check + 1
                    tempGrps = simpleGrps[:]
                    tempAdd = 0
                    while tempGrps.count(simple) > 0:
                        errorInfo.append(grps[int(tempGrps.index(simple) + tempAdd)])
                        tempAdd = tempAdd + 1
                        tempGrps.remove(simple)
        return list(set(errorInfo))

    # 重名字典存储,存储数据深度
    def checkSameNameDetails(self , nodeType='transform' , objs = []):
        needNodeType = ['transform','mesh','nurbsCurve']
        # 相同名字
        if objs == []:
            if nodeType in needNodeType:
                grps = self.checkSameName(nodeType)
            # 全部大写MSH
            if nodeType == 'MSH':
                grps = mc.ls('msh_*', type='transform', l=1)
            # 全部小写msh
            if nodeType == 'msh':
                grps = mc.ls('MSH_*', type='transform', l=1)
        else:
            grps = objs
        # 信息
        simpleGrps = []
        # 全名信息
        sameDetails = dict({})
        MSHNameDetails = []
        # 组深度信息
        deepDetails = dict({})
        MSHDeepDetails = []
        if grps:
            for grp in grps:
                simple = grp.split('|')[-1]
                simpleGrps.append(simple)
                if nodeType == 'MSH' or nodeType == 'msh':
                    MSHNameDetails.append(grp)
                    MSHDeepDetails.append(len(grp.split('|')))
            # 键集
            simpleSetGrps = list(set(simpleGrps))
            # 键集合,创建默认键list(set(simpleGrps))
            for key in simpleSetGrps:
                # 创建键
                sameDetails[key] = []
                deepDetails[key] = []
                if nodeType in needNodeType:
                    allIndex = self.checkListSameAllIndex(simpleGrps, key)
                    for index in allIndex:
                        sameDetails[key].append(grps[index])
                        deepDetails[key].append(len(grps[index].split('|'))) 
        else:
            sameDetails = []
            deepDetails = []
        # 返回数据
        result = []
        if nodeType in needNodeType:
            result.append(sameDetails)
            result.append(deepDetails)
        if nodeType == 'MSH' or nodeType == 'msh':
            result.append(MSHNameDetails)
            result.append(MSHDeepDetails)
        return result

    
    # 重命名相同名字 
    def checkSameRename(self, nodeType='transform',renderCheck = 'MODEL'):
        # 对本身要处理，MSH类
        # 组深度信息
        info = self.checkSameNameDetails(nodeType)
        sameDetails = info[0]
        deepDetails = info[1]
        # 重名编号
        checkID = 1
        if info != [[], []]:
            # 获取key数组
            keyDetail = sameDetails.keys()   
            # Key值下最深信息
            maxDetails = []
            for key in sameDetails:
                if deepDetails[key]:
                    maxDetails.append(max(deepDetails[key]))
            # 处理组类型
            while max(maxDetails) != 0:
                deepIndex = self.checkListSameAllIndex(maxDetails, max(maxDetails))
                # 最深的编号
                for index in deepIndex:
                    # 获取key组内最大值
                    keyMaxIndex = self.checkListSameAllIndex(deepDetails[keyDetail[index]], max(maxDetails))
                    # 重名编号
                    for jIndex in keyMaxIndex:
                        # 判断是否需要重命名
                        doRename = 0
                        if renderCheck:
                            if ('|' + renderCheck + '|') in sameDetails[keyDetail[index]][jIndex]:
                                doRename = 1
                        else:
                            doRename = 1
                        # 重命名
                        if doRename:
                            # 先处理shape
                            shape = mc.listRelatives(sameDetails[keyDetail[index]][jIndex], s=1, f=1)
                            if shape:
                                # 重命名
                                # mesh类,nurbs及细分类
                                if mc.nodeType(shape[0]) == 'mesh' or mc.nodeType(shape[0]) == 'nurbsSurface' or mc.nodeType(shape[0]) == 'subdiv':
                                    newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + str(checkID) + '_'
                                    checkID = checkID + 1
                                    mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                                # nurbs曲线及骨骼等
                                else:
                                    newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + '_' + str(checkID)
                                    checkID = checkID + 1
                                    mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                            # 大组类
                            else:
                                newName = sameDetails[keyDetail[index]][jIndex].split('|')[-1] + '_' + str(checkID)
                                checkID = checkID + 1
                                mc.rename(sameDetails[keyDetail[index]][jIndex] , newName)
                        # 清除key信息
                        sameDetails[keyDetail[index]][jIndex] = ''
                        deepDetails[keyDetail[index]][jIndex] = 0
                # 下一轮更新
                maxDetails = []
                for key in sameDetails:
                    # objs = sameDetails[key]
                    if deepDetails[key]:
                        maxDetails.append(max(deepDetails[key]))
                    else:
                        maxDetails.append(0)           
        # 输出重命名数量
        #print(unicode('====================共处理【%s】处【%s】重命名====================' % (str(checkID - 1), str(nodeType)), 'utf8'))
        print(u'====================共处理【%s】处【%s】重命名====================' % ((checkID - 1), (nodeType)))

    # 处理物体和形节点同名
    def checkTransformShapeSameNameConfig(self):
        grps = mc.ls(type = 'transform',l=1)
        renameNum = 0
        if grps:
            for grp in grps:
                shape = mc.listRelatives(grp,ni=1 ,s = 1,f = 1)
                if shape:
                    grpName = grp.split('|')[-1]
                    shapeName = shape[0].split('|')[-1]
                    if grpName == shapeName:
                        mc.rename(shape[0],shapeName + 'Shape')
                        renameNum = renameNum + 1
        print(u'====================共处理【%s】处【%s】重命名====================' % ((renameNum), (u'物形')))
    
    # 处理mesh同名物体
    def checkMeshSameNameNodesConfig(self):
        meshInfos = self.checkMeshSameNameNodes()
        renameNum = 0
        if meshInfos and meshInfos != [u'有同名mesh!!!']:
            # 被transform和mesh检测干掉后应该不存在同类型的同名
            # 保险点不处理组
            num = 0
            for infoNode in meshInfos:
                shape = mc.listRelatives(infoNode,ni=1 ,s = 1,f = 1)
                if shape:
                    nodeName = infoNode.split('|')[-1]
                    # 后缀记数
                    num = num + 1
                    if mc.nodeType(shape[0]) == 'mesh':
                        newName = nodeName + str(num) + '_'
                    else:
                        newName = nodeName + str(num)
                    mc.rename(infoNode , newName)
                    renameNum = renameNum  + 1 
        print(u'====================共处理【%s】处【%s】重命名====================' % ((renameNum), (u'mesh同名')))
                        

    # 检测mesh同名物体（包括）
    def checkMeshSameNameNodes(self):
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


    # 处理msh及MSH统一问题
    def checkMSHKeepOneRename(self, mshType='MSH'):
        # 处理msh大小写问题，统一大写
        grpInfos = self.checkSameNameDetails(mshType)
        nameDetails = grpInfos[0]
        deepDetails = grpInfos[1]
        # ID
        checkID = 0
        if nameDetails:
            # 传递数据
            nameConfig = nameDetails[:]
            deepConfig = deepDetails[:]
            # 处理最深的
            maxDeep = max(deepConfig)
            # 开始循环
            while deepConfig:
                maxInfo = self.checkListSameAllIndex(deepConfig, maxDeep)
                # 开始处理
                for i in range(len(maxInfo)):
                    oldName = nameConfig[maxInfo[i] - i]
                    if mshType == 'MSH':
                        tempName = oldName.split('|')[-1]
                        samePart = tempName.split('msh_')[-1]
                    if mshType == 'msh':
                        tempName = oldName.split('|')[-1]
                        samePart = tempName.split('MSH_')[-1]
                    newName = mshType + '_' + samePart
                    mc.rename(oldName , newName)
                    checkID += 1
                    # 剔除记录
                    nameConfig.remove(nameConfig[maxInfo[i] - i])
                    deepConfig.remove(deepConfig[maxInfo[i] - i])
                if deepConfig:
                    maxDeep = max(deepConfig)
        # 输出重命名数量
        #print(unicode('====================共处理【%s】处【%s】重命名====================' % (str(checkID), str(mshType)), 'utf8'))
        print(u'====================共处理【%s】处【%s】重命名====================' % ((checkID), (mshType)))

    # MODEL或者其他阶段的instance检测
    def checkInstance(self, model):
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
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
    
    # 所有节点中_an_与_ca_无法共存; 同一节点中，_si_,_nr_,_an_,_ca_只能存在一个
    # ca标记的物体必须是mesh的transform节点
    # ca标记的必须是nurbsCurve
    def checkSignName(self):
        import sk_infoConfig
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        grps = mc.ls(type='transform', l=1)
        errorInfo = []
        caCheck = 0
        anCheck = 0
        for grp in grps:
            grpName = grp.split('|')[-1]
            signCheck = 0
            # 仅仅mesh
            # 对白海豚来说，_ca_在收集创建list时有MODEL和mesh两个条件，不必再检测
            if '_ct_an' in grpName:
                signCheck = signCheck + 1         
            if '_si_' in grpName:
                signCheck = signCheck + 1
            if '_nr_' in grpName:
                signCheck = signCheck + 1   
            if signCheck > 1:
                errorInfo.append(grp)
        #if caCheck == 1 and anCheck == 1:
        #    errorInfo.append('cache命名和an命名同时存在！')
        return errorInfo

    # 多边面检测
    def checkFaceVertexs(self, model):
        if model == 1:
            grps = mc.ls(type='transform', l=1)
            grps.remove('|persp')
            grps.remove('|top')
            grps.remove('|front')
            grps.remove('|side')
        else:
            model = mc.ls('MODEL')
            try:
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
            except:
                grps = []
        errorInfo = []
        if grps:
            for grp in grps:
                if grp[-1] == '_':
                    shape = mc.listRelatives(grp, ni=1 , s=1 , type='mesh' , f=1)
                    if shape:
                        try:
                            faceNum = mc.polyEvaluate(grp, f=1)
                            # 这里有时候会出错,尤其是命名中加了"_ca_"和"_"后缀的时候
                            if faceNum:
                                for i in range(faceNum):
                                    # 获取面的点
                                    pointInfo = list(set(mc.polyInfo((grp + '.f[' + str(i) + ']'), faceToVertex=1)[0].split(':')[1].split(' ')))
                                    if len(pointInfo) == 5 or len(pointInfo) == 6:
                                        pass
                                    else:
                                        errorInfo.append(grp)
                            else:
                                errorInfo.append(grp)
                        # 对残留的shape节点进行处理，某些组有shape节点，但不是polygon
                        except:
                            errorInfo.append(grp)
                    else:
                        #mc.warning(unicode('====================<<注意>> 请检查【%s】，该物体非mesh====================' % (str(grp)), 'utf8'))
                        mc.warning(u'====================<<注意>> 请检查【%s】，该物体非mesh====================' % (grp))
        return list(set(errorInfo))
    
    # 非法mesh检测
    # 这个处理大纲里显示为空组，但实际上有mesh节点的情况
    def checkMeshError(self):
        shaderSGList = self.checkCacheRecordMaterial()
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
    
    
    # smoothSet检测
    #　MODEL下所有物体在3个smoothSet下
    def checkModelSmoothSet(self,projType):
        import sk_smoothSet
        reload(sk_smoothSet)
        errorInfo = []
        # 合并smoothSet组
        smoothSetCheck = sk_smoothSet.sk_smoothSetTools().smoothSetCombine('Smooth',projType)
        if smoothSetCheck == 0:
            # 检测是否有货
            smoothObjs = sk_smoothSet.sk_smoothSetTools().smoothSetGetObjects(0) + sk_smoothSet.sk_smoothSetTools().smoothSetGetObjects(1) + sk_smoothSet.sk_smoothSetTools().smoothSetGetObjects(2)
            errorInfo = []
            if smoothObjs:
                needSmoothObjs = []
                for obj in smoothObjs:
                    if '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                        needSmoothObjs.append(mc.ls(obj,l=1)[0])
                # 获取MODEL下所有物体
                meshes = mc.listRelatives('MODEL',ad = 1 ,type = 'mesh',f= 1)
                objs = []
                if meshes:
                    for mesh in meshes:
                        objs.append(mc.listRelatives(mesh,p=1,type = 'transform',f=1)[0])
                    objs = list(set(objs))
                    for obj in objs:
                        # 排除参考
                        if '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj and ':' not in obj:
                            if obj not in needSmoothObjs:
                                errorInfo.append(obj)
            else:
                errorInfo = [u'未发现有效SMOOTH物体']
        else:
            errorInfo = [u'未发现正版SMOOTH_SET']
        return errorInfo

    # MODEL组下，模型基本渲染属性开启检测
    def checkMeshRenderStates(self):
        errorObjs = []
        if mc.ls('MODEL'):
            objs = mc.listRelatives('MODEL',ad = 1 ,type = 'transform',f= 1)
            if objs:
                for obj in objs:
                    if mc.listRelatives(obj,c=1,ni=1,type = 'mesh',f=1):
                        if not (obj+'.MoA'):
                            mesh = mc.listRelatives(obj,c=1,ni=1,type = 'mesh',f=1)[0]
                            attrs = ['.castsShadows','.receiveShadows','.motionBlur','.primaryVisibility','.smoothShading']
                            checkState = 0
                            for attr in attrs:
                                state = mc.getAttr(mesh + attr)
                                if state == 0:
                                    checkState = 1
                                    break
                            if checkState:
                                if '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj and ':' not in obj:
                                    errorObjs.append(obj)
        else:
            errorObjs = ['No Model']
        return errorObjs

    # 错误警告显示
    def checkModelDetailsWarning(self,checkType = ''):
        infoWrong = []
        errorPrint = 0
        mo = 0
 
        # 创建ErrorSet
        self.checkErrorSetCreate()
 
        # 文件名检测，判断环节
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)

        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if len(info) > 3:
            
            # 错误检测，根据阶段不同而不同
            fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
            if info[3] == ('mo' + fileFormat):
                mo = 1
            
            # 参考检测
            if checkType == '' or checkType == 'refCheck':
                # 对set类不检测
                if info[1][0] not in ['s', 'S']:
                    # 获取参考数
                    rfnNods = mc.file(q=1, reference=1)
                    # 有参考时
                    if rfnNods:
                        infoWrong.append(u'【 警告 】\t\t有参考存在，请注意核查！！')
                # 无参考时
                else:
                    # 检测是否有非法MODEL组
                    if info[0] == 'ice':
                        for i in range(0, 9):
                            grp = mc.ls('MODEL' + str(i))
                            if mc.ls('MODEL' + str(i)):
                                infoWrong.append(u'【错误存在】\t\t%s' % (str(grp[0])))
                                errorPrint = errorPrint + 1
            print '\n'
            
            # 对set类不检测
            if info[1][0] not in ['s', 'S']:
                # 检测namespace
                if checkType == '' or checkType == 'nsCheck':
                    namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
                    if len(namespace) > 2:
                        infoWrong.append(u'【 错 误 】\t\t存在namespace，请清理掉！')
                        errorPrint = errorPrint + 1
                        
            print '\n'
                        
            # 检测MODEL组重命名
            model = mc.ls('MODEL')
            # ZM的设置居然出现MODEL1这样的组。。。我很无语了。。。就这样吧
            if info[0] != 'zm':
                for num in range(9):
                    model = model + mc.ls('MODEL' + str(num) + '*')
            if model:
                if len(model) > 1:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不止一个！')
                    errorPrint = errorPrint + 1
                else:
                    print '\n'
                    
                    # 检测大组数目
                    rootGrps = self.checkOutlinerGroup()
                    if rootGrps:
                        # 根目录大组数目。特殊项目特殊情况
                        if info[0] == 'ice':
                            numRootGrp = len(rootGrps)
                            if numRootGrp > 1:
                                infoWrong.append(u'【 错 误 】\t\t大组不止一个！')
                                errorPrint = errorPrint + 1
                    else:
                        infoWrong.append(u'【 错 误 】\t\t文件是空的！！')
                        errorPrint = errorPrint + 1

                print '\n'

                # 需要判断[mo]的MODEL的函数才能执行
                if checkType == '' or checkType == 'MSHCheck':
                    # 检测错误命名
                    errorNames = self.checkMSHName(mo)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【命名错误】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1  
                        mc.sets(errorNames , e=1 , addElement='Error_MSHName')  
                    else:
                        mc.delete('Error_MSHName')

                print '\n'

                # 渲染属性检测
                if checkType == '' or checkType == 'renderState':
                    # 对zm的set不检测
                    if not (info[0] == 'zm' and info[1][0] in ['s', 'S']):
                        errorNames = self.checkMeshRenderStates()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_RenderState')  
                        else:
                            mc.delete('Error_RenderState')     

                print '\n'


                # 多边面错误
                if checkType == '' or checkType == 'faceCheck':
                    # 英雄工厂不检测五边面
                    if info[0] != 'hf' and info[1][0] not in ['s', 'S']:
                        errorNames = self.checkFaceVertexs(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_N4Edges')  
                        else:
                            mc.delete('Error_N4Edges')     
                    else:
                        mc.delete('Error_N4Edges')      
                    
                print '\n'
                
                # instance检测
                # 对场景不检测
                if checkType == '' or checkType == 'insCheck':
                    if info[1][0] not in ['s', 'S']:
                        errorNames = self.checkInstance(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【instance】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_Instance')  
                        else:
                            mc.delete('Error_Instance')    
                    else:
                        mc.delete('Error_Instance')  
                        
                print '\n'

                # 检测MaxSmooth属性
                if checkType == '' or checkType == 'smoothCheck':
                    # 英雄工厂需要
                    if info[0] == 'hf':
                        errorNames = self.checkModelSmooth(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【无Max平滑】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_MaxSmooth')  
                        else:
                            mc.delete('Error_MaxSmooth')         
                    else:
                        mc.delete('Error_MaxSmooth')                 

                print '\n'

                # 检测标记错误
                if checkType == '' or checkType == 'signCheck':
                    if info[0] == 'zm':
                        errorNames = self.checkSignName()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【标记错误】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_SignInfo')  
                        else:
                            mc.delete('Error_SignInfo')  
                    else:
                        mc.delete('Error_SignInfo')  
                if checkType =='':
                    from idmt.maya.py_common import GDC_checkin
                    reload(GDC_checkin)
                    GDC_checkin.GDC_checkin().gdc_geocheck()
                    GDC_checkin.GDC_checkin().yd_checkGeo()
                    GDC_checkin.GDC_checkin().GDC_faceAssignments()
                    print u'非法模型，文件结构，面赋材质检测'
            else:
                print '\n'
                infoWrong.append(u'【 错 误 】\t\tMODEL组不存在！！')
                errorPrint = errorPrint + 1

            print '\n'

            # 对set类不检测
            if info[1][0] not in ['s', 'S']:
                # 检测重名错误
                if checkType == ''  or checkType == 'sameTransformCheck' :
                    errorNames = []
                    errorNamesTemp = self.checkSameName(needShape = 1)
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    passList = ['zm_p075001Rope101B']
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameNode')  
                    else:
                        mc.delete('Error_SameNameNode')  
                            
                print '\n'   
                
                # 检测重名错误|shape节点检测
                if checkType == '' or checkType == 'sameShapeCheck':
                    errorNames = []
                    errorNamesTemp = self.checkSameName('mesh')
                    errorNamesTemp = errorNamesTemp + self.checkSameName('nurbsCurve')
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    passList = ['zm_p075001Rope101B']
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameShape')  
                    else:
                        mc.delete('Error_SameNameShape')                      
    
                print '\n'
                
                # 检测mesh同名节点 
                if checkType == '' or checkType == 'sameShapeNodeCheck':
                    errorNames = []
                    errorNamesTemp = self.checkMeshSameNameNodes()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    if errorNames:
                        if errorNames == [u'有同名mesh!!!']:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str('有同名mesh!!!')))
                        else:
                            for name in errorNames:
                                infoWrong.append(u'【shape同名】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_SameShapeNode')  
                    else:
                        mc.delete('Error_SameShapeNode')                      
    
                print '\n'

            # 检测proxy属性信息
            if checkType == '' or checkType == 'proxyInfo':
                from idmt.maya.py_common import sk_sceneConfig
                reload(sk_sceneConfig)
                errorNames = sk_sceneConfig.sk_sceneConfig().sk_sceneProxyInfoCheck(0)
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【proxy位移】\t\t%s' % (str(name)))
                        errorPrint = errorPrint + 1
                    mc.sets(errorNames , e=1 , addElement='Error_ProxyInfo')  
                else:
                    mc.delete('Error_ProxyInfo')
                    
            print '\n'

            # 检测Mesh错误
            if checkType == '' or checkType == 'meshError':
                errorNames = self.checkMeshError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【Mesh错误】\t\t%s' % (str(name)))
                        errorPrint = errorPrint + 1

            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
                reload(sk_smoothSet)
                if info[3].split('.')[0] in ['mo','tx']:
                    if info[0] in ['zm','csl']:
                        errorNames = self.checkModelSmoothSet(info[0])
                        if errorNames:
                            if errorNames == [u'未发现正版SMOOTH_SET']:
                                infoWrong.append(u'【SmoothSet】\t\tDidn\'t find SMOOTH_SET')
                                errorPrint = errorPrint + 1
                            if errorNames == [u'未发现有效SMOOTH物体']:
                                infoWrong.append(u'【SmoothSet】\t\tDidn\'t find Smooth Objects')
                                errorPrint = errorPrint + 1
                            if errorNames and errorNames != [u'未发现正版SMOOTH_SET'] and errorNames != [u'未发现有效SMOOTH物体']:
                                for name in errorNames:
                                    infoWrong.append(u'【Smmoth漏掉】\t\t%s' % (str(name)))
                                    errorPrint = errorPrint + 1
                                mc.sets(errorNames , e=1 , addElement='Error_SmoothLost')  
                        else:
                            mc.delete('Error_SmoothLost')
            if  checkType == '':
                pass
                if info[0] == 'zm':
                    # CacheSet
                    self.checkCacheSetAdd()
                    # AnimSet
                    self.checkTransAnimSetAdd()
                    sk_sceneConfig.sk_sceneConfig().sk_sceneSetCombineConfig("ZM")
                    
                if info[0] == 'ice':
                    self.checkCacheSetAdd()
                    self.checkTransAnimSetAdd()
                # abc属性和MESHES都代表出cache的物体，只要一个标记即可
                #if info[0] == u'mi':
                #    import Other.minitiger.mi_base_proc as mbp;reload(mbp)
                #    mbp.abc_info_checkin()
            # 检测参考有没有加载
            if checkType == '' or checkType == 'refCheck':
                from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
                reload(sk_referenceConfig)
                refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                checkRef = 0
                if refInfos[0][0]:
                    for refNode in refInfos[0][0]:
                        isLoad = mc.referenceQuery(refNode,isLoaded = 1)
                        if not isLoad:
                            checkRef = 1
                if checkRef:
                    infoWrong.append(u'【Unload Reference】\t\t请加载所有参考！！！')
                    errorPrint += 1
        else:
            print '\n'
            infoWrong.append(u'【 错 误 】\t\t文件名错误！ ')
            errorPrint = errorPrint + 1
        # 删除ErrorSet
        if errorPrint == 0:
            try:
                mc.delete('ErrorTemp_Set')
            except:
                pass
        

        # 输出错误消息
        #print(unicode('=============================【文件中错误如下】=============================', 'utf8'))
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            #print(unicode('%s' % (str(info)), 'utf8'))
            print info
        #print(unicode('===========================【目前】共计【%s】处错误===========================' % (str(errorPrint)), 'utf8'))
        print(u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
        #mc.warning(unicode('===========================【目前】共计【%s】处错误===========================' % (str(errorPrint)), 'utf8'))
        mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrint)
        
        # 解锁
        self.checkUnlockMSHV()
        self.checkUnlockMSHGeo()
        
        return errorPrint

    # 选取报错物体
    def checkDetailsObject(self, info):
        info = info.split('\t')[-1]

    # ErrorSet
    def checkErrorSetCreate(self):
        # 文件名检测，判断环节
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)

        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if mc.objExists('ErrorTemp_Set'):
            pass
        else:
            mc.createNode('objectSet', n='ErrorTemp_Set')
        # 命名错误
        if mc.objExists('Error_MSHName'):
            mc.sets(cl='Error_MSHName')
        else:
            mc.createNode('objectSet', n='Error_MSHName')
            mc.sets('Error_MSHName', e=1, addElement='ErrorTemp_Set')
        # 非四边形
        if mc.objExists('Error_N4Edges'):
            mc.sets(cl='Error_N4Edges')
        else:
            mc.createNode('objectSet', n='Error_N4Edges')
            mc.sets('Error_N4Edges', e=1, addElement='ErrorTemp_Set')   
        # instance
        if mc.objExists('Error_Instance'):
            mc.sets(cl='Error_Instance')
        else:
            mc.createNode('objectSet', n='Error_Instance')
            mc.sets('Error_Instance', e=1, addElement='ErrorTemp_Set')   
        if len(info) > 3:
            # MaxSmoothSet
            if mc.objExists('Error_MaxSmooth'):
                mc.sets(cl='Error_MaxSmooth')
            else:
                mc.createNode('objectSet', n='Error_MaxSmooth')
                mc.sets('Error_MaxSmooth', e=1, addElement='ErrorTemp_Set')
            # MaxSmoothSet
            if mc.objExists('Error_SignInfo'):
                mc.sets(cl='Error_SignInfo')
            else:
                mc.createNode('objectSet', n='Error_SignInfo')
                mc.sets('Error_SignInfo', e=1, addElement='ErrorTemp_Set')
        # SameName Transform
        if mc.objExists('Error_SameNameNode'):
            mc.sets(cl='Error_SameNameNode')
        else:
            mc.createNode('objectSet', n='Error_SameNameNode')
            mc.sets('Error_SameNameNode', e=1, addElement='ErrorTemp_Set')  
        # SameName Shape
        if mc.objExists('Error_SameNameShape'):
            mc.sets(cl='Error_SameNameShape')
        else:
            mc.createNode('objectSet', n='Error_SameNameShape')
            mc.sets('Error_SameNameShape', e=1, addElement='ErrorTemp_Set')  
        # Error_SameShapeNode
        if mc.objExists('Error_SameShapeNode'):
            mc.sets(cl='Error_SameShapeNode')
        else:
            mc.createNode('objectSet', n='Error_SameShapeNode')
            mc.sets('Error_SameShapeNode', e=1, addElement='ErrorTemp_Set') 
        # ProxyInfo
        if mc.objExists('Error_ProxyInfo'):
            mc.sets(cl='Error_ProxyInfo')
        else:
            mc.createNode('objectSet', n='Error_ProxyInfo')
            mc.sets('Error_ProxyInfo', e=1, addElement='ErrorTemp_Set')  
        # SmoothLost
        if mc.objExists('Error_SmoothLost'):
            mc.sets(cl='Error_SmoothLost')
        else:
            mc.createNode('objectSet', n='Error_SmoothLost')
            mc.sets('Error_SmoothLost', e=1, addElement='ErrorTemp_Set')  
        # RenderState
        if mc.objExists('Error_RenderState'):
            mc.sets(cl='Error_RenderState')
        else:
            mc.createNode('objectSet', n='Error_RenderState')
            mc.sets('Error_RenderState', e=1, addElement='ErrorTemp_Set')  


    # cache path 环境变量处理
    def checkCacheEnvPath(self):
        cacheFiles = mc.ls(type='cacheFile')
        if cacheFiles:
            for node in cacheFiles:
                cachePath = mc.getAttr(node + '.cachePath')
                cachePathNew = cachePath.replace('//file-cluster/GDC/Projects','${IDMT_PROJECTS}')
                mc.setAttr((node + '.cachePath'),cachePathNew,type = 'string')

    # 前期角色道具tx文件检测选面
    def checkFaceShaderDetails(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        check = 1
        if shotInfo[0] == 'zm':
            # 特殊内部任务ID
            strangeID = self.checkStrangeIDInfo()
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
                            meshFull = mc.ls(mesh,l = 1)[0]
                            if '|MODEL|' in meshFull and '.f[' in mesh:
                                errorAssetMeshes.append(meshFull)
            if errorAssetMeshes:
                for info in errorAssetMeshes:
                    print info
                print (u'------------请处理好以上选面赋予材质的物体------------')
                mc.error(u'------------请处理好以上选面赋予材质的物体------------')

    '''
            【通用：文件中透明贴图物体信息输出】
    0.仅在model,rig,texture通用
    Author: 沈  康
    Data    :2013_05_16
    '''
    # 获取有透明贴图的物体 assetTrans
    def checkTransparencyObjsInfoExport(self):
        transparencySG = []
        # 获取file节点
        SGNodes = mc.ls(type = 'shadingEngine')
        for SGNode in SGNodes:
            transLayerShaderCheckState = 0
            transRampShaderCheckState = 0
            # 判断是否有透明值
            transValueState = 0
            # 获取shader
            shaderNode = mc.listConnections( SGNode + '.surfaceShader')
            if shaderNode:
                # 获取提供透明属性的上级连接的节点
                transpancyNode = ''
                needTranparencyAttr = ''
                if mc.nodeType(shaderNode[0]) != 'surfaceShader':
                    # 判断是否层纹理
                    # 对于层纹理，一旦发现有透明贴图，立即将本节点的outTransparency输出给新layer shader
                    if mc.nodeType(shaderNode[0]) == 'layeredShader':
                        # 获取层纹理的input
                        layerInputs = mc.getAttr((shaderNode[0] + '.inputs'),mi = 1)
                        if layerInputs:
                            for inputNum in layerInputs:
                                transpancyNode = ''
                                transpancyAttr = mc.ls(shaderNode[0] + '.inputs[' + str(inputNum) + ']' + '.transparency')
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
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
                            transList = mc.getAttr((shaderNode[0] + '.transparency'),mi = 1)
                            for inputNum in transList:
                                transpancyNode = ''
                                transpancyAttr = mc.ls(shaderNode[0] + '.transparency[' + str(inputNum) + ']' + '.transparency_Color')
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
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
                                transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                                #print '-----'
                                #print transpancyAttr
                                #print transpancyNode
                                # 获取值
                                if not transpancyNode:
                                    transValue = mc.getAttr(transpancyAttr[0])
                                    if transValue[0][0] != 0:
                                        transValueState = 1
                                        transpancyNode = '[food]' + str(transValue[0][0])
                else:
                    transpancyAttr = mc.ls(shaderNode[0] + '.outTransparency')
                    transpancyNode = mc.listConnections(transpancyAttr[0], plugs = 1 , connections = 1 ,destination = 0 )
                    # 获取值
                    if not transpancyNode:
                        transValue = mc.getAttr(transpancyAttr[0])
                        if transValue[0][0] != 0:
                            transValueState = 1
                            transpancyNode = '[food]' + str(transValue[0][0])
                #print transpancyNode
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
                        meshes = mc.sets(SGNode,q=1)
                        #记录信息

                        transparencySG.append([SGNode,meshes,needTransNode])
                    else:
                        #meshes = mc.listConnections(SGNode,type = 'mesh')
                        meshes = mc.sets(SGNode,q=1)
                        #print u'------------------'
                        #print meshes
                        #print transpancyNode
                        #记录信息
                        if transValueState == 1:
                            transparencySG.append([SGNode,meshes,needTransNode])
                        else:
                            transparencySG.append([SGNode,meshes,needTransNode])
        # 输出信息
        import sk_infoConfig
        reload(sk_infoConfig)
        # 必须全部输出，避免由有内容到无内容的不更新bug更新
        #if transparencySG:
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
        mc.sysFile(localTransPath ,makeDir = 1)
        serverTransPath = serverPath + 'data/AssetInfos/transShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        
        # 本地输出及更新
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transSGNodes.txt'), transpancySGNodes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transSGNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transSGNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transMeshes.txt'), transpancyMeshes)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transMeshes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'transNodes.txt'), transpancyNode)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'transNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'transNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
            
    '''
            【通用：文件中置换贴图物体信息输出】
    0.仅在model,rig,texture通用
    Author: 沈  康
    Data    :2013_05_16
    '''
    # 获取有置换贴图的物体 assetTrans
    def checkDisplacementObjsInfoExport(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        
        displacementSGNodesAll = []
        displacementMeshesAll = []
        displacementNodesAll = []
        
        SGNodes = mc.ls(type = 'shadingEngine')
        for SGNode in SGNodes:
            # 判断SG节点是否有置换连接
            displacementCheck = 0
            checkDisNo1 = mc.listConnections((SGNode + '.displacementShader'),s = 1)
            if checkDisNo1:
                displacementCheck = 1
            if mc.objExists(SGNode + '.miDisplacementShader'):
                checkDisNo2 = mc.listConnections((SGNode + '.miDisplacementShader'),s = 1)
                if checkDisNo2:
                    displacementCheck = 2
            if displacementCheck:
                displacementSGNodesAll.append(SGNode)
                displacementMeshesAll.append(mc.sets(SGNode,q=1))
                if displacementCheck == 1:
                    displacementNodesAll.append( mc.listConnections((SGNode + '.displacementShader'),s = 1)[0] )
                if displacementCheck == 2:
                    displacementNodesAll.append( mc.listConnections((SGNode + '.miDisplacementShader'),s = 1)[0] )
        
        # 必须全部输出，避免由有内容到无内容的不更新bug更新
        # 本地及服务器端路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localTransPath = localPath + 'displacementShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        mc.sysFile(localTransPath ,makeDir = 1)
        serverTransPath = serverPath + 'data/AssetInfos/displacementShaderInfo/' + shotInfo[0] + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverTransPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        
        # 本地输出及更新
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'displacementSGNodes.txt'), displacementSGNodesAll)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'displacementSGNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'displacementSGNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'displacementMeshes.txt'), displacementMeshesAll)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'displacementMeshes.txt') + '"' + ' ' + '"' + (serverTransPath + 'displacementMeshes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        sk_infoConfig.sk_infoConfig().checkFileWrite((localTransPath +  'displacementNodes.txt'), displacementNodesAll)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localTransPath + 'displacementNodes.txt') + '"' + ' ' + '"' + (serverTransPath + 'displacementNodes.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)

    '''
    【通用：后缀'_'更改】
    0.仅在model,rig,texture通用
    Author: 沈  康
    Data    :2013_05_16
    '''
    # 此函数只处理_ca_及_ct_an
    def checkRenameAddPosfix(self, need, noNeed):
        nodes = mc.ls(sl=1)
        allNodes = mc.ls(type='transform')
        for node in allNodes:
            if noNeed in node:
                #print(unicode('====================发现【%s】，删除【%s】====================' % (str(noNeed), str(noNeed)), 'utf8'))
                print(u'====================发现【%s】，删除【%s】====================' % (noNeed, noNeed))
                temp = node.split(noNeed)
                newNode = temp[0] + temp[1]
                if newNode[-1] != '_':
                    newNode = newNode + '_'
                mc.rename(node, newNode)
        for node in nodes:
            if mc.nodeType(node) == 'transform' and need not  in node and '_nr_' not in node  and '_si_' not in node:
                if node[-1] != '_':
                    nodeNew = node + '_' + need[1:]
                else:
                    nodeNew = node + need[1:]
                mc.rename(node, nodeNew)

    # 添加'_'后缀
    def checkRenameMSHPosfix(self):
        nodes = mc.ls(sl=1,l=1)
        ID = 0
        for node in nodes:
            temp = node.split('|')[-1]
            if temp[-1] != '_':
                newName = temp + '_'
                mc.rename(node,newName)
                ID = ID + 1
        #print(unicode('====================共处理【%s】处【无_后缀】命名====================' % (str(ID)), 'utf8'))
        print(u'====================共处理【%s】处【无_后缀】命名====================' % (ID))
    
    '''
           选取所有的mesh的transfrom节点
    '''
    # 选取非MODEL组的
    def sk_sceneSelectAllPolygon(self):
        grps = mc.ls(type = 'transform',l=1)
        objs = []
        for grp in grps:
            if '|MODEL' not in grp:
                shape = mc.listRelatives(grp,s=1,type = 'mesh')
                if shape:
                    objs.append(grp)
        if objs:
            mc.select(objs)
                

    '''
            去掉物体中的'_ca_'标记
    '''
    # 去掉_ca_
    def checkSignReplace(self,sign):
        objs = mc.ls(sl=1)
        for obj in objs:
            if sign in obj:
                splitInfo = obj.split(sign)
                newName = ''
                for i in range(len(splitInfo)):
                    if i == 0:
                        newName = splitInfo[i]
                    if i <(len(splitInfo)-1) and i != 0:
                        newName = newName + splitInfo[i]
                    if i == (len(splitInfo)-1):
                        newName = newName + splitInfo[i]
                print newName
                mc.rename(obj,newName)
        mc.select(cl=1)
    
    
    '''
    【通用：cacheSet自动创建】
    0.仅在model,rig,texture通用
    1.含创建、更新cacheSet
    Author: 沈  康
    Data    :2013_05_16
    '''
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
        if mc.objExists('CACHE_CURVES'):
            pass
        else:
            mc.createNode('objectSet', n='CACHE_CURVES')
        if mc.objExists('CURVES'):
            pass
        else:
            mc.createNode('objectSet', n='CURVES')
            mc.sets('CURVES', e=1, addElement='CACHE_CURVES')            
    
        # 必须前面是指定物体，后面是set名
        #mc.sets(cl='MESHES')
        
    
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

    
    # 更新CacheSet列表
    def checkCacheSetAdd(self):
        self.checkCacheSetCreate()
        mc.sets(cl='MESHES')
        self.checkTransAnimSetCreate()
        needNodes=[]  
        nodes = mc.ls(type='transform',l=1)
        if nodes:
            for node in nodes:
                # 首先确保在MODEL组下
                if '|MODEL|' in mc.ls(node,l=1)[0] or '|SLP_GRP|'  in mc.ls(node,l=1)[0] or '|FUR_GRP|' in mc.ls(node,l=1)[0]:
                    if node[-1] == '_':
                        needNodes.append(node)
                    shape = mc.listRelatives(node, c=1, type='mesh',f=1)
                    if shape:
                        if node not in needNodes:
                            needNodes.append(node)
                            
        nodeNeeds=[]
        if needNodes:        
            for node in needNodes:
                if mc.objExists(node+'.alembic'):
                    nodeNeeds.append(node)
        
        if nodeNeeds:
            mc.sets(nodeNeeds , e=1 , addElement='MESHES')   
            print u'---'
        print (u'CacheList    ' + str(len(needNodes)))
   
        needCurs=[]  
        curves = mc.ls(type='transform',l=1)
        if curves:
            for cur in curves:
                if '|SHAVE|' in mc.ls(cur,l=1)[0]:           
                    shape = mc.listRelatives(cur,ad=1,f=1,ni=1,type='nurbsCurve')
                    if shape:
                        if cur not in needCurs:
                            needCurs.append(cur)
                           
        CurNeeds=[]
        if needCurs:        
            for node in needCurs:
                if mc.objExists(node+'.abc_curve'):                                           
                    CurNeeds.append(node)                    
        if CurNeeds:
            mc.sets(CurNeeds , e=1 , addElement='CURVES') 
            print u'---'
        print (u'CacheCurve   ' + str(len(CurNeeds)))    
    # 更新AnimSet列表 ，这个不会在mo阶段处理
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
    # 为所选物体添加ct_an标记|属性
    def checkCTANSignAdd(self):
        nodes = mc.ls(sl = 1,l= 1)
        if not nodes:
            print(u'=====请选择有效curve====')
            mc.error(u'=====请选择有效curve====')
        nodeNurbsCurveShapes = mc.listRelatives(nodes,ni = 1 ,c = 1 ,type = 'nurbsCurve',f = 1)
        if not nodeNurbsCurveShapes:
            print(u'=====请选择有效curve====')
            mc.error(u'=====请选择有效curve====')
        
        sign = 'ct_an'
        nodeNurbsCurves = mc.listRelatives(nodeNurbsCurveShapes,p = 1 ,type = 'transform',f = 1)
        for node in nodeNurbsCurves:
            attrList = mc.listAttr(node)
            if sign not in attrList:
                mc.select(node)
                mc.addAttr(longName = sign , keyable = 1,attributeType = 'float' , defaultValue = 1.0)
        mc.select(cl = 1)
    
 
    # 检测传递动画类型或者cacheSet类型
    def checkSetsType(self):
        cache = 0
        anim = 0
        # 合并Set
        self.checkCacheAnimSetCombine('Cache')
        self.checkCacheAnimSetCombine('Anim')
        # 检测cache
        self.checkCacheSetAdd()
        objs = mc.sets('MESHES', q=1)
        if objs:
            cache = 1
        # 检测anim
        self.checkTransAnimSetAdd()
        objs = mc.sets('CTRLS', q=1)
        if objs:
            anim = 1
            
        checkSets = [cache,anim]
        return checkSets
    
    # 记录tx文件中的smoothSet  角色道具不允许重名，场景。。随遇而安
    def checkAssetSmoothSetUpdate(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 本地路径
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        localInfoPath = localPath + 'smoothSetInfoTemp/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
        mc.sysFile(localInfoPath , makeDir = 1)
        serverInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
        makeDirCMD = 'zwSysFile(\"MD\",\"' + serverInfoPath + '\",\"\",1)'
        mel.eval(makeDirCMD)
        # 记录信息
        smoothObjs_lv0 = mc.sets('smooth_0',q=1)
        if smoothObjs_lv0 == None:
            smoothObjs_lv0 = []
        smoothObjs_lv1 = mc.sets('smooth_1',q=1)
        if smoothObjs_lv1 == None:
            smoothObjs_lv1 = []
        smoothObjs_lv2 = mc.sets('smooth_2',q=1)
        if smoothObjs_lv2 == None:
            smoothObjs_lv2 = []
        # 输出信息
        self.checkFileWrite((localInfoPath + 'smooth_0.txt'), smoothObjs_lv0)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_0.txt' ) + '"' + ' ' + '"' + (serverInfoPath + 'smooth_0.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        self.checkFileWrite((localInfoPath + 'smooth_1.txt'), smoothObjs_lv1)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_1.txt' ) + '"' + ' ' + '"' + (serverInfoPath + 'smooth_1.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
        self.checkFileWrite((localInfoPath + 'smooth_2.txt'), smoothObjs_lv2)
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localInfoPath + 'smooth_2.txt' ) + '"' + ' ' + '"' + (serverInfoPath + 'smooth_2.txt') + '"' + ' true'
        mel.eval(updateAnimCMD)
    
    '''
            【通用：后台检测anim和render版本是否一致】
    0.阶段通用
    Author: 沈  康
    Data    :2013_11_27
    '''
    # UI篇前台篇
    def checkAnim2RenderSetUI(self):
        # 窗口
        if mc.window ("sk_checkAnim2RenderSetUI", ex=1):
            mc.deleteUI("sk_checkAnim2RenderSetUI", window=True)
        mc.window("sk_checkAnim2RenderSetUI", title="Check Anim Render Cache List", widthHeight=(175, 100), menuBar=0)
        # 主界面
        mc.columnLayout()

        # Asset范围
        mc.frameLayout( label=u'检测Anim及Render版本', borderStyle='etchedOut' ,width = 175 )
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
        
        mc.optionMenuGrp('sk_checkAnim2RenderCheckType' ,e = 1 ,select = 5 )
        mc.optionMenuGrp('checkAnim2RenderModelType' ,e = 1 ,select = 3 )
        
        mc.rowLayout()
        mc.button(w=180 , h=50 , bgc=[0.3, 0.6, 0.3], label=(unicode('执行检测', 'utf8')), c='import maya.cmds as mc\ncheckType = mc.optionMenuGrp(\"sk_checkAnim2RenderCheckType\",q=1, value=1)[1]\nmodelType = mc.optionMenuGrp(\"checkAnim2RenderModelType\",q=1, value=1)[1]\nsk_checkCommon.sk_checkTools().checkAnim2RenderSetInfo(checkType,modelType)')
        mc.setParent("..")

        mc.setParent("..")
        mc.setParent("..")   
        mc.showWindow("sk_checkAnim2RenderSetUI")
        
    
    '''
    # 检测 anim和render版本差异，核心函数
    def checkAssetAnim2RenderCore(self,assetName,assetType,checkType,modelType):
        # 获取项目信息
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        difInfo = ''
        nofileInfo = ''
        # 准备工作
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        mayaType = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        modelHML = ['','_l_','_m_','_h_']
        masterFolderPath = '\\\\file-cluster\\GDC\\Projects\\' + projectName + '\\Project\\scenes\\' + assetType + '\\' + assetName + '\\master\\'
        # 模型类型处理
        if modelType in [1,2,3]:
            assetHML = modelHML[modelType]
            HMLcheck = 1
        if modelType == 0:
            HMLcheck = 3
        # 对于ZM，角色没有中低模
        if assetName[0] == 'c':
            HMLcheck = 1
        # 各个模型检测
        for i in range(HMLcheck):
            if HMLcheck == 1:
                if assetName[0] == 'c':
                    assetHML = modelHML[2]
                else:
                    assetHML = modelHML[modelType]
            else:
                assetHML = modelHML[i]
            animFile = masterFolderPath + shotInfo[0] + '_' + assetName + assetHML + 'ms_anim' + mayaType
            renderFile = masterFolderPath + shotInfo[0] + '_' + assetName + assetHML + 'ms_render' + mayaType
            if os.path.exists(animFile) and os.path.exists(renderFile):
                animSetNum = []
                cacheSetNum =[]
                difInfo = ''
                print u'\n'
                print u'------------------------------------------'
                print u'[Asset    %s|CheckType    %s|ModelType    %s]'%(assetName,str(checkType),assetHML)

                print u'---------------------open anim file...'
                # 检测版本性
                # 先打开anim文件
                # 先检测本文件
                mc.file((animFile + animFile ),open = 1 ,force = 1)
                self.checkTransAnimSetAdd()
                self.checkCacheSetAdd()
                localCacheObjs = []
                anotherCacheObjs = []
                if mc.sets('CTRLS', q=1):
                    localAnimObjs = mc.sets('CTRLS', q=1)
                    animSetNum.append(len(mc.sets('CTRLS', q=1)))
                else:
                    animSetNum.append(0)
                if mc.sets('MESHES', q=1):
                    localCacheObjs = mc.sets('MESHES', q=1)
                    cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                else:
                    cacheSetNum.append(0)
                # 打开render文件
                # 打开另一半文件并检测
                mc.file(renderFile , open = 1, f = 1)
                localAnimObjs = []
                anotherAnimObjs = []
                self.checkTransAnimSetAdd()
                self.checkCacheSetAdd()
                if mc.sets('CTRLS', q=1):
                    anotherAnimObjs = mc.sets('CTRLS', q=1)
                    animSetNum.append(len(mc.sets('CTRLS', q=1)))
                else:
                    animSetNum.append(0)
                if mc.sets('MESHES', q=1):
                    anotherCacheObjs = mc.sets('MESHES', q=1)
                    cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                else:
                    cacheSetNum.append(0)
                # 开始对比！！！！！
                # 数量对比处理
                if animSetNum[0] != animSetNum[1]:
                    difInfo = difInfo + (u'AnimSetNum_Dif') + '\n'
                if cacheSetNum[0] != cacheSetNum[1]:
                    difInfo = difInfo + (u'CacheSetNum_Dif') + '\n'
                if difInfo:
                    result = u'======本素材rg和tx版本CacheList有出入，请前期和设置协商共同处理======'
                    errorAssetFile.append(asset)
                    errorAssetFile.append(result)
                else:
                    # cache处理异常名字
                    difLocalCacheNameInfo = []
                    difAnotherCacheNameInfo = []
                    for cacheObj in localCacheObjs:
                        if cacheObj not in anotherCacheObjs:
                            difLocalCacheNameInfo.append(cacheObj)
                    for cacheObj in anotherCacheObjs:
                        if cacheObj not in localCacheObjs:
                            difAnotherCacheNameInfo.append(cacheObj)
                    # anim处理异常名字
                    difLocalAnimNameInfo = []
                    difAnotherAnimNameInfo = []
                    for animObj in localAnimObjs:
                        if animObj not in anotherAnimObjs:
                            difLocalAnimNameInfo.append(animObj)
                    for animObj in anotherAnimObjs:
                        if animObj not in localAnimObjs:
                            difAnotherAnimNameInfo.append(animObj)
                    if difLocalCacheNameInfo or difLocalAnimNameInfo:
                        errorAssetFile.append(asset)
                        if difLocalCacheNameInfo:
                            errorAssetFile.append(u'------------------[cache][anim文件][异常不同名字][如下]------------------')
                            for info in difLocalCacheNameInfo:
                                errorAssetFile.append(info)
                            errorAssetFile.append(u'------------------[cache][render文件][异常不同名字][如下]------------------')
                            for info in difAnotherCacheNameInfo:
                                errorAssetFile.append(info)
                        if difLocalAnimNameInfo:
                            errorAssetFile.append(u'------------------[anim][anim文件][异常不同名字][如下]------------------')
                            for info in difLocalAnimNameInfo:
                                errorAssetFile.append(info)
                            errorAssetFile.append(u'------------------[anim][render文件][异常不同名字][如下]------------------')
                            for info in difAnotherAnimNameInfo:
                                errorAssetFile.append(info)

                    mc.file(renderFile,open = 1,f =1)
                self.checkTransAnimSetAdd()
                self.checkCacheSetAdd()
                
                if mc.sets('CTRLS', q=1):
                    anotherAnimObjs = mc.sets('CTRLS', q=1)
                    animSetNum.append(len(mc.sets('CTRLS', q=1)))
                else:
                    animSetNum.append(0)
                if mc.sets('MESHES', q=1):
                    anotherCacheObjs = mc.sets('MESHES', q=1)
                    cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                else:
                    cacheSetNum.append(0)
                if j == 1:
                    print u'---------------------open render file...'
                if mc.sets('CTRLS', q=1):
                    animSetNum.append(len(mc.sets('CTRLS', q=1)))
                else:
                    animSetNum.append(0)
                if mc.sets('MESHES', q=1):
                    cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                else:
                    cacheSetNum.append(0)
                if animSetNum[0] != animSetNum[1]:
                    difInfo = difInfo + (u'[%s]_AnimSetNum_Dif'%assetName)
                if cacheSetNum[0] != cacheSetNum[1]:
                    difInfo = difInfo + (u'[%s]_CacheSetNum_Dif'%assetName)
                # 二级检测，处理同数量不同名
                if difInfo == '':
                    # cache处理异常名字
                    difLocalCacheNameInfo = []
                    difAnotherCacheNameInfo = []
                    for cacheObj in localCacheObjs:
                        if cacheObj not in anotherCacheObjs:
                            difLocalCacheNameInfo.append(cacheObj)
                    for cacheObj in anotherCacheObjs:
                        if cacheObj not in localCacheObjs:
                            difAnotherCacheNameInfo.append(cacheObj)
                    # anim处理异常名字
                    difLocalAnimNameInfo = []
                    difAnotherAnimNameInfo = []
                    for animObj in localAnimObjs:
                        if animObj not in anotherAnimObjs:
                            difLocalAnimNameInfo.append(animObj)
                    for animObj in anotherAnimObjs:
                        if animObj not in localAnimObjs:
                            difAnotherAnimNameInfo.append(animObj)
                    if difLocalCacheNameInfo or difLocalAnimNameInfo:
                        errorAssetFile.append(asset)
                        if difLocalCacheNameInfo:
                            errorAssetFile.append(u'------------------[cache][anim文件][异常不同名字][如下]------------------')
                            for info in difLocalCacheNameInfo:
                                errorAssetFile.append(info)
                            errorAssetFile.append(u'------------------[cache][render文件][异常不同名字][如下]------------------')
                            for info in difAnotherCacheNameInfo:
                                errorAssetFile.append(info)
                        if difLocalAnimNameInfo:
                            errorAssetFile.append(u'------------------[anim][anim文件][异常不同名字][如下]------------------')
                            for info in difLocalAnimNameInfo:
                                errorAssetFile.append(info)
                            errorAssetFile.append(u'------------------[anim][render文件][异常不同名字][如下]------------------')
                            for info in difAnotherAnimNameInfo:
                                errorAssetFile.append(info)
                print u'------------------------------------------'
            else:
                nofileInfo = (u'[no file]    [%s]    [%s]'%(assetHML,assetName))
        # 检测文件内mesh异常
        meshError = self.checkMeshError()
        meshInfo = ''
        if meshError:
            meshInfo = u'[Asset    %s|CheckType    %s|ModelType    %s]'%(assetName,str(checkType),assetHML)
        result = []
        result.append(difInfo)
        result.append(nofileInfo)
        result.append(meshInfo)
        return result
        '''

    # check in时检测Anim和Render版本差异
    # 增加豁免列表| keys: anim render 差异 | anim render 一致性
    def checkAssetAnim2RenderCheckInConfig(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        import os
        # 豁免判断
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        projectPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        scenesInfo = projectPath.split('/')[-2]
        doNotCheckTxtPath = projectPath + 'data/rgtxIgnore.txt'
        # 有文件，且本文件在文件列表里，则判断return跳出
        if os.path.exists(doNotCheckTxtPath):
            fileInfo = self.checkFileRead(doNotCheckTxtPath)
            if fileInfo:
                if shotInfo[1] in fileInfo:
                    print u'==========[一致性]本Asset处于豁免检测状态=========='
                    return 'ok'
        # zm项目部分植物豁免检测
        if shotInfo[0] == 'zm' and shotInfo[1][:4] == 'p000':
            print u'==========[一致性]本Asset处于豁免检测状态=========='
            return 'ok'
        # 非豁免状态，全部强制检测
        # 记录文件名
        mc.file(save = 1, force = 1)
        fileName = mc.file(query=1, exn=1)
        # 开始检测
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectName = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfo[0])
        mayaType = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        if len(shotInfo) >= 4: 
            assetInfo = sk_infoConfig.sk_infoConfig().checkProjectAssetNames()
            assetName = shotInfo[1]
            # 对ZM系列的p000050之后p002001之前的不检测
            if shotInfo[0] == 'zm' and shotInfo[1][0] == 'p':
                # 特殊内部任务ID
                strangeID = sk_infoConfig.sk_infoConfig().checkStrangeIDInfo()
                if shotInfo[1] not in strangeID:
                    assetID = shotInfo[1][1:7]
                    if int(assetID) > 50 and int(assetID) <= 2000:
                        return 'Pass'
            # 获取assetType
            if assetName in assetInfo[1] or shotInfo[1][0] == 'c':
                assetType = 'characters'
            if assetName in assetInfo[2] or shotInfo[1][0] == 'p':
                assetType = 'props'
            if assetName in assetInfo[3] or shotInfo[1][0] in ['s','m']:
                assetType = 'sets'
            modelHML = ['l','m','h']
            print u'---------------'
            print shotInfo[3].split('.')[0]
            print shotInfo[2]
            if shotInfo[2] in modelHML and shotInfo[3].split('.')[0] in ['rg','tx']:
                animSetNum = []
                cacheSetNum =[]
                difInfo = ''
                masterFolderPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
                masterFolderPath = masterFolderPath + 'scenes/' + assetType + '/' + assetName + '/master/'
                # 首先查询是否存在另一半文件,不存在则pass
                if shotInfo[3].split('.')[0] == 'tx':
                    assetOther = '_ms_anim'
                if shotInfo[3].split('.')[0] == 'rg':
                    assetOther = '_ms_render'
                fileOther = masterFolderPath + shotInfo[0] + '_' + assetName  + '_' + shotInfo[2] + assetOther + mayaType
                print u'------'
                print fileOther
                if os.path.exists(fileOther):
                    # 先检测本文件
                    self.checkTransAnimSetAdd()
                    self.checkCacheSetAdd()
                    localAnimObjs = []
                    localCacheObjs = []
                    localFaceNum = []
                    localVertexNum = []
                    localUVsNum = []
                    
                    anotherAnimObjs = []
                    anotherCacheObjs = []
                    anotherFaceNum = []
                    anotherVertexNum = []
                    anotherUVsNum = []

                    if mc.sets('CTRLS', q=1):
                        localAnimObjs = mc.sets('CTRLS', q=1)
                        if localAnimObjs:
                            localAnimObjs = mc.ls(localAnimObjs,l = 1)
                        animSetNum.append(len(mc.sets('CTRLS', q=1)))
                    else:
                        animSetNum.append(0)
                    if mc.sets('MESHES', q=1):
                        localCacheObjs = mc.sets('MESHES', q=1)
                        if localCacheObjs:
                            localCacheObjs = mc.ls(localCacheObjs , l = 1)
                        cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                    else:
                        cacheSetNum.append(0)
                    # 记录faceNum，vertex，uvs
                    if localCacheObjs:
                        for checkObj in localCacheObjs:
                            localFaceNum.append(mc.polyEvaluate(checkObj,face =1))
                            localVertexNum.append(mc.polyEvaluate(checkObj,vertex =1))
                            localUVsNum.append(mc.polyEvaluate(checkObj,uvcoord =1))
                            
                    # 打开另一半文件并检测
                    mc.file(fileOther , open = 1, f = 1)
                    self.checkTransAnimSetAdd()
                    self.checkCacheSetAdd()
                    if mc.sets('CTRLS', q=1):
                        anotherAnimObjs = mc.sets('CTRLS', q=1)
                        if anotherAnimObjs:
                            anotherAnimObjs = mc.ls(anotherAnimObjs,l = 1)
                        animSetNum.append(len(mc.sets('CTRLS', q=1)))
                    else:
                        animSetNum.append(0)
                    if mc.sets('MESHES', q=1):
                        anotherCacheObjs = mc.sets('MESHES', q=1)
                        if anotherCacheObjs:
                            anotherCacheObjs = mc.ls(anotherCacheObjs , l = 1)
                        cacheSetNum.append(len(mc.sets('MESHES', q=1)))
                    else:
                        cacheSetNum.append(0)
                    # 记录faceNum，vertex，uvs
                    if anotherCacheObjs:
                        for checkObj in anotherCacheObjs:
                            anotherFaceNum.append(mc.polyEvaluate(checkObj,face =1))
                            anotherVertexNum.append(mc.polyEvaluate(checkObj,vertex =1))
                            anotherUVsNum.append(mc.polyEvaluate(checkObj,uvcoord =1))
                    # 返回文件
                    mc.file(fileName,open = 1,f=1)
                    
                    # 检测阶段
                    # 数量对比处理
                    checkObjNum = 0
                    if animSetNum[0] != animSetNum[1]:
                        difInfo = difInfo + (u'AnimSetNum_Dif') + '\n'
                        checkObjNum = 1
                    if cacheSetNum[0] != cacheSetNum[1]:
                        difInfo = difInfo + (u'CacheSetNum_Dif') + '\n'
                        checkObjNum = 1
                    if checkObjNum:
                        print difInfo
                        print(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                        mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                    else:
                        # 此时数量都相等
                        checkNameDif = 0
                        # cache处理异常名字
                        difLocalCacheNameInfo = []
                        difAnotherCacheNameInfo = []
                        if localCacheObjs:
                            for cacheObj in localCacheObjs:
                                if cacheObj not in anotherCacheObjs:
                                    difLocalCacheNameInfo.append(cacheObj)
                            for cacheObj in anotherCacheObjs:
                                if cacheObj not in localCacheObjs:
                                    difAnotherCacheNameInfo.append(cacheObj)
                        # anim处理异常名字
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
                        if checkNameDif:
                            print(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                            mc.error(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                            
                        # cache物体和anim物体 faceNum，vertexNum，UV对比
                        difObjInfo = []
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
                            print(u'======本素材rg和tx版本有出入，请前期和设置协商共同处理======')
                            mc.error(u'\n======本素材rg和tx版本有出入，请前期和设置协商共同处理======')

                        print u'=====================AnimRender版本检测完毕====================='
                else:
                    pass
            else:
                print(u'==============================找不到对应Asset,请检查文件名==============================')
                mc.error(u'==============================找不到对应Asset,请检查文件名==============================')
        else:
            print(u'==============================找不到对应Asset,请检查文件名==============================')
            mc.error(u'==============================找不到对应Asset,请检查文件名==============================')
    
    
    '''
    【通用：清理工具系列】
    0.阶段通用
    Author: 沈  康
    Data    :2013_05_16
    '''
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
                            if layer.lower() not in donotLayers:
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
                            if layer.lower() not in donotLayers:
                                mc.delete(layer)
                        else:
                            mc.delete(layer)
        return errorDelete

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
        
    # 获取当前空组    #transform节点无shape子节点的，空
    def checkGetLastEmptyGroup(self):
        grps = mc.ls(type='transform')
        grp_empty = []
        for grp in grps:
            grp_child = mc.listRelatives(grp, c=1)
            if mc.nodeType(grp) == 'transform':
                if grp_child == None:
                    grp_empty.append(grp)
        return grp_empty
    
    # 删除空组，再获取上级空组，直到没有空组
    def checkCleanEmptyGroup(self):
        mel.eval('deleteEmptyGroups()')
        '''
        grp_empty = self.checkGetLastEmptyGroup()
        while grp_empty:
            try:
                mc.delete(grp_empty)
            except:
                pass
            grp_empty = self.checkGetLastEmptyGroup()
        '''
        
    # 清理asset里的persp相机关键帧
    def checkCleanPerspAnimation(self):
        attrs = ['translateX','translateY','translateZ','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ','visibility']
        for attr in attrs:
            if mc.ls('persp' + '_' + attr ):
                mc.delete('persp' + '_' + attr )
     
    
    '''    
    通用：锁lock/解锁unlock工具】
    0.阶段通用
    1.对指定节点及其下属子节点及其本身进行lock处理
    2.将显示属性解锁
    Author: 沈  康
    Data    :2013_03_29
    Data    :2013_05_10 处理重名物体带来的问题。解锁和锁合并函数
    '''
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

    # 解锁所有V
    # 解锁所有lodV
    def checkUnlockMSHV(self):
        meshes = mc.ls(type = 'mesh',l=1)
        if meshes:
            for mesh in meshes:
                grp = mc.listRelatives(mesh,p=1,type = 'transform',f=1)
                if grp:
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
    
    
    
    
    # 补充，解锁道具的geo组 ,需要下面的文件支持
    def checkUnlockMSHGeo(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
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
                     
    '''
            【通用：检测v属性】
            参考老赵思路：没有现成的函数，只能自己写
    Author: 沈  康
    Data    :2014_02_10
    '''
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

    '''
            【通用：文件名检测】
    0.所有阶段通用
    1.检测文件名
    Author: 沈  康
    Data    :2013_05_16
    '''
    #文件名镜头信息================
    def checkShotInfo(self):
        temp = (mc.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            #mc.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            mc.warning(u'========================【！！！文件名不规范！！！】========================')
             
        return info                   
    
    # 获取本地文件路径
    def checkPCFilePath(self):
        filePath = (mc.file(query=1, exn=1)).split('/')
        path = ''
        if filePath[0] != 'Z' and filePath[0] != '':
            for i in range(len(filePath) - 1):
                path = path + filePath[i] + '\\'
        return path
    
    
    '''
    【通用：处理normal】
    0.仅在model,rig,texture通用
    1.统一Normal，处理normal
    Author: 沈  康
    Data    :2013_05_18
    '''
    def checkNormalFix(self):
        grps = mc.ls(type='transform', l=1)
        for grp in grps:
            if grp[-1] == '_':
                # 法线统一
                mc.polyNormal(grp, normalMode=2)
                '''
                #判断当前法线方向是否正确
                faceNum = mc.polyEvaluate(grp, f = 1)
                for i in range(faceNum):
                    error = 0
                    normals = mc.polyInfo((grp + '.f['+ str(i) +']'),faceNormals= 1)[0].split(':')[1].split(' ')
                    for i in range(1, len(normals)):
                        if normals[i][0] == '-':
                            #判断错误方向
                            error = 1
                            break
                    if error == 1:
                        #翻转法线
                        mc.polyNormal(grp, normalMode = 0)
                        break  
                '''

    '''
    【通用：清理管理】
    0.仅在moErrorTemp_Set    1.对道具类的MSH_geo的lock进行解锁
    Author: 沈  康
    Data    :2013_05_18
    '''
    # 清理工具
        # 文件名
        # 清理历史
        # 法线处理
    # instance
    # 记得处理动画曲线
    def checkMoFileClean(self):
        errors = self.checkModelDetailsWarning()
        if errors == 0:
            # 文件名检测
            import sk_infoConfig
            info = sk_infoConfig.sk_infoConfig().checkShotInfo()
            fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
            if info[3] == ('mo' + fileFormat):
                #print(unicode('=====================【开始清理文件】=====================', "utf8"))
                print(u'=====================【开始清理文件】=====================')
                # 预清理历史
                model = mc.ls('MODEL')
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
                mc.select(grps)
                mel.eval('DeleteAllHistory')
                mc.select(cl=1)
                
                # 清理空组
                self.checkCleanEmptyGroup()
                #print(unicode('=====================【空组】清理完毕=====================', "utf8"))
                print(u'=====================【空组】清理完毕=====================')
                
                # 法线统一
                self.checkNormalFix()
                #print(unicode('=====================【normal】处理完毕=====================', "utf8"))
                print(u'=====================【normal】处理完毕=====================')
                
                # 清理displayer
                self.checkCleanDisplayLayers()
                #print(unicode('=====================【displayLayer】清理完毕=====================', "utf8"))
                print(u'=====================【displayLayer】清理完毕=====================')
                
                # 清理renderLayer
                self.checkCleanRenderLayers()
                #print(unicode('=====================【renderLayer】清理完毕=====================', "utf8"))
                print(u'=====================【renderLayer】清理完毕=====================')
                
                # 清理unusedNodes及未知节点
                self.checkDonotNodeClean()
                #print(unicode('=====================【垃圾节点】清理完毕=====================', "utf8"))
                print(u'=====================【垃圾节点】清理完毕=====================')
                
                # 清理历史
                model = mc.ls('MODEL')
                grps = mc.listRelatives(model[0], c=1, type='transform', ad=1, f=1)
                mc.select(grps)
                mel.eval('DeleteAllHistory')
                mc.select(cl=1)
                #print(unicode('=====================【MODEL】【history】清理完毕=====================', "utf8"))
                print(u'=====================【MODEL】【history】清理完毕=====================')
                
                # cacheSet更新
                self.checkCacheSetAdd()
                #print(unicode('=====================【cacheSet】更新完毕=====================', "utf8"))
                print(u'=====================【cacheSet】更新完毕=====================')

                # 锁物体
                if info[1][0] not in ['s', 'S']:
                    self.checkLockObjs(['MODEL'], 1)
                    self.checkUnlockMSHGeo()
                #print(unicode('=====================【锁】更新完毕=====================', "utf8"))
                print(u'=====================【锁】更新完毕=====================')
                
                # 清理完毕
                print '\n'
                #print(unicode('=====================【恭喜】清理完毕=====================', "utf8"))
                print(u'=====================【恭喜】清理完毕=====================')
            else:
                mc.warning(unicode('=====================【！！！您所用的不是【mo】阶段文件！！！】=====================', "utf8"))
                mc.warning(u'=====================【！！！您所用的不是【mo】阶段文件！！！】=====================')
                 
        else:
            #mc.warning(unicode('=====================【！！！请先处理所有错误命名！！！】=====================', "utf8"))
            mc.warning(u'=====================【！！！请先处理所有错误命名！！！】=====================')
             

    # 不参与渲染的物体清单
    def checkNoRenderObjs(self):
        grps = mc.ls(type='transform', l=1)
        outGrps = []
        for grp in grps:
            if '_si_' in grp or  '_nr_' in grp:
                outGrps.append(grp)
        return outGrps
    
    '''
    【通用：清理unUsed及unknown节点及turtle节点】
    0.通用
    Author: 沈  康
    Data    :2013_05_19
    '''
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
    
    # 全流程用
    def checkAssetforbidenNodes(self,arnoldCheck = 1):
        if arnoldCheck:
            arnoldNodes = mc.ls(type='aiAOVDriver')+ mc.ls(type='aiAOVFilter') +mc.ls(type='aiOptions')
            if arnoldNodes:
                print u'=====Asset 存在 Arnold 节点，请Export清理====='
                mc.error(u'=====Asset 存在 Arnold 节点，请Export清理=====')
    
    # 个人专用
    def checkDonotNodeClean(self, unuse=1 , turtle=1 , arnold = 0):
        
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
        if turtle and turtleNodes:
            for node in turtleNodes:
                # 非参考才执行删除
                if mc.referenceQuery(node,inr = 1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)
        
        # 清理arnold节点
        arnoldNodes = mc.ls(type='aiAOVDriver')+ mc.ls(type='aiAOVFilter') +mc.ls(type='aiOptions')
        if arnoldNodes and arnold:
            mc.setAttr('defaultRenderGlobals.ren','mayaSoftware',type = 'string')
            try:
                mel.eval('unloadPlugin "mtoa"')
            except:
                pass
            mc.disconnectAttr(':defaultArnoldFilter.msg' , ':defaultArnoldRenderOptions.filt')
            mc.disconnectAttr(':defaultArnoldDriver.msg' , ':defaultArnoldRenderOptions.drvr')
            for node in arnoldNodes:
                if mc.referenceQuery(node,inr = 1):
                    pass
                else:
                    if mc.ls(node):
                        mc.lockNode(node, l=0)
                        mc.delete(node)

    # 有必要一个norender组
    '''
    【通用：cache测试管理】
    0.仅在rig阶段使用
    1.cache测试
    Author: 沈  康
    Data    :2013_05_19 - 2013_05_20
    '''
    # 设置cache测试,rgCache
    def checkCacheRigTest(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        errors = self.checkModelDetailsWarning()
        if errors == 0:
            #shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localFilePath = sk_infoConfig.sk_infoConfig().checkTX2AnimRenderLocalPath()
            fileName = mc.file( exn = 1 , q = 1 )
            rgFileName = fileName.split('/')[-1]
            # 本地另存
            mc.file(rename = (localFilePath + rgFileName) )
            mc.file(save = 1 ,force = 1)
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
                mc.setKeyframe(v=0 , at='rotateY')
                # 最后一帧K帧
                mc.currentTime(frameEnd)
                mc.setKeyframe(v=50 , at='translateZ')
                mc.setKeyframe(v=360 , at='rotateY')
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
                
                # 镜头信息
                #dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                #cacheFileName = dirInfo[1]  + '_' + dirInfo[2] + '_cacheTest'

                # 更新cache列表，测试rig用时不需要祛除隐藏物体
                self.checkCacheSetAdd()
                self.checkTransAnimSetAdd()
                cacheObjs = mc.sets('MESHES', q=1)
                animObjs = mc.sets('CTRLS', q=1)
                
                if cacheObjs:
                    # 执行缓存创建,local,不偏移,非ref模式,不连接模式
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    self.checkCacheSetCacheExport( cacheObjs , 0 , 0 , 0  ,0)
                    
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
                            self.sk_checkBakeConstraints()
                        
                        # 执行约束导出,local,非ref模式
                        self.checkAnimCurveInfoExport(animObjs,0)
                        
                    # 转render文件
                    mc.file((localFilePath + rgFileName),open = 1 ,force = 1)
                    self.checkTexMo2CacheMo(checkin = 0)
                    
                    # 导入cache
                    self.checkCacheSetCacheImport( cacheObjs , 0 )

                    # 导入anim信息
                    if animObjs:
                        self.checkAnimCurveInfoImport(0)
                        
                    print u'\n'
                    print u'=====================Rg Cache创建完毕====================='
                    print u'>>>>>当前文件为您的rg文件模拟出的render文件'
                    print u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'
                    print u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'
                    print u'>>>>>如果涉及到_ct_an标记，请检测与Master环约束的_ct_an是否运动'
                    print u'\n'
                        
                else:
                    mc.warning(u'=====================【错误】未发现cache物体 ！！！】=====================')

                
                '''
                if objs:
                    for obj in objs:
                        if mc.getAttr((obj + '.v'),l=1):
                            try:
                                mc.setAttr((obj + '.v'),l=0)
                            except:
                                pass
                        try:
                            mc.setAttr((obj + '.v'), 1)
                        except:
                            pass
                else:
                    mc.warning(u'=====================【错误】未发现cache物体 ！！！】=====================')
                # mel用path
                localCachePath = self.checkLocalInfoPath()
                localCacheTestPath = (localCachePath + '/cacheTestTemp/' + dirInfo[0] + '/' + dirInfo[1] + '/')

                # 执行缓存创建
                #self.checkCacheCreateConfig(cacheFileName, objs, localCacheTestPath,1)
                
                # 清空动画
                mc.currentTime(frameStart)
                animCurves = mc.ls(type='animCurve')
                mc.delete(animCurves)
                '''
            else:
                #mc.warning(unicode('=====================【错误】 未发现Master控制器！！！】=====================', "utf8"))
                mc.warning(u'=====================【错误】 未发现Master控制器！！！】=====================')
                 
        else:
            #mc.warning(unicode('=====================【！！！请先处理所有错误命名！！！】=====================', "utf8"))
            mc.warning(u'=====================【！！！请先处理所有错误命名！！！】=====================')
             
    '''
    【通用：cache测试管理】
    0.仅在texture阶段使用
    1.cache测试
    Author: 沈  康
    Data    :2013_12_18
    '''
    # txcache
    def checkCacheTxTest(self):
        import os
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        # 判断是否tx文件
        if 'tx.' in shotInfo[3]:
            txFileName = mc.file( exn = 1 , q = 1 )
            # 寻找服务器端rg文件
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            assetType = ''
            if shotInfo[1][0] == 'c':
                assetType = 'characters'
            if shotInfo[1][0] == 'p':
                assetType = 'props'

            if assetType:
                needFolder = '/rigging/'
                fileKeyInfo = shotInfo[0] + '_' + str(shotInfo[1]) + '_' + str(shotInfo[2]) +'_rg.m'
                assetServerPath = serverPath + 'scenes/' + assetType + '/' + str(shotInfo[1]) + needFolder

                if os.path.exists(assetServerPath):
                    # 获取文件名
                    assetFiles = mc.getFileList(folder = assetServerPath)
                    if assetFiles:
                        rgCheck = 0
                        for fileName in assetFiles:
                            if fileKeyInfo in fileName:
                                rgCheck = 1
                                # 打开rg文件
                                mc.file((assetServerPath + fileName) , open = 1 , force = 1)
                                # rg文件cache检测
                                # 获取控制器
                                ctrl = mc.ls('Master', type='transform') + mc.ls('Master_ct_an', type='transform') +mc.ls('master', type='transform') + mc.ls('master_ct_an', type='transform')
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
                                    mc.setKeyframe(v=0 , at='rotateY')
                                    # 最后一帧K帧
                                    mc.currentTime(frameEnd)
                                    mc.setKeyframe(v=50 , at='translateZ')
                                    mc.setKeyframe(v=360 , at='rotateY')
                                    mc.select(cl=1)
                    
                                    # 更新cache列表，测试rig用时不需要祛除隐藏物体
                                    self.checkCacheSetAdd()
                                    self.checkTransAnimSetAdd()
                                    cacheObjs = mc.sets('MESHES', q=1)
                                    animObjs = mc.sets('CTRLS', q=1)
                                    if cacheObjs:
                                        # 执行缓存创建,local,非ref模式
                                        # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                                        self.checkCacheSetCacheExport( cacheObjs , 0 , 0 ,0 ,0 )
                                        
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
                                                self.sk_checkBakeConstraints()
                                            
                                            self.checkAnimCurveInfoExport(animObjs,0)
                                    
                                        # 回到tx文件检测
                                        mc.file(txFileName, open = 1 , force = 1)
                                        
                                        # 清理历史
                                        mc.select(cacheObjs)
                                        mel.eval('DeleteAllHistory')
                                        
                                        # 导入cache
                                        self.checkCacheSetCacheImport( cacheObjs , 0 )
                                        
                                        # 导入anim信息
                                        if animObjs:
                                            self.checkAnimCurveInfoImport(0)
                                        
                                        print u'\n'
                                        print u'=====================Tx Cache创建完毕====================='
                                        print u'>>>>>请滑动时间轴，看所有用于渲染的物体是否有动'
                                        print u'>>>>>如果有部分或全部没动，请检查cache list和_ca_标记'
                                        print u'\n'
                                        
                                    else:
                                        # 回到tx文件检测
                                        mc.file(txFileName, open = 1 , force = 1)
                                        
                                        print u'\n'
                                        print u'=====================Tx Cache创建完毕====================='
                                        print u'>>>>>rg文件没有cache物体'
                                        print u'>>>>>请和rg确定，该asset rg文件是否cache测试正确'
                                        print u'\n'
                                else:
                                    # 回到tx文件检测
                                    mc.file(txFileName, open = 1 , force = 1)
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

    '''
    【通用：cache创建】
    0.仅在rig,texture及finallayout阶段使用
    1.需要添加log，以及加快效率
    Author: 沈  康
    Data    :2013_05_20
    '''

    # 执行创建cache
    def checkCacheDoCreate(self, fileName, objs, path , createType = 0 , cachePre = 0):
        # 标准设置
        cacheType = 'OneFilePerFrame'
        # cacheType = 'OneFile'
        cacheFormat = 'mcc'
        # 参数获取
        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        # 获取shape
        objsShape = []
        for obj in objs:
            # 需要进行甄别
            # 有输出的才有效；OG无效
            mesh = mc.listRelatives( obj ,pa=1,ni=1,s=1,type='mesh')
            if mesh:
                objsShape.append(mesh[0])
            
        # 本函数只创建，不连接
        if createType == 0:
            print '============'
            print frameStart+cachePre
            mc.cacheFile(f = fileName ,singleCache = 1,dir = path , st = (frameStart+cachePre) , et = frameEnd ,points = objsShape)
        
        # 创建并连接，比较慢
        if createType == 1:
            cacheType = 'OneFile'
            mc.select(objs)
            # doCreateGeometryCache 6 { "3", "1", "24", "OneFile", "1", "E:/TD_work/Data/test","0","","0", "add", "0", "1", "1","0","1","mcc","0" } ;
            # doCreateGeometryCache (版本号6) {(), (startFrame), (endFrame), (onFile), (), (path), (‘0‘),  (fileName) ,(‘0‘) ,('add'),(),('1'),('1'),('0').('1').('mcc'),'0'}
            # add后的参数为1时自动覆盖
            cacheCMD = 'doCreateGeometryCache 6 { "3", "%s", "%s", "%s", "1", "%s","0","%s","0", "add", "1", "1", "1","0","1","%s","0" }' % (str(frameStart + cachePre) , str(frameEnd) , cacheType, path , fileName , cacheFormat)
            mel.eval(cacheCMD)
            mc.select(cl = 1)
        
    # cache分割
    def checkCacheCreateConfig(self, fileName, objs, path , createType = 0 , cachePre = 0):
        # textLogPath = path + 'geoCache_log.txt'
        # 255判断，进行250分割
        lenObjs = len(objs)
        step = 250
        if lenObjs > step:
            objTemp = []
            if lenObjs % step == 0:
                grpNum = lenObjs / step
            else:
                grpNum = lenObjs / step + 1
            for i in range(grpNum):
                if i < grpNum :
                    objTemp = objs[i * step : (i + 1) * step]
                else:
                    objTemp = objs[i * 250:]
                fileNameTemp = fileName + '_' + str(i)
                self.checkCacheDoCreate(fileNameTemp , objTemp , path , createType ,cachePre)
        else:
            grpNum = 1
            self.checkCacheDoCreate(fileName , objs , path , createType,cachePre)

    '''
    【通用：经典/newType cache PYTHON版】
    0.通用
    Author: 
    Data    :2013_05_28
    '''

    # 传递v显示的动画，OK！！！
    # cache，需要开通GeoCache删写权限
    # 处理的分割情况
    # 加入上传服务器功能
    def checkCacheSetCacheExport(self, objsCache, serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
        if objsCache:
            # 获取时间轴
            frameStart = mc.playbackOptions(q=1, min=1) 
            frameEnd = mc.playbackOptions(q=1, max=1) 
            mc.playbackOptions(min=frameStart, max=frameEnd + 5)
            
            # 镜头信息
            import sk_infoConfig
            reload(sk_infoConfig)
            dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'

            # mel用path
            localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
            # local_animPath___python用转mel
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')
    
            # 服务器端Cache及Anim路径
            # server_cachePath___mel用
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            # server_animPath___python用转mel
            serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
     
 
            # 清理历史文件
            oldFiles = mc.getFileList(folder=localPathCache)
            for of in oldFiles:
                if of not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in of:
                    mc.sysFile((localPathCache + of), delete=1)

            # 获取cache物体
            # objsCache = self.checkCacheSetObjects()

            # 备份显示隐藏动画
            animVObjs = []
            hideObjs = []
            for obj in objsCache:
                animCurve = mc.listConnections((obj + '.v'), s=1, d=0)
                if animCurve:
                    animVObjs.append(obj)
                else:
                    if mc.getAttr(obj + '.v') != True:
                        hideObjs.append(obj)

            # 先处理有动画的
            if animVObjs:
                self.checkAnimCurveInfoExport(animVObjs, 0 , 'ca_animV')
            else:
                # 输出空信息
                self.checkAnimCurveInfoExport([], 0 , 'ca_animV')
            # 处理自身隐藏的
            if hideObjs:
                self.checkAnimCurveInfoExport(hideObjs, 0 , 'ca_hideV')
            else:
                # 输出空信息
                self.checkAnimCurveInfoExport([], 0, 'ca_hideV')
                
            
            # cachePath
            if serverFile:
                cachePath = serverPathCache
            else:
                cachePath = localPathCache
            
            # 清理目录内文件
            # 只清理txt和cache
            files = mc.getFileList(folder = cachePath , filespec = '*.mc') + mc.getFileList(folder = cachePath , filespec = '*.xml') + mc.getFileList(folder = cachePath , filespec = '*.txt')
            if files:
                for one in files:
                    if one not in ['assetReference.txt' , 'shotHideObjs.txt' , 'cacheObjVInfo.txt'] and '_anim_' not in one:
                        mc.sysFile( ( cachePath + one ) , delete = 1)
            print '\n'
            print u'=====================历史文件清理完毕====================='
            print '\n'
                

            # 备份材质
            #MatLists = self.checkCacheRecordMaterial()

            '''
            # NewType版cache处理,各种诡异问题，待定
            # 复制物体
            result = self.checkCacheObjectsSoftCopy(objsCache)
            copyObjs = result[0]
            objsCache = copyObjs
            
            '''
            # 经典版本cache处理
            mc.select(objsCache)
            # 删除已有的cache
            try:
                mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            except:
                pass
            mc.select(cl=1)

            # 经典版本cache处理
            print '\n'
            print u'=====================【cache】【经典模式】【开始创建】====================='
            print '\n'
            
            # 执行缓存创建
            if refMode == 0:
                lenObjs = len(objsCache)
                splitStep = 250
                if lenObjs > splitStep:
                    objTemp = []
                    if lenObjs % splitStep == 0:
                        grpNum = lenObjs / splitStep
                    else:
                        grpNum = lenObjs / splitStep + 1
                    for i in range(grpNum):
                        # 判断最后一位的范围
                        if i == (grpNum - 1):
                            objTemp = objsCache[i * splitStep:]
                        else:
                            objTemp = objsCache[i * splitStep : (i + 1) * splitStep]
                        self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath , createType ,cachePre)
                        # 输出分段物体信息
                        objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                        self.checkFileWrite(objPath, objTemp)
                    # 输出分段信息
                    cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                    self.checkFileWrite(cacheIndexPath, [str(grpNum)])
                else:
                    self.checkCacheDoCreate((fileName + '_0'), objsCache, cachePath,createType,cachePre)
                    # 输出分段物体信息
                    objPath = cachePath + 'cache_objs_0.txt'
                    self.checkFileWrite(objPath, objsCache)
                    # 输出分段信息
                    cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                    self.checkFileWrite(cacheIndexPath, '0')
            
            # 按namespace处理
            if refMode == 1:
                needCacheObjs = dict()
                for obj in objsCache:
                    nsInfo = needCacheObjs.keys()
                    ns = obj.split(':')[0]
                    if nsInfo == []:
                        if ns:
                            needCacheObjs[ns] = [obj]
                    else:
                        if ns in nsInfo:
                            needCacheObjs[ns].append(obj)
                        else:
                            needCacheObjs[ns] = [obj]
                nsInfo = needCacheObjs.keys()
                
                print '--------'
                print nsInfo

                if nsInfo:
                    for i in range(len(nsInfo)):
                        ns = nsInfo[i]
                        objTemp = needCacheObjs[ns]
                        print u'-------------------------'
                        print u'处理cache[%s]ing'%ns
                        print (fileName + '_' + str(i))
                        #print objTemp
                        #print cachePath
                        #print cachePre
                        # 创建cache
                        self.checkCacheDoCreate((fileName + '_' + str(i)), objTemp, cachePath,createType,cachePre)
                        # 输出分段物体信息
                        objPath = cachePath + 'cache_objs_' + str(i) + '.txt'
                        self.checkFileWrite(objPath, objTemp)
                        print u'处理cache[%s]完毕！'%ns
                    # 输出分段信息 , 不加[]给str(len(nsInfo))，会把str(len(nsInfo))处理成list，每个单位一个字符,如16为1,6
                    cacheIndexPath = cachePath + 'cache_objsIndex.txt'
                    self.checkFileWrite(cacheIndexPath, [str(len(nsInfo))])
            
            # 公用cache
            mel.eval('zwOptimizeGeoCache();')

            # 还原时间轴
            mc.playbackOptions(min=frameStart, max=frameEnd)
            
            # 还原材质
            #self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            #self.checkCacheBakeTexAniFiles()
            
            
            # 上传cache及animPath
            #if serverFile == 1:
            #    self.checkCacheLocalUpdate()
    
    # 处理上传
    def checkCacheLocalUpdate(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 本地Cache及Anim路径
        # local_cachePath___mel用
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        # local_animPath___python用转mel
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')

        # 服务器端Cache及Anim路径
        # server_cachePath___mel用
        serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        # server_animPath___python用转mel
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
        # cache上传
        cacheInfos = mc.getFileList(folder=localPathCache)
        
        for cacheInfo in cacheInfos:
            fileInfo = cacheInfo
            updateCacheCMD = 'zwSysFile "copy" ' + '"' + (localPathCache + fileInfo) + '"' + ' ' + '"' + (serverPathCache + fileInfo) + '"' + ' true'
            mel.eval(updateCacheCMD)
            print u'===[Updating Cache To Server]===传输[%s]完毕==='%fileInfo
            
        # anim上传
        fileInfo = 'ca_animV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_animV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        fileInfo = 'ca_hideV.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating Info To Server]===传输[%s]完毕==='%fileInfo
        
        print u'==============缓存及动画数据全部传输完毕=============='
    
    # 导入cache，还原V动画，yes!
    # 需要细看共享节点
    # 增加从服务器读取功能
    def checkCacheSetCacheImport(self, objsCache, serverFile=1):      
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)  
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        mc.playbackOptions(min=frameStart - 5, max=frameEnd + 5)
        
        # 镜头信息
        dirInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileName = dirInfo[0] + '_' + dirInfo[1] + '_' + dirInfo[2] + '_geoCache'
        
        # mel用path
        localPathCache = sk_infoConfig.sk_infoConfig().checkCacheLocalPath()
        # server端path
        if serverFile == 1:
            serverPathCache = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            localPathCache = serverPathCache
        
        if objsCache:
            # 备份材质
            MatLists = self.checkCacheRecordMaterial()
            
            # 经典版本cache处理
            # 删除已有的cache
            try:
                mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            except:
                pass
            
            # 导入cache
            # 查看分段信息
            cacheIndexPath = localPathCache + 'cache_objsIndex.txt'
            splitInfo = self.checkFileRead(cacheIndexPath)
            splitNum = int(splitInfo[0])
            if splitNum == 0:
                mc.select(cl=1)
                mc.select(objsCache)
                localCacheFile = localPathCache + fileName + '_0' + '.xml'
                melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                mel.eval(melCacheCMD)
                mc.select(cl=1)
            else:
                mc.select(cl=1)
                for num in range(splitNum):
                    cacheObjsPath = localPathCache + 'cache_objs_' + str(num) + '.txt'
                    objs = self.checkFileRead(cacheObjsPath)
                    mc.select(objs)
                    localCacheFile = localPathCache + fileName + '_' + str(num) + '.xml'
                    melCacheCMD = 'doImportCacheFile ' + '"' + localCacheFile + '"' + ' "xml" {} {};' 
                    print '-----'
                    print melCacheCMD
                    mel.eval(melCacheCMD)
                    mc.select(cl=1)

            # 还原v状态
            try:
                self.checkAnimCurveInfoImport(serverFile, 'ca_hideV')
            except:
                pass
            try:
                self.checkAnimCurveInfoImport(serverFile, 'ca_animV')
            except:
                pass

            # 公用cache
            mel.eval('zwOptimizeGeoCache();')
            
            # 打断所有连接
            #mel.eval('eyRenderRehyperShade')
            
            # 还原材质
            self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()

            # 上传cache
            
        # 还原时间轴
        mc.playbackOptions(min=frameStart, max=frameEnd)

    # 备份材质，不处理Set材质
    # 字典真爽/\ /\
    def checkCacheRecordMaterial(self, checkObjs = [] , finalLayout = 0 ,cacheMode = 1 ):
        SG = mc.ls(type='shadingEngine')
        # 选取模式
        if checkObjs:
            needSG = []
            errorObjs = []
            for obj in checkObjs:
                if mc.ls(obj) == []:
                    errorObjs.append(obj)
            if errorObjs:
                print u'------------------------以下物体不存在------------------------'
                for info in errorObjs:
                    print info
                print u'------------------------以上物体不存在------------------------'
                mc.error(u'------------------------请检测物体清单------------------------')
            else:
                for obj in checkObjs:
                    mesh = mc.listRelatives(obj,ni=1,type = 'mesh', s=1 ,f = 1)[0]
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
                MatLists[node] = connectObjsSG
        # finalLayout上传信息
        if finalLayout:
            self.checkCacheRecordMaterialExport(MatLists)
        return MatLists
        
    # 还原材质
    def checkCacheReturnMaterial(self, MatLists = [] ,finalLayout = 0):
        if finalLayout:
            MatLists = self.checkCacheRecordMaterialImport()
        keysSG = MatLists.keys()
        for key in keysSG:
            objs = MatLists[key]
            # 必须加objs，不然会断掉
            if objs:
                mc.sets(objs, forceElement = key)
                
    # 输出材质信息
    def checkCacheRecordMaterialExport(self,MatLists):
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        localPath = sk_infoConfig.sk_infoConfig().checkLocalInfoPath()
        localShaderInfoPath = localPath + 'finalLayoutTemp/' + str(shotInfo[0]) + '/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        SGKeys = MatLists.keys()
        allInfo = []
        for i in range(len(SGKeys)):
            if i == 0:
                allInfo = SGKeys + [u'********'] + MatLists[SGKeys[i]] + [u'--------']
            else:
                allInfo = allInfo  + MatLists[SGKeys[i]] + [u'--------']
        # 写
        fileInfo = 'ShotShaderInfo.txt'
        mc.sysFile(localShaderInfoPath, makeDir=True)
        self.checkFileWrite((localShaderInfoPath + fileInfo),allInfo)
        # 上传
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localShaderInfoPath + fileInfo) + '"' + ' ' + '"' + (serverDataPath + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'===[Updating ShotShaderInfo To Server]===传输[%s]完毕==='%fileInfo
            
    # 输出材质信息
    def checkCacheRecordMaterialImport(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        serverDataPath = serverPath + 'data/ShotShaderInfo/' + str(shotInfo[1]) + '/' + str(shotInfo[2]) + '/'
        fileInfo = 'ShotShaderInfo.txt'
        allInfo = self.checkFileRead(serverDataPath + fileInfo)
        # 分割点
        signKeyIndex = self.checkListSameAllIndex(allInfo,u'********')[0]
        signMeshSplitIndexList = self.checkListSameAllIndex(allInfo,u'--------')
        # 开始还原
        MatLists = dict({})
        # 创建keys
        for i in range(signKeyIndex):
            MatLists[allInfo[i]] = []
        # 每类创建
        for i in range(len(signMeshSplitIndexList)):
            if i == 0:
                meshNum = signMeshSplitIndexList[i] - signKeyIndex - 1
            else:
                meshNum = signMeshSplitIndexList[i] - signMeshSplitIndexList[i-1] - 1
            for j in range(meshNum):
                baseMeshIndex = signMeshSplitIndexList[i] - meshNum
                #print u'**********'
                #print len(allInfo)
                #print (baseMeshIndex + j)
                #print allInfo[baseMeshIndex + j]
                MatLists[allInfo[i]].append(allInfo[baseMeshIndex + j])
        return MatLists

    # bake表情贴图
    def checkCacheBakeTexAniFiles(self):
        # 获取时间轴
        frameStart = mc.playbackOptions(q=1, min=1) 
        frameEnd = mc.playbackOptions(q=1, max=1) 
        files = mc.ls(type='file')
        for f in files:
            cons = mc.listConnections(f + '.frameExtension')
            if cons:
                mc.bakeResults(f + '.frameExtension', sb=1, t=(frameStart, frameEnd))
    
    # 获取namespace
    def checkObjNamespace(self, obj):
        nmInfo = obj.split(':')
        namespace = ''
        for i in range(len(nmInfo) - 1):
            if i == 0:
                namespace = nmInfo[i]
            else:
                namespace = namespace + ':' + nmInfo[i]
        return namespace
    
    # 复制物体
    # 将顺序一一对应
    def checkCacheObjectsSoftCopy(self, objs):
        # 回到起始帧
        frameStart = mc.playbackOptions(q=1, min=1) 
        mc.currentTime(frameStart)
        # 全局变量
        geoCacheHighend_geoGroup = []
        geoCacheHighend_particleGroup = []
        # 开始创建grp及物体
        if mc.ls('Food_CacheTempGrp'):
            mc.delete('Food_CacheTempGrp')
        grp = mc.group(em=1, n='Food_CacheTempGrp')
        mc.select(cl=1)
        
        # objs = self.checkCacheSetObjects()
        copyObjs = []
        # 复制，进组，柔体
        for i in range(len(objs)):
            # 复制后namespace会消除，后面填上namespace
            # 利用执行复制命令后选取状态是复制后的物体获取复制后物体名
            mc.select(objs[i])
            mc.duplicate(rr=1)
            copyObj = mc.ls(sl=1, l=0)
            # 利用打组后选取物体状态不消失获取打组后物体名
            mc.parent(copyObj[0], grp)
            copyObj = mc.ls(sl=1, l=1)
            # 更新列表
            copyObjs.append(copyObj[0])
            # 创建柔体
            mc.select(copyObj[0])    
            softParticle = mc.soft(copyObj[0], c=1)
            # 设置柔体解算起始帧
            mc.setAttr((softParticle[0] + '.startFrame'), frameStart)
            # 存储变量方便传递
            geoCacheHighend_geoGroup.append(copyObj[0])
            geoCacheHighend_particleGroup.append(softParticle[0])
            # goal处理
            mc.goal(copyObj[0], g=objs[i], w=1, utr=0)
        result = []
        result.append(copyObjs)
        result.append(geoCacheHighend_geoGroup)
        result.append(geoCacheHighend_particleGroup)
        return result
    
    # 复制物体
    # 将顺序一一对应
    def checkCacheObjectsCopy(self, objs):
        # 回到起始帧
        frameStart = mc.playbackOptions(q=1, min=1) 
        mc.currentTime(frameStart)
        # 开始创建grp及物体
        if mc.ls('Cache_Grp'):
            mc.delete('Cache_Grp')
        grp = mc.group(em=1, n='Cache_Grp')
        mc.select(cl=1)
        
        # objs = self.checkCacheSetObjects()
        copyObjs = []
        # 复制，进组，柔体
        for i in range(len(objs)):
            # 复制后namespace会消除，后面填上namespace
            # 利用执行复制命令后选取状态是复制后的物体获取复制后物体名
            mc.select(objs[i])
            mc.duplicate(rr=1)
            copyObj = mc.ls(sl=1, l=0)
            # 利用打组后选取物体状态不消失获取打组后物体名
            mc.parent(copyObj[0], grp)
            copyObj = mc.ls(sl=1, l=0)
            # 添加到物体
            newName = copyObj[0] + 'dy_'
            mc.rename(copyObj[0], newName)
            copyObj[0] = newName
            copyObjs.append(copyObj[0])
        return copyObjs
    
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
                
    # 获取场景中所有AnimSet的物体
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def checkAnimSetObjects(self,otcGrp = 1):
        tempSet = mc.ls(type='objectSet')
        objsSet = []
        objsAnim = []
        for temp in tempSet:
            if 'CTRLS' in temp:
                objsSet.append(temp)
        if objsSet:
            for objSet in objsSet:
                ctrls = mc.sets(objSet, q=1)
                if ctrls:
                    for ctrl in ctrls:
                        # 排除otc组信息
                        if otcGrp == 1:
                            if 'OTC_GRP' not in mc.ls(ctrl,l=1)[0] and 'SET_GRP' not in mc.ls(ctrl,l=1)[0]:
                                print ctrl
                                objsAnim.append(ctrl)
        if objsAnim:
            print (u'[Anim  Object]    ' + str(len(objsAnim)))
        else:
            print (u'[Anim  Object]    0')
        return objsAnim
    
    '''
            【通用：约束烘焙工具】
    Author: 沈康
    Data    :2013_06_03
    '''
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def sk_checkBakeConstraints(self):
        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if  constraintsAll:
            tobake= []
            # 处理非参考的物体
            constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,d=0,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            print shape 
                            print obj
                            if mc.nodeType(shape[0]) != 'camera':
                                plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-1, mc.playbackOptions(q=1, maxTime=1)+1)

            # 处理参考的_ct_an物体
            constraintRefs = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
            for constraint in constraintRefs:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1,d = 0 ,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            if mc.nodeType(shape[0]) != 'camera':
                                if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                    plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (mc.playbackOptions(q=1, minTime=1)-10, mc.playbackOptions(q=1, maxTime=1)+10)

            tobake = list(set(tobake))
            
            # 改进版，不bake，而是给新locator bake
            if tobake:
                # 删除locators
                locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    mc.delete(locators)
                '''
                # 老赵bake脚本
                mc.select(tobake)
                mel.eval('source \"zzjUtilityTools\"')
                mel.eval('zzjUtilityTools \"bakeAnim\"')
                '''
                # 数值传递到locators
                locators = []
                constraintTemp = []
                for i in range(len(tobake)):
                    locTemp = mc.spaceLocator()
                    locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
                    cons = mc.parentConstraint(tobake[i] , locTemp)
                    constraintTemp.append(cons[0])
                    locators.append(locTemp)
                # 一次烘焙
                mc.bakeResults(locators,  t=io,
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
                mc.delete(constraintTemp)

                # 重新约束物体
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                #locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    for i in range(len(locators)):
                        # 打断t和r属性
                        for attr in attrs:
                            #mel.eval('CBdeleteConnection \"' + tobake[i] + attr + '\"')
                            self.checkDeleteConnection(tobake[i] + attr)
                        locatorGrp = locators[i]
                        #  父子约束 ,cam已经锁住
                        if 'cam_' not in tobake[i]:
                            print u'----------------'
                            print locatorGrp
                            print tobake[i].split('|')[-1]
                            # 位移检测
                            skipTranslateAxis = []
                            checkTAttr = ['.tx','.ty','.tz']
                            for j in range(3):
                                passAttr = ['x','y','z']
                                tState = mc.getAttr((tobake[i] + checkTAttr[j]),settable = 1)

                                if tState:
                                    pass
                                else:
                                    skipTranslateAxis.append(passAttr[j])
                            # 旋转检测
                            skipRotateAxis = []
                            checkRAttr = ['.rx','.ry','.rz']
                            for k in range(3):
                                passAttr = ['x','y','z']
                                rState = mc.getAttr((tobake[i] + checkRAttr[k]),settable = 1)
                                if rState:
                                    pass
                                else:
                                    skipRotateAxis.append(passAttr[k])
                            # 父子约束
                            if skipTranslateAxis and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis)
                            if skipTranslateAxis == [] and skipRotateAxis:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipRotate = skipRotateAxis)
                            if skipTranslateAxis and skipRotateAxis:
                                print '------'
                                print locatorGrp
                                print tobake[i]
                                # 修正全忽略的问题，全部忽略再去创建约束会报错
                                if (skipTranslateAxis == ['x','y','z']) and (skipRotateAxis == ['x','y','z']):
                                    pass
                                else:
                                    mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                        
                            if skipTranslateAxis == [] and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i])

                    # 二次烘焙
                    mc.bakeResults(tobake,    t=io,
                            simulation=1,
                            sampleBy=1,
                            disableImplicitControl=1,
                            preserveOutsideKeys=1,
                            sparseAnimCurveBake=1,
                            removeBakedAttributeFromLayer=0,
                            bakeOnOverrideLayer=0,
                            controlPoints=0,
                            shape=1)

                    # 删除约束
                    constraintConfigs = [x for x in (constraints + constraintRefs) if not mc.referenceQuery(x,inr=1)]
                    for cons in constraintConfigs:
                        ref = mc.referenceQuery(cons,isNodeReferenced = 1)
                        if not ref:
                            mc.delete(cons)

                    # 删除locators
                    mc.delete(locators)

                    print(u'\n========================【约束】【烘焙】【成功】========================')
                    print u'\n'
        else:
            print(u'\n========================【约束】【烘焙】【失败】========================')
            print u'\n'
            
    # 完全断开指定属性
    def checkDeleteConnection(self , attr ):
        # 被输入方
        if mc.connectionInfo(attr , isDestination = 1):
            destination = mc.connectionInfo(attr , getExactDestination = 1)
            srcConn = mc.listConnections(destination, s = 1, d = 0 , type = 'character')
            if srcConn:
                # 断开
                mc.character(destination , e = 1 ,rm = srcConn[0])
            
            sArr = mc.ls(destination , ro = 1)
            if sArr:
                src = mc.connectionInfo(destination , sourceFromDestination = 1)
                if src:
                    mc.disconnectAttr(src , destination)
            else:
                mc.delete(destination , icn = 1)
    '''
    anim传递版FinalLayout处理
    
    '''
    # 算法不好。。很多时候动画是有中间媒介的，最好控制器set组
    # 注意 mute！！！！
    def checkAnimCurveObjs(self):
        animCurveInfos = mc.ls(type = 'animCurve')
        needObjs = []
        for info in animCurveInfos:
            if 'CAM:' not in info:
                needObj = info [:-1*(1 + len(info.split('_')[-1]))]
                if mc.objExists(needObj):
                    needObjs.append(needObj)
                else:
                    needObj = mc.listConnections(info,d =1 )[0]
                    needObjs.append(needObj)
        needObjs = list(set(needObjs))
        return needObjs
    
    '''
            【通 用】处理文件中的显示隐藏
            专用cache流程
    '''
    # 处理数据，并输出
    def checkCacheVStateExport(self , cacheObjs ):
        if cacheObjs:
            # 获取时间轴
            startFrame  =   mc.playbackOptions(min=1,q = 1)
            endFrame    =   mc.playbackOptions(max=1,q = 1)
            # 数据创建
            vData = dict()
            for checkObj in cacheObjs:
                vData[checkObj] = []
            # 即时更新
            for i in range(int(endFrame - startFrame + 1)):
                frameNow = int(startFrame + i)
                mc.currentTime(frameNow)
                for checkObj in cacheObjs:
                    # 处理vState
                    vState = self.checkObjVState(checkObj)
                    if vState:
                        needInfo = [1 , frameNow]
                    else:
                        needInfo = [0 , frameNow]
                    # 处理记录与否
                    if vData[checkObj] == []:
                        vData[checkObj].append(needInfo)
                    else:
                        # 不同的数据则记录
                        if vData[checkObj][-1][0] != vState:
                            vData[checkObj].append(needInfo)
            # 进一步处理数据,处理成list
            resultData = []
            for checkObj in cacheObjs:
                resultData.append([checkObj,vData[checkObj]])
            # 输出服务器端
            import sk_infoConfig
            ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            
            self.checkFileWrite((ObjsVDataServerPath +  'cacheObjVInfo.txt'), resultData)
            return  resultData
        
    # v信息导入
    def checkCacheVStateImport(self):
        vData = self.checkObjsVData()
        if vData:
            cacheObjs = vData.keys()
            for cacheObj in cacheObjs:
                keyInfo = vData[cacheObj]
                #print '-----'
                #print len(keyInfo)
                #print keyInfo
                # 单帧
                if len(keyInfo) == 1:
                    vState = keyInfo[0][0]
                    mc.setAttr((cacheObj + '.v'),vState)
                # 多帧
                else:
                    for i in range(len(keyInfo)):
                        vState = keyInfo[i][0]
                        frame = keyInfo[i][1]
                        #print vState
                        #print frame
                        mc.currentTime(frame)
                        mc.setAttr((cacheObj + '.v'),vState)
                        mc.setKeyframe((cacheObj + '.v'))

    # vData数据处理
    def checkObjsVData(self):
        import sk_infoConfig
        ObjsVDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        resultData = self.checkFileRead(ObjsVDataServerPath +  'cacheObjVInfo.txt')
        vData = dict()
        import os
        if os.path.exists(ObjsVDataServerPath +  'cacheObjVInfo.txt'):
            for lineInfo in resultData:
                # obj
                obj = lineInfo.split(', ')[0][3:-1]
                vData[obj] = []
                # frameList
                frameList = lineInfo.split('\', ')[-1]
                # 单帧情况
                if '], ' not in frameList:
                    frameInfo = frameList.split(', ')
                    vState = frameInfo[0][2:]
                    frame = frameInfo[-1][:-3]
                    vData[obj].append([int(vState),int(frame)])
                # 多帧情况
                else:
                    allInfos = frameList.split('], ')
                    needInfo = []
                    for i in range(len(allInfos)):
                        frameInfo = allInfos[i].split(', ')
                        vState = frameInfo[0][1:]
                        frame = frameInfo[-1][:]
                        if i == 0:
                            vState = frameInfo[0][2:]
                        if i == (len(allInfos) - 1):
                            frame = frameInfo[-1][:-3]
                        needInfo.append([int(vState),int(frame)])
                    vData[obj] = needInfo
        return vData

    '''
    【通用：FinalLayout环节工具】
    0.anim文件专用
    Author: 沈康
    Data    :2013_06_03
    '''
    # cache最好先本地使用，最后upload并更新cache路径
    # anim可直接upload至服务器
    # 需要增加每个角色创建cache的功能
    # 新增功能：但凡cache物体和anim物体，只要其属于OTC_GRP,一概不参与cache和anim记录
    # template模式下，强制换anim参考，不处理帧信息，不导入相机，只输出cache到服务器端，不check in到服务器
    def checkFinalLayoutPerform(self , server = 1 , viewCheck = 0 , cachePre = -20 ):
        import sk_sceneConfig
        reload(sk_sceneConfig)
        import sk_infoConfig
        reload(sk_infoConfig)
        import sk_hbExceptCam
        reload(sk_hbExceptCam)
        import sk_referenceConfig
        reload(sk_referenceConfig)
        import os

        # 处理非参考的namespace
        sk_sceneConfig.sk_sceneConfig().sk_sceneNoRefNamespaceClean()
        print u'\n====================多层namespace清理完毕====================\n'
        
        # 清理无用ref
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            for i in range(len(refNodes)):
                removePaths = ['//file-cluster/GDC/Projects/ZoomWhiteDolphin/Project/data/ClusterCache/Splash_Base/Splash_Above_I/zm_ef_SplashIn_Above_l_c001.mb']
                removePaths = ['//file-cluster/GDC/Projects/ZoomWhiteDolphin/Project/data/ClusterCache/Splash_Base/Splash_Above_O/zm_ef_SplashOut_Above_l_c001.mb'] + removePaths
                if refPaths[i] in removePaths:
                    rerPath = mc.referenceQuery(refNodes[i],filename = 1)
                    mc.file(rerPath,removeReference = 1)
        

        # 检测参考是否正确，是否有render参考
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refPaths:
            errorAsset = []
            for i in range(len(refPaths)):
                refPath = refPaths[i]
                renderFilePath = refPath.replace('_anim.','_render.')
                if os.path.exists(renderFilePath):
                    pass
                else:
                    errorAsset.append(refNodes[i])
            if errorAsset:
                print u'-------------------以下render文件不存在-------------------'
                for info in errorAsset:
                    print info[:-2]
                print u'-------------------以上render文件不存在-------------------'
                print u'==================请先检查shot文件确定参考是否正确=================='
                print u'==================正确后请再和前期协商更新asset文件=================='
                mc.error(u'==================请和前期协商更新asset文件==================')
        else:
            print u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系=================='
            mc.error(u'==================shot文件没有参考下请先检查shot文件确定参考是否正确，请和动画联系==================')

        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfos[0])
        print u'\n'
        print(u'=====================【%s_%s】【FinalLayout】开始处理！！！====================='%(shotInfos[1],shotInfos[2]))
        print(u'=========================================================================')

        # 修正时间轴
        sk_sceneConfig.sk_sceneConfig().sk_sceneImportFrame('frame')
        
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath()
        # 获取finalLayout服务器端路径
        serverPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutServerPath()

        # 本地另存
        localFile = localPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3] + '_c001' + fileFormat
        mc.file(rename = localFile)
        mc.file(save=1,force = 1)
        
        if mc.ls('zwHeadsUpDisplay',type = 'expression'):
            mc.delete('zwHeadsUpDisplay')
            print u'\n'
            print u'====================【zwHeadsUpDisplay】清理完毕===================='
            print u'\n'

        sk_sceneConfig.sk_sceneConfig().sk_sceneUnloadRefDel(1,0)
        print u'\n'
        print u'========================未勾选参考清理完毕========================'
        print u'\n'

        # 初步清理垃圾节点
        self.checkDonotNodeClean(0)
        
        # 强制启动IK解算
        mc.ikSystem(e = 1,sol = 1)
        print u'\n'
        print u'=========================IK解算器强制更新========================'
        print u'\n'

        # 更新摄像机
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(shotInfos[0])
        camServerPath = '//file-cluster/GDC/Projects/' + projectInfo + '/Project/scenes/Animation/episode_' + shotInfos[1] + '/episode_camera/'
        camServerPath = camServerPath + shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_cam_baked.ma'
        if os.path.exists(camServerPath):
            pass
        else:
            if server:
                sk_sceneConfig.sk_sceneConfig().sk_sceneCameraUpdate(1)
                print u'\n'
                print u'==========================camera传输完毕=========================='
                print u'\n'

        # 预处理，约束清理
        self.sk_checkBakeConstraints()
        #print(u'========================【约束】【烘焙】【成功】========================')

        # 清理服务器端旧的SET和OTC文件
        sk_sceneConfig.sk_sceneConfig().sk_sceneGRPDelete('SET')
        sk_sceneConfig.sk_sceneConfig().sk_sceneGRPDelete('OTC')

        # 处理SET_GRP和OTC_GRP内的参考
        # 处理大组
        sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
        print u'\n'
        print u'==========================文件整理完毕=========================='
        print u'\n'
        
        unDisplayLayerObjs = []
        # 记录：shot文件非参考的隐藏的显示层的物体
        if server:
            displayLayers = mc.ls(type = 'displayLayer')
            if displayLayers:
                for layer in displayLayers:
                    isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                    if isRef == 0 and layer != 'defaultLayer':
                        viewState  = mc.getAttr(layer + '.visibility')
                        if viewState == False:
                            objs = mc.editDisplayLayerMembers( layer, query=True )
                            if objs:
                                unDisplayLayerObjs = unDisplayLayerObjs + objs
            hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            mc.sysFile(hideObjsServerPath,makeDir = 1)
            self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
            print u'\n'
            print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')
            print u'\n'

        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        rfnLv1 = refInfos[0][0]
        
        # 处理大组
        noNeedRefNodeInfo = []
        if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
            allGrps = []
            if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
            if mc.listRelatives('SET_GRP',ad = 1,f=1):
                allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
            if allGrps:
                for grp in allGrps:
                    if mc.referenceQuery(grp,isNodeReferenced = 1):
                        refNode = mc.referenceQuery(grp,referenceNode = 1)
                        noNeedRefNodeInfo.append(refNode)
                if noNeedRefNodeInfo:
                    noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
                    
        # 输出需要的角色和道具参考信息
        if server:
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
                    if refNode.split('_')[1][0] not in ['s', 'S']:
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        assetNeedOutputInfo.append(newPath)
                        assetNeedOutputInfo.append(ns)
            assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            mc.sysFile(assetNeedServerPath,makeDir = 1)
            self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
            print u'\n'
            print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
            print u'\n'

        # 在输出SET和OTC之前处理好anim中材质更改的情况
        # 诡异，这个居然会影响到新建文件的参考
        #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        
        # 导出SET_GRP和OTC_GRP文件
        sk_sceneConfig.sk_sceneConfig().sk_sceneGRPExport('SET')
        sk_sceneConfig.sk_sceneConfig().sk_sceneGRPExport('OTC')
        print u'\n'
        print(u'=====================【Group】【服务器端】【输出】完毕=====================')
        print u'\n'

        print u'\n-------------------------'
        print '[Ref Info]'
        print refInfos[0][0]
        print u'-------------------------'

        # 判断是否ms_anim文件
        if shotInfos[3] == 'an':
            # 首先删除set参考，加快速度
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            if refNodes:
                for ref in refNodes:
                    if not mc.ls(ref):
                        continue
                    if '_' not in ref:
                        continue
                    if ref.split('_')[1][0] in ['s', 'S']:
                        mc.file(rfn=ref, removeReference=1,f = 1)
            print u'\n'
            print(u'=====================【SET类参考】【清理】完毕=====================')
            print u'\n'

            # 输出cache 及 anim
            # 先输出anim
            animObjs = self.checkAnimSetObjects()
            self.checkAnimCurveInfoExport(animObjs, 1)
            #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
            print u'\n'
            print(u'=====================【Anim】【服务器端】【输出】完毕=====================')
            print u'\n'
            # 输出cache
            # 需要加入250分割处理
            # checkCacheSetObjects
            cacheObjs = self.checkCacheSetObjects()

            if cacheObjs:
                # 输出显示隐藏动画信息
                self.checkCacheVStateExport(cacheObjs)
                print u'\n'
                print(u'=====================【Cache】【V信息】【服务器端】【输出】完毕=====================')
                print u'\n'
                # 输出cache
                # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                print '-----'
                print len(cacheObjs)
                print server
                print cachePre
                self.checkCacheSetCacheExport(cacheObjs, server , cachePre ,1 ,0)
                if server:
                    print u'\n'
                    print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
                    print u'\n'
                else:
                    print u'\n'
                    print(u'=====================【Cache】【本地】【输出】完毕=====================')
                    print u'\n'
            else:
                print u'\n'
                print(u'=====================【Cache】无物体！！！！！！=====================')
                print u'\n'

            # 新建文件之前处理好SET_GRP文件 | 后面处理了 |此时处理避免备份时的崩溃
            sk_sceneConfig.sk_sceneConfig().sk_sceneSETRefShaderReset([shotInfos[0],shotInfos[1],shotInfos[2]])

            # 新建文件,临时文件夹另存
            mc.file(f=1, new=1)
            
            print '\n'
            print '[Ref Info]'
            print refInfos[0][0]
            print '\n'
            print(u'=========================【创建新文件】=========================')
            print '\n'
            
            # 准备先另存，因为update需要用到文件名
            #fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_base_lr_c001' + fileFormat
            fileName = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_base_fs_c001' + fileFormat
            # 本地文件
            localFile = localPath + fileName
            # 服务器端文件
            # serverFile = serverPath + fileName
            
            # 重命名
            mc.file( rename= localFile )
            mc.file(save = 1 ,force = 1)

            # 导入场景
            # 必须先导入OTC，后载入参考，否则容易出错(PORORO经验)
            # 导回SET_GRP和OTC_GRP
            sk_sceneConfig.sk_sceneConfig().sk_sceneGRPImport('SET')
            sk_sceneConfig.sk_sceneConfig().sk_sceneGRPImport('OTC')
            print u'\n'
            print(u'=====================【Group】【服务器端】【导入】完毕=====================')
            print u'\n'

            # 导入reference及share nodes（新导入场景，后导入参考）
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
                
            print '[Ref Info]'
            print refInfos[0][0]
            print '[NoNeedRef Info]'
            print noNeedRefNodeInfo
            # 导入参考，注意将_ms_anim替换成_ms_render
            # OTC内的参考不参与处理
            # shareNode只能对第一级reference处理。。。
            for i in range(len(rfnLv1)):
                ns = refInfos[2][0][i]
                refNode = refInfos[0][0][i]
                if noNeedRefNodeInfo:
                    if refNode not in noNeedRefNodeInfo:
                        # 应清理refNode及namespace
                        if mc.ls(refNode):
                            try:
                                mc.file(rfn=refNode , removeReference=1)
                            except:
                                mc.lockNode(refNode, l=0)
                                mc.delete(refNode)
                        # 清理namespace
                        try:
                            # 使得namespace成为空的namespace
                            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                            # 清理空namespace
                            mc.namespace(removeNamespace= (':' + ns))
                        except:
                            pass
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        # 此处加referenceNode，是必须的，因为部分文件里即便namespace一致但数字1在refNode顺序不一样
                        # 保证强行一致
                        # shareNodes和cache以及ref list edit有冲突？角色道具可以关闭，同时场景已经合并材质节点
                        # mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns , referenceNode = refNode )
                        mc.file(newPath, r=1, namespace = ns , referenceNode = refNode )
                        print u'\n'
                        print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                        print u'\n'
                else:
                    if refNode.split('_')[1][0] not in ['s', 'S']:
                        # 应清理refNode及namespace
                        if mc.ls(refNode):
                            try:
                                mc.file(rfn=refNode , removeReference=1)
                            except:
                                mc.lockNode(refNode, l=0)
                                mc.delete(refNode)
                        # 清理namespace
                        try:
                            # 使得namespace成为空的namespace
                            mc.namespace(force = 1 ,moveNamespace = [(':' + ns) , ':'])
                            # 清理空namespace
                            mc.namespace(removeNamespace= (':' + ns))
                        except:
                            pass
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        #mc.file(newPath, r=1, sharedNodes="shadingNetworks", namespace=ns)
                        mc.file(newPath, r=1, namespace = ns , referenceNode = refNode )
                        print u'\n'
                        print(u'=====================【创建参考】【%s】=====================' % (rfnLv1[i]))
                        print u'\n'


            # 导入cam
            # 导入相机
            sk_hbExceptCam.sk_hbExceptCam().camServerReference()
    
            # 处理大组
            sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(1)
            
            # 检测cache物体列表
            errorObjs = []
            for obj in cacheObjs:
                if mc.ls(obj) == []:
                    errorObjs.append(obj)
            if errorObjs:
                print u'-------------------以下物体不存在-------------------'
                for info in errorObjs:
                    print info
                print u'-------------------以上物体不存在-------------------'
                print u'=====================请通知前期检测anim和render版本cache list====================='
                mc.error(u'=====================请通知前期检测anim和render版本cache list=====================')
            
            # 强行备份材质
            if cacheObjs:
                MatLists = self.checkCacheRecordMaterial(cacheObjs,1)

            # 传递动画前bake约束一帧
            self.ly_BakeConstraints()                        
            # 载入anim
            self.checkAnimCurveInfoImport(1)
            print u'\n'
            print(u'=====================【Anim】【服务器端】【导入】完毕=====================')
            print u'\n'
            # 处理buging

            # 载入cache及自带的anim
            cacheObjs = self.checkCacheSetObjects()
            if cacheObjs:
                self.checkCacheSetCacheImport(cacheObjs, server)
                # 进行参考reload
                for i in range(len(rfnLv1)):
                    ns = refInfos[2][0][i]
                    refNode = refInfos[0][0][i]
                    if noNeedRefNodeInfo:
                        if refNode not in noNeedRefNodeInfo:
                            print u'================='
                            print refNode
                            print noNeedRefNodeInfo
                            print u'================='
                            newPath = mc.referenceQuery(refNode, filename=True)
                            #mc.file(newPath,loadReference=1)
                # 导入显示隐藏信息
                self.checkCacheVStateImport()
                if server:
                    print u'\n'
                    print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                    print u'\n'
                else:
                    print u'\n'
                    print(u'=====================【Cache】【本地】【导入】完毕=====================')
                    print u'\n'
            else:
                print u'\n'
                print(u'=====================【Cache】无物体！！！！！！！=====================')
                print u'\n'
            # 处理显示层相关物体
            if unDisplayLayerObjs:
                hideObjs = []
                for obj in unDisplayLayerObjs:
                    if mc.ls(obj):
                        hideObjs.append(obj)
                # 放到norender层
                if hideObjs:
                    if mc.ls('norender',type = 'displayLayer'):
                        pass
                    else:
                        mc.createDisplayLayer(empty = 1, name = 'norender')
                    mc.setAttr('norender.visibility',0)
                    mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
            print u'\n'
            print(u'=====================【Displayer】隐藏恢复=====================')
            print u'\n'
            
            # 本地保存
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            # 设置时间轴等消息
            # 命令
            shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2]
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
            # FPS
            if fpsFrame == 25:
                mc.currentUnit(time='pal')
            if fpsFrame == 24:
                mc.currentUnit(time='film')
            if fpsFrame == 30:
                mc.currentUnit(time='ntsc')
            # frame
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
            # 设置帧播放模式每帧
            mc.playbackOptions(playbackSpeed=0)
                
            # 允许undo
            mc.undoInfo(state=True, infinity=True)
            
            description = 'FinalLayout Base File'
            
            # 强行还原材质
            if cacheObjs:
                self.checkCacheReturnMaterial(MatLists)
            
            # 烘焙表情贴图
            self.checkCacheBakeTexAniFiles()
            
            # 处理camera视野
            if viewCheck:
                # 加载所有参考
                sk_sceneConfig.sk_sceneConfig().sk_sceneUnloadRefDel(0,1)
                import sk_camMatrixScene
                reload(sk_camMatrixScene)
                print '\n'
                print(u'=====================【Camera】【全自动检测视野】【开始】=====================')
                print '\n'
                # 记录显示层，默认全开启
                
                
                camName = 'CAM:cam_' + shotInfos[1] + '_' + shotInfos[2] + '_baked'
                if mc.ls(camName):
                    sk_camMatrixScene.sk_camMatrixScene().sk_sceneMeshCamConfig( startFrame, endFrame ,camName,[],8)
                else:
                    pass
                # 特殊处理大面积低密度类物体，如_sea_
                seaObj = mc.ls('*:*_sea_*',type = 'transform') + mc.ls('*_sea_*',type = 'transform')
                if seaObj:
                    for obj in seaObj:
                        mc.setAttr((obj+'.v'),1)
                        
                # 还原显示层        
                
                print '\n'
                print(u'=====================【Camera】【全自动检测视野】【成功】=====================')
                print '\n'
                description = 'FinalLayout Base File | View Sight Configed'
                
            mc.file(save=1, force = 1)
            
            # 重打开FL文件
            mc.file(localFile , open = 1, loadReferenceDepth = 'none' , force = 1)
            sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)

            # 处理cache环境变量
            self.checkCacheEnvPath()

            mc.file(save=1, force = 1)
            
            # 上传服务器处理
            if server == 1:
                #self.checkFinalLayoutUpdate()
                # 开始提交文件至服务器
                mc.file(save=1,force = 1)
                # 用户名
                userName = os.environ['USERNAME']
                newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(newInfo[0])
                fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                #print checkOutCmd
                mel.eval(checkOutCmd)
                # checkIn
                mel.eval('idmtProject -checkin -description \" ' + description + '\"')

            # 缺少check in baseFile
            print '\n'
            print(u'=========================================================================')
            print(u'=====================【%s_%s】【FinalLayout】处理完毕====================='%(shotInfos[1],shotInfos[2]))

            # 成功代码
            return 0

    # 处理FINALLAYOUT文件
    def sk_sceneFLRefShaderReset(self , info ):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        # 处理OTC的SET文件，但不载入参考
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
        fileGrpType = '_base_fs_c001'

        needFilePath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath() 
        needFsFile = needFilePath + info[0] + '_' + info[1] + '_' + info[2] + fileGrpType + fileFomat
        
        print needFsFile
        
        # 不加载参考导入
        mc.file(needFsFile , open = 1, loadReferenceDepth = 'none' , force = 1)
        # 处理好所有参考
        sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
        mc.file(save = 1, force = 1)

    # finalLayout上传服务器
    def checkFinalLayoutUpdate(self):
        # 记录项目，场次，镜头号
        # shotInfos = self.checkShotInfo()
        # 获取finalLayout临时路径
        # localPath = self.checkFinalLayoutLocalPath()
        # 获取finalLayout服务器端路径
        # serverPath = self.checkFinalLayoutServerPath()
        
        # 获取cacheSet物体
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            # 上传服务器
            self.checkCacheLocalUpdate()
            #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
            print(u'=====================【Cache】【服务器端】【输出】完毕=====================')

            # 删除cache
            #mc.select(cacheObjs)
            #try:
            #    mel.eval('deleteCacheFile 3 { "keep", "", "geometry" } ;')
            #except:
            #    pass

            # 更改路径
            #self.checkCacheSetCacheImport(cacheObjs, 1)
            #print(unicode('=====================【Cache】【服务器端】【导入】完毕=====================', "utf8"))
            #print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
        
        # 最后保存
        mc.file(save=1)
        # 上传finalLayout文件
        # fileInfo = fileName
        # updateFinalLayoutCMD = 'zwSysFile "copy" ' + '"' + (serverPath + fileInfo) + '"' + ' ' + '"' + (serverPath + fileInfo) + '"' + ' true'
        # mel.eval(updateFinalLayoutCMD)

    # 重新输出数据
    def checkFinalLayoutExport(self, grpExport = 0 , cacheExport = 0 , animExport = 0 , assetInfoExport = 0 , hideInfoExport = 0 ,server = 1 , cachePre = -50):
        if grpExport or cacheExport or animExport or assetInfoExport or hideInfoExport:
            import sk_sceneConfig
            reload(sk_sceneConfig)
            import sk_referenceConfig
            reload(sk_referenceConfig)
            import sk_infoConfig
            reload(sk_infoConfig)
            
            # info记录
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # 强制更新IK解算器
            mc.ikSystem(e = 1,sol = 1)
            
            # 预处理，约束清理
            if not hideInfoExport or not assetInfoExport:
                self.sk_checkBakeConstraints()

            # 获取references信息
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # 处理大组
            sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(server)
            
            # 在输出SET和OTC之前处理好anim中材质更改的情况
            # 这个会出错。。导致新参考材质挂掉
            #sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
            
            #导出SET和OTC
            if grpExport:
                # 清理旧的SET和OTC文件
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPDelete('SET')
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPDelete('OTC')
                # 导出SET_GRP和OTC_GRP文件
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPExport('SET')
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPExport('OTC')
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')
                
                # 新建文件之前处理好SET_GRP文件
                sk_sceneConfig.sk_sceneConfig().sk_sceneSETRefShaderReset([shotInfos[0],shotInfos[1],shotInfos[2]])
                print(u'=====================【Group】【服务器端】【输出】完毕=====================')

            # 输出assetInfo
            if assetInfoExport:
                # 处理大组
                noNeedRefNodeInfo = []
                if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
                    allGrps = []
                    if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                        allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
                    if mc.listRelatives('SET_GRP',ad = 1,f=1):
                        allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
                    if allGrps:
                        for grp in allGrps:
                            if mc.referenceQuery(grp,isNodeReferenced = 1):
                                refNode = mc.referenceQuery(grp,referenceNode = 1)
                                noNeedRefNodeInfo.append(refNode)
                        if noNeedRefNodeInfo:
                            noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
                # 处理asset
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
                        if refNode.split('_')[1][0] not in ['s', 'S']:
                            newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                            assetNeedOutputInfo.append(newPath)
                            assetNeedOutputInfo.append(ns)
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
                mc.sysFile(assetNeedServerPath,makeDir = 1)
                self.checkFileWrite((assetNeedServerPath +  'assetReference.txt'), assetNeedOutputInfo)
                print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')

            # 输出cache 及 anim
            if animExport:
                # 输出anim
                animObjs = self.checkAnimSetObjects()
                self.checkAnimCurveInfoExport(animObjs, server)
                #print(unicode('=====================【Anim】【服务器端】【输出】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【输出】完毕=====================')

            # 输出cache
            if cacheExport:
                # 需要加入250分割处理
                # checkCacheSetObjects
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    self.checkCacheVStateExport(cacheObjs)
                    # serverFile=1 , cachePre = 0 , refMode = 1 , createType = 0):
                    self.checkCacheSetCacheExport(cacheObjs, server , cachePre , 1, 0)
                    #print(unicode('=====================【Cache】【服务器端】【输出】完毕=====================', "utf8"))
                    print(u'=====================【Cache】【服务器端】【输出】完毕=====================')
                else:
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    
            # 输出hideInfo
            if hideInfoExport:
                # 记录：shot文件非参考的隐藏的显示层的物体
                unDisplayLayerObjs = []
                displayLayers = mc.ls(type = 'displayLayer')
                if displayLayers:
                    for layer in displayLayers:
                        isRef = mc.referenceQuery(layer, isNodeReferenced = 1)
                        if isRef == 0 and layer != 'defaultLayer':
                            viewState  = mc.getAttr(layer + '.visibility')
                            if viewState == False:
                                objs = mc.editDisplayLayerMembers( layer, query=True )
                                if objs:
                                    unDisplayLayerObjs = unDisplayLayerObjs + objs
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
                mc.sysFile(hideObjsServerPath,makeDir = 1)
                self.checkFileWrite((hideObjsServerPath +  'shotHideObjs.txt'), unDisplayLayerObjs)
                print(u'=====================【hideObjs】【服务器端】【输出】完毕=====================')

            # 成功代码
            return 0

    # 重新载入数据
    def checkFinalLayoutImport(self, grpImport = 0 , cacheImport = 0 , animImport = 0 , assetInfoImport = 0 ,  hideInfoImport= 0 ,server = 1):
        if grpImport or cacheImport or animImport or assetInfoImport or hideInfoImport:
            import sk_sceneConfig
            reload(sk_sceneConfig)
            import sk_infoConfig
            reload(sk_infoConfig)
            import sk_referenceConfig
            reload(sk_referenceConfig)
            import os
            
            # info记录
            shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
            # 处理大组
            sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(server)
            
            # 获取references信息
            refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
            
            # 首先处理好时间轴
            # FPS
            sk_sceneConfig.sk_sceneConfig().sk_sceneImportFrame('FPS')
            # frame
            sk_sceneConfig.sk_sceneConfig().sk_sceneImportFrame('frame')
            
            #导入SET和OTC
            if grpImport:
                # 清除SET_GRP和OTC的参考
                # 目前通过namespace获取物体判断是否在两个组内
                refNode = refInfos[0][0]
                #refPathInfo = refInfos[1][0]
                refNsInfo = refInfos[2][0]
                for i in range(len(refNsInfo)):
                    mc.namespace(setNamespace = (  ':' + refNsInfo[i]))
                    objs = mc.namespaceInfo(ls= 1,dagPath =1 )
                    mc.namespace(setNamespace = ':')
                    if objs:
                        needObj = ''
                        for obj in objs:
                            if obj[-1] == '_' and mc.listRelatives(obj, c= 1,type = 'mesh'):
                                needObj = obj
                                break
                        if needObj:
                            objLong = mc.ls(needObj,l=1)[0]
                            # 判断是否在两个组
                            if 'SET_GRP' in objLong or 'OTC_GRP' in objLong:
                                print objLong
                                print refNode[i]
                                # 执行删除参考
                                mc.file(rfn = refNode[i] , removeReference = 1)
                    print(u'=====================【Group】【原参考】【清理】完毕=====================')
                # 删除SET_GRP和OTC_GRP
                if mc.ls('SET_GRP'):
                    mc.delete('SET_GRP')
                if mc.ls('OTC_GRP'):
                    mc.delete('OTC_GRP')
                # 导回SET_GRP和OTC_GRP
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPImport('SET')
                sk_sceneConfig.sk_sceneConfig().sk_sceneGRPImport('OTC')
                print(u'=====================【Group】【服务器端】【导入】完毕=====================')
            
            # 创建asset
            if assetInfoImport:
                assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
                if os.path.exists(assetNeedServerPath +  'assetReference.txt'):
                    assetNeedOutputInfo = self.checkFileRead((assetNeedServerPath +  'assetReference.txt'))
                    if assetNeedOutputInfo:
                        for i in range(len(assetNeedOutputInfo)/2):
                            newPath = assetNeedOutputInfo[i*2]
                            ns = assetNeedOutputInfo[i*2 + 1]
                            mc.file(newPath, r=1, namespace= ns , referenceNode = (ns + 'RN') )
                            print u'\n'
                            print(u'=====================【创建参考】【%s】=====================' % (ns))
                            print u'\n'
                else:
                    print u'\n'
                    print(u'=====================【server缺少】【%s】请重新【输出】=====================' % ('assetInfo'))
                    print u'\n'
                
            # 载入anim
            if animImport:
                #animObjs = self.checkAnimSetObjects()
                self.checkAnimCurveInfoImport(server)
                #print(unicode('=====================【Anim】【服务器端】【导入】完毕=====================', "utf8"))
                print(u'=====================【Anim】【服务器端】【导入】完毕=====================')

            # 输入cache
            if cacheImport:
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    #self.checkCacheSetCacheImport(cacheObjs, server)
                    self.sk_flCacheImportRefreshShaders(server)
                    # 导入显示隐藏信息
                    self.checkCacheVStateImport()
                    #print(unicode('=====================【Cache】【服务器端】【导入】完毕=====================', "utf8"))
                    print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                else:
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    
            # 载入hideInfo
            if hideInfoImport :
                hideObjsServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
                unDisplayLayerObjs = self.checkFileRead((hideObjsServerPath +  'shotHideObjs.txt'))
                if unDisplayLayerObjs:
                    hideObjs = []
                    for obj in unDisplayLayerObjs:
                        if mc.ls(obj):
                            hideObjs.append(obj)
                    # 放到norender层
                    if hideObjs:
                        if mc.ls('norender',type = 'displayLayer'):
                            pass
                        else:
                            mc.createDisplayLayer(empty = 1, name = 'norender')
                        mc.setAttr('norender.visibility',0)
                        mc.editDisplayLayerMembers('norender',hideObjs , nr = 1)
                        print u'\n'
                        print(u'=====================【Displayer】隐藏恢复=====================')
                        print u'\n'
    
    # asset信息输出
    # needType : 0 需要所有asset，chr,prop,set 标准信息 |  1 只要chr ,prop
    def sk_assetInfoUpdate(self,reorganize = [0,0],needType = 1):
        from idmt.maya.py_common import sk_sceneConfig
        reload(sk_sceneConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon  import sk_infoConfig
        reload(sk_infoConfig)
        
        # 获取references信息
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()

        assetNeedOutputInfo = []    
        rfnLv1 = refInfos[0][0]
        rfnPathLv1 = refInfos[1][0]
        
        # 只要reference标准信息
        if needType == 0:
            txtName = 'assetAllReference.txt'
            for i in range(len(rfnLv1)):
                if '/master/' in rfnPathLv1[i]:
                    refAsset = rfnPathLv1[i].split('/master/')[0].split('/')[-1]
                    newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                    assetNeedOutputInfo.append(newPath)
                    assetNeedOutputInfo.append(refAsset)
        
        # 只要非VFX_GRP和SET_GEP的chr 和 prop
        if needType == 1:
            txtName = 'assetReference.txt'
            # 处理大组
            if reorganize[0]:
                sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(reorganize[1])

            # 处理大组
            noNeedRefNodeInfo = []
            if mc.ls('OTC_GRP') and mc.ls('SET_GRP'):
                allGrps = []
                if mc.listRelatives('OTC_GRP',ad = 1,f=1):
                    allGrps = allGrps +  mc.listRelatives('OTC_GRP',ad = 1,f=1)
                if mc.listRelatives('SET_GRP',ad = 1,f=1):
                    allGrps = allGrps + mc.listRelatives('SET_GRP',ad = 1,f=1)
                if allGrps:
                    for grp in allGrps:
                        if mc.referenceQuery(grp,isNodeReferenced = 1):
                            refNode = mc.referenceQuery(grp,referenceNode = 1)
                            noNeedRefNodeInfo.append(refNode)
                    if noNeedRefNodeInfo:
                        noNeedRefNodeInfo = list(set(noNeedRefNodeInfo))
            # 输出数据
            for i in range(len(rfnLv1)):
                ns = refInfos[2][0][i]
                refNode = refInfos[0][0][i]
                if noNeedRefNodeInfo:
                    if refNode not in noNeedRefNodeInfo:
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        assetNeedOutputInfo.append(newPath)
                        assetNeedOutputInfo.append(ns)
                else:
                    if refNode.split('_')[1][0] not in ['s', 'S']:
                        newPath = rfnPathLv1[i].replace('_ms_anim', '_ms_render')
                        assetNeedOutputInfo.append(newPath)
                        assetNeedOutputInfo.append(ns)

        assetLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(2)
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if shotInfos[0]=='csl':
            assetLocalPath = sk_infoConfig.sk_infoConfig().checkCacheLocalPath(3)
        assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        if shotInfos[0]=='csl':
            assetNeedServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(shotType = 3)        
        print assetNeedServerPath
        print txtName
        # 写
        self.checkFileWrite((assetLocalPath +  txtName), assetNeedOutputInfo)
        # 传递
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (assetLocalPath + txtName) + '"' + ' ' + '"' + (assetNeedServerPath + txtName) + '"' + ' true'
        mel.eval(updateAnimCMD)
        print u'\n'
        print(u'=====================【assetInfo】【服务器端】【输出】完毕=====================')
        print u'\n'
    
    
    # fl文件处理cache并保持更新材质
    def sk_flCacheImportRefreshShaders(self,server):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneConfig
        reload(sk_sceneConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            needIds = []
            for i in range(len(refNodes)):
                if 'CAM' not in refNodes[i]:
                    if refNodes[i].split('_')[1][0] in ['c','p']:
                        needIds.append(i)
            if needIds:
                # unload参考 ,cleanUp ,load参考
                for num in needIds:
                    mc.file(rfn=refNodes[num] , unloadReference=1)
                    mc.file(rfn=refNodes[num], cleanReference = refNodes[num])
                    mc.file(rfn=refNodes[num] , loadReference=1)
                # 导入cache
                cacheObjs = self.checkCacheSetObjects()
                if cacheObjs:
                    self.checkCacheSetCacheImport(cacheObjs, server)
                    if server:
                        print u'\n'
                        print(u'=====================【Cache】【服务器端】【导入】完毕=====================')
                        print u'\n'
                    else:
                        print u'\n'
                        print(u'=====================【Cache】【本地】【导入】完毕=====================')
                        print u'\n'
                else:
                    print u'\n'
                    print(u'=====================【Cache】无物体！！！！！！！=====================')
                    print u'\n'
                # 处理参考编辑列表
                for num in needIds:
                    mc.file(rfn=refNodes[num] , unloadReference=1)
                #  清理
                sk_referenceConfig.sk_referenceConfig().checkReferenceShaderReset(1)
                # load
                for num in needIds:
                    mc.file(rfn=refNodes[num] , loadReference=1)
                # 整理
                sk_sceneConfig.sk_sceneConfig().sk_sceneReorganize(0)
    
    # 非anim转anim
    def sk_zmNotAnim2Anim(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
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
                
    '''
    【通用：自动生成animModel及masterMode】
    0.仅在texture阶段使用
    Author: 沈  康
    Data    :2013_05_20 - 2013_05_
    '''
    # 中后期，rg生成anim
    # 主函数，处理切换
    def checkTexTransformtMo(self, checkIn=0, backTx=1):
        # 用户名
        import os
        userName = os.environ['USERNAME']
        # 项目名
        import sk_infoConfig
        reload(sk_infoConfig)
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        projectInfo = sk_infoConfig.sk_infoConfig().checkProjectNameSimple2Full(info[0])
        # 改成复制到本地
        # 是否本地文件判断
        # path = self.checkPCFilePath()
        # 另存到temp文件夹
        pathLocal = self.checkTX2AnimRenderLocalPath()
        fileLocal = pathLocal + mc.file(sceneName=1, q=1).split('/')[-1]
        mc.file(rename=fileLocal)
        mc.file(save=1 , force = 1)
        # 加入错误检测
        errors=''
        if info[1][0] != 'm' :
            errors = self.checkModelDetailsWarning()
        else:
             errors=0                                   
        if errors == 0:
            # 仅允许tx阶段使用
            # 先输出smoothSet信息
            self.checkAssetSmoothSetUpdate()
            # 处理文件内ca模型渲染开启属性
            self.checkCaheObjRenderState()
            # info = self.checkShotInfo()
            fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(info[0])
            fileName = mc.file(query=1, exn=1)
            # rootGrp检测
            rootGrp = self.checkOutlinerGroup()[0]
            if info[3].split('.')[0] == 'tx'and 'MODEL' not in rootGrp:
                # 检测 材质着色
                self.checkTextureModelShader()
                # 【规定】有an的，保留MODEL组；没an的，保留MODEL组并清历史
                # 角色类全cache处理
                # 对道具类可能存在的超大型物体，部分cache部分anim，根据情况处理
                if info[1][0] not in ['s', 'S'] and info[1][0] != 'm' :
                    # set检测
                    setType = self.checkSetsType()
                    # setType 有4种情况 [0,0];[0,1];[1,0];[1,1]
                    # 无_ct_an标记的cache文件
                    if setType == [1,0]:
                        for i in range(2):
                            mc.file(fileName, force=1, options="v=0", type=fileTypeFull , open=1)
                            # 转 animModel
                            if i == 0:
                                pass
                                '''
                                self.checkTexNoAC2AnimMo('anim')
                                if checkIn == 1:
                                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                                    # checkOut
                                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
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
                                # self.checkTexMo2CacheMoNewType()
                                self.checkTexMo2CacheMo()
                                if checkIn == 1:
                                    print(unicode('=====================[Check in] Start=====================', "utf8"))
                                    # checkOut
                                    newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                                    fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                                    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                                    #print checkOutCmd
                                    mel.eval(checkOutCmd)
                                    # checkIn
                                    mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                                #print(unicode('=====================创建【RenderFile】完毕=====================', "utf8"))
                                print(u'=====================创建【RenderFile】完毕=====================')
                    # 有an的文件，以及什么都无的文件
                    if setType[1] == 1 or setType == [0,0]:
                        '''
                        # 另存anim
                        mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                        self.checkTexNoAC2AnimMo('anim')
                        if checkIn == 1:
                            print(unicode('=====================[Check in] Start=====================', "utf8"))
                            # checkOut
                            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
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
                        mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                        self.checkTexNoAC2AnimMo('render')
                        if checkIn == 1:
                            print(unicode('=====================[Check in] Start=====================', "utf8"))
                            # checkOut
                            newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                            fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                            checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                            #print checkOutCmd
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
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                    self.checkTexNoAC2AnimMo('anim')
                    if checkIn == 1:
                        print(unicode('=====================[Check in] Start=====================', "utf8"))
                        # checkOut
                        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        #print checkOutCmd
                        mel.eval(checkOutCmd)
                        # checkIn
                        mel.eval('idmtProject -checkin -description \"Creted By TX File\"')
                    #print(unicode('=========【非cache文件，直接输出anim文件。复制到render文件】=========', "utf8"))
                    print(u'=========【Set_Asset，直接输出anim文件。复制到render文件】=========')
                    #print(unicode('=====================创建【AnimFile】完毕=====================', "utf8"))
                    print(u'=====================创建【AnimFile】完毕=====================')

                    # 另存render
                    mc.file(fileName, force=1, options="v=0", type=fileTypeFull  , open=1)
                    self.checkTexNoAC2AnimMo('render')
                    if checkIn == 1:
                        print(unicode('=====================[Check in] Start=====================', "utf8"))
                        # checkOut
                        newInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
                        fileInfo = '1|' + projectInfo + '|' + newInfo[0] + '_' + newInfo[1] + '_' + newInfo[2] + '_' + newInfo[3] + '_' + newInfo[4] + '|' + userName
                        checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
                        #print checkOutCmd
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
                    mc.file(fileName, force=1, options="v=0" , type=fileTypeFull , open=1)
                #print(unicode('=====================【返回 tx 文件】=====================', "utf8"))
                print(u'=====================【返回 tx 文件】=====================')
            else:
                # 要报错处理,check in 用
                #print(unicode('=====================【！！！您所用的不是【tx】阶段文件！！！】=====================', "utf8"))
                print(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')
                #print(unicode('=====================【！！！【tx】【MODEL】处于第二层！！！】=====================', "utf8"))
                print(u'=====================【！！！【tx】【MODEL】处于第二层！！！】=====================')
                #mc.error(unicode('=====================【！！！您所用的不是【tx】阶段文件！！！】=====================', "utf8")) 
                print(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')
                mc.error(u'=====================【！！！您所用的不是【tx】阶段文件！！！】=====================')
                
        else:
            # 要报错处理，check in用
            #print(unicode('=====================【！！！请先处理所有错误命名！！！】=====================', "utf8"))
            print(u'=====================【！！！请先处理所有错误命名！！！】=====================')
            #mc.error(unicode('=====================【！！！请先处理所有错误命名！！！】=====================', "utf8"))
            mc.error(u'=====================【！！！请先处理所有错误命名！！！】=====================')
    
    # tx check in shader
    # tx文件测试，所有模型重新赋予材质，失败则报错
    def checkTextureModelShader(self):
        meshes = mc.ls(type = 'mesh',l = 1)
        if meshes:
            # 创建新渲染层
            if mc.ls('food_shaderLayer_test'):
                mc.delete('food_shaderLayer_test')
            # 获取MODEL下的
            needObjs = []
            for mesh in meshes:
                if '|MODEL|' in mesh:
                    needObjs.append(mc.listRelatives(mesh,p=1,f=1)[0])
            needObjs = list(set(needObjs))
            # 创建层
            if needObjs:
                errorObjs = []
                mc.createRenderLayer(needObjs , name='food_shaderLayer_test' , noRecurse=1 , makeCurrent=1)
                # 创建材质
                shaderMain = mc.shadingNode ('lambert', asShader=True, name= 'food_shader_test')  
                shaderMianSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= 'food_shader_test_SG')
                mc.connectAttr((shaderMain + '.outColor'), (shaderMianSG + '.surfaceShader'))
                for obj in needObjs:
                    mesh = mc.listRelatives(obj,ni=1,s=1)[0]
                    #print u'-------------'
                    #print mesh
                    try:
                        mc.sets(obj, e=1, forceElement= shaderMianSG )
                    except:
                        errorObjs.append(mesh)
                
                if errorObjs:
                    for errorObj in errorObjs:
                        print u'-------------'
                        print errorObj
                        print errorObj.split('|')[-1]
                    print(u'>>>>>>------------以上mesh无法正常赋予材质，请回到原tx文件进行处理！！！')
                    mc.error(u'>>>>>>------------以上mesh无法正常赋予材质，请回到原tx文件进行处理！！！')
                # 删除层，清理垃圾节点
                # Back To MasterLayer
                mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
                mc.delete('food_shaderLayer_test')
                #mel.eval('MLdeleteUnused')
    
    # 强行将所有SG和shader打断，并重新连接
    def checkShaderSGReConnection(self):
        # 获取有效的mesh及shader及SG节点
        SGNodes = mc.ls(type = 'shadingEngine')
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
                    if mc.listConnections((sgNode + '.surfaceShader'),source = 1 , plugs = 1):
                        shaderAttr = mc.listConnections((sgNode + '.surfaceShader'),source = 1,plugs = 1)[0]
                    if mc.listConnections(sgNode,source = 1 , type = 'mesh'):
                        meshes = mc.listConnections(sgNode,source = 1 , type = 'mesh')
                    if shaderAttr and meshes:
                        # 删除SG节点
                        mc.delete(sgNode)
                        # 重连物体
                        newSGNode = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= (sgNode ))
                        mc.connectAttr((shaderAttr), (newSGNode + '.surfaceShader'))
                        mc.sets( meshes, e=1, forceElement= newSGNode )


    # 将所有用于渲染的模型render state开启
    def checkCaheObjRenderState(self):
        cacheObjs = self.checkCacheSetObjects()
        if cacheObjs:
            for obj in cacheObjs:
                shape = mc.listRelatives(obj ,c= 1,type ='mesh',f = 1)
                if shape:
                    mc.setAttr((shape[0] + '.castsShadows'),1)
                    mc.setAttr((shape[0] + '.receiveShadows'),1)
                    mc.setAttr((shape[0] + '.motionBlur'),1)
                    mc.setAttr((shape[0] + '.primaryVisibility'),1)
                    mc.setAttr((shape[0] + '.smoothShading'),1)
                    mc.setAttr((shape[0] + '.visibleInReflections'),1)
                    mc.setAttr((shape[0] + '.visibleInRefractions'),1)
                    mc.setAttr((shape[0] + '.doubleSided'),1)

    # # 执行 :  texModel - > animModel
    # 执行：单独另存清理
    def checkTexNoAC2AnimMo(self, fileType):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)

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
        
        # CacheSet
        self.checkCacheSetAdd()

        # AnimSet
        self.checkTransAnimSetAdd()
        
        # 合并Set
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache","ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim","ZM")

        # 处理cache环境变量
        self.checkCacheEnvPath()
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)

        # anim着色
        if fileType == 'anim':
            # set类
            if info[1][0] in ['s', 'S']:
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
                        mc.file(newPath, loadReference = rfnNodeLv1[i])
            # 着色
            # 着色需要对参考进行支持
            self.checkAddColorShader()

            
        # render删除不参与渲染物体
        # 这里算法可以加速
        if fileType == 'render':
            # set类
            if info[1][0] in ['s', 'S']:
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
                        mc.file(newPath, loadReference = rfnNodeLv1[i])
                # 全部显示层显示
                layerInfos = mc.ls(type = 'displayLayer')
                for layer in layerInfos:
                    a = layer.lower()
                    if 'defaultLayer' not in a and u'norender' not in a:
                        mc.setAttr((layer + '.visibility'),1)
                # cache turn on
                nodes = mc.ls(type = 'cacheFile')
                if nodes:
                    for nd in nodes:
                        mc.setAttr((nd + '.enable'),1)
                # 清理proxy物体
                proxyObjs = mc.ls('*:*_proxy_*',l=1) + mc.ls('*_proxy_*',l=1)
                if proxyObjs:
                    mc.delete(proxyObjs)
            # 删除_si_和_nr_物体
            grps = mc.ls(type='transform')
            for grp in grps:
                if '_si_' in grp or '_nr_' in grp:
                    # 对参考进行pass
                    try:
                        mc.delete(grp)
                    except:
                        pass


        # displayeLayer及renderPlayer删除
        # 对set不清理显示层
        if info[1][0] not in ['s', 'S']:
            self.checkCleanDisplayLayers()
        self.checkCleanRenderLayers()
        
        # 清理节点
        self.checkDonotNodeClean()
         
        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if joints:
            for joint in joints:
                if mc.getAttr(joint + '.drawStyle',l=1):
                    pass
                else:
                    mc.setAttr((joint + '.drawStyle'), 2)

        # 锁,但SET类不处理
        if info[1][0] not in ['s', 'S']:
            objs = ['MODEL']
            self.checkLockObjs(objs, 1)
            self.checkUnlockMSHGeo()
        
        # 保存anim
        mc.file(force=1, save=1)
    
    # 执行 :  texModel - > cacheModel
    def checkTexMo2CacheMo(self , checkin = 1 ):
        from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
        reload(sk_smoothSet)
        # MODEL物体清理历史
        self.checkCacheSetAdd()
        meshes = mc.sets('MESHES', q=1)
        
        mc.select(meshes)
        mel.eval('DeleteAllHistory')
        mc.select(cl=1)

        # 删除非MODEL
        rootGrp = self.checkOutlinerGroup()[0]
        grps = mc.listRelatives(rootGrp, c=1,f = 1)
        for grp in grps:
            if '|MODEL' not in grp:
                mc.delete(grp)
        
        # 删除_si_和_nr_物体
        grps = mc.ls(type='transform')
        for grp in grps:
            if '_si_' in grp or '_nr_' in grp:
                mc.delete(grp)
        
        # 清理，导出
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_render' + fileFomat
        mc.select(rootGrp)
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        mc.file(fileName, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
        
        # 打开CacheMODEL新文件
        mc.file(fileName, force=1, options="v=0" , type=fileTypeFull, open=1)
        
        # 清理ShapeOrig
        shapes = mc.ls(type = 'mesh')
        for mesh in shapes:
            if mc.getAttr(mesh + '.intermediateObject'):
                mc.delete(mesh)
        
        # 重建cacheSet
        self.checkCacheSetAdd()
        
        # 重建smoothSet
        if checkin:
            serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
            serverSmoothSetInfoPath = serverPath + 'data/AssetInfos/smoothSetInfo/' + shotInfo[0] + '/' + shotInfo[1] + '/' + shotInfo[2] + '/'
            objsSmoothSet_lv0 = self.checkFileRead(serverSmoothSetInfoPath + 'smooth_0.txt')
            if objsSmoothSet_lv0:
                needObjs = []
                for obj in objsSmoothSet_lv0:
                    if mc.ls(obj):
                        objName = mc.ls(obj,l = 1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv0 = needObjs
                    mc.select(objsSmoothSet_lv0)
                    sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,0)
            objsSmoothSet_lv1 = self.checkFileRead(serverSmoothSetInfoPath + 'smooth_1.txt')
            if objsSmoothSet_lv1:
                needObjs = []
                for obj in objsSmoothSet_lv1:
                    if mc.ls(obj):
                        objName = mc.ls(obj,l = 1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv1 = needObjs
                    mc.select(objsSmoothSet_lv1)
                    sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,1)
            objsSmoothSet_lv2 = self.checkFileRead(serverSmoothSetInfoPath + 'smooth_2.txt')
            if objsSmoothSet_lv2:
                needObjs = []
                for obj in objsSmoothSet_lv2:
                    if mc.ls(obj):
                        objName = mc.ls(obj,l = 1)[0]
                        if '|MODEL|' in objName and '_si_' not in obj and  '_nr_' not in obj and '_proxy_' not in obj:
                            needObjs.append(obj)
                if needObjs:
                    objsSmoothSet_lv2 = needObjs
                    mc.select(objsSmoothSet_lv2)
                    sk_smoothSet.sk_smoothSetTools().smoothSetAdd(1,2)
            mc.select(cl = 1)

        # 清理
        self.checkDonotNodeClean()
        
        # displayeLayer及renderPlayer删除
        # 对set不清理显示层
        if shotInfo[1][0] not in ['s', 'S']:
            self.checkCleanDisplayLayers()
        self.checkCleanRenderLayers()
        
        # 合并Set
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache","ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim","ZM")

        # 锁物体
        if shotInfo[1][0] not in ['s', 'S']:
            objs = []
            objs.append(rootGrp)
            self.checkLockObjs(objs, 1)
            self.checkUnlockMSHGeo()

        # 保存
        mc.file(save=1)

    '''
    # 执行 :  texModel - > animModel
    def checkTexMo2AnimMo(self):
        import sk_infoConfig
        reload(sk_infoConfig)
        # 另存
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_anim' + fileFomat
        mc.file(rename=fileName)
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        # mc.file(force=1, options="v=0" , type='mayaBinary' , save=1)
        mc.file(force=1, options="v=0" , type=fileTypeFull , save=1)

        # 删除proxy下的植物
        #import sk_sceneConfig
        #reload(sk_sceneConfig)
        #sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetAdd()
        #sk_sceneConfig.sk_sceneConfig().sk_sceneProxySetObjects()
        #sk_sceneConfig.sk_sceneConfig().sk_sceneMasterDelete()

        # 保存
        mc.file(save=1)
        
    
    # 执行 :  texModel - > cacheModel
    # 和newType cache配合的cache文件
    def checkTexMo2CacheMoNewType(self):
        # MODEL物体清理历史
        self.checkCacheSetAdd()
        meshes = mc.sets('MESHES', q=1)
        
        mc.select(meshes)
        mel.eval('DeleteAllHistory')
        mc.select(cl=1)
        
        # 删除非MODEL
        rootGrp = self.checkOutlinerGroup()[0]
        grps = mc.listRelatives(rootGrp, c=1)
        for grp in grps:
            if 'MODEL' not in grp and 'MSH_c_hi_proxy_' not in grp:
                mc.delete(grp)
        
        # 删除_si_和_nr_物体
        grps = mc.ls(type='transform')
        for grp in grps:
            if '_si_' in grp or '_nr_' in grp:
                mc.delete(grp)

        # 清理，导出
        import sk_infoConfig
        reload(sk_infoConfig)
        path = sk_infoConfig.sk_infoConfig().checkPCFilePath()
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        fileFomat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(shotInfo[0])
        fileName = path + shotInfo[0] + '_' + shotInfo[1] + '_' + shotInfo[2] + '_ms_render' + fileFomat
        # objs = mc.listRelatives(rootGrp,allDescendents = 1,type = 'transform',f =1 )
        mc.select(rootGrp)
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfo[0])
        # mc.file(fileName, force=1, options="v=0" , type='mayaBinary', preserveReferences=1, exportSelected=1)
        mc.file(fileName, force=1, options="v=0" , type=fileTypeFull, preserveReferences=1, exportSelected=1)
        
        # 打开CacheMODEL新文件
        # mc.file(fileName, force=1, options="v=0" , type='mayaBinary', open=1)
        mc.file(fileName, force=1, options="v=0" , type=fileTypeFull, open=1)
        
        # 清理ShapeOrig
        shapes = mc.ls(type = 'mesh')
        for mesh in shapes:
            if mc.getAttr(mesh + '.intermediateObject'):
                mc.delete(mesh)
        
        # 复制文件
        cacheObjs = self.checkCacheObjectsCopy(meshes)

        # 删除原始文件
        mc.delete(rootGrp)

        # CacheSet
        self.checkCacheSetAdd()
        
        # AnimSet
        self.checkTransAnimSetAdd()
        
        # 合并Set
        import sk_sceneConfig
        sk_sceneConfig.sk_sceneConfig().sk_sceneCacheAnimSetConfig("Cache","ZM")
        sk_sceneConfig.sk_sceneConfig().sk_sceneCacheAnimSetConfig("Anim","ZM")

        # 清理节点
        self.checkDonotNodeClean()
        
        # 锁物体
        objs = []
        objs.append(rootGrp)
        self.checkLockObjs(objs, 1)
        self.checkUnlockMSHGeo()
        
        # 保存
        mc.file(save=1)
    '''

    # 处理颜色
    def checkAddColorShader(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        # CacheSet
        self.checkCacheSetAdd()
        
        # AnimSet
        self.checkTransAnimSetAdd()

        # 合并Set
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Cache","ZM")
        sk_sceneTools.sk_sceneTools().sk_sceneCacheAnimSetConfig("Anim","ZM")

        # 隐藏瞳孔
        noNeedObjs = mc.ls('*_si_*',type ='transform')
        for obj in noNeedObjs:
            mc.setAttr((obj+'.v'),0)
        
        # 新版本
        self.checkShaderColorImport()
                                        
        # displayeLayer及renderPlayer删除
        if shotInfo[1][0] not in ['s', 'S']:
            self.checkCleanDisplayLayers()
        self.checkCleanRenderLayers()

        # 隐藏骨骼
        joints = mc.ls(type='joint')
        for joint in joints:
            if mc.getAttr(joint + '.drawStyle',l=1):
                pass
            else:
                mc.setAttr((joint + '.drawStyle'), 2)
            
        # 隐藏晶格
        lattices = mc.ls(type = 'lattice')
        for lattice in lattices:
            grp = mc.listRelatives(lattice,p=1,f=1)
            mc.setAttr((grp[0]+'.v'),0)
        lattices = mc.ls(type = 'baseLattice')
        for lattice in lattices:
            grp = mc.listRelatives(lattice,p=1,f=1)
            mc.setAttr((grp[0]+'.v'),0)

        # 锁,但对参考物体不使用
        if shotInfo[1][0] not in ['s', 'S']:
            if mc.ls('MODEL', type='transform'):
                objs = ['MODEL']
                self.checkLockObjs(objs, 1)
                self.checkUnlockMSHGeo()
    
    '''
            【通用：检测动画曲线】
    0.动画通用
    1.动画曲线点问题修正
    2.动画曲线0清除
    Author: 沈  康
    Data    :2013_03_01
    '''
    # 清理无用动画曲线，修正动画曲线问题
    def checkAnimCleanSingleKey(self):
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 删除单帧动画曲线
                keysNum = mc.keyframe(animC, query=True, keyframeCount=True)
                if keysNum == 3:
                    try:
                        # 清除动画曲线
                        mc.delete(animC)
                    except:
                        #mc.warning(unicode('=====================【错误】【单帧动画】【%s】 参考无法删除=====================') % (str(animC), "utf8"))
                        mc.warning(u'=====================【错误】【单帧动画】【%s】 参考无法删除=====================' % (animC))
                         

    # 判断静态动画
    def checkAnimNoneAnimationCurves(self):
        # 1.值不变
        # 每个点内的切线角度不为0
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 关键帧值
                keysValue = mc.keyframe(animC, query=True, vc=True)
                tempValue = list(set(keysValue))
                # 值相同判断
                if len(tempValue) == 1:
                    # 角度获取
                    # keyAngle = mc.keyTangent(animC, query =True, ia = 1,  oa = 1)
                    tempAngle = list(set(keysValue))
                    # 角度都为0打平判断
                    if len(tempAngle) == 1:
                        # 执行删除
                        mc.delete(animC)


    # 处理动画切线
    def checkAnimKeyTangentConfig(self):
        # 修正问题
        animCurvs = mc.ls(type='animCurve')
        if animCurvs:
            for animC in animCurvs:
                # 曲线点数及时间
                # keysNum  = mc.keyframe( animC, query=True, keyframeCount=True )
                keysTime = mc.keyframe(animC, query=True, tc=True)
                # 切入和切出曲线类型
                inType_animKeys = mc.keyTangent(animC, query=True, itt=1)
                outType_animKeys = mc.keyTangent(animC, query=True, ott=1)
                # 合法切线类型
                types = ["spline", "linear" , "fast" , "slow" , "flat", "step", "stepnext", "fixed" , "clamped" , "plateau" , "auto"] 
                # 修正类型
                fiixType = 'auto'
                if inType_animKeys:
                    # 执行修正
                    for i in range(len(inType_animKeys)):
                        if inType_animKeys[i] not in types:
                            mc.selectKey(animC, k=1 , t=(keysTime[i], keysTime[i]))
                            mc.keyTangent(itt=fiixType)
                    for i in range(len(outType_animKeys)):
                        if outType_animKeys[i] not in types:
                            mc.selectKey(animC, k=1 , t=(keysTime[i], keysTime[i]))
                            mc.keyTangent(ott=fiixType)
                else:
                    mc.delete(animC)

    # 执行清理动画垃圾信息
    def checkAnimDoClean(self):
        # 清理单帧
        self.checkAnimCleanSingleKey()
        # 清理静止动画
        self.checkAnimNoneAnimationCurves()
        # 修正动画曲线问题
        self.checkAnimKeyTangentConfig()

    '''
            【系统】【通用：动画数据导入导出PYTHON版】
    0.通用
    Author: 万寿龙
    Data    :2013_05_24 - 2013_05_28
    '''
    # 导出信息
    # 增加上传服务器功能
    def checkAnimCurveInfoExport(self, objs, serverFile=1, infoFile='anim' , targetPath = ''):
        # 前提基本信息
        AnimsInfo = []
        AnimsInfo.append('ImportExportAnimationForSets v 1.0   (Author: wanshoulong)')
        # 版本号
        AnimsInfo.append('mayaVersion  ' + mc.about(v=1) + ';')
        # 单位类型
        AnimsInfo.append('linearUnit  ' + mc.currentUnit(q=1, f=1, l=1) + ';')
        # 角度单位，弧度还是角度
        AnimsInfo.append('angularUnit  ' + mc.currentUnit(q=1, f=1, a=1) + ';')
        # 制式，PAL等
        AnimsInfo.append('timeUnit  ' + mc.currentUnit(q=1, f=1, t=1) + ';')
        # 获取objs
        if objs:
            for obj in objs:
                # 通道盒子里能被K帧的属性
                keys = mc.listAttr(obj, k=1)
                # 通道盒子中无法被K帧的属性
                noKeys = mc.listAttr(obj, cb=1)
                if noKeys:
                    allAttr = keys + noKeys
                else:
                    allAttr = keys
                if allAttr:
                    for attr in allAttr:
                        animCurve = []
                        if mc.objExists(obj + '.' + attr):
                            # 获取属性的动画曲线
                            animCurve = mc.listConnections((obj + '.' + attr), s=1, d=0)
                        # 剔除无法K帧的情况
                        if animCurve:
                            # 判断是否存在及是否animCurve
                            if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                AnimsInfo.append('anim ' + obj + '.' + attr + '\n{')
                                # 更新信息
                                infoAll = self.checkAnimCurveInfoGet(animCurve[0])  
                                for info in infoAll:
                                    AnimsInfo.append(info)
                                AnimsInfo.append('}')
                        else:
                            # 无动画的信息
                            if mc.objExists(obj + '.' + attr):
                                if 'double3' not in mc.getAttr((obj + '.' + attr), type=1) :
                                    value = mc.getAttr(obj + '.' + attr)
                                    AnimsInfo.append('non-anim ' + obj + '.' + attr + ' ' + str(value) + ';')
                # 对曲线K点的处理
                expShapes = mc.listHistory(obj)
                # 显示控制点的判断
                if expShapes and mc.objectType(expShapes[0], isType='nurbsCurve') and mc.getAttr(expShapes[0] + '.dispCV'):
                    pointNum = mc.getAttr(expShapes[0] + '.spans')
                    # 此处和原脚本不一样
                    for j in range(pointNum * 2):
                        if mc.objExists(expShapes[0] + '.cv[' + str(j) + ']'):
                            allAttr = mc.listAttr((expShapes[0] + '.cv[' + str(j) + ']'), k=1)
                            if allAttr:
                                for attr in allAttr:
                                    animCurve = mc.listConnections((expShapes[0] + '.' + attr), type='animCurve', s=1, d=0)
                                    if animCurve:
                                        if mc.objExists(animCurve[0]) and 'animCurve' in mc.nodeType(animCurve[0]):
                                            AnimsInfo.append('anim ' + expShapes[0] + '.' + attr + '\n{') 
                                            # 更新信息
                                            infoAll = (self.checkAnimCurveInfoGet(animCurve[0]))
                                            for info in infoAll:
                                                AnimsInfo.append(info)
                                            AnimsInfo.append('}')
                                    else:
                                        # 无动画的信息，不过对于点来说基本用不到
                                        if 'double3' not in mc.getAttr((expShapes[0] + '.' + attr), type=1) :             
                                            value = mc.getAttr(expShapes[0] + '.' + attr)
                                            AnimsInfo.append('non-anim ' + expShapes[0] + '.' + attr + ' ' + str(value) + ';')
        # fsMode，指定输出地址
        if targetPath == '':
            # 本地输出
            import sk_infoConfig
            reload(sk_infoConfig)
            # shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath()
            mc.sysFile(localPathAnim, makeDir=True)
            self.checkFileWrite((localPathAnim + infoFile + '.sla'), AnimsInfo)
            # 本地输出object信息
            personalObjsFile = localPathAnim + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
            if serverFile == 1:
                # 上传服务器
                self.checkAnimInfoUpdate(infoFile)
        else:
            # 自定义输出地址
            self.checkFileWrite( (targetPath + infoFile + '.sla') , AnimsInfo)
            # 本地输出object信息
            personalObjsFile = targetPath + infoFile + '_objs.txt'
            self.checkFileWrite(personalObjsFile, objs)
        
        # 动画信息更新到服务器
    def checkAnimInfoUpdate(self, infoFile):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        # 本地路径转mel用
        localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath().replace('\\', '/')
        # 服务器端路径转mel用
        serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath().replace('\\', '/')
        # 开始上传
        fileInfo = infoFile + '.sla'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        fileInfo = infoFile + '_objs.txt'
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPathAnim + fileInfo) + '"' + ' ' + '"' + (serverPathAnim + fileInfo) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
            
    # 模块：记录功能
    def checkAnimCurveInfoGet(self, animCurve):
        #print '-----------------'
        #print animCurve
        # 帧的时间值
        time = mc.keyframe(animCurve, q=1, tc=1)
        #print time
        # 帧的属性值
        value = mc.keyframe(animCurve, q=1, vc=1)
        # 切线 类型
        inputType = mc.keyTangent(animCurve, q=1, itt=1)
        outputType = mc.keyTangent(animCurve, q=1, ott=1)
        # 切线角度
        inputAngle = mc.keyTangent(animCurve, q=1, ia=1)
        outputAngle = mc.keyTangent(animCurve, q=1, oa=1)
        # 权重
        inputWeight = mc.keyTangent(animCurve, q=1, iw=1)
        outputWeight = mc.keyTangent(animCurve, q=1, ow=1)
        # 锁与否
        # lockType = mc.keyTangent(animCurve, q= 1, l=1)
        weightLock = mc.keyTangent(animCurve, q=1, wl=1)
        
        infoW = ''
        infoAll = []
        if time:
            for i in range(len(time)):
                # time  value  inputType   outputType weightLock
                infoW = (' ' + str(time[i]) + ' ' + str(value[i]) + ' ' + str(inputType[i]) + ' ' + str(outputType[i]) + ' ' + str(weightLock[i])) 
                specialFix = ['fixed']
                # 特殊情况补充行
                if inputType[i] in specialFix or outputType[i] in specialFix and weightLock[i]:
                    infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(outputAngle[i]))
                else:
                    if inputType[i] in specialFix  or outputType[i] in specialFix  and weightLock[i] != 'True':
                        infoW = infoW + (' ' + str(inputAngle[i]) + ' ' + str(inputWeight[i]) + ' ' + str(outputAngle[i]) + ' ' + str(outputWeight[i]))
                infoAll.append(infoW + ';')
        return infoAll


    # 导入信息
    # 加入从服务器端读取功能
    def checkAnimCurveInfoImport(self, serverFile=1, infoFile='anim' , replace = [] ,targetPath = ''):
        # 考虑下清理动画
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        # 错误信息
        errorInfo = []
        # fsMode，指定路径读取
        if targetPath == '':
            # 本地获取
            if serverFile == 1:
                serverPathAnim = sk_infoConfig.sk_infoConfig().checkAnimServerPath()
                personalAmimFile = serverPathAnim + infoFile + '.sla'
                personalObjFile = serverPathAnim + infoFile + '_objs.txt'
            else:
                localPathAnim = sk_infoConfig.sk_infoConfig().checkAnimLocalPath()
                personalAmimFile = localPathAnim + infoFile + '.sla'
                personalObjFile = localPathAnim + infoFile + '_objs.txt'
        else:
            # 自定义读取路径
            personalAmimFile = targetPath + infoFile + '.sla'
            personalObjFile = targetPath + infoFile + '_objs.txt'
        # 动画信息
        AnimsInfo = self.checkFileRead(personalAmimFile)
        # 获取objct信息，检测obj
        nsObjs = self.checkFileRead(personalObjFile)
        print nsObjs
        # 对物体有效性进行处理
        if nsObjs:
            checkNoneName = []
            for obj in nsObjs:
                # 替换物处理
                if replace:
                    obj = obj.replace(replace[0],replace[1])
                    if infoFile == 'proxy':
                        # master传proxy
                        if 'MSH_c_hi_proxy' not in replace[0]:
                            obj = obj + '_'
                        # proxy传master
                        if 'MSH_c_hi_proxy' in replace[0]:
                            obj = obj[0:-1]
                exist = mc.objExists(obj)
                if exist != True:
                    checkNoneName.append(obj)
            # 无错误
            if checkNoneName == []:
                linesInfo = len(AnimsInfo)
                if linesInfo > 5:
                    # 预设置
                    aniID = []
                    nonAnimID = []
                    # 单位
                    # linear = mc.currentUnit(q=1, f=1, l=1) 
                    linearSla = AnimsInfo[2].split(' ')[2][0:-1]
                    mc.currentUnit(linear=linearSla) 
                    # 角度
                    # anglular = mc.currentUnit(q=1, f=1, a=1)
                    anglularSla = AnimsInfo[3].split(' ')[2][0:-1]
                    mc.currentUnit(angle=anglularSla) 
                    # 制式
                    # timeType = mc.currentUnit(q=1, f=1, t=1)
                    timeTypeSla = AnimsInfo[4].split(' ')[2][0:-1]
                    mc.currentUnit(time=timeTypeSla) 
                    # 处理不对信息
                    for i in range(5, linesInfo):
                        # 去掉回车符
                        lineInfo = AnimsInfo[i][0:-1]
                        # 取anim行数信息
                        # maya的python中没有startsWith，换个方法
                        if 'anim ' in lineInfo and 'non-anim' not in lineInfo:
                            aniID.append(i)
                        if 'non-anim'  in lineInfo:
                            nonAnimID.append(i)
                    # 处理anim信息
                    for aid in aniID:
                        lineInfo = AnimsInfo[aid][0:-1]
                        # 获取属性
                        attr = lineInfo.split('.')[-1]
                        # 物体名处理
                        objCtrl = lineInfo.split('.')[0].split(' ')[-1]
                        # 替换
                        if replace:
                            objCtrl = objCtrl.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    objCtrl = objCtrl + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    objCtrl = objCtrl[0:-1]
                                    
                        key = ''
                        if 'Shape' not in objCtrl:
                            key = objCtrl + '.' + attr
                        else:
                            ctrolPoint = lineInfo.split('.')[-2]
                            key = objCtrl + '.' + ctrolPoint + '.' + attr
                        # key要存在，且只有一个，且可K帧，且没被锁
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取{}内数据
                            for j in range(1, linesInfo):
                                nextLine = AnimsInfo[aid + j ]
                                if (nextLine != '}') :
                                    if (nextLine != '{'):
                                        # 开始获取属性数据
                                        infoDetails = nextLine.split(' ')
                                        # time
                                        keyFrame = float(infoDetails[1])
                                        # value
                                        keyValue = float(infoDetails[2])
                                        # in & out
                                        keyInput = infoDetails[3]
                                        keyOutput = infoDetails[4]
                                        # weight
                                        infoWeightLock = infoDetails[5]
                                        if infoWeightLock == 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                            # in & out angle
                                            keyInputAngle = float(infoDetails[6])
                                            if ';' in infoDetails[7]:
                                                infoDetails[7] = infoDetails[7][0:-1]
                                            keyOutputAngle = float(infoDetails[7])
                                            # 还原帧
                                            mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                            mc.selectKey(key, k=keyFrame, r=1)
                                            mc.keyTangent(e=1, ia=keyInputAngle, iw=1, oa=keyOutputAngle, ow=1)
                                        else:
                                            if infoWeightLock != 'True' and (infoDetails[3] == 'fixed' or infoDetails[4] == 'fixed'):
                                                # in & out angle and weight
                                                keyInputAngle = float(infoDetails[6])
                                                keyInputWeight = float(infoDetails[7])
                                                keyOutputAngle = float(infoDetails[8])
                                                if ';' in infoDetails[9]:
                                                    infoDetails[9] = infoDetails[9][0:-1]
                                                keyOutputWeight = float(infoDetails[9])
                                                # 还原帧
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue)
                                                mc.selectKey(key, k=keyFrame, r=1)
                                                mc.keyTangent(e=1, ia=keyInputAngle, iw=keyInputWeight, oa=keyOutputAngle, ow=keyOutputWeight)
                                            else:
                                                mc.setKeyframe(key, t=keyFrame , v=keyValue, itt=keyInput, ott=keyOutput)
                                else:       
                                    break
                        else:
                            #errorInfo.append(('===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============') % (str(key)))
                            errorInfo.append(u'===============请检查【%s】，是否唯一，是否可K帧，是否解锁===============' % (key))
                    # 处理non-anim信息
                    for nid in nonAnimID:
                        # 获取属性
                        key = AnimsInfo[nid].split(' ')[1]
                        # 替换
                        if replace:
                            key = key.replace(replace[0],replace[1])
                            if infoFile == 'proxy':
                                # master传proxy
                                if 'MSH_c_hi_proxy' not in replace[0]:
                                    key = key + '_'
                                # proxy传master
                                if 'MSH_c_hi_proxy' in replace[0]:
                                    key = key[0:-1]
                        # key要存在，且只有一个，且可K帧，且没被锁
                        # 锁住后无法处理
                        if len(mc.ls(key)) == 1 and mc.getAttr(key, k=1) and mc.getAttr(key, l=1) != 1:
                            # 处理存在的动画曲线
                            existAnim = mc.listConnections(key, s=1, d=0)
                            if existAnim:
                                mc.delete(existAnim)
                            # 获取属性数据
                            value = AnimsInfo[nid].split(' ')[2][0:-1]
                            if value == 'True':
                                value = float(1.0)
                            if value == 'False':
                                value = float(0.0)
                            if value != 'True' and value != 'False':
                                value = float(value)
                            mc.setAttr(key, value)
                else:  
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            # 丢失物体
            else:
                for error in checkNoneName:
                    #errorInfo.append(('=====================【！！！错误！！！】不存在传递物体【%s】=====================') % (error))
                    errorInfo.append(u'=====================【！！！错误！！！】不存在传递物体【%s】=====================' % (error))
                    #errorInfo.append('=====================【！！！动画信息错误！！！】=====================')
                    errorInfo.append(u'=====================【！！！动画信息错误！！！】=====================')
            for i in errorInfo:
                print(i)
                 
    
    '''
            【通用：着色方案系统】
    0.通用
    Author: 沈  康
    Data    :2013_09_17
    '''
    # 输出着色方案
    def checkShaderColorExport(self):
        # 创建本地txt
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        localPath = sk_infoConfig.sk_infoConfig().checkTexLocalPath() + 'shader.txt'
        serverPath = sk_infoConfig.sk_infoConfig().checkTexServerPath() + 'shader.txt'
        
        # 清理节点
        #self.checkDonotNodeClean()
        # 获取搜有SG节点
        shaderInfo = mc.ls(type = 'lambert')
        shaderNeedInfo = []
        objWithShaderInfo = []
        for shader in shaderInfo:
            # 记录名字,color,透明度
            shaderDetails = shader + '|' + str(mc.getAttr(shader + '.colorR')) + '|' + str(mc.getAttr(shader + '.colorG')) + '|' + str(mc.getAttr(shader + '.colorB'))  + '|'+ str(mc.getAttr(shader + '.transparencyR')) + '|' + str(mc.getAttr(shader + '.transparencyG')) + '|' + str(mc.getAttr(shader + '.transparencyB')) + '|' + str(mc.getAttr(shader + '.diffuse'))
            shaderNeedInfo.append(shaderDetails)
            mc.hyperShade( objects = shader)
            objs = mc.ls(sl=1)
            objNeed = []
            if objs:
                for obj in objs:
                    if '|MODEL|' in mc.ls(obj,l=1)[0]:
                        objNeed.append(obj)
            objWithShaderInfo.append(objNeed)
        # 清空
        mc.select(cl=1)
        # 写文本
        self.checkFileWrite(localPath , shaderNeedInfo , 0)
        self.checkFileWrite(localPath , objWithShaderInfo , 1)
        
        # 传递到服务器
        updateAnimCMD = 'zwSysFile "copy" ' + '"' + (localPath) + '"' + ' ' + '"' + (serverPath) + '"' + ' true'
        mel.eval(updateAnimCMD)
        
    # 导入着色方案 , 对参考物体不处理
    def checkShaderColorImport(self):
        # 读取服务器端数据
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        serverPath = sk_infoConfig.sk_infoConfig().checkTexServerPath() + 'shader.txt'
        
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        
        # 豁免清单
        donotMeshes = []
        if mc.ls('sea_SHD',type = 'lambert'):
            sgNode = mc.listConnections('sea_SHD',d = 1 ,type = 'shadingEngine')
            if sgNode:
                meshes = mc.sets(sgNode[0],q = 1)
                if meshes:
                    donotMeshes = donotMeshes + meshes
        print u'=--=-0---'
        print donotMeshes
        
        # 判断数据文本是否在
        import os
        if os.path.exists(serverPath) :
            # 读文本
            infoAll = self.checkFileRead(serverPath)
            infoNum = len(infoAll)
            if infoNum and infoNum % 2 == 0:
                for i in range(infoNum/2):
                    shaderDetailsInfo = infoAll[i].split('|')
                    objWithShaderInfo = infoAll[infoNum/2 + i]
                    #print(unicode('===!!!开始处理【%s】!!!====' % (str(shaderDetailsInfo[0])), 'utf8'))
                    print(u'===!!!开始处理【%s】!!!====' % (shaderDetailsInfo[0]))
                    # 清理shader
                    if mc.ls(shaderDetailsInfo[0]) and shaderDetailsInfo[0] != 'lambert1':
                        mc.delete(shaderDetailsInfo[0])
                    if mc.ls(shaderDetailsInfo[0] + '_SG'):
                        mc.delete(shaderDetailsInfo[0] + '_SG')
                    # 创建shader和SG
                    if shaderDetailsInfo[0] != 'lambert1':
                        shader = mc.shadingNode ('lambert', asShader=True, name= shaderDetailsInfo[0] )  
                    else:
                        shader = 'lambert1'
                    mc.setAttr(('%s.color') % (shader), float(shaderDetailsInfo[1]), float(shaderDetailsInfo[2]),float(shaderDetailsInfo[3]), type="double3")
                    mc.setAttr(('%s.transparency') % (shader), float(shaderDetailsInfo[4]), float(shaderDetailsInfo[5]),float(shaderDetailsInfo[6]), type="double3")
                    mc.setAttr(('%s.diffuse') % (shader), float(shaderDetailsInfo[7]))
                    shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(shaderDetailsInfo[0] + '_SG'))
                    mc.connectAttr(('%s.%s') % (shader , 'outColor') , ('%s.%s') % ((shaderSG) , 'surfaceShader'), f=True)
                    
                    if objWithShaderInfo:
                        # 赋予材质
                        objs = []
                        for info in objWithShaderInfo.split('\''):
                            if mc.ls(info):
                                # 参考物体不着色
                                ifRef = mc.referenceQuery( info ,isNodeReferenced = 1)
                                if ifRef:
                                    pass
                                else:
                                    if '|MODEL|' in mc.ls(info,l=1)[0]:
                                        objs.append(info)
                        if objs:
                            # 对set类的参考进行处理
                            # 可能会有重复的，因为namespace不同但后缀名相同的有可能
                            if shotInfo[1][0] in ['s', 'S']:
                                if refInfos[0][0]:
                                    for i in range(len(objs)):
                                        # 无参考判断
                                        if mc.objExists(objs[i]):
                                            objs[i] = objs[i]
                                        else:
                                            # 一级参考判断
                                            if mc.objExists('*:*' + objs[i]):
                                                objs[i] = mc.ls('*:*' + objs[i])[0]
                                            else:
                                                # 二级参考判断
                                                if mc.objExists('*:*:*' + objs[i]):
                                                    objs[i] = mc.ls('*:*:*' + objs[i])[0]
                            mc.sets(objs, e=1, forceElement = (shaderDetailsInfo[0] + '_SG') )
                            print(unicode('===!!!【%s】处理完毕!!!====' % (str(shaderDetailsInfo[0])), 'utf8'))
                            print(u'===!!!【%s】处理完毕!!!====' % (shaderDetailsInfo[0]))
                        else:
                            #mc.warning(unicode('===【%s】没有着色物体====' % (str(shaderDetailsInfo[0])), 'utf8'))
                            mc.warning(u'===【%s】没有着色物体====' % (shaderDetailsInfo[0]))
                             
                    else:
                        #mc.warning(unicode('===【%s】没有着色物体====' % (str(shaderDetailsInfo[0])), 'utf8'))
                        mc.warning(u'===【%s】没有着色物体====' % (shaderDetailsInfo[0]))
                        
                # 清理节点
                self.checkDonotNodeClean()
            else:
                #mc.error(unicode('====【！！！着色信息错误！！！】===='), 'utf8')
                print(u'====【！！！着色信息错误！！！】====')
                mc.error(u'====【！！！着色信息错误！！！】====')
        else:
            # 默认着色
            shapes = mc.ls(type = 'mesh',l = 1)
            shapeNeed = []
            for shape in shapes:
                if '|MODEL|' in mc.ls(shape,l=1)[0]:
                    # 参考物体不着色
                    ifRef = mc.referenceQuery(shape,isNodeReferenced = 1)
                    if ifRef:
                        pass
                    else:
                        if donotMeshes:
                            if shape.split('|')[-1] not in donotMeshes:
                                shapeNeed.append(shape)
                        else:
                            shapeNeed.append(shape)
            shapes = shapeNeed
            if shapes:
                shader = mc.shadingNode ('lambert', asShader=True, name= 'IDMT_Shader_Base')  
                shaderSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name=(shader + '_SG'))
                mc.connectAttr(('%s.%s') % (shader , 'outColor') , ('%s.%s') % ((shaderSG) , 'surfaceShader'), f=True)
                try:
                    mc.sets(shapes, e=1, forceElement=shaderSG)
                except:
                    for mesh in shapes:
                        print mesh.split('|')[-1]
                        mc.sets(mesh, e=1, forceElement=shaderSG)
                # 清理节点
                self.checkDonotNodeClean()
            #mc.warning(unicode('====【！！！着色文件不存在，请重新输出！！！】===='), 'utf8')
            mc.warning(u'====【！！！着色文件不存在，请重新输出！！！】====')
    
    '''
    【通用：路径更改地址】
    0.通用
    Author: 沈  康
    Data    :2013_06_10
    '''
    # 本地infot路径
    def checkLocalInfoPath(self):
        localInfoPath = ('D:/Info_Temp/temp/')
        mc.sysFile(localInfoPath, makeDir=True)
        return localInfoPath
    
    # 服务器端project路径
    def checkProjectServerPath(self):
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        projectServerPath = '//file-cluster/GDC/Projects/' + project + '/Project/'
        return projectServerPath
            
    # 本地tex方案路径
    def checkTexLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathTex = ('D:/Info_Temp/temp/texTemp/' + str(dirInfo[1]) + '/' )
        mc.sysFile(localPathTex, makeDir=True)
        return localPathTex
    
    # 服务器端tex方案路径
    def checkTexServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathTex = ('//file-cluster/GDC/Projects/' + project + '/Project/data/AssetShader/' + str(dirInfo[1]) + '/')
        return serverPathTex
        
    # 本地tx2AnimRender路径
    def checkTX2AnimRenderLocalPath(self):
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/tx2AnimRenderTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
        
    # 本地cache路径
    def checkCacheLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathCache = ('D:/Info_Temp/temp/geoCacheTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2])+ '/')
        mc.sysFile(localPathCache, makeDir=True)
        return localPathCache
    
    # 服务器端cache路径
    def checkCacheServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathCache = ('//file-cluster/GDC/Projects/' + project + '/Project/data/GeoCache/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        return serverPathCache
        
    # 本地anim路径
    def checkAnimLocalPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        localPathAnim = ('D:\\Info_Temp\\temp\\animInfoTemp\\' + shotInfo[0] + '\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        mc.sysFile(localPathAnim, makeDir=True)
        return localPathAnim

    # 服务器端cache路径
    def checkAnimServerPath(self):
        # python用
        shotInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(shotInfo[0])
        serverPathAnim = ('\\\\file-cluster\\GDC\\Projects\\' + project + '\\Project\\data\\AnimInfo\\' + str(shotInfo[1]) + '\\' + str(shotInfo[2]) + '\\')
        return serverPathAnim

    # 本地finalLayout路径
    def checkFinalLayoutLocalPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        localPathFinalLayout = ('D:/Info_Temp/temp/finalLayoutTemp/' + dirInfo[0] + '/' + str(dirInfo[1]) + '/' + str(dirInfo[2]) + '/')
        mc.sysFile(localPathFinalLayout, makeDir=True)
        return localPathFinalLayout
    
    # 服务器端cache路径
    def checkFinalLayoutServerPath(self):
        # mel用
        dirInfo = self.checkShotInfo()
        project = self.checkProjectNameSimple2Full(dirInfo[0])
        serverPathFinalLayout = ('//file-cluster/GDC/Projects/' + project + '/Project/scenes/Animation/' + 'episode_' + str(dirInfo[1]) + '/' + 'scene_' + str(dirInfo[2]) + '/' + 'finishing/')
        return serverPathFinalLayout
    
    # 特殊内部任务ID
    def checkStrangeIDInfo(self):
        dataPath = self.checkProjectServerPath() + 'data/localAsset.txt'
        strangeID = self.checkFileRead(dataPath)
        if strangeID:
            strangeID.remove(strangeID[0])
        return strangeID
    
    '''
    【通用：创建目录，读写文件】
    0.通用
    1.读写文件
    Author: 沈  康
    Data    :2013_03_01
    '''
    # 创建目录
    def checkPathInfo(self):
        dirInfo = self.checkShotInfo()
        path = ('D:\\Info_Temp\\temp\\cacheTemp\\' + dirInfo[0] + '\\' + str(dirInfo[1]) + '\\' + str(dirInfo[2]) + '\\')
        mc.sysFile(path, makeDir=True)
        return path
    
    #读文件================
    def checkFileRead(self, path):
        print u'>>>>>>[read]'
        print path
        txt = open(path, 'r');
        try:
            fileContent = txt.readlines()
            print('Loading........')
        finally:
            txt.close()
        result = []
        for info in fileContent:
            if '\r\n' in info:
                result.append(info.split('\r\n')[0])
            else:
                result.append(info)
        return result
    
    #写文件================
    def checkFileWrite(self, path , info , addtion=0):
        print u'>>>>>>[write]'
        print path
        if addtion == 1:
            info = self.checkFileRead(path) + info
        txt = open(path, 'w')
        try:
            txt.writelines(str(a) + '\r\n' for a in info)
            print('Writing........')
        finally:
            txt.close()
    
    '''
            【通用，对list实现乱序功能，lenList必须大于1】
    '''       
    def checkRandomList(self,sourceList):
        if len(sourceList) > 1:
            import random
            tempList = sourceList[:]
            indexNum = len(tempList)
            needList = []
            for i in range(indexNum):
                tempIndex = int(random.uniform(1,indexNum))-1
                needList.append(tempList[tempIndex])
                tempList.remove(tempList[tempIndex])
                indexNum = indexNum - 1
            return needList
    
    
    '''
    【通用：空namespace清理工具，清理namespace工具】
    本函数只对非参考的namespace有效
    Author: 沈  康
    Data    :2013_04_07
    '''       
    def checkNamespaceCleanEmpty(self, configType=1):
        # 设置之前必须清除当前默认前缀，最后还原回去
        preName = mc.namespaceInfo(currentNamespace=1)
        mc.namespace(set=':')
        namespaces = mc.namespaceInfo(listOnlyNamespaces=1)
        namespaces.remove('UI')
        namespaces.remove('shared')
        if namespaces :
            for name in namespaces:
                # 必须设置namespace才能返回当前默认set的信息
                mc.namespace(setNamespace=str(':' + name))
                # 1为处理空的namespace
                if configType == 1:
                    info = mc.namespaceInfo(listOnlyDependencyNodes=1, dagPath=1)
                    if info == None:
                        mc.namespace(set=':')
                        mc.namespace(removeNamespace=name)
                # 2为处理所有非参考namespace
                if configType == 2:
                    mc.namespace(set=':')
                    mc.namespace(force=1, moveNamespace=[name, ':'])
                    mc.namespace(removeNamespace=name)
        mc.namespace(set=str(':' + preName))


    '''
            【通用：同类判断归类脚本】
    0.通用
    Author: 沈  康
    Data    :2013_06_20
    '''
    def checkSameIDConfig(self, objs, configType):
        details = dict({})
        # 处理循环
        for grp in objs:
            ID = ''
            # 处理类型
            # 截取'_'第二位
            if configType == 1:
                ID = grp.split('_')[1]
            if configType == 2: 
            # 截取'_'第二位和第三位
                size = len(grp.split('_'))
                if size >= 3:
                    ID = grp.split('_')[1] + '_' + grp.split('_')[2]
                else:
                    ID = grp.split('_')[1]
            # 开始处理数据
            keys = details.keys()
            if ID in keys:
                details[ID].append(grp)
            else:
                details[ID] = []
                details[ID].append(grp)
        return details
    
    '''
            【核心通用：检测关键字是否在其内，搜索，允许-屏蔽关键字】
    0.通用
    Author: 沈  康
    Data    :2013_03_16
    '''           
   
    def checkInfoSearch(self, KEYS, INFO):
    #    INFO = ['大碗是','大家 好/fw']
    #    KEYS = ['大','是','大家','大碗']
        do_y = []
        do_n = []
        do_o = []
        temp_keys = KEYS[:]
        for key in temp_keys:
            if '-' in key:
                temp_keys.remove(key)
                do_n.append(key.split('-')[1])   
                
        if do_n:    
            for info in INFO:
                for don in do_n:
                    if don in info:
                        return None         
                               
        for i in range(len(temp_keys)):
            do_o.append(1)
            do_y.append(0)
            for info in INFO:
                if temp_keys[i] in info:
                    do_y[i] = 1
         
        if do_y == do_o:
            return True   
        
    '''
    【通用：切换显示|隐藏骨骼】
    0.通用
    Author: 沈  康
    Data    :2013_06_4
    '''
    # 显示|隐藏骨骼
    def checkJointViewHide(self):
        # 隐藏骨骼
        joints = mc.ls(type='joint')
        if mc.getAttr(joints[0] + '.drawStyle') == 2:
            showType = 0
        if mc.getAttr(joints[0] + '.drawStyle') == 0:
            showType = 2
        for joint in joints:
            if mc.getAttr(joint +'.drawStyle',l=1):
                pass
            else:
                mc.setAttr((joint + '.drawStyle'), showType)

    '''
    【通用：项目简写转换全称】
    0.通用
    Author: 沈  康
    Data    :2013_06_4
    '''
    def checkProjectNameSimple2Full(self, simple):
        full = ''
        if simple == 'zm':
            full = 'ZoomWhiteDolphin'
        if simple == 'zo':
            full = 'Zorro'
        if simple == 'cl':
            full = 'Calimero'
        if simple == 'hf':
            full = 'HeroFactory'
        return full
        
    def checkProjectNameFull2Simple(self, full):
        simple = ''
        if full == 'ZoomWhiteDolphin':
            simple = 'zm'
        if full == 'Zorro':
            simple = 'zo'
        if full == 'Calimero':
            simple = 'cl'
        if full == 'HeroFactory':
            simple = 'hf'
        return simple
    
    def checkProjectAudioPath(self, full):
        audioPath = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            audioPath = 'zm'
        if full == 'Zorro' or full == 'zo':
            audioPath = 'zo'
        if full == 'Calimero' or full == 'cl':
            audioPath = 'CA'
        if full == 'HeroFactory' or full == 'hf':
            audioPath = 'hf'
        return audioPath
    
    
    def checkProjectStartFrame(self, full):
        startFrame = ''
        if full == 'ZoomWhiteDolphin' or full == 'zm':
            startFrame = 1001
        if full == 'Zorro' or full == 'zo':
            startFrame = 101
        if full == 'Calimero' or full == 'cl':
            startFrame = 1
        if full == 'HeroFactory' or full == 'hf':
            startFrame = 101
        return startFrame
    
    
    def checkProjectFileFormat(self, pro):
        fileType = ''
        maList = ['cl']
        if pro in maList:
            fileType = '.ma'
        else:
            fileType = '.mb'
        return fileType
    
    def checkProjectFileFormatFull(self, pro):
        fileType = self.checkProjectFileFormat(pro)
        fileTypeFull = ''
        if fileType == '.ma':
            fileTypeFull = 'mayaAscii'
        if fileType == '.mb':
            fileTypeFull = 'mayaBinary'
        return fileTypeFull

    def printTest(self):
        print u'大家好'
        print '大家好'


    '''
            【通用：约束烘焙第一帧】
    Author: liangyu
    Data    :2014_10_10
    '''
    # 为方便修改更新，所有cacheSet物体全部创建cache
    def ly_BakeConstraints(self):
        constraintsAll = mc.ls(type='constraint')
        nodeTypeConfig = ['transform','joint']
        #约束烘焙
        if  constraintsAll:
            tobake= []
            # 处理非参考的物体
            constraints = [x for x in constraintsAll if not mc.referenceQuery(x,inr=1)]
            for constraint in constraints:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            print shape 
                            print obj
                            if mc.nodeType(shape[0]) != 'camera':
                                plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs

            # 处理参考的_ct_an物体
            constraintRefs = [x for x in constraintsAll if mc.referenceQuery(x,inr=1)]
            for constraint in constraintRefs:
                objs = mc.listHistory(constraint)
                for checkType in nodeTypeConfig:
                    temp = mc.listConnections(constraint,s = 1 ,type = checkType)
                    if temp:
                        objs = objs + temp
                plugs = []
                for obj in objs:
                    if (mc.nodeType(obj) in nodeTypeConfig) and mc.nodeType(obj) != "constraint":
                        # 不接受cam
                        shape = mc.listRelatives( obj , s=1 ,ni = 1,f = 1)
                        if shape:
                            if mc.nodeType(shape[0]) != 'camera':
                                if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                    plugs.append(mc.ls(obj,l=1)[0])
                        else:
                            if '_ct_an' in obj or mc.ls(obj + '.ct_an'):
                                plugs.append(mc.ls(obj,l=1)[0])
                plugs = list(set(plugs))
                tobake+= plugs
            io = (0.0,1.0)

            tobake = list(set(tobake))
            
            # 改进版，不bake，而是给新locator bake
            if tobake:
                # 删除locators
                locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    mc.delete(locators)

                # 数值传递到locators
                locators = []
                constraintTemp = []
                for i in range(len(tobake)):
                    locTemp = mc.spaceLocator()
                    locTemp = mc.rename(locTemp[0] , ('IDMT_BakeAnim_' + str(i)))
                    cons = mc.parentConstraint(tobake[i] , locTemp)
                    constraintTemp.append(cons[0])
                    locators.append(locTemp)
                # 一次烘焙
                mc.bakeResults(locators,  t=io,
                        simulation=1,
                        sampleBy=1,
                        disableImplicitControl=1,
                        preserveOutsideKeys=1,
                        sparseAnimCurveBake=1,
                        removeBakedAttributeFromLayer=0,
                        bakeOnOverrideLayer=0,
                        controlPoints=0,
                        shape=1)
                mc.delete(constraintTemp)

                # 重新约束物体
                attrs = ['.tx','.ty','.tz','.rx','.ry','.rz']
                #locators = mc.ls('IDMT_BakeAnim*',type = 'transform')
                if locators:
                    for i in range(len(locators)):
                        # 打断t和r属性
                        for attr in attrs:
                            #mel.eval('CBdeleteConnection \"' + tobake[i] + attr + '\"')
                            self.checkDeleteConnection(tobake[i] + attr)
                        locatorGrp = locators[i]
                        #  父子约束 ,cam已经锁住
                        if 'cam_' not in tobake[i]:
                            print u'----------------'
                            print locatorGrp
                            print tobake[i].split('|')[-1]
                            # 位移检测
                            skipTranslateAxis = []
                            checkTAttr = ['.tx','.ty','.tz']
                            for j in range(3):
                                passAttr = ['x','y','z']
                                tState = mc.getAttr((tobake[i] + checkTAttr[j]),settable = 1)

                                if tState:
                                    pass
                                else:
                                    skipTranslateAxis.append(passAttr[j])
                            # 旋转检测
                            skipRotateAxis = []
                            checkRAttr = ['.rx','.ry','.rz']
                            for k in range(3):
                                passAttr = ['x','y','z']
                                rState = mc.getAttr((tobake[i] + checkRAttr[k]),settable = 1)
                                if rState:
                                    pass
                                else:
                                    skipRotateAxis.append(passAttr[k])
                            # 父子约束
                            if skipTranslateAxis and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis)
                            if skipTranslateAxis == [] and skipRotateAxis:
                                mc.parentConstraint(locatorGrp , tobake[i] , skipRotate = skipRotateAxis)
                            if skipTranslateAxis and skipRotateAxis:
                                print '------'
                                print locatorGrp
                                print tobake[i]
                                # 修正全忽略的问题，全部忽略再去创建约束会报错
                                if (skipTranslateAxis == ['x','y','z']) and (skipRotateAxis == ['x','y','z']):
                                    pass
                                else:
                                    mc.parentConstraint(locatorGrp , tobake[i] , skipTranslate = skipTranslateAxis, skipRotate = skipRotateAxis)
                                        
                            if skipTranslateAxis == [] and skipRotateAxis == []:
                                mc.parentConstraint(locatorGrp , tobake[i])

                    # 二次烘焙
                    mc.bakeResults(tobake,    t=io,
                            simulation=1,
                            sampleBy=1,
                            disableImplicitControl=1,
                            preserveOutsideKeys=1,
                            sparseAnimCurveBake=1,
                            removeBakedAttributeFromLayer=0,
                            bakeOnOverrideLayer=0,
                            controlPoints=0,
                            shape=1)

                    # 删除约束
                    constraintConfigs = [x for x in (constraints + constraintRefs) if not mc.referenceQuery(x,inr=1)]
                    for cons in constraintConfigs:
                        ref = mc.referenceQuery(cons,isNodeReferenced = 1)
                        if not ref:
                            mc.delete(cons)

                    # 删除locators
                    mc.delete(locators)

                    print(u'\n========================【约束】【烘焙】【成功】========================')
                    print u'\n'
        else:
            print(u'\n========================【约束】【烘焙】【失败】========================')
            print u'\n'

    def csl_Attrlist(self,attrtype='GD'):
        objList=[]
        objs=mc.ls(type='transform',l=1)
        if objs: 
            for obj in objs:
                if mc.objExists(obj+'.'+attrtype) and mc.getAttr(obj+'.'+attrtype)==1:
                     objList.append(obj)
        return objList  
    
    
    def ly_checkBASE(self): 
      
        #查询set组
        AnimObjs=[]
        if mc.objExists('TRANSANIM_OBJS'):
            AnimObjs = mc.sets('TRANSANIM_OBJS', q=1)
        if AnimObjs:
            pass
        else:
            mc.error(u'文件中没有”TRANSANIM_OBJ“SSET组')

        CacheObjs=[]
        if mc.objExists('MESHES'):
            CacheObjs = mc.sets('MESHES', q=1)
        if CacheObjs:
            pass
        else:
            mc.error(u'文件中没有做Cache的物体')
                       
        CacheCurves=[]
        if mc.objExists('CACHE_CURVES'):
            CacheCurves = mc.sets('CACHE_CURVES', q=1)
        if CacheCurves:
            pass
        else:
            mc.error(u'文件中没有”CACHE_CURVES“SSET组')
        
        smoothSet=[]
        if mc.objExists('smooth_2'):    
            smoothSet= mc.sets('smooth_2',q=1)
        if smoothSet:
            pass
        elif mc.objExists('smooth_1'):
            smoothSet = mc.sets('smooth_1',q=1)
            if smoothSet:
                pass
            elif mc.objExists('smooth_0'):
                smoothSet = mc.sets('smooth_0',q=1)
                if smoothSet:
                    pass
                else:
                    mc.error(u'文件中没有设置smooth物体')
        #查询多余set组
        CACHE_CURVES=mc.ls('CACHE_CURVES*',type='objectSet')
        CACHE_OBJS=mc.ls('CACHE_OBJS*',type='objectSet')
        SMOOTH_SET=mc.ls('SMOOTH_SET*',type='objectSet')
        TRANSANIM_OBJS=mc.ls('TRANSANIM_OBJS*',type='objectSet')
        if CACHE_CURVES:
            if len(CACHE_CURVES)>1:
                mc.error(u'文件有多余CACHE_CURVES SET组')
                
        if CACHE_OBJS:
            if len(CACHE_OBJS)>1:
                mc.error(u'文件有多余CACHE_OBJS SET组')
                
        if SMOOTH_SET:
            if len(SMOOTH_SET)>1:
                mc.error(u'文件有多余SMOOTH_SET组')
                
        if TRANSANIM_OBJS:
            if len(TRANSANIM_OBJS)>1:
                mc.error(u'文件有多余TRANSANIM_OBJS SET组')    
                
        if mc.ls('ErrorTemp_Set*'):
            mc.error(u'文件检测有错误，请处理好再上传')                    
        #查询文件是否有MODEL组       
        ModelGRP=mc.ls('MODEL')
        if ModelGRP:
            pass
        else:
           mc.error(u'模型文件中要有”MODEL“组') 
            
        #查询物体最后字符是否加‘-’标志
        needGrp=[]
        objs=mc.ls(type='transform',l=1)
        if objs:
            for obj in objs:
                meshcs=mc.listRelatives(obj, c=1, type='mesh',f=1)
                if meshcs:
                    for meshc in meshcs: 
                        if mc.nodeType(meshc)=='mesh':
                            needGrp.append(obj) 
                            
        if needGrp:
            for obj in needGrp:            
                if obj.split('|')[1]=='MODEL':                
                    if obj[-1]=='_':
                        continue
                    else:
                        print obj
                        mc.error(u'MODEL下的多边形物体命名最后要加‘_’,请检查')
                        
        print u'基本检查完毕'

    # 重命名检测
    def checkFileSameNames(self):
        fileName = mc.file(exn=1,q=1).split('/')[-1]
        fileInfo = fileName.split('_')
        # 对set类不检测
        if fileInfo[1][0] in ['s', 'S']:
            return
        # 检测重名错误
        infoWrong = []
        errorNamesTemp = self.checkSameName(needShape = 1)
        if errorNamesTemp:
            for name in errorNamesTemp:
                if '|MODEL|' not in name:
                    continue
                infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))

        errorNamesTemp = self.checkSameName('mesh')
        errorNamesTemp = errorNamesTemp + self.checkSameName('nurbsCurve')
        if errorNamesTemp:
            for name in errorNamesTemp:
                if '|MODEL|' not in name:
                    continue
                infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))

        # 检测mesh同名节点
        errorNamesTemp = self.checkMeshSameNameNodes()
        if errorNamesTemp:
            for name in errorNamesTemp:
                if '|MODEL|' not in name:
                    continue
                infoWrong.append(u'【shape同名】\t\t%s' % (str(name)))

        if infoWrong:
            print u'\n-------------请处理好以下错误-------------'
            for errorInfo in infoWrong:
                print errorInfo
            print u'-------------请处理好以上错误-------------\n'
            raise