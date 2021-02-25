#-*- coding: utf-8 -*-
from maya.cmds import *

class CreateControler():
    def __init__(self,color = 22,scaleControl = [1,1,1]):
        self.color = color
        self.curveSale = scaleControl
        self.signValue = 98
            
    def setColor(self,currentColor):
        self.color = currentColor  
    
    def setObjScale(self,scaleValue):
        self.curveSale = scaleValue  
        
    def getCurvePointInfo(self,curveName):
        vertxs = ls(curveName+'.cv[*]',fl = True)
        commomandPosition = []
        vertexNum = []
        for i,ver in enumerate(vertxs):
            vertexPos = xform(ver,q = True,t = True,ws = True)
            commomandPosition.append(tuple(vertexPos))
            vertexNum.append(i)
        commandStr = 'curveName = curve(n = reCurveName,d = 1,p ='+str(commomandPosition)+',k = '+str(vertexNum)+')'
        return commandStr
        
    def addExtraFunction(self,curveName):
        addAttr(curveName,ln = 'sign',at = 'long',dv = self.signValue)
        curveNameShape = listRelatives(curveName,s = True)[0]
        curveNameShape = rename(curveNameShape,curveName+'Shape')
        setAttr(curveNameShape+'.overrideEnabled',1)
        setAttr(curveNameShape+'.overrideColor',self.color)
        setAttr(curveName+'.scaleX',self.curveSale[0]) 
        setAttr(curveName+'.scaleY',self.curveSale[1])        
        setAttr(curveName+'.scaleZ',self.curveSale[2])
        makeIdentity(curveName,apply = True,t = True,r = True,s = True)          
                   
    def SK_b01(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p = [(-1,1,1),(-1,1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,-1,1),(-1,-1,-1),(-1,1,-1),(-1,1,1),(-1,-1,1),(1,-1,1),(1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(1,-1,-1),(-1,-1,-1)],k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
        self.addExtraFunction(curveName)
        return curveName
    
    
    def SK_b02(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.14276976800930941, 0.14276976800930941, -1.5366909763867611), (0.14276976800930941, -0.14276976800930941, -1.5366909763867611), (4.4428575842012287e-016, 0.0, -2.0008851760642932), (0.14276976800930941, -0.14276976800930941, -1.5366909763867611), (-0.14276976800930941, -0.14276976800930941, -1.5366909763867611), (4.4428575842012287e-016, 0.0, -2.0008851760642932), (-0.14276976800930941, -0.14276976800930941, -1.5366909763867611), (-0.14276976800930941, 0.14276976800930941, -1.5366909763867611), (4.4428575842012287e-016, 0.0, -2.0008851760642932), (-0.14276976800930941, 0.14276976800930941, -1.5366909763867611), (0.14276976800930941, 0.14276976800930941, -1.5366909763867611), (4.4428575842012287e-016, 0.0, -2.0008851760642932), (0.0, 0.0, 0.0), (-2.0008851760642932, 0.0, 0.0), (-1.5366909763867611, 0.14276976800930941, -0.14276976800930941), (-2.0008851760642932, 0.0, 0.0), (-1.5366909763867611, 0.14276976800930941, 0.14276976800930941), (-1.5366909763867611, -0.14276976800930941, 0.14276976800930941), (-2.0008851760642932, 0.0, 0.0), (-1.5366909763867611, -0.14276976800930941, -0.14276976800930941), (-1.5366909763867611, 0.14276976800930941, -0.14276976800930941), (-1.5366909763867611, 0.14276976800930941, 0.14276976800930941), (-1.5366909763867611, -0.14276976800930941, 0.14276976800930941), (-1.5366909763867611, -0.14276976800930941, -0.14276976800930941), (-2.0008851760642932, 0.0, 0.0), (0.0, 0.0, 0.0), (-4.4428575842012287e-016, 0.0, 2.0008851760642932), (-0.14276976800930941, -0.14276976800930941, 1.5366909763867611), (0.14276976800930941, -0.14276976800930941, 1.5366909763867611), (0.14276976800930941, 0.14276976800930941, 1.5366909763867611), (-0.14276976800930941, 0.14276976800930941, 1.5366909763867611), (-0.14276976800930941, -0.14276976800930941, 1.5366909763867611), (-4.4428575842012287e-016, 0.0, 2.0008851760642932), (0.14276976800930941, -0.14276976800930941, 1.5366909763867611), (0.14276976800930941, 0.14276976800930941, 1.5366909763867611), (-4.4428575842012287e-016, 0.0, 2.0008851760642932), (-0.14276976800930941, 0.14276976800930941, 1.5366909763867611), (-4.4428575842012287e-016, 0.0, 2.0008851760642932), (0.0, 0.0, 0.0), (2.0008851760642932, 0.0, 0.0), (1.5366909763867611, 0.14276976800930941, 0.14276976800930941), (1.5366909763867611, 0.14276976800930941, -0.14276976800930941), (2.0008851760642932, 0.0, 0.0), (1.5366909763867611, 0.14276976800930941, -0.14276976800930941), (1.5366909763867611, -0.14276976800930941, -0.14276976800930941), (2.0008851760642932, 0.0, 0.0), (1.5366909763867611, -0.14276976800930941, -0.14276976800930941), (1.5366909763867611, -0.14276976800930941, 0.14276976800930941), (2.0008851760642932, 0.0, 0.0), (1.5366909763867611, -0.14276976800930941, 0.14276976800930941), (1.5366909763867611, 0.14276976800930941, 0.14276976800930941)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
        self.addExtraFunction(curveName)
        return curveName
    
    
    def SK_b03(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p = [(0,1,0),(0,0.92388,0.382683),(0,0.707107,0.707107),(0,0.382683,0.92388),(0,0,1),(0,-0.382683,0.92388),(0,-0.707107,0.707107),(0,-0.92388,0.382683),(0,-1,0),(0,-0.92388,-0.382683),(0,-0.707107,-0.707107),(0,-0.382683,-0.92388),(0,0,-1),(0,0.382683,-0.92388),(0,0.707107,-0.707107),(0,0.92388,-0.382683),(0,1,0),(0.382683,0.92388,0),(0.707107,0.707107,0),(0.92388,0.382683,0),(1,0,0),(0.92388,-0.382683,0),(0.707107,-0.707107,0),(0.382683,-0.92388,0),(0,-1,0),(-0.382683,-0.92388,0),(-0.707107,-0.707107,0),(-0.92388,-0.382683,0),(-1,0,0),(-0.92388,0.382683,0),(-0.707107,0.707107,0),(-0.382683,0.92388,0),(0,1,0),(0,0.92388,-0.382683),(0,0.707107,-0.707107),(0,0.382683,-0.92388),(0,0,-1),(-0.382683,0,-0.92388),(-0.707107,0,-0.707107),(-0.92388,0,-0.382683),(-1,0,0),(-0.92388,0,0.382683),(-0.707107,0,0.707107),(-0.382683,0,0.92388),(0,0,1),(0.382683,0,0.92388),(0.707107,0,0.707107),(0.92388,0,0.382683),(1,0,0),(0.92388,0,-0.382683),(0.707107,0,-0.707107),(0.382683,0,-0.92388),(0,0,-1)],k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
        self.addExtraFunction(curveName)
        return curveName
    
    
    def SK_b04(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.0, 2.7937496295181701, 0.0), (-0.46562493825302836, 2.7937496295181701, 0.0), (0.0, 3.7249995060242269, 0.0), (0.46562493825302836, 2.7937496295181701, 0.0), (0.0, 2.7937496295181701, 0.0), (0.0, 0.46562493825302836, 0.0), (0.12038593091050574, 0.44935507166059102, 0.0), (0.23261597540257142, 0.4028670778254087, 0.0), (0.32924898133797537, 0.32924921415044456, 0.0), (0.40286742704411238, 0.23261585899633683, 0.0), (0.4493546060356528, 0.1203860473167403, 0.0), (0.46562843044006524, -2.6846769877323982e-008, 0.0), (0.4493546060356528, -0.12038593091050574, 0.0), (0.40286742704411238, -0.23261597540257142, 0.0), (0.32924898133797537, -0.32924898133797537, 0.0), (0.23261597540257142, -0.40286742704411238, 0.0), (0.12038593091050574, -0.4493546060356528, 0.0), (0.0, -0.46562843044006524, 0.0), (-0.12038593091050574, -0.4493546060356528, 0.0), (-0.23261597540257142, -0.40286742704411238, 0.0), (-0.32924898133797537, -0.32924898133797537, 0.0), (-0.40286742704411238, -0.23261597540257142, 0.0), (-0.4493546060356528, -0.12038593091050574, 0.0), (-0.46562843044006524, -2.6846769877323982e-008, 0.0), (-0.4493546060356528, 0.1203860473167403, 0.0), (-0.40286742704411238, 0.23261585899633683, 0.0), (-0.32924898133797537, 0.32924921415044456, 0.0), (-0.23261597540257142, 0.4028670778254087, 0.0), (-0.12038593091050574, 0.44935507166059102, 0.0), (0.0, 0.46562493825302836, 0.0)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])
        self.addExtraFunction(curveName)
        return curveName
    
    
    def SK_b05(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.0, 2.1767556185711627, 0.0), (-0.17434363973420747, 2.2003234927389257, 0.0), (-0.33687556824535481, 2.2676466057307794, 0.0), (-0.47681988632445044, 2.3742610232111976, 0.0), (-0.58343430380486649, 2.5142053412902929, 0.0), (-0.6507574167967195, 2.6767372698014413, 0.0), (-0.6743252909644829, 2.8510809095356486, 0.0), (-0.6507574167967195, 3.0254245492698568, 0.0), (-0.58343430380486649, 3.1879560109887506, 0.0), (-0.47681988632445044, 3.3279007958601015, 0.0), (-0.33687556824535481, 3.4345147465482642, 0.0), (-0.17434363973420747, 3.5018387931246275, 0.0), (0.0, 3.5254005989930746, 0.0), (0.17434363973420747, 3.5018387931246275, 0.0), (0.33687556824535481, 3.4345147465482642, 0.0), (0.47681988632445044, 3.3279007958601015, 0.0), (0.58343430380486649, 3.1879560109887506, 0.0), (0.6507574167967195, 3.0254245492698568, 0.0), (0.6743252909644829, 2.8510809095356486, 0.0), (0.6507574167967195, 2.6767372698014413, 0.0), (0.58343430380486649, 2.5142053412902929, 0.0), (0.47681988632445044, 2.3742610232111976, 0.0), (0.33687556824535481, 2.2676466057307794, 0.0), (0.17434363973420747, 2.2003234927389257, 0.0), (0.0, 2.1767556185711627, 0.0), (0.0, 0.0, 0.0)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]) 
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b06(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(-1.8179497808237617, 0.0, 0.0), (-1.0907698684942568, 0.0, -0.72717991232950463), (-1.0907698684942568, 0.0, -0.36358995616475231), (-0.36358995616475231, 0.0, -0.36358995616475231), (-0.36358995616475231, 0.0, -1.0907698684942568), (-0.72717991232950463, 0.0, -1.0907698684942568), (0.0, 0.0, -1.8179497808237617), (0.72717991232950463, 0.0, -1.0907698684942568), (0.36358995616475231, 0.0, -1.0907698684942568), (0.36358995616475231, 0.0, -0.36358995616475231), (1.0907698684942568, 0.0, -0.36358995616475231), (1.0907698684942568, 0.0, -0.72717991232950463), (1.8179497808237617, 0.0, 0.0), (1.0907698684942568, 0.0, 0.72717991232950463), (1.0907698684942568, 0.0, 0.36358995616475231), (0.36358995616475231, 0.0, 0.36358995616475231), (0.36358995616475231, 0.0, 1.0907698684942568), (0.72717991232950463, 0.0, 1.0907698684942568), (0.0, 0.0, 1.8179497808237617), (-0.72717991232950463, 0.0, 1.0907698684942568), (-0.36358995616475231, 0.0, 1.0907698684942568), (-0.36358995616475231, 0.0, 0.36358995616475231), (-1.0907698684942568, 0.0, 0.36358995616475231), (-1.0907698684942568, 0.0, 0.72717991232950463), (-1.8179497808237617, 0.0, 0.0)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b07(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.86016622641951312, -1.0421035791954429, 5.5470404419354216e-008), (0.83010407736574043, -1.0421035791954429, -0.22238810834064518), (0.74422416276127967, -1.0421035791954429, -0.42971998248517196), (0.60822948432531698, -1.0421035791954429, -0.60822977104519427), (0.4297201258451106, -1.0421035791954429, -0.7442235893215251), (0.22238796498070648, -1.0421035791954429, -0.83010493752537229), (0.0, -1.0421035791954429, -0.86015963186233557), (0.0, 1.0501766458770525, -0.86015963186233557), (0.22238796498070648, 1.0501766458770525, -0.83010493752537229), (0.4297201258451106, 1.0501766458770525, -0.7442235893215251), (0.60822948432531698, 1.0501766458770525, -0.60822977104519427), (0.74422416276127967, 1.0501766458770525, -0.42971998248517196), (0.83010407736574043, 1.0501766458770525, -0.22238810834064518), (0.86016622641951312, 1.0501766458770525, 5.5470404419354216e-008), (0.86016622641951312, -1.0421035791954429, 5.5470404419354216e-008), (0.83010407736574043, -1.0421035791954429, 0.22238796498070648), (0.74422416276127967, -1.0421035791954429, 0.4297201258451106), (0.60822948432531698, -1.0421035791954429, 0.6082293409653784), (0.4297201258451106, -1.0421035791954429, 0.74422416276127967), (0.22238796498070648, -1.0421035791954429, 0.83010407736574043), (0.0, -1.0421035791954429, 0.86016622641951312), (-0.22238796498070648, -1.0421035791954429, 0.83010407736574043), (-0.4297201258451106, -1.0421035791954429, 0.74422416276127967), (-0.60822948432531698, -1.0421035791954429, 0.6082293409653784), (-0.74422416276127967, -1.0421035791954429, 0.4297201258451106), (-0.83010407736574043, -1.0421035791954429, 0.22238796498070648), (-0.86016622641951312, -1.0421035791954429, 5.5470404419354216e-008), (-0.86016622641951312, 1.0501766458770525, 5.5470404419354216e-008), (-0.83010407736574043, 1.0501766458770525, -0.22238810834064518), (-0.74422416276127967, 1.0501766458770525, -0.42971998248517196), (-0.60822948432531698, 1.0501766458770525, -0.60822977104519427), (-0.4297201258451106, 1.0501766458770525, -0.7442235893215251), (-0.22238796498070648, 1.0501766458770525, -0.83010493752537229), (0.0, 1.0501766458770525, -0.86015963186233557), (0.0, -1.0421035791954429, -0.86015963186233557), (-0.22238796498070648, -1.0421035791954429, -0.83010493752537229), (-0.4297201258451106, -1.0421035791954429, -0.7442235893215251), (-0.60822948432531698, -1.0421035791954429, -0.60822977104519427), (-0.74422416276127967, -1.0421035791954429, -0.42971998248517196), (-0.83010407736574043, -1.0421035791954429, -0.22238810834064518), (-0.86016622641951312, -1.0421035791954429, 5.5470404419354216e-008), (-0.86016622641951312, 1.0501766458770525, 5.5470404419354216e-008), (-0.83010407736574043, 1.0501766458770525, 0.22238796498070648), (-0.74422416276127967, 1.0501766458770525, 0.4297201258451106), (-0.60822948432531698, 1.0501766458770525, 0.6082293409653784), (-0.4297201258451106, 1.0501766458770525, 0.74422416276127967), (-0.22238796498070648, 1.0501766458770525, 0.83010407736574043), (0.0, 1.0501766458770525, 0.86016622641951312), (0.0, -1.0421035791954429, 0.86016622641951312), (0.0, 1.0501766458770525, 0.86016622641951312), (0.22238796498070648, 1.0501766458770525, 0.83010407736574043), (0.4297201258451106, 1.0501766458770525, 0.74422416276127967), (0.60822948432531698, 1.0501766458770525, 0.6082293409653784), (0.74422416276127967, 1.0501766458770525, 0.4297201258451106), (0.83010407736574043, 1.0501766458770525, 0.22238796498070648), (0.86016622641951312, 1.0501766458770525, 5.5470404419354216e-008)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
        self.addExtraFunction(curveName)
        return curveName        
        
    def SK_b08(self,reCurveName = 'Create_NurbsCurve'):
        curveName = circle(n = reCurveName,ch  = False,o = True,nr = (0 ,1, 0), r = 1.5 )[0]
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b09(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.47781362323510618, 0.0, 1.815730363906124), (0.47781362323510618, 0.0, -0.85200931441093686), (1.1293076882320596, 0.0, -0.85200931441093686), (0.0, 0.0, -2.492290392206129), (-1.1293076882320596, 0.0, -0.85200931441093686), (-0.47781362323510618, 0.0, -0.85200931441093686), (-0.47781362323510618, 0.0, 1.815730363906124), (0.47781362323510618, 0.0, 1.815730363906124)],k = [0, 1, 2, 3, 4, 5, 6, 7])
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b10(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p = [(0.99849,-0.361451,-0.00832399),(1.0,-0.339251,-0.777634),(1.0,-0.257393,-1.430587),(1.0,-0.128336,-1.867774),(1.001447,0.0,-2.0),(-0.00188492,-0.242605,-0.999625),(-1.001447,0.0,-2.0),(-1.0,-0.128336,-1.867774),(-1.0,-0.257393,-1.430587),(-1.0,-0.339251,-0.777634),(-0.99849,-0.361451,-0.00832399),(-1.0,-0.339251,0.777634),(-1.0,-0.257393,1.430587),(-1.0,-0.128336,1.867774),(-1.001447,0.0,2.0),(-2.79164e-009,-0.242553,1.000375),(1.001447,0.0,2.0),(1.0,-0.128336,1.867774),(1.0,-0.257393,1.430587),(1.0,-0.339251,0.777634),(0.99849,-0.361451,-0.00832399)],k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b11(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(0.0, -0.23751066114757699, 2.2467592170845747), (0.59319414819436145, 8.6397941783769455e-020, 1.1525140643207143), (0.19922009007264921, 0.0, 1.1525140643207143), (0.19922009007264921, 0.091151894309201106, 1.0647846984854648), (0.19922009007264921, 0.16820581729264805, 0.81495129837927183), (0.19922009007264921, 0.21969125957182345, 0.44104838555972253), (0.19922009007264921, 0.23777138717723448, 1.0010592074394163e-016), (0.19922009007264921, 0.21969125957182345, -0.44104838555972253), (0.19922009007264921, 0.16820581729264805, -0.81495129837927183), (0.19922009007264921, 0.091151894309201106, -1.0647846984854648), (0.19922009007264921, 0.0, -1.1525140643207143), (0.59319414819436145, 0.0, -1.1525140643207143), (0.0, -0.23751066114757699, -2.2467592170845747), (-0.59319414819436145, 0.0, -1.1525140643207143), (-0.19922009007264921, 0.0, -1.1525140643207143), (-0.19922009007264921, 0.091151894309201106, -1.0647846984854648), (-0.19922009007264921, 0.16820581729264805, -0.81495129837927183), (-0.19922009007264921, 0.21969125957182345, -0.44104838555972253), (-0.19922009007264921, 0.23777138717723448, 1.0010592074394163e-016), (-0.19922009007264921, 0.21969125957182345, 0.44104838555972253), (-0.19922009007264921, 0.16820581729264805, 0.81495129837927183), (-0.19922009007264921, 0.091151894309201106, 1.0647846984854648), (-0.19922009007264921, 0.0, 1.1525140643207143), (-0.59319414819436145, 8.6397941783769455e-020, 1.1525140643207143), (0.0, -0.23751066114757699, 2.2467592170845747)],k = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]) 
        self.addExtraFunction(curveName)
        return curveName    
    
    def SK_b12(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p = [(0.0,0.0,0.0),(0.0,2.13814898866,0.0),(-0.418923967766,2.27426533506,0.0),(-0.677834210593,2.63062349984,0.0),(-0.677834210593,3.07110713658,0.0),(-0.418923967766,3.42746530135,0.0),(0.0,3.56358164776,0.0),(0.418923967766,3.42746530135,0.0),(0.677834210593,3.07110713658,0.0),(0.677834210593,2.63062349984,0.0),(0.418923967766,2.27426533506,0.0),(0.0,2.13814898866,0.0)],k = [0,1,2,3,4,5,6,7,8,9,10,11])
        self.addExtraFunction(curveName)
        return curveName
    
    def SK_b13(self,reCurveName = 'Create_NurbsCurve'):
        curveName = curve(n = reCurveName,d = 1,p =[(-2.0000000000000018, 0.0, -2.0000000000000004), (-2.0000000000000018, 0.0, 2.0000000000000004), (2.0000000000000018, 0.0, 2.0000000000000004), (2.0000000000000018, 0.0, -2.0000000000000004), (-2.0000000000000018, 0.0, -2.0000000000000004)],k = [0, 1, 2, 3, 4])
        self.addExtraFunction(curveName)
        return curveName

