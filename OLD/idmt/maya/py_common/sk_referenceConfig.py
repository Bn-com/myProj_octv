# -*- coding: utf-8 -*-

'''
Created on 2013-06-09

@author: shenkang
'''
import maya.cmds as mc
import maya.mel as mel

import sk_infoConfig

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
        # 获取references信息
        refInfos = self.checkReferenceListInfo()

        # 记录项目，场次，镜头号,文件类型
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        
        # 记录时间轴
        frameStart = mc.playbackOptions(q=1, min=1)
        frameEnd = mc.playbackOptions(q=1, max=1)
        
        # 获取finalLayout临时路径
        localPath = sk_infoConfig.sk_infoConfig().checkFinalLayoutLocalPath()

        # 输出cache 及 anim
        # 先输出anim
        import sk_sceneTools
        reload(sk_sceneTools)
        from idmt.maya.commonCore.coreFinalLayout import sk_cacheFinalLayout
        reload(sk_cacheFinalLayout)
        animObjs = sk_sceneTools.sk_sceneTools().checkAnimSetObjects()
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 0)
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
        fileTypeFull = sk_infoConfig.sk_infoConfig().checkProjectFileFormatFull(shotInfos[0])
        mc.file(force=1, options="v=0", type=fileTypeFull , save=1)
        
        # 场景搭建完毕
        # 载入anim
        animObjs = sk_sceneTools.sk_sceneTools().checkAnimSetObjects()
        sk_cacheFinalLayout.sk_cacheFinalLayout().checkAnimCurveInfoExport(animObjs, 0)
        #print(unicode('=====================【Anim】【本地】【导入】完毕=====================', "utf8"))
        print(u'=====================【Anim】【本地】【导入】完毕=====================')


        # 设置时间轴等消息
        mc.playbackOptions( min=frameStart )
        mc.playbackOptions( frameEnd )

        # 最后保存
        mc.file(save=1)
            
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
    # assetType 0 第一位代表类型 | 1 第二位代表类型
    def checkReferenceShaderReset(self,configType = 0 , assetType = 0):
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo= sk_infoConfig.sk_infoConfig().checkShotInfo()
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
                        #print refNode
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
                        if 'SG' in info and shotInfo[0]!='cl':
                            if '\"' in info:
                                needInfo = info.split('\"')[1]
                                #print needInfo
                                resetShaderInfo.append(needInfo)
                        if '.uv' in info :
                            #print '-----------'
                            print info
                            needInfo = info.split(' ')[1]
                            #print needInfo
                            resetUVInfo.append(needInfo)
                        if 'initialShadingGroup.dagSetMembers' in info:
                            print info
                            needInfo = info.split('\"')[1]
                            #print needInfo
                            resetShaderInfo.append(needInfo)
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
            
    # 参考全部import
    def checkRefAllImport(self):
        refInfos = self.checkReferenceListInfo()
        refNodes = refInfos[0][0]
        if refNodes:
            print u'=====请确保所有参考都已经load====='
            for i in range(len(refNodes)):
                refPath = mc.referenceQuery(refNodes[i],filename = 1)
                if '/episode_camera/' not in refPath.lower():
                    mc.file(refPath,importReference = 1, f = 1)

