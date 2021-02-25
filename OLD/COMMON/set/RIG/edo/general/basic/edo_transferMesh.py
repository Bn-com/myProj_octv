import maya.cmds as cmds
def edo_transferMesh():
    sels=cmds.ls(sl=1)
    if sels==None or sels==[]:
        cmds.confirmDialog( title='error', message='you must select something', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if not len(sels)>=2:
        cmds.confirmDialog( title='error', message='you must select more than two mesh', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    sc=sels[0]
    dt=sels[1]
    input=cmds.listConnections(dt+'.inMesh',s=1,d=0)
    if not input==None:
        cmds.confirmDialog( title='error', message='the direct mesh is connected,check it!', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    else:
        edo_setMeshVertexsZero(dt)
        cmds.connectAttr(sc+'.outMesh',dt+'.inMesh',f=1)
        edo_setMeshVertexsZero(dt)
        cmds.disconnectAttr(sc+'.outMesh',dt+'.inMesh')
        
def edo_transferMeshes():
    sels=cmds.ls(sl=1)
    sc=sels[0]
    for i in range(1,len(sels)):
        dt=sels[i]
        cmds.select(sc)
        cmds.select(dt,add=1)
        edo_transferMesh()


def edo_setMeshVertexsZero(mesh):
    #mesh='BS_facial_eb_inup6'
    print 'reset vertex position!'
    num=cmds.polyEvaluate(mesh,v=1)
    for n in range(0,num):
        #n=56
        #print n
        vertex=mesh+'.vtx['+str(n)+']'
        cmds.setAttr(vertex+'.pntx',0)
        cmds.setAttr(vertex+'.pnty',0)
        cmds.setAttr(vertex+'.pntz',0)