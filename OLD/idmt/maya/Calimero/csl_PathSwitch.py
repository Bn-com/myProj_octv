# -*- coding: utf-8 -*-
# 【Cl】【工具】
#  Author : 韩虹
#  Data   : 2015_02
# import sys
# sys.path.append('D:\\food\pyp\common')


#顺溜项目常用工具

import maya.cmds as mc
import maya.mel as mel
import re
import os
import sys
class cl_PathSwitch(object):
    def __init__(self):
        pass

    # 通过refPath 获取refNode的namespace
    def checkReferenceGetNamespaceInfoByPath(self,refPth):
        namespace = mc.file( refPth ,namespace = 1 ,q = 1 )
        # 判断是不是子参考
        parentRef = mc.referenceQuery( refPth , referenceNode=True, parent = True )
        if parentRef:
            namespace = parentRef[:-2] + ':' + namespace 
        return namespace 
    def checkReferencePathConfig(self, path):
        if '{' in path:
            path = path.split('{')[0]
        return path               
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
    def cl_camPathSwitch(self):
#        camPath='M:/CAL_RSYNC/CAL_MAYA/scenes/CAMERA/CAL_CAMERA_00.ma'
        camPath='Z:/Projects/Calimero/Common_Sync/CAL_MAYA/scenes/CAMERA/CAL_CAMERA_00.ma'
        camName='CAMERA'
        camRN='CAL_CAMERA_00RN'      
        refInfo=self.checkReferenceListInfo()
        refRN=refInfo[0]
        refPath=refInfo[1]
        refName=refInfo[2]
        if refName:
            for i in range(len(refName)):
                if 'CAM' in refName[i] and '_' not in refName[i] and refRN[i] != 'CAL_CAMERA_00RN':
                    try:
                        mc.file(rfn=refRN[i], removeReference=1)
                    except:
                        mc.lockNode(refRN[i], l=0)
                        mc.delete(refRN[i])
        try:
            mc.file(camPath,r=1,namespace=camName,referenceNode = camRN) 
        except:
            print(u'=====================【参考文件路径已经转换完成】=====================') 
        return  0                    
                                                                                            
                                                                
         