def setAimObj(sour,targ):
    aimName = aimConstraint(sour,targ,aimVector = (0,0,-1),upVector = (0,1,0),worldUpType = 'vector',worldUpVector = (0,1,0))
    delete(aimName)

def SK_createCompoundAttrs(outName,num):
    setStrs = []
    upName = 'Boss'
    midName = 'data'
    lowName = 'bess'
    
    outDataName = 'inData'
    suffix = 0
    
    objSC = createNode('choice',n = outName.split('_')[0]+'_SC',ss = True)
    addAttr(objSC,longName=upName, numberOfChildren=num, attributeType='compound' )
    addAttr(outName,longName=outDataName, numberOfChildren=num, attributeType='compound')

    for i in range(num):
        addAttr(outName, longName='out'+lowName+str(i), attributeType='double') 
        addAttr(outName, longName=lowName+str(i), attributeType='double',parent = outDataName) 
        addAttr(objSC,longName=midName+str(i), numberOfChildren=num, attributeType='compound',p = upName )
        for j in range(num):
            suffix += 1
            if(i == j):
                setStrs.append('.'+upName+'.'+midName+str(i)+'.'+lowName+str(suffix))
                addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )
            else:
                addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )            

    for i,attrName in enumerate(setStrs):
        connectAttr(outName+'.'+outDataName+'.'+lowName+str(i),outName+'.out'+lowName+str(i))
        connectAttr(objSC+'.'+upName+'.'+midName+str(i),objSC+'.input['+str(i)+']')
        setAttr(objSC+attrName,1)
        
    connectAttr(objSC+'.output',outName+'.'+outDataName)
        
    return objSC

