#-*- coding: gbk -*-
'''
Created on 2013-8-20
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
#usage:
import idmt.maya.Pluto.GdcP2.Ani.Header_Shoulder_Ctrl as hsc
reload(hsc)
hsc.main()
    
'''

import os,sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.uic import loadUi
import sip
import maya.OpenMayaUI as apiUI
import maya.OpenMaya as om
import maya.cmds as cmds
import maya.mel as mel
sys.path.append(r'\\file-cluster\gdc\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\Pluto')

import MyPyQt.setWindow as MySW



def getMayaWindow():                                          #   使用sip来获得maya的主窗口
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QtCore.QObject)

        


def main():                                                             #    主函数，程序入口
    oldDialog = apiUI.MQtUtil.findWindow('Header_Shoulder_Ctrl')
    try:
        sip.wrapinstance(long(oldDialog), QtGui.QWidget).close()
    except:
        pass
    
    PlutoGW = Header_Shoulder_Ctrl()
    if PlutoGW.SelectChr != False:
        PlutoGW.show()   





class Header_Shoulder_Ctrl(QtGui.QMainWindow):
    '''
    classdocs
    '''
    FILE =__file__
    UI = os.path.splitext(FILE)[0] + '.myuis'
    SelectChr = False

    def __init__(self,parent =getMayaWindow()):
        '''
        Constructor
        '''
        super(Header_Shoulder_Ctrl, self).__init__(parent)
        self.setWindowTitle("Header_Shoulder_Ctrl")
        self.setObjectName("Header_Shoulder_Ctrl")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.resize(400, 80)
        
        self.win = loadUi(self.UI,QtGui.QMainWindow()) 
        
        self.splitter = QtGui.QSplitter()
        self.splitter.setStyleSheet("background-color:transparent;")
         
        self.splitter.addWidget(self.win)
        self.splitter.addWidget(self.win)
        self.splitter.setOrientation(0x1)
        self.setCentralWidget(self.win) 
         
        MySW.setQMainWindow().setFollowMouse(self)                          #    设置窗口初始位置跟着鼠标
         
        sl = cmds.ls(sl=1)                                                                               #    判断是否选择了角色
        if sl ==[] or ':' not in sl[0]:
            cmds.confirmDialog(m='Please Select a Character!!')
        else:
            self.SelectChr = ':'.join(sl[0].split(':')[:-1])
            
            self.win.lineEdit.setText(self.SelectChr)
            
            self.H = self.SelectChr + ":" + "head_ctrl.rx"
            self.L = self.SelectChr + ":" + "Lf_shoulder.rz"
            self.R = self.SelectChr + ":" + "Rt_shoulder.rz"
            
            self.MyInitValue()

            #===========================================================================================
            # CONNECTION
            #===========================================================================================
            
            self.win.slider_h.sliderPressed.connect(lambda:cmds.undoInfo(openChunk=True))               #    锁住maya的撤销信息
            self.win.slider_h.sliderReleased.connect(self.MyInitValue)
            self.win.slider_h.sliderReleased.connect(lambda:self.win.slider_h.setValue(0))
            
            self.win.slider_h.valueChanged.connect(lambda x: self.win.lcdNumber.display(float(x)/5))
            self.win.slider_h.valueChanged.connect(self.MySetValue)
            self.win.slider_h.sliderReleased.connect(lambda:cmds.undoInfo(closeChunk=True))
    
    def MyInitValue(self):
        self.HV = cmds.getAttr(self.H)
        self.LV = cmds.getAttr(self.L)
        self.RV = cmds.getAttr(self.R)
                
    def MySetValue(self,value):
        value_H = float(value)/5 +self.HV
        value_S = value_H * 15/25
        
        try:
            cmds.setAttr (self.H,value_H)
            cmds.setAttr (self.L,value_S)
            cmds.setAttr (self.R,value_S)
        except:
            pass
            

        

    def MySetDoubleSpinBox_h(self):
        value = self.win.doubleSpinBox_h.value()*100
        self.win.slider_h.setValue(value)




if __name__ == "__main__":

    app = QApplication(sys.argv)
    pgw = Header_Shoulder_Ctrl()
    pgw.show()   
    app.exec_()    
    

    
