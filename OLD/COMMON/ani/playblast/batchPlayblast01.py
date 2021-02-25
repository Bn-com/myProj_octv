# -*- coding: utf-8 -*-
__author__ = 'zhaozhongjie'

PlutoGW = None

'''
批量playBlast
import sys
del COMMON
sys.path.append(r'D:\CloudKP\Solar\GDC_TD')

'''
from PySide.QtCore import *
from PySide.QtGui import *
import shiboken
import maya.OpenMayaUI as apiUI
import maya.cmds as cmds
import UI
reload(UI)

import maya.utils
from functools import partial
import time
import os
import maya.mel as mel
mel.eval("source \"performPlayblast.mel\"")

"""
作用：
    批量playblast。

原理：
1.  先开第一个文件。
2.  执行playblast的函数。playblast的函数，写个循环。在循环里，先playblast，再开后一个文件。
3.  循环完成，再playblast最后那个文件。
"""


#   使用shiboken来获得maya的主窗口
def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken.wrapInstance(long(ptr), QWidget)


def toQtObject(mayaName):  # 获得maya控件的名称
    ptr = apiUI.MQtUtil.findControl(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findLayout(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findMenuItem(mayaName)
    if ptr is not None:
        return shiboken.wrapInstance(long(ptr), QWidget)




class BatchPlayblast(QMainWindow, UI.Ui_batch_playblast_MainWindow):  # BatchPlayblast
    def __init__(self, parent=getMayaWindow()):
        super(BatchPlayblast, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.play_list = []

    @Slot()
    def on_QB_add_clicked(self):
        """添加文件"""
        myAllowType = ['ma', 'mb']
        allow_type = "*."+" *.".join(myAllowType)
        settings = QSettings("GDCs", "BatchPlayblast")
        folder = settings.value("LastOpenedFolder")
        if folder is None:
            folder = [[""]]
        if folder[0] == []:
            folder[0].append("")
        filename = QFileDialog.getOpenFileNames(self ,"Select File", folder[0][0], "Image Files ( %s)"%(allow_type))
        settings.setValue("LastOpenedFolder", filename)
        if len(filename[0]) > 0:
            # ======设置文件路径======
            for file in filename[0]:
                self.QL_list.addItem(file)

    @Slot()
    def on_QB_del_clicked(self):
        """删除文件"""
        selects = self.QL_list.selectedItems()
        for s in selects:
            qindex = self.QL_list.indexFromItem(s)
            self.QL_list.takeItem(qindex.row())


    @Slot()
    def on_QB_start_clicked(self):
        """开始playblast"""
        self.play_list = []
        for i in range(self.QL_list.count()):
            item = self.QL_list.item(i)
            self.play_list.append(item.text())

        self.playblast()

    def pbfile(self):
        """playblast"""
        movName=cmds.file(q=1,sn=1,shn=1).replace('.'+cmds.file(q=1,sn=1,shn=1).split('.')[-1],'')
        movPath='D:/TempInfo/playblast/yd/'
        cmds.sysFile(movPath, makeDir=True)
        if os.path.isfile(movPath+movName):
            try:
                cmds.sysFile((movPath+movName),delete=1)
            except:
                pass
        cmds.optionVar(intValue=('playblastSaveToFile',1))
        cmds.optionVar(stringValue=("playblastFile",(movPath+movName)))
        print u'===============开始拍屏============='
        cmds.setFocus('modelPanel4')
        cam=self.GDC_CamInfo()
        cmds.select(cam)
        mov=cmds.evalDeferred("mel.eval(\"performPlayblast 8001\")", lp=True)
        #cmds.evalDeferred("cmds.file('%s', open=True, force=True)"%file, lp=True)
        print u'[%s]'%(movPath+movName)


    def playblast(self, i = 0):
        #1 开文件
        if i > len(self.play_list) - 1:
            return
        cmds.file(self.play_list[i], open=True, force=True)

        # 2.设置拍屏前参数
        movName=cmds.file(q=1,sn=1,shn=1).replace('.'+cmds.file(q=1,sn=1,shn=1).split('.')[-1],'')
        shotInfo=self.checkShotInfo()
        movPath='D:/TempInfo/playblast/'+shotInfo[0]+'/'
        cmds.sysFile(movPath, makeDir=True)
        cmds.sysFile("%s%s.avi" % (movPath, movName), delete = True)
        cmds.optionVar(intValue=('playblastViewerOn', 0))
        cmds.optionVar(stringValue=("playblastFormat", "avi"))
        cmds.optionVar(stringValue=("playblastCompression", "PVMJPG40"))
        cmds.optionVar(intValue=('playblastSaveToFile',1))
        cmds.optionVar(stringValue=("playblastFile",(movPath+movName)))
        self.setupHardwareSettings(colorManaged=True, textures=True, lights=False)
        print u'===============开始拍屏============='
        cmds.setFocus('modelPanel4')
        mel.eval('autoUpdateAttrEd')
        mel.eval('updateShowMenu MayaWindow|formLayout1|viewPanes|modelPanel4|menu30 modelPanel4 "modelPanel4" "Playblast Display"')
        mel.eval('modelEditor -e -allObjects 0 modelPanel4')
        mel.eval('modelEditor -e -polymeshes true modelPanel4')
        cam = self.GDC_CamInfo()
        cmds.select(cam)
        cmds.lookThru(cam)
        cmds.loadModule(scan=1)
        cmds.select(cam)

        #3.拍屏
        command = "mel.eval(\"performPlayblast 8001; python \\\"bp.PlutoGW.playblast(%d)\\\";\")" % (i + 1)
        cmds.evalDeferred(command, lp=True)

    def GDC_CamInfo(self,shotType=3):
        shotInfo=self.checkShotInfo()
        cam=''
        proShort=['yd']
        if shotInfo[0] not in ['yd']:
            cmds.warning(u'=============本工具仅支持【%s】 项目，请检查文件命名================'%proShort)
            cmds.error(u'=============本工具仅支持【%s】 项目，请检查文件命名================'%proShort)
        if shotInfo[0] in ['yd'] and shotType==3:
            cam='cam_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]
        if shotInfo[0] in ['yd'] and shotType==2:
            cam='cam_'+shotInfo[1]+'_'+shotInfo[2]
        if cam:
            ca=cmds.ls(cam,l=1)
            if len(ca)>1:
                cmds.warning(u'=============文件中有不止一个【%s】相机，请检查，并修改文件================'%cam)
                cmds.error(u'=============文件中有不止一个【%s】相机，请检查，并修改文件================'%cam)
            else:
                cam=cmds.listRelatives(ca[0],s=1,f=1)[0]
        else:
            cmds.warning(u'=============文件中缺少【%s】相机，请检查================'%cam)
            cmds.error(u'=============文件中缺少【%s】相机，请检查================'%cam)
        return cam
    def checkShotInfo(self):
        temp = (cmds.file(query=1, exn=1)).split('/')
        info = []
        if '_' in temp[len(temp) - 1]:
            info = temp[len(temp) - 1].split('_')
        else:
            #cmds.warning(unicode('========================【！！！文件名不规范！！！】========================', 'utf8'))
            cmds.warning(u'========================【！！！文件名不规范！！！】========================')
        return info

    def setupHardwareSettings(self,colorManaged=True, textures=True, lights=False):

        # Turn off the parallel evaluation which is just to unstable
        cmds.evaluationManager(mode="off")

        # Get rid of the stupid faceplate setting on Rowan
        facePlates = cmds.ls('faceplate_Shape', r=True, long=True)
        for plate in facePlates:
            cmds.setAttr(plate+'.holdOut', 0)

        # remove hardware shader links (leftover shaders from AnimaPoint assets. They show up black. This makes them gray and better to see)
        fxShaders = cmds.ls(type="ShaderfxShader", long=True)
        if fxShaders:
            for fxShader in cmds.ls(type="ShaderfxShader", long=True):
                connections = cmds.listConnections(fxShader, source=False, connections=True, plugs=True)
                for index in range(0, len(connections), 2):
                    if connections[index+1].find('.hardwareShader') != -1 or connections[index+1].find('.hardwareShaderLink') != -1:
                        cmds.disconnectAttr(connections[index], connections[index+1])

        if colorManaged:
            # Enable color managment
            cmds.colorManagementPrefs(edit=True, cmEnabled=True)

            # Tell the render output to be doing srgb gamma
            cmds.colorManagementPrefs(edit=True, outputTarget='renderer', outputTransformEnabled=True)
            cmds.colorManagementPrefs(edit=True, outputTarget='renderer', outputTransformName='sRGB gamma')

        # Ok trying to set the default render first
        cmds.setAttr('defaultRenderGlobals.currentRenderer', 'mayaHardware2', type='string')

        import maya.mel as mel
        # mel.eval("createObjectTypeFilters(2)");
        mel.eval("objectTypeFilterNoneCallback()") # Hide Everything
        mel.eval("objectTypeFilterOnCallback(2)")  # Show Polygons
        mel.eval("objectTypeFilterOnCallback(3)")  # Show SubDiv
        mel.eval("objectTypeFilterOnCallback(4)")  # Show Particles
        mel.eval("objectTypeFilterOnCallback(5)")  # Show Particles Instancers
        mel.eval("objectTypeFilterOnCallback(6)")  # Show Fluids

        if textures:
            cmds.setAttr("hardwareRenderingGlobals.renderMode", 4)  # 1:shaded, 4:shaded+texture
        else:
            cmds.setAttr("hardwareRenderingGlobals.renderMode", 1)  # 1:shaded, 4:shaded+texture

        if lights:
            cmds.setAttr("hardwareRenderingGlobals.lightingMode", 1)  # 0:Default, 1:all
        else:
            cmds.setAttr("hardwareRenderingGlobals.lightingMode", 0)  # 0:Default, 1:all
        cmds.setAttr("hardwareRenderingGlobals.renderDepthOfField", 0)

        # Set the output image format
        cmds.setAttr("defaultRenderGlobals.imageFormat", 32)  # 32: png

        # Set the standard 4 padding settings
        cmds.setAttr('defaultRenderGlobals.animation', True)
        cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
        cmds.setAttr('defaultRenderGlobals.periodInExt', 1)
        cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', True)
        cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)

        # Disable old style gammaCorrectionEnable
        cmds.setAttr("hardwareRenderingGlobals.gammaCorrectionEnable", 0)

        # Make it consolidate world, seems to give more stable results
        cmds.setAttr("hardwareRenderingGlobals.consolidateWorld", 1)

        cmds.setAttr("hardwareRenderingGlobals.lineAAEnable", 0)  # Smooth wireframe

        # Enable multisampling
        cmds.setAttr("hardwareRenderingGlobals.multiSampleEnable", 1)
        cmds.setAttr("hardwareRenderingGlobals.multiSampleCount", 16)

        # Enable Ambient Occlusion
        cmds.setAttr("hardwareRenderingGlobals.ssaoEnable", 1)
        cmds.setAttr("hardwareRenderingGlobals.ssaoAmount", 1.00)
        cmds.setAttr("hardwareRenderingGlobals.ssaoRadius", 16)
        cmds.setAttr("hardwareRenderingGlobals.ssaoFilterRadius", 16)
        cmds.setAttr("hardwareRenderingGlobals.ssaoSamples", 16)

        # Have it clamp the texture resolutions
        cmds.setAttr("hardwareRenderingGlobals.enableTextureMaxRes", 1)
        cmds.setAttr("hardwareRenderingGlobals.textureMaxResolution", 1024)
        cmds.setAttr("hardwareRenderingGlobals.transparencyAlgorithm", 1)  # 0:simple, 1:object, 2:weightedAverage, 3:depthPeeling

        # Set some defaults
        cmds.setAttr("hardwareRenderingGlobals.maxHardwareLights", 8)
        cmds.setAttr("hardwareRenderingGlobals.floatingPointRTEnable", 0)


def main():
    oldDialog = apiUI.MQtUtil.findWindow('batch_playblast_MainWindow')
    try:
        shiboken.wrapInstance(long(oldDialog), QWidget).close()
    except:
        pass
    global PlutoGW
    PlutoGW = BatchPlayblast()

    PlutoGW.show()
