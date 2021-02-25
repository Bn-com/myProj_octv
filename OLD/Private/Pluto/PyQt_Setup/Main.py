# -*- coding: utf-8 -*-
"""
Created on 2015-7-14
@version: 2014
@author: zhaozhongjie
usage:
import sys
sys.path.insert(0,r'D:\CloudKP\Solar\GDC_TD\Private\Pluto\PyQt_Setup')
import Main as m;reload(m);m.MainUI().show()
"""
import sip
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import pymel.all as pm
import maya.OpenMayaUI as apiUI
import maya.OpenMaya as OM
import maya.cmds as cmds
import Main_UI as MUI;reload(MUI)  # 界面.ui转py的文件

def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QObject)

def toQtObject(mayaName):  # 获得maya控件的名称
    ptr = apiUI.MQtUtil.findControl(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findLayout(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findMenuItem(mayaName)
    if ptr is not None:
        return sip.wrapinstance(long(ptr), QObject)


class MainUI(MUI.DesignerUI):
    def __init__(self, parent=getMayaWindow()):
        super(MainUI, self).__init__(parent)
        self.camera = pm.PyNode('persp')
        self.auto_camera = True
        self.qt_cam = ''
        self.my_connect()


        fc = pm.ls("*:FM_FACIAL_CAM")
        if len(fc):
            self.camera = fc[0]
        self.create_cam_win(self.camera)

    def my_connect(self):
        """ 我的控件的链接"""
        self.ui.QPushButton_CMD.clicked.connect(self.my_button_CMD)
        self.ui.QCheckBox_autocam.toggled.connect(self.my_toggle_CMD)

    def show(self):
        """ 重写show函数，让每次显示的时候，创建一个 SelectionChanged 的 Maya API 反馈 """
        super(MainUI, self).show()
        #   用Maya API设置一个选择改变的事件
        self.maya_selection_call_back = OM.MEventMessage.addEventCallback("SelectionChanged", self.callback_cmd )

    def closeEvent(self, *args, **kwargs):
        """关闭窗口的时候，自动删除callback事件"""
        print 'delete ---', self.maya_selection_call_back
        try:
            OM.MEventMessage.removeCallback(self.maya_selection_call_back)
        except:
            pass

    def callback_cmd(self,data):
        """ 如果选择发生变化后，要执行的函数 """
        print "---------  Something Selected !!!!!  ---------"
        # 选择物体数量 不等于 1 则退出：
        if len(pm.selected()) != 1:
            return

        # 显示选择物体的 TX TY TZ:
        select_obj = pm.selected()[0]
        if select_obj.hasAttr('tx'):
            self.ui.QDoubleSpinBox_tx.setValue(select_obj.tx.get())
        if select_obj.hasAttr('ty'):
            self.ui.QDoubleSpinBox_ty.setValue(select_obj.ty.get())
        if select_obj.hasAttr('tz'):
            self.ui.QDoubleSpinBox_tz.setValue(select_obj.tz.get())

        # 自动切换摄像机：
        if self.auto_camera:
            facial = pm.selected()[0].name()
            if facial.endswith('Facial_CTRL_FRAME'):
                camera = facial.split(':')
                camera[-1] = 'FM_FACIAL_CAM'
                camera = ':'.join(camera)

                # 判断: 当前选择控制器对应摄像机是否为当前摄像机
                if camera != self.camera.name():
                    self.create_cam_win(pm.PyNode(camera))

    def create_cam_win(self, camera):
        """ 创建摄像机工作视图到工具中 """
        if self.qt_cam != '':
            self.qt_cam.deleteLater()     # 删除旧的qt的camera
        model_editor = pm.modelEditor()
        self.camera = camera
        pm.modelEditor(model_editor, e=True,
                       camera=camera,
                       allObjects=0, grid=0, polymeshes=1, nurbsCurves=0, activeView=1,
                       displayAppearance='smoothShaded', displayTextures=0
                       )
        self.qt_cam = toQtObject(model_editor)
        self.ui.Layout_left.insertWidget(1, self.qt_cam)

    def my_button_CMD(self):
        print '111111111111111111111111111111111111'

    def my_toggle_CMD(self):
        self.auto_camera = self.ui.QCheckBox_autocam.isChecked()

if __name__ == '__main__':
    window = MainUI()
    window.show()