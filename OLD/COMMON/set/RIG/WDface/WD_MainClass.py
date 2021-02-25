#-*- coding: utf-8 -*-
import maya.OpenMaya as om
import maya.cmds as rig
import copy
import re
import pickle
import tempfile

#===============================================================================
# 增加并连接属性
#===============================================================================
class connectAttribute():
    def __init__(self):
        self.force = False
        self.dv = 1
        self.attrType = 'long'
        self.sourceAttr = 'testA'
        self.targetAttr = 'visibility'
        
    def connect(self,sourceObj,*targetObj):

        if not rig.attributeQuery(self.sourceAttr,node = sourceObj,ex = True):
            rig.addAttr(sourceObj,at = self.attrType,ln = self.sourceAttr , dv = self.dv)
        
        typeName = type(targetObj[0]).__name__
        if 'str' == typeName:
            targetObj = targetObj[0]
            if not rig.attributeQuery(self.targetAttr,node = targetObj,ex = True):
                rig.addAttr(targetObj,at = self.attrType,ln = self.targetAttr)
            rig.connectAttr(sourceObj+'.'+self.sourceAttr, targetObj+'.'+self.targetAttr, f = self.force)
        if 'list' == typeName:
            targetObj = targetObj[0]
            for obj in targetObj:
                if not rig.attributeQuery(self.targetAttr,node = obj,ex = True):
                    rig.addAttr(obj,at = self.attrType,ln = self.targetAttr)
                rig.connectAttr(sourceObj+'.'+self.sourceAttr, obj+'.'+self.targetAttr, f = self.force)

#------------------------------------------------------------------------- 平均曲线上
class curveAverage():
    def __init__(self):
        pass
    
    def getInfo(self,objShape,num):
        ListShape = om.MSelectionList()
        ListShape.add(objShape)
        curveNode = om.MDagPath()
        ListShape.getDagPath( 0, curveNode)
        CurveMFn = om.MFnNurbsCurve(curveNode)
        
        curveLength = CurveMFn.length()
        averageNum = curveLength/(num - 1)
        pnt = om.MPoint()
        deLength = 0
        
        paramer = []
        points = []
        for i in range(num):
            curParam = CurveMFn.findParamFromLength(deLength)
            paramer.append(curParam)
            CurveMFn.getPointAtParam(curParam,pnt,om.MSpace.kWorld)
            points.append((pnt.x,pnt.y,pnt.z))
            deLength += averageNum
        
        return paramer,points

#------------------------------------------------------------------------ 获得变形节点
class getDeformerNode():
    def __init__(self):
        self.Deform = 'skinCluster'
    
    def getInfo(self,obj):
        skinCls = rig.ls(rig.listHistory(obj,pdo = True),type = self.Deform)
        if skinCls:
            return skinCls[0] 
        else:
            return False
        
        
