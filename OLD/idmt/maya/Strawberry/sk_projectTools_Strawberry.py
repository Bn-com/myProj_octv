# -*- coding: utf-8 -*-

'''
Created on 2013-6-18

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel

from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class sk_projectTools_Strawberry(object):
    def __init__(self):
        pass

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 【UI篇】【前期】【check工具集】
    #------------------------------#
    # 前期check工具集
    def sk_sceneUICheckTools(self):
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        # 窗口
        if mc.window ("sk_sceneUICheckTools", ex=1):
            mc.deleteUI("sk_sceneUICheckTools", window=True)
        mc.window("sk_sceneUICheckTools", title="Check Tools", widthHeight=(450, 450), menuBar=0)
        # 主界面
        mc.columnLayout()

        # 行按钮
        mc.rowLayout(numberOfColumns=2, columnWidth2=(150, 250))
        # 全自动
        mc.button(w=150 , h=350 , bgc=[0, 0.5, 0.2], label=(unicode('【SK4】【全自动】【Check】', 'utf8')), c='from idmt.maya.Strawberry import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning()')
        mc.columnLayout()
        # 分割按钮
        # 第1排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【参考】          ', 'utf8')), c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"refCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动更新标记Set>>', 'utf8')),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_checkTools.sk_checkTools().checkCacheSetAdd()\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkTransAnimSetAdd()\nfrom idmt.maya.py_common import sk_sceneConfig\nreload(sk_sceneConfig)\nsk_sceneConfig.sk_sceneConfig().sk_sceneCacheAnimSetConfig(\"Cache\",\"ZM\")\nsk_sceneConfig.sk_sceneConfig().sk_sceneCacheAnimSetConfig(\"Anim\",\"ZM\")')
        mc.setParent("..")
        # 第2排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【namespace】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"nsCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<namespace工具>>', 'utf8')),c = 'mel.eval(\"common_namespaceTools\")')
        mc.setParent("..")
        # 第3排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【命名】          ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"MSHCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<选取添加_后缀>>', 'utf8')),c ='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_checkTools)\nsk_checkTools.sk_checkTools().checkRenameMSHPosfix()')
        mc.setParent("..")
        # 第4排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【面数】          ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"faceCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动处理重命名>>', 'utf8')),c ='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_checkTools)\nsk_checkTools.sk_checkTools().checkSameRename()\nsk_checkTools.sk_checkTools().checkSameRename(\"mesh\")\nsk_checkTools.sk_checkTools().checkSameRename(\"nurbsCurve\")\nsk_checkTools.sk_checkTools().checkMSHKeepOneRename(\"MSH\")')
        mc.setParent("..")
        # 第5排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【instance】    ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"insCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<displaceLayer清理>>', 'utf8')),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanDisplayLayers()')
        mc.setParent("..")
        # 第6排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【smooth】     ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"smoothCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<renderLayer清理>>', 'utf8')), c = 'from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools\nreload(sk_sceneTools)\nsk_sceneTools.sk_sceneTools().checkCleanRenderLayers()')
        mc.setParent("..")        
        # 第7排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【标记】         ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"signCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<自动清理空组>>', 'utf8')),c = 'mel.eval(\"deleteEmptyGroups()\")')
        mc.setParent("..")
        # 第8排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【物体重名】  ', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"sameTransformCheck\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.7], label=(unicode('<<显示|隐藏骨骼>>', 'utf8')),c = 'from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_checkTools)\nsk_checkTools.sk_checkTools().checkJointViewHide()')
        mc.setParent("..")      
        
        # 第9排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【shape重名】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"sameShapeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.0, 0.0, 0.0], label=(unicode('保留功能', 'utf8')),c='')
        mc.setParent("..")        
        
        # 第10排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【Mesh同名】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_projectTools_Strawberry\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"sameShapeNodeCheck\")')
        mc.button(w=125 , h=30 , bgc=[0.0, 0.0, 0.0], label=(unicode('保留功能', 'utf8')),c='')
        mc.setParent("..")   
        
        # 第11排
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125, 125))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【smoothSet】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"smoothSet\")')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.1], label=(unicode('【Check】【renderState】', 'utf8')),c='from idmt.maya.commonCore.core_mayaCommon import sk_checkTools\nreload(sk_projectTools_Strawberry)\nsk_projectTools_Strawberry.sk_projectTools_Strawberry().checkModelDetailsWarning(\"renderState\")')
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

    #----------------------------------------------------------------------------------------------#
    #------------------------------#
    # 检测系统
    #------------------------------#
    def checkModelDetailsWarning(self,checkType = ''):
        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        infoWrong = []
        errorPrint = 0
        mo = 0
 
        # 创建ErrorSet
        self.checkErrorSetCreate()
        
        # 清理前期节点
        self.checkAssetforbidenNodes(1,1)
        
        # 文件名检测，判断环节
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if len(info) > 3:
            
            # 错误检测，根据阶段不同而不同
            fileFormat = sk_infoConfig.sk_infoConfig().checkProjectFileFormat(info[0])
            if info[3] == ('mo' + fileFormat):
                mo = 1
            #-------------#
            '''
            # 参考检测
            if checkType == '' or checkType == 'refCheck':
                # 对set类不检测
                if info[1][1] not in ['s', 'S']:
                    # 获取参考数
                    rfnNods = mc.file(q=1, reference=1)
                    # 有参考时
                    if rfnNods:
                        infoWrong.append(u'【 警告 】\t\t有参考存在，请注意核查！！')
                else:
                    # 场景有参考时检测是否加载
                    refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
                    checkRef = 0
                    if refInfos[0][0]:
                        for refNode in refInfos[0][0]:
                            isLoad = mc.referenceQuery(refNode,isLoaded = 1)
                            if not isLoad:
                                checkRef = 1
                    if checkRef:
                        infoWrong.append(u'【Unload Reference】\t\t请加载所有参考！！！')
                        errorPrint = errorPrint + 1
            print '[Done]    RefCheck'
            print '\n'
            '''

            # 对set类不检测
            #-------------#
            # 检测namespace
            if checkType == '' or checkType == 'nsCheck':
                if info[1][1] not in ['s', 'S']:
                    namespace = mc.namespaceInfo(listOnlyNamespaces = 1)
                    if len(namespace) > 2:
                        infoWrong.append(u'【 错 误 】\t\t存在namespace，请清理掉！')
                        errorPrint = errorPrint + 1
            print '[Done]    NsCheck'
            print '\n'
                        
            #-------------#
            # 检测MODEL组重命名
            for i in range(0, 9):
                grp = mc.ls('MODEL' + str(i))
                if mc.ls('MODEL' + str(i)):
                    infoWrong.append(u'【错误存在】\t\t%s' % (str(grp[0])))
                    errorPrint = errorPrint + 1
                    
            model = mc.ls('MODEL')
            if model:
                if len(model) > 1:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不止一个！')
                    errorPrint = errorPrint + 1
                else:
                    print '\n'
                    # 检测大组数目
                    rootGrps = sk_checkTools.sk_checkTools().checkOutlinerGroup()
                    if rootGrps:
                        # 根目录大组数目。特殊项目特殊情况
                        numRootGrp = len(rootGrps)
                        if numRootGrp > 1:
                            infoWrong.append(u'【 错 误 】\t\t大组不止一个！')
                            errorPrint = errorPrint + 1
                    else:
                        infoWrong.append(u'【 错 误 】\t\t文件是空的！！')
                        errorPrint = errorPrint + 1

                print '\n'
                '''
                #-------------#
                # 渲染属性检测
                if checkType == '' or checkType == 'renderState':
                    # 对zm的set不检测
                    if not (info[1][1] in ['s', 'S']):
                        errorNames = sk_checkTools.sk_checkTools().checkMeshRenderStates()
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【渲染属性】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_RenderState')  
                        else:
                            mc.delete('Error_RenderState')     

                print '\n'
                '''
                #-------------#
                # 多边面错误
                if checkType == '' or checkType == 'faceCheck':
                    if info[1][1] not in ['s', 'S']:
                        errorNames = sk_checkTools.sk_checkTools().checkFaceVertexs(mo)
                        if errorNames:
                            for name in errorNames:
                                infoWrong.append(u'【非四边形】\t\t%s' % (str(name)))
                                errorPrint = errorPrint + 1
                            mc.sets(errorNames , e=1 , addElement='Error_N4Edges')  
                        else:
                            mc.delete('Error_N4Edges')     
                    else:
                        mc.delete('Error_N4Edges')      
                    
                print '[Done]    faceCheck'
                print '\n'
                
            else:
                print '\n'
                # Set文件不处理
                if info[1][1] not in ['s', 'S']:
                    infoWrong.append(u'【 错 误 】\t\tMODEL组不存在！！')
                    errorPrint = errorPrint + 1

            print '[Done]    MODEL'
            print '\n'
            
            # 重名检测，对s不检测
            if info[1][1] not in ['s', 'S']:
                #-------------#
                # 检测重名错误
                if checkType == ''  or checkType == 'sameTransformCheck':
                    errorNames = []
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName()
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    if errorNames:
                        for name in errorNames:
                            infoWrong.append(u'【节点重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameNode')  
                    else:
                        mc.delete('Error_SameNameNode')  
                            
                print '\n'   
                
                #-------------#
                # 检测重名错误|shape节点检测
                if checkType == '' or checkType == 'sameShapeCheck':
                    errorNames = []
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkSameName('mesh')
                    errorNamesTemp = errorNamesTemp + sk_checkTools.sk_checkTools().checkSameName('nurbsCurve')
                    if errorNamesTemp:
                        for name in errorNamesTemp:
                            if '|MODEL|' in name:
                                errorNames.append(name)
                    passList = []
                    if errorNames and (info[0] + '_' + info[1]) not in passList:
                        for name in errorNames:
                            infoWrong.append(u'【shape重名】\t\t%s' % (str(name)))
                            errorPrint = errorPrint + 1
                        mc.sets(errorNames , e=1 , addElement='Error_SameNameShape')  
                    else:
                        mc.delete('Error_SameNameShape')                      
    
                print '\n'
                
                #-------------#
                # 检测mesh同名节点 
                if checkType == '' or checkType == 'sameShapeNodeCheck':
                    errorNames = []
                    errorNamesTemp = sk_checkTools.sk_checkTools().checkMeshSameNameNodes()
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

            #-------------#
            # 检测Mesh错误
            if checkType == '' or checkType == 'meshError':
                errorNames = sk_checkTools.sk_checkTools().checkMeshError()
                if errorNames:
                    for name in errorNames:
                        infoWrong.append(u'【Mesh错误】\t\t%s' % (str(name)))
                        errorPrint = errorPrint + 1

            print '[Done]    MeshError'
            print '\n'

            #-------------#
            # 检测SmoothSet
            # 只对model，tx，render进行检测
            if checkType == '' or checkType == 'smoothSet':
                from idmt.maya.commonCore.core_mayaCommon import sk_smoothSet
                reload(sk_smoothSet)
                if info[3].split('.')[0] in ['mo','tx','rg']:
                    errorNames = sk_checkTools.sk_checkTools().checkModelSmoothSet(info[0])
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
            
            print '[Done]    SmoothSet'
            print '\n'
            
            #-------------#
            # 检测MR
            if checkType == '' or checkType == 'mrcheck':
                mrState = mc.pluginInfo('Mayatomr' , loaded = 1 , q = 1)
                if mrState:
                    mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
                    if mrNodes:
                        infoWrong.append(u'【MR检测】\t\t本文件 存在  MR 节点，请清理')
                        errorPrint = errorPrint + 1
                    else:
                        try:
                            mel.eval('unloadPlugin "Mayatomr"')
                        except:
                            pass
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
        print(u'=============================【文件中错误如下】=============================')
        for info in infoWrong:
            print info
        print(u'===========================【目前】共计【%s】处错误===========================' % (errorPrint))
        mc.warning(u'===========================【目前】共计【%s】处错误===========================' % errorPrint)
        
        # 解锁
        sk_sceneTools.sk_sceneTools().checkUnlockMSHV()
        sk_sceneTools.sk_sceneTools().checkUnlockMSHGeo()
        
        return errorPrint
    
    #-------------#
    # 【后台】清理anim文件
    #-------------#
    def sk_rebuildClean(self , serverClean = 0 , norenderConfig = 0):
        # 开始处理
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_checkTools
        reload(sk_checkTools)
        from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
        reload(sk_referenceConfig)
        
        sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
        print u'====================多层namespace清理完毕===================='
        
        refInfo = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        
        # 检测ref
        #self.calimeroRefCheck('an',1)
        from idmt.maya.commonCore.core_mayaCommon import sk_animFileCheck
        reload(sk_animFileCheck)
        sk_animFileCheck.sk_animFileCheck().shotAssetRefCheck('an',1)
        
        print u'====================ref对比情况检测完毕===================='
        
        unload = 0
        result = u'[清理完毕]'
        if refNodes:
            for ref in refNodes:
                check = mc.referenceQuery(ref,isLoaded = 1)
                if check:
                    pass
                else:
                    unload = unload + 1
            if unload:
                result = result + u'|Ref Cleaned'
        
        print u'====================ref载入情况检测===================='
        '''
        shareNodes = mc.ls('sharedReferenceNode',type = 'reference')
        if shareNodes:
            print u'\n'
            print u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======'
            print u'\n'
            mc.error(u'======本文件发现ShareNodes模式的参考，请修改为正常模式的参考======')
        '''
        print u'====================ShareNodes检测==================='
        
        sk_animFileCheck.sk_animFileCheck().shotAssetTextureCheck()
        
        print u'====================贴图信息情况检测===================='
        
        # 处理参考
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
        
        sk_sceneTools.sk_sceneTools().sk_sceneAssetNamespaceConfig()
        
        print u'==================Ref Info 处理完毕=================='
        
        # FPS
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('FPS')
        # frame
        sk_sceneTools.sk_sceneTools().sk_sceneImportFrame('frame')
        
        print u'=====================镜头标准化完毕=====================' 
        
        # 清理孙望参考
        # 处理参考
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            print '-------------'
            print refNode
            refPath = mc.referenceQuery(refNode, f=1)
            path = refPath.lower()
            # 清理外部参考
            #if 'strawberry' not in path:
            #    refExist = mc.referenceQuery(refPath,rfn=1)
            #    mc.file(rfn=refExist , removeReference=1)
            # 转换参考
            if '/rigging/' in path:
                newPath = path.replace('/rigging/','/master/')
                newPath = newPath.replace('_rg.','_ms_anim.')
                # 替换参考
                mc.file(newPath, loadReference = refNodes[i])
                
        print u'====================参考整理完毕===================='

        print mc.ls(type='unknown')
        sk_sceneTools.sk_sceneTools().checkDonotNodeClean(1)
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
        print mc.ls(type='unknown')
        
        print u'==================垃圾节点清理完毕=================='

        # 清理层和渲染层
        try:
            mel.eval('editRenderLayerGlobals -currentRenderLayer "defaultRenderLayer"')
        except:
            print u'===请检查文件masterLayer，名字异常==='
            mc.error(u'===请检查文件masterLayer，名字异常===')
        if norenderConfig == 0:
            errorDelete = sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers([],['norender'],0)
            if errorDelete:
                tempLayers = errorDelete
                errorDelete = []
                for layer in tempLayers:
                    vAttr = mc.getAttr(layer + '.v')
                    if not vAttr:
                        errorDelete.append(layer)
            if errorDelete:
                print u'---------------请清理以下显示层---------------'    
                for layer in errorDelete:
                    print layer
                print u'---------------请清理以上显示层---------------' 
                print (u'===请动画拿回返修处理显示层===')   
                mc.error(u'===请动画拿回返修处理显示层===')   
        else:
            errorDelete = sk_sceneTools.sk_sceneTools().checkCleanDisplayLayers([],['norender'],1)
        sk_sceneTools.sk_sceneTools().checkCleanRenderLayers()
        print u'=================显示层|渲染层处理完毕================='    

        sk_sceneTools.sk_sceneTools().sk_sceneCameraUpdate(1)
        
        print u'==================camera传输完毕=================='
        '''
        # mr插件检测
        mrState = mc.pluginInfo('Mayatomr' , loaded = 1 , q = 1)
        if mrState:
            mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
            if mrNodes:
                print u'=====本文件 存在  MR 节点，请Export清理====='
                mc.error(u'=====本文件 存在  MR 节点，请Export清理=====')
            else:
                try:
                    mel.eval('unloadPlugin "Mayatomr"')
                except:
                    pass
        print u'==================MR 加载检测完毕=================='
        '''
        # 处理组
        sk_sceneTools.sk_sceneTools().sk_sceneReorganize(2)
        
        print u'=================outLiner重新分组================='  
    
    
    
    #------------------------------#
    # 选取报错物体
    def checkDetailsObject(self, info):
        info = info.split('\t')[-1]

    #------------------------------#
    # ErrorSet
    def checkErrorSetCreate(self):
        # 文件名检测，判断环节
        info = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if mc.objExists('ErrorTemp_Set'):
            pass
        else:
            mc.createNode('objectSet', n='ErrorTemp_Set')
        # 非四边形
        if mc.objExists('Error_N4Edges'):
            mc.sets(cl='Error_N4Edges')
        else:
            mc.createNode('objectSet', n='Error_N4Edges')
            mc.sets('Error_N4Edges', e=1, addElement='ErrorTemp_Set')   
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
            
            
    #------------------------------#
    # 前期用工具，修改非法字符系列
    #------------------------------#
    # 修改指定目录文件[梁宇]
    def checkFolderNameConfig(self, rootPath):
        noNeedSign = ['-',' ','(',')','{','}']
        fileName = ''
        folderList = mc.getFileList(folder= rootPath)
        if not folderList:
            return 0
        for folderPath in folderList:
            fileList =  mc.getFileList(folder= (rootPath + folderPath + '/'))
            if not fileList:
                continue
            for fileName in fileList:
                newName = fileName
                for sign in noNeedSign:
                    if sign in newName:
                        newName = newName.replace(sign,'_')
                mc.sysFile((rootPath + '/' + folderPath + '/' + fileName),rename = (rootPath + '/' + folderPath + '/' + newName))
            
    #------------------------------#
    # 贴图文件处理[梁宇]
    def checkFilePathNameConfig(self):
        noNeedSign = ['-',' ','(',')','{','}']
        textureNodes = mc.ls(type='file')
        if not textureNodes:
            return 0
        for texNode in textureNodes:
            texPath = mc.getAttr(texNode+'.fileTextureName')
            texName = texPath.split('/')[-1]
            texPathPre = texPath[:(-1*len(texName))]
            newName = texName
            for sign in noNeedSign:
                if sign in newName:
                    newName = newName.replace(sign,'_')
            mc.setAttr((texNode+'.fileTextureName'),( texPathPre + newName),type = 'string')
            
            
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
        # 新文件状态下清理
        mc.file(f=1, new=1)
        try:
            mel.eval('unloadPlugin "Mayatomr"')
        except:
            pass
        # 打开文件时处理
        try:
            mc.file(maName,open = 1 ,force = 1)
        except:
            pass
        # 清理加载但无效果的MR
        try:
            mel.eval('unloadPlugin "Mayatomr"')
        except:
            pass
        # 另存mb
        mbName = localPath + fileName.split('.')[0].split('/')[-1] + '.mb'
        mc.file(rename = mbName)
        mc.file(force=1, options="v=0", type='mayaBinary' , save=1)
        
            
    # 删除mr节点简版
    def checkMrNodesDelSimple(self):
        mrState = mc.pluginInfo('Mayatomr' , loaded = 1 , q = 1)
        if mrState:
            mrNodes = mc.ls(type='mentalrayGlobals')+ mc.ls(type='mentalrayItemsList') +mc.ls(type='mentalrayOptions')
            if mrNodes:
                print u'=====本文件 存在  MR 节点，请Export清理====='
                mc.error(u'=====本文件 存在  MR 节点，请Export清理=====')
            else:
                try:
                    mel.eval('unloadPlugin "Mayatomr"')
                except:
                    pass
                
    #------------------------------#
    # 体积光替换系统
    # 体积光创建，及替换
    def checkVolumeReplace(self,deleteType = 1):
        volumeLights = mc.ls(type = 'volumeLight')
        for volumeLight in volumeLights:
            lightGrp = mc.listRelatives(volumeLight,p = 1 ,f= 1)[0]
            # path
            lightGrpParent = ''
            if lightGrp.count('|') > 1:
                lightGrpParent = lightGrp[:-1*len(lightGrp.split('|')[-1])]
            # 新volumeLight
            newVolume = mc.shadingNode('volumeLight',asLight=1)
            newVolumeName = lightGrp.split('|')[-1] + '_m2012_'
            volumeLightNew = mc.rename(newVolume,newVolumeName)
            # 处理属性
            self.checkVolumeAttrConfig(lightGrp,volumeLightNew)
            # 父子关系
            if lightGrpParent:
                mc.parenct(volumeLightNew,lightGrpParent)
            # 删除旧灯光
            if deleteType:
                mc.delete(lightGrp)
    
    #------------------------------#
    def checkVolumeAttrConfig(self,oldVolume,newVolume):
        # 单值属性
        floatAttrs = ['.newVolumeName','.emitDiffuse','.emitSpecular','.lightShape','.volumeLightDir','.emitAmbient']
        for attr in floatAttrs:
            mc.setAttr((newVolume+attr),mc.getAttr(oldVolume + attr))
        # double3属性
        double3Attrs = ['.color','.shadowColor']
        for attr in double3Attrs:
            value = mc.getAttr(oldVolume + attr)
            mc.setAttr((newVolume+ attr),value[0][0],value[0][1],value[0][2],type = 'double3')
        # colorRange
        rangeAttrs = []
        # lightFog
        fogAttrs = []
        # 光线追踪系列
        depthMode = mc.getAttr(oldVolume + '.useDepthMapShadows')
        mc.setAttr((newVolume + '.useDepthMapShadows'),depthMode)
        if depthMode:
            shadowAttrs = ['.dmapResolution','.useMidDistDmap','.dmapFilterSize','.dmapBias','.fogShadowIntensity','.volumeShadowSamples']
        rayTraceMode = mc.getAttr(oldVolume + '.useRayTraceShadows')
        mc.setAttr((newVolume + '.useRayTraceShadows'),rayTraceMode)
        if rayTraceMode:
            shadowAttrs = ['.lightRadius','.shadowRays','.rayDepthLimit']
        for attr in shadowAttrs:
            mc.setAttr((newVolume+attr),mc.getAttr(oldVolume + attr))
            
    #------------------------------#
    #  全流程用
    #------------------------------#
    # 前期禁止arnold,mr
    def checkAssetforbidenNodes(self,arnoldCheck = 1,mentalray = 1):
        if arnoldCheck:
            arnoldNodes = mc.ls(type='aiAOVDriver')+ mc.ls(type='aiAOVFilter') +mc.ls(type='aiOptions')
            if arnoldNodes:
                print(u'=====Asset 存在 Arnold 节点，请Export清理=====')
                mc.error(u'=====Asset 存在 Arnold 节点，请Export清理=====')
        if mentalray:
            mentalrayNodes = mc.ls(type='mentalrayFramebuffer')+ mc.ls(type='mentalrayOptions') +mc.ls(type='mentalrayGlobals') + mc.ls(type='mentalrayItemsList')
            if mentalrayNodes:
                print(u'=====Asset 存在MR 节点，请用专用工具清理=====')
                mc.error(u'=====Asset 存在MR 节点，请用专用工具清理=====')
            try:
                mel.eval('unloadPlugin "Mayatomr"')
            except:
                pass
            