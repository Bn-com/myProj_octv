#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.face.controlers import CreateControler

def SK_FollicleControl(cons,multiple = 3,SV = 1,conPrefix = 'Lf_eyeBrow',nurbsMesh = 'Lf_eyeBrow_Loft',FaceFolScale = 'Face_Sclale_Grp'):
#    nurbsMesh  nurbs名字
#    conPrefix   控制器名字
#    FaceFolScale  毛囊缩放组
#    multiple    次级毛囊缩放组
#     SV          缩放值
    TR = 0.1*SV
    conSize = 1*SV
    tempCurves = []
    FOLs = []
    NewCons = [] #生成的新的控制器
    MainJnts = [] #主控蒙皮骨骼
    SeJnts = []   #次控蒙皮骨骼
    MainController = CreateControler(13,(conSize*0.1,conSize*0.1,conSize*0.1))
    
    #创建曲线上传Nurbs片
    for con in cons:
        emptyGrp = rig.group(n = con+'_EM_GRP',empty = True)
        rig.parent(emptyGrp,con)
        rig.xform(emptyGrp,ro = (0,0,0.0),wd = True)
        rig.xform(emptyGrp,t = (0,0,0.0),wd = True)
        Mpos = rig.xform(emptyGrp,q = True,t = True,ws = True) 
        rig.xform(emptyGrp,t = (0,0,TR),wd = True)
        Fpos = rig.xform(emptyGrp,q = True,t = True,ws = True)  
        rig.xform(emptyGrp,t = (0,0,-TR),wd = True)
        Bpos = rig.xform(emptyGrp,q = True,t = True,ws = True)       
        
        curs = rig.curve(d = 2,p = [Fpos,Mpos,Bpos])
        tempCurves.append(curs)
        rig.delete(emptyGrp)
    
    loftNurbs = rig.loft(tempCurves)[0]
    rig.rebuildSurface(loftNurbs,rpo  = 1,rt = 0,end = 1,kr = 0,su = len(cons)*2,du = 3,sv = 0,dv = 3,tol = 0.001,fr = 0,dir = 2,ch = True)
#    rig.rebuildSurface(loftNurbs,rt = 1,kr = 0,ch = True)
    mainMesh = rig.duplicate(loftNurbs,n = nurbsMesh)[0]
    SCMesh = rig.duplicate(mainMesh,n = mainMesh+'_SC')[0]
    rig.hide(mainMesh,SCMesh)
    rig.delete(loftNurbs,tempCurves)
    
    
    #在主nurbs片上生成毛囊
    MainMeshShape = rig.listRelatives(mainMesh,s = True)[0]
    CPO = rig.createNode('closestPointOnSurface',n = mainMesh+'_CPO',ss = True)
    rig.connectAttr(MainMeshShape+'.worldSpace[0]',CPO+'.inputSurface')
    for i,con in enumerate(cons):
        pos = rig.xform(con,q = True,t = True,ws = True)
        rig.setAttr(CPO+'.inPositionX',pos[0])
        rig.setAttr(CPO+'.inPositionY',pos[1])
        rig.setAttr(CPO+'.inPositionZ',pos[2])
        U = rig.getAttr(CPO+'.parameterU')
        V = rig.getAttr(CPO+'.parameterV')
    
        FOLShape = rig.createNode('follicle',n = con+'_EB_FOLShape',ss = True)
        rig.connectAttr(MainMeshShape+'.worldSpace[0]',FOLShape+'.inputSurface')
        FOL = rig.listRelatives(FOLShape,p = True)[0]
        rig.connectAttr(FaceFolScale+'.scale',FOL+'.scale')
        newFol = rig.rename(FOL,con+'_EB_FOL')
        rig.connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
        rig.connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
        rig.setAttr(FOLShape+'.parameterU',U)
        rig.setAttr(FOLShape+'.parameterV',V)
        rig.setAttr(FOLShape+'.simulationMethod',0)
        
    #    生成控制器，完成主要控设置。
        Mcon = MainController.SK_b05(conPrefix+'_'+str(i+1)+'_M') 
        rig.parent(Mcon,con)
        rig.xform(Mcon,ro = (-90,0,0),wd = True)   
        rig.xform(Mcon,t = (0,0,0),wd = True)
        rig.setAttr(Mcon+'.sy',-0.5)
        rig.makeIdentity(Mcon,apply = True,s = True,r = True)
        MconGrp = rig.group(Mcon,n = Mcon+'Grp',r = True)
        rig.parent(MconGrp,FOL)
        JNT = rig.joint(n = Mcon+'_JNT')
        rig.xform(JNT,t = pos,ws = True)
        rig.parent(JNT,Mcon)
        
        rig.hide(FOLShape,JNT)
        NewCons.append(Mcon)
        FOLs.append(FOL)
        MainJnts.append(JNT)
    rig.skinCluster(MainJnts,SCMesh)    
        
    #在次nurbs片上生成毛囊
    
    SCMeshShape = rig.listRelatives(SCMesh,s = True)[0]
    CPO = rig.createNode('closestPointOnSurface',n = SCMesh+'_CPO',ss = True)
    rig.connectAttr(SCMeshShape+'.worldSpace[0]',CPO+'.inputSurface')
    
    IterFol = len(cons)*multiple
    addPos = 1.0/IterFol
    dvUV = 0.0
    for con in range(IterFol+1):
        V = 0.5
        FOLShape = rig.createNode('follicle',n = SCMesh+'_'+str(con)+'_SC_FOLShape',ss = True)
        rig.connectAttr(SCMeshShape+'.worldSpace[0]',FOLShape+'.inputSurface')
        FOL = rig.listRelatives(FOLShape,p = True)[0]
        rig.connectAttr(FaceFolScale+'.scale',FOL+'.scale')
        newFol = rig.rename(FOL,SCMesh+'_'+str(con)+'_SC_FOL')
        rig.connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
        rig.connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
        rig.setAttr(FOLShape+'.parameterU',dvUV)
        rig.setAttr(FOLShape+'.parameterV',V)
        rig.setAttr(FOLShape+'.simulationMethod',0)  
        
        dvUV += addPos
        
        JNT = rig.joint(n = conPrefix+'_'+str(con+1)+'_SC_JNT')
        pos = rig.xform(FOL,q = True,t = True,ws = True)
        rig.xform(JNT,t = pos,ws = True)
        rig.parent(JNT,FOL)
        
        rig.hide(FOLShape,JNT)
        FOLs.append(FOL)
        SeJnts.append(JNT)
    AllGrp = rig.group(mainMesh,SCMesh,FOLs,n = nurbsMesh+'_DEF_GRP') 
    
    
    return mainMesh,SeJnts,AllGrp,NewCons
