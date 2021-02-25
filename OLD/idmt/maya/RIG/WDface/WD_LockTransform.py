#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import RIG.face.baseClass as BC
import re


class LockTransform():
    def __init__(self):
        self.conSetObj = CA.getSetElements().getEle()
 
    def startLockTransform(self):
        Trans = CA.getAllTransform()
        Trans.removeObj = self.conSetObj
        
        
        Trans.grpName = 'Head_FaceRig_Control_GRP'
        Head_FaceRig_Control_GRP = Trans.getTransform()    
            
        Trans.grpName = 'Head_FaceDeformers_GRP'
        Head_FaceDeformers_GRP = Trans.getTransform()  
        
        Head_FaceRig_Control_GRP.extend(Head_FaceDeformers_GRP)
        allTransforms =  Head_FaceRig_Control_GRP
        
        
        for obj in allTransforms:
            Lock = BC.LockHideAttr(False, False, False, False)
            Lock.hideAndLockObj(obj)
    
    def startLockCons(self):
        cons = self.conSetObj
        
        ScaleCons = []                            
        RotateCons = [u'Dn_Lip_M', u'Up_Lip_M', u'Nose_M']  
        TranslateCons = [con for con in cons if not con in ['jawSwivel_M']]      
         
        for con in cons:
            T = False
            S = False
            R = False
            
            if con in RotateCons:
                R = True
            if con in ScaleCons:
                S = True   
            if con in TranslateCons:
                T = True
            
            Lock = BC.LockHideAttr(T, R, S, False)    
            Lock.hideAndLockObj(con) 
            
                     
            if rig.attributeQuery('sign', node = con, ex = True):
                if 44390 == rig.getAttr(con+'.sign'):#blendShape控制器
                    X = Y = Z = True 
                    RVS = rig.listConnections(con, s = False, d = True, type = 'remapValue')
                    if RVS:
                        
                        if con+'_IN_RV' in RVS or con+'_OUT_RV' in RVS:
                            X = False
                        if con+'_DN_RV' in RVS or con+'_UP_RV' in RVS:
                            Y = False
                        if con+'_BACK_RV' in RVS or con+'_Front_RV' in RVS:
                            Z = False
                            
                        if X:
                            rig.setAttr(con+'.translateX', cb = False, l = True, k = False)
                        if Y:
                            rig.setAttr(con+'.translateY', cb = False, l = True, k = False)
                        if Z:
                            rig.setAttr(con+'.translateZ', cb = False, l = True, k = False)
                    
                    rotateCon = con+'_Rotation'#旋转组
                    if rig.objExists(rotateCon):#如果存在旋转blendShape
                        X = Y = Z = True
                        RVS = rig.listConnections(rotateCon, s = False, d = True, type = 'remapValue')
                        if RVS:
                            print '============================'+rotateCon
                            rig.setAttr(con+'.rotateX', l = False, k = True)
                            rig.setAttr(con+'.rotateY', l = False, k = True)
                            rig.setAttr(con+'.rotateZ', l = False, k = True)
                            
                            
                            if rotateCon+'_IN_RV' in RVS or rotateCon+'_OUT_RV' in RVS:
                                X = False
                            if rotateCon+'_DN_RV' in RVS or rotateCon+'_UP_RV' in RVS:
                                Y = False
                            if rotateCon+'_BACK_RV' in RVS or rotateCon+'_Front_RV' in RVS:
                                Z = False
                                
                            if X:
                                rig.setAttr(con+'.rotateX', cb = False, l = True, k = False)
                            if Y:
                                rig.setAttr(con+'.rotateY', cb = False, l = True, k = False)
                            if Z:
                                rig.setAttr(con+'.rotateZ', cb = False, l = True, k = False)
                                
                                
                if 1258 == rig.getAttr(con+'.sign'):#眼睛控制器
                    rig.setAttr(con+'.rotateZ',  l = False, k = True)
                    rig.setAttr(con+'.scaleX',  l = False, k = True)
                    rig.setAttr(con+'.scaleZ',  l = False, k = True)
                    
                if 58914 == rig.getAttr(con+'.sign'):#耳朵控制器
                    rig.setAttr(con+'.rotateX',  l = False, k = True)
                    rig.setAttr(con+'.rotateY',  l = False, k = True)
                    rig.setAttr(con+'.rotateZ',  l = False, k = True)
                    
                if 54861 == rig.getAttr(con+'.sign'):#下巴控制器
                    rig.setAttr(con+'.rotateX',  l = False, k = True)
                    rig.setAttr(con+'.rotateY',  l = False, k = True)
                    rig.setAttr(con+'.rotateZ',  l = False, k = True)
                    rig.setAttr(con+'.scaleX',  l = False, k = True)
                    rig.setAttr(con+'.scaleY',  l = False, k = True)
                    rig.setAttr(con+'.scaleZ',  l = False, k = True)
                        
                if 32547 == rig.getAttr(con+'.sign'):#舌头控制器
                    rig.setAttr(con+'.rotateX',  l = False, k = True)
                    rig.setAttr(con+'.rotateY',  l = False, k = True)
                    rig.setAttr(con+'.rotateZ',  l = False, k = True)
                    
                if 11548 == rig.getAttr(con+'.sign'):#新增加的控制器
                    rig.setAttr(con+'.rotateX',  l = False, k = True)
                    rig.setAttr(con+'.rotateY',  l = False, k = True)
                    rig.setAttr(con+'.rotateZ',  l = False, k = True)
                    rig.setAttr(con+'.scaleX',  l = False, k = True)
                    rig.setAttr(con+'.scaleY',  l = False, k = True)                    
                    rig.setAttr(con+'.scaleZ',  l = False, k = True)
                    
    def done(self):
        self.startLockTransform()
        self.startLockCons()
    