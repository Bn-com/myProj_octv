import maya.cmds as cmds
import maya.mel as mel
def edo_outputCluster():
    sels=cmds.ls(sl=1)
    clus=sels[0]
    m=sels[1]
    bfvtxs=edo_getMeshVtxs(m)
    cmds.setAttr(clus+'.tz',100)
    ctvtxs=edo_getMeshVtxs(m)
    ws=edo_computeWeightFromList(bfvtxs,ctvtxs)
    cmds.setAttr(clus+'.tz',0)
    name=clus
    piv=cmds.xform(name,q=1,ws=1,t=1)
    spiv=edo_listToStr(piv)
    filename=''
    fn=cmds.fileDialog2(dialogStyle=1,fm=0)
    if fn==None:
        return False
    else:
        if fn[0].split('.')[-1]=='*':
            filename=fn[0].replace('*','clw')
        else:
            filename=fn[0]
    fobj=open(filename,'w')
    fobj.writelines(name+'\n')
    fobj.writelines(spiv+'\n')
    id=0
    for w in ws:
        wt=str(id)+':'+str(w)+'\n'
        fobj.writelines(wt)
        id+=1
    fobj.writelines('//theEnd')
    fobj.close()

def edo_importCluster():
    mesh=cmds.ls(sl=1)[0]
    clusters=mel.eval("newCluster \" -envelope 1\"")
    cd=clusters[0]
    ch=clusters[1]
    ws=[]
    filename=''
    fn=cmds.fileDialog2(dialogStyle=1,fm=1)
    if fn==None:
        return False
    else:
        if fn[0].split('.')[-1]=='*':
            filename=fn[0].replace('*','clw')
        else:
            filename=fn[0]
    fobj=open(filename,'r')
    l=fobj.readline()
    piv=fobj.readline().split(',')
    t=''
    while(not t=='//theEnd'):
        t=fobj.readline()
        if t=='//theEnd':
            break
        ws.append(t[:len(t)-1].split(':')[1])
    fobj.close()
    cmds.connectAttr(ch+'.parentInverseMatrix',cd+'.bindPreMatrix',f=1)
    id=0
    for w in ws:
        #w=ws[0]
        cmds.setAttr(cd+'.weightList[0].weights['+str(id)+']',float(w))
        id+=1
    nch=cmds.rename(ch,l)
    nchg=cmds.createNode('transform',n='GRP_'+nch)
    cmds.setAttr(nch+'.rotatePivotX',0)
    cmds.setAttr(nch+'.rotatePivotY',0)
    cmds.setAttr(nch+'.rotatePivotZ',0)
    cmds.setAttr(nch+'.scalePivotX',0)
    cmds.setAttr(nch+'.scalePivotY',0)
    cmds.setAttr(nch+'.scalePivotZ',0)
    cmds.parent(nch,nchg)
    cmds.xform(nchg,ws=1,t=[float(piv[0]),float(piv[1]),float(piv[2])])
    
        
        
    
def edo_listToStr(list):
    s=''
    for l in list:
        s+=(str(l)+',')
    return s[:len(s)-1]
      
def edo_computeWeightFromList(bf,ct):
    ws=[]
    l=len(bf)
    for i in range(0,l):
        bfz=bf[i][2]
        ctz=ct[i][2]
        w=(ctz-bfz)*0.01
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