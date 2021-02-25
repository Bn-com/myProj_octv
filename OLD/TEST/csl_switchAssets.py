# -*- coding: utf-8 -*-
#  Author : 沈康
#  Data   : 2017
import maya.cmds as mc
import maya.mel as mel

def switchAssetsPerform(checkIDList = {}):
    # 寻找
    if not checkIDList.keys():
        assetIDList = {'c0102ShunLiuFin':'c0108ShunLiuDesertCamo','c0201ShangYuFin':'c0209ShangYuDesertCamo',
                   'c0301GaoChaoFin':'c0309GaoChaoDesertCamo','c3003ChengtianFin':'c3002ChengtianDesert',
                   'c2904AniuFin':'c2912AniuDesertCamo','c3102ZhenghuFin':'c3106ZhenghuDesertCamo'}
    else:
        assetIDList = checkIDList
    refNodes = mc.ls(type='reference')
    refDict = {}
    for refNode in refNodes:
        try:
            refPath = mc.referenceQuery(refNode,filename=1)
            addState = 0
            needKey = ''
            for checkKey in assetIDList.keys():
                if checkKey in refPath:
                    addState = 1
                    needKey = checkKey
            if addState:
                refDict[needKey] = [refNode,refPath]
        except:
            pass
    # 替换
    for checkKey in refDict.keys():
        newPath = refDict[checkKey][1].replace(checkKey,assetIDList[checkKey])
        refNode = refDict[checkKey][0]
        mc.file(newPath, loadReference = refNode)
        newNs = 'csl_%s_h'%(assetIDList[checkKey])
        try:
            mc.file(newPath, e=1, ns=newNs)
        except:
            errorInfo = u'-----[%s]无法被编辑，请处理好-----'%refNode
            print errorInfo
            mc.error()
    # save
    localPath = 'D:/transferTemp/csl/'
    import os
    if not os.path.exists(localPath):
        os.makedirs(localPath)
    fileName = mc.file(q=1,exn=1).split('/')[-1]
    mc.file(rename = localPath + fileName)
    mc.file(s=1,f=1)
    print '--------------------'
    print localPath + fileName