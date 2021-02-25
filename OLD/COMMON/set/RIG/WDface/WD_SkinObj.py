#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler
import re

class skinToObjs():
    def __init__(self):
        self.bts = {'SkinBT':'Face_Main_Sets','BlendShapeBT':'Face_BsMesh_Sets','LfEyeBT':'Face_LfEye_Sets','RtEyeBT':'Face_RtEye_Sets','LfToothBT':'Face_DnTeeth_Sets','RtToothBT':'Face_UpTeeth_Sets','LfEyebrowBT':'','RtEyebrowBT':'','TongueBT':'Face_Tongue_Sets'}
 
    def startSkin(self):
        print self.checkBoxDict
        print self.textFieldDict
        print self.relativeDict
        
        for CB in self.checkBoxDict:
            if self.checkBoxDict[CB]:
                bts = self.relativeDict[CB]
                if 0 == len(bts):
                    pass
                
                if 1 == len(bts):
                    obj = self.textFieldDict[bts[0]]
                    newObj = obj[2:-1]
                    objs =  newObj.split("', u'")
                    
                    if self.bts[bts[0]] and objs[0] != '':
                        infs = rig.sets(self.bts[bts[0]], q = True)
                        CA.skinClusterObj().skinClusters(infs, objs)
                
                if 1 < len(bts):
                    for bt in bts:
                        obj = self.textFieldDict[bt]
                        newObj = obj[2:-1]
                        objs =  newObj.split("', u'")
                        
                        if self.bts[bt] and objs[0] != '':
                            infs = rig.sets(self.bts[bt], q = True)
                            CA.skinClusterObj().skinClusters(infs, objs)
                        
                        
            
    def done(self, checkBoxDict,textFieldDict,relativeDict):
        self.checkBoxDict = checkBoxDict
        self.textFieldDict = textFieldDict
        self.relativeDict = relativeDict
        self.startSkin()
    