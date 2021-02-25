import maya.cmds as rig
import maya.OpenMaya as om
import maya.mel as MEL
import math

def IKSplineUI():
    if(rig.window('tongue',ex = True)):
        rig.deleteUI('tongue',window = True)
    else:
        rig.window('tongue',w = 310,h = 310,t = 'spineOnCurve', s = True, tb = True)
        rig.columnLayout('mainLayout')    
        rig.button('loadCur',l = 'load your curve',w = 300,c = 'loadCurve()')
        rig.rowColumnLayout(nc = 2,columnWidth = [(1,150),(2,150)])
        rig.textField('Trans', w = 150)
        rig.textField('Shap',w = 150)
        rig.setParent('..')
        
        rig.separator(w = 300)
        rig.separator(w = 300)
        
        rig.checkBox('rebCurve',l = 'rebuild curve',v = False)
        rig.checkBox('revCurve',l = 'reverse curve')
        rig.separator(w = 300)
        
        rig.rowColumnLayout(nc = 2,columnWidth = [(1,120),(2,180)])
        rig.text('enter joint name')
        rig.textField('jointNameText',ed = 1)
        rig.setParent('..')
        
        rig.rowColumnLayout(nc = 2,columnWidth = [(1,120),(2,40)])
        rig.text('enter number of joints')
        rig.textField('jointNumText',ed = 1,tx = 7)
        rig.setParent('..')   
        rig.separator(w = 300)
        
        rig.radioButtonGrp('jointOrientGrp',l = 'AimAxis',nrb = 3,la3 = ('x','y','z'),sl = 1,cw4 = (80,40,40,40))
        rig.button(l = 'create setup',w = 300,c = 'createSetup()') 
        rig.separator(w = 300)
            
        rig.rowColumnLayout(nc = 2,columnWidth = [(1,100),(2,40)])
        rig.text('second num')
        rig.textField('secondNum',w = 150,tx = 3)
        rig.setParent('..')
        rig.button(l = 'create dynamics',w = 300,c = 'createDy()')
        rig.setParent('mainLayout')
        rig.separator(w = 300)
        rig.separator(w = 300) 
            
        rig.text('connect character Translate > ikSplineHandle.TranslateFactor',w = 300)
        
        rig.showWindow('tongue')

def loadCurve():
    selObj = rig.ls(sl = True)[0]
    selShape = rig.listRelatives(selObj,s = True)[0]
    rig.textField('Trans',e = True,tx = selObj)
    rig.textField('Shap',e = True,tx = selShape)
    rig.textField('jointNameText',e = True,tx = selObj)
    
