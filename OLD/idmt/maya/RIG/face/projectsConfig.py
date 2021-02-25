#-*- coding: utf-8 -*-
import maya.cmds as rig
from maya.cmds import *
from RIG.face.baseClass import *
from RIG.face.controlers import CreateControler

def deleteFaceCon():
    rig.delete('Face_Con')
    
def ModifyControllerColorAndShape():
    exSphere = [u'Lf_canthusOut_M', u'Lf_canthusIn_M', u'Rt_canthusIn_M', u'Rt_canthusOut_M', u'Lf_mouth_M', u'Rt_mouth_M']#球形控制器
    SV = rig.getAttr('Face_Scale_Grp.scaleVal')
    controller = CreateControler(13,[0.05*SV,0.05*SV,0.05*SV])
    cons = rig.listConnections('Face_Scale_Grp.signA',s = False,d = True)
    for con in cons:
        conColor = 13 #控制器默认颜色
        if ('_dnEyelid_' in con) or ('_dnLip_' in con):
            conColor = 22
        
        controller.setColor(conColor)
        if con in exSphere:
            NewCon = controller.SK_b03('TemName_Controllers')
        else:
            NewCon = controller.SK_b08('TemName_Controllers') #新控制器默认形状
        

                   
        conShape = rig.listRelatives(con,s = True)
        rig.delete(conShape)
        NewConShape = rig.listRelatives(NewCon,s = True)[0]
        rig.rename(NewConShape,conShape)
        rig.setAttr(NewCon+'.tz',0.05*SV)
        rig.setAttr(NewCon+'.rx',90)
        rig.makeIdentity(NewCon,apply = True,r = True,t = True) 
        rig.parent(conShape,con,add = True,s = True)
        rig.delete(NewCon)

def addUpDnEyelid():
    Lock = LockHideAttr(False,False,False,False)
    SV = rig.getAttr('Face_Scale_Grp.scaleVal')
    controller = CreateControler(13,[0.06*SV,0.06*SV,0.06*SV])
    
    def modiUpDnEyelid(prefix ,SV,controller,RtV = 1):
        UpDnSign = False
        controller.setColor(13)
        if('_dn' in prefix):
            UpDnSign = True
            controller.setColor(22)
        
        Lf_up_Cons = [prefix+'Eyelid_1_M', prefix+'Eyelid_3_M']
        NewCon = rig.group(controller.SK_b14(prefix+'Eyelid_M'),n = prefix+'Eyelid_M_GRP')
        rig.setAttr(NewCon+'.tz',0.05*SV)
        rig.setAttr(NewCon+'.rx',90)
        if UpDnSign:
           rig.setAttr(NewCon+'.sy',-1) 
        rig.makeIdentity(NewCon,apply = True,r = True,t = True) 
        rig.setAttr(prefix+'Eyelid_M.sign',73)
        rig.connectAttr('Jaw_M.vis_second',NewCon+'.visibility')
        M = rig.getAttr(prefix+'Eyelid_1_M.worldMatrix')
        rig.xform(NewCon,matrix = M)
        rig.parent(NewCon,'Face_Rigging_GRP')
        rig.pointConstraint(Lf_up_Cons[0].replace('_1_M','_2_P_FOL'),NewCon)
        rig.hide(Lf_up_Cons[0].replace('_1_M','_2_M'))
        
        
        Lf_up_MD = rig.createNode('multiplyDivide',n = Lf_up_Cons[0].replace('_1_M','MD'),ss = True)
        rig.setAttr(Lf_up_MD+'.input2X',0.5)
        rig.setAttr(Lf_up_MD+'.input2Y',0.5)
        rig.setAttr(Lf_up_MD+'.input2Z',0.5)
        rig.connectAttr(prefix+'Eyelid_M.translate',Lf_up_MD+'.input1')
        for i,con in enumerate(Lf_up_Cons):
            sign = -1*RtV
            if (1 == i):
                sign = 1*RtV
                
            PMA = rig.createNode('plusMinusAverage',n = con+'_PMA',ss = True)
            rig.connectAttr(Lf_up_MD+'.output',PMA+'.input3D[0]')        
            rig.connectAttr(PMA+'.output3D',con+'_GRP.translate')
            
            RV = rig.createNode('remapValue',n = con+'_RV',ss = True)
            rig.setAttr(RV+'.inputMin',-30)
            rig.setAttr(RV+'.inputMax',30)
            rig.setAttr(RV+'.outputMin',-0.08*sign*SV)
            rig.setAttr(RV+'.outputMax',0.08*sign*SV)
            rig.connectAttr(prefix+'Eyelid_M.rz',RV+'.inputValue')
            rig.connectAttr(RV+'.outValue',PMA+'.input3D[1].input3Dy')
        Lock.hideInvertAttr(prefix+'Eyelid_M',('translateY','translateX','translateZ','rotateZ'))
        rig.transformLimits(prefix+'Eyelid_M',rz = (-30,30),erz = (1,1))    
        return NewCon
    
    AllControlGrp = []    
    AllControlGrp.append(modiUpDnEyelid('Lf_up',SV,controller))
    AllControlGrp.append(modiUpDnEyelid('Rt_up',SV,controller,-1))
    AllControlGrp.append(modiUpDnEyelid('Lf_dn',SV,controller))
    AllControlGrp.append(modiUpDnEyelid('Rt_dn',SV,controller,-1))
    GRP = rig.group(AllControlGrp,n = 'AddUpDnLid_GRP')
        
