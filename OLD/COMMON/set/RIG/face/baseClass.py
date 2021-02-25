import maya.cmds as rig


class LockHideAttr(object):
    def __init__(self,Tr = True,Ro = True,Sc = True,Vis = True):
        self.Tr = Tr
        self.Ro = Ro
        self.Sc = Sc
        self.Vis = Vis
    def hideAndLockObj(self,obj):
        transAttr = [u'translateX', u'translateY', u'translateZ']
        scaleAttr = [u'scaleX', u'scaleY', u'scaleZ']
        rotateAttr = [u'rotateX', u'rotateY', u'rotateZ']
        
        if not (self.Tr):
            for AttrName in transAttr:
               rig.setAttr(obj+'.'+AttrName,cb = False,k = False,l = True)
    
        if not (self.Ro):
            for AttrName in rotateAttr:
                rig.setAttr(obj+'.'+AttrName,cb = False,k = False,l = True)
                   
        if not (self.Sc):
            for AttrName in scaleAttr:
                rig.setAttr(obj+'.'+AttrName,cb = False,k = False,l = True)     
                   
        if not (self.Vis):
            rig.setAttr(obj+'.visibility',cb = False,k = False,l = True)           
       
    def hideInvertAttr(self,obj,inputAtt = []):
        attrs = rig.listAttr(obj,k = True)
        if attrs:
            for att in attrs:
                if inputAtt and att in inputAtt:
                    pass
                else:
                    rig.setAttr(obj+'.'+att,l = True,k = False)

class MirrorCurveController(object):
    def __init__(self):
        self.sign = 'morcoCon'
        self.Lf= 'Lf'
        self.Rt = 'Rt'
        
    def mirrorMicorContrl(self,controls):
        for con in controls:
            if(self.Lf in con.split('_')[0]):
#                print con
                pos = rig.xform(con,q = True,t = True,ws = True)
#                print pos
                ro = rig.xform(con,q = True,ro = True,ws = True)
                pos[0] = pos[0]*-1
                ro[1] = ro[1]*-1
                ro[2] = ro[2]*-1
                RtName = con.replace(self.Lf,self.Rt)
#                print RtName
#                print pos
                rig.xform(RtName,t = pos,ws = True)
                rig.xform(RtName,ro = ro,ws = True)
                
#                rig.xform(con,t = [0,0,0],wd = True)
#                rig.xform(con,ro = [0,0,0],wd = True)   
   
class unLockAttr(object):
    def __init__(self,Tr = True,Ro = True,Sc = True,Vis = True):
        self.Tr = Tr
        self.Ro = Ro
        self.Sc = Sc
        self.Vis = Vis
    def unLockObj(self,obj):
        transAttr = [u'translateX', u'translateY', u'translateZ']
        scaleAttr = [u'scaleX', u'scaleY', u'scaleZ']
        rotateAttr = [u'rotateX', u'rotateY', u'rotateZ']
        
        if not (self.Tr):
            for AttrName in transAttr:
               rig.setAttr(obj+'.'+AttrName,k = True,l = False)
    
        if not (self.Ro):
            for AttrName in rotateAttr:
                rig.setAttr(obj+'.'+AttrName,k = True,l = False)
                   
        if not (self.Sc):
            for AttrName in scaleAttr:
                rig.setAttr(obj+'.'+AttrName,k = True,l = False)     
                   
        if not (self.Vis):
            rig.setAttr(obj+'.visibility',k = True,l = False)  
            
