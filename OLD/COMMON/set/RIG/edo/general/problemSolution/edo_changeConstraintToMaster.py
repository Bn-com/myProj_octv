import maya.cmds as cmds
def edo_changeConstraintToMaster():
    sels=cmds.ls(sl=1)
    for sel in sels:
        #sel=sels[0]
        pas=cmds.listRelatives(sel,c=1,pa=1)
        for pa in pas:
            if ':' in pa:
                #pa='do4_p416001Smartphone:PROP'
                ns=pa.replace(pa.split(':')[-1],'')
                mas=ns+'Master'
                if cmds.objExists(mas):
                    edo_changeConnections(sel,mas,'tx',0)
                    edo_changeConnections(sel,mas,'ty',0)
                    edo_changeConnections(sel,mas,'tz',0)
                    edo_changeConnections(sel,mas,'rx',0)
                    edo_changeConnections(sel,mas,'ry',0)
                    edo_changeConnections(sel,mas,'rz',0)
                    edo_changeConnections(sel,mas,'sx',1)
                    edo_changeConnections(sel,mas,'sy',1)
                    edo_changeConnections(sel,mas,'sz',1)
                    edo_changeConnections(sel,mas,'v',1)
                
def edo_changeConnections(org,new,attr,df):
    #org=sel
    #new=mas
    #attr='tx'
    #listConnectionsTX
    intx=cmds.listConnections(org+'.'+attr,s=1,d=0,p=1)
    if intx:
        cmds.disconnectAttr(intx[0],org+'.'+attr)
        cmds.connectAttr(intx[0],new+'.'+attr)
    else:
        tx=cmds.getAttr(org+'.'+attr)
        cmds.setAttr(new+'.'+attr,tx)
    cmds.setAttr(org+'.'+attr,df)