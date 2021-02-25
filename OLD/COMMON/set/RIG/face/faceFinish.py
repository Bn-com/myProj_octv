#-*- coding: utf-8 -*-
from RIG.commonly.base import SK_getSkinCluster
import math
import maya.cmds as rig
import maya.mel as mel
from RIG.face.controlers import CreateControler
from RIG.face.eyebrow import SK_FollicleControl
from RIG.face.baseClass import *
class FC_FaceSetup(object):
    def __init__(self,eyeSign,tongueSign,faceSign,eyebrowSign,toothSign,face,signRun = True):
        self.Lock = LockHideAttr(False,False,False,False)
        self.eyeSn = eyeSign
        self.tongueSign = tongueSign
        self.faceSn = faceSign
        self.eyebrowSn = eyebrowSign
        self.toothSn = toothSign
        self.face = face
        if signRun:
            self.combine()
        
    def distanceBetween(self,parA,parB):
        Apos = rig.xform(parA,q = True,t = True,ws = True)
        Bpos = rig.xform(parB,q = True,t = True,ws = True)
        dis = math.sqrt((Apos[0]- Bpos[0])**2 + (Apos[1]- Bpos[1])**2 + (Apos[2]- Bpos[2])**2)
        return dis
    
    def getTFstr(self,inputData):
        data = rig.textField(inputData,q = True,tx = True)
        return data
    
    def genBaseFace(self,mesh):
        skinMesh = rig.duplicate(mesh,n = mesh+'_Skin_Mesh')[0]
        self.skinMesh = skinMesh
        self.Mesh = mesh
        rig.transferAttributes(self.Mesh,self.skinMesh,transferUVs = 1,sampleSpace = 5)
        rig.select(self.skinMesh)
        mel.eval('DeleteHistory')
        skinMeshShape = rig.listRelatives(skinMesh,s = True,ni = True)[0]
        meshShape = rig.listRelatives(mesh,s = True,ni = True)[0]

        
        
        self.scaleVal =self.distanceBetween('Lf_ear_P','Rt_ear_P')/3.39395596416
        FaceFolScale = rig.group(empty = True,n = 'Face_Scale_Grp')
        FaceDeformersGrp = rig.group(empty = True,n = 'Face_Deformers_Grp')
        self.faceRig = rig.group(empty = True,n = 'Face_Rigging_GRP')
        rig.addAttr(FaceFolScale,at = 'float',ln = 'scaleVal',dv = self.scaleVal)
        rig.addAttr(FaceFolScale,at = 'float',ln = 'signA',dv = 11)
        rig.addAttr(FaceFolScale,at = 'float',ln = 'signB',dv = 22)
        self.controller = CreateControler(13,[0.05*self.scaleVal,0.05*self.scaleVal,0.05*self.scaleVal])
        
        cons = [objCon for objCon in [obj for obj in rig.ls(type = 'transform') if rig.attributeQuery('sign',n = obj,ex = True)] if (78 == rig.getAttr(objCon+'.sign') or 71 == rig.getAttr(objCon+'.sign'))]
        
        
        
        CLM = rig.createNode('closestPointOnMesh',n = 'Face_CLM',ss = True)
        rig.connectAttr(meshShape+'.outMesh',CLM+'.inMesh')
        
        JNTS = []
        FOLS = []
        EXFOLS = []
        self.allCons = []
        for con in cons:
            pos = rig.xform(con,q = True,t = True,ws = True)
            rig.setAttr(CLM+'.inPositionX',pos[0])
            rig.setAttr(CLM+'.inPositionY',pos[1])
            rig.setAttr(CLM+'.inPositionZ',pos[2])
            U = rig.getAttr(CLM+'.result.parameterU')
            V = rig.getAttr(CLM+'.result.parameterV') 
            
            FOLShape = rig.createNode('follicle',n = con+'_FOLShape',ss = True)
            rig.connectAttr(meshShape+'.worldMesh[0]',FOLShape+'.inputMesh')
            FOL = rig.listRelatives(FOLShape,p = True)[0]
            rig.connectAttr(FaceFolScale+'.scale',FOL+'.scale')
            rig.connectAttr(meshShape+'.worldMatrix[0]',FOL+'.inputWorldMatrix')
            newFol = rig.rename(FOL,con+'_FOL')
            rig.connectAttr(FOLShape+'.outTranslate',newFol+'.translate')
            rig.connectAttr(FOLShape+'.outRotate',newFol+'.rotate')
            rig.setAttr(FOLShape+'.parameterU',U)
            rig.setAttr(FOLShape+'.parameterV',V)
            rig.setAttr(FOLShape+'.simulationMethod',0)

            
    #        åˆ›å»ºæŽ§åˆ¶å™¨
            CurConName = con.replace('_P','_M')
            ConName = self.controller.SK_b03(CurConName)
            if 78 == rig.getAttr(con+'.sign'):
                rig.connectAttr(FaceFolScale+'.signA',ConName+'.sign')
            else:
                rig.connectAttr(FaceFolScale+'.signB',ConName+'.sign')
            ConNameShape = rig.listRelatives(ConName,s = True)[0]
            ConColor = rig.getAttr(rig.listRelatives(con,s = True)[0]+'.overrideColor')
            rig.setAttr(ConNameShape+'.overrideColor',ConColor)
            ConGRP = rig.group(ConName,n = ConName+'_GRP')
            MirrorGRP = rig.group(ConGRP,n = ConName+'_Mirror_GRP')
           
            
    #        ç”Ÿæˆ�éª¨éª¼
            rig.select(cl = True)
            FOLMatrix = rig.getAttr(FOLShape+'.worldMatrix[0]')
            jntName = rig.joint(n = CurConName+'_JNT')
            JNTGrp = rig.group(jntName,n = jntName+'_GRP')
            
            rig.parent(JNTGrp,ConName)
            rig.xform(MirrorGRP,matrix = FOLMatrix)
            rig.parent(MirrorGRP,FOL)
            
            rig.setAttr(jntName+'.visibility',0)
            rig.setAttr(FOLShape+'.visibility',0)
            if 11 == rig.getAttr(ConName+'.sign'):
                JNTS.append(jntName)
            else:
                EXFOLS.append(FOLShape)
            FOLS.append(FOL)
            self.allCons.append(ConName)
            
        SkinClus = rig.skinCluster(JNTS,skinMesh,n = 'Face_BlendShape_SKIN')[0]
        infs = rig.skinCluster(SkinClus,q = True,inf = True)
        for i,inf in enumerate(infs):
            MirrorGRP = inf.replace('_M_JNT','_M_Mirror_GRP')
            rig.connectAttr(MirrorGRP+'.worldInverseMatrix[0]',SkinClus+'.bindPreMatrix['+str(i)+']')
                    
