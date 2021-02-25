# -*- coding: utf-8 -*-
__author__ = 'zhaozhongjie'

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
        for file in self.play_list[1:]:
            movName=cmds.file(q=1,sn=1,shn=1).replace('.'+cmds.file(q=1,sn=1,shn=1).split('.')[-1],'')
            movPath='D:/TempInfo/playblast/yd/'
            cmds.sysFile(movPath, makeDir=True)
            cmds.optionVar(intValue=('playblastSaveToFile',1))
            cmds.optionVar(stringValue=("playblastFile",(movPath+movName)))
            print u'===============开始拍屏============='
            cam=self.GDC_CamInfo()
            mel.eval('autoUpdateAttrEd')
            mc.lookThru(cam)
            mc.loadModule(scan=1)
            modelPane=mc.getPanel( withFocus=1 )
            mc.setFocus(modelPane)
            mov=cmds.evalDeferred("mel.eval(\"performPlayblast 8001\")", lp=True)
            cmds.evalDeferred("cmds.file('%s', open=True, force=True)"%file, lp=True)
            print u'[%s]'%(movPath+movName)


    def playblast(self):
        # 1.先开第一个文件，执行playblast的函数。
        cmds.file(self.play_list[0], open=True, force=True)

        # 2.执行playblast的函数。
        self.pbfile()

        # 3.playblast最后那个文件。
        cmds.evalDeferred("mel.eval(\"performPlayblast 8001\")", lp=True)

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
                cam=ca[0]
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



def main():
    oldDialog = apiUI.MQtUtil.findWindow('batch_playblast_MainWindow')
    try:
        shiboken.wrapInstance(long(oldDialog), QWidget).close()
    except:
        pass
    PlutoGW = BatchPlayblast()
    PlutoGW.show()