#===============================================================================
# 镜像控制器
#===============================================================================
class BlendShapeController():
    def __init__(self):
        self.grp = 'Head_Control_GRP'
        self.baseCurve = ''
        self.origencurve = ''
        self.axis = 'X'
        self.direction = True
        self.select = False
        self.conType = 'small'
        
        self.axisNum = {'X':0,'Y':1,'Z':2}
        self.rigging = False
        self.execute = True
    def runMirror(self,CTRLCurves):
        num = self.axisNum[self.axis]
        
        if self.direction:
            LfRt = 'Lf'
        else:
            LfRt = 'Rt'
        Cons = [con for con in CTRLCurves if re.match('\A'+LfRt+'', con)] 
        for con in Cons:
            #----------------------------------------------------- 镜像transform信息
            pos = rig.xform(con, q = True, t = True, ws = True)
            ro = rig.xform(con, q = True, ro = True, ws = True)
            
            newPos = []#存放新的位置信息
            newRo = []#存放新的旋转信息
            for i,p in enumerate(pos):
                if num == i:
                    newPos.append(p*-1)
                    newRo.append(ro[i])
                else:
                    newPos.append(p)
                    newRo.append(ro[i]*-1)
            
            #得到新的控制器名字
            if LfRt == 'Lf':
                newCon = re.compile('\A'+LfRt+'').sub('Rt',con)
                
                if (not self.rigging) and self.execute:
                    rig.setAttr(newCon+'.scale'+self.axis,-1)#设置对称
            else:
                newCon = re.compile('\A'+LfRt+'').sub('Lf',con)
            
            rig.xform(newCon, t = newPos, ws = True)#重新设置位置  
            
            if (not self.rigging) and self.execute: 
                rig.xform(newCon, ro = newRo, ws = True)#重新设置旋转      
            
            #--------------------------------------------------------- 镜像shape信息
            origenShape = rig.listRelatives(con,s = True)
            if origenShape:#如果有shape节点
                for sp in origenShape:
                    #得到新的控制器名字
                    if LfRt == 'Lf':
                        newShape = re.compile('\A'+LfRt+'').sub('Rt',sp)
                    else:
                        newShape = re.compile('\A'+LfRt+'').sub('Lf',sp)
                        
                    origenVtxs = [rig.xform(vtx, q = True, t = True, wd = True) for vtx in rig.ls(sp+'.cv[*]',fl = True)]
                    for i,vtx in enumerate(origenVtxs):
                        rig.xform(newShape+'.cv['+str(i)+']', t = vtx, wd = True)#重新设置位置
    
    def blendShapes(self):
        small = rig.listConnections(self.grp+'.CTRLCurve', s = False, d = True)
        #得到控制器与曲线点的对应关系
        ControllerDict = dict([(rig.getAttr(con+'.vtxNum'),con) for con in small if  not re.match('\w+_Back_\d+M',con)])#创建控制器字典
        nums = [i for i in ControllerDict.keys()]#获得编号
        nums.sort()#对编号进行排序
        cons = [ControllerDict[i] for i in nums]#对small控制器排序

        duDict =  {}
        for i,con in enumerate(cons):
            if re.match('\ALf', con):
                Index = cons.index(con)
                NCon = re.compile('\ALf').sub('Rt',con)
                oppositeIndex = cons.index(NCon)
                duDict[Index] = oppositeIndex
            elif re.match('\ARt', con):
                Index = cons.index(con)
                NCon = re.compile('\ARt').sub('Lf',con)
                oppositeIndex = cons.index(NCon)
                duDict[Index] = oppositeIndex
            else:
                duDict[i] = i               
        
        
        LR = {'Lf':'Rt','Rt':'Lf'}
        InOut ={'Lf':'IN','Rt':'OUT'}
        BackFront = {'Lf':'BACK', 'Rt':'Front'}
        #得到blendShape曲线
        allBsCurve = rig.listRelatives(self.grp+'_BSCurve ', ad = True, c = True)
        allCurve = rig.ls(allBsCurve,type = 'transform')
        
        

        #镜像的轴向
        num = self.axisNum[self.axis]
        #镜像的方向
        if self.direction:
            LfRt = 'Lf'
        else:
            LfRt = 'Rt'
        
        #对所有blendShape曲线进行分析    
        for cur in allCurve:
            if cur.split('_')[0] != LR[LfRt]:
                origenCurve = copy.deepcopy(cur)#原始的blendShape曲线
                if re.match('\ALf_|\ARt_', cur):
                    newCurve = re.compile('\A'+LfRt+'').sub(LR[LfRt],cur)

                else:
                    if re.match('\w+_M_'+InOut[LR[LfRt]]+'_RV_Curve\Z', cur):
                        newCurve = re.compile(InOut[LR[LfRt]]+'_RV_Curve\Z').sub(InOut[LfRt]+'_RV_Curve',cur)
                    
                    elif re.match('\w+_Rotation_'+BackFront[LR[LfRt]]+'_RV_Curve\Z', cur):
                        newCurve = re.compile(BackFront[LR[LfRt]]+'_RV_Curve\Z').sub(BackFront[LfRt]+'_RV_Curve',cur)
                    
                    elif re.match('\w+_'+InOut[LfRt]+'_RV_Curve\Z', cur):
                        pass  
                      
                    else:
                        newCurve = cur
                    
                    
                #原始blendShape曲线的位置信息
                newPos = [rig.xform(vtx, q = True, t = True, ws = True) for vtx in rig.ls(origenCurve+'.cv[*]',fl = True)]

                if re.match('(\ALf_|\ARt_)', cur):#是否为左边或右边的blendShape曲线
#                    print origenCurve+'--------------------->'+newCurve
                    for i,con in enumerate(cons):
                        nPos = newPos[i]
                        nPos[num] = nPos[num]*-1
                        pos = nPos
                        rig.xform(newCurve+'.cv['+str(duDict[i])+']', t = pos, ws = True)
                       
  
                    
                else:#曲线为一条曲线，修改这条曲线的一边即可
                    if re.match('\w+_M_'+InOut[LR[LfRt]]+'_RV_Curve\Z', cur):