def addOrientConstrint():
    allCons = []
    allCons.extend(rig.ls('*_canthusOut_M'))
    allCons.extend(rig.ls('*_canthusIn_M'))
    allCons.extend(rig.ls('*_upEyelid_*_M'))
    allCons.extend(rig.ls('*_dnEyelid_*_M'))
    allCons.extend(rig.ls('*_upLip_*_M'))
    allCons.extend(rig.ls('*_dnLip_*_M'))
    allCons.extend(rig.ls('Mid_*Lip_M'))
    allCons.extend(rig.ls('*_mouth_M'))
    
    rig.addAttr('Jaw_M',at = 'enum',ln = 'normals',en = 'OFF:ON:',k = True)
    rig.setAttr('Jaw_M.normals',channelBox = True,k = False)
    rig.addAttr('Face_Scale_Grp',at = 'enum',ln = 'normals',en = 'OFF:ON:')
    rig.connectAttr('Jaw_M.normals','Face_Scale_Grp.normals')
    for con in allCons:
        Grp = con+'_Mirror_GRP'
        ro = rig.xform(Grp,q = True,ro = True,wd = True)
        rig.addAttr(Grp,at = 'float',ln = 'X',dv = ro[0])
        rig.addAttr(Grp,at = 'float',ln = 'Y',dv = ro[1])
        rig.addAttr(Grp,at = 'float',ln = 'Z',dv = ro[2])
        
        
        
        GrpFol = rig.listRelatives(Grp,p = True)[0]
#        OrientCons = rig.orientConstraint(GrpFol,'Face_Rigging_GRP',Grp,mo = True)[0]
#        RVS = rig.createNode('reverse',n = con+'_RVS')
#        rig.connectAttr('Jaw_M.normals',RVS+'.inputX')
#        rig.connectAttr(RVS+'.inputX',OrientCons+'.Face_Rigging_GRPW1')
#        rig.connectAttr(RVS+'.outputX',OrientCons+'.'+GrpFol+'W0')
        OrientCons = rig.orientConstraint('Face_Rigging_GRP',Grp,mo = True,n = con+'_OCT')[0]
        BC = rig.createNode('blendColors',n = con+'_BC')
        rig.connectAttr('Face_Scale_Grp.normals',BC+'.blender')
        rig.connectAttr(BC+'.outputR',Grp+'.rx',f = True)
        rig.connectAttr(BC+'.outputG',Grp+'.ry',f = True)
        rig.connectAttr(BC+'.outputB',Grp+'.rz',f = True)
        rig.connectAttr(OrientCons+'.constraintRotate',BC+'.color2')
        rig.connectAttr(Grp+'.X',BC+'.color1.color1R')    
        rig.connectAttr(Grp+'.Y',BC+'.color1.color1G')     
        rig.connectAttr(Grp+'.Z',BC+'.color1.color1B')   

