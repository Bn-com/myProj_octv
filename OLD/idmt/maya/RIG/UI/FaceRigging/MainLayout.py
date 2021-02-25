#-*- coding: utf-8 -*-
import maya.cmds as rig

class FaceRigging():
    def __init__(self, parentLayout):
        self.parent = parentLayout
        self.returnLayout = ''
        self.createLayout()

    
    def createLayout(self):
        rig.setParent(self.parent)
        self.runLayout()
        rig.setParent(self.parent)
    
    def getLayout(self):
        return self.returnLayout      
    
    def runLayout(self):
        self.returnLayout = rig.columnLayout(w =300,h=355)
        
        rig.button(l= u'打开面部设置窗口',c='from RIG.face.faceUI import *\nOpenFaceUI()',w = 325)
    
        rig.separator(w = 325,h=5,style='in')
        rig.button(l= u'打开最新面部设置窗口',c='import RIG.WDface.WD_FaceUI as face;face.WD_SelectUI()',w = 325)

        rig.separator(w = 325,h=5,style='in')
        rig.text(u' 增加下颚设置')
        rig.rowColumnLayout(numberOfColumns=2,columnWidth = [(1,162),(2,162)])
        rig.button(label = u' 确定 ' ,c = 'from RIG.tools.AddJawSetup import *\nSK_AddJawSetup()')
        rig.button(l= u'移除设置',c = 'from RIG.tools.AddJawSetup import *\nSK_removeJawSetup()')
        rig.setParent('..')
            
        rig.separator(w = 325,h=5,style='in')
        rig.text(u' 增加眼睛设置')    
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,108),(2,108),(3,108)],columnAttach = (3,'both',0))
        rig.button(l= u'导入控制器',c= 'from RIG.tools.AddEyeSetup import SK_AddEyeSetup\nSK_AddEyeSetup(True)')
        rig.button(l= u'完成设置',c= 'from RIG.tools.AddEyeSetup import SK_AddEyeSetup\nSK_AddEyeSetup(False)')
        rig.button(l= u'移除设置',c= 'from RIG.tools.AddEyeSetup import SK_removeEyeSetup\nSK_removeEyeSetup()')
        
        rig.setParent(self.returnLayout)
        return self.returnLayout