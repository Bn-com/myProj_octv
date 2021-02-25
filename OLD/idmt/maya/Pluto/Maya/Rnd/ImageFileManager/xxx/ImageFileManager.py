#-*- coding: gbk -*-
'''
Created on 2013-8-20
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
usage:
    import idmt.maya.Pluto.Maya.Rnd.ImageSwitchPath as isp
    reload(isp)
    isp.main()
'''

import os,sys

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import loadUi
import sip
# import maya.OpenMayaUI as apiUI
# import maya.cmds as cmds
# import maya.mel as mel


def getMayaWindow():                                          #   使用sip来获得maya的主窗口
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

        
def main():                                                             #    程序的入口
    oldDialog = apiUI.MQtUtil.findWindow('ImageSwitchPath')
    try:
        sip.wrapinstance(long(oldDialog), QtGui.QWidget).close()
    except:
        pass
    pgw = ImageSwitchPath()
    pgw.show()   
    


my_array = [str(i) for i in range(5)]



class ImageSwitchPath(QtGui.QMainWindow):
    '''
    classdocs
    '''
    FILE =__file__
    UI = os.path.splitext(FILE)[0] + '.myuis'

    def __init__(self,parent =None):
        '''
        Constructor
        '''
        super(ImageSwitchPath, self).__init__(parent)
        self.setWindowTitle("ImageSwitchPath")
        self.setObjectName("ImageSwitchPath")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(800, 600)
        
        self.win = loadUi(self.UI,QtGui.QMainWindow()) 
        
        self.splitter = QtGui.QSplitter()
        self.splitter.setStyleSheet("background-color:transparent;")
        
        self.splitter.addWidget(self.win)
        self.splitter.addWidget(self.win)
        self.splitter.setOrientation(0x1)
        self.setCentralWidget(self.win) 
        
        self.setTabelView_list()



    def setTabelView_list(self):
        tablemodel = MyTableModel_list(my_array, self)
        self.win.tableView_list.setModel(tablemodel)

        tableDelegate = MyShipDelegate(self)
        self.win.tableView_list.setItemDelegate(tableDelegate)

        

class MyTableModel_list(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
    def rowCount(self, parent):
        return 1
    def columnCount(self, parent):
        return 5
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return (self.arraydata[index.column()][index.row()])
    
    
    
    def flags(self, index):
        return Qt.ItemFlags(
                QAbstractTableModel.flags(self, index) |
                Qt.ItemIsEditable)    

class MyShipDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super(MyShipDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        ctrl = QSlider(parent)
        ctrl.setOrientation(Qt.Horizontal)

        return ctrl

app = QApplication(sys.argv)
pgw = ImageSwitchPath()
pgw.show()   
app.exec_()    
    
    
    
