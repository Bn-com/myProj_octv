# -*- coding: utf-8 -*-
import maya.OpenMayaUI as apiUI
from PyQt4 import QtGui, QtCore
import sip
import maya.cmds as cmds
from PyQt4.uic import loadUi
import os , sys
import time
#import pymel.core as pm
import maya.mel as mel


def main():
    
    oldDialog = apiUI.MQtUtil.findWindow('PlutoGun')
    try:
        sip.wrapinstance(long(oldDialog), QtGui.QWidget).close()
    except:
        pass
    
    PlutoGunWindow = MayaSubWindow()
    PlutoGunWindow.show()   

def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

def toQtObject(mayaName):
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


#global PlutoGunScriptNode
#PlutoGunScriptNode = 0
    
class MayaSubWindow(QtGui.QMainWindow):
    def __init__(self, parent=getMayaWindow()):
        super(MayaSubWindow, self).__init__(parent)
        self.setWindowTitle("PlutoGun")
        self.setObjectName("PlutoGun")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        
#    这里是用来备份的，各种不同的窗体写法
##        wgt = os.path.join(path, 'wgt.myuis')
##        wgt = loadUi(wgt , QtGui.QWidget()) 
##        self.setCentralWidget(wgt)
        
##        form = cmds.formLayout()
##        cmds.button()
##        qtObj = toQtObject(form)
##        self.setCentralWidget(qtObj)     

#    获得当前文件所在目录，为了找到.ui文件
        path_split = __file__.split('\\')
        path = '\\'.join(path_split[:-1])
        win = os.path.join(path, 'PlutoGunWin.myuis')

#    将loadUi的窗体作为子窗体
        self.win = loadUi(win , QtGui.QMainWindow()) 
#        self.setCentralWidget(self.win)

        self.splitter = QtGui.QSplitter()
        self.splitter.addWidget(self.win.widget_left)
        self.splitter.addWidget(self.win.widget_right)

        self.splitter.setOrientation(0x1)
        
        self.setCentralWidget(self.splitter) 


#        创建一个scriptNode用来并联选择的曲线和table的显示
#            self.ScriptJobNum = cmds.scriptJob( e= ["SelectionChanged","PlutoGun.MayaSubWindow().selected_Change_ScriptJob()"], protected=True)
#    创建摄像机视图
        self.Cams = []
        self.Cam = ''
        self.Namespace = ''
        self.Speed = 2
        self.moEditor =''
        
        cam_Window = self.create_camWin("first_time")
        if cam_Window != 'noCamera_In_File':
            self.win.tmp_label.deleteLater()        
            qtObj = toQtObject(cam_Window)
            self.win.Left_Layout.addWidget(qtObj)

#   飞机选择菜单初始化
            self.initComboBox()
            self.initTable()

#    高低模切换
        QtCore.QObject.connect(self.win.Low_High, QtCore.SIGNAL("clicked()"), self.Low_High)
#    comboBox 选项改变后， 刷新飞船
        QtCore.QObject.connect(self.win.comboBox, QtCore.SIGNAL("currentIndexChanged(QString)"), self.refresh_Aircraft)
#    发射激光        
        QtCore.QObject.connect(self.win.Shoot_Gun, QtCore.SIGNAL("clicked()"), self.PlutoGun_Shoots)
#   Speed滑动条值改变后，并联的东西            
        QtCore.QObject.connect(self.win.horizontalSlider, QtCore.SIGNAL("valueChanged(int)"), self.set_Speed)
#   选择行首的标签后，自动选择该物体
        QtCore.QObject.connect(self.win.tableWidget, QtCore.SIGNAL("itemSelectionChanged()"), self.selections)


    def selections(self):
        list = []
        for a in  self.win.tableWidget.selectedIndexes():
            if a.column() == 0:
                index = a.row()
                list.append(index)
        loser = []
        for b in list:
            name = str(self.win.tableWidget.item(b, 0).text())
            loser.append(name)
        
            
        if len(loser): cmds.select(loser)
        else:   cmds.select(cl=1)
