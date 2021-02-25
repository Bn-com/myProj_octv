# -*- coding: utf-8 -*-
#!/usr/local/bin/python

from PyQt4 import QtGui, QtCore
import sip
import os
import subprocess
import time
import sys
import re
import shutil
import maya.OpenMayaUI as ui
import maya.cmds as mc
import maya.mel as mm
import maya.OpenMaya as om

#代理库的路径
OCT_ArnoldPathNew = r'\\octvision.com\CG\Resource\Material_Library\Proxy\ProxySeed'
# CPAU_PATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
REMOTE_USER = r'octvision.com\supermaya'
REMOTE_PWD = 'supermaya'
USERNAME = os.environ['USER']
NEWPROJECT_NAME = 'New_Project_Sixteeh'
MAYAFOLDER_NAME = 'MayaFiles'
IMAGESFLODER_NAME = 'Images'
PROJECT_PATH = mm.eval('getenv "OCTV_PROJECTS"')
OCT_DRIVE = r'\\octvision.com\cg'
SERVE_PATH = r'\\192.168.80.205'
OCT_FilePath = r'\\file.com\share'
OCT_MDRIVE = r'\\file2.nas\share'
 
class AssetDeadline():
    def __init__(self):
        #UI
        self.windowSize = (600, 350)
        self.windowName = "DeadlineSubmitUI"
        self.assetRadio = ""
        self.outputFiled = ""
        self.okButton = ""
        self.deadlineSereveIp = ""
        self.messageRadio = ''
        self.fileSName = mc.file(q=True, sn=True, shn=True)
        self.copyType = 0
        '''
        copyType分两种模式
        1、单纯的检查模式
        2、检查并打开提交窗口，拷贝提交模式
        3、检查并打开提交窗口，仅提交模式
        '''
        #当存在Arnold时检查各层渲染器
        self.myUseRender = []
        #判断是否有加载

    def close(self, *args):
        if mc.window(self.windowName, q=True, exists=True):
            mc.deleteUI(self.windowName)

    def show(self, *args):
        self.close()

        #make the window
        win = mc.window(self.windowName,
                        t='DeadlineSubmitUI_zwz',
                        wh=self.windowSize,
                        mnb=False, mxb=False, rtf=True, s=True)
        form = mc.formLayout(numberOfDivisions=100)
        oneC = mc.columnLayout('First_Set')
        messageRadio = mc.radioButtonGrp('messagRadioBG', label=u'查看Deadline服务器信息', labelArray2=[u'是', u'否'], sl=2, cl3=['left', 'left', 'left'], cw3=[150, 100, 100], numberOfRadioButtons=2, p=oneC)
        mc.radioButtonGrp('AutoSubmit', label=u'是否全自动提交Deadline', labelArray2=[u'是', u'否'], sl=2, cl3=['left', 'left', 'left'], cw3=[150, 100, 100], numberOfRadioButtons=2, p=oneC)
        mc.radioButtonGrp('ArnoldProxy', label=u'aiStandIn', labelArray2=[u'是', u'否'], sl=1, cl3=['left', 'left', 'left'], cw3=[150, 100, 100], numberOfRadioButtons=2, p=oneC)
        mc.textFieldGrp('imgesPool', label=u'输出路径: ', text='', editable=False, cw2=[120, 150], cal=[1, 'left'], p=oneC)
        one = mc.columnLayout('row1', p=form)
        mc.frameLayout('form', l="Servers List", h=20, borderStyle='out', p='row1')
        mc.columnLayout('row2', p='row1', rs=20)
        selectRadio = mc.radioCollection('myselectRadio', p='row2')
        #mc.radioButton('one', l=u'#1 (211池)', onc=self.selectServer, p='row2')
        mc.radioButton('one', l=u'#1 (206池)', onc=self.selectServer, p='row2')
        mc.radioButton('two', l=u'#2 (222池)', onc=self.selectServer, p='row2')
        mc.radioButton('three', l=u'#3 (223池)', onc=self.selectServer, p='row2')
        mc.radioButton('four', l=u'#4 (224池)', onc=self.selectServer, p='row2')
        #mc.radioButton('five', l=u'#5 (163池)', onc=self.selectServer, p='row2')
        mc.radioButton('six', l=u'#4 (221池)', onc=self.selectServer, p='row2')
        mc.radioButton('seven', l=u'#6 (100池)', onc=self.selectServer, backgroundColor=(0.3, 0.1, 0), p='row2')
        mc.radioButton('eight', l=u'#7 (102池)', onc=self.selectServer, backgroundColor=(0.3, 0.1, 0), p='row2')
        two_one = mc.frameLayout('frame2', l="Server Info", h=20, borderStyle='out', p=form)
        two_two = mc.scrollField('serverInfo', tx='', ww=True, ed=False, p=form)
        three_one = mc.button('slButton', l='Submint', c=self.copyFile, p=form, en=False, bgc=[0, 0.7, 0], w=100)
        three_two = mc.button('cancelButton', l='Cancel', c=self.close, p=form, w=100)

        mc.formLayout(form, edit=True,
                      attachForm=[(one, 'left', 5), (two_one, 'right', 5), (two_two, 'right', 5), (one, 'top', 84), (two_one, 'top', 84), (three_one, 'left', 5), (three_one, 'right', 5), (three_two, 'left', 5), (three_two, 'right', 5), (three_two, 'bottom', 5)],
                      attachControl=[(two_one, 'left', 1, one), (two_two, 'left', 1, one), (two_two, 'top', 1, two_one), (one, 'bottom', 1, three_one), (two_two, 'bottom', 1, three_one), (three_one, 'bottom', 1, three_two)],
                      attachNone=[(three_one, 'top')],
                      )

        self.windowName = win
        self.messageRadio = messageRadio
        self.assetRadio = selectRadio
        self.outputFiled = two_two
        self.okButton = three_one

        mc.showWindow(win)

    def selectServer(self, *args):
        global SERVE_PATH
        mc.waitCursor(state=True)
        selectOption = mc.radioCollection(self.assetRadio, q=True, sl=True)
        if selectOption == 'one':
            self.deadlineSereveIp = r'//192.168.80.206'
            SERVE_PATH = r'\\192.168.80.206'
        if selectOption == 'two':
            self.deadlineSereveIp = r'//192.168.80.222'
            SERVE_PATH = r'\\192.168.80.222'
        elif selectOption == 'three':
            self.deadlineSereveIp = r'//192.168.80.223'
            SERVE_PATH = r'\\192.168.80.223'
        elif selectOption == 'four':
            self.deadlineSereveIp = r'//192.168.80.224'
            SERVE_PATH = r'\\192.168.80.224'
        # elif selectOption == 'five':
        #    self.deadlineSereveIp = r'//192.168.90.163'
        #    SERVE_PATH = r'\\192.168.90.163'
        elif selectOption == 'six':
            self.deadlineSereveIp = r'//192.168.80.221'
            SERVE_PATH = r'\\192.168.80.221'
        elif selectOption == 'seven':
            self.deadlineSereveIp = r'//192.168.90.100'
            SERVE_PATH = r'\\192.168.80.205'
        elif selectOption == 'eight':
            self.deadlineSereveIp = r'//192.168.80.102'
            SERVE_PATH = r'\\192.168.80.225'
        path = os.getenv('PATH').split(';')
        addr = ''
        for eachPath in path:
            if 'Deadline/bin' in eachPath:
                addr = eachPath
                if os.path.isfile('%s/deadlinecommand.exe' % addr):
                    break
        if addr == '':
            mc.confirmDialog(title=u'温馨提示：', message=u'找不到Deadline客户端安装目录,请安装Deadline客户端.', button=['OK'], defaultButton='Yes', dismissString='No')
            sys.stderr.write(u'找不到Deadline客户端安装目录,请安装Deadline客户端.')
        else:
            try:
                str = os.popen(r'"%s/deadlinecommand.exe" -ChangeRepository %s/DeadlineRepository' % (addr, self.deadlineSereveIp)).read()
            except:
                sys.stderr.write(u'设定Deadline服务器时出错,请检查网络连接或权限.')
                mc.button(self.okButton, e=True, en=False)
            else:
                #是否加载服务器信息
                mValue = mc.radioButtonGrp('messagRadioBG', q=True, sl=True)
                if mValue == 1:
                    try:
                        str = os.popen(r'"%s/deadlinecommand.exe" -executescript //octvision.com/cg/Tech/maya/2013/Python/OCT_generel/Deadline/getServerInfo.py' % addr).read()
                    except:
                        mc.confirmDialog(title=u'温馨提示：', message=u'获取Deadline的信息失败，请联系技术管理员！', button=['OK'], defaultButton='Yes', dismissString='No')
                        sys.stderr.write('Error getting Server Info')
                    else:
                        mc.scrollField(self.outputFiled, e=True, tx=str)
                if self.deadlineSereveIp == r'//192.168.90.163':
                    myImagesPaths = ['192.168.90.163', '192.168.90.147']
                    try:
                        address = os.popen(r'"%s/deadlinecommand.exe" -executescript //octvision.com/cg/Tech/maya/2013/Python/OCT_generel/Deadline/getImagesPath.py' % addr).read()
                    except:
                        pass
                    else:
                        minIndex = 0
                        if address:
                            myNum = []
                            for mypath in myImagesPaths:
                                myNum.append(address.count(mypath))
                            minNum = min(myNum)
                            minIndex = myNum.index(minNum)
                        SERVE_PATH = r'\\%s' % myImagesPaths[minIndex]
                mc.button(self.okButton, e=True, en=True)
                mc.textFieldGrp('imgesPool', e=True, text=SERVE_PATH)
        mc.waitCursor(state=False)

    def checkRender(self, *args):
        MrLayers = []
        ArLayers = []
        VrLayers = []
        OtherLayers = []
        #记录了所有层的渲染器
        AllUsedRender = []
        CurrentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
        allLayers = mc.listConnections('renderLayerManager.renderLayerId')
        if  mc.getAttr('%s.renderable' % CurrentLayer):
            CurrentRender = mc.getAttr('defaultRenderGlobals.currentRenderer')
            if CurrentRender == 'arnold':
                ArLayers.append(CurrentLayer)
            elif CurrentRender == 'mentalRay':
                MrLayers.append(CurrentLayer)
            elif CurrentRender == 'vray':
                VrLayers.append(CurrentLayer)
            else:
                OtherLayers.append(CurrentLayer)
            AllUsedRender.append(CurrentRender)
        if allLayers:
            eachRender = ''
            for Layer in allLayers:
                if Layer != CurrentLayer:
                    if mc.getAttr('%s.renderable' % Layer):
                        mc.editRenderLayerGlobals(currentRenderLayer=Layer)
                        eachRender = mc.getAttr('defaultRenderGlobals.currentRenderer')
                        if eachRender == 'mentalRay':
                            MrLayers.append(Layer)
                        elif eachRender == 'arnold':
                            ArLayers.append(Layer)
                        elif eachRender == 'vray':
                            VrLayers.append(Layer)
                        else:
                            OtherLayers.append(Layer)
                        AllUsedRender.append(eachRender)
            if not ArLayers and MrLayers:
                if eachRender != 'mentalRay':
                    mc.editRenderLayerGlobals(currentRenderLayer=MrLayers[0])
            else:
                mc.editRenderLayerGlobals(currentRenderLayer=CurrentLayer)
        return [OtherLayers, MrLayers, ArLayers, VrLayers, AllUsedRender]

    def myChangeNetPath(self, TempPath):
        if TempPath.find('${OCTV_PROJECTS}') >= 0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        elif TempPath.find('w:') >= 0:
            TempPath = TempPath.replace('w:', OCT_FilePath)
        elif TempPath.find('W:') >= 0:
            TempPath = TempPath.replace('W:', OCT_FilePath)
        elif TempPath.find('M:') >= 0:
            TempPath = TempPath.replace('M:', OCT_MDRIVE)
        elif TempPath.find('m:') >= 0:
            TempPath = TempPath.replace('m:', OCT_MDRIVE)
        return TempPath

    def checkFile(self, copyType):
        '''
        copyType分两种模式
        1、单纯的检查模式
        2、检查并打开提交窗口，拷贝提交模式
        3、检查并打开提交窗口，仅提交模式
        '''
        self.copyType = copyType
        self.OtherLayers = []
        OtherLayers = []
        MrLayers = []
        ArLayers = []
        AllUsedRender = []
        #检查是否存在可渲染的摄像机
        myAllCameras = []
        CameraShape = ''
        AllCameras = AllCameras = mc.listCameras(p=True)
        if AllCameras:
            for Camera in AllCameras:
                try:
                    CameraShape = mc.listRelatives(Camera, s=True)[0]
                except:
                    if mc.getAttr('%s.renderable'%Camera):
                        myAllCameras.append(Camera)
                else:
                    if mc.getAttr('%s.renderable'%CameraShape):
                        myAllCameras.append(Camera)
        if not myAllCameras:
            om.MGlobal.displayInfo(u'无可渲染的摄像机！请设置需要渲染的摄像机\n')
            mc.confirmDialog(title=u'温馨提示：', message=u'无可渲染的摄像机！请设置需要渲染的摄像机', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

        if copyType != 1:
            if self.fileSName:
                nameFlag = False
                fileSN = self.fileSName.split('_')
                while '' in fileSN:
                    fileSN.remove('')
                if len(fileSN) >= 3:
                    #判断服务器是否存在该工程
                    serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
                    if os.path.isdir(serFilePath):
                        if mc.file(q=True, amf=True):
                            if self.copyType == 2 or self.copyType == 4:
                                saveFlag = mc.confirmDialog(title=u'温馨提示', message=u'文件已被修改过，请问是否先保存再继续提交？', button=['Yes', 'SaveAs', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                                if saveFlag == 'Yes':
                                    mm.eval("SaveScene")
                                elif saveFlag == "SaveAs":
                                    mm.eval("SaveSceneAs")
                                    nameFlag = True
                    else:
                        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                        return False
                else:
                    mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                    return False

                if nameFlag:
                    self.fileSName = mc.file(q=True, sn=True, shn=True)
                    fileSNew = self.fileSName.split('_')
                    while '' in fileSNew:
                        fileSNew.remove('')
                    if len(fileSNew)>=3:
                        #判断服务器是否存在该工程
                        serFilePath = os.path.join(PROJECT_PATH, fileSNew[0], r'Project\scenes\animation', fileSNew[1], fileSNew[2])
                        if not os.path.isdir(serFilePath):
                            mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                            return False
                    else:
                        mc.confirmDialog(title=u'警告', message=u'在\\octvision.com\cg\Themes下不存在相应工程！\n--------请检查文件命名是否正确！--------', button=['OK'], defaultButton='Yes', dismissString='No')
                        return False
                             
            else:
                mc.confirmDialog(title=u'警告', message=u'文件名为空！', button=['OK'], defaultButton='Yes', dismissString='No')
                return False
            #判断Arnold存在时，是否有加载其他渲染器的渲染层
            self.myUseRender = self.checkRender()
            OtherLayers = self.myUseRender[0]
            MrLayers = self.myUseRender[1]
            ArLayers = self.myUseRender[2]
            AllUsedRender = self.myUseRender[4]
            # print AllUsedRender
            if len(set(AllUsedRender)) > 1:
                mc.confirmDialog(title=u'警告', message=u'提交的文件仅能使用一种渲染器！\n----------请修改文件---------', button=['OK'], defaultButton='Yes', dismissString='No')
                return False


        #设置前缀名
        mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<Camera>", type="string")
        if mc.pluginInfo("mtoa.mll", q = True, loaded = True) and mc.getAttr("defaultRenderGlobals.currentRenderer")=="arnold":
            mc.setAttr("defaultRenderGlobals.imageFilePrefix", "<Scene>/<RenderLayer>/<Camera>/<RenderPass>/<Camera>", type="string")

        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True) and mc.objExists('vraySettings'):
            mc.setAttr("vraySettings.fileNamePrefix", "<Scene>/<Layer>/<Camera>/<Camera>", type="string")
            if not mc.ls(type = 'pgYetiMaya'):
                mc.setAttr("defaultRenderGlobals.preMel", "", type ="string")
                mc.setAttr("defaultRenderGlobals.postMel", "", type ="string")

        def outPutSets(nodes, name):
            if nodes:
                mc.select(nodes)
                if mc.objExists(name):
                    mc.sets(cl=name)
                    mc.sets(add=name)
                else:
                    mc.sets(n=name)
            else:
                if mc.objExists(name):
                    mc.delete(name)

        #检查贴图路径
        noTexFiles = []
        #Arnold的Tx贴图
        noArnoldTxTexFiles = []
        ArnoldFlag = False
        if ArLayers:
            ArnoldFlag = True
        allTexFiles = mc.ls(type='file')
        if allTexFiles:
            for texFile in allTexFiles:
                try:
                    texFileName = mc.getAttr('%s.fileTextureName' % texFile)
                except:
                    pass
                else:
                    if texFileName:
                        texFileName = self.myChangeNetPath(texFileName)
                        #当有层使用了Arnold渲染器之后，需要判断是否存在TX文件
                        if ArnoldFlag:
                            PathSplitT = os.path.splitext(texFileName)
                            if len(PathSplitT) > 1:
                                LowerPathType = PathSplitT[1].lower()
                                #序列帧不拷贝tx
                                UseSeqFlag = mc.getAttr('%s.useFrameExtension' % texFile)
                                if (LowerPathType != '.hdr') and ((LowerPathType != '.tx') and (not UseSeqFlag)):
                                    ArnoldTxFileName = PathSplitT[0]+'.tx'
                                    if not os.path.isfile(ArnoldTxFileName):
                                        noArnoldTxTexFiles.append(texFile)
                                else:
                                    if not os.path.isfile(texFileName):
                                        noTexFiles.append(texFile)
                            else:
                                noTexFiles.append(texFile)
                        else:
                            if not os.path.isfile(texFileName):
                                noTexFiles.append(texFile)
                    else:
                        noTexFiles.append(texFile)
        outPutSets(noTexFiles, 'sortNo_TexFiles_sets')
        outPutSets(noArnoldTxTexFiles, 'sortNo_ArnoldTxFiles_sets')

       #检查缓存路径
        wrongCacheFiles = []
        noCacheFiles = []
        allCacheFiles = mc.ls(type='cacheFile')
        LocaDatalPath = mc.workspace(en='data')
        LocaPath = mc.workspace(fn = True)
        file_type = ['data', 'cache']
        if allCacheFiles:
            for mycacheFile in allCacheFiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % mycacheFile)
                except:
                    pass
                else:
                    if cachePath:
                        cachePath = self.myChangeNetPath(cachePath)
                        cacheName = mc.getAttr('%s.cacheName' % mycacheFile)
                        cacheFilePath = os.path.join(cachePath, cacheName) + '.xml'
                        if not os.path.isfile(cacheFilePath):
                            noCacheFiles.append(mycacheFile)
                        # LocaPaths = ""
                        # for types in file_type:
                        #     cachePath = cachePath.replace('\\', '/')
                        #     texFileNameS = cachePath.split('/')
                        #     if types in texFileNameS:
                        #         LocaPaths = '%s/%s'%(LocaPath, types)

                        # if LocaPaths:
                        #     LocaPaths = self.myChangeNetPath(LocaPaths)
                        #     LocaPaths = os.path.normpath(LocaPaths)
                        #     if os.path.isdir(LocaPaths):
                        #         cachePath = os.path.normpath(cachePath)
                        #         if cachePath.lower().find(LocaPaths.lower()) < 0:
                        #             wrongCacheFiles.append(mycacheFile)
                        #     else:
                        #         noCacheFiles.append(mycacheFile)
                        # else:
                        #     wrongCacheFiles.append(mycacheFile)
                    else:
                        noCacheFiles.append(mycacheFile)

        outPutSets(noCacheFiles, 'sortNo_CacheFiles_sets')
        # outPutSets(wrongCacheFiles, 'sortWrong_CacheFiles_sets')
        
        #检查Yeti缓存路径、以及贴图路径下
        noYetiCacheFiles = []
        wrongYetiTexFiles = []
        noYetiTexFiles = []
        allYetiCacheFiles = mc.ls(type='pgYetiMaya')
        if allYetiCacheFiles:
            for myYetiCacheFile in allYetiCacheFiles:
                YetiFileMode = None
                try:
                    YetiFileMode = mc.getAttr('%s.fileMode' % myYetiCacheFile)
                except:
                    pass
                else:
                    if YetiFileMode == 1:
                        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
                        if YetiCachePath:
                            YetiCachePath = self.myChangeNetPath(YetiCachePath)
                            YetiCacheBasePath = os.path.basename(YetiCachePath)
                            YetiCacheBName = YetiCacheBasePath.split('.')[0]
                            YetiCacheDirPath = os.path.dirname(YetiCachePath)
                            if os.path.isdir(YetiCacheDirPath):
                                allYetiDirs = os.listdir(YetiCacheDirPath)
                                FindYetiFileFlag = False
                                for yetiDir in allYetiDirs:
                                    if yetiDir.find(YetiCacheBName) >= 0:
                                        FindYetiFileFlag = True
                                        break
                                if not FindYetiFileFlag:
                                    noYetiCacheFiles.append(myYetiCacheFile)
                            else:
                                noYetiCacheFiles.append(myYetiCacheFile)
                    YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
                    if YetiTexPath:
                        YetiTexPath = self.myChangeNetPath(YetiTexPath)
                        YetiTexPath=YetiTexPath.replace("\\","/")
                        Textype = YetiTexPath.split('/')[-1]
                        if Textype.lower() != 'yeti':
                            wrongYetiTexFiles.append(myYetiCacheFile)
                        else:
                            if os.path.isdir(YetiTexPath):
                                allYetiTexFiles = os.listdir(YetiTexPath)
                                if not allYetiTexFiles:
                                    noYetiTexFiles.append(myYetiCacheFile)
                            else:
                                noYetiTexFiles.append(myYetiCacheFile)
        outPutSets(noYetiCacheFiles, 'sortNo_pgYetiMaya_CacheFiles_sets')
        outPutSets(wrongYetiTexFiles, 'sortWorng_pgYetiMaya_TexFiles_sets')
        outPutSets(noYetiTexFiles, 'sortNo_pgYetiMaya_TexFiles_sets')

        #检查ABC缓存路径
        wrongAbcCacheFiles = []
        noAbcCacheFiles = []
        type_file = 'alembic'
        myLocaProjectPath= mc.workspace(fn=True)
        allCacheFiles = mc.ls(type='AlembicNode')
        if allCacheFiles:
            for myAbccacheFile in allCacheFiles:
                try:
                    abcCachePath = mc.getAttr('%s.abc_File' % myAbccacheFile)
                except:
                    pass
                else:
                    abcCachePath = self.myChangeNetPath(abcCachePath)
                    abcCachePath = os.path.normpath(abcCachePath)
                    mc.setAttr('%s.abc_File' % myAbccacheFile, abcCachePath, type = 'string')
                    if abcCachePath:
                        try:
                            indexType = abcCachePath.index("alembic")
                        except:
                            wrongAbcCacheFiles.append(myAbccacheFile)
                        else:
                            if not os.path.isfile(abcCachePath):
                                abcCachePath = os.path.join(myLocaProjectPath, abcCachePath)
                                abcCachePath = os.path.normpath(abcCachePath)
                                if not os.path.isfile(abcCachePath):
                                    noAbcCacheFiles.append(myAbccacheFile)
                    else:
                        noAbcCacheFiles.append(myAbccacheFile)
        outPutSets(noAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')
        outPutSets(wrongAbcCacheFiles, 'sortWorng_Alembic_CacheFiles_sets')

        #检查粒子缓存
        noParticle = ''
        #
        AllIsParFlag = False
        AllPars = mc.ls(type='particle')
        if AllPars:
            for eachP in AllPars:
                if mc.nodeType(eachP) == 'particle':
                    AllIsParFlag = True
                    break
        if AllIsParFlag:
            mydynGlobals = mc.dynGlobals(q=True, a=True)
            #parPath = mc.workspace(en='particles')
            parPath = mc.workspace(fullName=True)+"/cache/particles"
            if os.path.isdir(parPath):
                allDirs = os.listdir(parPath)
                if mydynGlobals:
                    if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
                        cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
                        if allDirs:
                            particleFlag = False
                            for direach in allDirs:
                                if direach.lower().find(cacheDirectory.lower()) >= 0:
                                    particleFlag = True
                                    break
                            if not particleFlag:
                                noParticle = mydynGlobals
                outPutSets(noParticle, 'sortNo_Particl_sets')
            #检查粒子初始化文件是否存在，不存在需要保存
                fileShortName = os.path.splitext(self.fileSName)[0]
                FindParStartFlag = False
                for perDir in allDirs:
                    if perDir.find(fileShortName) >= 0:
                        if perDir.find('_startup') >= 0:
                            FindParStartFlag = True
                            break
                if not FindParStartFlag:
                    saveFlag = mc.confirmDialog(title=u'警告：', message=u'文件中的粒子没有相应的Startup文件，必须进行保存！', button=[u'保存', u'中断退出'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    if saveFlag == u'\u4fdd\u5b58':
                        mm.eval("SaveScene")
                        time.sleep(1)
                    else:
                        return False
            else:
                mc.confirmDialog(title=u'警告：', message=u'工程目录下不存在particles！\n请完整齐全的工程目录', button='Bye Bye!', defaultButton='Yes', cancelButton='No', dismissString='No')
                return False

        #检查毛发Shave缓存
        noShaveCacheFiles = []
        allOnlyShaveShapes = []
        allShaveShapes = mc.ls(type='shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        if len(allShaveShapes) > len(allOnlyShaveShapes):
            mc.warning(u"毛发Shave的shapes节点有重名的，将导致同名的Shave使用同一个缓存！")
        myshaveGlobals = "shaveGlobals"
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
            if shavePath:
                shavePath = self.myChangeNetPath(shavePath)
                if not os.path.isdir(shavePath):
                    proPath = mc.workspace(q=True, rd=True)
                    shavePath = os.path.normpath(os.path.join(proPath, shavePath))
                if shavePath.find('z:') >= 0:
                    shavePath = shavePath.replace('z:', OCT_DRIVE)
                elif shavePath.find('Z:') >= 0:
                    shavePath = shavePath.replace('Z:', OCT_DRIVE)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        shaveNames = []
                        for eachDir in allSahveDirs:
                            shaveNames.append(eachDir.split(".")[0])
                        shaveNames = list(set(shaveNames))
                        for eachShape in allShaveShapes:
                            myName = "shaveStatFile_%s" % eachShape.split("|")[-1]
                            if not myName in shaveNames:
                                eachTran = mc.listRelatives(eachShape, f=True, p=True)[0]
                                noShaveCacheFiles.append(eachTran)
                        if noShaveCacheFiles:
                            noShaveCacheFiles.append(myshaveGlobals)
                    else:
                        noShaveCacheFiles.append(myshaveGlobals)
                else:
                    noShaveCacheFiles.append(myshaveGlobals)
        outPutSets(noShaveCacheFiles, 'sortNo_Shave_CacheFiles_sets')

        #检查代理文件/或路径是否存在的模板
        def myCheck_FileOrFolderModel(myType, mtAttr, fileType, NoTypeSets):
            myLocalSourcePath = mc.workspace(en='sourceimages')
            noFiles = []
            try:
                allFiles = mc.ls(type=myType)
            except:
                pass
            else:
                if allFiles:
                    for fileeach in allFiles:
                        try:
                            myFileName = mc.getAttr('%s.%s' % (fileeach, mtAttr))
                        except:
                            pass
                        else:
                            if myFileName:
                                myFileName = self.myChangeNetPath(myFileName)
                                #print myFileName
                                if fileType == 'file':
                                    #针对Arnold
                                    FileOkFlag = False
                                    if os.path.isfile(myFileName):
                                        FileOkFlag = True
                                    if not FileOkFlag:
                                        myFileName = myLocalSourcePath+'/%s' % myFileName
                                        if not os.path.isfile(myFileName):
                                            noFiles.append(fileeach)
                                else:
                                    if not os.path.isdir(myFileName):
                                        noFiles.append(fileeach)
            outPutSets(noFiles, NoTypeSets)
            return noFiles

        #拷贝某些贴图节点的文件
        def myCheck_VrSetFilesModel(typeOn, typeModel, typeFuleAttr, numModel, NoTypeSets):
            nofile = []
            try:
                if mc.getAttr("vraySettings.%s" % typeOn):
                    if mc.getAttr('vraySettings.%s' % typeModel) == numModel:
                        localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
                        if not os.path.isfile(localFile):
                            nofile.append('vraySettings')
                            
            except:
                pass
            outPutSets(nofile, NoTypeSets)
            return nofile

        #检查arnold代理
        def myCheck_AiStandIn():
            #检查Arnold的代理
            # ArType = 'aiStandIn'
            # ArAttr = 'dso'
            # ArSets = 'sortNo_AiStandIn_set'
            # ArFileType = 'file'

            myLocalSourcePath = mc.workspace(en='sourceimages')
            noFiles = []
            noArnoldFile = []
            try:
                allFiles = mc.ls(type = 'aiStandIn')
            except:
                pass
            else:
                if allFiles:
                    serverFile = []
                    for fileeach in allFiles:
                        try:
                            myFileName = mc.getAttr('%s.dso' % fileeach)
                        except:
                            pass
                        else:
                            FileOkFlag = False
                            if myFileName:
                                myFileName = self.myChangeNetPath(myFileName)
                                if os.path.isfile(myFileName):
                                    FileOkFlag = True
                                if not FileOkFlag:
                                    myFileName = myLocalSourcePath+'/%s' % myFileName
                                    if os.path.isfile(myFileName):
                                        FileOkFlag = True
                                        # noFiles.append(fileeach)

                                #检查文件中的代理在代理库中是否有
                                if self.copyType == 1 and not FileOkFlag:
                                    proxyName = os.path.basename(myFileName)
                                    dirName = proxyName.split('_')[0]
                                    proxyPaths = mc.getFileList(folder = '%s'%OCT_ArnoldPathNew)
                                    for i in proxyPaths:
                                        path = os.path.join(OCT_ArnoldPathNew, i, dirName, r'sourceimages', r'arnoldtex', proxyName)
                                        path = path.replace('\\', '/')
                                        if os.path.isfile(path):
                                            FileOkFlag = True
                                            serverFile.append(fileeach)
                                            break

                                    if not FileOkFlag :
                                        noFiles.append(fileeach)

                                elif FileOkFlag:
                                    #代理路径限制
                                    #提交代理必须在工程目录sourceimages\arnoldtex下，代理贴图文件夹也要在相应的路径下
                                    arnoldProxyName = os.path.basename(myFileName)
                                    sourcePath = os.path.join(myLocalSourcePath, r'arnoldtex', arnoldProxyName)
                                    if not os.path.isfile(sourcePath):
                                        serverFile.append(fileeach)
                                        # noArnoldFile.append(fileeach)

                                    dirName = arnoldProxyName.split('_')[0]

                                    myLocalSourceFilePath = os.path.join(myLocalSourcePath, r'arnoldtex', dirName)
                                    SourceFilePath = os.path.join(os.path.dirname(myFileName), dirName)

                                    if not os.path.isdir(myLocalSourceFilePath):
                                        if not os.path.isdir(SourceFilePath):
                                            noArnoldFile.append(fileeach)
                                        else:
                                            if fileeach not in serverFile:
                                                serverFile.append(fileeach)

                                elif not FileOkFlag:
                                    noFiles.append(fileeach)

                            else:
                                noFiles.append(fileeach)


                    outPutSets(serverFile, 'sortWarning_AiStandIn_set')
                    if serverFile:
                        mc.confirmDialog(title=u'警告', message=u'有 %s 个aiStandIn，并存在 "%s"的set节点下\n' % (len(serverFile), 'sortWarning_AiStandIn_set'))
            
            outPutSets(noArnoldFile, 'sortNo_AiStandIn_Tex_set')                   
            outPutSets(noFiles, 'sortNo_AiStandIn_set')
            return noFiles, noArnoldFile

        #错误数量
        numnoTexFiles = 0
        numNoCacheFiles = 0
        numWrongCacheFiles = 0
        numNoYetiCacheFiles = 0
        numWrongYetiTexFiles = []
        numNoYetiTexFiles = []
        numNoAbcCacheFiles = 0
        numWrongAbcCacheFiles=0
        numNoParticle = 0
        numNorfParFiles = 0
        numNorfMeshFiles = 0
        numNocamImFiles = 0
        #Mr
        numNoMrIblFiles = 0
        numNoMrTxFiles = 0
        #Vray
        numNoVRayMeshFiles = 0
        numNoVrIesLFiles = 0
        numNoVrIrrMapFiles = 0
        numNoVrLightCFiles = 0
        numNoVrCausticsFiles = 0
        #Arnold
        numNoAiStandInhFiles = 0
        numNoArnoldFiles = 0
        numNoArIesLFiles = 0
        #Shave
        numNoShaveCacheFiles = 0
        

        #检查摄像机投影贴图
        camImType = 'imagePlane'
        camImAttr = 'imageName'
        camImFileType = 'file'
        camImSets = 'sortNo_imagePlan_set'
        nocamImFiles = myCheck_FileOrFolderModel(camImType, camImAttr, camImFileType, camImSets)
        #检查Realflow的particles粒子和Meshs缓存
        #检查RF的particles缓存
        rfParType = 'RealflowEmitter'
        rfParAttr = 'Paths[0]'
        rfParFileType = 'path'
        rfParSets = 'sortNo_RealflowEmitter_set'
        norfParFiles = myCheck_FileOrFolderModel(rfParType, rfParAttr, rfParFileType, rfParSets)
        #检查RF的meshs缓存
        rfMeshType = 'RealflowMesh'
        rfMeshAttr = 'Path'
        rfMeshFileType = 'file'
        rfMeshSets = 'sortNo_RealflowMesh_set'
        norfMeshFiles = myCheck_FileOrFolderModel(rfMeshType, rfMeshAttr, rfMeshFileType, rfMeshSets)

        if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
            #检查mentalrayIblShape节点的贴图
            mrIblType = 'mentalrayIblShape'
            mrIblAttr = 'texture'
            mrIblFileType = 'file'
            mrIblSets = 'sortNo_mentalrayIblShape_set'
            noMrIblFiles = myCheck_FileOrFolderModel(mrIblType, mrIblAttr, mrIblFileType, mrIblSets)
            #检查mentalrayTexture节点的贴图
            mrTxType = 'mentalrayTexture'
            mrTxAttr = 'fileTextureName'
            mrTxFileType = 'file'
            mrTxSets = 'sortNo_mentalrayTexture_set'
            noMrTxFiles = myCheck_FileOrFolderModel(mrTxType, mrTxAttr, mrTxFileType, mrTxSets)
            #统计错误
            numNoMrIblFiles = len(noMrIblFiles)
            numNoMrTxFiles = len(noMrTxFiles)

        if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
            #检查Vray的代理
            VrType = 'VRayMesh'
            VrAttr = 'fileName'
            VrSets = 'sortNo_VRayMesh_set'
            VrFileType = 'file'
            noVRayMeshFiles = myCheck_FileOrFolderModel(VrType, VrAttr, VrFileType, VrSets)
            #检查Vray的VRayLightIESShape灯光贴图
            VrIesLType = 'VRayLightIESShape'
            VrIesLAttr = 'iesFile'
            VrIesLFileType = 'file'
            VrIesLSets = 'sortNo_VRayLightIESShape_set'
            noVrIesLFiles = myCheck_FileOrFolderModel(VrIesLType, VrIesLAttr, VrIesLFileType, VrIesLSets)
            #Irradiance map光子贴图
            VrIrrMap_typeOn = 'giOn'
            VrIrrMap_typeModel = 'imap_mode'
            VrIrrMap_typeFuleAttr = 'imap_fileName'
            VrIrrMap_numModel = 2
            VrIrrMapSets = 'sortNo_VrayIrradianceMap_set'
            noVrIrrMapFiles = myCheck_VrSetFilesModel(VrIrrMap_typeOn, VrIrrMap_typeModel, VrIrrMap_typeFuleAttr, VrIrrMap_numModel, VrIrrMapSets)
            #Light cache map光子贴图
            VrLightC_typeOn = 'giOn'
            VrLightC_typeModel = 'mode'
            VrLightC_typeFuleAttr = 'fileName'
            VrLightC_numModel = 2
            VrLightCSets = 'sortNo_VrayLightCacheMap_set'
            noVrLightCFiles = myCheck_VrSetFilesModel(VrLightC_typeOn, VrLightC_typeModel, VrLightC_typeFuleAttr, VrLightC_numModel, VrLightCSets)
            #Caustics的焦散贴图
            VrCaustics_typeOn = 'causticsOn'
            VrCaustics_typeModel = 'causticsMode'
            VrCaustics_typeFuleAttr = 'causticsFile'
            VrCaustics_numModel = 1
            VrCausticsSets = 'sortNo_CausticsMap_set'
            noVrCausticsFiles = myCheck_VrSetFilesModel(VrCaustics_typeOn, VrCaustics_typeModel, VrCaustics_typeFuleAttr, VrCaustics_numModel, VrCausticsSets)
            #统计错误
            numNoVRayMeshFiles = len(noVRayMeshFiles)
            numNoVrIesLFiles = len(noVrIesLFiles)
            numNoVrIrrMapFiles = len(noVrIrrMapFiles)
            numNoVrLightCFiles = len(noVrLightCFiles)
            numNoVrCausticsFiles = len(noVrCausticsFiles)
            
        if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
            # #检查Arnold的代理
            noAiStandInhFiles, noArnoldFiles = myCheck_AiStandIn()
            # ArType = 'aiStandIn'
            # ArAttr = 'dso'
            ArSets = 'sortNo_AiStandIn_set'

            WarnArSets = 'sortNo_AiStandIn_Tex_set'
            # ArFileType = 'file'
            # noAiStandInhFiles = myCheck_FileOrFolderModel(ArType, ArAttr, ArFileType, ArSets)
            #检查Arnold的aiPhotometricLight灯光贴图
            ###################
            #改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
            ####################
            ArIesLType = 'aiPhotometricLight'
            ArIesLAttr = 'aiFilename'
            ArIesLFileType = 'file'
            ArIesLSets = 'sortNo_aiPhotometricLight_set'
            noArIesLFiles = myCheck_FileOrFolderModel(ArIesLType, ArIesLAttr, ArIesLFileType, ArIesLSets)
            #统计错误
            numNoAiStandInhFiles = len(noAiStandInhFiles)
            numNoArnoldFiles = len(noArnoldFiles)
            numNoArIesLFiles = len(noArIesLFiles)

        ErrorText = u''
        numnoTexFiles = len(noTexFiles)
        numnoArnoldTxFiles = len(noArnoldTxTexFiles)
        numNoCacheFiles = len(noCacheFiles)
        numWrongCacheFiles = len(wrongCacheFiles)
        numNoYetiCacheFiles = len(noYetiCacheFiles)
        numWrongYetiTexFiles = len(wrongYetiTexFiles )
        numNoYetiTexFiles = len(noYetiTexFiles )
        numNoAbcCacheFiles = len(noAbcCacheFiles)
        numWrongAbcCacheFiles=len(wrongAbcCacheFiles)
        numNoParticle = len(noParticle)
        numNorfParFiles = len(norfParFiles)
        numNorfMeshFiles = len(norfMeshFiles)
        numNocamImFiles = len(nocamImFiles)
        numNoShaveCacheFiles = len(noShaveCacheFiles)

        numNoFiles = (numnoTexFiles + numnoArnoldTxFiles + numNoCacheFiles + numWrongCacheFiles + numNoYetiCacheFiles + numWrongYetiTexFiles + numNoYetiTexFiles + numNoAbcCacheFiles +
                      numWrongAbcCacheFiles+numNoParticle + numNorfParFiles + numNorfMeshFiles + numNocamImFiles + numNoMrIblFiles + numNoMrTxFiles + numNoVRayMeshFiles + numNoVrIesLFiles +
                      numNoVrIrrMapFiles + numNoVrLightCFiles + numNoVrCausticsFiles + numNoAiStandInhFiles + numNoArnoldFiles + numNoArIesLFiles + numNoShaveCacheFiles)

        if numNoFiles > 0:
            ErrorText += u'文件存在以下错误：\n在输入的路径下，相应文件或文件夹并不存在!\n有以下类型的节点:\n\n'
            if numnoTexFiles:
                ErrorText += u'有 %s 个 file 贴图文件,并存在"%s"的sets节点下\n' % (numnoTexFiles, 'sortNo_TexFiles_sets')
            if numnoArnoldTxFiles:
                ErrorText += u'有 %s 个 file Arnold的Tx贴图文件,并存在"%s"的sets节点下\n' % (numnoArnoldTxFiles, 'sortNo_ArnoldTxFiles_sets')
            if numNoCacheFiles:
                ErrorText += u'有 %s 个 cacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoCacheFiles, 'sortNo_CacheFiles_sets')
            # if numWrongCacheFiles:
            #     ErrorText += u'有 %s 个 cacheFile 缓存文件没有放在本工程的data目录下,并存在"%s"的sets节点下\n' % (numWrongCacheFiles, 'sortWrong_CacheFiles_sets')
            if numNoYetiCacheFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti毛发缓存文件,并存在"%s"的sets节点下\n' % (numNoYetiCacheFiles, 'sortWrong_pgYetiMaya_CacheFiles_sets')
            if numWrongYetiTexFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti毛发贴图路径为空或最终不在“yeti”文件夹里,并存在"%s"的sets节点下\n' % (numWrongYetiTexFiles, 'sortWorng_pgYetiMaya_TexFiles_sets')
            if numNoYetiTexFiles:
                ErrorText += u'有 %s 个 pgYetiMaya Yeti指定的路径下找不到贴图,并存在"%s"的sets节点下\n' % (numNoYetiTexFiles, 'sortNo_pgYetiMaya_TexFiles_sets')
            if numNoAbcCacheFiles:
                ErrorText += u'有 %s 个 Alembic CacheFile 缓存文件,并存在"%s"的sets节点下\n' % (numNoAbcCacheFiles, 'sortNo_Alembic_CacheFiles_sets')
            if numWrongAbcCacheFiles:
                ErrorText += u'有 %s 个 Alembic CacheFile 缓存文件最终文件不在“alembic”文件夹里,并存在"%s"的sets节点下\n' % (numWrongAbcCacheFiles, 'sortWorng_Alembic_CacheFiles_sets')
            if numNoShaveCacheFiles:
                if numNoShaveCacheFiles == 1:
                    ErrorText += u'有 %s 个 Shave shaveGlobals 缓存设置找不到相应文件,并存在"%s"的sets节点下\n' % (numNoShaveCacheFiles, 'sortNo_Shave_CacheFiles_sets')
                else:
                    ErrorText += u'在Shave shaveGlobals的指定路径下有 %s 个  Shave节点找不到相应的缓存文件,并存在"%s"的sets节点下\n' % (numNoShaveCacheFiles-1, 'sortNo_Shave_CacheFiles_sets')
            if numNoParticle:
                ErrorText += u'有 %s 个 particle 缓存文件,并存在"%s"的sets节点下\n' % (numNoParticle, 'sortNo_Particl_sets')
            if numNorfParFiles:
                ErrorText += u'有 %s 个 RealflowEmitter 缓存文件,并存在"%s"的sets节点下\n' % (numNorfParFiles, rfParSets)
            if numNorfMeshFiles:
                ErrorText += u'有 %s 个 RealflowMesh 缓存文件,并存在"%s"的sets节点下\n' % (numNorfMeshFiles, rfMeshSets)
            if numNocamImFiles:
                ErrorText += u'有 %s 个 imagePlane 摄像机投影文件,并存在"%s"的sets节点下\n' % (numNocamImFiles, camImSets)
            if numNoMrIblFiles:
                ErrorText += u'有 %s 个 mentalrayIblShape MR的Image Base Lighting的环境球贴图文件,并存在"%s"的sets节点下\n' % (numNoMrIblFiles, mrIblSets)
            if numNoMrTxFiles:
                ErrorText += u'有 %s 个 mentalrayTexture MR的贴图文件,并存在"%s"的sets节点下\n' % (numNoMrTxFiles, mrTxSets)
            if numNoVRayMeshFiles:
                ErrorText += u'有 %s 个 VRayMesh Vray的代理文件,并存在"%s"的sets节点下\n' % (numNoVRayMeshFiles, VrSets)
            if numNoVrIesLFiles:
                ErrorText += u'有 %s 个 VRayLightIESShape Vray的灯光贴图,并存在"%s"的sets节点下\n' % (numNoVrIesLFiles, VrIesLSets)
            if numNoVrIrrMapFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Irradiance map光子贴图,并存在"%s"的sets节点下\n' % (numNoVrIrrMapFiles, VrIrrMapSets)
            if numNoVrLightCFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Light cache map光子贴图,并存在"%s"的sets节点下\n' % (numNoVrLightCFiles, VrLightCSets)
            if numNoVrCausticsFiles:
                ErrorText += u'有 %s 个 vraySettings Vray的Caustics的焦散贴图,并存在"%s"的sets节点下\n' % (numNoVrCausticsFiles, VrCausticsSets)
            if numNoAiStandInhFiles:
                ErrorText += u'有 %s 个 aiStandIn Arnold的代理文件,并存在"%s"的sets节点下\n' % (numNoAiStandInhFiles, ArSets)
            if numNoArnoldFiles:
                ErrorText += u'有 %s 个 aiStandIn Arnold的代理文件和代理贴图,不在工程目录\sourceimages\\arnoldtex路径,并存在"%s"的sets节点下\n' % (numNoArnoldFiles, WarnArSets)
            if numNoArIesLFiles:
                ErrorText += u'有 %s 个 aiPhotometricLight Arnold的灯光贴图,并存在"%s"的sets节点下\n' % (numNoArIesLFiles, ArIesLSets)
        if ErrorText:
            mc.warning(ErrorText)
            mc.confirmDialog(title=u'警告', message=u'%s' % ErrorText, button=['OK'], defaultButton='Yes', dismissString='No')
            try:
                mc.outlinerEditor('outlinerPanel1', e=True, ssm=True)
            except:
                pass
            return False
        try:
            mc.outlinerEditor('outlinerPanel1', e=True, ssm=False)
        except:
            pass
        return True

    #modelEditor的show改为none
    def NonePlane(self):
        a=['', 'F', 'B']
        b=['UL_panel', 'U_panel', 'UR_panel', 'L_panel', 'M_panel', 'R_panel', 'DL_panel', 'D_panel', 'DR_panel']
        for i in a:
            for j in b:
                if i=='F' or i=='B':
                    planeName='%s_%s' %(i, j)
                else:
                    planeName=j
                if mc.modelPanel(planeName, ex=True):
                    mc.modelEditor(planeName,e=True, allObjects=False)
        i=1
        while(i):
            try:
                tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
            except:
                pass
            else:
                if tmp:
                    myactivePlane = 'modelPanel%d' % i
                    break
            i+=1
        if myactivePlane:
            mc.modelEditor(myactivePlane, e=True, allObjects=False)

    def copyFile(self, *args):
        #self.NonePlane()
        if not mc.radioCollection(self.assetRadio, q=True, sl=True):
            mc.confirmDialog(title=u'温馨提示：', message=u'请选择服务器！', button=['OK'], defaultButton='Yes', dismissString='No')
        else:
            print("line 988 {}".format(self.copyType))
            print(self.myUseRender)
            # raise Exception("td check line 989")
            #检查、拷贝、提交
            #CopyJob 2 为拷贝提交模式 3为仅提交模式
            if self.copyType == 2:
                CopyJob = CopyProject()
                CopyJob.main(2, self.myUseRender)
                self.close()
            #检查、提交
            elif self.copyType == 3:
                CopyJob = CopyProject()
                CopyJob.main(3)
                self.close()

            #检查，拷贝，提交(deep)
            elif self.copyType==4:
                CopyJob = CopyProject()
                CopyJob.main(4, self.myUseRender)
                self.close()

class CopyJobThread(QtCore.QThread):
    #发射完成比例
    # percent = QtCore.pyqtSignal('int')

    def __init__(self, parent=None):
        super(CopyJobThread, self).__init__(parent)
        self.myLocalFlag = False

    def __del__(self):
        self.wait()

    def ready(self, CpauPath, FcopyPath, source, dest):
        self.myFcopyPath = FcopyPath
        self.myCpauPath = CpauPath
        self.mySourceFile = source
        self.myDestFile = dest
        self.start()

    def run(self):
        if not self.myLocalFlag:
            cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\""' % (self.myCpauPath, REMOTE_USER, REMOTE_PWD, self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
        else:
            cmd = '%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\"' % (self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break

class CopyProject(QtGui.QDialog):
    #发射完成比例
    percent = QtCore.pyqtSignal('int')

    def __init__(self, parent=None):
        super(CopyProject, self).__init__(parent)
        self.fileSName = mc.file(q=True, sn=True, shn=True)
        self.CopyLocalPath = self.getCopyPath()
        self.CpauLocalPath = self.getCPauPath()
        self.worker1 = CopyJobThread(self)
        self.worker2 = CopyJobThread(self)
        self.percent.connect(self.EditProgressWindow)
        self.stateMsg = ''
        # copyType分三种模式
        # 1 单纯拷贝模式
        # 2 拷贝提交模式
        # 3 单纯提交模式
        self.copyType = 1
        #记录渲染层星系
        self.myUseRender = []
        self.ArnoldFlag = False

    def __del__(self):
        del self.worker1, self.worker2

    def EditProgressWindow(self, i):
        mc.progressWindow(edit=True, progress=i)

    #双线程拷贝
    def CopyDataJob(self, myDict, OpenDoubleCopyFlag):
        i = 0
        for key in myDict.keys():
            if mc.progressWindow(q=True, isCancelled=True):
                while True:
                    if self.worker1.wait() and self.worker2.wait():
                        break
                return False
            mySourceFile = key
            myDestFile = myDict[key]
            if OpenDoubleCopyFlag:
                if i == 0:
                    self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                elif i == 1:
                    self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                else:
                    while True:
                        if self.worker1.isFinished():
                            self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                            break
                        elif self.worker2.isFinished():
                            self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                            break
            else:
                self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                while True:
                    if self.worker1.isFinished():
                        break
            i += 1
            self.percent.emit(i)
        while True:
            if self.worker1.wait() and self.worker2.wait():
                break
        return True

    def fileCountIn(self, dir):
        return sum([len(files) for root, dirs, files in os.walk(dir)])

    #拷贝fastcopy
    def getCopyPath(self):
        FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'
        FCOPY_SPATH_BN = os.path.basename(FCOPY_SPATH)
        FCOPY_SPATH_DN = os.path.dirname(FCOPY_SPATH)
        FCOPY_LPATH_DN = r'C:\OCTVTools\fCopy'
        cmd = ''
        if os.path.isdir(FCOPY_LPATH_DN):
            numSpath = self.fileCountIn(FCOPY_SPATH_DN)
            numLpath = self.fileCountIn(FCOPY_LPATH_DN)
            if numSpath != numLpath:
            #     cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
                cmd = r'%s /cmd=force_copy /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
        else:   # add by zhangben 20190220  copy override repeative texture
            cmd = r'%s /cmd=force_copy /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
        # cmd = r'%s /cmd=update /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)

        if cmd:
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
        return os.path.join(FCOPY_LPATH_DN, FCOPY_SPATH_BN)

    #拷贝Cpau
    def getCPauPath(self):
        CPAY_SPATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
        CPAU_LPATH_DN = r'C:\OCTVTools\CPAU'
        CPAU_LPATH_FP = r'C:\OCTVTools\CPAU\CPAU.exe'
        cmd = ''
        if not os.path.isfile(CPAU_LPATH_FP):
            # cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (self.CopyLocalPath, CPAY_SPATH, CPAU_LPATH_DN)
            cmd = r'%s /cmd=force_copy /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (self.CopyLocalPath, CPAY_SPATH, CPAU_LPATH_DN)
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
        return CPAU_LPATH_FP

    #创建文件夹命令
    def myCreateFolder(self, address):
        try:
            os.makedirs(address)
        except:
            cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (self.CpauLocalPath, REMOTE_USER, REMOTE_PWD, address)
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
                else:
                    time.sleep(0.001)
        time.sleep(0.1)

        # 创建在W盘渲染deep的文件夹
    def myCreateDeepFolder(self, address):
        try:
            os.makedirs(address)
        except:
            print address
            cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
            self.CpauLocalPath, r'octvision\rd', r'rd1234', address)
            print cmd
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
                else:
                    time.sleep(0.001)
        time.sleep(0.1)

    # 创建相应场景
    def myCreateScenes(self):
        fileSN = self.fileSName.split('_')
        while '' in fileSN:
            fileSN.remove('')
        ProjectName = '_'.join(fileSN[:3])
        if self.copyType == 2 or self.copyType == 4:
            serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSN[0], fileSN[1], fileSN[2], USERNAME,
                                        ProjectName)
        elif self.copyType == 1:
            result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel',
                                     ds='Cancel')
            if result == 'OK':
                myPath = mc.promptDialog(q=True, t=True)
                if myPath[:2] == "z:":
                    myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
                elif myPath[:2] == "Z:":
                    myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
                if os.path.isdir(myPath):
                    myPath = os.path.normpath(myPath)
                    myLastPath = myPath.split("\\")[-1]
                    myProjectName = os.path.splitext(self.fileSName)[0]
                    if myLastPath.lower() == "work":
                        ErrorFlag = True
                        if len(fileSN) >= 3:
                            # 判断服务器是否存在该工程
                            serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation',
                                                       fileSN[1], fileSN[2])
                            if os.path.isdir(serFilePath):
                                ErrorFlag = False
                                serveProject = os.path.join(myPath, fileSN[0], ProjectName)
                        if ErrorFlag:
                            fileResult = mc.confirmDialog(title=u'温馨提示',
                                                          message=u'服务器找不到相应的工程目录!\n是否直接在输入路径下按照文件名创建项目?',
                                                          button=['Yes', 'No'], defaultButton='Yes',
                                                          cancelButton='No', dismissString='No')
                            if fileResult == 'Yes':
                                serveProject = os.path.join(myPath, myProjectName)
                            else:
                                return False
                    else:
                        serveProject = os.path.join(myPath, myProjectName)
                else:
                    mc.confirmDialog(m=u'无效路径，请重新输入')
                    return False
            else:
                return False

        elif self.copyType == 5:
            myPath = r"\\file2.nas\share\ALL\transfer"
            # myPath = r"E:\b"
            if myPath[:2] == "z:":
                myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
            elif myPath[:2] == "Z:":
                myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
            if os.path.isdir(myPath):
                serveProject = os.path.join(myPath, fileSN[0], fileSN[1], fileSN[2])
            else:
                mc.confirmDialog(m=u'%s无效路径，请检查网络！' % myPath)
                return False

            self.worker1.myLocalFlag = True
            self.worker2.myLocalFlag = True

        if not os.path.isdir(serveProject):
            self.myCreateFolder(serveProject)
            exampleProject = os.path.join(r"\\octvision.com\cg\Tech", NEWPROJECT_NAME)
            copyData = {exampleProject: serveProject}
            self.CopyDataJob(copyData, True)
        return serveProject

    def myCreateImagesFolder(self):
        fileSNameSplit = self.fileSName.split('_')
        # ProjectName = os.path.splitext(self.fileSName)[0]
        serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1],
                                    fileSNameSplit[2], USERNAME)
        if not os.path.isdir(serveProject):
            self.myCreateFolder(serveProject)
        return serveProject

    #创建deep输出素材的路径  
    def myCreateDeepImagesFolder(self):
        fileSNameSplit = self.fileSName.split('_')
        # ProjectName = os.path.splitext(self.fileSName)[0]
        serveProject = os.path.join(r"\\file.com\share\VFX\Images", fileSNameSplit[0], r'Deep', fileSNameSplit[1], fileSNameSplit[2], USERNAME)
        if not os.path.isdir(serveProject):
            self.myCreateDeepFolder(serveProject)
        return serveProject

    def myChangeNetPath(self, TempPath):
        if TempPath.find('${OCTV_PROJECTS}') >= 0:
            TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
        elif TempPath.find('z:') >= 0:
            TempPath = TempPath.replace('z:', OCT_DRIVE)
        elif TempPath.find('Z:') >= 0:
            TempPath = TempPath.replace('Z:', OCT_DRIVE)
        elif TempPath.find('w:') >= 0:
            TempPath = TempPath.replace('w:', OCT_FilePath)
        elif TempPath.find('W:') >= 0:
            TempPath = TempPath.replace('W:', OCT_FilePath)
        elif TempPath.find('M:') >= 0:
            TempPath = TempPath.replace('M:', OCT_MDRIVE)
        elif TempPath.find('m:') >= 0:
            TempPath = TempPath.replace('m:', OCT_MDRIVE)
        return TempPath

    def myJudeArnoldTxFile(self, texFileName):
        PathSplitT = os.path.splitext(texFileName)
        if len(PathSplitT) > 1:
            LowerPathType = PathSplitT[1].lower()
            if (LowerPathType != '.hdr') or (LowerPathType != '.tx'):
                ArnoldTxFileName = PathSplitT[0]+'.tx'
                if os.path.isfile(ArnoldTxFileName):
                    return texFileName
                else:
                    return ArnoldTxFileName
        return False

    #拷贝所有file节点的文件并改变节点
    def myCopyType_Files(self):
        tmpCopyFlag = True
        #判断是否有使用Arnold层
        type_file = 'sourceimages'
        serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type='file')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                texFileNameGroup = []
                try:
                    texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
                except:
                    pass
                else:
                    texFirstFileName = self.myChangeNetPath(texFirstFileName)
                    #判断贴图是否开启了序列帧模式
                    #序列标识：
                    UseSeqFlag = mc.getAttr('%s.useFrameExtension' % eachfile)

                    #获取选择uvTilingMode的模式
                    UvSeqFlag = mc.getAttr('%s.uvTilingMode' % eachfile)

                    if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                        #当存在Arnold渲染器时
                        # print ("1328")
                        # if self.ArnoldFlag:
                        if mc.getAttr('defaultRenderGlobals.currentRenderer') == u"arnold":
                            # print("1330")
                            #当仅仅是复制模式时，需要把普通贴图也拷贝
                            CopyHdrFlag = False
                            if self.copyType == 1 or self.copyType == 5:
                                texFileNameGroup.append(texFirstFileName)
                                CopyHdrFlag = True
                            PathSplitT = os.path.splitext(texFirstFileName)
                            # print(PathSplitT)
                            if len(PathSplitT) > 1:
                                LowerPathType = PathSplitT[1].lower()
                                #当不是hdr贴图时，需要拷贝tx贴图
                                if LowerPathType != '.hdr':
                                    ArnoldTxFileName = ''               #  add by zhangben 2019 02 19   copy jpg
                                    if LowerPathType != ".tx":
                                        ArnoldTxFileName = PathSplitT[0]+'.tx'
                                    else:
                                        ArnoldTxFileName = PathSplitT[0]+'.jpg'
                                    if os.path.isfile(ArnoldTxFileName):
                                        texFileNameGroup.append(ArnoldTxFileName)
                                    # print("line 1349 {}".format(ArnoldTxFileName))
                                else:
                                    if not CopyHdrFlag:
                                        texFileNameGroup.append(texFirstFileName)

                        else:
                            texFileNameGroup.append(texFirstFileName)
                    #当开启了序列时
                    # elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2 :
                    #     myTexDirName = os.path.dirname(texFirstFileName)
                    #     myTexBaseName = os.path.basename(texFirstFileName)
                    #     myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
                    #     myAllFileName = os.listdir(myTexDirName)
                    #     for eachDirFileName in myAllFileName:
                    #         if eachDirFileName.find(myTexFileTopName) >= 0:
                    #             IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    #             #当存在Arnold渲染器时
                    #             if self.ArnoldFlag:
                    #                 #当仅仅是复制模式时，需要把普通贴图也拷贝
                    #                 CopyHdrFlag = False
                    #                 if self.copyType == 1 or self.copyType == 5:
                    #                     texFileNameGroup.append(IndexTexName)
                    #                     CopyHdrFlag = True
                    #                 IndexPathSplitT = os.path.splitext(IndexTexName)
                    #                 if len(IndexPathSplitT) > 1:
                    #                     IndexLowerPathType = IndexPathSplitT[1].lower()
                    #                     #当不是hdr贴图时，需要拷贝tx贴图
                    #                     if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                    #                         IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                    #                         if os.path.isfile(IndexArnoldTxFileName):
                    #                             texFileNameGroup.append(IndexArnoldTxFileName)
                    #                     else:
                    #                         if not CopyHdrFlag:
                    #                             texFileNameGroup.append(IndexTexName)
                    #             else:
                    #                 texFileNameGroup.append(IndexTexName)
                    elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2: # add by Ben  20190115
                        #print("HHHHH")
                        myTexDirName = os.path.dirname(texFirstFileName)
                        myTexBaseName = os.path.basename(texFirstFileName)
                        myTexBaseNameSpl = os.path.splitext(myTexBaseName)
                        re_isSeq = re.search('_\d+$|\.\d+$|_u\d+$|\.u\d+$', myTexBaseNameSpl[0])
                        if not re_isSeq:
                            texFileNameGroup.append(texFirstFileName)
                        else:
                            myTexFileTopName = re.sub('_\d+$|\.\d+$|_u\d+$|\.u\d+$', '', myTexBaseNameSpl[0])
                            myAllFileName = os.listdir(myTexDirName)
                            for eachDirFileName in myAllFileName:
                                # eachDirFileName = u'LYCB_ch001001Owner_head_1001.jpg'
                                # eachDirFileName = u'LYCB_ch001001Owner_head_roughees_1001.tx'
                                if eachDirFileName.find(myTexFileTopName) >= 0 and re.search('{}(_\d+|\.\d+|_u\d+|\.u\d+)'.format(myTexFileTopName), eachDirFileName):
                                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                                    # 当存在Arnold渲染器时
                                    if self.ArnoldFlag:
                                        # 当仅仅是复制模式时，需要把普通贴图也拷贝
                                        CopyHdrFlag = False
                                        if self.copyType == 1 or self.copyType == 5:
                                            if IndexTexName not in texFileNameGroup:
                                                texFileNameGroup.append(IndexTexName)
                                                print("append at ======1======{}".format(IndexTexName))
                                            CopyHdrFlag = True
                                        IndexPathSplitT = os.path.splitext(IndexTexName)
                                        if len(IndexPathSplitT) > 1:
                                            IndexLowerPathType = IndexPathSplitT[1].lower()
                                            # 当不是hdr贴图时，需要拷贝tx贴图
                                            if IndexLowerPathType != '.hdr' and not UseSeqFlag and IndexLowerPathType != '.tx':
                                                IndexArnoldTxFileName = IndexPathSplitT[0] + '.tx'
                                                if os.path.isfile(
                                                        IndexArnoldTxFileName) and IndexArnoldTxFileName not in texFileNameGroup:
                                                    texFileNameGroup.append(IndexArnoldTxFileName)
                                                    print("append at =========2=========={}".format(IndexArnoldTxFileName))
                                            else:
                                                if not CopyHdrFlag:
                                                    texFileNameGroup.append(IndexTexName)
                                                    print ("append at =============3==========={}".format(IndexTexName))
                                    else:
                                        texFileNameGroup.append(IndexTexName)
                                        print("append at ======4===========".format(IndexTexName))
                    #elif not UseSeqFlag and (UvSeqFlag == 2 or UvSeqFlag == 3):
                    elif not UseSeqFlag and UvSeqFlag == 2:
                        myTexDirName = os.path.dirname(texFirstFileName)
                        myTexBaseName = os.path.basename(texFirstFileName)
                        myTexFileTopName = myTexBaseName.split('_u')[0]
                        if not myTexFileTopName:
                            myTexFileTopName = myTexBaseName.split('_U')[0]
                        myTexFileTopNames = re.findall(r'\D+', myTexBaseName)[0]
                        myAllFileName = os.listdir(myTexDirName)
                        for eachDirFileName in myAllFileName:
                            if eachDirFileName.find(myTexFileTopName) >= 0:
                                IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                                #当存在Arnold渲染器时
                                if self.ArnoldFlag:
                                    #当仅仅是复制模式时，需要把普通贴图也拷贝
                                    CopyHdrFlag = False
                                    if self.copyType == 1 or self.copyType == 5:
                                        texFileNameGroup.append(IndexTexName)
                                        CopyHdrFlag = True
                                    IndexPathSplitT = os.path.splitext(IndexTexName)
                                    if len(IndexPathSplitT) > 1:
                                        IndexLowerPathType = IndexPathSplitT[1].lower()
                                        #当不是hdr贴图时，需要拷贝tx贴图
                                        if IndexLowerPathType != '.hdr':
                                            IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                            if os.path.isfile(IndexArnoldTxFileName):
                                                texFileNameGroup.append(IndexArnoldTxFileName)
                                        else:
                                            if not CopyHdrFlag:
                                                texFileNameGroup.append(IndexTexName)
                                else:
                                    texFileNameGroup.append(IndexTexName)
                            elif eachDirFileName.find(myTexFileTopNames) >= 0:
                                IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                                #当存在Arnold渲染器时
                                if self.ArnoldFlag:
                                    #当仅仅是复制模式时，需要把普通贴图也拷贝
                                    CopyHdrFlag = False
                                    if self.copyType == 1 or self.copyType == 5:
                                        texFileNameGroup.append(IndexTexName)
                                        CopyHdrFlag = True
                                    IndexPathSplitT = os.path.splitext(IndexTexName)
                                    if len(IndexPathSplitT) > 1:
                                        IndexLowerPathType = IndexPathSplitT[1].lower()
                                        #当不是hdr贴图时，需要拷贝tx贴图
                                        if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                            IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                            if os.path.isfile(IndexArnoldTxFileName):
                                                texFileNameGroup.append(IndexArnoldTxFileName)
                                        else:
                                            if not CopyHdrFlag:
                                                texFileNameGroup.append(IndexTexName)
                                else:
                                    texFileNameGroup.append(IndexTexName)

                    # print texFileNameGroup
                    if texFileNameGroup:
                        print texFileNameGroup
                        for texFileName in texFileNameGroup:
                            # print texFileName
                            texFileName = os.path.normpath(texFileName)
                            texFileNameS = texFileName.split('\\')
                            try:
                                indexType = texFileNameS.index(type_file)
                            except:
                                texFileNameBN = os.path.basename(texFileName)
                                serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                                copyFinalTexFilePath = serFileName
                            else:
                                serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
                                serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                                copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                            serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                            copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                            if texFileName != serFinalTexFileName:
                                #加入拷贝字典
                                #设置拷贝标帜
                                tmpCopyFlag = True
                                if os.path.isdir(serFileName):
                                    if os.path.isfile(serFinalTexFileName):
                                        testMtime = os.path.getmtime(texFileName)
                                        tmpMtime = os.path.getmtime(serFinalTexFileName)
                                        if int(tmpMtime) >= int(testMtime):
                                            tmpCopyFlag = False
                            else:
                                tmpCopyFlag = False
                            if tmpCopyFlag:
                                copyData.update({texFileName: copyFinalTexFilePath})
                        #加入设置字典，只设置第一帧
                        if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                            #数组1是Arnold
                            setData.update({eachfile: serFinalTexFileName})
                        else:
                            mySetTexDirName = os.path.dirname(serFinalTexFileName)
                            serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
                            serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
                            if self.ArnoldFlag:
                                myFirstFileName = os.path.splitext(myTexBaseName)[0]+ '.tx'
                                #serFinalSetTexFileName = os.path.splitext(serFinalSetTexFileName)[0] + '.tx'
                                serFinalSetTexFileName = os.path.join(mySetTexDirName, myFirstFileName)
                                setData.update({eachfile: serFinalSetTexFileName})
                            else:
                                setData.update({eachfile: serFinalSetTexFileName})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData)+1, status=u"正在拷贝相应的 file 贴图!")
                #拷贝文件
                if not self.CopyDataJob(copyData, True):
                    return False
            #设置路径
            for key in setData.keys():
                mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')

            # #临时拷贝Arnold贴图文件夹
            # if mc.ls(type='aiStandIn'):
            #     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
            #     ArnoldProxyCopyData = {}
            #     if os.path.isdir(myLocalArnoldSourcePath):
            #         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
            #         serArnoldFileName = serFileName + '\\arnoldTex'
            #         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
            #         #拷贝文件
            #         if not self.CopyDataJob(ArnoldProxyCopyData, True):
            #             return False
        return True

    def myCopy_Data(self):
        #type_file = 'data'
        types_file = ['data', 'cache']
        other_file = 'otherCache'
        setSercachePath = ''
        # serFileName = os.path.join(self.serveProject, type_file)
        allfiles = mc.ls(type='cacheFile')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    cachePath = mc.getAttr('%s.cachePath' % eachfile)
                except:
                    pass
                else:
                    cachePath = self.myChangeNetPath(cachePath)
                    if OCT_MDRIVE in cachePath or OCT_FilePath in cachePath:
                        continue
                    cachePath = os.path.normpath(cachePath)
                    cachePathS = cachePath.split('\\')
                    for types in types_file:
                        try:
                            indexType = cachePathS.index(types)
                            break
                        except:
                            pass
                    if indexType:
                        serLastcachePath = '\\'.join(cachePathS[indexType::])
                        copyFinalcachePath = os.path.join(self.serveProject, serLastcachePath)
                    else:
                        copyFinalcachePath = os.path.join(self.serveProject, types, other_file)
                    # try:
                    #     indexType = cachePathS.index(type_file)
                    # except:
                    #     copyFinalcachePath = os.path.join(serFileName, other_file)
                    # else:
                    #     serLastcachePath = '\\'.join(cachePathS[indexType+1::])
                    #     copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                    setSercachePath = '\\'.join(cachePathS[indexType::])
                    copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                    if cachePath != copyFinalcachePath:
                        #整体文件夹拷贝
                        if cachePath!= copyFinalcachePath:
                            copyData.update({cachePath: copyFinalcachePath})
                        #设置列表
                        setData.update({eachfile: copyFinalcachePath})
                       
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 caChe 缓存!")
                #拷贝文件
                if not self.CopyDataJob(copyData, False):
                    return False
            #设置路径
            for key in setData.keys():
                try:
                    mc.setAttr('%s.cachePath' % key, setData[key], type='string')
                except:
                    mc.warning(u'cacheFile设置文件出错！')
                    return False
        return True

    #拷贝Yeti缓存和贴图
    def myCopy_YetiCache(self):
        #缓存
        type_file = 'cache'
        other_file = 'otherCache'
        setSercachePath = ''
        serFileName = os.path.join(self.serveProject, type_file)
        serFileName = os.path.normpath(serFileName)
        #贴图
        type_TexFile = 'sourceimages'
        serTexFileName = os.path.join(self.serveProject, type_TexFile)
        serFileName = os.path.normpath(serFileName)
        allYetiCacheFiles = mc.ls(type='pgYetiMaya')
        setTexData = {}
        #进行
        setSerTexPath = ''
        copyData = {}
        setData = {}
        if allYetiCacheFiles:
            for myYetiCacheFile in allYetiCacheFiles:
                YetiFileMode = None
                try:
                    YetiFileMode = mc.getAttr('%s.fileMode' % myYetiCacheFile)
                except:
                    pass
                else:
                    if YetiFileMode == 1:
                        YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
                        if YetiCachePath:
                            YetiCachePath = self.myChangeNetPath(YetiCachePath)
                            YetiCachePath = os.path.normpath(YetiCachePath)
                            cachePathS = YetiCachePath.split('\\')
                            try:
                                indexType = cachePathS.index(type_file)
                            except:
                                copyFinalcachePath = os.path.join(serFileName, other_file, '%s' %myYetiCacheFile)
                            else:
                                serLastcachePath = '\\'.join(cachePathS[indexType+1:-1])
                                copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                            YetiCacheBasePath = os.path.basename(YetiCachePath)
                            YetiCacheDirPath = os.path.dirname(YetiCachePath)
                            setSercachePath = os.path.join(copyFinalcachePath, YetiCacheBasePath)
                            copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                            #整体文件夹拷贝
                            if YetiCacheDirPath!= copyFinalcachePath:
                                copyData.update({YetiCacheDirPath: copyFinalcachePath})
                                setSercachePath = setSercachePath.replace("\\", "/")
                                setData.update({myYetiCacheFile: setSercachePath})
                    #拷贝和设置贴图
                    YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
                    if YetiTexPath:
                        YetiTexPath = self.myChangeNetPath(YetiTexPath)
                        if os.path.isdir(YetiTexPath):
                            copyFinalTexPath = os.path.join(serTexFileName, "Yeti")
                            YetiTexPath = os.path.normpath(YetiTexPath)
                            if YetiTexPath != copyFinalTexPath:
                                copyData.update({YetiTexPath: copyFinalTexPath})
                                setTexData.update({myYetiCacheFile: copyFinalTexPath})

                    if copyData:
                        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 pgYetiMaya Yeti缓存!")
                        #拷贝文件
                        if not self.CopyDataJob(copyData, False):
                            return False
                    #设置路径
                    for key in setData.keys():
                        try:
                            mc.setAttr('%s.cacheFileName' % key, setData[key], type='string')
                        except:
                            mc.warning(u'Yeti的缓存设置文件出错！')
                            return False
                    for key in setTexData.keys():
                        try:
                            mc.setAttr('%s.imageSearchPath' % key, setTexData[key], type='string')
                        except:
                            mc.warning(u'Yeti的贴图设置文件出错！')
                            return False
        return True

    #拷贝所有ABC的data节点的文件并改变节点
    def myCopy_AbcData(self):
        tmpCopyFlag = True
        type_file = 'alembic'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        allfiles = mc.ls(type='AlembicNode')
        copyData = {}
        setData = {}
        if allfiles:
            for eachfile in allfiles:
                try:
                    abcCachePath = mc.getAttr('%s.abc_File' % eachfile)
                except:
                    pass
                else:
                    abcCachePath = self.myChangeNetPath(abcCachePath)
                    abcCachePath = os.path.normpath(abcCachePath)
                    mc.setAttr('%s.abc_File' % eachfile, abcCachePath, type = 'string')
                    abcCachePath_S = abcCachePath.split('\\')
                    #多层目录
                    copyFinalAbcCachePath = ''
                    try:
                        indexType = abcCachePath_S.index(type_file)
                    except:
                        abcCachePathBN = os.path.basename(abcCachePath)
                        serFinalAbcCachePath = os.path.join(serFileName, abcCachePathBN)
                        copyFinalAbcCachePath = serFileName
                        copyFinalAbcCachePath_dir = serFileName
                    else:
                        serLastAbcCachePath = '\\'.join(abcCachePath_S[indexType+1::])
                        copyFinalAbcCachePath = os.path.join(serFileName, serLastAbcCachePath)
                        copyFinalAbcCachePath_dir = os.path.dirname(copyFinalAbcCachePath)
                    if copyFinalAbcCachePath:
                        copyFinalAbcCachePath = os.path.normpath(copyFinalAbcCachePath)
                        copyFinalAbcCachePath_dir = os.path.normpath(copyFinalAbcCachePath_dir)
                        if abcCachePath != copyFinalAbcCachePath:
                            #拷贝列表
                            #设置拷贝标帜
                            tmpCopyFlag = True
                            if os.path.isdir(serFileName):
                                if os.path.isfile(copyFinalAbcCachePath):
                                    testMtime = os.path.getmtime(abcCachePath)
                                    tmpMtime = os.path.getmtime(copyFinalAbcCachePath)
                                    if int(tmpMtime) >= int(testMtime):
                                        tmpCopyFlag = False
                            if tmpCopyFlag:
                                copyData.update({abcCachePath: copyFinalAbcCachePath_dir})
                            #设置列表
                            setData.update({eachfile: copyFinalAbcCachePath})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Alembic caChe 缓存!")
                #拷贝文件
                if not self.CopyDataJob(copyData, False):
                    return False
            #设置路径
            for key in setData.keys():
                if os.path.isfile(setData[key]):
                    mc.setAttr('%s.abc_File' % key, setData[key], type='string')
        return True

    #拷贝所有Shave缓存
    def myCopy_Shavedata(self):
        tmpCopyFlag = True
        type_file = 'shave'
        serFileName = os.path.join(self.serveProject, 'cache\\'+type_file)
        copyData = {}
        setData = {}
        allOnlyShaveShapes = []
        allShaveShapes = mc.ls(type='shaveHair')
        for eachShape in allShaveShapes:
            allOnlyShaveShapes.append(eachShape.split("|")[-1])
        allShaveOnlyNames = []
        for OnlyShaveShape in allOnlyShaveShapes:
            allShaveOnlyNames.append("shaveStatFile_%s" % OnlyShaveShape)
        allOnlyShaveShapes = list(set(allOnlyShaveShapes))
        myshaveGlobals = "shaveGlobals"
        if allShaveShapes and myshaveGlobals:
            shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
            if shavePath:
                shavePath = self.myChangeNetPath(shavePath)
                if not os.path.isdir(shavePath):
                    proPath = mc.workspace(q=True, rd=True)
                    shavePath = os.path.normpath(os.path.join(proPath, shavePath))
                shavePath = self.myChangeNetPath(shavePath)
                if os.path.isdir(shavePath):
                    allSahveDirs = os.listdir(shavePath)
                    if allSahveDirs:
                        #多层目录
                        shavePath = os.path.normpath(shavePath)
                        shaveCachePath_S = shavePath.split('\\')
                        try:
                            indexType = shaveCachePath_S.index(type_file)
                        except:
                            shaveCachePathBN = os.path.basename(shavePath)
                            serFinalShaveCachePath = os.path.join(serFileName, shaveCachePathBN)
                            copyFinalShaveCacheDir = serFileName
                        else:
                            serLastShaveCachePath = '\\'.join(shaveCachePath_S[indexType+1::])
                            copyFinalShaveCacheDir = os.path.join(serFileName, serLastShaveCachePath)
                        copyFinalShaveCacheDir = os.path.normpath(copyFinalShaveCacheDir)
                        #整体文件夹拷贝
                        #单文件，赛选时间重复拷贝
                        if os.path.isdir(copyFinalShaveCacheDir):
                            if copyFinalShaveCacheDir!= copyFinalShaveCacheDir:
                                copyData.update({copyFinalShaveCacheDir: copyFinalShaveCacheDir})
                        setData.update({myshaveGlobals: copyFinalShaveCacheDir})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Shave caChe 缓存!")
                    #拷贝文件
                    if not self.CopyDataJob(copyData, False):
                        return False
                #设置路径
                for key in setData.keys():
                    mc.setAttr('%s.tmpDir' % key, setData[key], type='string')
        return True
       
    #拷贝粒子缓存
    def myCopy_Particles(self):
        tmpCopyFlag = True
        type_file = 'particles'
        type_cache = 'cache'
        serFileName = os.path.join(self.serveProject, type_cache, type_file)
        AllIsParFlag = False
        myAllParticles = mc.ls(type='particle')
        for eachP in myAllParticles:
            if mc.nodeType(eachP) == 'particle':
                AllIsParFlag = True
                break
        mydynGlobals = mc.dynGlobals(q=True, a=True)
        copyData = {}
        if mydynGlobals and AllIsParFlag:
            fileShortName = os.path.splitext(self.fileSName)[0]
            #parPath = mc.workspace(en='particles')
            parPath = mc.workspace(fullName=True)+"/cache/particles"
            cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
            if not cacheDirectory:
                cacheDirectory = fileShortName
            parCachePath = os.path.join(parPath, cacheDirectory)
            parCachePath = os.path.normpath(parCachePath)
            parCacheSPath = os.path.join(parPath, cacheDirectory+'_startup')
            parCacheSPath = os.path.normpath(parCacheSPath)
            #粒子缓存文件
            if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
                if os.path.isdir(parCachePath):
                    if cacheDirectory != 'untitled':
                        serFinalPerPath = os.path.join(serFileName, cacheDirectory)
                    else:
                        serFinalPerPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory)
                    serFinalPerPath = os.path.normpath(serFinalPerPath)
                    #整个文件拷贝方式
                    if parCachePath != serFinalPerPath:
                        copyData.update({parCachePath: serFinalPerPath})
            #拷贝初始化缓存方案
            if not os.path.isdir(parCacheSPath):
                cacheDirectory = fileShortName
                parCacheSPath = os.path.join(parPath, cacheDirectory+'_startup')
            #粒子初始化文件
            if os.path.isdir(parCacheSPath):
                if cacheDirectory != 'untitled':
                    serFinalPerSPath = os.path.join(serFileName, cacheDirectory+'_startup')
                else:
                    serFinalPerSPath = os.path.join(serFileName, fileShortName+'_'+cacheDirectory+'_startup')
                serFinalPerSPath = os.path.normpath(serFinalPerSPath)
                #整个文件拷贝方式
                if parCacheSPath != serFinalPerSPath:
                    copyData.update({parCacheSPath: serFinalPerSPath})
            if copyData:
                mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 particle缓存!")
                #拷贝文件
                if not self.CopyDataJob(copyData, False):
                    return False
            #设置粒子缓存的新文件名
            if cacheDirectory == 'untitled':
                parCacheNName = fileShortName+'_'+cacheDirectory
                mc.setAttr('%s.cacheDirectory' % mydynGlobals, parCacheNName, type='string')
        return True

    #拷贝Vray、Arnold代理、某些贴图节点的文件
    def myCopy_Proxy_OImagesModel(self, myType, mtAttr):
        tmpCopyFlag = True
        myLocalSourcePath = mc.workspace(en='sourceimages')
        try:
            allTypeShapes = mc.ls(type=myType)
        except:
            pass
        else:
            if allTypeShapes:
                copyData = {}
                setData = {}
                type_file = 'sourceimages'
                serFileName = os.path.join(self.serveProject, type_file)
                for shapeEach in allTypeShapes:
                    try:
                        myFilepath = mc.getAttr('%s.%s' % (shapeEach, mtAttr))
                    except:
                        pass
                    else:
                        if myFilepath:
                            myFilepath = self.myChangeNetPath(myFilepath)
                            #获取文件名
                            FileOkFlag = False
                            if os.path.isfile(myFilepath):
                                FileOkFlag = True
                            if not FileOkFlag:
                                myFilepath = myLocalSourcePath+'/%s' % myFilepath
                                if os.path.isfile(myFilepath):
                                    FileOkFlag = True
                            if FileOkFlag:
                                myFileBaseName = os.path.basename(myFilepath)
                                #最终网络文件名
                                myFinalName = os.path.join(serFileName, myFileBaseName)
                                myFinalName = os.path.normpath(myFinalName)
                                #原始的文件地址
                                myFilepath = os.path.normpath(myFilepath)
                                #服务器地址
                                serFileName = os.path.normpath(serFileName)
                                if myFilepath != myFinalName:
                                    #加入拷贝文件
                                   #设置拷贝标帜
                                    tmpCopyFlag = True
                                    if os.path.isdir(serFileName):
                                        if os.path.isfile(myFinalName):
                                            testMtime = os.path.getmtime(myFilepath)
                                            tmpMtime = os.path.getmtime(myFinalName)
                                            if int(tmpMtime) >= int(testMtime):
                                                tmpCopyFlag = False
                                    if tmpCopyFlag:
                                        copyData.update({myFilepath: serFileName})
                                    #加入设置字典
                                    setData.update({shapeEach: myFinalName})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 %s 文件!" % myType)
                    #拷贝文件
                    if not self.CopyDataJob(copyData, True):
                        return False
                for key in setData.keys():
                    mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
        return True

    #拷贝arnold代理文件和贴图
    def myCopy_Ar_Proxy(self):
        #判断arnold代理是否拷贝至服务器
        print("line 1936 ========={}".format(self.copyType))
        # raise Exception("Trigger a exception")
        if self.copyType != 1:
            mValue = mc.radioButtonGrp('ArnoldProxy', q=True, sl=True)
            if mValue == 2:
                return True

        myType = 'aiStandIn'
        mtAttr = 'dso'
        tmpCopyFlag = True
        myLocalSourcePath = mc.workspace(en='sourceimages')
        try:
            allTypeShapes = mc.ls(type = myType)
        except:
            pass
        else:
            if allTypeShapes:
                copyData = {}
                setData = {}
                type_file = 'sourceimages'
                serFileName = os.path.join(self.serveProject, type_file)
                print serFileName
                print "\\n"
                for shapeEach in allTypeShapes:
                    try:
                        myFilepath = mc.getAttr('%s.dso' % shapeEach)
                    except:
                        pass
                    else:
                        if myFilepath:
                            myFilepath = self.myChangeNetPath(myFilepath)
                            #获取文件名
                            FileOkFlag = False
                            if os.path.isfile(myFilepath):
                                FileOkFlag = True
                            if not FileOkFlag:
                                myFilepath = myLocalSourcePath+'/%s' % myFilepath
                                if os.path.isfile(myFilepath):
                                    FileOkFlag = True
                            # print("line 1975 file ok ??? {}".format(FileOkFlag))
                            if FileOkFlag:
                                myFilepath = myFilepath.replace('/','\\')
                                texFileNameS = myFilepath.split('\\')
                                indexType = texFileNameS.index(type_file)
                                # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
                                myFileBaseName = os.path.basename(myFilepath)

                                #最终网络文件名
                                myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)
                                myFinalName = os.path.normpath(myFinalName)
                                #原始的文件地址
                                myFilepath = os.path.normpath(myFilepath)
                                #服务器地址
                                copyFinalTexFilePath = os.path.dirname(myFinalName)
                                copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                                print copyFinalTexFilePath
                                if myFilepath != myFinalName:
                                    #加入拷贝文件
                                    #设置拷贝标帜
                                    tmpCopyFlag = True
                                    tempSetFlag = False
                                    if os.path.isdir(serFileName):
                                        if os.path.isfile(myFinalName):
                                            testMtime = os.path.getmtime(myFilepath)
                                            tmpMtime = os.path.getmtime(myFinalName)
                                            if int(tmpMtime) >= int(testMtime):
                                                tmpCopyFlag = False
                                                tempSetFlag =True
                                    if tmpCopyFlag:
                                        tempSetFlag =True
                                        copyData.update({myFilepath: copyFinalTexFilePath})

                                    if tempSetFlag:
                                        #加入设置字典
                                        setData.update({shapeEach: myFinalName})

                                #拷贝arnold贴图
                                myArFilePath = os.path.dirname(myFilepath)
                                myArFileName = os.path.basename(myFilepath)
                                myArImageFolder = myArFileName.split('_')[0]
                                #原贴图文件夹
                                myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
                                myFinalImageFolder = os.path.join(serFileName, r'arnoldtex', myArImageFolder)
                                if os.path.isdir(myArFilePaths):
                                    copyData.update({myArFilePaths: myFinalImageFolder})
                            # print("line 2020 {}".format(FileOkFlag))
                            # raise Exception("Check lin 2020")
                            if self.copyType == 1 and not FileOkFlag:
                                # print("line 2023::: enter fileokflag not ok")
                                # myFilepath = myFilepath.replace('/','\\')
                                # texFileNameS = myFilepath.split('\\')
                                # indexType = texFileNameS.index(type_file)
                                # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
                                myFileBaseName = os.path.basename(myFilepath)
                                
                                #最终网络文件名
                                #myFinalName = os.path.join(serFileName, myFileBaseName)
                                myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)


                                #原始的文件地址
                                dirName = myFileBaseName.split('_')[0]
                                arProxyPathName = ''
                                proxyPaths = mc.getFileList(folder = '%s'%OCT_ArnoldPathNew)
                                for i in proxyPaths:
                                    paths = os.path.join(OCT_ArnoldPathNew, i, dirName, r'sourceimages', r'arnoldtex', myFileBaseName)
                                    paths = paths.replace('/', '\\')
                                    if os.path.isfile(paths):
                                        arProxyPathName = paths
                                        break

                                if arProxyPathName:
                                    copyFinalTexFilePath = os.path.dirname(myFinalName)
                                    copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                                    if arProxyPathName != myFinalName:
                                        #加入拷贝文件
                                        #设置拷贝标帜
                                        tmpCopyFlag = True
                                        tempSetFlag = False
                                        if os.path.isdir(serFileName):
                                            if os.path.isfile(myFinalName):
                                                testMtime = os.path.getmtime(arProxyPathName)
                                                tmpMtime = os.path.getmtime(myFinalName)
                                                if int(tmpMtime) >= int(testMtime):
                                                    tmpCopyFlag = False
                                                    tempSetFlag =True
                                        if tmpCopyFlag:
                                            tempSetFlag =True
                                            copyData.update({arProxyPathName: copyFinalTexFilePath})

                                        if tempSetFlag:
                                            #加入设置字典
                                            setData.update({shapeEach: myFinalName})
                                            
                                #拷贝arnold贴图
                                myArFilePath = os.path.dirname(arProxyPathName)
                                myArFileName = os.path.basename(arProxyPathName)
                                myArImageFolder = myArFileName.split('_')[0]
                                # print("line 2073 copy  arnold texutre to folder ====>{}".format(myArImageFolder))
                                #原贴图文件夹
                                myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
                                myFinalImageFolder = os.path.join(copyFinalTexFilePath, myArImageFolder)
                                # print("line 2077 the source image folder is :::: {}".format(myFinalImageFolder))
                                if os.path.isdir(myArFilePaths):
                                    copyData.update({myArFilePaths: myFinalImageFolder})
                                raise Exception("td check copy texture")
                print("line 2083")
                for eachDate in copyData:
                    print eachDate
                # self.CopyDataJob(copyData,True)
                # raise Exception("Td Check line 2085")
                if copyData:
                    print("line 2076 ::: now ready to copy  aiStandin")
                    #mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 aiStandIn 文件!")
                    #拷贝文件
                    if not self.CopyDataJob(copyData, True):
                        return False

                if setData:
                    for key in setData.keys():
                        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
        return True

         # #临时拷贝Arnold贴图文件夹
            # if mc.ls(type='aiStandIn'):
            #     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
            #     ArnoldProxyCopyData = {}
            #     if os.path.isdir(myLocalArnoldSourcePath):
            #         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
            #         serArnoldFileName = serFileName + '\\arnoldTex'
            #         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
            #         #拷贝文件
            #         if not self.CopyDataJob(ArnoldProxyCopyData, True):
            #             return False

    #拷贝Vr光子贴图、焦散贴图
    def myCopy_VrSetFilesModel(self, typeOn, typeModel, typeFuleAttr, numModel):
        tmpCopyFlag = True
        copyData = {}
        typeName = ''
        type_file = 'sourceimages'
        serFileName = os.path.join(self.serveProject, type_file)
        try:
            if mc.getAttr("vraySettings.%s" % typeOn):
                if mc.getAttr('vraySettings.%s' % typeModel) == numModel:
                    localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
                    if localFile:
                        localFile = self.myChangeNetPath(localFile)
                        locaFileBaseName = os.path.basename(localFile)
                        serFileFinalName = os.path.join(serFileName, locaFileBaseName)
                        serFileFinalName = os.path.normpath(serFileFinalName)
                        serFileName = os.path.normpath(serFileName)
                        localFile = os.path.normpath(localFile)
                        if os.path.isfile(localFile):
                            if localFile != serFileFinalName:
                                #设置拷贝标帜
                                tmpCopyFlag = True
                                if os.path.isdir(serFileName):
                                    if os.path.isfile(serFileFinalName):
                                        testMtime = os.path.getmtime(localFile)
                                        tmpMtime = os.path.getmtime(serFileFinalName)
                                        if int(tmpMtime) >= int(testMtime):
                                            tmpCopyFlag = False
                                if tmpCopyFlag:
                                    copyData.update({localFile: serFileName})
                                if typeModel == 'imap_mode':
                                    typeName = u'Irradiance map光子贴图'
                                elif typeModel == 'imap_mode':
                                    typeName = u'Light cache map光子贴图'
                                else:
                                    typeName = u'Caustics的焦散贴图'
                                if copyData:
                                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的Vray的 %s!" % typeName)
                                    if not self.CopyDataJob(copyData, True):
                                        return False
                                mc.setAttr('vraySettings.%s' % typeFuleAttr, serFileFinalName, type='string')
        except:
            pass
        return True

    def myCopy_Mr(self):
        #拷贝mentalrayIblShape节点的贴图
        mrIbType = 'mentalrayIblShape'
        mrIbAttr = 'texture'
        if not self.myCopy_Proxy_OImagesModel(mrIbType, mrIbAttr):
            return False
        #拷贝mentalrayTexture节点的贴图
        mrTxType = 'mentalrayTexture'
        mrTxAttr = 'fileTextureName'
        if not self.myCopy_Proxy_OImagesModel(mrTxType, mrTxAttr):
            return False
        return True

    def myCopy_Vr(self):
        #拷贝Vray的代理
        VrType = 'VRayMesh'
        VrAttr = 'fileName'
        if not self.myCopy_Proxy_OImagesModel(VrType, VrAttr):
            return False
        #检查Vray的VRayLightIESShape灯光贴图
        VrIesLType = 'VRayLightIESShape'
        VrIesLAttr = 'iesFile'
        if not self.myCopy_Proxy_OImagesModel(VrIesLType, VrIesLAttr):
            return False
        #Irradiance map光子贴图
        IrrMap_typeOn = 'giOn'
        IrrMap_typeModel = 'imap_mode'
        IrrMap_typeFuleAttr = 'imap_fileName'
        IrrMap_numModel = 2
        if not self.myCopy_VrSetFilesModel(IrrMap_typeOn, IrrMap_typeModel, IrrMap_typeFuleAttr, IrrMap_numModel):
            return False
        #Light cache map光子贴图
        LightC_typeOn = 'giOn'
        LightC_typeModel = 'mode'
        LightC_typeFuleAttr = 'fileName'
        LightC_numModel = 2
        if not self.myCopy_VrSetFilesModel(LightC_typeOn, LightC_typeModel, LightC_typeFuleAttr, LightC_numModel):
            return False
        #Caustics的焦散贴图
        Caustics_typeOn = 'causticsOn'
        Caustics_typeModel = 'causticsMode'
        Caustics_typeFuleAttr = 'causticsFile'
        Caustics_numModel = 1
        if not self.myCopy_VrSetFilesModel(Caustics_typeOn, Caustics_typeModel, Caustics_typeFuleAttr, Caustics_numModel):
            return False
        return True

    def myCopy_Ar(self):
        #拷贝Arnold代理与代理贴图
        if not self.myCopy_Ar_Proxy():
            return False
        # ArType = 'aiStandIn'
        # ArAttr = 'dso'
        # if not self.myCopy_Proxy_OImagesModel(ArType, ArAttr):
        #     return False
        #拷贝Arnold的aiPhotometricLight灯光贴图
        ###################
        #改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
        ####################
        ArIesLType = 'aiPhotometricLight'
        ArIesLAttr = 'aiFilename'
        if not self.myCopy_Proxy_OImagesModel(ArIesLType, ArIesLAttr):
            return False
        return True

    #拷贝mrIb贴图、mrTex节点的贴图路径、摄像机投影贴图、检查Vray的VRayLightIESShape灯光贴图
    def myCopy_OtherImages(self):
        #检查摄像机投影贴图
        camImType = 'imagePlane'
        camImAttr = 'imageName'
        if not self.myCopy_Proxy_OImagesModel(camImType, camImAttr):
            return False
        return True

    #拷贝Realflow缓存的模块
    def myCopy_rfCacheModel(self, myType, mtAttr):
        tmpCopyFlag = True
        try:
            allRfNodes = mc.ls(type=myType)
        except:
            pass
        else:
            copyData = {}
            setData = {}
            type_file = 'cache'
            type_data = 'realflowCache'
            serFileName = os.path.join(self.serveProject, type_file, type_data)
            if allRfNodes:
                for RfNode in allRfNodes:
                    myFileFullpath = mc.getAttr('%s.%s' % (RfNode, mtAttr))
                    if myFileFullpath:
                        myFileFullpath = self.myChangeNetPath(myFileFullpath)
                        if myType == 'RealflowEmitter':
                            rfbaseName = 'particles'
                            myFilepath = myFileFullpath
                            myFilePreName = mc.getAttr('%s.Prefixes[0]' % RfNode)
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = myFinalName
                        else:
                            rfbaseName = 'meshes'
                            myFilepath = os.path.dirname(myFileFullpath)
                            myFileBasePath = os.path.basename(myFileFullpath)
                            FramePadding = mc.getAttr('%s.framePadding' % RfNode)
                            myFileBasePathText = os.path.splitext(myFileBasePath)[0]
                            myFilePreName = myFileBasePathText[:-FramePadding]
                            myFinalName = os.path.join(serFileName, rfbaseName)
                            myFinalSName = os.path.join(myFinalName, myFileBasePath)
                        #获取文件名
                        myFinalName = os.path.normpath(myFinalName)
                        myFinalSName = os.path.normpath(myFinalSName)
                        myFilepath = os.path.normpath(myFilepath)
                        #网络盘存在标帜
                        tmpSerPathFlag = os.path.isdir(myFinalName)
                        if os.path.isdir(myFilepath):
                            if myFilepath != myFinalName:
                                #整体文件夹拷贝
                                copyData.update({myFilepath: myFinalName})
                                setData.update({RfNode: myFinalSName})
                if copyData:
                    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 %s 文件!" % myType)
                    #拷贝文件
                    if not self.CopyDataJob(copyData, True):
                        return False
                for key in setData.keys():
                    mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
        return True

    #拷贝Realflow的particles粒子和Meshs缓存
    def myCopy_rfCache(self):
        #拷贝particles缓存
        rfParType = 'RealflowEmitter'
        rfParAttr = 'Paths[0]'
        if not self.myCopy_rfCacheModel(rfParType, rfParAttr):
            return False
        #拷贝meshs缓存
        rfMeshType = 'RealflowMesh'
        rfMeshAttr = 'Path'
        if not self.myCopy_rfCacheModel(rfMeshType, rfMeshAttr):
            return False
        return True

    #保存文件
    def mySaveFile(self):
        #try:
        #    mc.deleteUI("hyperShadePanel1Window")
        #except:
        #    pass
        # mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
        # myactivePlane = ''
        # i = 1
        # while(i):
        #     try:
        #         tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
        #     except:
        #         pass
        #     else:
        #         if tmp:
        #             myactivePlane = 'modelPanel%d' % i
        #             break
        #     i += 1
        # if myactivePlane:
        #     mc.modelEditor(myactivePlane, e=True, da='boundingBox')
        driveFlag = False
        myDrives = ['D:', 'E:', 'C:']
        type_file = 'scenes'
        myFileFullpath = mc.file(q=True, sn=True)
        fileSize = os.path.getsize(myFileFullpath)
        for drive in myDrives:
            freeSV = mm.eval('strip(system("wmic LogicalDisk where Caption=\'%s\' get FreeSpace /value"))' % drive)
            freeMV = re.sub("\D", "", freeSV)
            if freeMV:
                freeLV = long(freeMV)
                if freeLV > fileSize:
                    driveFlag = True
                    break
        if driveFlag:
            localTempPath = r'%s\octvTemp' % drive
            if not os.path.isdir(localTempPath):
                os.mkdir(localTempPath)
            locaoFileName = os.path.join(localTempPath, self.fileSName)
            myTyprName = 'mayaBinary'
            if self.fileSName.lower().find('mb') >= 0:
                myTyprName = 'mayaBinary'
            else:
                myTyprName = 'mayaAscii'
            serFileName = os.path.join(self.serveProject, type_file)
            fileserName = os.path.join(serFileName, self.fileSName)
            #判断是否有用Vray渲染器和是否是渲染动画帧
            VrayFlag = False
            VrayAnimationFlag = False
            ChangeFlag = False
            if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
                if mc.objExists('vraySettings'):
                    VrayFlag = True
                    VrayAnimationFlag = mc.getAttr("defaultRenderGlobals.animation")
            if VrayFlag and VrayAnimationFlag:
                try:
                    mc.setAttr("defaultRenderGlobals.animation", False)
                except:
                    pass
                else:
                    ChangeFlag = True
                    time.sleep(1)
            if not self.worker1.myLocalFlag or self.copyType == 5:
                mc.file(rename=locaoFileName)
                mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
                time.sleep(1)
                copyData = {locaoFileName: serFileName}
                self.CopyDataJob(copyData, True)
                # myProjectAddress = self.serveProject.replace('\\', '/')
                # mm.eval('setProject "%s"' % myProjectAddress)
                if self.copyType != 5:
                    os.remove(locaoFileName)
            else:
                print fileserName
                mc.file(rename=fileserName)
                mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
                time.sleep(1)
            if self.copyType == 1 or self.copyType == 5:
                myProjectAddress = self.serveProject.replace('\\', '/')
                mm.eval('setProject "%s"' % myProjectAddress)
            if ChangeFlag:
                try:
                    mc.setAttr("defaultRenderGlobals.animation", True)
                except:
                    pass
            return fileserName
        else:
            mc.confirmDialog(title=u'温馨提示：', message=u'本地盘符不够空间来临时存储文件！\n请清理空间', button=['OK'], defaultButton='Yes', dismissString='No')
            return False

    def delDefaultRenderLayer(self):
        layers = mc.ls(exactType='renderLayer')
        count = 0
        pattern = re.compile('^[a-zA-Z0-9_\:-]*defaultRenderLayer$')
        for eachLayer in layers:
            if pattern.match(eachLayer):
                if not eachLayer == 'defaultRenderLayer':
                    try:
                        mc.delete(eachLayer)
                    except:
                        om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                    else:
                        count += 1
        del pattern

        resolutions = mc.ls(exactType='resolution')
        count = 0
        patternS = re.compile('^[a-zA-Z0-9_\:-]*defaultResolution$')
        for each in resolutions:
            if patternS.match(each):
                if not each == 'defaultResolution':
                    try:
                        mc.delete(each)
                    except:
                        om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
                    else:
                        count += 1
        del patternS

        allmylayers = mc.listConnections("renderLayerManager.renderLayerId")
        for layer in layers:
            if not layer in allmylayers:
                try:
                    mc.delete(layer)
                except:
                    pass
                else:
                    count += 1
        om.MGlobal.displayInfo(u'一共清除了%d 个defaultRenderLayer' % count)

    def writeInfo(self):
        # 输出job_info文件：
        #       Plugin
        #       Name
        #       Frames
        #       OutputDirectory0
        #       如果界面的Frames里为空的话，这里的Frames会读取渲染设置
        # 输出plugin_info文件：
        #       SceneFile
        #       Renderer
        #       UsingRenderLayers
        #       RenderLayer
        #       ImageWidth
        #       ImageHeight
        #       AspectRatio
        #       ProjectPath
        #       OutputFilePath
        #       OutputFilePrefix
        #       如果没有渲染层的话，Renderer设为File， UsingRenderLayers/RenderLayer/ImageWidth/ImageHeight/AspectRatio可以不写
        layers = mc.ls(exactType='renderLayer')
        pattern = re.compile('^defaultRenderLayer')
        for eachLayer in layers:
            if pattern.match(eachLayer):
                if not eachLayer == 'defaultRenderLayer':
                    try:
                        mc.select(eachLayer, r=True)
                        mc.lockNode(l=False)
                        mc.delete(eachLayer)
                    except:
                        self.stateMsg += u'注意,%s节点无法删除.\n'
                        om.MGlobal.displayWarning(u'注意,%s节点无法删除.\n')
        del pattern

        imgFormat = {23:'avi', 11:'cin', 35:'dds', 9:'eps', 0:'gif', 8:'jpg', 7:'iff', 10:'iff', 31:'psd', 36:'psd', 32:'png', 12:'yuv', 2:'rla', 5:'sgi', 13:'sgi', 1:'pic', 19:'tga', 3:'tif', 4:'tif', 20:'bmp', \
                     2:'rla', 5:'rgb', 51:'tif', 6:'als'}
        getTempFolderScriptFile = r'\\192.168.5.38\td\APP\RenderFarm\getDeadlineTemp.py'
        p = os.popen(r'deadlinecommand -executescript %s' % getTempFolderScriptFile, 'r')
        tempFolder = p.read()
        p.close()
        del p
        tempFolder = tempFolder[:-1]
        key = ['Version', 'Build', 'Name', 'StartFrames', 'EndFrames', 'FrameStep', 'OutputDirectories0', 'SceneFile', 'Renderer', 'RenderLayer', 'ImageWidth',
               'ImageHeight', 'AspectRatio', 'ProjectPath', 'OutputFilePath', 'OutputFilePrefix', 'RenderableLayers']

        renderGlobal = mc.ls(et='renderGlobals')
        resolution = mc.ls(et='resolution')
        if len(renderGlobal) > 1:
            self.stateMsg += u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n'
            om.MGlobal.displayError(u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n')
            return

        if not len(resolution) == 1 and len(resolution) > 0:
            self.stateMsg += u'有多于一个Resolution节点,请检查场景删除多余的节点.\n'
            om.MGlobal.displayError(u'有多于一个Resolution节点,请检查场景删除多余的节点.\n')
            return

        #filePrefixName = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
        fileNameWithExt = mc.file(q=True, sn=True, shn=True)
        fileName = [os.path.splitext(fileNameWithExt)[0]]
        hostFile = ['%s\\scenes\\%s' % (self.serveProject, fileNameWithExt)]
        outputDir = [self.serveImages]
        projPath = [self.serveProject]
        version = [mc.about(version=True)]
        build = ['32bit']
        allCam = mc.ls(et='camera')

        if mc.about(is64=True):
            build[0] = '64bit'

        allLayer = []
        renderable = []

        currentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
        if len(layers):
            for eachLayer in layers:
                if 'defaultRenderLayer' == eachLayer:
                    mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)
                    #continue
                allLayer.append(eachLayer)

        renCam = []
        renderer = []
        filePrefix = []
        # resolveName = []
        format = []
        startFrame = []
        endFrame = []
        frameStep = []
        width = []
        height = []
        ratio = []

        if len(allLayer):
            for eachLayer in allLayer:
                mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)

                if mc.getAttr('%s.renderable' % eachLayer):
                    renderable.append(eachLayer)

                for eachCam in allCam:
                    if mc.getAttr('%s.renderable' % eachCam):
                        renCam.append(eachCam)

                if not len(renCam):
                    #om.MGlobal.displayError(u'%s渲染层没有渲染摄像机,终止操作.' % eachLayer)
                    pass
                currentRenderName = mc.getAttr('%s.currentRenderer' % renderGlobal[0])
                renderer.append(currentRenderName.capitalize())
                if currentRenderName.find('vray') >= 0:
                    prefix = mc.getAttr('vraySettings.fileNamePrefix')
                    frameStep.append(int(mc.getAttr('vraySettings.fileNamePadding')))
                else:
                    prefix = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
                    frameStep.append(int(mc.getAttr('defaultRenderGlobals.byFrameStep')))
                filePrefix.append(prefix)
                # prefix = prefix.replace(u'<Scene>', fileName[0])
                # prefix = prefix.replace(u'<RenderLayer>', eachLayer)
                # prefix = prefix.replace(u'<Camera>', renCam[0])
                # resolveName.append(prefix)

                formatIndex = mc.getAttr('%s.imageFormat' % renderGlobal[0])
                format.append(imgFormat[formatIndex])
                startFrame.append(int(mc.getAttr('%s.startFrame' % renderGlobal[0])))
                endFrame.append(int(mc.getAttr('%s.endFrame' % renderGlobal[0])))
                width.append(mc.getAttr('%s.width' % resolution[0]))
                height.append(mc.getAttr('%s.height' % resolution[0]))
                ratio.append(mc.getAttr('%s.deviceAspectRatio' % resolution[0]))

        all = []
        all.append(version)
        all.append(build)
        all.append(fileName)
        all.append(startFrame)
        all.append(endFrame)
        all.append(frameStep)
        all.append(outputDir)
        all.append(hostFile)
        all.append(renderer)
        all.append(allLayer)
        all.append(width)
        all.append(height)
        all.append(ratio)
        all.append(projPath)
        all.append(outputDir)
        all.append(filePrefix)
        all.append(renderable)

        mc.editRenderLayerGlobals(currentRenderLayer=currentLayer)

        writeStr = ''
        for i in range(len(key)):
            writeStr += '[%s]\n' % key[i]
            for eachItem in all[i]:
                writeStr += '%s\n' % eachItem
            writeStr += '[/%s]\n\n' % key[i]

        fPath = os.path.join(tempFolder, 'fileSettings.cfg')
        f = file(fPath, 'w')
        try:
            f.writelines(writeStr)
        except:
            self.stateMsg += u'%s写入信息时出错,终止操作.\n' % fPath
            om.MGlobal.displayError(u'%s写入信息时出错,终止操作.\n' % fPath)
        else:
            f.close()
            self.stateMsg += u'成功写入信息文件.\n'
            om.MGlobal.displayInfo(u'成功写入信息文件.\n')
        del all[:]
        del fileName[:]
        del startFrame[:]
        del endFrame[:]
        del outputDir[:]
        del hostFile[:]
        del renderer[:]
        del allLayer[:]
        del width[:]
        del height[:]
        del ratio[:]
        del projPath[:]
        del filePrefix[:]
        del renderable[:]
        del writeStr

    def executeScript(self):
        try:
            str = os.popen(r'"deadlinecommand.exe" -ExecuteScript \\octvision.com\cg\td\APP\RenderFarm\MayaSubmission.py').read()
        except:
            pass
        else:
            sys.stdout.write(str)

    def changeMrLayer(self):
        if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
            if not mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
                allLayers = mc.listConnections('renderLayerManager.renderLayerId')
                if allLayers:
                    for Layer in allLayers:
                        if mc.getAttr('%s.renderable' % Layer):
                            mc.editRenderLayerGlobals(currentRenderLayer=Layer)
                            if mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
                                break

    def Cancelsimulation(self):
        #关闭布料和毛发动力解算
        try:
            AllNucleus= mc.ls(type='nucleus')
        except:
            pass
        else:
            if AllNucleus:
                for eachNucleu in AllNucleus:
                    try:
                        mc.setAttr('%s.enable' % eachNucleu, 0)
                    except:
                        pass
        #Yeti毛发缓存
        try:
            AllYetiCahces= mc.ls(type='pgYetiGroom')
        except:
            pass
        else:
            if AllYetiCahces:
                for eachYetiCahce in AllYetiCahces:
                    try:
                        mc.setAttr('%s.doSimulation' % eachYetiCahce, 0)
                    except:
                        pass

    def main(self, *args):
        copyType = args[0]
        self.ArnoldFlag = False
        if len(args) > 1:
            if args[1]:
                self.myUseRender = args[1]
                if len(self.myUseRender[2]) > 0:
                    self.ArnoldFlag = True
        '''
        copyType分三种模式
        1 单纯拷贝模式
        2 拷贝提交模式
        3 单纯提交模式
        '''
        self.copyType = copyType

        # print ("line 2655 ============{}".format(self.copyType))
        #创建素材输入文件夹
        if copyType == 2 or copyType == 3:
            self.serveImages = self.myCreateImagesFolder()
        #设置deep层输出的路径
        elif copyType == 4:
            self.serveImages = self.myCreateDeepImagesFolder()

        #当模式为1和2时工程目录，3时为读取当前工程目录
        if copyType == 1 or copyType == 2 or copyType == 4 or copyType == 5:
            self.serveProject = self.myCreateScenes()
        elif copyType == 3:
            self.serveProject = mc.workspace(q=True, rd=True)
            myFileFullName = mc.file(q=True, sn=True)
        if self.serveProject.find('z:') >= 0:
            self.serveProject = self.serveProject.replace('z:', OCT_DRIVE)
        elif self.serveProject.find('Z:') >= 0:
            self.serveProject = self.serveProject.replace('Z:', OCT_DRIVE)

        #检查当前工程是否有读写权限
        checkAccessFile = os.path.join(self.serveProject, 'myTest_TD')
        try:
            os.makedirs(checkAccessFile)
        except:
            pass
        try:
            os.removedirs(checkAccessFile)
        except:
            self.worker1.myLocalFlag = False
            self.worker2.myLocalFlag = False
        else:
            self.worker1.myLocalFlag = True
            self.worker2.myLocalFlag = True

        #去掉检查参考
        # if copyType == 2 or copyType == 3 or copyType == 4:
        #     if mc.file(q=True, reference=True):
        #         om.MGlobal.displayInfo(u'文件含有参考，请导入后再继续！\n')
        #         mc.confirmDialog(title=u'温馨提示：', message=u'文件含有参考，请导入后再继续！', button=['OK'], defaultButton='Yes', dismissString='No')
        #         return False
        # raise Exception("test")
        if (copyType == 2 or copyType == 4) and self.ArnoldFlag:
            if mc.objExists("defaultArnoldRenderOptions"):
                mc.setAttr("defaultArnoldRenderOptions.use_existing_tiled_textures", 1)
                mc.setAttr("defaultArnoldRenderOptions.absoluteTexturePaths", 0)
                mc.setAttr("defaultArnoldRenderOptions.absoluteProceduralPaths", 1)
                mc.setAttr("defaultArnoldRenderOptions.textureMaxOpenFiles", 200)
                # mc.setAttr("defaultArnoldRenderOptions.absoluteProceduralPaths", 0)
                myArnoldLocalPath = mc.getAttr("defaultArnoldRenderOptions.texture_searchpath")
                # myArnoldProxyPath = mc.getAttr("defaultArnoldRenderOptions.procedural_searchpath")
                if myArnoldLocalPath:
                    if myArnoldLocalPath[-1] != ';':
                         mc.setAttr("defaultArnoldRenderOptions.texture_searchpath", myArnoldLocalPath+';'+self.serveProject+'\\sourceimages;', type="string")
                    else:
                        mc.setAttr("defaultArnoldRenderOptions.texture_searchpath", myArnoldLocalPath+self.serveProject+'\\sourceimages;', type="string")
                else:
                    mc.setAttr("defaultArnoldRenderOptions.texture_searchpath", self.serveProject+'\\sourceimages;', type="string")
                # if myArnoldProxyPath:
                #     if myArnoldProxyPath[-1] != ';':
                #          mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", myArnoldProxyPath+';'+self.serveProject+'sourceimages;', type="string")
                #     else:
                #         mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", myArnoldProxyPath+self.serveProject+'sourceimages;', type="string")
                # else:
                #     mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", self.serveProject+'sourceimages;', type="string")
        #运行主程序
        print self.serveProject
        if self.serveProject:
            # print("line2735 TD Check")
            # self.myCopy_Ar()
            # raise Exception("TD check 2736")

            mc.progressWindow(title=u'提交文件', status=u'即将开始', isInterruptable=True)
            if copyType == 1 or copyType == 2 or copyType == 4 or copyType == 5:
                i = 0
                j = 1
                k = 10
                mrFlag = False
                vrFlag = False
                arFlag = False
                if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
                    mrFlag = True
                    i += 1
                if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
                    vrFlag = True
                    i += 1
                if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
                    arFlag = True
                    i += 1
                k = k + i
                # print("line 2751 td check copy aistandin texture=========set start")
                #self.myCopy_Ar()
                # print("line 2753 td check copy aistandin texture=========end")
                # raise Exception("td check")
                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 file 贴图文件' % (k, j))
                if self.myCopyType_Files():
                    j += 1
                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 cacheFile 缓存文件' % (k, j))
                    if self.myCopy_Data():
                        j += 1
                        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Alembic cacheFile 缓存文件' % (k, j))
                        if self.myCopy_AbcData():
                            j += 1
                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Shave cacheFile 缓存文件' % (k, j))
                            if self.myCopy_Shavedata():
                                j += 1
                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 particle 缓存文件' % (k, j))
                                if self.myCopy_Particles():
                                    j += 1
                                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Realflow 缓存' % (k, j))
                                    if self.myCopy_rfCache():
                                        j += 1
                                        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Yeti毛发缓存' % (k, j))
                                        if self.myCopy_YetiCache():
                                            j += 1
                                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传摄像机投影贴图' % (k, j))
                                            if self.myCopy_OtherImages():
                                                if mrFlag:
                                                    j += 1
                                                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Mr渲染器的相关文件' % (k, j))
                                                    if not self.myCopy_Mr():
                                                        mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                        mc.progressWindow(endProgress=True)
                                                        return False
                                                if vrFlag:
                                                    j += 1
                                                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Vr渲染器的相关文件' % (k, j))
                                                    if not self.myCopy_Vr():
                                                        mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                        mc.progressWindow(endProgress=True)
                                                        return False
                                                if arFlag:
                                                    j += 1
                                                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Ar渲染器的相关文件' % (k, j))
                                                    if not self.myCopy_Ar():
                                                        mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！', button=[u'确认'], icn='critical', defaultButton='ok', dismissString='No')
                                                        mc.progressWindow(endProgress=True)
                                                        return False
                                                j += 1
                                                mc.progressWindow(edit=True, progress=1, min=0, max=1, status=u"正在保存文件!", title=u'共%s步, 第 %s 步,正在保存文件' % (k, j))
                                                self.delDefaultRenderLayer()
                                                self.Cancelsimulation()
                                                raise Exception("line 2813 td stop!!!")
                                                myFileFullName = self.mySaveFile()
                                                if myFileFullName:
                                                    mm.eval('autoUpdateAttrEd;')
                                                    om.MGlobal.displayWarning(u'\n文件上传成功！')
                                                    j += 1
                                                    mc.progressWindow(edit=True, status=u'上传完毕!', title=u'共%s步, 第 %s 步,上传完毕！' % (k, j))
            if copyType == 2 or copyType == 3 or copyType == 4:
                if copyType == 3:
                    self.delDefaultRenderLayer()
                self.changeMrLayer()
                myfileBaseName = os.path.splitext(self.fileSName)[0]
                mm.eval(r'global string $myFileName = "%s"' % myfileBaseName)
                mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineSceneFile = "%s"' % myFileFullName.replace('\\', '/'))
                mm.eval(r'global string $myDeadlineProjectPath= "%s"' % self.serveProject.replace('\\', '/'))
                mm.eval('source "SubmitMayaToDeadline_zwz";')
                mm.eval('SubmitMayaToDeadline_zwz')
                if mc.radioButtonGrp('AutoSubmit', q=True, sl=True) == 1:
                    mm.eval('evalDeferred "SetupSubmission()"')
                # self.writeInfo()
                # self.executeScript()
            mc.progressWindow(endProgress=True)
            return True

# i = AssetDeadline()
# if i.checkFile(2):
#     i.show()