def SK_hideWheelAttr(objs = []):
    for obj in objs:
        setAttr(obj+'.tx',cb = False,l = True,k = False)
        setAttr(obj+'.ty',cb = False,l = True,k = False)
        setAttr(obj+'.tz',cb = False,l = True,k = False)
        setAttr(obj+'.sx',cb = False,l = True,k = False)
        setAttr(obj+'.sy',cb = False,l = True,k = False)
        setAttr(obj+'.sz',cb = False,l = True,k = False)
        setAttr(obj+'.ry',cb = False,l = True,k = False)
        setAttr(obj+'.rz',cb = False,l = True,k = False)        
        
def setSelectAttr():
    slGrpObj = group(empty = True,n = 'slectLock')
    addAttr(slGrpObj,at = 'float',ln = 'Front')
    addAttr(slGrpObj,at = 'float',ln = 'Back')
    slGrp = SK_createCompoundAttrs(slGrpObj,6)
    setAttr(slGrp+'.Boss.data0.bess1',1)
    setAttr(slGrp+'.Boss.data0.bess2',0)
    setAttr(slGrp+'.Boss.data0.bess3',1)
    setAttr(slGrp+'.Boss.data0.bess4',0)
    setAttr(slGrp+'.Boss.data0.bess5',0)
    setAttr(slGrp+'.Boss.data0.bess6',0)
    
    
    setAttr(slGrp+'.Boss.data1.bess7',0)
    setAttr(slGrp+'.Boss.data1.bess8',1)
    setAttr(slGrp+'.Boss.data1.bess9',0)
    setAttr(slGrp+'.Boss.data1.bess10',1)
    setAttr(slGrp+'.Boss.data1.bess11',0)
    setAttr(slGrp+'.Boss.data1.bess12',0)
    
    
    setAttr(slGrp+'.Boss.data2.bess13',1)
    setAttr(slGrp+'.Boss.data2.bess14',1)
    setAttr(slGrp+'.Boss.data2.bess15',0)
    setAttr(slGrp+'.Boss.data2.bess16',0)
    setAttr(slGrp+'.Boss.data2.bess17',0)
    setAttr(slGrp+'.Boss.data2.bess18',0)
    
    
    setAttr(slGrp+'.Boss.data3.bess19',0)
    setAttr(slGrp+'.Boss.data3.bess20',0)
    setAttr(slGrp+'.Boss.data3.bess21',1)
    setAttr(slGrp+'.Boss.data3.bess22',1)
    setAttr(slGrp+'.Boss.data3.bess23',0)
    setAttr(slGrp+'.Boss.data3.bess24',0)
    
    
    setAttr(slGrp+'.Boss.data4.bess25',1)
    setAttr(slGrp+'.Boss.data4.bess26',1)
    setAttr(slGrp+'.Boss.data4.bess27',1)
    setAttr(slGrp+'.Boss.data4.bess28',1)
    setAttr(slGrp+'.Boss.data4.bess29',1)
    setAttr(slGrp+'.Boss.data4.bess30',1)
    
    setAttr(slGrp+'.Boss.data5.bess31',0)
    setAttr(slGrp+'.Boss.data5.bess32',0)
    setAttr(slGrp+'.Boss.data5.bess33',0)
    setAttr(slGrp+'.Boss.data5.bess34',0)
    setAttr(slGrp+'.Boss.data5.bess35',0)
    setAttr(slGrp+'.Boss.data5.bess36',0)
    
    return slGrpObj,slGrp