#        print xx
        
        
    def create_camWin(self, cam):                                   #创建摄像机工作视图到工具中
        
        cameras = cmds.ls(type = 'camera')

        cameras_tmp = cameras[:]
        for c in cameras:
            if c.find('FM_plutoGun_CAM')==-1:
                cameras_tmp.remove(c)
        cameras = cameras_tmp
        
        if len(cameras) == 0:
            return 'noCamera_In_File'
        camerasGP = []
        for a in cameras:
            camerasGP.append(cmds.listRelatives(a, parent =1)[0])
    
        self.Cams = camerasGP

        form = ''
        current_cam = ''
        if cam == 'first_time':
            
            wind = cmds.window()
            form = cmds.formLayout()
            self.moEditor = cmds.modelEditor()
            current_cam= camerasGP[0]
            
            column = cmds.columnLayout('true')
            cmds.formLayout( form, e=True, 
                            attachForm=[(column, 'top', 0), (column, 'left', 0), (self.moEditor, 'top', 0), (self.moEditor, 'bottom', 0), (self.moEditor, 'right', 0)], 
                            attachNone=[(column, 'bottom'), (column, 'right')], 
                            attachControl=(self.moEditor, 'left', 0, column)
                            )
            cmds.modelEditor( self.moEditor, e=True, 
                             camera= camerasGP[0], 
                             allObjects = 0,    grid = 0, polymeshes = 1, nurbsCurves = 1, activeView =1, 
                             displayAppearance = 'smoothShaded',  displayTextures = 0
                            )     
        else:
            current_cam= cam
            cmds.modelEditor( self.moEditor, edit=True, 
                             camera= cam, 
                            )    
        
        self.Cam = current_cam
        current_cam_split = current_cam.split(':')
        self.Namespace = ':'.join(current_cam_split[:-1])
        
#        print self.Namespace
        
        return form
        





    def refresh_Aircraft(self):                                          #当改变comboBox的时候，此函数，用来刷新所有控件
#    求comboBox中，选中的摄像机
        currentText = str(self.win.comboBox.currentText())
        
#    设置当前的视图中的摄像机
        cam_Window = self.create_camWin(currentText)
        self.Cam = currentText
        self.initTable()
#        self.selected_Change_ScriptJob()
        
    def set_Speed(self, speed):                                        #设置滑条的变化改变函数
        self.Speed = int(speed)


        
        
    def show_hide(self, xx):
        
        
        x =  xx.row()
        y =  xx.column()
        
        value = str(xx.text())
        if value != '0':
            value = 1
        else:
            value = 0
        
        selectItems = self.win.tableWidget.selectedIndexes()
        list = []
        for a in  selectItems:
            if a.column() == 1:
                index = a.row()
                list.append(index)

        for b in list:
            name = str(self.win.tableWidget.item(b, 0).text())
#        print name, x, y, value
            cmds.setAttr(name+'.lodVisibility', value)
        
        self.initTable()
        
        self.win.tableWidget.clearSelection()
        for a in  selectItems:
            self.win.tableWidget.setItemSelected(self.win.tableWidget.item( a.row(),a.column()),  1)

    def Low_High(self):
        Ctrl = self.Namespace + ':body_Ctrl'
        ctrl = self.Namespace + ':body_ctrl'
        try:
            state = cmds.getAttr(ctrl+'.low')
            cmds.setAttr( (ctrl+'.low'),(1-state))
        except:
            pass
        try:
            state = cmds.getAttr(Ctrl+'.low')
            cmds.setAttr( (Ctrl+'.low'),(1-state))
        except:
            pass



    def closeEvent(self, event):                                        #关闭窗口后，消除一些多余的控件和窗体
        print 'Close!!!!!'





    def PlutoGun_Shoots(self):                                          #连发开枪的主函数
        print 'xxx'
        selected = cmds.ls(sl =1, type='transform') 
        for s in selected:
            cmds.select(cl=1)
            cmds.select(s)
            self.PlutoGun_Shoot()
        cmds.select(cl=1)
        cmds.select(selected)
        
    def PlutoGun_Shoot(self):                                           #开枪的主函数
        selected = cmds.ls(sl =1, type='transform') 
        if len(selected)==0:    return
        select_split = selected[0].split(':')
        select_namespace = ':'.join(select_split[:-1])
        select_contrl = select_split[-1]       
        
        
        if select_namespace == self.Namespace: 
            try:
                cmds.setAttr(selected[0]+'.plutoGun', 1)
            except:
                return
                pass
        else:
            return
            
        
        self.init____PlutoGun____Group()
            
        current_Bullets = self.Namespace+"_Bullets"
            
