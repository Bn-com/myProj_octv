import maya.cmds as cmds
##param='LfLeg' or 'RtLeg'
def edo_addLegTipIkCtrl(param):
    jnt=param[:2]+'_'+param[2:].lower()
    cmds.group(param+'_ALL_CTRL_GRP',n='GRP_'+param+'_ALL_CTRL_GRP')
    cmds.file('E:/mayaProject/nj_project/data/baseIkCtrl.mb',i=True)
    if param=='RtLeg':
        cmds.setAttr('baseIkCtrl.rz',-180)
        cmds.makeIdentity('baseIkCtrl',apply=True)
    cmds.rename('baseIkCtrl',param+'_tipIkCtrl')
    cmds.group(param+'_tipIkCtrl',n='GRP_'+param+'_tipIkCtrl')
    cmds.xform('GRP_'+param+'_tipIkCtrl',os=1,piv=[0,0,0])
    cmds.parent('GRP_'+param+'_tipIkCtrl',jnt+'_drv_jnt')
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.tx',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.ty',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.tz',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.rx',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.ry',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.rz',0)
    cmds.parent('GRP_'+param+'_tipIkCtrl','root_waist_ikCtrl')
    cmds.parent('GRP_'+param+'_ALL_CTRL_GRP',param+'_tipIkCtrl')
    cmds.sets(param+'_tipIkCtrl',add='bodySet')
    cmds.setAttr(param+'_tipIkCtrl.rx',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.ry',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.rz',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sx',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sy',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sz',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.v',lock=True,keyable=False,channelBox=False)
      
##param='LfArm' or 'RtArm'
def edo_addArmTipIkCtrl(param):
    jnt=param[:2]+'_up'+param[2:]
    cmds.group(param+'_ALL_CTRL_GRP',n='GRP_'+param+'_ALL_CTRL_GRP')
    cmds.file('E:/mayaProject/nj_project/data/baseIkCtrl.mb',i=True)
    if param=='RtArm':
        cmds.setAttr('baseIkCtrl.rz',-180)
        cmds.makeIdentity('baseIkCtrl',apply=True)
    cmds.rename('baseIkCtrl',param+'_tipIkCtrl')
    cmds.group(param+'_tipIkCtrl',n='GRP_'+param+'_tipIkCtrl')
    cmds.xform('GRP_'+param+'_tipIkCtrl',os=1,piv=[0,0,0])
    cmds.parent('GRP_'+param+'_tipIkCtrl',jnt+'_drv_jnt')
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.tx',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.ty',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.tz',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.rx',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.ry',0)
    cmds.setAttr('GRP_'+param+'_tipIkCtrl.rz',0)
    cmds.parent('GRP_'+param+'_tipIkCtrl',param[:2]+'_clavicle2_jnt')
    cmds.parent('GRP_'+param+'_ALL_CTRL_GRP',param+'_tipIkCtrl')
    cmds.sets(param+'_tipIkCtrl',add='bodySet')
    cmds.setAttr(param+'_tipIkCtrl.rx',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.ry',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.rz',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sx',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sy',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.sz',lock=True,keyable=False,channelBox=False)
    cmds.setAttr(param+'_tipIkCtrl.v',lock=True,keyable=False,channelBox=False)
    