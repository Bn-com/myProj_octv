import maya.cmds as cmds
def edo_ikfkSwitch():
    sels=cmds.ls(sl=1)   
    for sel in sels:
        '''        
        #sel=sels[0]
        tok=sel.split(':')
        nameSpace=''
        if len(tok)>1:
            nameSpace=tok[0]+':'
        param=sel.split('_')[0]
        param=param.replace('LegLeg','Leg')
        swtichCtrl=nameSpace+param+'_'+'Switch'
        ikfk=cmds.getAttr(swtichCtrl+'.IKFK')
        '''        
        prefix = sel.split(':')
        nameSpace=''
        if len(prefix)>1:
            for i in range(len(prefix)-1):
                nameSpace=nameSpace+prefix[i]+':'        
        if len(prefix)==1:
            nameSpace=''
            
        CtrlName = sel.split(':')[-1]    
        param=CtrlName.split('_')[0]
        param=param.replace('LegLeg','Leg')
        swtichCtrl=nameSpace+param+'_'+'Switch'        
        ikfk=cmds.getAttr(swtichCtrl+'.IKFK')        
        if ikfk==0:
            edo_fkToIk(param,nameSpace)
        else:
            edo_ikToFk(param,nameSpace)

def edo_ikToFk(param,nameSpace):
    if 'Leg' in param:
        #nameSpace=''
        switch=nameSpace+param+'_Switch'
        ik=nameSpace+param+'_Leg_IK'
        pole=nameSpace+param+'_Pole_ctrl'
        upleg=nameSpace+param+'_Leg_FK'
        midleg=nameSpace+param+'_Knee_FK'
        lowleg=nameSpace+param+'_Ankle_FK'
        toe=nameSpace+param+'Leg_ball_FK'
    if 'Arm' in param:
        #nameSpace=''
        switch=nameSpace+param+'_Switch'
        ik=nameSpace+param+'_Wrist_IK'
        pole=nameSpace+param+'_Pole_ctrl'
        upleg=nameSpace+param+'_UpArm_FK'
        midleg=nameSpace+param+'_Elbow_FK'
        lowleg=nameSpace+param+'_Wrist_FK'
        toe=nameSpace+param+'_wristMid_FK'
    #upleg
    cmds.setAttr(upleg+'.rx',cmds.getAttr(upleg+'_location.rx'))
    cmds.setAttr(upleg+'.ry',cmds.getAttr(upleg+'_location.ry'))
    cmds.setAttr(upleg+'.rz',cmds.getAttr(upleg+'_location.rz'))
    #midleg
    cmds.setAttr(midleg+'.rx',cmds.getAttr(midleg+'_location.rx'))
    cmds.setAttr(midleg+'.ry',cmds.getAttr(midleg+'_location.ry'))
    cmds.setAttr(midleg+'.rz',cmds.getAttr(midleg+'_location.rz'))
    #lowleg
    cmds.setAttr(lowleg+'.rx',cmds.getAttr(lowleg+'_location.rx'))
    cmds.setAttr(lowleg+'.ry',cmds.getAttr(lowleg+'_location.ry'))
    cmds.setAttr(lowleg+'.rz',cmds.getAttr(lowleg+'_location.rz'))
    #lowleg
    cmds.setAttr(toe+'.rx',cmds.getAttr(toe+'_location.rx'))
    cmds.setAttr(toe+'.ry',cmds.getAttr(toe+'_location.ry'))    
    cmds.setAttr(toe+'.rz',cmds.getAttr(toe+'_location.rz'))
    #ikfkswitch
    cmds.setAttr(switch+'.IKFK',0)
    
    
def edo_fkToIk(param,nameSpace):
    if 'Leg' in param:
        #nameSpace=''
        switch=nameSpace+param+'_Switch'
        ik=nameSpace+param+'_Leg_IK'
        pole=nameSpace+param+'_Pole_ctrl'
        upleg=nameSpace+param+'_Leg_FK'
        midleg=nameSpace+param+'_Knee_FK'
        lowleg=nameSpace+param+'_Ankle_FK'
        toe=nameSpace+param+'Leg_ball_FK'
    if 'Arm' in param:
        switch=nameSpace+param+'_Switch'
        ik=nameSpace+param+'_Wrist_IK'
        pole=nameSpace+param+'_Pole_ctrl'
        upleg=nameSpace+param+'_UpArm_FK'
        midleg=nameSpace+param+'_Elbow_FK'
        lowleg=nameSpace+param+'_Wrist_FK'
        toe=nameSpace+param+'_wristMid_FK'
    #ik
    cmds.setAttr(ik+'.tx',cmds.getAttr(ik+'_location.tx'))
    cmds.setAttr(ik+'.ty',cmds.getAttr(ik+'_location.ty'))
    cmds.setAttr(ik+'.tz',cmds.getAttr(ik+'_location.tz'))
    cmds.setAttr(ik+'.rx',cmds.getAttr(ik+'_location.rx'))
    cmds.setAttr(ik+'.ry',cmds.getAttr(ik+'_location.ry'))
    cmds.setAttr(ik+'.rz',cmds.getAttr(ik+'_location.rz'))
    cmds.setAttr(ik+'.raiseToe',cmds.getAttr(toe+'_location.rz'))
    cmds.setAttr(ik+'.swivelToe',cmds.getAttr(toe+'_location.ry'))
    cmds.setAttr(ik+'.twistToe',cmds.getAttr(toe+'_location.rx'))
    #pole
    cmds.setAttr(pole+'.tx',cmds.getAttr(pole+'_location.tx'))
    cmds.setAttr(pole+'.ty',cmds.getAttr(pole+'_location.ty'))
    cmds.setAttr(pole+'.tz',cmds.getAttr(pole+'_location.tz'))
    #other
    if 'Leg' in param:
        cmds.setAttr(ik+'.raiseToeTip',0)
        cmds.setAttr(ik+'.side',0)
        cmds.setAttr(ik+'.swivel',0)
        cmds.setAttr(ik+'.roll',0)
    cmds.setAttr(ik+'.raiseBall',0)
    cmds.setAttr(switch+'.IKFK',1)