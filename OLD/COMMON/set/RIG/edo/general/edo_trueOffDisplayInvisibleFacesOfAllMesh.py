import maya.cmds as cmds
#edo_trueOffDisplayInvisibleFacesOfAllMesh(0)
def edo_trueOffDisplayInvisibleFacesOfAllMesh(value=False):
    meshes=cmds.ls(ni=1,type='mesh')
    for mesh in meshes:
        cmds.setAttr(mesh+'.difs',value)