#-*- coding: utf-8 -*-
from maya.cmds import *
import RIG.tools.ImportExportHairCache.hairCache as HC
import maya.mel as MEL

class SK_HairCacheUI(object):
    def __init__(self):
        self.displayUI()
        
    def displayUI(self):
        IDMTRigGUI='SK_AutoAddSetUI'
        if window(IDMTRigGUI,exists=True):
            deleteUI(IDMTRigGUI)
        self.CurveSign = 'OFF'
        self.mainUI = window(IDMTRigGUI,title= u'导入导出头发Cache工具',menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = formLayout()
        self.mainSRL = scrollLayout(cr = True)
        self.mainCLM = columnLayout(adj = True)
        
        self.mainBT = button(l = u'导出Cache',c = lambda x:self.exportCache())
        
        separator(st = 'out')
        self.mainBT = button(l = u'导入cache',c = lambda x:self.importCache())
        
        setParent(self.mainFLY)
        formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'top', 2))
        formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'left', 2))
        formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'bottom', 2))
        formLayout(self.mainFLY,e=True, attachForm=(self.mainSRL,'right', 2))
        showWindow(IDMTRigGUI)  
        window(self.mainUI,e=True,wh=(325,200))
        
    def exportCache(self):
        MeshObj = ls(sl = True)[0]
        if MeshObj:
            MeshShape = listRelatives(MeshObj, s = True)
            TempHair = HC.GenraterCurve('mesh', MeshShape)
            TempHair.createCurve()
            MEL.eval('doCreateGeometryCache 5 { "2", "1", "10", "OneFile", "1", "","0","","0", "add", "0", "1", "1","0","1","mcc" }')
            TempHair.deleteCurve()