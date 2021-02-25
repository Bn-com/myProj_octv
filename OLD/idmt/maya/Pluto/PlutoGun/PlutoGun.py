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


    
class MayaSubWindow(QtGui.QMainWindow):
    def __init__(self, parent=getMayaWindow()):
        super(MayaSubWindow, self).__init__(parent)
        self.setWindowTitle("PlutoGun")
        self.setObjectName("PlutoGun")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        