#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.simulation.simulationMain import *

class SK_simulationUI (object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='simulation'
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
        rig.window(IDMTRigGUI,title= u'simulation',menuBar=True,wh=  (320,500),minimizeButton=True,maximizeButton=True)
        self.mainCLT = rig.columnLayout()
        
        
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,100),(2,150),(3,73)],columnAttach = (3,'both',0))
        rig.text(u'载入Ploygon物体:')
        self.ploygonTF = rig.textField(tx = u'')
        rig.button(l = u'>>',w = 30,c = lambda x:self.loadSeleteObj())
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns=5,columnWidth = [(1,100),(2,35),(3,10),(4,35),(5,50)],columnAttach = (5,'left',0))
        rig.text(u'输入控制器数量:')
        self.columnIF = rig.intField(min = 1,max = 1000,v = 2,cc = lambda x:self.computeCount())
        rig.text(l = 'X')
        self.rowIF = rig.intField(min = 1,max = 1000,v = 2,cc = lambda x:self.computeCount())
        self.countTX = rig.text(l = '  4',fn = "boldLabelFont")
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,100),(2,150)],columnAttach = (2,'both',0))
        rig.text(u'输入控制器名字:')
        self.inputName = rig.textField(tx = u'Pre_3_M')
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        self.inputSizeFSG = rig.floatSliderGrp(field=True, label=u'控制器大小:',minValue=0.0001, maxValue=2, fieldMinValue=0.0001, fieldMaxValue=10000, value=1,columnAttach=[(1,'left',20),(2,'left',0),(3,'both',0)],columnWidth3 = (100,30,150))
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        self.inputShapeOM = rig.optionMenuGrp( label= u'选择控制器形状: ',columnWidth=[(1,100),(2, 100)] )
        rig.menuItem( label= u'球形' )
        rig.menuItem( label= u'正方形' )
        rig.menuItem( label= u'长圆形')
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        self.inputColorOM = rig.optionMenuGrp( label= u'选择控制器颜色: ',columnWidth=[(1,100),(2, 100)] )
        rig.menuItem( label= u'红色' )
        rig.menuItem( label= u'黄色' )
        rig.menuItem( label= u'蓝色')
        rig.setParent(self.mainCLT)
        rig.separator(w = 312,h=15,style='in')
        
        rig.button(l = u'导入定位点',w = 325,c = lambda x:self.importLocatorPoint())
        rig.separator(w = 312,h=15,style='in')
        
        rig.rowColumnLayout(numberOfColumns=3,columnWidth = [(1,125),(2,125),(3,73)],columnAttach = (1,'left',0))
        rig.text(u'载入增加属性的控制器:')
        self.MasterTF = rig.textField(tx = u'Master')
        rig.button(l = u'>>',w = 30,c = lambda x:self.loadMasterObj())
        rig.setParent(self.mainCLT)
        rig.button(l = u'自动生成布料设置',w = 325,c = lambda x:self.autoClothSetup())
        
        rig.button(l = u'生成设置',w = 325,c = lambda x:self.setup())
        rig.window(IDMTRigGUI,e=True,wh=(325,500))
        rig.showWindow(IDMTRigGUI)   
        
    def loadSeleteObj(self):
        obj =rig.ls(sl = True)
        if obj:
            rig.textField(self.ploygonTF,e = True,tx = obj[0])
        
    def loadMasterObj(self):#载入master物体
        obj =rig.ls(sl = True)
        if obj:
            rig.textField(self.MasterTF,e = True,tx = obj[0])
            
    def importLocatorPoint(self):
        ployName = rig.textField(self.ploygonTF,q = True,tx = True)
        col = rig.intField(self.columnIF,q = True,v = True)
        row = rig.intField(self.rowIF,q = True,v = True)
        conPre = rig.textField(self.inputName,q = True,tx = True)
        size = rig.floatSliderGrp(self.inputSizeFSG,q = True,v = True)
        shape = rig.optionMenuGrp(self.inputShapeOM,q = True,sl = True)
        color = rig.optionMenuGrp(self.inputColorOM,q = True,sl = True)
        SM_importControllerTem(ployName,col,row,conPre,size,shape,color)
        
    def setup(self):
        ployName = rig.textField(self.ploygonTF,q = True,tx = True)
        SMSetup = SM_createSetup(ployName)
        rig.delete(SMSetup.origenCurve)
        
        #连接属性
        masterName = rig.textField(self.MasterTF,q = True,tx = True)
        if rig.objExists(masterName+'.SecondCtrl'):
            rig.connectAttr(masterName+'.SecondCtrl', ployName+'_ScaleSM_GRP.vis', f = True)
        else:
            rig.addAttr(masterName, ln = 'SecondCtrl', at = 'enum', en = ':off:on', k = True)
            rig.connectAttr(masterName+'.SecondCtrl', ployName+'_ScaleSM_GRP.vis', f = True)
            
    def autoClothSetup(self):
        ployName = rig.textField(self.ploygonTF,q = True,tx = True)
        masterName = rig.textField(self.MasterTF,q = True,tx = True)
        SM_AutoNclothSetup(ployName,masterName)
    #------------------------------------------------------------------ 计算控制器的数量
    def computeCount(self):
        col = rig.intField(self.columnIF,q = True,v = True)
        row = rig.intField(self.rowIF,q = True,v = True)
        rig.text(self.countTX,e = True,l = str(col*row))