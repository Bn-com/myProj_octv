#-*- coding: utf-8 -*-
from maya.cmds import *


class GenraterCurve():
    def __init__(self,inputType, slObjs):
        self.type = inputType#现在的类型
        self.selectObjs = slObjs
        self.allFollicles = []#所有毛囊
        self.allCurveFolSystem = []#所有曲线、毛囊和毛发系统信息
        
        
    def getAllFollicls(self):
        if self.selectObjs:
            for obj in self.selectObjs:
                self.getSingleFollicle(obj)
        else:
            return None
        
        
    def getSingleFollicle(self, obj):
        if 'mesh' == self.type:
            folSign = listConnections(obj, s = False, d = True, sh = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'follicle' == self.type:
            self.allFollicles.extend(obj)
                
        elif 'pfxHair' == self.type:
            folSign = listConnections(obj, d = False, s = True, type = 'hairSystem')
            if folSign:
                for hs in folSign:
                    fols = listConnections(hs, d = Fasle, s = True, type = 'follicle')
                    if fols:
                        self.allFollicles.extend(fols)
                
        elif 'nurbsCurve' == self.type:
            folSign = listConnections(obj, s = False, d = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'hairSystem' == self.type:
            folSign = listConnections(obj, s = True, d = False, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'nurbsSurface' == self.type:
            folSign = listConnections(obj, s = False, d = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
                
                
    def getInfo(self):
        self.getAllFollicls()
        fols = self.allFollicles
        if fols:
            allFols = set(fols)
            for fol in allFols:
                inputCurve = listConnections(fol, s = True, d = False, type = 'nurbsCurve')
                HS = listConnections(fol, s = False, d = True, type = 'hairSystem')
                if inputCurve and HS:
                    startCurve = inputCurve[0]
                    startCurveShape = listRelatives(startCurve, s = True)[0]
                    HSName = HS[0]
                    HSShape = listRelatives(HSName, s = True)[0]
                    self.allCurveFolSystem.append([startCurve,startCurveShape,fol,HSName,HSShape])
       
    def createCurve(self):
        self.getInfo()
        if self.allCurveFolSystem:
            
            print self.allCurveFolSystem
#            jnt = joint(n = 'hair_Temp_JNT')
            for iterInfo in self.allCurveFolSystem:
                rename(iterInfo[0],iterInfo[0]+'_Cache')
                outputCurveShape = createNode('nurbsCurve', n = iterInfo[1])
                print outputCurveShape+'---------outputCurveShape'
                outputCurve = listRelatives(outputCurveShape, p = True)[0]
                print outputCurve+'---------outputCurve'
                rename(outputCurve, iterInfo[0])
                
                inputCurve = listConnections(iterInfo[2]+'.outHair', d = True, s = False, p = True)[0]
                outputCurve = inputCurve.replace('.inputHair', '.outputHair')
                connectAttr(outputCurve, iterInfo[2]+'.currentPosition')
                
                connectAttr(iterInfo[2]+'.outCurve', outputCurveShape+'.create')
                skinCluster(jnt, outputCurveShape)    
            
            select([cur[0] for cur in self.allCurveFolSystem])
    
    def deleteCurve(self):
        if self.allCurveFolSystem:
            
            delete([cur[0] for cur in self.allCurveFolSystem])
            for iterInfo in self.allCurveFolSystem:
                print iterInfo
                defaultCurve = rename(iterInfo[0]+'_Cache',iterInfo[0])
                defaultCurveShape = listRelatives(defaultCurve, s = True)[0]
                rename(defaultCurveShape,iterInfo[1])
