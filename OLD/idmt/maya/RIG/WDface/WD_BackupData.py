#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import RIG.tools.importExputCurveShape as InportExport

class backupData():
    def __init__(self,checkBoxDict,textFieldDict,relativeDict, parameter):
        self.checkBoxDict = checkBoxDict
        self.textFieldDict = textFieldDict
        self.relativeDict = relativeDict
        self.parameter = parameter
        
        self.grp = CA.getRigGrp().createGrp()
    
    def startBackupData(self):
        CA.convertData().setAttrData(self.grp+'.parameter', self.parameter)        
        CA.convertData().setAttrData(self.grp+'.checkBoxDict', self.checkBoxDict)
        CA.convertData().setAttrData(self.grp+'.textFieldDict', self.textFieldDict)
        CA.convertData().setAttrData(self.grp+'.relativeDict', self.relativeDict)
        CA.convertData().setAttrData(self.grp+'.templateInfo', self.getTemplateInfo())   
   
    def getTemplateInfo(self):#获得模版信息   
        AllTrans = []
        if rig.objExists('Head_FaceRig_Control_GRP'):
            AllTransforms = rig.listRelatives('Head_FaceRig_Control_GRP', c = True, ad = True)
            AllTrans = rig.ls(AllTransforms, type = 'transform')
            AllTrans.extend(AllTrans)
                
        TempIE = InportExport.SK_ImportExportUI()
        TempIE.guiName = 'IETemplateInfo_UI'
        TempIE.allCons = AllTrans
        TempIE.relativesSet = False
        TempIE.shapeSign = False
        TempIE.conSpace = False
        return TempIE.SK_getCurveShape()  
            
    def done(self):
        self.startBackupData()
    