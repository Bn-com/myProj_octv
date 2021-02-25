import maya.cmds as cmds
def edo_mirrorCluster():
    sels=cmds.ls(sl=1)
    mesh=sels[0]
    cmds.setAttr(mesh+'.sx',10)
    cmds.setAttr(mesh+'.sy',10)
    cmds.setAttr(mesh+'.sz',10)
    mcwm=cmds.duplicate(mesh,n='MCW_'+mesh)[0]
    cmds.setAttr(mcwm+'.sx',-10)
    cmds.select(mcwm,r=1)
    cmds.select(mesh,add=1)
    mel.eval('CreateWrap')
    sels.remove(mesh)
    for c in sels:
        #c=sels[1]
        ovtxs=edo_getMeshVtxs(mcwm)
        cmds.setAttr(c+'.tz',100)
        cvtxs=edo_getMeshVtxs(mcwm)
        ws=edo_computeWeightFromList(ovtxs,cvtxs)
        cmds.setAttr(c+'.tz',0)
        cmds.setAttr(mesh+'.sx',1)
        cmds.setAttr(mesh+'.sy',1)
        cmds.setAttr(mesh+'.sz',1)
        cmds.select(mesh,r=1)
        clusters=mel.eval("newCluster \" -envelope 1\"")
        cmds.setAttr(mesh+'.sx',10)
        cmds.setAttr(mesh+'.sy',10)
        cmds.setAttr(mesh+'.sz',10)
        ch=clusters[1]
        cd=clusters[0]
        id=0
        for w in ws:
            #w=ws[0]
            cmds.setAttr(cd+'.weightList[0].weights['+str(id)+']',w)
            id+=1
        chg=cmds.createNode('transform',n='GRP_'+ch)
        piv=cmds.xform(c,q=1,ws=1,t=1)
        cmds.connectAttr(ch+'.parentInverseMatrix',cd+'.bindPreMatrix',f=1)
        cmds.parent(ch,chg)
        piv[0]=piv[0]*-1
        cmds.xform(chg,ws=1,t=piv)
    cmds.delete(mcwm)
    cmds.setAttr(mesh+'.sx',1)
    cmds.setAttr(mesh+'.sy',1)
    cmds.setAttr(mesh+'.sz',1)
    
        
def edo_computeWeightFromList(bf,ct):
    ws=[]
    l=len(bf)
    for i in range(0,l):
        bfz=bf[i][2]
        ctz=ct[i][2]
        w=(ctz-bfz)*0.001
        ws.append(w)
    return ws
        
def edo_getMeshVtxs(mesh):
    #mesh='MCW_pSphere1'
    vn=cmds.polyEvaluate(mesh,v=1)
    vtxs=[]
    for i in range(0,vn):
        #i=0
        vname=mesh+'.pnts['+str(i)+']'
        vp=cmds.xform(vname,q=1,ws=1,t=1)
        vtxs.append(vp)
    return vtxs

def edo_mirroClusterWeightToSelf():
    sels=cmds.ls(sl=1)
    mesh=sels[0]
    clus=sels[1]
    cmds.setAttr(mesh+'.sx',10)
    cmds.setAttr(mesh+'.sy',10)
    cmds.setAttr(mesh+'.sz',10)
    cs=cmds.listConnections(clus+'.worldMatrix',s=0,d=1)
    if cs:
        c=cs[0]
        cmds.setAttr(c+'.envelope',0)
        pxvs=edo_findHalfAxisPointFromMesh(mesh,'+x')
        cmds.setAttr(mesh+'.sx',1)
        cmds.setAttr(mesh+'.sy',1)
        cmds.setAttr(mesh+'.sz',1)
        edo_mirrorVertexesClusWeight(pxvs,c)
        cmds.setAttr(c+'.envelope',1)


def edo_findHalfAxisPointFromMesh(mesh,axis):
    #axis='+x'
    #mesh='pSphere1'
    mpointcount=cmds.polyEvaluate(mesh,v=1)
    ids=[]
    for i in range(0,mpointcount):
        #i=0
        vtx=mesh+'.vtx['+str(i)+']'
        position=cmds.xform(vtx,q=1,ws=1,t=1)
        if axis=='+x':
            if position[0]>0.1:
                ids.append(vtx)
    return ids
    
def edo_mirrorVertexesClusWeight(list,clus):
    #list=pxvs
    #clus=c
    cpom='edo_mirroClusterWeightToSelf_ClosestPointOnMesh'
    if not list:
        return False
    if not cmds.objExists(cpom):
        cmds.createNode('closestPointOnMesh',n=cpom)
    try:
        cmds.connectAttr(list[0].split('.')[0]+'.outMesh',cpom+'.inMesh',f=1)
    except:
        print 'connect closest poin on mesh false'
    for v in list:
        #len(list)
        #v='body1.vtx[3700]'
        pos=cmds.xform(v,q=1,ws=1,t=1)
        pos[0]=pos[0]*-1
        cmds.setAttr(cpom+'.inPositionX',pos[0])
        cmds.setAttr(cpom+'.inPositionY',pos[1])
        cmds.setAttr(cpom+'.inPositionZ',pos[2])
        vindex=cmds.getAttr(cpom+'.closestVertexIndex')
        weight=cmds.percent(clus,v,q=1,v=1)
        if not weight[0]==0:
            print 'percent ... '+clus+' ... '+v.split('.')[0]+'.vtx['+str(vindex)+'] ... '+str(weight[0])
        cmds.percent(clus,v.split('.')[0]+'.vtx['+str(vindex)+']',v=weight[0])
    cmds.delete(cpom)
    return True