#                        print 'Mirror:'+origenCurve+'--------------------->'+newCurve
                        for con in cons:
                            i = cons.index(con)
                            nPos = newPos[i]
                            nPos[num] = nPos[num]*-1
                            pos = nPos
                            
                            rig.xform(newCurve+'.cv['+str(duDict[i])+']', t = pos, ws = True)
                            
                            
                    elif re.match('\w+_Rotation_'+BackFront[LR[LfRt]]+'_RV_Curve\Z', cur):
#                        print 'rotation:'+origenCurve+'--------------------->'+newCurve
                        for con in cons:
                            i = cons.index(con)
                            nPos = newPos[i]
                            nPos[num] = nPos[num]*-1
                            pos = nPos
                            
                            rig.xform(newCurve+'.cv['+str(duDict[i])+']', t = pos, ws = True)
                    
                    elif re.match('\w+_'+InOut[LfRt]+'_RV_Curve\Z', cur) or re.match('\w+_Rotation_'+BackFront[LfRt]+'_RV_Curve\Z', cur):
                        pass  
                       
                            
                    else:
                        print 'else:'+origenCurve+'--------------------->'+newCurve
                        halfCon = [con for con in cons if re.match('\A'+LfRt+'', con)]
                        for con in halfCon:
                            i = cons.index(con)
                            nPos = newPos[i]
                            nPos[num] = nPos[num]*-1
                            pos = nPos
                            
                            rig.xform(newCurve+'.cv['+str(duDict[i])+']', t = pos, ws = True)
                    
           
            
                    
                   
    #--------------------------------------------------------------------- 镜像控制器
    def Mirror(self):
        if 'small' == self.conType:
            CTRLCurves = rig.listConnections(self.grp+'.CTRLCurve',s = False, d = True)
            self.runMirror(CTRLCurves)
            
        if 'macro' == self.conType:
            CTRLBsCurves = rig.listConnections(self.grp+'.CTRLBsCurve',s = False, d = True)
            CTRLMacroCurves = rig.listConnections(self.grp+'.CTRLMacroCurve',s = False, d = True)
            CTRLJoint = rig.listConnections(self.grp+'.CTRLJoint',s = False, d = True)
            
            self.runMirror(CTRLBsCurves)
            self.runMirror(CTRLMacroCurves)
            
            if not self.rigging:
                self.runMirror(CTRLJoint)
            
        if 'blendShape' == self.conType:
            self.blendShapes()        
        
        if 'eye' == self.conType:
            CTRLCurves = rig.listConnections(self.grp+'.CTRLCurve',s = False, d = True)
            CTRLJoint = rig.listConnections(self.grp+'.CTRLJoint',s = False, d = True)
            
            self.execute = False
            self.runMirror(CTRLCurves) 
            
            if not self.rigging:
                self.runMirror(CTRLJoint)
            
        if 'ear' == self.conType:

            CTRLJoint = rig.listConnections(self.grp+'.CTRLJoint',s = False, d = True)
            
            if not self.rigging:
                self.runMirror(CTRLJoint)
            
    #----------------------------------------- 新建blendColor节点，限制位移，连接BlendShape.
    def startLink(self):
        CTRLBsCurves = rig.listConnections(self.grp+'.CTRLBsCurve',s = False, d = True)
        CTRLMacroCurves = rig.listConnections(self.grp+'.CTRLMacroCurve',s = False, d = True)
    

        
    def done(self):
        self.startLink()
        
        
#===============================================================================
# 显示或隐藏控制器，调整控制器大小，恢复控制器初始值        
#===============================================================================
class changeController():
    def __init__(self):
        self.main = 'Main_Control_GRP'
        self.head = 'Head_Control_GRP'
        self.size = 1
        self.operate = ''