def setJawGrpPovit():
    pos = rig.xform('Jaw_UP_JNT',q = True,t = True,ws = True)
    rig.move(pos[0],pos[1],pos[2],'Jaw_M_GRPA.scalePivot','Jaw_M_GRPA.rotatePivot')
    
def setRedEyeCon():
    def ReRV(RV):
        minV = rig.getAttr(RV+'.outputMin')
        maxV = rig.getAttr(RV+'.outputMax') 
        minV = minV*-1
        maxV = maxV*-1
        rig.setAttr(RV+'.outputMin',minV)
        rig.setAttr(RV+'.outputMax',maxV) 
    def inputScale(con,sc = [1,1,1],sign = False):
        rig.setAttr(con+'.sx',l = False)    
        rig.setAttr(con+'.sy',l = False)
        rig.setAttr(con+'.sz',l = False)
        if sign:
            rig.setAttr(con+'.sy',-1)
            rig.makeIdentity(con,apply = True,s = True)   
        rig.setAttr(con+'.sx',sc[0])    
        rig.setAttr(con+'.sy',sc[1])
        rig.setAttr(con+'.sz',sc[2]) 
        rig.setAttr(con+'.sx',l = True)    
        rig.setAttr(con+'.sy',l = True) 
        rig.setAttr(con+'.sz',l = True)        
             
#    left eye  
    inputScale('Lf_dnEyelid_M',(1,-1,1),True) 
    rig.setAttr('Lf_dnEyelidMD.input2X',0.5)
    rig.setAttr('Lf_dnEyelidMD.input2Y',0.5)
    rig.setAttr('Lf_dnEyelidMD.input2Z',0.5)    
#    ReRV('Lf_dnEyelid_1_M_RV')
#    ReRV('Lf_dnEyelid_3_M_RV')

#    right eye 
    inputScale('Rt_dnEyelid_M',(-1,-1,1),True) 
    inputScale('Rt_upEyelid_M',(-1,1,1))   
    rig.setAttr('Rt_dnEyelidMD.input2X',0.5)
    rig.setAttr('Rt_dnEyelidMD.input2Y',0.5)
    rig.setAttr('Rt_dnEyelidMD.input2Z',0.5)   
    rig.setAttr('Rt_upEyelidMD.input2X',0.5)
    rig.setAttr('Rt_upEyelidMD.input2Y',0.5)
    rig.setAttr('Rt_upEyelidMD.input2Z',0.5)     
    ReRV('Rt_upEyelid_1_M_RV')
    ReRV('Rt_upEyelid_3_M_RV')    
    ReRV('Rt_upEyelid_1_M_RV')
    ReRV('Rt_upEyelid_3_M_RV')       

#缺省配置
def Default_config():
    setJawGrpPovit()
    deleteFaceCon()
    ModifyControllerColorAndShape()
#    addUpDnEyelid()
    addOrientConstrint()
    
#    setRedEyeCon()

#RainbowRiders项目配置    
def RR_config():
    setJawGrpPovit()
    deleteFaceCon()
    ModifyControllerColorAndShape()
    addUpDnEyelid()
    addOrientConstrint()
    setRedEyeCon()

#WinxTV项目配置  
def WinxTV_config():
    setJawGrpPovit()
    deleteFaceCon()
    ModifyControllerColorAndShape()
#    addUpDnEyelid()
    addOrientConstrint()
    
#    setRedEyeCon()

def extraModify(face):
    if rig.radioButton(face.OrigenRB,q = True,sl = True):
        Default_config()
    elif rig.radioButton(face.RainbowRidersRB,q = True,sl = True):
        RR_config()
    elif rig.radioButton(face.WinxTVRB,q = True,sl = True):
        WinxTV_config()
    