#            if 'Rt' == MirrorGRP.split('_')[0]:
#                rig.setAttr(MirrorGRP+'.sx',-1)
#                rig.setAttr(MirrorGRP+'.sy',-1) 
#            if 'Lf' == MirrorGRP.split('_')[0]:
#                rig.setAttr(MirrorGRP+'.rx',180)
#                rig.setAttr(MirrorGRP+'.sz',-1)

#            校正控制器轴向到世界
#            rig.rotate(0,0,0,MirrorGRP,ws = True)
#            校正控制器轴向到法线向上方向指向世界的Y方向。
#            MirrorMatrix = rig.getAttr(MirrorGRP+'.worldMatrix[0]')
#            aimEmptyGrp = rig.group(n = MirrorGRP+'_Aim',empty = True)
#            rig.xform(aimEmptyGrp,matrix = MirrorMatrix)
#            rig.parent(aimEmptyGrp,MirrorGRP)
#            rig.setAttr(aimEmptyGrp+'.tz',1)
#            rig.parent(aimEmptyGrp,w = True)
#            rig.aimConstraint(aimEmptyGrp,MirrorGRP,aimVector = (0,0,1),upVector = (0,1,0),worldUpType = 'scene')
#            rig.delete(aimEmptyGrp)

#            根据规定的轴向校正
            SK_ConOrientation(MirrorGRP.replace('_Mirror_GRP',''))
        
        if EXFOLS:
            for fol in  EXFOLS:
                rig.connectAttr(skinMeshShape+'.worldMesh[0]',fol+'.inputMesh',f = True)
                MirrorGRP = fol.replace('_P_FOLShape','_M_Mirror_GRP')
#                rig.setAttr(childGrp+'.sz',-1)

