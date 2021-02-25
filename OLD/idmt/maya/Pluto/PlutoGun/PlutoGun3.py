# -*- coding: utf-8 -*-
# Copyright (C) 2000-2013 IDMT. All rights reserved.
'''
Pluto Gun:
1)shoot the laser for YODA's craft
2)control the speed and vis for the lasers of the craft
'''
__author__ = 'zhaozhongjie'
__date__ = '2013-11-12'


from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUi
import sip
import maya.OpenMayaUI as apiUI
import maya.cmds as cmds
import maya.mel as mel

import os
import sys
import time


import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PlutoGun_Ships2 as ships
reload(ships)
NAME, VIS,  SPEED, LENGTH = range(4)

#   使用sip来获得maya的主窗口


def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


def toQtObject(mayaName):  # 获得maya控件的名称
    '''
    Given the name of a Maya UI element of any type,
    return the corresponding QWidget or QAction.
    If the object does not exist, returns None
    '''
    ptr = apiUI.MQtUtil.findControl(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findLayout(mayaName)
    if ptr is None:
        ptr = apiUI.MQtUtil.findMenuItem(mayaName)
    if ptr is not None:
        return sip.wrapinstance(long(ptr), QtCore.QObject)


class PlutoGunShip(object):

    def __init__(self, name, vis, speed, length):
        self.name = QString(name)
        self.vis = QString(vis)
        self.speed = speed
        self.length = length


class PlutoGunTable(QTableView):  # 自定义的tableView

    def __init__(self, PGW):
        super(PlutoGunTable, self).__init__()
        self.msw = PGW

#   鼠标释放后的事件-----选择物体
    def mouseReleaseEvent(self, QMouseEvent):
        QTableView.mouseReleaseEvent(self, QMouseEvent)
        Z_selectOBJ(self.msw, self)


class PlutoGunWindow(QtGui.QMainWindow):  # PlutoGunWindow窗口

    def __init__(self, parent=getMayaWindow()):
        super(PlutoGunWindow, self).__init__(parent)
        self.setWindowTitle("PlutoGun")
        self.setObjectName("PlutoGun")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(850, 600)

        self.setStyleSheet("QMainWindow{background: url(:/myuis/StarWar.jpg)}")

#    获得当前文件所在目录，为了找到.ui文件
        path_split = __file__.split('\\')
        path = '\\'.join(path_split[:-1])
        win = os.path.join(path, 'PlutoGunWin.myuis')

#    将loadUi的窗体作为子窗体
        self.win = loadUi(win, QtGui.QMainWindow())
#        return
        self.win.tableWidget.deleteLater()

#   时间发射器
        self.timer = QtCore.QTimer()
#    创建摄像机视图
        self.Cams = []
        self.Cam = ''
        self.Namespace = ''
        self.InitSpeed = 5
        self.moEditor = ''

        self.tableView = PlutoGunTable(self)

        self.model = ships.ShipTableModel()
        self.model.tableView = self.tableView

        self.tableView.setModel(self.model)
        self.tableView.setItemDelegate(ships.ShipDelegate(self))
        self.win.verticalLayout_2.insertWidget(0, self.tableView)
#         self.tableView.horizontalHeader().setStretchLastSection(1)
        self.tableView.horizontalHeader().setResizeMode(0, 1)
        self.tableView.horizontalHeader().resizeSection(1, 30)
        self.tableView.horizontalHeader().resizeSection(2, 50)
        self.tableView.horizontalHeader().resizeSection(3, 50)

        self.splitter = QtGui.QSplitter()
        self.splitter.setStyleSheet("background-color:transparent;")

        self.splitter.addWidget(self.win.widget_left)
        self.splitter.addWidget(self.win.widget_right)
        self.splitter.setOrientation(0x1)
        self.setCentralWidget(self.splitter)

        cam_Window = self.Z_create_camWin("first_time")
        if cam_Window != 'noCamera_In_File':
            self.win.tmp_label.deleteLater()
            qtObj = toQtObject(cam_Window)
            self.win.Left_Layout.addWidget(qtObj)

#   飞机选择菜单初始化
            self.Z_initComboBox()
            self.Z_InitialLoad()
            self.Z_LCD_Color(5)

#    comboBox 选项改变后， 刷新飞船
        self.win.comboBox.currentIndexChanged.connect(
            self.PlutoGun_RefreshAircraft)
#    数据改变后的操作
        self.model.dataChanged.connect(self.Z_SomeDataChanged)
#    高低模切换
        self.win.Low_High.clicked.connect(self.Z_Low_High)
#    刷新表格
        self.win.Refresh.clicked.connect(self.Z_InitialLoad)
#    刷新初始速度
        self.win.horizontalSlider.valueChanged.connect(self.Z_LCD_Color)
        self.win.horizontalSlider.valueChanged.connect(self.PlutoGun_Setspeed)
#    horizontalHeaderView选择整列后，自动选择物体
        self.tableView.horizontalHeader().sectionClicked.connect(
            self.Z_HeaderViewSelected)

#    发射激光
        self.connect(self.win.Shoot_Gun, SIGNAL(
            "clicked()"), self.PlutoGun_Shoots)

    #当改变comboBox的时候，此函数，用来刷新所有控件
    def PlutoGun_RefreshAircraft(self):
#    求comboBox中，选中的摄像机
        currentText = str(self.win.comboBox.currentText())

#    设置当前的视图中的摄像机
        cam_Window = self.Z_create_camWin(currentText)
        self.Cam = currentText
        self.Z_InitialLoad()

    def PlutoGun_Setspeed(self, speed):  # 设置滑条的变化改变函数
        self.InitSpeed = int(speed)

    #连发开枪的主函数
    def PlutoGun_Shoots(self):
        selected = cmds.ls(sl=1, type='transform')
        if len(selected) == 0:
            return
        for s in selected:
            cmds.select(cl=1)
            cmds.select(s)
            self.PlutoGun_Shoot()
        cmds.select(cl=1)
        cmds.select(selected)

    #开枪的主函数
    def PlutoGun_Shoot(self):
        selected = cmds.ls(sl=1, type='transform')
        if len(selected) == 0:
            return
        select_split = selected[0].split(':')
        select_namespace = ':'.join(select_split[:-1])
        select_contrl = select_split[-1]

        if select_namespace == self.Namespace:
            try:
                cmds.setAttr(selected[0] + '.plutoGun', 1)
            except:
                print u'该控制器上没有plutoGun属性，请联系前期添加'
                return
                pass
        else:
            return

        self.Z_InitialGroup()
        current_Lasers = self.Namespace + "_Lasers"

        Bullets = cmds.listRelatives(
            '____PlutoGun____|' + current_Lasers, c=1, pa=1)
        try:
            len(Bullets)
        except:
            Bullets = []
        if len(Bullets) < 50:
            cmds.select(selected)

            new_Bullet = self.PlutoGun_Shoot_cmd(2, 20)
            new_Bullet_parent = cmds.listRelatives(new_Bullet, p=1, f=1)

            try:
                if new_Bullet_parent[0] != ('|____PlutoGun____|' + current_Lasers):
                    cmds.parent(
                        new_Bullet, '____PlutoGun____|' + current_Lasers)
            except:
                cmds.parent(new_Bullet, '____PlutoGun____|' + current_Lasers)
                pass

        else:
            cmds.confirmDialog(m='More than 50!!!')

        cmds.select(selected)
        self.Z_InitialLoad()

    def PlutoGun_Shoot_cmd(self, frame_time, move):  # 开枪函数中用到的命令
        selected = cmds.ls(sl=1, type='transform')

        laser_Color = 'Red'
        if self.win.RedButton.isChecked():
            laser_Color = 'Red'
        elif self.win.GreenButton.isChecked():
            laser_Color = 'Green'
        elif self.win.BlueButton.isChecked():
            laser_Color = 'Blue'

        laser_GRP = ''

        if laser_Color == 'Red':
            if not cmds.objExists('GRP_laser_lightInder_001'):
                cmds.file(
                    "//file-cluster/GDC/Projects/Ninjago/Reference/TD/GDC_PlugIn/PlutoGun/laser_lightInder.mb",
                    i=1, type="mayaBinary", rpr="laser_lightInder", pr=1)
                laser_GRP = 'GRP_laser_lightInder_001'
            else:
                laser_GRP = cmds.duplicate('GRP_laser_lightInder_001')[0]

        elif laser_Color == 'Green':
            if not cmds.objExists('GRP_laser_lightInder_green_001'):
                cmds.file(
                    "//file-cluster/GDC/Projects/Ninjago/Reference/TD/GDC_PlugIn/PlutoGun/laser_lightInder_green.mb",
                    i=1, type="mayaBinary", rpr="laser_lightInder", pr=1)
                laser_GRP = 'GRP_laser_lightInder_green_001'
            else:
                laser_GRP = cmds.duplicate(
                    'GRP_laser_lightInder_green_001')[0]

        elif laser_Color == 'Blue':
            if not cmds.objExists('GRP_laser_lightInder_blue_001'):
                cmds.file(
                    "//file-cluster/GDC/Projects/Ninjago/Reference/TD/GDC_PlugIn/PlutoGun/laser_lightInder_blue.mb",
                    i=1, type="mayaBinary", rpr="laser_lightInder", pr=1)
                laser_GRP = 'GRP_laser_lightInder_blue_001'
            else:
                laser_GRP = cmds.duplicate('GRP_laser_lightInder_blue_001')[0]

        laser_GRP_laser = cmds.listRelatives(laser_GRP, c=1, path=1)[0]

        cmds.cutKey(laser_GRP_laser, t=(), at = "tx")
        cmds.setAttr((laser_GRP_laser + '.tx'), 0)
        cmds.cutKey(laser_GRP_laser, t=(), at = "ty")
        cmds.setAttr((laser_GRP_laser + '.ty'), 0)
        cmds.cutKey(laser_GRP_laser, t=(), at = "tz")
        cmds.setAttr((laser_GRP_laser + '.tz'), 0)

        temp_Constraint = cmds.parentConstraint(selected[0], laser_GRP)
        cmds.delete(temp_Constraint[0])

        frame_s = cmds.currentTime(query=1)
        frame_e = frame_s + 2

        position = cmds.getAttr((laser_GRP_laser + ".tz"))
        position_e = position + move * self.InitSpeed

        cmds.setKeyframe(
            laser_GRP_laser, attribute='visibility', t=frame_s - 1, v=0)

        cmds.setKeyframe(
            laser_GRP_laser, attribute='visibility', t=frame_s, v=1)

        cmds.setKeyframe(laser_GRP_laser, attribute='translateZ', t=frame_s)

        cmds.setKeyframe(
            laser_GRP_laser, attribute='translateZ', t=frame_e, v=position_e)

        cmds.selectKey(laser_GRP_laser, attribute='translateZ')
        cmds.setInfinity(pri='constant', poi='linear')
        cmds.keyTangent(laser_GRP_laser, edit=True,
                        attribute='translateZ',  itt='linear', ott='linear')

        cmds.currentTime(frame_s)

        return laser_GRP

    def keyPressEvent(self, event):  # 键盘事件
        if event.key() == Qt.Key_Delete:
            self.Z_DeleteLaser()
            pass

#   =====================ZZJ 写的函数=====================
    #   如果没有____PlutoGun____这个组，就创建一个
    def Z_InitialGroup(self):
#        创建一个空的____PlutoGun____的组
        if cmds.objExists('____PlutoGun____') == 0:
            cmds.group(em=True, n='____PlutoGun____')

#        如果self.Namespace不为空，则根据self.Namespace创建一个组
        if self.Namespace != '':
            current_Lasers = self.Namespace + "_Lasers"
            if cmds.objExists('____PlutoGun____|' + current_Lasers) == 0:
                cmds.group(em=True, )
                sle = cmds.ls(sl=1, type='transform', l=1)
                cmds.parent(sle[0], '____PlutoGun____')
                sle = cmds.ls(sl=1, type='transform', l=1)
                cmds.rename(sle[0], current_Lasers)

    def Z_LCD_Color(self, v):  # 滑条和显示的颜色做并联
        if v < 3:
            self.win.lcdNumber.setStyleSheet("color: rgb(192, 192, 192);")
        elif v < 5:
            self.win.lcdNumber.setStyleSheet("color: rgb(255, 255, 0);")
        elif v < 8:
            self.win.lcdNumber.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.win.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);")

    def Z_HeaderViewSelected(self, v):  # 选择表头时的动作
        Z_selectOBJ(self, self.tableView)

    #   每隔一秒刷新一次表格，选中上次所选的cell
    def Z_OnTimer(self):
        indexes = self.tableView.selectedIndexes()
