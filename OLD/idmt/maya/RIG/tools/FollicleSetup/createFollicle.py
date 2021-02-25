#-*- coding: utf-8 -*-
from maya.cmds import *
import re
import maya.OpenMaya as om
from RIG.face.controlers import CreateControler


class SK_CreateJontCTRL_UI(object):
    def __init__(self):
        self.curve = ''
        self.curveShape = ''
        self.num = 50
        self.allParams = []
        self.allCons = []
        self.controlType = CreateControler()
        self.ConName = 'CTRL0'
        self.displayUI()
           
    def displayUI(self):
        IDMTRigGUI='roma_animCurve'
        if window(IDMTRigGUI,exists=True):
            deleteUI(IDMTRigGUI)
 
        self.mainUI = window(IDMTRigGUI,title= u'生成曲线',menuBar=True,minimizeButton=True,maximizeButton=True)
        self.mainFLY = columnLayout()

        rowColumnLayout(numberOfColumns=2,columnWidth = [(1,100),(2,150)],columnAttach = (2,'both',0))
        text(u'载入Ploygon物体:')
        self.numIF = intField(v = 5)
        setParent(self.mainFLY)
        
        separator(w = 312,h=15,style='in')
        button(l = u'生成所有',c = lambda x:self.createControlSetup())
        button(l = u'生成选择的',c = lambda x:self.createSelectControlSetup())
        button(l = u'创建Locator控制',c = lambda x:self.createSelectLocatorSetup())        
        button(l = u'创建选择的毛囊',c = lambda x:self.createSelectFollicle())        
        button(l = u'创建选择的毛囊nurbsSurface',c = lambda x:self.createSelectFollicleNurbsSurface())    
        button(l = u'创建拉伸IK',c = lambda x:stretchIK())
        showWindow(self.mainUI)  
#        window(self.mainUI,e=True,wh=(325,350))
    
    def createCurve(self):#生成曲线控制器
        allControl = []
        Points,Params = GetCurvePosition(self.curve, self.num)
        print Params
        if objExists(self.ConName+'_0_Grp'):
            currentNum = re.search('[0-9]+', self.ConName).group()
            self.ConName = self.ConName.replace(currentNum, str(int(currentNum) + 1))
        for i,pos in enumerate(Points):
            con = self.controlType.SK_b01(self.ConName+'_'+str(i))
            xform(con, t = pos, ws = True)
            allControl.append(con)
            
        return allControl 
    
        
    def setToShape(self):#设置曲线shape节点
        Shape = listRelatives(self.curve, s = True)[0]
        self.curveShape = Shape
        
    def setPanel(self):
        self.num = intField(self.numIF, q = True, v = True)
                 
    def createControlSetup(self):
        slCurves = ls(sl = True)
        self.curve = slCurves[0]
        self.setToShape()
        self.setPanel()
        self.allCons = self.createCurve()
        self.getParams( self.allCons )
        self.createPointOnCurveInfo()


            
    def createSelectControlSetup(self):#创建选择的
        slCurves = ls(sl = True)
        self.curve = slCurves.pop(0)
        self.setToShape()
#        self.allCons = self.createCurve()
        self.allCons = slCurves
        self.getParams( self.allCons )
        self.createPointOnCurveInfo()

    def createSelectLocatorSetup(self):#创建Locator控制
        slCurves = ls(sl = True)
        self.curve = slCurves.pop(0)
        self.setToShape()
#        self.allCons = self.createCurve()
        self.allCons = slCurves
        self.getParams( self.allCons )
        self.createLocator()
        
    
    def createLocator(self):#创建pointCurveConstraint节点
        for i,param in enumerate(self.allParams):
            print "---------"
#            pointCurveConstraint( 'curve1.un[1.0]', ch=True, w=1.0 )

            Locator = pointCurveConstraint(self.curve+'.u['+str(param)+']', ch = True, w = 1)
            LC = rename(Locator[0],self.allCons[i]+'_LC')
            parent(LC, self.allCons[i] )
            
            
    def createSelectFollicle(self):#通过选择的控制器生成毛囊
        slCurves = ls(sl = True)
        self.curve = slCurves.pop(0)
        self.setToShape()
