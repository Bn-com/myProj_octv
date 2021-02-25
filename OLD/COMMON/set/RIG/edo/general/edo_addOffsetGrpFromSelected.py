def edo_addOffsetGrpFromSelected():
    sels=cmds.ls(sl=1)
    if sels:
        for s in sels:
            edo_addOffsetGrp(s)

def edo_addOffsetGrp(s):
    #s='r_armA_wrist_ctrl'
    if cmds.nodeType(s)=='joint':
        if not cmds.objExists('OFFSETJOINT_'+s):
            jnt=cmds.createNode('joint',n='OFFSETJOINT_'+s)
            pas=cmds.listRelatives(s,p=1,pa=1)
            if pas:
                cmds.parent(jnt,pas[0])
                edo_resetJoint(jnt)
                cmds.parent(s,jnt)
                edo_childTransformToParent(s,jnt)
        else:
            print 'the group is exists!'
    else:
        if not cmds.objExists('OFFSETTRANSFORM_'+s):
            grp=cmds.group(s,n='OFFSETTRANSFORM_'+s)
            edo_childTransformToParent(s,grp)
        else:
            print 'the group is exists!'


def edo_childTransformToParent(c,p):
    #c=s
    #p=grp
     cmds.setAttr(p+'.tx',cmds.getAttr(p+'.tx')+cmds.getAttr(c+'.tx'))
     cmds.setAttr(p+'.ty',cmds.getAttr(p+'.ty')+cmds.getAttr(c+'.ty'))
     cmds.setAttr(p+'.tz',cmds.getAttr(p+'.tz')+cmds.getAttr(c+'.tz'))
     try:
         cmds.setAttr(c+'.tx',0)
     except:
         print c+'.tx'+'....is locked'
     try:
         cmds.setAttr(c+'.ty',0)
     except:
         print c+'.ty'+'....is locked'
     try:
         cmds.setAttr(c+'.tz',0)
     except:
         print c+'.tz'+'....is locked'
     piv=cmds.xform(c,q=1,ws=1,rp=1)
     spiv=cmds.xform(c,q=1,ws=1,sp=1)
     cmds.xform(p,ws=1,rp=piv)
     cmds.xform(p,ws=1,sp=spiv)
     cmds.setAttr(p+'.rx',cmds.getAttr(p+'.rx')+cmds.getAttr(c+'.rx'))
     cmds.setAttr(p+'.ry',cmds.getAttr(p+'.ry')+cmds.getAttr(c+'.ry'))
     cmds.setAttr(p+'.rz',cmds.getAttr(p+'.rz')+cmds.getAttr(c+'.rz'))
     try:
         cmds.setAttr(c+'.rx',0)
     except:
         print c+'.rx'+'....is locked'
     try:
         cmds.setAttr(c+'.ry',0)
     except:
         print c+'.ry'+'....is locked'
     try:
         cmds.setAttr(c+'.rz',0)
     except:
         print c+'.rz'+'....is locked'
     cmds.setAttr(p+'.sx',cmds.getAttr(p+'.sx')+cmds.getAttr(c+'.sx')-1)
     cmds.setAttr(p+'.sy',cmds.getAttr(p+'.sy')+cmds.getAttr(c+'.sy')-1)
     cmds.setAttr(p+'.sz',cmds.getAttr(p+'.sz')+cmds.getAttr(c+'.sz')-1)
     try:
         cmds.setAttr(c+'.sx',1)
     except:
         print c+'.sx'+'....is locked'
     try:
         cmds.setAttr(c+'.sy',1)
     except:
         print c+'.sy'+'....is locked'
     try:
         cmds.setAttr(c+'.sz',1)
     except:
         print c+'.sz'+'....is locked'
     cmds.setAttr(p+'.rotateOrder',cmds.getAttr(c+'.rotateOrder'))
     
def edo_resetJoint(jnt):
    cmds.setAttr(jnt+'.tx',0)
    cmds.setAttr(jnt+'.ty',0)
    cmds.setAttr(jnt+'.tz',0)
    cmds.setAttr(jnt+'.rx',0)
    cmds.setAttr(jnt+'.ry',0)
    cmds.setAttr(jnt+'.rz',0)
    cmds.setAttr(jnt+'.sx',1)
    cmds.setAttr(jnt+'.sy',1)
    cmds.setAttr(jnt+'.sz',1)
    cmds.setAttr(jnt+'.jointOrientX',0)
    cmds.setAttr(jnt+'.jointOrientY',0)
    cmds.setAttr(jnt+'.jointOrientZ',0) 