#               校正控制器轴向到世界
#               rig.rotate(0,0,0,MirrorGRP,ws = True)
#               校正控制器轴向到法线向上方向指向世界的Y方向。
#                MirrorMatrix = rig.getAttr(MirrorGRP+'.worldMatrix[0]')
#                aimEmptyGrp = rig.group(n = MirrorGRP+'_Aim',empty = True)
#                rig.xform(aimEmptyGrp,matrix = MirrorMatrix)
#                rig.parent(aimEmptyGrp,MirrorGRP)
#                rig.setAttr(aimEmptyGrp+'.tz',1)
#                rig.parent(aimEmptyGrp,w = True)
#                rig.aimConstraint(aimEmptyGrp,MirrorGRP,aimVector = (0,0,1),upVector = (0,1,0),worldUpType = 'scene')
#                rig.delete(aimEmptyGrp)
          
#                根据规定的轴向校正
                SK_ConOrientation(MirrorGRP.replace('_Mirror_GRP',''))
                
        FOLALLGRP = rig.group(FOLS,n = 'All_FOLS_GRP')
        rig.parent(FaceFolScale,self.Mesh,self.skinMesh,FOLALLGRP,FaceDeformersGrp)
        
    def findSkinCluster(self,Mesh):
        skinName = ''
        hisNode = rig.listHistory(Mesh,pdo = True)
        if hisNode:
            sign = [skinCL for skinCL in rig.listHistory(Mesh,pdo = True) if ('skinCluster' == rig.nodeType(skinCL))]
            if sign:
                skinName = sign[0]
        return skinName
             
    def connectFaceModel(self,skinModel):
        rig.select(cl = True)
        rig.hide('Mid_base_M')
        jawHeads = [ u'HeadRoot_JNT_P', u'Jaw_JNT_P',u'JawTip_JNT_P']
        for jnt in jawHeads:
            pos = rig.xform(jnt,q = True,t = True,ws = True)
            NJnt = rig.joint(n = jnt.replace('_JNT_P','_JNT'))
            rig.xform(NJnt,t = pos,ws = True)
            if 'Jaw_JNT_P' == jnt:
                jawUP = rig.joint(n = jnt.replace('_JNT_P','_UP_JNT'))
                rig.xform(jawUP,t = pos,ws = True)
                jawUPA = rig.joint(n = jnt.replace('_JNT_P','_UPA_JNT'))
                rig.xform(jawUPA,t = pos,ws = True)
                jawUPB = rig.joint(n = jnt.replace('_JNT_P','_UPB_JNT'))
                rig.xform(jawUPB,t = pos,ws = True)
                
        jaw = 'Jaw_M'
        rig.addAttr(jaw,at = 'enum',ln = 'vis_second',en = 'OFF:ON',k = False)
        rig.setAttr(jaw+'.vis_second',cb = True)
        jawPos = rig.xform(jaw,q = True,piv = True,ws = True)[0:3]  
        rig.xform('JawTip_JNT',t = jawPos,ws = True)      
        rig.parent(jaw,w = True) 
        rig.makeIdentity(jaw,apply = True,t = True,s = True,r = True)
        
        IK = rig.ikHandle(sj = 'Jaw_UPB_JNT',ee = 'JawTip_JNT',n = 'Jaw_IK')[0]
        rig.parent(IK ,jaw)
        rig.connectAttr(jaw+'.rz',IK+'.twist') 
        rig.connectAttr(jaw+'.tz','Jaw_UPA_JNT'+'.tz')  
        
        
        sign = self.findSkinCluster(skinModel) 
        if sign:
            rig.skinCluster(sign,e = True,ai = 'Jaw_UPB_JNT',lw = True,wt = 0)
        else:
            rig.skinCluster('Jaw_UPB_JNT','HeadRoot_JNT',skinModel,tsb = True,n = 'Jaw_Skin')
        rig.blendShape(skinModel,self.skinMesh,w = (0,1),n = 'SKIN_BS',foc = True)
        rig.blendShape(skinModel,self.Mesh,w = (0,1),n = 'Mesh_BS')
        
        grpA = rig.group(jaw,n = jaw+'_GRPA',r = True)
        grpB = rig.group(grpA,n = jaw+'_GRPB',r = True)
        jntGrp = rig.group('HeadRoot_JNT',n = 'Head_JNT_GRP',r = True)
        rig.hide(jntGrp)
        rig.hide(IK)
        rig.parent(grpB,jntGrp,self.faceRig)
        
        allCons = self.allCons
        for con in allCons:
            rig.connectAttr(jaw+'.vis_second',rig.listRelatives(con,p = True)[0]+'.visibility')
        
        self.Lock.hideInvertAttr(jaw,('translateZ','translateY','translateX','rotateZ','vis_Second'))

        rig.parent(skinModel,'Face_Deformers_Grp')
    def eyeSetup(self,LfEye,RtEye):
        LfPos = rig.xform('Lf_EYE_JNT_P',q = True,t = True,ws = True)
        rig.select(cl = True)
        LfJnt = rig.joint(n = 'Lf_EYE_JNT')
        rig.xform(LfJnt,t = LfPos,ws = True)
        RtPos = rig.xform('Rt_EYE_JNT_P',q = True,t = True,ws = True)
        rig.select(cl = True)
        RtJnt = rig.joint(n = 'Rt_EYE_JNT')
        rig.xform(RtJnt,t = RtPos,ws = True)
        
        LfLoc = rig.spaceLocator(n = LfJnt+'_Loc')[0]
        RtLoc = rig.spaceLocator(n = RtJnt+'_Loc')[0]
        LfLocPos = (LfPos[0],LfPos[1]+self.scaleVal,LfPos[2])
        rig.xform(LfLoc,t = LfLocPos,ws = True)
        RtLocPos = (RtPos[0],RtPos[1]+self.scaleVal,RtPos[2])
        rig.xform(RtLoc,t = RtLocPos,ws = True)
        locEyeGrp = rig.group(LfLoc,RtLoc,n = 'Eye_LOC_GRP')
        rig.hide(locEyeGrp)
    
        eyeCon = 'eye_M'
        rig.addAttr(eyeCon,at = 'enum',ln = 'follow',en = 'OFF:ON',k = False,dv = True)
        rig.setAttr(eyeCon+'.follow',cb = True)
        LfCon = 'Lf_eye_M'
        RtCon = 'Rt_eye_M'
        rig.parent(eyeCon,w = True)
        rig.setAttr(eyeCon+'.rx',0)
        eyegroupA = rig.group(eyeCon,n = 'eye_GoupA',r = True)
        eyegroupB = rig.group(eyegroupA,n = 'eye_GoupB',r = True)
        Lf_conGrp = rig.group(LfCon,n = LfCon+'_GRP',r = True)
        Rt_conGrp = rig.group(RtCon,n = RtCon+'_GRP',r = True)

        grpL = rig.group('Lf_EYE_JNT',n = 'Eye_JNT_GRPL',r = True)
        grpR = rig.group('Rt_EYE_JNT',n = 'Eye_JNT_GRPR',r = True)
        rig.parent(grpL,grpR,locEyeGrp,eyegroupB,self.faceRig)
        
        rig.makeIdentity(eyegroupA,apply = True,s = True,t = True,r = True)