def createDy():
    
    curveName = rig.textField('Trans',q = True,tx = True)
    copyCurve = rig.duplicate(curveName,n = curveName+'_dynamics')  
    rig.select(copyCurve)
    MEL.eval('makeCurvesDynamicHairs 1 0 1')
    HSShape = rig.ls(sl = True)[0]
    rig.select(cl = True)
    HS = rig.listRelatives(HSShape,p = True)[0]
    
    FOL = rig.listRelatives(copyCurve,p = True)[0]
    FOLShape = rig.listRelatives(FOL,s = True)[0]    
    conCurve = rig.listConnections(FOLShape,s = False ,d = True,type = 'nurbsCurve')[0]
    
    HSname = rig.rename(HS,'HS_'+curveName)
    FolName =rig.rename(FOL,'FOL_'+curveName)     
    conCurve = rig.rename(conCurve,copyCurve[0]+'_con') 
    
    delA = (rig.listRelatives(FolName,p = True)[0])  
    delB = (rig.listRelatives(conCurve,p = True)[0])     
    rig.parent(FolName,w = True)
    rig.parent(conCurve,w = True)
    rig.parent(copyCurve,w = True)
    rig.delete(delA,delB)
    
    FolShape = rig.listRelatives(FolName,s = True)[0]
    rig.setAttr(FolName+'.pointLock',1)
    curveNameShape = rig.listRelatives(curveName,s = True)[0]
    conCurveShape = rig.listRelatives(conCurve,s = True)[0]
    rig.connectAttr(conCurveShape+'.worldSpace[0]',curveNameShape+'.create')
   
    ikCurve = rig.listConnections(curveNameShape,s = False,d = True,type = 'ikHandle')[0]
    startJoint = rig.ikHandle(ikCurve,q = True,sj = True)
    jointUpList = createDyCon(startJoint)
    
    rig.skinCluster(jointUpList,copyCurve,toSelectedBones = True)
    allCon = rig.listRelatives(rig.listRelatives(rig.listRelatives(jointUpList[0],p = True)[0],p = True)[0],p = True)[0]
    rig.parent(startJoint,allCon)
    constraintGrp = rig.listConnections(rig.listConnections(startJoint,s = False,d = True,type = 'scaleConstraint')[0],s = False,d = True,type = 'transform')[0]
    deformersGrp = rig.group(constraintGrp,ikCurve,FolName,HSname,curveName,copyCurve,conCurve,n =curveName+'_dynimics_Grp' )
    conAllGrp = rig.group(allCon,n = allCon+'_Grp')
    
    rig.setAttr(deformersGrp+'.visibility',0)
    HsShape = rig.listRelatives(HSname,s = True)[0]
    rig.parent(HsShape,allCon,add = True,s = True)
    rig.setAttr(HsShape+'.visibility',0)
    
    rig.addAttr(allCon,ln = 'second_vis',at = 'bool',k = True)
    for visObj in jointUpList:
        jointShape = rig.listRelatives(visObj,s = True)[0]
        rig.connectAttr(allCon+'.second_vis',jointShape+'.visibility')
    
def createSetup():
    jointNumstr = rig.textField('jointNumText',q = True,tx = True)
    jointName = rig.textField('jointNameText',q = True,tx = True)
    jointName = jointName+'_'
    orient = rig.radioButtonGrp('jointOrientGrp',q = True,sl = True)
    currntCurve = rig.textField('Shap',q =True,tx = True)
    
    jointNum = int(jointNumstr)
    disdenceList = []
    jointList = []
    
    aim = ''
    xyz = ''   
    if(orient == 1):
        aim = 'xyz'
        xyz = 'tx'
    elif(orient == 2):
        aim = 'yzx'
        xyz = 'ty'
    elif(orient == 3):
        aim = 'zxy'
        xyz = 'tz'
        
    if(rig.checkBox('rebCurve',q = True,v = True)):
        vtxNum = len(rig.ls(currntCurve+'.cv[*]',fl = True))
        rig.rebuildCurve(currntCurve,ch = 1,rpo = 1,rt = 0,end = 1,kr = 0,kcp = 0,kep = 1,kt = 0,s = vtxNum,d = 3,tol = 0.001)
        
        
    if(rig.checkBox('revCurve',q = True,v = True)):
        rig.reverseCurve(currntCurve,ch = True,rpo = True)
          

        
    rig.select(cl = True)
    ListShape = om.MSelectionList()
    ListShape.add(currntCurve)
    curveNode = om.MDagPath()
    ListShape.getDagPath( 0, curveNode)
    CurveMFn = om.MFnNurbsCurve(curveNode)
    
    curveLength = CurveMFn.length()
    averageNum = curveLength/(jointNum - 1)
    pnt = om.MPoint()
    deLength = 0
    
    for x in range(jointNum):
        curParam = CurveMFn.findParamFromLength(deLength)
        CurveMFn.getPointAtParam(curParam,pnt,om.MSpace.kWorld)
        jointN = rig.createNode('pointOnCurveInfo', n = jointName+'jointPos'+str(x),ss = True) 
        rig.connectAttr(currntCurve+'.worldSpace',jointN+'.inputCurve')