def SK_createCompoundAttrs(outName,num):
    setStrs = []
    upName = 'Boss'
    midName = 'data'
    lowName = 'bess'
    
    outDataName = 'inData'
    suffix = 0
    
    objSC = rig.createNode('choice',n = outName.split('_')[0]+'_SC',ss = True)
    rig.addAttr(objSC,longName=upName, numberOfChildren=num, attributeType='compound' )
    rig.addAttr(outName,longName=outDataName, numberOfChildren=num, attributeType='compound')

    for i in range(num):
        rig.addAttr(outName, longName='out'+lowName+str(i), attributeType='double') 
        rig.addAttr(outName, longName=lowName+str(i), attributeType='double',parent = outDataName) 
        rig.addAttr(objSC,longName=midName+str(i), numberOfChildren=num, attributeType='compound',p = upName )
        for j in range(num):
            suffix += 1
            if(i == j):
                setStrs.append('.'+upName+'.'+midName+str(i)+'.'+lowName+str(suffix))
                rig.addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )
            else:
                rig.addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )            

    for i,attrName in enumerate(setStrs):
        rig.connectAttr(outName+'.'+outDataName+'.'+lowName+str(i),outName+'.out'+lowName+str(i))
        rig.connectAttr(objSC+'.'+upName+'.'+midName+str(i),objSC+'.input['+str(i)+']')
        rig.setAttr(objSC+attrName,1)
        
    rig.connectAttr(objSC+'.output',outName+'.'+outDataName)
        
    return objSC   

def SK_ConOrientation(con):
    orCon = ['_pull_','_dnLip_','_upLip_','_mouth_M','_dnEyelid_','_upEyelid_','_canthusOut_','_canthusIn_']
    sign = False
    for subCon in orCon:
        if subCon in con:
            sign = True

    MirrorGRP = con+'_Mirror_GRP'
    rig.xform(MirrorGRP,ro = (0,0,0),wd = True)
    MirrorMatrix = rig.getAttr(MirrorGRP+'.worldMatrix[0]')
    aimEmptyGrp = rig.group(n = MirrorGRP+'_Aim',empty = True)
    rig.xform(aimEmptyGrp,matrix = MirrorMatrix)
    rig.parent(aimEmptyGrp,MirrorGRP)
    rig.setAttr(aimEmptyGrp+'.tz',1)
    rig.parent(aimEmptyGrp,w = True)
    rig.aimConstraint(aimEmptyGrp,MirrorGRP,aimVector = (0,0,1),upVector = (0,1,0),worldUpType = 'scene')
    rig.delete(aimEmptyGrp)
    if sign:
        MirrorGRP = con+'_Mirror_GRP'
        MirrorMatrix = rig.getAttr(MirrorGRP+'.worldMatrix[0]')
        aimEmptyGrp = rig.group(n = MirrorGRP+'_Aim',empty = True)
        rig.xform(aimEmptyGrp,matrix = MirrorMatrix)
        rig.parent(aimEmptyGrp,MirrorGRP)
        rig.setAttr(aimEmptyGrp+'.tx',1)
        rig.parent(aimEmptyGrp,w = True)
        rig.aimConstraint(aimEmptyGrp,MirrorGRP,aimVector = (1,0,0),upVector = (0,1,0),worldUpType = 'vector',worldUpVector = (0,1,0))
        rig.delete(aimEmptyGrp)      
 
 
def SK_mirrorEyebrowBS():
    eyebrowMeshs = [u'Lf_eyeBrow_Loft_UP', u'Lf_eyeBrow_Loft_DN', u'Lf_eyeBrow_Loft_LF', u'Lf_eyeBrow_Loft_RT']
    for eyebrow in eyebrowMeshs:
        LfEyebrow = eyebrow
        RtEyebrow = eyebrow.replace('Lf_','Rt_')
        rig.xform(LfEyebrow,t = (0,0,0),wd = True)
        rig.xform(LfEyebrow,ro = (0,0,0),wd = True)  
        rig.xform(RtEyebrow,t = (0,0,0),wd = True)
        rig.xform(RtEyebrow,ro = (0,0,0),wd = True)  
        cvs = rig.ls(LfEyebrow+'.cv[*][*]',fl = True)
        for cv in cvs:
            RtCv = cv.replace('Lf_','Rt_')
            pos = rig.xform(cv,q = True,t = True,ws = True)
            pos[0] = pos[0]*-1
            rig.xform(RtCv,t = pos,ws = True)    
       
       