#        self.allCons = self.createCurve()
        self.allCons = slCurves
        self.follicle()

    def createSelectFollicleNurbsSurface(self):#在nurbsSurface上通过选择的控制器生成毛囊
        slCurves = ls(sl = True)
        self.curve = slCurves.pop(0)
        self.setToShape()
#        self.allCons = self.createCurve()
        self.allCons = slCurves
        self.nurbsSurfaceFollicle()
        
        
    def follicle(self):#生成毛囊
        FOLS = []
        ClosestPoint = om.MPoint()
        closestPolygon = None
        uvSet = None
        util = om.MScriptUtil()
        util.createFromList([0.0, 0.0], 2)
        uvPoint = util.asFloat2Ptr()

        
        ListShape = om.MSelectionList()
        print self.curveShape
        ListShape.add(self.curveShape)
        curveNode = om.MDagPath()
        ListShape.getDagPath( 0, curveNode)
        CurveMFn = om.MFnMesh(curveNode)
        
        for con in self.allCons:
            #获得UV
            pos = xform(con,q = True,t = True,ws = True)
            Point = om.MPoint(pos[0], pos[1], pos[2])
            CurveMFn.getClosestPoint(Point, ClosestPoint, om.MSpace.kWorld, closestPolygon)
            CurveMFn.getUVAtPoint(ClosestPoint, uvPoint, om.MSpace.kWorld, uvSet, closestPolygon)
            U = om.MScriptUtil.getFloat2ArrayItem( uvPoint, 0, 0 )
            V = om.MScriptUtil.getFloat2ArrayItem( uvPoint, 0, 1 )
            
            
            #创建毛囊
            FOLShape = createNode('follicle',n = con.replace('_P','_'+con)+'_FOLShape',ss = True)
            hide(FOLShape)
            connectAttr(self.curveShape+'.worldMesh[0]',FOLShape+'.inputMesh')
            FOL = listRelatives(FOLShape,p = True)[0]
            
                           
            connectAttr(self.curveShape+'.worldMatrix[0]',FOL+'.inputWorldMatrix')
            
            newFol = rename(FOL,con.replace('_P','_'+con)+'_FOL')
            connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
            connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
            setAttr(FOLShape+'.parameterU',U)
            setAttr(FOLShape+'.parameterV',V)
            setAttr(FOLShape+'.simulationMethod',0)
            
            parent(con, newFol)
            xform(con, t = (0, 0 ,0), wd = True)
            xform(con, ro = (0, 0 ,0), wd = True)
            conGRP = group(con, n = con+'_Trans_GRP')
            group(conGRP, n = con+'_UP_GRP')
            FOLS.append(newFol)
            
        return FOLS
        
    def nurbsSurfaceFollicle(self):#生成毛囊在nurbs面上
        FOLS = []
        ClosestPoint = om.MPoint()
        closestPolygon = None
        uvSet = None
#        util = om.MScriptUtil()
#        util.createFromList([0.0, 0.0], 2)
#        uvPoint = util.asFloat2Ptr()
        Uutil = om.MScriptUtil()
        UPtr = Uutil.asDoublePtr()
        Vutil = om.MScriptUtil()
        VPtr = Vutil.asDoublePtr()
        
        ListShape = om.MSelectionList()
        print self.curveShape
        ListShape.add(self.curveShape)
        curveNode = om.MDagPath()
        ListShape.getDagPath( 0, curveNode)
        CurveMFn = om.MFnNurbsSurface(curveNode)
        
        for con in self.allCons:
            #获得UV
            pos = xform(con,q = True,t = True,ws = True)
            Point = om.MPoint(pos[0], pos[1], pos[2])
            ClosestPoint = CurveMFn.closestPoint(Point, UPtr, VPtr, False, 1.0e-3, om.MSpace.kWorld)
#            CurveMFn.getUVAtPoint(ClosestPoint, uvPoint, om.MSpace.kWorld, uvSet, closestPolygon)
#            LOC = spaceLocator()
#            xform(LOC, t = (ClosestPoint[0], ClosestPoint[1], ClosestPoint[2]), ws = True)
            U = om.MScriptUtil.getDouble(UPtr)
            print U
            V = om.MScriptUtil.getDouble(VPtr)
            print V
