#-*- coding: utf-8 -*-
#file: VFX_CheckIn.py
__author__ = 'l'

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sip,os,sys
from PyQt4.uic import loadUi
import maya.OpenMayaUI as apiUI
import maya.cmds as mc
import maya.mel as mel

def getMayaWindow():
    ptr = apiUI.MQtUtil.mainWindow()
    return sip.wrapinstance(long(ptr), QObject)

class XXX(QMainWindow):
    def __init__(self,parent=getMayaWindow()):
        super(XXX, self).__init__(parent)
        self.ui = loadUi(r'\\file-cluster\GDC\Resource\Support\Python\2.7-x64\Lib\site-packages\idmt\maya\Lion\UI\Lion_renderLayer.myuis')
        self.setCentralWidget(self.ui)
        self.resize(self.ui.frameSize())

        self.aIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.7-x64\Lib\site-packages\idmt\maya\Lion\UI\icon\abc.gif")
        self.bIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.7-x64\Lib\site-packages\idmt\maya\Lion\UI\icon\bcd.gif")

                
        #self.myuis.pic_button.setIconSize (self.myuis.pic_button.frameSize())


        self.ui.pic_button.setIcon(self.bIcon)
        self.ui.pic_button.setIcon(self.aIcon)   
        

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.changeIcon)
        self.timer.start(7000)
        self.currentColor = "1"

        self.ui.creatproject.clicked.connect(self.pro )
        self.ui.deleteLayer.clicked.connect(self.dellayer )
        
        self.ui.CHR_CO.clicked.connect(self.CHR_COLOR )
        self.ui.BG_CO.clicked.connect(self.BG_COLOR )
        self.ui.CHR_IDP.clicked.connect(self.CHR_RGB )
        self.ui.BG_IDP.clicked.connect(self.BG_RGB )
                                        
        self.ui.pic_button.clicked.connect(self.music )
        
    def changeIcon(self):
        if self.currentColor == "1":
            self.ui.pic_button.setIcon(self.aIcon)
            self.currentColor = "2"
        elif self.currentColor == "2":
            self.ui.pic_button.setIcon(self.bIcon)
            self.currentColor = "1" 

             
                                              
    def closeEvent(self,QCloseEvent):
        self.timer.stop()
        
    def pro(self):
        mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/Strawberry4/sk4_SetProject.mel"')
        mel.eval("skSetProject")
        
    def dellayer(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldALLDelete(nodetype="renderLayer")
        
    def CHR_COLOR(self):
        from idmt.maya.Lion import Lion_renderLayer
        reload(Lion_renderLayer)
        Lion_renderLayer.Lion_renderLayer().Lion_CHRcolorCreate()
        
    def BG_COLOR(self):
        from idmt.maya.Lion import Lion_renderLayer
        reload(Lion_renderLayer)
        Lion_renderLayer.Lion_renderLayer().Lion_SETcolorCreate()             

    def CHR_RGB(self):
        from idmt.maya.Lion import Lion_renderLayer
        reload(Lion_renderLayer)
        Lion_renderLayer.Lion_renderLayer().Lion_CHRidpCreate()

    def BG_RGB(self):
        from idmt.maya.Lion import Lion_renderLayer
        reload(Lion_renderLayer)
        Lion_renderLayer.Lion_renderLayer().Lion_SETidpCreate()

         
    def music(self):
        from idmt.maya.norch import north_music
        reload(north_music)
        north_music.soundStart()          


                
def main():
    PlutoGW = XXX()
    PlutoGW.show()