#        self.Z_InitialLoad()
        for i in indexes:
            self.tableView.selectionModel().select(
                i, QItemSelectionModel.Select)

    #   当按下delete键的时候，执行此函数
    def Z_DeleteLaser(self, ):
        indexes = self.tableView.selectedIndexes()
        list = []

        for indexSel in indexes:
            if indexSel.column() == NAME:
                list.append(indexSel.row())
        list.sort()
        list.reverse()

        for a in list:

            name_index = self.model.index(a,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index).toString())
            try:
                cmds.delete(name)
            except:
                pass
            self.model.removeRow(a)

    #   当改变单元格内容后：  1.显示/隐藏模型   2. 改变速度   3.改变长度
    def Z_SomeDataChanged(self, x, y):
        if x.column() == VIS:
            row = x.row()

            name_index = self.model.index(row,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index).toString())

            model_index = self.model.index(row,  VIS)
            vis = self.model.data(model_index).toInt()[0]

            if cmds.objExists(name):
                try:
                    cmds.setAttr((name + '.v'), vis)
                except:
                    pass

        elif x.column() == SPEED:
            row = x.row()

            name_index = self.model.index(row,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index).toString())

            model_index = self.model.index(row,  SPEED)
            speed = self.model.data(model_index).toFloat()[0] * 20

            laser_GRP_laser = cmds.listRelatives(name, c=1, path=1)[0]

            keyCurveIndex = cmds.keyframe(laser_GRP_laser, q=1, at='tz')
