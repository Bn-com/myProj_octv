#-*- coding: utf-8 -*-

import maya.cmds as rig
import RIG.WDface.WD_MainClass as CA
import re

class RigStart():
    def __init__(self):
        self.model = []
        self.grp = 'Main_Control_GRP'
        self.baseCurve = 'Main_Base_Curve'
        self.origenCurve = 'Main_Origen_Curve'
        self.numToController = {}#建立控制器与loft曲线点之间的字典
        self.curveToController = {}#建立控制器与曲线点之间的字典
        print 'mainControl'
    
    #-------------------------------------------------------------------- 创建基础曲线并完成曲线的连接工作
    def createBaseCurve(self):
        #-------------------------------------------------------------- 创建Base曲线
        ControllerDict = dict([(rig.getAttr(con+'.vtxNum'),con) for con in rig.listConnections(self.grp+'.CTRLCurve', s = False, d = True) if  not re.match('\w+_Back_\d+M',con)])#创建控制器字典
        nums = [i for i in ControllerDict.keys()]#获得编号
        nums.sort()#对编号进行排序
        
        curvePos = [rig.xform(ControllerDict[num],q = True,t = True,ws = True)for num in nums]#获得位置信息
        self.curveToController = dict([(ControllerDict[num],i) for i,num in enumerate(nums)])#建立base曲线点与控制器的字典
        TempCurve = rig.curve(d = 1,p = curvePos)#生成曲线
        baseCurve = rig.rename(TempCurve,self.baseCurve)#重命名曲线
        origenCurve = rig.duplicate(baseCurve,n = self.origenCurve)[0]#原始曲线
    
        #-------------------------------------------------- 创建pointOnCurveInfo节点
        baseCurveShape = rig.listRelatives(baseCurve,s = True)[0]
        NPO = rig.createNode('nearestPointOnCurve',n = self.grp+'_NPO',ss = True)#创建nearestPointOnCurve节点
        rig.connectAttr(baseCurveShape+'.worldSpace[0]',NPO+'.inputCurve')#连接属性
        
        for i,num in enumerate(nums):
            con = ControllerDict[num]#得到控制器名字
            pos = curvePos[i]#得到控制器文件信息
            #设置最近点的parameter值
            rig.setAttr(NPO+'.inPositionX',pos[0])
            rig.setAttr(NPO+'.inPositionY',pos[1])
            rig.setAttr(NPO+'.inPositionZ',pos[2])
            P = rig.getAttr(NPO+'.parameter')
            
            #创建pointOnCurveInfo节点
            POCI = rig.createNode('pointOnCurveInfo',n = con+'_POCI')
            rig.connectAttr(baseCurveShape+'.worldSpace[0]',POCI+'.inputCurve')
            rig.setAttr(POCI+'.parameter',P)
            
            #创建并连接空组
            posGrp = rig.group(empty = True,n  = con+'_Position_GRP')
            Grp = rig.group(posGrp,n  = con+'_GRP')
            rig.connectAttr(POCI+'.position',Grp+'.translate')
        
        #--------------------------------------------------------- 连接out曲线.create属性
        outCurve = [cur for cur in  rig.listConnections(self.grp+'.LoftCurve', s = False, d = True) if re.match('\Aout_',cur)]
        for cur in  outCurve:
            inputCurve = rig.duplicate(cur,n = cur+'_Input')[0]#复制InputCurve曲线
            inputCurveShape = rig.listRelatives(inputCurve,s = True)[0]#得到形节点
            print inputCurve
            conShape = rig.listRelatives(cur,s = True)[0]#得到形点
            cons = rig.listConnections(conShape,s = True, d = False)#获得与它相连的控制器
            
            inputPlus = []#用于存放被连接的控制点的数值
            for con in cons:
                plus = rig.listConnections(con+'.translate',s = False, d = True, p = True)[0]
                self.numToController[plus] = con #增加到字典
                inputPlus.append(plus)
                rig.disconnectAttr(con+'.translate',plus)#断开连接
                parentGrp = rig.listRelatives(con,p = True)[0]#获得控制器以前在它什么的物体
                rig.parent(con,con+'_Position_GRP')#P给上面的组
                rig.parent(con+'_GRP',parentGrp)#放回以前层级
                rig.connectAttr(con+'_GRP.translate',inputCurveShape+'.'+plus.split('.')[-1])#与新复制出来的曲线的controlPoints属性连接
        
            rig.connectAttr(inputCurveShape+'.worldSpace[0]',conShape+'.create')#create属性连接
            
            for i,con in enumerate(cons):
                rig.connectAttr(con+'.translate',inputPlus[i])#重新连接
                
                
        #--------------------------------------------------------- 连接in曲线.create属性
        inCurve = [cur for cur in  rig.listConnections(self.grp+'.LoftCurve', s = False, d = True) if re.match('\Ain_',cur)]
        for cur in  inCurve:
            inputCurve = rig.duplicate(cur,n = cur+'_Input')[0]#复制InputCurve曲线
            inputCurveShape = rig.listRelatives(inputCurve,s = True)[0]#得到形节点
            print inputCurve
            conShape = rig.listRelatives(cur,s = True)[0]#得到形点
            cons = rig.listConnections(conShape,s = True, d = False)#获得与它相连的控制器
            
            inputPlus = []#用于存放被连接的控制点的数值
            for con in cons:
                conMatrix = rig.getAttr(con+'.worldMatrix')
                plus = rig.listConnections(con+'.translate',s = False, d = True, p = True)[0]
                inputPlus.append(plus)
                rig.disconnectAttr(con+'.translate',plus)#断开连接
                parentGrp = rig.listRelatives(con,p = True)[0]#获得控制器以前在它什么的物体
                
                posGrp = rig.group(empty = True,n  = con+'_Position_GRP')#创建空组
                Grp = rig.group(posGrp,n  = con+'_GRP')#创建空组
                rig.xform(Grp,m = conMatrix)#设置空组到以前的控制器位置
                
                rig.parent(con,posGrp)#P给上面的组
                rig.parent(Grp,parentGrp)#放回以前层级
                
                rig.connectAttr(con+'_GRP.translate',inputCurveShape+'.'+plus.split('.')[-1])#与新复制出来的曲线的controlPoints属性连接
        
            rig.connectAttr(inputCurveShape+'.worldSpace[0]',conShape+'.create')#create属性连接
            
            for i,con in enumerate(cons):
                rig.connectAttr(con+'.translate',inputPlus[i])#重新连接
    #整理层级            
    def Groups(self):
        self.grpName = self.grp
        self.connectAddAttr(self.baseCurve, 'CTRLBaseCurve')
        self.connectAddAttr(self.origenCurve, 'CTRLOrigenCurve')  
        
        curveGrp = rig.group(self.baseCurve,self.origenCurve,n = self.grp+'_CTRLMainCurve')  
        rig.setAttr(curveGrp+'.template', 1) 
        rig.parent(curveGrp, self.grp)   
        
    def connectAddAttr(self,AddObj,Attr):#增加并连接属性
        rig.addAttr(AddObj,at = 'long',ln = Attr)
        if not rig.attributeQuery(Attr,node = self.grpName,ex = True):
            rig.addAttr(self.grpName,at = 'long',ln = Attr)
        rig.connectAttr(self.grpName+'.'+Attr,AddObj+'.'+Attr)  
    
    
    #连接隐藏控制器
    def linkVis(self):
        allCons = rig.listConnections(self.grp+'.CTRLCurve', s = False, d = True)
        frontGrp = []
        backGrp = []
        for con in allCons:
            grp = rig.listRelatives(con, p = True)[0]
            if re.match('\w+_Back_\d+M',con):
                backGrp.append(grp)               
            else:
                frontGrp.append(grp)
                
        connectVisibility = CA.connectAttribute()
        connectVisibility.sourceAttr = 'smallVis'
        connectVisibility.connect(self.grp, frontGrp)
        connectVisibility.sourceAttr = 'smallBackVis'
        connectVisibility.connect(self.grp, backGrp)
        
    #恢复轴心点
    def centerPivot(self):
        allMesh = rig.listConnections(self.grp+'.LoftMesh', s = False, d = True)
        for loftMesh in allMesh:
            rig.xform(loftMesh,p = True, cp = True)
    
    #创建Set
    def skinSet(self):
        InfSets = CA.addSets()
        InfSets.componentSets = 'Face_Main_Sets'
        infs = rig.listConnections(self.grp+'.LoftMesh', s = False, d = True)
        InfSets.startAdd(infs)
        
    #增加rigging属性
    def addRiggingAttr(self):
        rig.addAttr(self.grp, at = 'long', ln = 'rigging', dv = 1)    
                      
    def done(self):
        self.addRiggingAttr()
        self.createBaseCurve()
        self.Groups()
        self.linkVis()
        self.centerPivot()
        self.skinSet()
    