#        aimConstraint
        rig.aimConstraint(LfCon,LfJnt,aimVector = (1,0,0),upVector = (0,1,0),worldUpType = 'object',worldUpObject = LfLoc)
        rig.aimConstraint(RtCon,RtJnt,aimVector = (1,0,0),upVector = (0,1,0),worldUpType = 'object',worldUpObject = RtLoc)
        
#       skin
        if (LfEye and RtEye):
            rig.skinCluster(LfJnt,LfEye,tsb = True)
            rig.skinCluster(RtJnt,RtEye,tsb = True)
        
        RV = rig.createNode('reverse',n = 'EYE_C_RV',ss = True)
        rig.scaleConstraint(self.faceRig,'Face_Scale_Grp',mo = True)
        parentNode = rig.parentConstraint(self.faceRig,'Face_Scale_Grp',eyegroupA,mo = True)[0]
        rig.connectAttr(eyeCon+'.follow',parentNode+'.'+self.faceRig+'W0')
        rig.connectAttr(RV+'.output.outputX',parentNode+'.'+'Face_Scale_Grp'+'W1')
        rig.connectAttr(eyeCon+'.follow',RV+'.input.inputX')
        
    def toothSetup(self,upTooth,dnTooth):
        UpTooth = 'UpTooth_JNT_P'
        DnTooth = 'DnTooth_JNT_P'
        upPos = rig.xform(UpTooth,q = True,t = True,ws = True)
        dnPos = rig.xform(DnTooth,q = True,t = True,ws = True)
        rig.select(cl = True)
        upJnt = rig.joint(n = UpTooth.replace('_P', ''))
        rig.xform(upJnt,t = upPos,ws = True)
        rig.select(cl = True)
        dnJnt = rig.joint(n = DnTooth.replace('_P', ''))  
        rig.xform(dnJnt,t = dnPos,ws = True)              
        