#    如果key帧的数据不正确，直接删除key帧的信息
            keyCount = -1
            try:
                keyCount = len(keyCurveIndex)
            except:
                keyCount = 0
            if keyCount == 0 or keyCount != 2:
                cmds.cutKey(laser_GRP_laser, at='tz')
#    重新key帧
                frame_s = cmds.currentTime(query=1)
                frame_e = frame_s + 2
                position = cmds.getAttr((laser_GRP_laser + ".tz"))
                position_e = position + 20 * speed
                cmds.setKeyframe(
                    laser_GRP_laser, attribute='translateZ', t=frame_s)
                cmds.setKeyframe(
                    laser_GRP_laser, attribute='translateZ', t=frame_e, v=position_e)
#    把曲线打直
                cmds.selectKey(laser_GRP_laser, attribute='translateZ')
                cmds.setInfinity(pri='constant', poi='linear')
                cmds.keyTangent(
                    laser_GRP_laser, edit=True, attribute='translateZ',  itt='linear', ott='linear')
#    如果一切都正确，修改key帧信息
            cmds.keyframe(laser_GRP_laser, index=(
                1, 1), at='tz', valueChange=speed)

        elif x.column() == LENGTH:
            row = x.row()

            name_index = self.model.index(row,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index).toString())

            model_index = self.model.index(row,  LENGTH)
            length = self.model.data(model_index).toFloat()[0]

            laser_GRP_laser = cmds.listRelatives(name, c=1, path=1)[0]
            cmds.setAttr(laser_GRP_laser + '.sz', length)
            cmds.setKeyframe(laser_GRP_laser,  at='sz', v=length)
