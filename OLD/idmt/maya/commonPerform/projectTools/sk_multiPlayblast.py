# -*- coding: utf-8 -*-
# 【通用】【前台批量拍屏工具】
#  Author : 沈康
#  Data   : 2017

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
import os

class sk_multiPlayblast(object):
    def __init__(self):
        pass

    def sk_multiPlayblastUI(self):
        uiName = 'sk_multiPlayblastUI'
        if mc.window (uiName, ex=1):
            mc.deleteUI(uiName, window=True)
        mc.window(uiName, title=u"批量前台拍屏", widthHeight=(245, 80), menuBar=0,sizeable = 1)
        columnLayout = mc.columnLayout(adjustableColumn = 1 , columnOffset = ['both',0])


        mc.rowColumnLayout(numberOfRows=2,height = 80)

        mc.frameLayout(l = u'请指定拍屏目录(需写入权限)' ,collapse = 0,collapsable = 0,borderStyle = 'etchedIn')
        mc.textFieldButtonGrp('sk_multiPlayblastFolder',columnWidth2 = [200,1],buttonCommand = 'reload(sk_multiPlayblast)\nsk_multiPlayblast.sk_multiPlayblast().buttonPlayblastFolder()',buttonLabel = u'   选取目录   ')
        mc.setParent("..")

        mc.rowLayout(numberOfColumns = 2,columnWidth2=(120 ,120))
        mc.button(l=u'  全新拍屏  ',w=136,bgc = [0.05,0.05,0.05],c = 'reload(sk_multiPlayblast);sk_multiPlayblast.sk_multiPlayblast().buttonRunPlayblast(1)')
        mc.button(l=u'  继续拍屏  ',w=136,bgc = [0.15,0.65,0.15],c = 'reload(sk_multiPlayblast);sk_multiPlayblast.sk_multiPlayblast().buttonRunPlayblast(0)')
        mc.setParent( '..' )

        mc.setParent("..")

        mc.showWindow(uiName)

    # butoon cmds
    def buttonPlayblastFolder(self):
        folder = mc.fileDialog2(fileMode = 3)
        if not folder:
            return
        mc.textFieldButtonGrp('sk_multiPlayblastFolder',e=1,text = folder[0])

    # mode 0 继续拍屏, 1全新拍屏
    def buttonRunPlayblast(self,mode = 0):
        rootPath = mc.textFieldButtonGrp('sk_multiPlayblastFolder',q=1,text =1)
        if not rootPath:
            print u'\n------[Error]:路径未指定------'
            mc.error()
        self.multiPlayblast(rootPath,mode)

    # 应用
    def multiPlayblast(self,rootPath,cleanMode = 0):
        needFiles = []
        for root, dirs, files in os.walk(rootPath):
            if '\\' in root:
                continue
            needFiles = files
        tempInfos = []
        for checkFile in needFiles:
            if '.m' not in checkFile:
                continue
            tempInfos.append(checkFile)
        needFiles = tempInfos
        # 拍屏路径设置
        movFolder = '%s/mov'%(rootPath)
        if not os.path.exists(movFolder):
            os.makedirs(movFolder)
        # 帮助处理
        readMe = [u'【帮助说明】',u'批量拍屏会打开指定目录的所有maya文件依次拍屏(仅限一级目录)']
        readMe += [u'done.txt记录着已经完成的文件名',u'mov文件夹是输出的路径']
        readMe += [u'\n\n若要在批量拍屏中重新拍屏某些文件，请在txt文件中删除那些已经完成的文件名']
        readMe = []
        sk_infoConfig.sk_infoConfig().checkFileWrite('%s/readMe.txt'%(rootPath),readMe)
        # 记录处理
        fixedTxt = '%s/done.txt'%(rootPath)
        fixedList = []
        if os.path.exists(fixedTxt):
            if cleanMode:
                os.unlink(fixedTxt)
            else:
                fixedList = sk_infoConfig.sk_infoConfig().checkFileRead(fixedTxt)
        else:
            sk_infoConfig.sk_infoConfig().checkFileWrite(fixedTxt,[])
        # 对比
        doneNum = 0
        for num in range(len(needFiles)):
            if needFiles[num] in fixedList:
                doneNum += 1
        # 批处理
        # 缺少自动更新列表
        while doneNum != len(needFiles):
            # 取最近的未完成任务来拍屏
            needFile = ''
            for checkFile in needFiles:
                # 完成的不拍屏
                if checkFile in fixedList:
                    continue
                needFile = checkFile
            print u'\n-----[Start]：%s\n'%needFile
            mayaFile = '%s/%s'%(rootPath,needFile)
            mc.file(mayaFile,o=1,f=1)
            self.playblastPerFile(movFolder)
            # 记录
            if os.path.exists(fixedTxt):
                oldInfos = sk_infoConfig.sk_infoConfig().checkFileRead(fixedTxt)
                if needFile not in oldInfos:
                    newInfos = oldInfos + [needFile]
                else:
                    newInfos = oldInfos
            else:
                newInfos = [needFile]

            sk_infoConfig.sk_infoConfig().checkFileWrite(fixedTxt,newInfos)
            # 更新总任务信息
            for root, dirs, files in os.walk(rootPath):
                if '\\' in root:
                    continue
                needFiles = files
            tempInfos = []
            for checkFile in needFiles:
                if '.m' not in checkFile:
                    continue
                tempInfos.append(checkFile)
            needFiles = tempInfos
            # 更新对比信息
            doneNum = 0
            for num in range(len(needFiles)):
                if needFiles[num] in newInfos:
                    doneNum += 1
            fixedList = newInfos

        print '-------===Mission All Done===-------'

    def playblastPerFile(self,rootPath):
        # 指定路径和文件名
        filePath = mc.file(exn=1,q=1)
        fileName = filePath.split('/')[-1].split('.')[0]
        # 项目特殊预处理
        self.projSpecailSettings(fileName)
        # 通用
        movFile = '%s/%s'%(rootPath,fileName)
        valueKey = 'playblastFile'
        if mc.optionVar(exists = valueKey):
            mc.optionVar(remove = valueKey)
        mc.optionVar(stringValue = [valueKey,movFile])
        valueKey = 'playblastSaveToFile'
        if mc.optionVar(exists = valueKey):
            mc.optionVar(remove = valueKey)
        mc.optionVar(stringValue = [valueKey,1])
        valueKey = 'playblastViewerOn'
        if mc.optionVar(exists = valueKey):
            mc.optionVar(remove = valueKey)
        mc.optionVar(stringValue = [valueKey,0])
        # 清理旧拍屏文件
        fmt = mc.optionVar(q = 'playblastFormat')
        oldFile = ''
        if fmt in ['qt']:
            oldFile = movFile+'.mov'
        if fmt in ['avi']:
            oldFile = movFile+'.avi'
        if oldFile and os.path.exists(oldFile):
            os.unlink(oldFile)
        print '--------oldFile'
        print oldFile
        print os.path.exists(oldFile)
        # 获取相机
        from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
        reload(sk_sceneTools)
        camList = sk_sceneTools.sk_sceneTools().sk_getProjNeedCamera()
        stereoState = sk_infoConfig.sk_infoConfig().checkStereoProj()
        # 切换相机面板
        for camName in camList:
            self.playBlastPerform(camName,stereoState)

    def playBlastPerform(self,camName,stereoState):
        mel.eval('setNamedPanelLayout "Single Perspective View"')
        mc.setFocus('modelPanel4')
        panelNow = mc.getPanel(withFocus = 1)
        if stereoState:
            mel.eval('stereoCameraSwitchToCamera "%s" "%s"'%(camName,panelNow))
            panelTemp = 'StereoPanelEditor'
            mc.modelEditor(panelTemp,e=1,displayAppearance='smoothShaded',displayTextures=0,displayLights='default')
            mc.modelEditor(panelTemp,e=1,nurbsCurves = 0)
        else:
            mel.eval('modelEditor -edit -camera "%s" "%s"'%(camName,panelNow))
            panelTemp= mc.getPanel(withFocus = 1)
            mc.modelEditor(panelTemp,e=1,displayAppearance='smoothShaded',displayTextures=0,displayLights='default')
            mc.modelEditor(panelTemp,e=1,nurbsCurves = 0)
        mel.eval('evalDeferred("performPlayblast(8001)")')

    # 项目特殊预处理
    def projSpecailSettings(self,fileName):
        if fileName.split('_')[0] in ['mk'] and '_dy_' in fileName:
            xgenNodes = mc.ls(type = 'xgmPalette',l=1)
            for checkNode in xgenNodes:
                checkNs = 'cBlueMonkey'
                if checkNs not in checkNode.split(':')[0]:
                    continue
                needXgenNode = checkNode.split('|')[-1]
                # General
                newValue = '${DESC}/Bakelow/'
                needDesc = '%s:BMK_head'%needXgenNode.split(':')[0]
                needObj = 'FileGenerator'
                mc.xgmSetAttr(a = 'inputDir',v = newValue,p = needXgenNode,d = needDesc,o = needObj)
                # BakedGroomManager
                newValue = '${DESC}/Bakelow/'
                needDesc = '%s:BMK_head'%needXgenNode.split(':')[0]
                needObj = 'BakedGroomManager'
                mc.xgmSetAttr(a = 'bakeDir',v = newValue,p = needXgenNode,d = needDesc,o = needObj)
                # 切换
                needDesc = '%s:BMK_head'%needXgenNode.split(':')[0]
                mel.eval('xgmPreview {"%s"}'%needDesc)
            # 隐藏代理
            aiProxy = mc.ls(type = 'aiStandIn',l=1)
            if aiProxy:
                for checkNode in aiProxy:
                    aiProxyP = mc.listRelatives(checkNode,p=1,f=1)
                    mc.setAttr(aiProxyP[0]+'.v',0)