#        nurbsControl
        self.controller.setColor(6)
        self.controller.setObjScale([0.2*self.scaleVal,0.2*self.scaleVal,-0.2*self.scaleVal])
        upCon = self.controller.SK_b09('UpTooth_M')
        dnCon = self.controller.SK_b09('DnTooth_M')
        rig.xform(upCon,t = upPos,ws = True)
        rig.xform(dnCon,t = dnPos,ws = True)
        upGrp = rig.group(upCon,n = upCon+'GRP',r = True)
        dnGrp = rig.group(dnCon,n = dnCon+'GRP',r = True)
        rig.makeIdentity(upCon,apply = True,s = True,r = True,t = True,jointOrient = True)
        rig.makeIdentity(dnCon,apply = True,s = True,r = True,t = True,jointOrient = True)

        rig.parent(upJnt,upCon)
        rig.parent(dnJnt,dnCon)
        rig.connectAttr('Jaw_M.vis_second',upGrp+'.visibility')
        rig.connectAttr('Jaw_M.vis_second',dnGrp+'.visibility')
        rig.skinCluster(upJnt,upTooth,tsb = True,n = 'UpTooth_Skin')
        rig.skinCluster(dnJnt,dnTooth,tsb = True,n = 'DnTooth_Skin')
        
#        rig.parent(dnGrp,'Jaw_UPB_JNT')
        rig.parent(upGrp,dnGrp,self.faceRig)
        rig.parentConstraint('Jaw_UPB_JNT',dnGrp,mo = True)
        
        
    def tongueSetup(self,tongue):
        JNT = 'Tongue_1_JNT_P'  
        cons = rig.listRelatives(JNT,c = True,ad = True)
        cons.append('Tongue_1_JNT_P')
        rig.select(cl = True)
        sign = ''
        conGrp = []
        NewJNTS = []
        for con in cons:
            pos = rig.xform(con,q = True,t = True,ws = True)
            jnt = rig.joint(n = con.replace('_P',''))
            self.controller.setColor(15)
            jntCon = self.controller.SK_b08(jnt+'_M')
            rig.setAttr(jntCon+'.rx',90)
            rig.xform(jntCon,t = pos,ws = True)
            rig.xform(jnt,t = pos,ws = True)
            rig.parent(jnt,jntCon)
            conUpGrp1 = rig.group(jntCon,n = jntCon+'_GRP1',r = True)
            conUpGrp2 = rig.group(conUpGrp1,n = jntCon+'_GRP2',r = True)
            
            if sign:
                rig.parent(sign,jnt)
            sign = conUpGrp2
            
            conGrp.append(conUpGrp1)
            NewJNTS.append(jnt)
            
        con = 'Tongue_M'
        rig.addAttr(con,at = 'enum',ln = 'vis_second',en = 'OFF:ON:',k = False)
        rig.setAttr(con+'.vis_second',cb = True)
        rig.makeIdentity('Tongue_1_JNT_M_GRP2',apply = True,t = True,r = True,s = True,jointOrient = True)  
        rig.connectAttr(con+'.vis_second','Tongue_1_JNT_M_GRP2.visibility')  
        rig.select(cl = True)
        
        
        sc = self.scaleVal
        rig.parent(con,w = True)
        rig.makeIdentity(con,apply = True,s = True,r = True,t = True)
        
