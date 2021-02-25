#-*- coding: utf-8 -*-
import maya.cmds as rig
import pickle


#def SK_ImportExportUI():
#    IDMTRigGUI='ImportExportCurves'
#    if rig.window(IDMTRigGUI,exists=True):
#        rig.deleteUI(IDMTRigGUI)
#    rig.window(IDMTRigGUI,title= u'导入导出控制器形状',menuBar=True,wh=  (300,80),minimizeButton=True,maximizeButton=True)
#    rig.columnLayout()
#    rig.button(l = u'导入',w = 295,c = 'SK_importCurveShape()')
#    rig.button(l = u'导出',w = 295,c = 'SK_exportCurveShape()')
#    rig.window(IDMTRigGUI,e=True,wh=(300,80))
#    rig.showWindow(IDMTRigGUI) 
    
    
class SK_ImportExportUI(object):
    def __init__(self):
        self.guiName = 'EXport_bodyControlShape'
        self.guiTitle = u'导出身体控制器形状'
        self.guiImport = u'导入'
        self.guiExport = u'导出'
        
        self.relativesSet = True
        self.allCons = []
        self.shapeSign = True
        
        self.conSpace = True
        
        
    def displayUI(self):
        IDMTRigGUI = self.guiName
        if rig.window(IDMTRigGUI,exists=True):
            rig.deleteUI(IDMTRigGUI)
            
        self.mainUI = rig.window(IDMTRigGUI,title= self.guiTitle,menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = rig.formLayout()
        self.mainSRL = rig.scrollLayout(cr = True)
        self.mainCLM = rig.columnLayout(adj = True)
        
        self.mainBT = rig.button(l = self.guiImport, c = lambda x:self.SK_importCurveShape())
        
        rig.separator(st = 'out')
        self.mainBT = rig.button(l = self.guiExport, c = lambda x:self.SK_exportCurveShape())
        
        rig.separator(st = 'out')
        
        rig.setParent(self.mainFLY)
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'top', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'left', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'bottom', 2))
        rig.formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'right', 2))
        rig.showWindow(IDMTRigGUI)  
        rig.window(self.mainUI,e=True,wh=(325,200))
       


    def SK_importCurveShape(self):
        filePath=rig.fileDialog(dm='*.cs',m=0)
        if filePath:
            readFile = open(filePath,'r')
            ShapeData = pickle.load(readFile)
            readFile.close()
            self.SK_setCurveShape(ShapeData)
    
    
    def SK_exportCurveShape(self):
        filePath=rig.fileDialog(dm='*.cs',m=1)
        if filePath:
            if 'cs' != filePath.split('.')[-1]:
                filePath += '.cs'
            ShapeData = self.SK_getCurveShape()
            newFile = open(filePath,'w')
            pickle.dump(ShapeData,newFile)
            newFile.close()
            
    def writeControllers(self, attrName):
        pass
        
    def readControllers(self, attrName):
        pass
        
                
    def SK_getCurveShape(self):
        if self.relativesSet:
            cons = rig.sets('bodySet',q = True)
        else:
            cons = self.allCons
            
        if self.shapeSign:#得到shape信息
            ShapeData = []
            for con in cons:
                conShapes = rig.listRelatives(con, s = True, ni = False)
                for conShape in conShapes:
                    Data = [conShape,[rig.xform(vtx,q = True,t = True,wd = self.conSpace, ws = not self.conSpace) for vtx in rig.ls(conShape+'.cv[*]',fl = True)]]
                    ShapeData.append(Data)
#            ShapeData = [[con,[rig.xform(vtx,q = True,t = True,wd = self.conSpace, ws = not self.conSpace) for vtx in rig.ls(con+'.cv[*]',fl = True)]]for con in cons]
        
        else:#得到transform信息
            ShapeData = [[con,rig.getAttr(con+'.matrix'), [rig.getAttr(con+'.sx'),rig.getAttr(con+'.sy'),rig.getAttr(con+'.sz')], rig.xform(con, q = True, ro = True, wd = True, r = True),self.getUserAttr(con)]for con in cons]

        return ShapeData
    
    
    def SK_setCurveShape(self,shapeData = []):
        if shapeData:
            for con in shapeData:
                conName = con[0]
#                print conName
                if rig.objExists(conName):
                    vtxDatas = con[1]
                    if self.shapeSign:#设置shape信息
                        for i,pos in enumerate(vtxDatas):
                            rig.xform(conName+'.cv['+str(i)+']',t = pos,wd = self.conSpace, ws = not self.conSpace)
                    else:#设置transform信息
#                        if 'joint' == rig.nodeType(conName):
#                            rig.joint(conName, e = True, p = con[1], co = True)
#                        else:
#                            rig.xform(conName,t = con[1], p = True, wd = self.conSpace, ws = not self.conSpace)
                        rig.xform(conName, m = con[1], p = False)
                        rig.setAttr(conName+'.sx',con[2][0])
                        rig.setAttr(conName+'.sy',con[2][1])                        
                        rig.setAttr(conName+'.sz',con[2][2])   
                        rig.setAttr(conName+'.rx',con[3][0])
                        rig.setAttr(conName+'.ry',con[3][1])                        
                        rig.setAttr(conName+'.rz',con[3][2])                       
        
                        if con[4]:#恢复旋转属性
                            self.setUserAttr(conName, con[4])
        
    def getUserAttr(self,con):
        udAttr = rig.listAttr(con, k = True, ud = True)
        if udAttr:
            udData = [[att,rig.getAttr(con+'.'+att)] for att in udAttr]
        else:
            udData = []
            
        return udData
    
        
    def setUserAttr(self,con, conData):
        for att in conData:
            if rig.attributeQuery(att[0], node = con, ex = True):
                rig.setAttr(con+'.'+att[0], att[1])

        