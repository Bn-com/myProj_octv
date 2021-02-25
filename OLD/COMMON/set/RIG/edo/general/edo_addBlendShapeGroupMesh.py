import maya.cmds as cmds
def edo_addBlendShapeGroupMesh():
    sels=cmds.ls(sl=1)
    s=sels[0]
    for i in range(1,len(sels)):
        #i=1
        grp=sels[i]
        d=cmds.duplicate(s)
        ds=cmds.listRelatives(d,s=1)[0]
        cmds.parent(ds,grp,s=1,r=1)
        cmds.rename(ds,grp+'Shape')
        cmds.delete(d)
    cmds.delete(s)