#    把曲线打直
            cmds.selectKey(laser_GRP_laser, attribute='scaleZ')
            cmds.setInfinity(pri='constant', poi='linear')
            cmds.keyTangent(
                laser_GRP_laser, edit=True, attribute='scaleZ',  itt='linear', ott='linear')

    def Z_InitialLoad(self):  # 初始化
#----------------------------------------删除旧的数据---------------------------
        count = self.model.rowCount()
        list = range(count)
        list.reverse()
        for i in list:
            self.model.removeRow(i)

#----------------------------------------新的数据-----------------------------
        current_Lasers = self.Namespace + "_Lasers"
        if cmds.objExists('____PlutoGun____|' + current_Lasers) == 0:
            return

        Lasers = cmds.listRelatives(
            '____PlutoGun____|' + current_Lasers, c=1, pa=1)
        try:
            len(Lasers)
        except:
            Lasers = []

        for name in Lasers:
#----------------------------------------Name-----------------------------
            name = name
#----------------------------------------Vis------------------------------
            vis = str(int(cmds.getAttr(name + ".v")))
#----------------------------------------Speed----------------------------
            laser_GRP_laser = cmds.listRelatives(name, c=1, path=1)[0]
            try:
                speed = cmds.keyframe(
                    laser_GRP_laser, at='tz', ev=1, index=(1, 1), q =1)[0]
            except:
                speed = cmds.getAttr(laser_GRP_laser + '.tz')
            speed = speed / 20