#        newConGrp：组为排除根部第一个组
        removeGrp = conGrp[-1]
        newConGrp = conGrp.remove(removeGrp)
        
        conSR = rig.createNode('setRange',n = 'TongueRG',ss = True)
        rig.connectAttr(con+'.tx',conSR+'.valueX')
        rig.connectAttr(con+'.ty',conSR+'.valueY')
        rig.connectAttr(con+'.tz',conSR+'.valueZ')
        rig.setAttr(conSR+'.oldMaxX',0.5*sc)
        rig.setAttr(conSR+'.oldMaxY',0.5*sc)
        rig.setAttr(conSR+'.oldMaxZ',2*sc)
        rig.setAttr(conSR+'.oldMinX',-0.5*sc)
        rig.setAttr(conSR+'.oldMinY',-0.5*sc)
        rig.setAttr(conSR+'.oldMinZ',-2*sc)
        rig.setAttr(conSR+'.maxX',20)
        rig.setAttr(conSR+'.maxY',-20)
        rig.setAttr(conSR+'.maxZ',0.5*sc)
        rig.setAttr(conSR+'.minX',-20)
        rig.setAttr(conSR+'.minY',20)
        rig.setAttr(conSR+'.minZ',-0.5*sc)

#        连接舌头的旋转
        for grp in conGrp:
            addName = grp.split('_JNT_')[0]
            rig.addAttr(con,at = 'float',ln = addName,dv = 1)
            rig.addAttr(grp,at = 'float',ln = 'SV',dv = 1)
            rig.connectAttr(con+'.'+addName,grp+'.SV')
            
            rig.connectAttr(con+'.rz',grp+'.rz')
            MD = rig.createNode('multiplyDivide',n = grp+'_MD',ss = True)
            rig.connectAttr(grp+'.SV',MD+'.input1X')
            rig.connectAttr(con+'.rx',MD+'.input2X')
            rig.connectAttr(MD+'.outputX',grp+'.rx')
            
            rig.connectAttr(grp+'.SV',MD+'.input1Y')
            rig.connectAttr(con+'.ry',MD+'.input2Y')
            rig.connectAttr(MD+'.outputY',grp+'.ry')
            
            rig.connectAttr(conSR+'.outValue.outValueZ',grp+'.tz')
            
#        连接舌头的位移和缩放
        rig.connectAttr(con+'.tx','Tongue_1_JNT_M_GRP1.tx')
        rig.connectAttr(con+'.ty','Tongue_1_JNT_M_GRP1.ty')
        rig.connectAttr(con+'.sx','Tongue_1_JNT_M_GRP1.sx')
        rig.connectAttr(con+'.sy','Tongue_1_JNT_M_GRP1.sy')
        rig.connectAttr(con+'.sz','Tongue_1_JNT_M_GRP1.sz')
                    
        rig.transformLimits(con,tx  =  (-1*0.5*sc,0.5*sc),erx = (1, 1))
        rig.transformLimits(con,tx  =  (-1*0.5*sc,0.5*sc),etx = (1, 1))
        rig.transformLimits(con,ty  =  (-1*0.5*sc,0.5*sc),erx = (1, 1))
        rig.transformLimits(con,ty  =  (-1*0.5*sc,0.5*sc),ety = (1, 1))
        rig.transformLimits(con,tz  =  (-1*0.5*sc,0.5*sc),erx = (1, 1))
        rig.transformLimits(con,tz  =  (-1*2.0*sc,2.0*sc),etz = (1, 1))
        
        rig.skinCluster(NewJNTS,tongue,tsb = True,n = 'Tongue_Skin')
        
        grpA = rig.group(con,n = con+'_GRPA',r = True)
        grpB = rig.group(grpA,n = con+'_GRPB',r = True)
        rig.parent(grpB,'Tongue_1_JNT_M_GRP2',self.faceRig)
        rig.parentConstraint('Jaw_UPB_JNT','Tongue_1_JNT_M_GRP2',mo = True)
        self.Lock.hideInvertAttr(con,('translateZ','translateY','translateX','vis_Second','rotateX','rotateY','rotateZ','scaleX','scaleY','scaleZ'))
        
    def eyebrowSetup(self,lfEyebrow,rtEyebrow):
        SV = rig.getAttr('Face_Scale_Grp.scaleVal')
        LfJnts = rig.ls('Lf_ebw_*_M_JNT')
        LfCons = rig.ls('Lf_ebw_*_M')
        LfAkinMesh,LfAkinJnt,LfAllGrp,LfNewCons = SK_FollicleControl(LfCons,2,SV,'Lf_eyeBrow','Lf_eyeBrow_Loft','Face_Scale_Grp')
        RtJnts = rig.ls('Rt_ebw_*_M_JNT')
        RtCons = rig.ls('Rt_ebw_*_M')
        RtAkinMesh,RtAkinJnt,RtAllGrp,RtNewCons = SK_FollicleControl(RtCons,2,SV,'Rt_eyeBrow','Rt_eyeBrow_Loft','Face_Scale_Grp')
        
        #生成blendShape
        LfUP = rig.duplicate(LfAkinMesh,n = LfAkinMesh+'_UP')   
        LfDN = rig.duplicate(LfAkinMesh,n = LfAkinMesh+'_DN') 
        LfLF = rig.duplicate(LfAkinMesh,n = LfAkinMesh+'_LF') 
        LfRT = rig.duplicate(LfAkinMesh,n = LfAkinMesh+'_RT') 
        RtUP = rig.duplicate(RtAkinMesh,n = RtAkinMesh+'_UP')   
        RtDN = rig.duplicate(RtAkinMesh,n = RtAkinMesh+'_DN') 
        RtLF = rig.duplicate(RtAkinMesh,n = RtAkinMesh+'_LF') 
        RtRT = rig.duplicate(RtAkinMesh,n = RtAkinMesh+'_RT') 
        rig.blendShape(LfUP,LfDN,LfLF,LfRT,LfAkinMesh,n = LfAkinMesh+'_BS')   
        rig.blendShape(RtUP,RtDN,RtLF,RtRT,RtAkinMesh,n = RtAkinMesh+'_BS') 
        
        rig.skinCluster(LfJnts,LfAkinMesh,tsb = True,n = 'Lf_eyeBrow_M_Skin')
        rig.skinCluster(LfAkinJnt,lfEyebrow,tsb = True,n = 'Lf_eyeBrow_Skin')
        rig.skinCluster(RtJnts,RtAkinMesh,tsb = True,n = 'Rt_eyeBrow_M_Skin')
        rig.skinCluster(RtAkinJnt,rtEyebrow,tsb = True,n = 'Rt_eyeBrow_Skin')
