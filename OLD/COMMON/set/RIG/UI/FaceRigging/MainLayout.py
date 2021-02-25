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
        
        rig.button(l= u'蒙皮-面部设置窗口',c='from RIG.face.faceUI import *\nOpenFaceUI()',w = 325)
    
        rig.separator(w = 325,h=5,style='in')
        rig.button(l= u'蒙皮-面部设置窗口（新）',c='import RIG.WDface.WD_FaceUI as face;face.WD_SelectUI()',w = 325)

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
        
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'目标体-面部设置窗口（LOW）',c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_facial_rig_ui(\'LOW\')',w = 322,h=40,bgc = (0.6,0.7,0.8))     
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'目标体-面部设置窗口（NORM）',c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_facial_rig_ui(\'NORM\')',w = 322,h=40,bgc = (0.6,0.8,0.7))                                
        rig.separator(w = 322,h=15,style='in')
        rig.button(l= u'目标体-面部设置窗口（HIGH）',c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().CJW_facial_rig_ui(\'HIGH\')',w = 322,h=40,bgc = (0.7,0.8,0.6))                                

        rig.separator(w = 322,h=15,style='in')       
        rig.rowColumnLayout(numberOfColumns=2,columnWidth = [(1,162),(2,162)])
        rig.button(l= u'导入动画选择面板文件',c='from RIG.face_BS import CJW_Facial_Rig_tool\nreload(CJW_Facial_Rig_tool)\nCJW_Facial_Rig_tool.CJW_Facial_AutoRig_Tool().High_importFacialSelectPannel()',w = 100,h=40,bgc = (0.8,0.7,0.6))                                
        rig.button(l= u'动画选择插件',c='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_H_Facial_Animation_Action_Tool()',w = 100,h=40,bgc = (0.8,0.7,0.6))                                
        rig.button(l= u'添加表情Set组',c='from RIG.commonly.sets import CJW_createFacialCtrlSets\nCJW_createFacialCtrlSets()',w = 100,h=40,bgc = (0.8,0.7,0.6))                                
        rig.button(l= u'添加身体Set组',c='from RIG.commonly.sets import CJW_createCtrlSets\nCJW_createCtrlSets()',w = 100,h=40,bgc = (0.8,0.7,0.6))                                
        rig.button(l= u'选中控制器\n连接MODEL组内模型属性',c='from RIG.tools.connectAttrTool import CJW_connectAttrTool\nCJW_connectAttrTool()',w = 100,h=40,bgc = (0.8,0.7,0.6))  
        rig.button(l= u'保存面板材质信息',c='from RIG.face_BS import CJW_facial_rig_H_py_v1\nreload(CJW_facial_rig_H_py_v1)\nCJW_facial_rig_H_py_v1.CJW_facial_rig_H_py_v1_Class().CJW_characterTextureWire()',w = 100,h=40,bgc = (0.6,0.7,0.8))             
        rig.setParent(self.returnLayout)
        return self.returnLayout