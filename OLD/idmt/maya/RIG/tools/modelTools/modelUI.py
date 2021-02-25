#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.simulation.simulationMain import *

class SK_modelUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='modelUI'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title= u'模型工具',menuBar=True,wh=  (325,500),minimizeButton=True,maximizeButton=True)
        self.mainCLT = rig.columnLayout()
        
        
#        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,100),(2,150),(3,73)],columnAttach = (3,'both',0))
#        rig.text(u'载入Ploygon物体:')
#        self.ploygonTF = rig.textField(tx = u'')
#        rig.button(l = u'>>',w = 30,c = lambda x:self.loadSeleteObj())
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        rig.rowColumnLayout(numberOfColumns=4,columnWidth = [(1,100),(2,35),(3,10),(4,35)],columnAttach = (4,'left',0))
#        rig.text(u'输入控制器数量:')
#        self.columnIF = rig.intField(v = 2)
#        rig.text('X')
#        self.rowIF = rig.intField(v = 2)
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,100),(2,150)],columnAttach = (2,'both',0))
#        rig.text(u'输入控制器名字:')
#        self.inputName = rig.textField(tx = u'Pre_3_M')
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        self.inputSizeFSG = rig.floatSliderGrp(field=True, label=u'控制器大小:',minValue=0, maxValue=5, fieldMinValue=0, fieldMaxValue=10000, value=5,columnAttach=[(1,'left',20),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150))
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        self.inputShapeOM = rig.optionMenuGrp( label= u'选择控制器形状: ',columnWidth=[(1,100),(2, 100)] )
#        rig.menuItem( label= u'球形' )
#        rig.menuItem( label= u'正方形' )
#        rig.menuItem( label= u'长圆形')
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        self.inputColorOM = rig.optionMenuGrp( label= u'选择控制器颜色: ',columnWidth=[(1,100),(2, 100)] )
#        rig.menuItem( label= u'红色' )
#        rig.menuItem( label= u'黄色' )
#        rig.menuItem( label= u'蓝色')
#        rig.setParent(self.mainCLT)
#        rig.separator(w = 312,h=15,style='in')
#        
#        rig.button(l = u'导入定位点',w = 325,c = lambda x:self.importLocatorPoint())
#        rig.separator(w = 312,h=15,style='in')
#        
#        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,125),(2,125),(3,73)],columnAttach = (1,'left',0))
#        rig.text(u'载入增加属性的控制器:')
#        self.MasterTF = rig.textField(tx = u'')
#        rig.button(l = u'>>',w = 30,c = lambda x:self.loadMasterObj())
#        rig.setParent(self.mainCLT)
#        rig.button(l = u'自动生成布料设置',w = 325,c = lambda x:self.autoClothSetup())
        
        rig.button(l = u'镜像眉毛',w = 320,c = lambda x:self.mirrorEyebrow())
        rig.separator(w = 312,h=15,style='in')
        rig.button(l = u'分离BlendShape',w = 320,c = lambda x:self.separateBlendShape())
                
        rig.window(IDMTRigGUI,e=True,wh=(325,500))
        rig.showWindow(IDMTRigGUI)   
        
    def mirrorEyebrow(self):
        from RIG.tools.modelTools.MirrorEyebrowUI import *;SK_MrrorEyebrowUI()
        SK_MrrorEyebrowUI()
        
    def separateBlendShape(self):
        from RIG.tools.modelTools.separateBlendShapeUI import *
        separateBlendShapeUI()
    
        
        

    