#        隐藏以前眉毛控制器
        LfCons.extend(RtCons)
        LfNewCons.extend(RtNewCons)
        rig.addAttr('All_FOLS_GRP',at = 'enum',ln = 'eyeBrow_Vis',en = 'OFF:ON:',k = True,dv = 0)
        for i,con in enumerate(LfCons):
            conShape = rig.listRelatives(con,s = True)[0]
            rig.setAttr(conShape+'.overrideColor',6)
            rig.connectAttr('All_FOLS_GRP.eyeBrow_Vis',con+'.visibility')
            UpCon = rig.listRelatives(LfNewCons[i],p = True)[0]
            rig.connectAttr('Jaw_M.vis_second',UpCon+'.visibility')
                             
        rig.parent(LfAllGrp,RtAllGrp,'All_FOLS_GRP')

        

        
        
    def faceBsSetup(self,faceInfo):
        
        pass
    def extraControl(self):
        rig.setAttr('Face_Con.visibility',0)
        
    def combine(self):
        head = self.getTFstr(self.face.headTF)
        skinHead = self.getTFstr(self.face.skinHeadTF)
        lfEye = self.getTFstr(self.face.loadLfEyeTF)
        rtEye = self.getTFstr(self.face.loadRtEyeTF)
        upTooth = self.getTFstr(self.face.loadUpToothTF)
        dnTooth = self.getTFstr(self.face.loadDnToothTF)
        lfEyebrow = self.getTFstr(self.face.loadLfEyebrowTF)
        rtEyebrow = self.getTFstr(self.face.loadRtEyebrowTF)
        tongue = self.getTFstr(self.face.loadTongueTF)
        faceInfo = self.getTFstr(self.face.bsFaceTF)
        
        
        self.genBaseFace(head)
        self.connectFaceModel(skinHead)
        if self.eyeSn:
            self.eyeSetup(lfEye,rtEye)
        if self.toothSn:
            self.toothSetup(upTooth,dnTooth)
        if self.toothSn:
            self.tongueSetup(tongue)
        if self.eyebrowSn:
            self.eyebrowSetup(lfEyebrow, rtEyebrow)
        if self.faceSn:
            self.faceBsSetup(faceInfo)
        self.extraControl()
        
    
        