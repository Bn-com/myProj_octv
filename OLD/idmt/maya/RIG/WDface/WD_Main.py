#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_Teeth as WDTeeth
import RIG.WDface.WD_Eyes as WDEyes
import RIG.WDface.WD_Tongue as WDTongue
import RIG.WDface.WD_MainControl as WDMain
import RIG.WDface.WD_Joint as WDJoint
import RIG.WDface.WD_Eyebrow as WDEyebrow
import RIG.WDface.WD_Ear as WDEar
import RIG.WDface.WD_MainClass as CA
import RIG.WDface.WD_MainToHead as MTH
import RIG.WDface.WD_SkinObj as SO
import RIG.WDface.WD_ConnectVisiblity as CV
import RIG.WDface.WD_TeethToHead as ToTeeth
import RIG.WDface.WD_TongueToHead as ToTongue
import RIG.WDface.WD_EyeToHead as ToEye
import RIG.WDface.WD_SeparateTemplate as ST
import RIG.WDface.WD_ConnectShape as CS
import RIG.WDface.WD_CreateControlSets as CCS
import RIG.WDface.WD_LockTransform as LT

class combineComponent():
    def __init__(self,checkBoxDict,textFieldDict,relativeDict):
        self.checkBoxDict = checkBoxDict
        self.textFieldDict = textFieldDict
        self.relativeDict = relativeDict

        
    def startSetup(self):
        for com in self.checkBoxDict:
            if self.checkBoxDict[com]:
                getTextField = []
                currentCom = self.selectMatch(com)
                getBT = self.relativeDict[com]
                if getBT:
                    for BT in getBT:
                        getTextField.append(self.textFieldDict[BT])
                    currentCom.model = getTextField
                currentCom.done()
    
    def selectMatch(self,com):
        if 'eyebrowCB' == com:
            return WDEyebrow.RigStart()
        elif 'eyeCB' == com:
            return WDEyes.RigStart()
        elif 'earCB' == com:
            return WDEar.RigStart()
        elif 'tongueCB' == com:
            return WDTongue.RigStart()
        elif 'toothCB' == com:
            return WDTeeth.RigStart()
        elif 'jointCB' == com:
            return WDJoint.RigStart()
        elif 'mainCB' == com:
            return WDMain.RigStart()   
        
         
    def startMainToHead(self):
        if rig.objExists('Head_Control_GRP') and rig.objExists('Main_Control_GRP'):
            Mth = MTH.mainToHead()
            Mth.head = 'Head_Control_GRP'
            Mth.main = 'Main_Control_GRP'
            Mth.done()
        
    def startTeethToHead(self):
        if rig.objExists('Head_Control_GRP') and rig.objExists('Tooth_Control_GRP'):
            Temp = ToTeeth.teethToHead()
            Temp.done()
        
    def startTongueToHead(self):
        if rig.objExists('Head_Control_GRP') and rig.objExists('Tongue_Control_GRP'):
            Temp = ToTongue.tongueToHead()
            Temp.done()   
    
        
    def startEyeToHead(self):
        if rig.objExists('Head_Control_GRP') and rig.objExists('Eye_Control_GRP'):
            Temp = ToEye.eyeToHead()
            Temp.done()   
    
    def addExtraJoint(self):
        if rig.objExists('Face_BsMesh_Sets'):
            rig.sets('Head_Zero_Joint', e = True, addElement = 'Face_BsMesh_Sets')
               
    def done(self):
        ST.separateTemplate().upParentGrp()#将主要组P到外面
        self.startSetup()
        self.startMainToHead()
        self.startTeethToHead()
        self.startTongueToHead()
        self.startEyeToHead()
        self.addExtraJoint()
        CV.ConnectVis().done()
        SO.skinToObjs().done(self.checkBoxDict,self.textFieldDict,self.relativeDict)
        CS.ConnectShapes().done(self.checkBoxDict,self.textFieldDict,self.relativeDict)
        CCS.createConSets().done()
        LT.LockTransform().done()
 
  
    