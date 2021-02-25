import maya.cmds as cmds
def edo_addTweakForModifyMesh():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
         return False
    for s in sels:
        #s=sels[0]
        cmds.select(s,r=1)
        tk=cmds.deformer(type='tweak',n='FS_tweak')
        cmds.connectAttr(tk[0]+'.vlist[0].vertex[0]',s+'.tweakLocation',f=1)
edo_addTweakForModifyMesh()