def wheelSetup():
    wheels = ls(sl = True)  
    
    curGrp,curSeNode = setSelectAttr()
    cusName = ['Lf_Front','Rt_Front','Lf_Back','Rt_Back']
    jntsPos = []
    jnts = []
    Locs = []
    LocGeo = []
    LocPoint = []
    LocPointPos = []
    for i,wl in enumerate(wheels):
        pos = objectCenter(wl,gl = True)
        Loc = cusName[i]+'_LOC'
        locPos = xform(Loc,q = True,t = True,ws = True)
        select(cl = True)
        jnt = joint(p = pos,n = cusName[i]+'_JNT')
        
        LocPt = duplicate(Loc,n = cusName[i]+'_LOC_Point')[0]
        LocGo = duplicate(Loc,n = cusName[i]+'_LOC_Geometry')[0]
        addAttr(LocGo,at = 'float',ln = 'sign')
        PNTConstraint = pointConstraint(LocPt,LocGo,Loc)[0]
        pointConstraint(LocPt,LocGo)
        addAttr(jnt,at = 'float',ln = 'Lock',k = False)
        jntRV = createNode('reverse',n = cusName[i]+'_RV',ss = True)
        connectAttr(jnt+'.Lock',jntRV+'.inputX')
        connectAttr(jntRV+'.outputX',PNTConstraint+'.'+LocPt+'W0')
        connectAttr(jnt+'.Lock',PNTConstraint+'.'+LocGo+'W1')
        connectAttr(curGrp+'.outbess'+str(i),jnt+'.Lock')    
        jnts.append(jnt)
        jntsPos.append(pos)
        LocPointPos.append(locPos)
        Locs.append(Loc)
        LocPoint.append(LocPt)
        LocGeo.append(LocGo)
     
    barFront = ((jntsPos[0][0]+ jntsPos[1][0])/2,(jntsPos[0][1]+ jntsPos[1][1])/2,(jntsPos[0][2]+ jntsPos[1][2])/2)
    barBack  = ((jntsPos[2][0]+ jntsPos[3][0])/2,(jntsPos[2][1]+ jntsPos[3][1])/2,(jntsPos[2][2]+ jntsPos[3][2])/2)
    chassis = ((barFront[0]+ barBack[0])/2.0,(barFront[1]+ barBack[1])/2.0,(barFront[2]+ barBack[2])/2.0)
    select(cl = True)
    BFName = joint(p = barFront,n = 'barFront_JNT')
    select(cl = True)
    BBName = joint(p = barBack,n = 'barBack_JNT')
    select(cl = True)
    BDName = joint(p = chassis,n = 'chassis_JNT')
    
    
    
    
    #创建空组
    controls = CreateControler(13,(5,5,5))
    carName = controls.SK_b01('MIS')
    setAttr(carName+'.visibility',cb = False,k = False)
    addAttr(carName,at = 'float',ln = 'direction',dv = 1,k = True)
    chassisCon = controls.SK_b09('Chassis_Con')
    setAttr(chassisCon+'.visibility',cb = False,k = False)
    closeCurve(chassisCon,ch = False,ps = True,rpo = True,bb = 0.5,p = 0.1)
    addAttr(chassisCon,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(chassisCon,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(chassisCon,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    
    LfCar = group(empty = True,n = 'Car_Con_Left')
    UpLfCar = group(LfCar,n = LfCar+'_UP',r = True)
    xform(UpLfCar,t = LocPointPos[0],ws = True)
    setAimObj(Locs[2],UpLfCar)
    parent(UpLfCar,carName)
    RtCar = group(empty = True,n = 'Car_Con_Right')
    UpRtCar = group(RtCar,n = RtCar+'_UP',r = True)
    xform(UpRtCar,t = LocPointPos[1],ws = True)
    setAimObj(Locs[3],UpRtCar)
    parent(UpRtCar,LfCar)
    FnCar = group(empty = True,n = 'Car_Con_Front')
    UpFnCar = group(FnCar,n = FnCar+'_UP',r = True)    
    xform(UpFnCar,t = LocPointPos[3],ws = True)
    parent(UpFnCar,RtCar)
    BcCar = group(empty = True,n = 'Car_Con_Back')
    UpBcCar = group(BcCar,n = BcCar+'_UP',r = True)      
    xform(UpBcCar,t = LocPointPos[0],ws = True)
    parent(UpBcCar,FnCar)
    normalCarGrp = group(carName,n = 'normal_Car_Grp')
    move(0,0,0,normalCarGrp+'.scalePivot',normalCarGrp+'.rotatePivot')
    addAttr(normalCarGrp,at = 'float',ln = 'sign')
    connectAttr('MIS.sign',normalCarGrp+'.sign')
    pathGrp = group(normalCarGrp,n = 'Path_Car_Grp')
    move(0,0,0,pathGrp+'.scalePivot',pathGrp+'.rotatePivot')
    addAttr(pathGrp,at = 'float',ln = 'sign')
    connectAttr('MIS.sign',pathGrp+'.sign')
    #end
    
    
    
    #生成condition节点�?
    addAttr(carName,at = 'enum',ln = 'Lock',en = 'Left:Right:Front:Back:All:None:',dv = 4,k = True)
    connectAttr(carName+'.Lock',curSeNode+'.selector')
    addAttr(carName,at = 'float',ln = 'LeftRight',k = True)
    addAttr(carName,at = 'float',ln = 'BackFront',k = True)
    
    LeftCDT = createNode('condition',n = 'Left_CDT',ss = True)
    setAttr(LeftCDT+'.operation',4)
    connectAttr(carName+'.LeftRight',LeftCDT+'.firstTerm')
    connectAttr(carName+'.LeftRight',LeftCDT+'.colorIfTrueR')
    setAttr(LeftCDT+'.colorIfFalseR',0)
    connectAttr(LeftCDT+'.outColor.outColorR',LfCar+'.rz')
    
    RightCDT = createNode('condition',n = 'Right_CDT',ss = True)
    setAttr(RightCDT+'.operation',2)
    connectAttr(carName+'.LeftRight',RightCDT+'.firstTerm')
    connectAttr(carName+'.LeftRight',RightCDT+'.colorIfTrueR')
    setAttr(RightCDT+'.colorIfFalseR',0)
    connectAttr(RightCDT+'.outColor.outColorR',RtCar+'.rz')
    
    FrontCDT = createNode('condition',n = 'Front_CDT',ss = True)
    setAttr(FrontCDT+'.operation',4)
    connectAttr(carName+'.BackFront',FrontCDT+'.firstTerm')
    connectAttr(carName+'.BackFront',FrontCDT+'.colorIfTrueR')
    setAttr(FrontCDT+'.colorIfFalseR',0)
    connectAttr(FrontCDT+'.outColor.outColorR',FnCar+'.rx')
    
    BackCDT = createNode('condition',n = 'Back_CDT',ss = True)
    setAttr(BackCDT+'.operation',2)
    connectAttr(carName+'.BackFront',BackCDT+'.firstTerm')
    connectAttr(carName+'.BackFront',BackCDT+'.colorIfTrueR')
    setAttr(BackCDT+'.colorIfFalseR',0)
    connectAttr(BackCDT+'.outColor.outColorR',BcCar+'.rx')
    
    
    PIOGRP = []
    upJntsGrp = ['UP','POI','NO','Trans','JUST','EX','MAN']
    for wheelJnt in upJntsGrp:
        for jnt in jnts:
            newGrp = group(jnt,n = jnt+'_'+wheelJnt)
            if wheelJnt == 'POI':
                pointConstraint(jnt.replace('JNT','LOC'),newGrp,mo  = True)
            if wheelJnt == 'UP':            
                PIOGRP.append(newGrp)
    allWheel = group(PIOGRP,n = 'Wheel_All_GRP')
    parent(allWheel,'Car_Con_Back')
    allLoc = group(LocPoint,n = 'Locator_All_GRP')
    parent(allLoc,'Car_Con_Back')
    origAllLoc = group(Locs,n = 'origLoc_All_GRP')
    parent(origAllLoc,'Car_Con_Back')
    geoAllLoc = group(LocGeo,n = 'GeoLoc_All_GRP')
    parent(geoAllLoc,'Car_Con_Back')
    
    #  wheel radius Loctor
    FrontWheelUPLoc = spaceLocator(n = 'Front_Wheel_UP_LOC')[0]
    FrontWheelDNLoc = spaceLocator(n = 'Front_Wheel_DN_LOC')[0]
    BackWheelUPLoc = spaceLocator(n = 'Back_Wheel_UP_LOC')[0]
    BackWheelDNLoc = spaceLocator(n = 'Back_Wheel_DN_LOC')[0]
    TemNode = pointConstraint('Lf_Front_JNT',FrontWheelUPLoc)
    delete(TemNode)
    TemNode = pointConstraint('Lf_Front_LOC',FrontWheelDNLoc)
    delete(TemNode)
    wheelNode = createNode('distanceBetween',n = 'Front_DIB')
    connectAttr(FrontWheelUPLoc+'.worldMatrix',wheelNode+'.inMatrix1')
    connectAttr(FrontWheelDNLoc+'.worldMatrix',wheelNode+'.inMatrix2')
    connectAttr(wheelNode+'.distance',curGrp+'.Front')
    TemNode = pointConstraint('Lf_Back_JNT',BackWheelUPLoc)
    delete(TemNode)
    TemNode = pointConstraint('Lf_Back_LOC',BackWheelDNLoc)
    delete(TemNode)
    wheelNode = createNode('distanceBetween',n = 'Bace_DIB')
    connectAttr(BackWheelUPLoc+'.worldMatrix',wheelNode+'.inMatrix1')
    connectAttr(BackWheelDNLoc+'.worldMatrix',wheelNode+'.inMatrix2')
    connectAttr(wheelNode+'.distance',curGrp+'.Back')
    radusLoc = group(FrontWheelUPLoc,FrontWheelDNLoc,BackWheelUPLoc,BackWheelDNLoc,n = 'rad_Grp')
    parent(radusLoc,'Car_Con_Back')
    
    PositionLoc = spaceLocator(n = 'space_Position')[0]
    pointConstraint('MIS',PositionLoc)
    
    
    setAttr(chassisCon+'.sz',-1)
    makeIdentity(chassisCon,apply = True,s = True)
    chassisAn = group(chassisCon,n = 'chassis_An')
    chassisUp = group(chassisAn,n = 'chassis_UP')
    chassisGrp = group(chassisUp,n = 'chassis_GRP')
    TemParent = parentConstraint('chassis_JNT',chassisGrp)
    delete(TemParent)
    parent('chassis_JNT',chassisCon)
    
    
    #Add controllers
    wheelRadi = getAttr('Front_DIB.distance')
    Lf_F_wheel = circle(ch = False,nr = (1,0,0),n = 'Lf_Front_wheel_C',r = wheelRadi)
    setAttr(Lf_F_wheel[0]+'.visibility',cb = False,k = False)
    addAttr(Lf_F_wheel,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(Lf_F_wheel,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(Lf_F_wheel,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    addAttr(Lf_F_wheel,at = 'float',ln = 'offset',dv = 0,k = True)
    connectAttr(Lf_F_wheel[0]+'.offset',Lf_F_wheel[0].replace('wheel_C','JNT_Trans')+'.ty')
    TemPoints = pointConstraint('Lf_Front_JNT',Lf_F_wheel)
    delete(TemPoints)
    parent(Lf_F_wheel,'Lf_Front_JNT_MAN')
    makeIdentity(Lf_F_wheel,apply = True,s = True,r = True,t = True)
    parent('Lf_Front_JNT',Lf_F_wheel)
    
    wheelRadi = getAttr('Front_DIB.distance')
    Rt_F_wheel = circle(ch = False,nr = (1,0,0),n = 'Rt_Front_wheel_C',r = wheelRadi)
    setAttr(Rt_F_wheel[0]+'.visibility',cb = False,k = False)
    addAttr(Rt_F_wheel,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    addAttr(Rt_F_wheel,at = 'float',ln = 'offset',dv = 0,k = True)
    connectAttr(Rt_F_wheel[0]+'.offset',Rt_F_wheel[0].replace('wheel_C','JNT_Trans')+'.ty')
    TemPoints = pointConstraint('Rt_Front_JNT',Rt_F_wheel)
    delete(TemPoints)
    parent(Rt_F_wheel,'Rt_Front_JNT_MAN')
    makeIdentity(Rt_F_wheel,apply = True,s = True,r = True,t = True)
    parent('Rt_Front_JNT',Rt_F_wheel)
    
    Lf_B_wheel = circle(ch = False,nr = (1,0,0),n = 'Lf_Back_wheel_C',r = wheelRadi)
    setAttr(Lf_B_wheel[0]+'.visibility',cb = False,k = False)
    addAttr(Lf_B_wheel,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(Lf_B_wheel,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(Lf_B_wheel,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    addAttr(Lf_B_wheel,at = 'float',ln = 'offset',dv = 0,k = True)
    connectAttr(Lf_B_wheel[0]+'.offset',Lf_B_wheel[0].replace('wheel_C','JNT_Trans')+'.ty')
    TemPoints = pointConstraint('Lf_Back_JNT',Lf_B_wheel)
    delete(TemPoints)
    parent(Lf_B_wheel,'Lf_Back_JNT_MAN')
    makeIdentity(Lf_B_wheel,apply = True,s = True,r = True,t = True)
    parent('Lf_Back_JNT',Lf_B_wheel)
    
    wheelRadi = getAttr('Front_DIB.distance')
    Rt_B_wheel = circle(ch = False,nr = (1,0,0),n = 'Rt_Back_wheel_C',r = wheelRadi)
    setAttr(Rt_B_wheel[0]+'.visibility',cb = False,k = False)
    addAttr(Rt_B_wheel,at = 'float',ln = 'frequency',dv = 30,k = True)
    addAttr(Rt_B_wheel,at = 'float',ln = 'sizeY',dv = 0,k = True)
    addAttr(Rt_B_wheel,at = 'float',ln = 'sizeZ',dv = 0,k = True)
    addAttr(Rt_B_wheel,at = 'float',ln = 'offset',dv = 0,k = True)
    connectAttr(Rt_B_wheel[0]+'.offset',Rt_B_wheel[0].replace('wheel_C','JNT_Trans')+'.ty')
    TemPoints = pointConstraint('Rt_Back_JNT',Rt_B_wheel)
    delete(TemPoints)
    parent(Rt_B_wheel,'Rt_Back_JNT_MAN')
    makeIdentity(Rt_B_wheel,apply = True,s = True,r = True,t = True)
    parent('Rt_Back_JNT',Rt_B_wheel)
    chassisBodyGRP = group([u'slectLock', u'barFront_JNT', u'barBack_JNT', u'chassis_GRP'],n = 'Chassis_All_GRP')
    parent(chassisBodyGRP,'Car_Con_Back')
    
    # 连接车轮旋转�?
    frontMD = createNode('multiplyDivide',n = 'Front_Rotate_MD',ss = True)
    backMD = createNode('multiplyDivide',n = 'Back_Rotate_MD',ss = True)
    addAttr('MIS',at = 'float',ln = 'FnRo')
    addAttr('MIS',at = 'float',ln = 'BcRo')
    connectAttr('MIS.FnRo',frontMD+'.input1X')
    connectAttr('MIS.BcRo',backMD+'.input1X')
    connectAttr(frontMD+'.outputX','Lf_Front_JNT_Trans.ry')
    connectAttr(frontMD+'.outputX','Rt_Front_JNT_Trans.ry')
    connectAttr(backMD+'.outputX','Lf_Back_JNT_Trans.ry')
    connectAttr(backMD+'.outputX','Rt_Back_JNT_Trans.ry')
    
    connectAttr('MIS.sign','Lf_Front_LOC_Geometry.sign')
    connectAttr('MIS.sign','Rt_Front_LOC_Geometry.sign')
    connectAttr('MIS.sign','Lf_Back_LOC_Geometry.sign')
    connectAttr('MIS.sign','Rt_Back_LOC_Geometry.sign')
    CHR = group(empty = True,n = 'CHR')
    MODEL = group(empty = True,n = 'MODEL')
    CARRIG = group('Path_Car_Grp',n = 'car_RIG')
    deformers = group('space_Position',n = 'car_deformers')
    parent(MODEL,CARRIG,deformers,CHR)
    setAttr('car_deformers.visibility',0)
    setAttr('Locator_All_GRP.visibility',0)
    setAttr('origLoc_All_GRP.visibility',0)
    setAttr('GeoLoc_All_GRP.visibility',0)
    setAttr('rad_Grp.visibility',0)
    
    SK_hideWheelAttr([u'Lf_Back_wheel_C', u'Lf_Front_wheel_C', u'Rt_Front_wheel_C', u'Rt_Back_wheel_C'])
    #createExpressions
    expression(n = 'car_motion',s = '''
    $preX = `getAttr -time(frame-1)space_Position.translateX`;
    $preY = `getAttr -time(frame-1)space_Position.translateY`;
    $preZ = `getAttr -time(frame-1)space_Position.translateZ`;
    
    $valX = space_Position.translateX - $preX;
    $valY = space_Position.translateY - $preY;
    $valZ = space_Position.translateZ - $preZ;
    
    float $disPow = $valX*$valX + $valY*$valY + $valZ*$valZ;
    $distance = sqrt($disPow);
    
    $FrontRotationWheel = $distance/(6.28*slectLock.Front)*360*MIS.direction;
    $BackRotationWheel = $distance/(6.28*slectLock.Back)*360*MIS.direction;
    
    Lf_Front_JNT_EX.rotateX  = Lf_Front_JNT_EX.rotateX + $FrontRotationWheel;
    Rt_Front_JNT_EX.rotateX  = Rt_Front_JNT_EX.rotateX + $FrontRotationWheel;
    Lf_Back_JNT_EX.rotateX  = Lf_Back_JNT_EX.rotateX + $BackRotationWheel;
    Rt_Back_JNT_EX.rotateX  = Rt_Back_JNT_EX.rotateX + $BackRotationWheel;
    
    //float $disObj = Lf_wheel_front.rotateZ;
    
    
    barBack_JNT.translateY = (Lf_Back_JNT_POI.translateY + Rt_Back_JNT_POI.translateY)/2 + Lf_Back_JNT.translateY;
    barFront_JNT.translateY = (Lf_Front_JNT_POI.translateY + Rt_Front_JNT_POI.translateY)/2 + Lf_Front_JNT.translateY;
    
    float $BBPosY = Lf_Back_JNT_POI.translateY + Lf_Back_JNT.translateY - Rt_Back_JNT_POI.translateY - Rt_Back_JNT.translateY;
    float $BBPosX = Lf_Back_JNT_POI.translateX + Lf_Back_JNT.translateX - Rt_Back_JNT_POI.translateX - Rt_Back_JNT.translateX;
    barBack_JNT.rotateZ = atand($BBPosY/$BBPosX)*1;
    
    float $FBPosY = Lf_Front_JNT_POI.translateY + Lf_Front_JNT.translateY - Rt_Front_JNT_POI.translateY - Rt_Front_JNT.translateY;
    float $FBPosX = Lf_Front_JNT_POI.translateX + Lf_Front_JNT.translateX - Rt_Front_JNT_POI.translateX - Rt_Front_JNT.translateX;
    barFront_JNT.rotateZ = atand($FBPosY/$FBPosX)*1;
    
    chassis_GRP.translateY = (barBack_JNT.translateY + barFront_JNT.translateY)/2;
    float $CLPosY = barBack_JNT.translateY - barFront_JNT.translateY;
    float $CLPosZ = barBack_JNT.translateZ - barFront_JNT.translateZ;
    chassis_GRP.rotateX = atand($CLPosY/$CLPosZ)*-1;
    chassis_GRP.rotateZ = (barBack_JNT.rotateZ + barFront_JNT.rotateZ)/2;
    
    //add wheel Noise
    Lf_Front_JNT_NO.translateY = noise(time*Lf_Front_wheel_C.frequency+0.2)*Lf_Front_wheel_C.sizeY;
    Lf_Front_JNT_NO.translateZ = noise(time*Lf_Front_wheel_C.frequency+0.4)*Lf_Front_wheel_C.sizeZ;
    Rt_Front_JNT_NO.translateY = noise(time*Rt_Front_wheel_C.frequency+0.15)*Rt_Front_wheel_C.sizeY;
    Rt_Front_JNT_NO.translateZ = noise(time*Rt_Front_wheel_C.frequency+0.76)*Rt_Front_wheel_C.sizeZ;
    Lf_Back_JNT_NO.translateY = noise(time*Lf_Back_wheel_C.frequency+0.41)*Lf_Back_wheel_C.sizeY;
    Lf_Back_JNT_NO.translateZ = noise(time*Lf_Back_wheel_C.frequency+0.67)*Lf_Back_wheel_C.sizeZ;
    Rt_Back_JNT_NO.translateY = noise(time*Rt_Back_wheel_C.frequency+0.24)*Rt_Back_wheel_C.sizeY;
    Rt_Back_JNT_NO.translateZ = noise(time*Rt_Back_wheel_C.frequency+0.38)*Rt_Back_wheel_C.sizeZ;
    chassis_UP.translateY = noise(time*Chassis_Con.frequency+0.11)*Chassis_Con.sizeY;
    chassis_UP.translateZ = noise(time*Chassis_Con.frequency+0.76)*Chassis_Con.sizeZ;
    ''')

    def RR_additonalModifly():
        scaleValue =  wheelRadi/17.2453288734
        chaisisPos = xform('chassis_JNT',q = True,t = True,ws = True)
        move(chaisisPos[0],chaisisPos[1],chaisisPos[2],'MIS.scalePivot','MIS.rotatePivot')
        
        rt = 8
        tr = 3*scaleValue
        transformLimits('Chassis_Con',rx  =  (-1*rt,rt),erx = (1, 1))
        transformLimits('Chassis_Con',rx  =  (-1*rt,rt),erx = (1, 1))
        transformLimits('Chassis_Con',ry  =  (-1*rt,rt),ery = (1, 1))
        transformLimits('Chassis_Con',ry  =  (-1*rt,rt),erx = (1, 1))
        transformLimits('Chassis_Con',rz  =  (-1*rt,rt),erx = (1, 1))
        transformLimits('Chassis_Con',rz  =  (-1*rt,rt),erz = (1, 1))
        transformLimits('Chassis_Con',tx  =  (-1*tr,tr),erx = (1, 1))
        transformLimits('Chassis_Con',tx  =  (-1*tr,tr),etx = (1, 1))
        transformLimits('Chassis_Con',ty  =  (-1*tr,tr),erx = (1, 1))
        transformLimits('Chassis_Con',ty  =  (-1*tr,tr),ety = (1, 1))
        transformLimits('Chassis_Con',tz  =  (-1*tr,tr),erx = (1, 1))
        transformLimits('Chassis_Con',tz  =  (-1*tr,tr),etz = (1, 1))
        setAttr('Chassis_Con.sz',k = False,l = True)
        setAttr('Chassis_Con.sy',k = False,l = True)
        setAttr('Chassis_Con.sx',k = False,l = True)
        setAttr('MIS.sz',k = False,l = True)
        setAttr('MIS.sy',k = False,l = True)
        setAttr('MIS.sx',k = False,l = True)
    RR_additonalModifly()

def locators():
    wheels = ls(sl = True)           
    cusName = ['Lf_Front','Rt_Front','Lf_Back','Rt_Back']
    for i,wl in enumerate(wheels):
        minY = xform(wl,q = True,bb = True,ws = True)[1]
        pos = objectCenter(wl,gl = True)
        locPos = (pos[0],minY,pos[2])
        Loc = spaceLocator(n = cusName[i]+'_LOC')[0]
        xform(Loc,t = locPos,ws = True)
        select(cl = True)

#build UI
class FaceUI(object):
    def DisPlay(self):
        faceUI = 'FACE_UI'
        if(window(faceUI,ex = True)):
            deleteUI(faceUI,window = True)
        else:
            window(faceUI,w = 310,h = 400,t = 'FACE_RIG', s = True, tb = True)
            columnLayout('mainLayout') 
               
            button(label = 'createLoctor',c = 'locators()')
            button(label = 'finishSetup',c = 'wheelSetup()')
            
            showWindow(faceUI)






