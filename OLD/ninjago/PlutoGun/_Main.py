# -*- coding: utf-8 -*-
# Copyright (C) 2000-2013 IDMT. All rights reserved.
'''
Pluto Gun:
1)shoot the laser for YODA's craft
2)control the speed and vis for the lasers of the craft
'''
__author__ = 'zhaozhongjie'
__date__ = '2013-11-12'

from PySide.QtCore import *
from PySide.QtGui import *
# import sip
import shiboken
import maya.OpenMayaUI as apiUI
import maya.cmds as cmds
import maya.mel as mel

import ui.My_TableView as xxx
reload(xxx)
My_TableView = xxx.My_TableView

import ui.My_TableModel
reload(ui.My_TableModel)

import ui.PlutoGunWin
reload(ui.PlutoGunWin)

import os
import sys
import time

# import PlutoGun_Ships2 as ships
# reload(ships)
NAME, VIS,  SPEED, LENGTH = range(4)
CAM_KW = "FM_plutoGun_CAM"



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








class PlutoGunWindow(QMainWindow):  # PlutoGunWindow窗口
    def __init__(self, parent=getMayaWindow()):
        super(PlutoGunWindow, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.win = ui.PlutoGunWin.Ui_PlutoGun()
        self.win.setupUi(self)
        folder = os.path.dirname(__file__)
        self.red_laser = os.path.join(folder, "laser_lightInder_red.mb")
        self.green_laser = os.path.join(folder, "laser_lightInder_green.mb")
        self.blue_laser = os.path.join(folder, "laser_lightInder_blue.mb")

        self.win.splitter.setSizes([300, 100])

        self.Namespace = ''
        self.InitSpeed = 5
        self.moPanel = ''
        self.tableView = self.win.tableView
        self.model = self.tableView.model
        self.cameras = []
        self.current_cam = ''
        cam_Window = self.Z_create_camWin("first_time")
        if cam_Window != 'noCamera_In_File':
            self.win.tmp_label.deleteLater()
            qtObj = toQtObject(cam_Window)
            self.win.Left_Layout.addWidget(qtObj)

            self.Z_initComboBox()
            self.Z_InitialLoad()
            self.Z_LCD_Color(5)

            self.connection()

    # def keyPressEvent(self, event):
    #     super(PlutoGunWindow,self).keyPressEvent(event)
    #     print event.key()

    def connection(self):
        # comboBox 选项改变后， 刷新飞船
        self.win.comboBox.currentIndexChanged.connect(self.PlutoGun_RefreshAircraft)
#    数据改变后的操作
        self.model.dataChanged.connect(self.Z_SomeDataChanged)
#    高低模切换
        self.win.Low_High.clicked.connect(self.Z_Low_High)
#    刷新表格
        self.win.Refresh.clicked.connect(self.Z_InitialLoad)
#    刷新初始速度
        self.win.horizontalSlider.valueChanged.connect(self.Z_LCD_Color)
        self.win.horizontalSlider.valueChanged[int].connect(self.PlutoGun_Setspeed)
#    horizontalHeaderView选择整列后，自动选择物体
        self.tableView.horizontalHeader().sectionClicked.connect(self.Z_selectOBJ)

#    发射激光
        self.win.Shoot_Gun.clicked.connect(self.PlutoGun_Shoots)



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

        if len(self.Namespace)==0:
            cmds.confirmDialog(m='No NameSpace!\n Make sure your selected obj is referenced')

        if select_namespace != self.Namespace:
            return
        else:
            pass
            # try:
            #     cmds.setAttr(selected[0] + '.plutoGun', 1)
            # except:
            #     print u'该控制器上没有plutoGun属性，请联系前期添加'
            #     return
            #     pass

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
            if not cmds.objExists('GRP_laser_lightInder_red_001'):
                cmds.file(
                    self.red_laser,
                    i=1, type="mayaBinary", rpr="laser_lightInder", pr=1)
                laser_GRP = 'GRP_laser_lightInder_red_001'
            else:
                laser_GRP = cmds.duplicate('GRP_laser_lightInder_red_001')[0]

        elif laser_Color == 'Green':
            if not cmds.objExists('GRP_laser_lightInder_green_001'):
                cmds.file(
                    self.green_laser,
                    i=1, type="mayaBinary", rpr="laser_lightInder", pr=1)
                laser_GRP = 'GRP_laser_lightInder_green_001'
            else:
                laser_GRP = cmds.duplicate(
                    'GRP_laser_lightInder_green_001')[0]

        elif laser_Color == 'Blue':
            if not cmds.objExists('GRP_laser_lightInder_blue_001'):
                cmds.file(
                    self.blue_laser,
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
        print move
        print self.InitSpeed
        position_e = position + move * self.InitSpeed

        cmds.setKeyframe(
            laser_GRP_laser, attribute='visibility', t=frame_s - 1, v=0)

        cmds.setKeyframe(
            laser_GRP_laser, attribute='visibility', t=frame_s, v=1)

        cmds.setKeyframe(laser_GRP_laser, attribute='translateZ', t=frame_s)

        cmds.setKeyframe(
            laser_GRP_laser, attribute='translateZ', t=frame_e, v=position_e)

        cmds.selectKey(laser_GRP_laser, attribute='translateZ')
        cmds.setInfinity(pri='constant', poi='cycleRelative')
        cmds.keyTangent(laser_GRP_laser, edit=True,
                        attribute='translateZ',  itt='linear', ott='linear')

        cmds.currentTime(frame_s)

        return laser_GRP


    def PlutoGun_Setspeed(self, speed):  # 设置滑条的变化改变函数
        self.InitSpeed = int(speed)


    def Z_LCD_Color(self, v):  # 滑条和显示的颜色做并联
        if v < 3:
            self.win.lcdNumber.setStyleSheet("color: rgb(192, 192, 192);")
        elif v < 5:
            self.win.lcdNumber.setStyleSheet("color: rgb(255, 255, 0);")
        elif v < 8:
            self.win.lcdNumber.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.win.lcdNumber.setStyleSheet("color: rgb(255, 0, 0);")


    def Z_initComboBox(self):  # 初始化ComboBox
        self.win.comboBox.clear()
        i = 0
        for cam in self.cameras:
            self.win.comboBox.addItem('')
            self.win.comboBox.setItemText(i, cam)
            i += 1


    def PlutoGun_RefreshAircraft(self):
        #    求comboBox中，选中的摄像机
        currentText = str(self.win.comboBox.currentText())

#    设置当前的视图中的摄像机
        cam_Window = self.Z_create_camWin(currentText)
        self.current_cam = currentText
        self.Z_InitialLoad()


    # 创建摄像机
    def Z_create_camWin(self, cam):
        self.cameras = [cmds.listRelatives(c, parent=1)[0] for c in cmds.ls(type='camera') if CAM_KW in c]

        if len(self.cameras) == 0:
            cmds.confirmDialog(m='Error!!! \n   Must have a camera named "FM_plutoGun_CAM" in selected prop! ')
            return 'noCamera_In_File'
        form = ''
        if cam == 'first_time':
            self.Z_init_PlutoGun_Group()  # 创建____PlutoGun____的空组

            wind = cmds.window()
            form = cmds.paneLayout()
            self.moPanel = cmds.modelPanel()
            self.current_cam = self.cameras[0]
            cmds.modelPanel(self.moPanel, e=True,cam=self.current_cam)
            moEditor = cmds.modelPanel(self.moPanel,q=1,modelEditor=1)
            cmds.modelEditor(moEditor, e=True,
                             camera=self.cameras[0],
                             allObjects=0,    grid=0, polymeshes=1, nurbsCurves=1, activeView=1,
                             displayAppearance='smoothShaded',  displayTextures=0
                             )
        else:
            self.current_cam = cam
            cmds.modelPanel(self.moPanel, e=True,cam=self.current_cam)

        tmp = self.current_cam.split(':')
        self.Namespace = ':'.join(tmp[:-1])
        # self.moPanel
        return form





    #   如果没有____PlutoGun____这个组，就创建一个
    def Z_InitialGroup(self):
        # 创建一个空的____PlutoGun____的组
        if cmds.objExists('____PlutoGun____') == 0:
            cmds.group(em=True, n='____PlutoGun____')

        # 如果self.Namespace不为空，则根据self.Namespace创建一个组
        if self.Namespace != '':
            current_Lasers = self.Namespace + "_Lasers"
            if cmds.objExists('____PlutoGun____|' + current_Lasers) == 0:
                cmds.group(em=True, )
                sle = cmds.ls(sl=1, type='transform', l=1)
                cmds.parent(sle[0], '____PlutoGun____')
                sle = cmds.ls(sl=1, type='transform', l=1)
                cmds.rename(sle[0], current_Lasers)











    # 初始化数据
    def Z_InitialLoad(self):
        # ----------------------------------------删除旧的数据---------------------------
        count = self.model.rowCount()
        list = range(count)
        list.reverse()
        for i in list:
            self.model.removeRow(i)
        # ----------------------------------------新的数据-----------------------------
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
            # ----------------------------------------Name-----------------------------
            name = name
            # ----------------------------------------Vis------------------------------
            vis = str(int(cmds.getAttr(name + ".v")))
            # ----------------------------------------Speed----------------------------
            laser_GRP_laser = cmds.listRelatives(name, c=1, path=1)[0]
            try:
                speed = cmds.keyframe(
                    laser_GRP_laser, at='tz', ev=1, index=(1, 1), q =1)[0]
            except:
                speed = cmds.getAttr(laser_GRP_laser + '.tz')
            speed = speed / 20

        # ----------------------------------------Length---------------------------
            length = cmds.getAttr(laser_GRP_laser + ".sz")

        # ----------------------------------------数据填入model------------------------
            ship = ui.My_TableModel.PlutoGunShip(name, vis, speed, length)
            self.model.ships.append(ship)
        self.model.reset()








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
                "_Lasers|" + str(self.model.data(name_index))
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
                "_Lasers|" + str(self.model.data(name_index))

            model_index = self.model.index(row,  VIS)
            vis = self.model.data(model_index)

            if cmds.objExists(name):
                try:
                    cmds.setAttr((name + '.v'), vis)
                except:
                    pass

        elif x.column() == SPEED:
            row = x.row()

            name_index = self.model.index(row,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index))

            model_index = self.model.index(row,  SPEED)
            speed = self.model.data(model_index) * 20

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
                cmds.setInfinity(pri='constant', poi='cycleRelative')
                cmds.keyTangent(
                    laser_GRP_laser, edit=True, attribute='translateZ',  itt='linear', ott='linear')
#    如果一切都正确，修改key帧信息
            cmds.keyframe(laser_GRP_laser, index=(
                1, 1), at='tz', valueChange=speed)

        elif x.column() == LENGTH:
            row = x.row()

            name_index = self.model.index(row,  NAME)
            name = '____PlutoGun____|' + self.Namespace + \
                "_Lasers|" + str(self.model.data(name_index))

            model_index = self.model.index(row,  LENGTH)
            length = self.model.data(model_index)

            laser_GRP_laser = cmds.listRelatives(name, c=1, path=1)[0]
            cmds.setAttr(laser_GRP_laser + '.sz', length)
            cmds.setKeyframe(laser_GRP_laser,  at='sz', v=length)
#    把曲线打直
            cmds.selectKey(laser_GRP_laser, attribute='scaleZ')
            cmds.setInfinity(pri='constant', poi='cycleRelative')
            cmds.keyTangent(
                laser_GRP_laser, edit=True, attribute='scaleZ',  itt='linear', ott='linear')





    def Z_selectOBJ(self):  # 选择maya里的模型
        Namespace = self.Namespace
        list = []
        for i in self.tableView.selectedIndexes():
            if i.column() == NAME:
                name = '____PlutoGun____|' + Namespace + \
                    "_Lasers|" + str(i.data())
                list.append(name)
    #   选择物体
        try:
            cmds.select(cl=1)
            cmds.select(list)
        except:
            pass






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












#    主函数，程序入口
def main():
    oldDialog = apiUI.MQtUtil.findWindow('PlutoGun')
    try:
        shiboken.wrapInstance(long(oldDialog), QWidget).close()
    except:
        pass

    PlutoGW = PlutoGunWindow()
    PlutoGW.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main()
    sys.exit(app.exec_())