#        Bullets = pm.ls('____PlutoGun____|'+current_Bullets)[0].listRelatives()
        Bullets = cmds.listRelatives('____PlutoGun____|'+current_Bullets , c=1 , pa=1)
        try:
            len(Bullets)
        except:
            Bullets = []
        if len(Bullets)<20:
            cmds.select(selected)
            
            new_Bullet = self.PlutoGun_Shoot_cmd(2, 10)
            try:
                cmds.parent(new_Bullet, '____PlutoGun____|'+current_Bullets)
            except:
                pass
            
        else:
            cmds.confirmDialog(m='More than 20!!!')

            
        cmds.select(selected)
        self.initTable()
        



    def PlutoGun_Shoot_cmd(self, frame_time,move):          #开枪函数中用到的命令
        selected = cmds.ls(sl =1, type='transform') 
        
        laser_GRP = ''
        
        if not cmds.objExists('GRP_laser_lightInder_001'):
            cmds.file( "Z:/Resource/Support/Maya/projects/YODA/laser_lightInder.mb",
                      i = 1 ,type = "mayaBinary" , rpr = "laser_lightInder" , pr = 1  )
            laser_GRP = 'GRP_laser_lightInder_001'
        
        else:
            laser_GRP = cmds.duplicate( 'GRP_laser_lightInder_001' )[0]
        
        laser_GRP_laser = cmds.listRelatives(laser_GRP, c=1 , path = 1)[0]
        
        temp_Constraint = cmds.parentConstraint(selected[0],laser_GRP )
        cmds.delete(temp_Constraint[0])
        
        frame_s = cmds.currentTime(query =1)
        frame_e = frame_s + frame_time       
        
        position = cmds.getAttr((laser_GRP_laser+".tz"))
        position_e = position + move*self.Speed

        
        cmds.setKeyframe(laser_GRP_laser, attribute='visibility',t= frame_s-1  ,v=0)

        cmds.setKeyframe(laser_GRP_laser, attribute='visibility',t= frame_s  ,v=1)

        cmds.setKeyframe(laser_GRP_laser, attribute='translateZ',t= frame_s)
        
        cmds.setKeyframe(laser_GRP_laser, attribute='translateZ',t= frame_e  , v = position_e)



        cmds.selectKey( laser_GRP_laser, attribute='translateZ' )
        cmds.setInfinity( pri='constant', poi='linear' )
        cmds.keyTangent(laser_GRP_laser, edit=True, attribute='translateZ',  itt='linear', ott='linear' )


        

        cmds.currentTime(frame_s)
        
        return laser_GRP
        


#        PlutoGun_Bullet = pm.ls('____PlutoGun____')[0].listRelatives()
#        
#        if self.Namespace in PlutoGun_Bullet:
#            print 'OKOK'
#        
#        else:        
#            xx = cmds.group( em=True)
#            cmds.parent(xx , '____PlutoGun____' )
#            cmds.rename('____PlutoGun____'+"|"+xx,self.Namespace)
        
        


 
 
    def init____PlutoGun____Group(self):                         #如果没有____PlutoGun____这个组，就创建一个
#        创建一个空的____PlutoGun____的组
        if cmds.objExists('____PlutoGun____')==0:
            cmds.group( em=True, n = '____PlutoGun____' )
        
