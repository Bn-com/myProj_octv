#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler

class ConnectShapes():
    def __init__(self):
        pass
    
    def startConnectShape(self):
#        print self.checkBoxDict
#        print self.textFieldDict
#        print self.relativeDict
        
        if self.checkBoxDict['mainCB']:
            skinObj = self.textFieldDict['SkinBT']
            skinNewObj = skinObj[2:-1]
            skinObjs =  skinNewObj.split("', u'")
    
            bsObj = self.textFieldDict['BlendShapeBT']
            bsNewObj = bsObj[2:-1]
            bsObjs =  bsNewObj.split("', u'")  
           
           
            if skinObjs and bsObjs:
                for obj in skinObjs:
                    if obj+'_BS' in bsObjs:
                        objShape = rig.listRelatives(obj, s = True, ni = True)[0]
                        BsShapeOrigen = rig.listRelatives(obj+'_BS', s = True, ni = False)[1]
                        
                        rig.connectAttr(objShape+'.outMesh', BsShapeOrigen+'.inMesh')

                    if obj+'BS' in bsObjs:
                        objShape = rig.listRelatives(obj, s = True, ni = True)[0]
                        BsShapeOrigen = rig.listRelatives(obj+'BS', s = True, ni = False)[1]
                        
                        rig.connectAttr(objShape+'.outMesh', BsShapeOrigen+'.inMesh')

            
    def done(self, checkBoxDict,textFieldDict,relativeDict):
        self.checkBoxDict = checkBoxDict
        self.textFieldDict = textFieldDict
        self.relativeDict = relativeDict
        
        self.startConnectShape()
    