#            U = om.MScriptUtil.getFloat2ArrayItem( uvPoint, 0, 0 )
#            V = om.MScriptUtil.getFloat2ArrayItem( uvPoint, 0, 1 )
            
            
            #创建毛囊
            FOLShape = createNode('follicle',n = con.replace('_P','_'+con)+'_FOLShape',ss = True)
            hide(FOLShape)
            connectAttr(self.curveShape+'.local',FOLShape+'.inputSurface')
            FOL = listRelatives(FOLShape,p = True)[0]
            
                           
            connectAttr(self.curveShape+'.worldMatrix[0]',FOL+'.inputWorldMatrix')
            
            newFol = rename(FOL,con.replace('_P','_'+con)+'_FOL')
            connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
            connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
            setAttr(FOLShape+'.parameterU',U)
            setAttr(FOLShape+'.parameterV',V)
            setAttr(FOLShape+'.simulationMethod',0)
            
            parent(con, newFol)
            xform(con, t = (0, 0 ,0), wd = True)
            xform(con, ro = (0, 0 ,0), wd = True)
            conGRP = group(con, n = con+'_Trans_GRP')
            group(conGRP, n = con+'_UP_GRP')
            FOLS.append(newFol)
            
        return FOLS            
    def getParams(self,cons):#获得getParam值
        self.allParams = []
        for con in cons:
            pos = xform(con,q = True, t = True, ws = True)
            param = getClosestPointOnCurve(self.curve, pos)
            self.allParams.append( param )            
        
    def createPointOnCurveInfo(self):#创建
        for i,param in enumerate(self.allParams):
            jointN = createNode('pointOnCurveInfo', n = self.ConName +'_JNTPS_'+str(i),ss = True) 
            connectAttr(self.curveShape+'.worldSpace',jointN+'.inputCurve')
            setAttr(jointN+'.parameter',param)
            
            xform(self.allCons[i], t = (0,0,0), wd = True)
            conGrp = group(self.allCons[i], n = self.allCons[i]+'_Grp')
            jnt = joint(n = self.allCons[i]+'_JNT')
            parent(jnt, self.allCons[i])
            connectAttr(jointN+'.result.position', conGrp+'.translate')
            
   
        
def getClosestPointOnCurve(currntCurve,point):#获得曲线上最近的点
    inputPoint = om.MPoint(point[0], point[1], point[2])
    ListShape = om.MSelectionList()
    ListShape.add(currntCurve)
    curveNode = om.MDagPath()
    ListShape.getDagPath( 0, curveNode)
    CurveMFn = om.MFnNurbsCurve(curveNode)
    
    ParamMS = om.MScriptUtil()
    Ptr = ParamMS.asDoublePtr()
    tolerance = 1.0e-3
    CurveMFn.closestPoint(inputPoint, Ptr , tolerance, om.MSpace.kWorld)
    params = om.MScriptUtil.getDouble(Ptr)    
    
    return params
        
def GetCurvePosition(currntCurve, num):
    ListShape = om.MSelectionList()
    ListShape.add(currntCurve)
    curveNode = om.MDagPath()
    ListShape.getDagPath( 0, curveNode)
    CurveMFn = om.MFnNurbsCurve(curveNode)
    
    curveLength = CurveMFn.length()
    averageNum = curveLength/(num)
    pnt = om.MPoint()
    deLength = 0
    
    Params = []
    Points = []
    for x in range(num + 1):
        curParam = CurveMFn.findParamFromLength(deLength)
        CurveMFn.getPointAtParam(curParam,pnt,om.MSpace.kWorld)
        deLength += averageNum
        
        Points.append([pnt.x, pnt.y, pnt.z])
        Params.append( curParam )
        
    return Points,Params