#    
#        rig.setAttr(jointN+'.turnOnPercentage',1)
        rig.setAttr(jointN+'.parameter',curParam)
    
        currentJoint = rig.joint(p = (rig.getAttr(jointN+'.positionX'),rig.getAttr(jointN+'.positionY'),rig.getAttr(jointN+'.positionZ')),n = 'Joint_'+jointName+str(x))
        jointList.append(currentJoint)
        deLength += averageNum
        if(x):
            disName = rig.createNode('distanceBetween',n = jointName+'Dis'+str(x), ss = True)
            rig.connectAttr(jointName+'jointPos'+str(x-1)+'.position',disName+'.point1')
            rig.connectAttr(jointN+'.position',disName+'.point2')
            disdenceList.append(disName)
            
            
    rig.joint(jointList[0], e = True, oj = aim, secondaryAxisOrient = 'yup', ch = True , zso = True)
    rig.joint(jointList[-1], e = True, oj = 'none', secondaryAxisOrient = 'yup', ch = True , zso = True)

                
    groupName = rig.group(empty = True,n = jointName+'Group')            
    scaleNode = rig.scaleConstraint(jointList[0],groupName,mo = True)  
    
    for n ,i  in enumerate(disdenceList):
        
        multi = rig.createNode('multiplyDivide',n = 'MD_'+i)
        rig.setAttr(multi+'.operation',2)
        rig.connectAttr(i+'.distance', multi+'.input1.input1X')
        rig.connectAttr(groupName+'.scale',multi+'.input2')


        rig.connectAttr(multi+'.output.outputX', jointList[n+1]+'.'+xyz)
           
    rig.ikHandle(n = jointName+'IKSpine',sol = 'ikSplineSolver',ccv = False,sj = jointList[0],ee = jointList[-1], c = currntCurve)



def conShape(objName,curveS,color):
    name = rig.curve(n = objName,d = 1,p = [(0,1,0),(0,0.92388,0.382683),(0,0.707107,0.707107),(0,0.382683,0.92388),(0,0,1),(0,-0.382683,0.92388),(0,-0.707107,0.707107),(0,-0.92388,0.382683),(0,-1,0),(0,-0.92388,-0.382683),(0,-0.707107,-0.707107),(0,-0.382683,-0.92388),(0,0,-1),(0,0.382683,-0.92388),(0,0.707107,-0.707107),(0,0.92388,-0.382683),(0,1,0),(0.382683,0.92388,0),(0.707107,0.707107,0),(0.92388,0.382683,0),(1,0,0),(0.92388,-0.382683,0),(0.707107,-0.707107,0),(0.382683,-0.92388,0),(0,-1,0),(-0.382683,-0.92388,0),(-0.707107,-0.707107,0),(-0.92388,-0.382683,0),(-1,0,0),(-0.92388,0.382683,0),(-0.707107,0.707107,0),(-0.382683,0.92388,0),(0,1,0),(0,0.92388,-0.382683),(0,0.707107,-0.707107),(0,0.382683,-0.92388),(0,0,-1),(-0.382683,0,-0.92388),(-0.707107,0,-0.707107),(-0.92388,0,-0.382683),(-1,0,0),(-0.92388,0,0.382683),(-0.707107,0,0.707107),(-0.382683,0,0.92388),(0,0,1),(0.382683,0,0.92388),(0.707107,0,0.707107),(0.92388,0,0.382683),(1,0,0),(0.92388,0,-0.382683),(0.707107,0,-0.707107),(0.382683,0,-0.92388),(0,0,-1)],k = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])
    rig.setAttr(name+'.scale',curveS,curveS,curveS)
    rig.makeIdentity(name,apply = True,s = 1)
    nameShape = rig.listRelatives(name,s = True)[0]
    rig.setAttr(nameShape+'.overrideEnabled',1)
    rig.setAttr(nameShape+'.overrideColor',color)    
    return name

def parentShape(conObj,jointObj):
    conObjShape = rig.listRelatives(conObj,s = True)[0]
    rig.parent(conObjShape,jointObj,s = True,add = True)
    rig.delete(conObj)
    
