#-*- coding: utf-8 -*-
#file: VFX_CheckIn.py
__author__ = 'zhaozhongjie'

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
        self.ui = loadUi(r'\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\Nor_renderTools.myuis')
        self.setCentralWidget(self.ui)
        self.resize(self.ui.frameSize())

        self.aIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\1.jpg")
        self.bIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\2.jpg")
        self.cIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\3.jpg")
        self.dIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\4.jpg")
        self.eIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\5.jpg")
        self.fIcon = QIcon(r"\\file-cluster\GDC\Resource\Support\Python\2.6-x64\Lib\site-packages\idmt\maya\norch\QT\icon\6.jpg")
                
        self.ui.pic_button.setIconSize (self.ui.pic_button.frameSize())

        self.ui.pic_button.setIcon(self.aIcon)
        self.ui.pic_button.setIcon(self.bIcon)
        self.ui.pic_button.setIcon(self.cIcon)
        self.ui.pic_button.setIcon(self.dIcon)
        self.ui.pic_button.setIcon(self.eIcon)
        self.ui.pic_button.setIcon(self.fIcon)        
        

        self.timer=QTimer(self)
        self.timer.timeout.connect(self.changeIcon)
        self.timer.start(10000)
        self.currentColor = "1"

        self.ui.creatproject.clicked.connect(self.pro )
        self.ui.deleteLayer.clicked.connect(self.dellayer )
        self.ui.hmesh_exr.clicked.connect(self.hmesh )
        self.ui.Amesh_exr.clicked.connect(self.Amesh )
        self.ui.humanIDP.clicked.connect(self.HIDP )
        self.ui.animalIDP.clicked.connect(self.AIDP )
        self.ui.Afur_tif.clicked.connect(self.Afur )
        self.ui.Hfur_tif.clicked.connect(self.Hfur )
        self.ui.save_ligntingfile.clicked.connect(self.ligntingfile )
        self.ui.save_Hfile.clicked.connect(self.Hfile )
        self.ui.save_Afile.clicked.connect(self.Afile )
        self.ui.import_Hlight.clicked.connect(self.Hlight )
        self.ui.import_Alight.clicked.connect(self.Alight )
        self.ui.ALL_IDP.clicked.connect(self.allIDP )
        self.ui.shadow.clicked.connect(self.Shadow )
        self.ui.occ.clicked.connect(self.OCC )        
        self.ui.refrection.clicked.connect(self.Reflection ) 
               
        self.ui.R.clicked.connect(self.rpro )        
        self.ui.G.clicked.connect(self.gpro )
        self.ui.B.clicked.connect(self.bpro )
        self.ui.M.clicked.connect(self.mpro)
        self.ui.Y.clicked.connect(self.ypro )        
        self.ui.C.clicked.connect(self.cpro )        
        self.ui.K.clicked.connect(self.kpro )         
        self.ui.left_eye.clicked.connect(self.eyeleftpro )
        self.ui.right_eye.clicked.connect(self.eyerightpro )        
        
                
        self.ui.pic_button.clicked.connect(self.music )
        
    def changeIcon(self):
        if self.currentColor == "1":
            self.ui.pic_button.setIcon(self.aIcon)
            self.currentColor = "2"
        elif self.currentColor == "2":
            self.ui.pic_button.setIcon(self.bIcon)
            self.currentColor = "3"
        elif self.currentColor == "3":
            self.ui.pic_button.setIcon(self.cIcon)
            self.currentColor = "4"
        elif self.currentColor == "4":
            self.ui.pic_button.setIcon(self.dIcon)
            self.currentColor = "5"
        elif self.currentColor == "5":
            self.ui.pic_button.setIcon(self.eIcon)
            self.currentColor = "6"
        elif self.currentColor == "6":
            self.ui.pic_button.setIcon(self.fIcon)
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
        
    def hmesh(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().NorH_meshCreate()
        
    def Amesh(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().NorA_MeshCreate()                

    def HIDP(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_IDPCreate('CHR')

    def AIDP(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_IDPCreate('AN')        

    def Afur(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().NorA_FurCreate()        

    def Hfur(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().NorH_FurCreate()


    def ligntingfile(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_filelightingSave()        

    def Hfile(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_SeprateFileSave('CHR')

    def Afile(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_SeprateFileSave('AN')
        
    def Hlight(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().norlightingImp('CHR')

    def Alight(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().norlightingImp('AN')        

    def allIDP(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().ALLRGBCreate()
        
    def Shadow(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign('Shadow',0)
        
    def OCC(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign('AO',0)
        
    def Reflection(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldShaderAssign('reflection',0)

    def rpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpR")


    def gpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpG")
        
    def bpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpB")        
        
        
    def mpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpM")        
        
        
    def ypro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpY")        
        
        
    def cpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpC")        



    def kpro(self):
        from idmt.maya.Hh_common import hh_RenderArnoldLayer
        reload(hh_RenderArnoldLayer)
        hh_RenderArnoldLayer.hh_RenderArnold().ArnoldIDCreat(idpShader="ArnoldIdpK")
        
    def music(self):
        from idmt.maya.norch import north_music
        reload(north_music)
        north_music.soundStart()          

    def eyeleftpro(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_eyeshaderchange(0)

    def eyerightpro(self):
        from idmt.maya.norch import north_renderLayer
        reload(north_renderLayer)
        north_renderLayer.north_renderLayer().Nor_eyeshaderchange(1)
                
def main():
    PlutoGW = XXX()
    PlutoGW.show()

