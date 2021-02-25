# -*- coding: utf-8 -*-

'''
Created on 2013-06-09

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel

class sk_referenceConfig(object):
    def __init__(self):
        #namespace清理
        pass
    '''
            【通用：无敌reference导入_shareNodes】
    0.通用
    Author: 沈康
    Data    :2013_07_01
    '''        
    # 通过次数变量和时间变量控制namespace
    def sk_referenceShareNodesImport(self):
        myNum = 1000
        special_add_a = 'food' + str(myNum)
        

    '''
            【通用：referenc处理工具集】
    0.通用
    Author: 沈康
    Data    :2013_06_03
    '''
    # 获取referenceList
    def checkReferenceListInfo(self):
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
            refPaths.append(self.checkReferencePathConfig(refInfo))
            #refPaths.append(self.checkReferencePathConfig(str(refInfo.path)))
            refPath = mc.referenceQuery(refInfo , filename = 1)
            refNamespace.append(self.checkReferenceGetNamespaceInfoByPath(refPath))
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
                        refPathsDown.append(self.checkReferencePathConfig(mc.referenceQuery(refNodeD, f=1)))
                        # 记录namespace
                        refNamespaceDown.append(self.checkReferenceGetNamespaceInfoByPath(mc.referenceQuery(refNodeD, f=1)))
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

    # 通过refNode 获取refNode的namespace
    def checkReferenceGetNamespaceInfo(self,refNode):
        refObjs = mc.referenceQuery( refNode ,nodes = 1 )
        namespace = ''
        if refObjs:
            nmInfo = refObjs[0].split(':')
            for i in range(len(nmInfo)-1):
                if i == 0:
                    namespace = nmInfo[i]
                else:
                    namespace =  namespace + ':' + nmInfo[i]
        return namespace
    
    # 通过refPath 获取refNode的namespace
    def checkReferenceGetNamespaceInfoByPath(self,refPth):
        namespace = mc.file( refPth ,namespace = 1 ,q = 1 )
        # 判断是不是子参考
        parentRef = mc.referenceQuery( refPth , referenceNode=True, parent = True )
        if parentRef:
            namespace = parentRef[:-2] + ':' + namespace 
        return namespace
    
    
    # reference重读，并赋予shareNodes
    def checkReferenceShareNodes(self):
        import sk_checkCommon
        reload(sk_checkCommon)
        errors = sk_checkCommon.sk_checkTools().checkModelDetailsWarning()
        
        if errors == 0:
            # 获取references信息
            refInfos = self.checkReferenceListInfo()

            # 记录项目，场次，镜头号,文件类型
            shotInfos = sk_checkCommon.sk_checkTools().checkShotInfo()
            
            # 记录时间轴
            frameStart = mc.playbackOptions(q=1, min=1)
            frameEnd = mc.playbackOptions(q=1, max=1)
            
            # 获取finalLayout临时路径
            localPath = sk_checkCommon.sk_checkTools().checkFinalLayoutLocalPath()
    
            # 输出cache 及 anim
            # 先输出anim
            animObjs = sk_checkCommon.sk_checkTools().checkAnimSetObjects()
            sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(animObjs, 0)
            #print(unicode('=====================【Anim】【本地】【输出】完毕=====================', "utf8"))
            print(u'=====================【Anim】【本地】【输出】完毕=====================')
    
            # 新建文件,临时文件夹另存
            mc.file(f=1, new=1)
            #print(unicode('=====================【创建新文件】=====================', "utf8"))
            print(u'=====================【创建新文件】=====================')
    
            # 导入reference及share nodes
            rfnLv1 = refInfos[0][0]
            rfnPathLv1 = refInfos[1][0]
            
            # shareNode只能对第一级reference处理。。。
            for i in range(len(rfnLv1)):
                ns = rfnLv1[i][0:-2]
                mc.file( rfnPathLv1[i], r=1, sharedNodes="shadingNetworks", namespace=ns)
                #print(unicode(('=====================【创建参考】【%s】=====================') % (str(rfnLv1[i])), "utf8"))
                print(u'=====================【创建参考】【%s】====================='% (rfnLv1[i]))
    
            # 准备另存
            fileName = ''
            for info in shotInfos:
                fileName = fileName + '_' + info
            fileName = fileName[1:]
            
            # 本地文件
            localFile = localPath + fileName
            # 本地保存
            mc.file(rename= localFile)
            fileTypeFull = sk_checkCommon.sk_checkTools().checkProjectFileFormatFull(shotInfos[0])
            mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
            
            # 场景搭建完毕
            # 载入anim
            animObjs = sk_checkCommon.sk_checkTools().checkAnimSetObjects()
            sk_checkCommon.sk_checkTools().checkAnimCurveInfoExport(animObjs, 0)
            #print(unicode('=====================【Anim】【本地】【导入】完毕=====================', "utf8"))
            print(u'=====================【Anim】【本地】【导入】完毕=====================')
    
    
            # 设置时间轴等消息
            mc.playbackOptions( min=frameStart )
            mc.playbackOptions( frameEnd )
    
            # 最后保存
            mc.file(save=1)
        else:
            #print(unicode('=====================【！！！请先处理完所有错误！！！】=====================', "utf8"))
            print(u'=====================【！！！请先处理完所有错误！！！】=====================')
            
    # 处理reference路径，清楚后面可能存在的{}
    def checkReferencePathConfig(self, path):
        if '{' in path:
            path = path.split('{')[0]
        return path
    
    # 读取选取物体所在的reference
    def checkReferenceGetInfo(self):
        objs = mc.ls(sl=1)
        rfNodes = []
        if objs:
            for obj in objs:
                rfNodes.append(mc.referenceQuery(obj, referenceNode=1))
            rfNodes = list(set(rfNodes))
        return rfNodes

    # 删除reference，如果有上级rf那么仅仅unload
    # rfNode为 【字符串】
    def checkReferenceUnload(self, rfNode):
        # 判断物体是否存在
        if mc.ls(rfNode , type='reference'):
            mc.file(rfn=rfNode , unloadReference=1)
        else:
            #mc.warning(unicode('===【参考不存在】===', 'utf8'))
            mc.warning(u'===【参考不存在】===')
            #print(unicode('===【参考不存在】===', 'utf8'))
            print(u'===【参考不存在】===')
            #print(unicode(('%s') % (rfNode), "utf8"))
            print(u'%s' % rfNode)
            #print(unicode('==================', 'utf8'))
            print(u'==================')

    
    # 删除reference，如果有上级rf那么仅仅unload
    # rfNode为 【字符串】
    def checkReferenceDelete(self, rfNode):
        # 判断物体是否存在
        if mc.ls(rfNode , type='reference'):
            # 判断是否有上级reference
            if ':' in rfNode:
                mc.file(rfn=rfNode , unloadReference=1)
            else:
                mc.file(rfn=rfNode , removeReference=1)
        else:
            #mc.warning(unicode('===【参考不存在】===', 'utf8'))
            mc.warning(u'===【参考不存在】===')
            #print(unicode('===【参考不存在】===', 'utf8'))
            print(u'===【参考不存在】===')
            #print(unicode(('%s') % (rfNode), "utf8"))
            print(u'%s' % rfNode)
            #print(unicode('==================', 'utf8'))
            print(u'==================')

    
    # 参考高中低模替换
    # rfNode为 【字符串】
    def checkReferenceHMLModelChange(self, rfNode, sourceType, replaceType):
        # 判断物体是否存在
        if mc.ls(rfNode , type='reference'):
            rfPath = self.checkReferencePathConfig(mc.referenceQuery(rfNode, filename=1))
            newPath = ''
            if sourceType in rfPath:
                newPath = rfPath.replace(sourceType, replaceType)
            return newPath
        else:
            #mc.warning(unicode('===【参考不存在】===', 'utf8'))
            mc.warning(u'===【参考不存在】===')
            #print(unicode('===【参考不存在】===', 'utf8'))
            print(u'===【参考不存在】===')
            #print(unicode(('%s') % (rfNode), "utf8"))
            print(u'%s' % rfNode)
            #print(unicode('==================', 'utf8'))
            print(u'==================')

    
    # 处理reference，替换路径
    # rfNode为 【字符串】
    def checkReferenceChange(self, rfNode, newPath):
        # 判断物体是否存在
        if mc.ls(rfNode , type='reference'):
            # 判断目标路径物体是否存在
            if mc.file(newPath, query=1, exists=1):
                try:
                    mc.file(newPath, loadReference = rfNode)
                except:
                    #mc.warning(unicode(('=====================【%s】有问题=====================')%(str(rfNode)), 'utf8'))
                    mc.warning(u'=====================【%s】有问题====================='% rfNode)
            else:
                #mc.warning(unicode('=====================【文件不存在】=====================', 'utf8'))
                mc.warning(u'=====================【文件不存在】=====================')
                #print(unicode('=====================【文件不存在】=====================', 'utf8'))
                print(u'=====================【文件不存在】=====================')
                #print(unicode(('%s') % (str(newPath)), "utf8"))
                print(u'%s' % newPath)
                #print(unicode('======================================================', 'utf8'))
                print(u'======================================================')
        else:
            #mc.warning(unicode('=====================【参考不存在】=====================', 'utf8'))
            mc.warning(u'=====================【参考不存在】=====================')
            #print(unicode('=====================【参考不存在】=====================', 'utf8'))
            print(u'=====================【参考不存在】=====================')
            #print(unicode(('%s') % (str(rfNode)), "utf8"))
            print(u'%s' % rfNode)
            #print(unicode('======================================================', 'utf8'))
            print(u'======================================================')
    
    # reference切换版本
    # 比如anim切换到render版本
    # 只对一级参考有效
    def checkReferenceReplaceFile(self,sourceKey,targetKey):
        refInfo = self.checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        for i in range(len(refNodes)):
            refNode = refNodes[i]
            oldPath = refPaths[i]
            if sourceKey in oldPath:
                newPath = oldPath.replace(sourceKey,targetKey)
                self.checkReferenceChange(refNode,newPath)

    
    # 处理参考里的材质变动，并恢复 ; 包括UV
    # 由于asset文件都是原始的，即便有参考也是原始的，因此只需要改第一级的即可
    # 0 只处理set参考   | 1 所有参考都处理
    def checkReferenceShaderReset(self,configType = 0 ):
        # 获取文件内参考信息
        refInfos = self.checkReferenceListInfo()
        refNodes = refInfos[0][0]
        if refNodes:
            checkTypes = ['setAttr','connectAttr','disconnectAttr','addAttr','parent']
            for checkType in checkTypes:
                # 更改过的属性信息
                modifyInfos = []
                for refNode in refNodes:
                    if 'CAM' not in refNode :
                        print refNode
                        if configType == 1:
                            modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                        if configType == 0:
                            if refNode.split('_')[1][0] in ['s', 'S']:
                                modifyInfos = modifyInfos + mc.referenceQuery( refNode ,failedEdits = 0 , successfulEdits = 1 ,editCommand = checkType , editStrings = 1)
                if modifyInfos:
                    # 需要欢迎的SG相关信息
                    resetShaderInfo = []
                    resetUVInfo = []
                    for info in modifyInfos:
                        if 'SG' in info :
                            print info
                            needInfo = info.split(' ')[1]
                            print needInfo
                            #resetShaderInfo.append(needInfo)
                        if '.uv' in info :
                            print '-----------'
                            print info
                            needInfo = info.split(' ')[1]
                            print needInfo
                            resetUVInfo.append(needInfo)
                    # 开始欢迎
                    if resetShaderInfo:
                        for info in resetShaderInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)
                    if resetUVInfo:
                        for info in resetUVInfo:
                            mc.referenceEdit(info,failedEdits = 1 , successfulEdits = 1 ,editCommand = checkType , removeEdits = 1)

    # 配合重出工具，默认空文件下，只加载角色和道具
    def checkRefLoadChrProp(self):
        refInfos = self.checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        if refNodes:
            for i in range(len(refNodes)):
                refNode = refNodes[i]
                if '_' in refNode:
                    if refNode.split('_')[1][0] not in ['s', 'S']:
                        mc.file(rfn=refNode , loadReference=1)
            
    # 小鸡专用，客户路径转GDC路径
    # 原理：
    # M:/CAL_RSYNC/CAL_MAYA/scenes/PROPS/ep_106/PRP_Outdoor_ChairA_Child/publish/prp_outdoor_chaira_child_layout_000.ma
    # 取publish前方的数据作为GDC的KEY，再判断进角色还是道具还是Set类
    def calimeroPathToGDC(self,path = ''):
        #path = 'M:/CAL_RSYNC/CAL_MAYA/scenes/PROPS/ep_106/PRP_Outdoor_ChairA_Child/publish/prp_outdoor_chaira_child_layout_000.ma'
        # 获取大类型
        folderType = path.split('/')[-5]
        # 获取GDC关键字
        assetKey = path.split('/')[-3]
        # 获取环节名
        oldFileType = path.split('/')[-1].split('_')[-2]
        # 判断所属
        assetType = folderType
        if folderType == 'CHARACTERS' or folderType == 'characters':
            assetType = 'characters'
        # 判断道具
        if folderType == 'PROPS' or folderType == 'props':
            assetType = 'props'
        # 判断SET
        if folderType == 'SETS' or folderType == 'sets':
            assetType = 'sets'
        # layout阶段
        if oldFileType == 'layout':
            #fileType = 'mo'
            #circleType = 'model'
            fileType = 'ms_anim'
            circleType = 'master'
        if oldFileType == 'anim':
            fileType = 'ms_anim'
            circleType = 'master'
        if oldFileType == 'tx':
            fileType = 'tx'
            circleType = 'texture'
        if oldFileType == 'render':
            fileType = 'ms_render'
            circleType = 'master'
        # GDC路径
        pathGDC = '//file-cluster/GDC/Projects/Calimero/Project/scenes/' + assetType + '/' + assetKey + '/' + circleType +'/cl_' + assetKey + '_h_' + fileType + '.ma'
        print pathGDC
        return pathGDC
    
    
    # 小鸡专用，layout文件转anim文件，及anim文件转render文件
    # 0为ly转anim
    # 1为小鸡模式
    # 2为白海豚layout转anim，所有没有ms_anim的一律转ms_anim
    def calimeroLayout2Anim2Render(self,transType = 1):
        # 进行优化，所有模型全部进layer然后隐藏
        import sk_checkCommon
        reload(sk_checkCommon)
        rootGrps = sk_checkCommon.sk_checkTools().checkOutlinerGroup()
        foodDisplayLayer = mc.createDisplayLayer(n = 'food_temp_DL')
        mc.editDisplayLayerMembers(foodDisplayLayer,rootGrps)
        mc.setAttr((foodDisplayLayer + '.visibility'),0)
        
        if transType == 0:
            old_file = '_mo.'
            new_file = '_ms_anim.'
            old_path = '/model/'
            new_path = '/master/'
        if transType == 1:
            old_file = '_ms_anim.'
            new_file = '_ms_render.'
            old_path = '/master/'
            new_path = '/master/'
        if transType == 2:
            new_file = '_ms_anim.'
            new_path = '/master/'
        
        # 获取ref信息
        refInfo = self.checkReferenceListInfo()
        refNodes = refInfo[0][0]
        refPaths = refInfo[1][0]
        # 开始替换
        for i in range(len(refPaths)):
            if transType == 0 or transType == 1:
                newPath = refPaths[i].replace(old_file,new_file)
                newPath = newPath.replace(old_path,new_path)
                if newPath != refPaths[i]:
                    self.checkReferenceChange(refNodes[i],newPath)
            if transType == 2:
                old_file = '_ms_anim.'
                old_path = '/master/'
                typeInfo = refPaths[i].split('_h')[-1][0:-2]
                if typeInfo != '_ms_anim.':
                    old_file = typeInfo
                typeInfo = refPaths[i].split('/')[-2]
                old_path = '/' + typeInfo + '/'
                newPath = refPaths[i].replace(old_file,new_file)
                newPath = newPath.replace(old_path,new_path)
                if newPath != refPaths[i]:
                    self.checkReferenceChange(refNodes[i],newPath)
        
        # 删除displayLayer
        mc.delete(foodDisplayLayer)
