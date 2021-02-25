# -*- coding: utf-8 -*-
# Copyright (C) 2000-2012 IDMT. All rights reserved.
'''
Pluto Gun:
1)shoot the laser for YODA's craft
2)control the speed and vis for the lasers of the craft
'''
__author__ = 'zhaozhongjie'
__date__    = '2013-01-19'


from PyQt4 import QtGui, QtCore
from PyQt4.uic import loadUi
import sip
import maya.OpenMayaUI as apiUI
import maya.cmds as cmds
import maya.mel as mel

import os , sys
import time

#from myuis import resources_rc

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PlutoGun_Ships as ships
reload(ships)
NAME ,VIS,  SPEED = range(3)
#from myuis import resources



def getMayaWindow():                                          #   使用sip来获得maya的主窗口
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)


def toQtObject(mayaName):                                   #   获得maya控件的名称
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
    def __init__(self, name, vis, speed ):
        self.name = QString(name)
        self.vis = QString(vis)
        self.speed = speed

class PlutoGunTable(QTableView):                            #   自定义的tableView
    def __init__(self, PGW):
        super(PlutoGunTable, self).__init__()
        self.msw = PGW

#   鼠标释放后的事件-----选择物体
    def mouseReleaseEvent (self, QMouseEvent):
        QTableView.mouseReleaseEvent (self, QMouseEvent)
        Z_selectOBJ(self.msw, self)

class PlutoGunWindow( QtGui.QMainWindow):           #   PlutoGunWindow窗口
    def __init__(self, parent=getMayaWindow()):
        super(PlutoGunWindow, self).__init__(parent)
        self.setWindowTitle("PlutoGun")
        self.setObjectName("PlutoGun")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(800, 600)

#        self.setStyleSheet("background: url(:/myuis/StarWar.jpg);")

        self.setStyleSheet("QMainWindow{background: url(:/myuis/StarWar.jpg)}")
#        self.setStyleSheet("image: url(:/myuis/slider_knob.png)")
#        self.setStyleSheet("background: url(:/myuis/StarWar.jpg)")
#        self.setStyleSheet("background-color:rgb(100,0,0)")
#        self.setStyleSheet("background-color:transparent") 
        
#    获得当前文件所在目录，为了找到.ui文件
        path_split = __file__.split('\\')
        path = '\\'.join(path_split[:-1])
        win = os.path.join(path, 'PlutoGunWin.myuis')

#    将loadUi的窗体作为子窗体
        self.win = loadUi(win , QtGui.QMainWindow()) 
#        return
        self.win.tableWidget.deleteLater()
        
#   时间发射器
        self.timer=QtCore.QTimer()
        
        
        self.splitter = QtGui.QSplitter()
        self.splitter.setStyleSheet("background-color:transparent;")
        
        self.splitter.addWidget(self.win.widget_left)
        self.splitter.addWidget(self.win.widget_right)
        self.splitter.setOrientation(0x1)
        self.setCentralWidget(self.splitter) 
        

       
        

#   =====================ZZJ 写的函数=====================


def main():                                                             #    主函数，程序入口
    oldDialog = apiUI.MQtUtil.findWindow('PlutoGun')
    try:
        sip.wrapinstance(long(oldDialog), QtGui.QWidget).close()
    except:
        pass
    
    PlutoGW = PlutoGunWindow()
    PlutoGW.show()   