#----------------------------------------Length---------------------------
            length = cmds.getAttr(laser_GRP_laser + ".sz")

#----------------------------------------数据填入model------------------------
            ship = PlutoGunShip(name, vis, speed, length)
            self.model.ships.append(ship)

        self.model.reset()

    def Z_Low_High(self):  # 高低模切换
        Ctrl = self.Namespace + ':body_Ctrl'
        ctrl = self.Namespace + ':body_ctrl'
        try:
            state = cmds.getAttr(ctrl + '.low')
            cmds.setAttr((ctrl + '.low'), (1 - state))
        except:
            pass
        try:
            state = cmds.getAttr(Ctrl + '.low')
            cmds.setAttr((Ctrl + '.low'), (1 - state))
        except:
            pass

    def Z_create_camWin(self, cam):  # 创建摄像机工作视图到工具中
        cameras = cmds.ls(type='camera')
        cameras_tmp = cameras[:]
        for c in cameras:
            if c.find('FM_plutoGun_CAM') == -1:
                cameras_tmp.remove(c)
        cameras = cameras_tmp

        if len(cameras) == 0:
            return 'noCamera_In_File'
        camerasGP = []
        for a in cameras:
            camerasGP.append(cmds.listRelatives(a, parent=1)[0])

        self.Cams = camerasGP

        form = ''
        current_cam = ''
        if cam == 'first_time':
            self.Z_init_PlutoGun_Group()  # 创建____PlutoGun____的空组

            wind = cmds.window()
            form = cmds.formLayout()
            self.moEditor = cmds.modelEditor()
            current_cam = camerasGP[0]

            column = cmds.columnLayout('true')
            cmds.formLayout(form, e=True,
                            attachForm=[(column, 'top', 0), (column, 'left', 0), (self.moEditor, 'top', 0), (
                                self.moEditor, 'bottom', 0), (self.moEditor, 'right', 0)],
                            attachNone=[(column, 'bottom'), (column, 'right')],
                            attachControl=(self.moEditor, 'left', 0, column)
                            )
            cmds.modelEditor(self.moEditor, e=True,
                             camera=camerasGP[0],
                             allObjects=0,    grid=0, polymeshes=1, nurbsCurves=1, activeView=1,
                             displayAppearance='smoothShaded',  displayTextures=0
                             )
        else:
            current_cam = cam
            cmds.modelEditor(self.moEditor, edit=True,
                             camera=cam,
                             )

        self.Cam = current_cam
        current_cam_split = current_cam.split(':')

        self.Namespace = ':'.join(current_cam_split[:-1])

        return form

    #  如果没有____PlutoGun____这个组，就创建一个
    def Z_init_PlutoGun_Group(self):
        if cmds.objExists('____PlutoGun____') == 0:
            cmds.group(em=True, n='____PlutoGun____')

#        如果self.Namespace不为空，则根据self.Namespace创建一个组
        if self.Namespace != '':
            current_Lasers = self.Namespace + "_Lasers"
            if cmds.objExists('____PlutoGun____|' + current_Lasers) == 0:
                cmds.group(em=True, )
                sle = cmds.ls(sl=1, type='transform', l=1)

                cmds.parent(sle[0], '____PlutoGun____')

                sle = cmds.ls(sl=1, type='transform', l=1)
                cmds.rename(sle[0], current_Lasers)

    def Z_initComboBox(self):  # 初始化ComboBox
        self.win.comboBox.clear()
        i = 0
        if len(self.Cams) != 0:
            for cam in self.Cams:

                self.win.comboBox.addItem('')
                self.win.comboBox.setItemText(i, cam)
                i += 1


def Z_selectOBJ(PGW, tv):  # 选择maya里的模型
    Namespace = PGW.Namespace
    list = []
    for i in tv.selectedIndexes():
        print i
        if i.column() == NAME:
            print i
            name = '____PlutoGun____|' + Namespace + \
                "_Lasers|" + str(i.data().toString())
            list.append(name)
#   选择物体
    try:
        cmds.select(cl =1)
        cmds.select(list)
    except:
        pass

#    主函数，程序入口


def main():
    oldDialog = apiUI.MQtUtil.findWindow('PlutoGun')
    try:
        sip.wrapinstance(long(oldDialog), QtGui.QWidget).close()
    except:
        pass

    PlutoGW = PlutoGunWindow()
    PlutoGW.show()
