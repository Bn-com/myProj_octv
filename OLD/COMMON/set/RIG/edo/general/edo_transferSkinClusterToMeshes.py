def edo_transferSkinClusterToMeshes():
    sels=cmds.ls(sl=1)
    if not sels:
        print 'you must select the skinmesh and the ohers mesh!'
        return False
    sc=sels[0]
    for s in sels:
        #s=sels[1]
        if s==sels[0]:
            continue
        print 'transfer  ... '+sc+'\'s skincluster  to  ...  '+s
        edo_transferSkinClusterToMesh(sc,s)
    return True


def edo_transferSkinClusterToMesh(sc,dir):
    #dir=s
    sk=edo_findNodeFromHis(sc,'skinCluster')
    infs=cmds.skinCluster(sk,q=1,inf=1)
    cmds.skinCluster(infs,dir,tsb=1)
    cmds.copySkinWeights(sc,dir,noMirror=1,surfaceAssociation='closestPoint',influenceAssociation='closestJoint')

    
def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node=his
    return node