#        如果self.Namespace不为空，则根据self.Namespace创建一个组
        if self.Namespace !='':            
            current_Bullets = self.Namespace+"_Bullets"
            if cmds.objExists('____PlutoGun____|'+current_Bullets)==0:
                cmds.group( em=True, )
                sle = cmds.ls(sl =1, type='transform',l =1) 
                cmds.parent(sle[0] , '____PlutoGun____' )
                sle = cmds.ls(sl =1, type='transform',l =1)      
                cmds.rename(sle[0], current_Bullets)    
    
    def initComboBox(self):                                             #初始化
        self.win.comboBox.clear()
        i = 0
        if len(self.Cams)!=0:
            for cam in self.Cams:
                
                self.win.comboBox.addItem('')
                self.win.comboBox.setItemText(i,cam )
                i+=1
        
 

    
    def initTable(self):                                                     #属性的chennelBox
#        item = win.tableWidget.selectedItems()
        QtCore.QObject.disconnect(self.win.tableWidget, QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), self.show_hide)
        
        self.win.tableWidget.setRowCount(0)
        current_Bullets = self.Namespace+"_Bullets"
        
        if cmds.objExists('____PlutoGun____|'+current_Bullets)==0:  return
#        Bullets = pm.ls('____PlutoGun____|'+current_Bullets)[0].listRelatives()
        Bullets = cmds.listRelatives('____PlutoGun____|'+current_Bullets , c=1 , pa=1)
        try:
            len(Bullets)
        except:
            Bullets = []
#        print dir(self.win.tableWidget)
        num = len(Bullets)
        self.win.tableWidget.setRowCount(num)
        
        
        for i in range(num):
            item = QtGui.QTableWidgetItem()
            item.setText(str(Bullets[i]))
            item.setFlags(QtCore.Qt.ItemFlag(32|1))

            color = QtGui.QColor()
            color.setRgb(100, 100, 100, 255)
            item.setBackgroundColor (color)
            self.win.tableWidget.setItem(i,0,  item)
            
            item = QtGui.QTableWidgetItem()
            item.setTextAlignment(0x0080|0x0004)
            vis = cmds.getAttr(Bullets[i]+".lodVisibility")
            item.setText(str(int(vis)))


            self.win.tableWidget.setItem(i,1,  item)
        self.win.tableWidget.setColumnWidth(0, 200)
        self.win.tableWidget.setColumnWidth(1, 30)
        self.win.tableWidget.setColumnWidth(2, 100)
#        self.win.tableWidget.horizontalHeader().setResizeMode(0)
#        self.win.tableWidget.horizontalHeader().resizeSection (1, 20)
        
        self.win.tableWidget.horizontalHeader().setResizeMode(0, QtGui.QHeaderView.Stretch)  
        self.win.tableWidget.horizontalHeader().setResizeMode(2, QtGui.QHeaderView.Stretch)  
        
        QtCore.QObject.connect(self.win.tableWidget, QtCore.SIGNAL("itemChanged(QTableWidgetItem*)"), self.show_hide)    








# 运行此工具的命令
#import idmt.maya.Pluto.PlutoGun.PlutoGun as PlutoGun
#reload(PlutoGun)
#PlutoGun.main()

'''
    def selected_Change_ScriptJob(self):
    
    
        self.Cam = str(self.win.comboBox.currentText())
        
        selected = cmds.ls(sl =1, type='transform')
        if len(selected) == 0:  return          #没选中物体，就停止

#        currentText = str(self.win.comboBox.currentText())

#        当前视图飞船摄像机
        currentCam =  str(self.win.comboBox.currentText())
        
        currentCam_split = currentCam.split(':')
        
        currentCam_namespace = ':'.join(currentCam_split[:-1])
        currentCam_contrl = currentCam_split[-1]
        
#        当前选中的物体
        select_split = selected[0].split(':')
        select_namespace = ':'.join(select_split[:-1])
        select_contrl = select_split[-1]
        
#        ----判断选择的曲线是不是当前视图飞船下的控制器        
        if select_namespace == currentCam_namespace:
            try:
                cmds.setAttr(selected[0]+'.plutoGun', 1)
                self.initTable()
            except:
                pass


'''