def createDyCon(Joints):
    aim = ''
    xyz = ''
    orient = rig.radioButtonGrp('jointOrientGrp',q = True,sl = True) 
    if(orient == 1):
        aim = 'xyz'
        xyz = 'tx'
    elif(orient == 2):
        aim = 'yzx'
        xyz = 'ty'
    elif(orient == 3):
        aim = 'zxy'
        xyz = 'tz'
        
    rig.select(Joints,hi = True)
    Joints = rig.ls(sl = True,type = 'joint')
    
    
    sege = int(rig.textField('secondNum',q = True,tx = True))
    curveName = rig.textField('Trans',q = True,tx = True)
    curveName = curveName+'_'
    lowJointName = 'lowJoint_'
    midJointName = 'midJoint_'
    upJointName = 'upJoint_'
    jointLow = []
    jointMid = []
    jointUp = [] 
    
    
    rig.select(cl = True)
    for i,jointObj in enumerate(Joints):        
        n = math.fmod(i,sege)
        if(0 == int(n) or jointObj == Joints[-1] or 0 == i):
            pos = rig.xform(jointObj,q = True,ws = True,rp = True)
            pre = len(jointLow)
            jointN = rig.joint(p = pos,n = curveName+lowJointName+str(pre))
            jointLow.append(jointN)
    
        if(jointObj == Joints[-1]):
            tempJointMid = rig.duplicate(jointLow[0],renameChildren = True)
            for j,jointTemp in enumerate(tempJointMid):
                jointTempName = rig.rename(jointTemp,curveName+midJointName+str(j))
                jointMid.append(jointTempName)
            rig.joint(jointMid[0],e = True,oj = aim,secondaryAxisOrient = 'yup',ch = True ,zso = True)
            rig.joint(jointMid[-1],e = True,oj = 'none',secondaryAxisOrient = 'yup',ch = True ,zso = True)
            
                
            tempJointUp =  rig.duplicate(jointLow[0],renameChildren = True)
            for j,jointTemp in enumerate(tempJointUp):
                jointTempName = rig.rename(jointTemp,curveName+upJointName+str(j))
                jointUp.append(jointTempName)
            rig.joint(jointUp[0],e = True,oj = aim,secondaryAxisOrient = 'yup',ch = True ,zso = True)
            rig.joint(jointUp[-1],e = True,oj = 'none',secondaryAxisOrient = 'yup',ch = True ,zso = True)
    
            
            
            for k in range(len(jointLow)):
                rig.parent(jointUp[k],jointMid[k]) 
                rig.parent(jointMid[k],jointLow[k])          
                if not(k == len(jointLow)-1):
                    rig.parent(jointLow[k+1],jointUp[k])
    
    
    conAll = conShape(curveName+'conAll',0.5,17)
    rig.addAttr(conAll,ln = 'stretch',at = 'float',k = True)
    rig.setAttr(conAll+'.stretch',1)
    rig.addAttr(conAll,ln = 'roX',at = 'float',k = True)
    rig.addAttr(conAll,ln = 'roY',at = 'float',k = True)
    rig.addAttr(conAll,ln = 'roZ',at = 'float',k = True)
    jointPos = rig.xform(jointUp[0],q = True,ws = True,rp = True)
    rig.move(jointPos[0],jointPos[1],jointPos[2],conAll,ws = True)    

        
    for i,cur in enumerate(jointUp):
        curveN = conShape(cur+'_curve',0.2,13)
        parentShape(curveN,cur) 
        rig.connectAttr(conAll+'.roY',jointLow[i]+'.ry')
        rig.connectAttr(conAll+'.roZ',jointLow[i]+'.rz')  
        rig.connectAttr(conAll+'.roX',jointLow[i]+'.rx')  
        
        if(0<i):
            transValue = rig.getAttr(jointLow[i]+'.'+xyz)
            multiNodes = rig.createNode('multiplyDivide',ss = True,n = 'MD_'+cur)
            rig.setAttr(multiNodes+'.input1.input1Z',transValue)
            rig.connectAttr(conAll+'.stretch',multiNodes+'.input2.input2Z') 
            rig.connectAttr(multiNodes+'.output.outputZ',jointLow[i]+'.'+xyz)
    rig.makeIdentity(conAll,apply = True,s = True,t = True,r = True)
    rig.parent(jointLow[0],conAll)        
    return jointUp   
        
               