def SK_mirrorRoateCons(obj):
    MorrirGrp = obj+'_Mirror_GRP'
    RX = MorrirGrp+'.rx'
    RY = MorrirGrp+'.ry'
    RZ = MorrirGrp+'.rz'
    DRX = rig.listConnections(RX,s = True,d = False,p = True)
    DRY = rig.listConnections(RY,s = True,d = False,p = True)
    DRZ = rig.listConnections(RZ,s = True,d = False,p = True)
    if DRX:
        rig.disconnectAttr(DRX[0],RX)
        rig.disconnectAttr(DRY[0],RY)
        rig.disconnectAttr(DRZ[0],RZ)
    
        OCT = obj+'_OCT'
        UpLoc = rig.spaceLocator(n = obj+'_Position_Up_Face_LOC')[0]
        AimLoc = rig.spaceLocator(n = obj+'_Position_Aim_Face_LOC')[0]
        LocGrp = rig.group(UpLoc,AimLoc,n = obj+'_Loc_GRP')
        Pos = rig.xform(obj,q = True,t = True,ws = True)
        rig.parent(LocGrp,obj)
        rig.xform(LocGrp,t = Pos,ws = True)
        rig.makeIdentity(LocGrp,apply = True,s = True,r = True,t = True)
        rig.setAttr(UpLoc+'.ty',1)  
        rig.setAttr(AimLoc+'.tz',1)
        rig.parent(UpLoc,w = True)     
        rig.parent(AimLoc,w = True) 
        AimCons = rig.aimConstraint(AimLoc,MorrirGrp,aimVector = (0,0,1),upVector = (0,1,0),worldUpType = 'object',worldUpObject = UpLoc)         
        rig.delete(AimCons,AimLoc,LocGrp,UpLoc)
           
        Ro = rig.xform(MorrirGrp,q = True,ro = True,wd = True)
        WsRo = rig.xform(MorrirGrp,q = True,ro = True,ws = True)
        rig.setAttr(MorrirGrp+'.X',Ro[0])
        rig.setAttr(MorrirGrp+'.Y',Ro[1])
        rig.setAttr(MorrirGrp+'.Z',Ro[2])               
        rig.connectAttr(DRX[0],RX)
        rig.connectAttr(DRY[0],RY)
        rig.connectAttr(DRZ[0],RZ)
        rig.setAttr(OCT+'.offsetX',WsRo[0])
        rig.setAttr(OCT+'.offsetY',WsRo[1])
        rig.setAttr(OCT+'.offsetZ',WsRo[2])
        rig.xform(obj,ro = (0,0,0),wd = True) 
        
    else:

        UpLoc = rig.spaceLocator(n = obj+'_Position_Up_Face_LOC')[0]
        AimLoc = rig.spaceLocator(n = obj+'_Position_Aim_Face_LOC')[0]
        LocGrp = rig.group(UpLoc,AimLoc,n = obj+'_Loc_GRP')
        Pos = rig.xform(obj,q = True,t = True,ws = True)
        rig.parent(LocGrp,obj)
        rig.xform(LocGrp,t = Pos,ws = True)
        rig.makeIdentity(LocGrp,apply = True,s = True,r = True,t = True)
        rig.setAttr(UpLoc+'.ty',1)  
        rig.setAttr(AimLoc+'.tz',1)
        rig.parent(UpLoc,w = True)     
        rig.parent(AimLoc,w = True) 
        AimCons = rig.aimConstraint(AimLoc,MorrirGrp,aimVector = (0,0,1),upVector = (0,1,0),worldUpType = 'object',worldUpObject = UpLoc)         
        rig.delete(AimCons,AimLoc,LocGrp,UpLoc)
        rig.xform(obj,ro = (0,0,0),wd = True)      