#        CTRLBsCurves = rig.listConnections(self.grp+'.CTRLBsCurve',s = False, d = True)
#        CTRLMacroCurves = rig.listConnections(self.grp+'.CTRLMacroCurve',s = False, d = True)
    
    def selectTypes(self,conType):
        if 'small' == conType:
            self.small()
        if 'macro' == conType:
            self.macro()
        if 'main' == conType:
            self.mains()
        if 'cross' == conType:
            self.cross()
        
    def small(self):
        smallCons = rig.listConnections(self.main+'.CTRLCurve',s = False, d = True)
        if 'hide' ==  self.operate:
            self.hides(smallCons, 0)
        if 'changeSize' == self.operate:
            self.changeSize(smallCons,self.size)
        if 'show' == self.operate:
            self.hides(smallCons, 1)
        if 'restore' == self.operate:
            pass
        
    def macro(self):
        macroCons = rig.listConnections(self.head+'.CTRLMacroCurve',s = False, d = True)
        if 'hide' ==  self.operate:
            self.hides(macroCons, 0)
        if 'changeSize' == self.operate:
            self.changeSize(macroCons,self.size)
        if 'show' == self.operate:
            self.hides(macroCons, 1)
        if 'restore' == self.operate:
            pass
        
    
    def mains(self):
        mainCons = rig.listConnections(self.head+'.CTRLBsCurve',s = False, d = True)
        if 'hide' ==  self.operate:
            self.hides(mainCons, 0)
        if 'changeSize' == self.operate:
            self.changeSize(mainCons,self.size)
        if 'show' == self.operate:
            self.hides(mainCons, 1)
        if 'restore' == self.operate:
            pass
        
    
    def cross(self):
        mainCons = rig.listConnections(self.head+'.CTRLBsCurve',s = False, d = True)
        if 'hide' ==  self.operate:
            self.hideShape(mainCons, 1)
        if 'changeSize' == self.operate:
            self.changeSize(mainCons,self.size)
        if 'show' == self.operate:
            self.hideShape(mainCons, 0)
        if 'restore' == self.operate:
            pass
        
    
    #隐藏物体父物体
    def hides(self,smallCons,value):
        for con in smallCons:
            conParent = rig.listRelatives(con,p = True)[0]
            
            P =  rig.listConnections(conParent+'.visibility', s = True, d = False, p = True)
            if P:
                P1 = rig.listConnections(P, s = True, d = False, p = True)
                if P1:
                    if not rig.getAttr(P1[0], l = True):
                        rig.setAttr(P1[0], value)
                else:
                    if not rig.getAttr(P,l = True):
                        rig.setAttr(P[0], value)
                    
                    
            else:
                print 'None'
                if not rig.getAttr(conParent+'.visibility', l = True):
                    rig.setAttr(conParent+'.visibility', value )
                    
    #隐藏形节点
    def hideShape(self,smallCons,value):
        for con in smallCons:
            allShapes = rig.listRelatives(con, s = True)
            if allShapes and len(allShapes) == 2:
                conShape,conShapeCross = rig.listRelatives(con, s = True)
                rig.setAttr(conShape+'.visibility', value)
                rig.setAttr(conShapeCross+'.visibility', 1-value)
    
    def changeSize(self,smallCons,size):
        for con in smallCons:
            pos = rig.xform(con, q = True, t = True, ws = True)
            conShape = rig.listRelatives(con,s = True)[0]
            
            rig.scaleComponents( size, size, size, conShape+'.cv[*]', pivot = pos)
            

    def show(self):
        pass
    
    def restore(self):
        pass
    
    
    
#===============================================================================
# 生成设置组
#===============================================================================
class getRigGrp():
    def __init__(self):
        self.grp = 'Head_FaceRig_Control_GRP'
    

    
    def createGrp(self):
        if not rig.objExists(self.grp):
            grpName = rig.group(empty = True, n = self.grp)
            return grpName
        else:
            return self.grp
        
       
#===============================================================================
# freeze物体       
#===============================================================================
class freezeObj():
    def __init__(self):
        self.t = True
        self.r = True
        self.s = True
        self.parents = []
        self.pos = []
        
    def upParent(self):
        for obj in self.agrs:
            objParent = rig.listRelatives(obj, p = True)
            if objParent:
                rig.parent(obj, w = True)
                self.parents.append(objParent[0])
                self.pos.append(rig.xform(obj, q = True, t = True, ws = True))
            else:
                self.parents.append('')
                self.pos.append(rig.xform(obj, q = True, t = True, ws = True))    
    
    def freeze(self, *agrs):
        self.agrs = agrs[0]
        self.upParent()
        for i,obj in enumerate(self.agrs):
            rig.xform(obj, t = (0.0,0.0,0.0), ws = True)
            rig.makeIdentity(obj, apply = True, s = self.s, t = self.t, r = self.r)
            rig.xform(obj, t = self.pos[i], ws = True)   
                     
            if self.parents[i]:
                rig.parent(obj, self.parents[i])
            
    
#===============================================================================
# 增加空组    
#===============================================================================
class addGrp():
    def __init__(self):
        pass
    
    def grp(self,con,key):
        conParent = rig.listRelatives(con, p = True)
        conMat = rig.getAttr(con+'.worldMatrix')
        grpUp = rig.group(empty = True, n = con+'_'+key+'_GRP_Up')
        grpTop = rig.group(grpUp, n = con+'_'+key+'_GRP_Top')
        rig.xform(grpTop, m = conMat)
        rig.parent(con, grpUp)
        
        if conParent:
            rig.parent(grpTop, conParent[0])
            
        return grpTop
        
        
