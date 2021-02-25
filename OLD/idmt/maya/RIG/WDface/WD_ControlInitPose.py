#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
from RIG.face.controlers import CreateControler
import re
import copy

class restoryControlInit():
    def __init__(self):
        self.grp = 'Main_Control_GRP'
        self.allBsCurve = []
        self.auto = False#是否打开自动调整blendShape曲线
        self.main = 'Main_Control_GRP'
        self.head = 'Head_Control_GRP'
        self.BSDict = {u'+translateX':'OUT', u'+translateY':'UP', u'+translateZ':'Front',u'-translateX':'IN', u'-translateY':'DN', u'-translateZ':'BACK'} 
        self.getData()
        
         
    def getData(self):
        self.baseCurve = rig.listConnections(self.main+'.CTRLBaseCurve', s = False, d = True)[0]
        self.origentCurve = rig.listConnections(self.main+'.CTRLOrigenCurve', s = False, d = True)[0]
        self.macro =  rig.listConnections(self.head+'.CTRLMacroCurve', s = False, d = True)
        self.small = rig.listConnections(self.main+'.CTRLCurve', s = False, d = True)
        self.bsCon = rig.listConnections(self.head+'.CTRLBsCurve', s = False, d = True)
        self.bsRoCon = rig.listConnections(self.head+'.CTRLBSRotate', s = False, d = True)
        self.bsDataRV,self.bsDataAtt,self.bsDataValue = self.getBsData()
        self.bsDataSet = set([att for att in self.bsDataAtt])
        
        #得到控制器与曲线点的对应关系
        ControllerDict = dict([(rig.getAttr(con+'.vtxNum'),con) for con in self.small if  not re.match('\w+_Back_\d+M',con)])#创建控制器字典
        nums = [i for i in ControllerDict.keys()]#获得编号
        nums.sort()#对编号进行排序
        self.cons = [ControllerDict[i] for i in nums]#对macro控制器排序
        
    #得到带有blendShape的属性
    def getBsData(self):
        bsDataRV = {}
        bsDataAtt = []
        bsDataValue = []
        BSDict = dict([(self.BSDict[translate],translate) for translate in self.BSDict])
        allBsCons = copy.deepcopy(self.bsCon)
        allBsCons.extend(self.bsRoCon)
        for con in allBsCons:
            RVS = rig.listConnections(con, s = False, d = True, type = 'remapValue')#列出remapValue节点
            if RVS:#如果存在
                bsDataRV[con] = RVS#增加到字典
                for RV in RVS:
                    translate = BSDict[RV.split('_')[-2]][1::]#得到位移属性
                    value = rig.getAttr(RV+'.limitValue')#得到位移值
                    
                    if value < 0:#设置remapValue节点的参数
                        rig.setAttr(RV+'.inputMin',value)
                        rig.setAttr(RV+'.inputMax',0)
                        rig.setAttr(RV+'.value[0].value_Position',0)
                        rig.setAttr(RV+'.value[0].value_FloatValue',1)
                        rig.setAttr(RV+'.value[1].value_Position',1)
                        rig.setAttr(RV+'.value[1].value_FloatValue',0)
                    else:
                        rig.setAttr(RV+'.inputMin',0)
                        rig.setAttr(RV+'.inputMax',value)
                    
                    bsDataAtt.append(con+'.'+translate)
                    bsDataValue.append(value)

                  
        return bsDataRV,bsDataAtt,bsDataValue
    
    def getMovePar(self):
        Tol = 0.0001
        RVname = None
        for conAtt in self.bsDataSet:
            value = rig.getAttr(conAtt)
            if Tol < value or value< -1*Tol:
                if value < 0:
                    conAttrList = conAtt.split('.')
                    con = conAttrList[0]
                    att = self.BSDict['-'+conAttrList[1]]
                    RVname = con+'_'+att+'_RV_Curve' #得到remapValue节点  

                else:
                    conAttrList = conAtt.split('.')
                    con = conAttrList[0]
                    att = self.BSDict['+'+conAttrList[1]]
                    RVname = con+'_'+att+'_RV_Curve' #得到remapValue节点     

                    
        return RVname
                    
                            
    def done(self):
        if (self.getMovePar() and rig.ls(sl = True)):
            blendShapeCurve = self.getMovePar()
            print blendShapeCurve
            
            #选择的控制器
            cons = rig.ls(sl = True)
            for con in cons:
                if 18424 == rig.getAttr(con+'.sign'):
                    for i, currentCon in enumerate(self.cons):
                        if con == currentCon:
                            vtx = '.cv['+str(i)+']'
                            pos = rig.xform(self.origentCurve+vtx, q = True,t = True, ws = True)
                            rig.xform(blendShapeCurve+vtx, t = pos ,ws = True)
                