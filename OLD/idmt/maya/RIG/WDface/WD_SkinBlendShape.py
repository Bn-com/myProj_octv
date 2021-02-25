#-*- coding: utf-8 -*-
import maya.cmds as rig
import maya.OpenMaya as mo
import RIG.WDface.WD_MainClass as CA



class SkinBlendShape():
    def __init__(self,skinObj,newObj):
        self.skinObj = skinObj#蒙皮物体
        self.newObj = newObj#完成后的物体形状
        
        self.cv = '.cv['
        self.copy = False
    def computeNewPosition(self):
        TempCA = CA.getDeformerNode()
        skin = TempCA.getInfo(self.skinObj)#得到skinCluster节点
        
        allVtxs = rig.ls(self.skinObj+self.cv+'*]',fl = True)
      
        newPos = []
        for i,vtx in enumerate(allVtxs):
            skinPos = rig.xform(vtx,q = True, t = True, ws = True)
            modiflyPos =  rig.xform(vtx.replace(self.skinObj,self.newObj),q = True, t = True, ws = True)
        
            weightList = rig.skinPercent(skin, vtx, q = True, v = True)
            
            thisMatrix = mo.MMatrix()
            nullMatrix = mo.MMatrix()
            mo.MScriptUtil().createMatrixFromList([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], nullMatrix)
            thisMatrix = nullMatrix
            for i in range(len(weightList)):
        
                index = str(i)
                bindPreMatrix = rig.getAttr(skin + ".bindPreMatrix[" + index + "]")
                drivingMatrix = rig.getAttr(skin + ".matrix[" + index + "]")
                
                bindPreMMatrix = mo.MMatrix()
                drivingMMatrix = mo.MMatrix()
                
                mo.MScriptUtil().createMatrixFromList(bindPreMatrix, bindPreMMatrix)
                mo.MScriptUtil().createMatrixFromList(drivingMatrix, drivingMMatrix)
            
                currentMatrix = bindPreMMatrix * drivingMMatrix * weightList[i]
                
                thisMatrix += currentMatrix
            
            thisMatrixInverse = thisMatrix.inverse()
            PT = mo.MPoint(modiflyPos[0], modiflyPos[1], modiflyPos[2])
            P = PT * thisMatrixInverse
            
            NP = [P[0], P[1], P[2]]
            newPos.append(NP)
    
        if self.copy:
            copyObj = rig.duplicate(self.newObj,n = self.newObj+'_MD')[0]
            for i,pos in enumerate(newPos):
                rig.xform(copyObj+self.cv+str(i)+']', t = pos, ws = True)
        else:
     
            for i,pos in enumerate(newPos):
                rig.xform(self.newObj+self.cv+str(i)+']', t = pos, ws = True)