def ParamToPosition(currntCurve, Params):#转换Param到Position
    ListShape = om.MSelectionList()
    ListShape.add(currntCurve)
    curveNode = om.MDagPath()
    ListShape.getDagPath( 0, curveNode)
    CurveMFn = om.MFnNurbsCurve(curveNode)
    
    pnt = om.MPoint()
    Points = []
    for currentParam in Params:
        CurveMFn.getPointAtParam(currentParam,pnt,om.MSpace.kWorld)
        Points.append([pnt.x, pnt.y, pnt.z])
    return Points

def stretchIK():
    obj = ls(sl = True)
    IKhandle = obj[0]
    
    allJnts = ikHandle(IKhandle, q = True, jl = True)
    endEffector = ikHandle(IKhandle, q = True, ee = True)
    endJnt = listConnections(endEffector, s = True, d = False)[0]
    allJnts.append(endJnt)
    
    #创建空组
    mat = getAttr(allJnts[0]+'.worldMatrix')
    ikStretchGrp = group(empty = True, n = allJnts[0]+'_stretch_GRP')
    xform(ikStretchGrp, m = mat)

    mat = getAttr(allJnts[-1]+'.worldMatrix')
    endIkStretchGrp = group(empty = True, n = allJnts[0]+'_endStretch_GRP')
    addAttr(endIkStretchGrp, at = 'float', ln = 'autoStretch', min = 0, max = 1, dv = 1)
    xform(endIkStretchGrp, m = mat)    
    #获得骨骼长度信息
    jntlength = 0.0
    preVector = om.MVector()
    for i,jnt in enumerate(allJnts):
        pos = xform(jnt, q = True, t = True, ws = True)
        CurrentVector = om.MVector(pos[0], pos[1], pos[2])
        if 0 == i:
            preVector = CurrentVector
        else:
            swapVector = CurrentVector - preVector
            jntlength += swapVector.length()
    
            preVector = CurrentVector
    
    #创建distanceBetween节点
    DB = createNode('distanceBetween', n = IKhandle+'_DB')
    connectAttr(ikStretchGrp+'.worldMatrix[0]', DB+'.inMatrix1')
    connectAttr(endIkStretchGrp+'.worldMatrix[0]', DB+'.inMatrix2')
    
    #创建此乘除节点用于控制整体缩放
    scaleMD = createNode('multiplyDivide', n = IKhandle+'_GlobalScale_MD')
    connectAttr(DB+'.distance', scaleMD+'.input1X')      

    #创建此乘除节点用于控制缩放大小
    sizeMD = createNode('multiplyDivide', n = IKhandle+'_Size_MD')
    setAttr(sizeMD+'.operation', 2)
    setAttr(sizeMD+'.input2X', jntlength)
    connectAttr(scaleMD+'.outputX', sizeMD+'.input1X')   

    
    #创建此乘除节点用于控制是否被缩放
    stretchMD = createNode('multiplyDivide', n = IKhandle+'_Stretch_MD')
    connectAttr(sizeMD+'.outputX', stretchMD+'.input1X')
    connectAttr(endIkStretchGrp+'.autoStretch', stretchMD+'.input2X')    
        
    
    
    #创建condition节点
    CD = createNode('condition', n = IKhandle+'_CD')
    connectAttr(stretchMD+'.outputX', CD+'.firstTerm')  
    connectAttr(stretchMD+'.outputX', CD+'.colorIfTrueR')  
    setAttr(CD+'.secondTerm', 1)    
    setAttr(CD+'.operation', 2)      
    
    #创建拉伸
    axis = ['.tx', '.ty', '.tz']
    pos = xform(allJnts[1], q = True, t = True, wd = True)
    pos = [abs(pos[0]), abs(pos[1]), abs(pos[2])]
    currentValue = max(pos)
    index = pos.index(currentValue)
    CurrentAxis = axis[index]
    print pos
    
    print CurrentAxis
    for i,jnt in enumerate(allJnts):
        if i != 0:
            value = getAttr( jnt+CurrentAxis )
            stMD = createNode('multiplyDivide', n = jnt+'_Stretch_MD')
            setAttr(stMD+'.input1X', value) 
            connectAttr(CD+'.outColorR', stMD+'.input2X')
            connectAttr(stMD+'.outputX', jnt+CurrentAxis )         
    
    

