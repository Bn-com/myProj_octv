#-*- coding: gbk -*-
'''
Created on 2013-8-20
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
usage:
    import idmt.maya.Pluto.Maya.Rnd.ImageFileManager.Main as isp
    reload(isp)
    isp.main()
'''

import os,sys
import PyQt4

import maya.OpenMayaUI as apiUI
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import loadUi

def getMayaWindow():                                          #   使用sip来获得maya的主窗口
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

class MainWindow(QtGui.QMainWindow):
    def __init__(self , parent=None):
        super(MainWindow, self).__init__(parent)
        
# class MainWindow(QtGui.QMainWindow):
#     def __init__(self, parent=getMayaWindow()):
#         super(MainWindow, self).__init__(parent)




def main():
#     app = qApp
    mainWin = MainWindow()
    mainWin.show()