#===============================================================================
# 获得两个物体之间的距离       
#===============================================================================
class distance():
    def __init__(self):
        self.res = ''
        self.tar = ''
        self.default = 1.0
        
    def getDistance(self, res, tar):
        resource = om.MVector(res[0], res[1], res[2])
        target = om.MVector(tar[0], tar[1], tar[2])
        dis = (resource - target).length()
        print dis
        return dis
    
    def getScale(self, resObj, tarObj, origenDistance = 1.0):
        self.default = origenDistance
        scale = (self.getDistance(rig.xform(resObj, q = True, t = True, ws = True), rig.xform(tarObj, q = True, t = True, ws = True)))/self.default
        return scale
    
    
    
#===============================================================================
# 对物体名字进行排序
#===============================================================================
class order():
    def __init__(self):
        pass
        
    def startOrder(self, objs = []):
        origenObjs = objs
        
        orderDict = {}
        for obj in origenObjs:
            objIndexs = int(re.findall('\d+', obj.split('_')[-1])[0])
            orderDict[objIndexs] = obj
        

        newObjs = [orderDict[i] for i in orderDict]
        
        return newObjs
            

#===============================================================================
# 增加set       
#===============================================================================
class addSets():
    def __init__(self):
        self.faceSets = 'face_Influences_Sets'
        self.componentSets = 'eyeSets'
        
    def addMainSets(self):
        if not rig.objExists(self.faceSets):
            rig.createNode('objectSet', n = self.faceSets)
        
        
    def startAdd(self, influence = []):
        self.addMainSets()
        if rig.objExists(self.componentSets):
            rig.sets(influence, e = True, addElement = self.componentSets)
        
        else:
            setName = rig.createNode('objectSet', n = self.componentSets)
            rig.sets(influence, e = True, addElement = setName)
            
            rig.sets(setName, e = True, addElement = self.faceSets)
          
#===============================================================================
# 对物体进行蒙皮        
#===============================================================================
class skinClusterObj():
    def __init__(self):
        pass
    
    def skinClusters(self, infs, skinObjs):
        print infs,skinObjs
        jnts = []
        objs = []
        for inf in infs:
            if rig.nodeType(inf) == 'joint':
                jnts.append(inf)
            else:
                objs.append(inf)
        
        for obj in skinObjs:
            skin = rig.skinCluster(jnts, obj, n = obj+'_Skin', tsb = True)[0]
            if objs:
                rig.setAttr(skin+'.useComponents', True)
                rig.skinCluster(skin, e = True, ai = objs, ug = True)
        
        
#===============================================================================
# 得到set中的所有元素       
#===============================================================================
class getSetElements():
    def __init__(self):
        self.setName = 'face_controls_Sets'
    
    def getEle(self):
        allObj = []
        

        objSets = rig.sets(self.setName, q = True)
        for s in objSets:
            objs = rig.sets(s, q = True)
            allObj.extend(objs)

        return allObj
    
    
#===============================================================================
# 得到所有transform       
#===============================================================================
class getAllTransform():
    def __init__(self):
        self.grpName = 'Head_FaceRig_Control_GRP'
        self.removeObj = []
    
    def getTransform(self):
        allChilds = rig.listRelatives(self.grpName, c = True, ad = True)
        allTransforms = rig.ls(allChilds, type = 'transform')
        
        if self.removeObj:
            for obj in self.removeObj:
                if obj in allTransforms:
                    allTransforms.pop(allTransforms.index(obj))
        
        return allTransforms


#===============================================================================
# 将信息写到属性上 
#===============================================================================
class convertData():
    def __init__(self):
        self.filePath =  tempfile.gettempdir()+'/PosFile.txt' 

    def getAttrData(self,attrName):
        con, attr = attrName.split('.')
        if rig.attributeQuery(attr, node = con, ex = True):
            newFile = open(self.filePath,'w')
            newFile.write(rig.getAttr(attrName))
            newFile.close()
            readFile = open(self.filePath,'r')
            dbase = pickle.load(readFile)
            readFile.close()
            
            return dbase
    
    def setAttrData(self,attrName,data):
        con, attr = attrName.split('.')
        if not rig.attributeQuery(attr, node = con, ex = True):
            rig.addAttr(con,dt = 'string',ln = attr)
            
        newFile = open(self.filePath,'w')
        pickle.dump(data,newFile)
        newFile.close()
        getData = open(self.filePath,'r')
        getDate = getData.read()
        getData.close()
        rig.setAttr(attrName,getDate,type = 'string')




 