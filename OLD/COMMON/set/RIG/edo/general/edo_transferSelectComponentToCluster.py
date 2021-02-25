import maya.cmds as cmds
import maya.mel as mel
def edo_transferSelectComponentToCluster():
    piv=edo_findSelectComponentPiv()
    sel=cmds.ls(sl=1,o=1)[0]
    vtxlen=cmds.polyEvaluate(sel,v=1)
    pnt=[]
    for i in range(0,vtxlen):
        #i=0
        pnt.append(cmds.xform(sel+'.vtx['+str(i)+']',q=1,os=1,t=1))
    cmds.move(0,100,0,r=1,os=1,wd=1)
    npnt=[]
    for i in range(0,vtxlen):
        #i=0
        npnt.append(cmds.xform(sel+'.vtx['+str(i)+']',q=1,os=1,t=1))
    cmds.move(0,-100,0,r=1,os=1,wd=1)
    weight=[]
    for i in range(0,vtxlen):
        #i=0
        weight.append((npnt[i][1]-pnt[i][1])*0.01)
    cmds.select(sel)
    cd=mel.eval('newCluster "-envelope 1";')
    grp=cmds.group(cd[1],n='GRP_'+cd[1])
    cmds.connectAttr(cd[1]+'.parentInverseMatrix[0]',cd[0]+'.bindPreMatrix',f=1)
    rp=cmds.xform(grp,q=1,ws=1,rp=1)
    piv=[piv[0]-rp[0],piv[1]-rp[1],piv[2]-rp[2]]
    cmds.xform(grp,ws=1,r=1,t=piv)
    for i in range(0,vtxlen):
        #i=0
        cmds.percent(cd[0],sel+'.vtx['+str(i)+']',v=weight[i])
    cmds.select(cd[1])
        
def edo_findSelectComponentPiv():
    osels=cmds.ls(sl=1,fl=1)
    cmds.ConvertSelectionToVertices()
    sels=cmds.ls(sl=1,fl=1)
    mxx=0
    mxy=0
    mxz=0
    mix=0
    miy=0
    miz=0
    for sel in sels:    
        tpiv=cmds.xform(sel,q=1,ws=1,t=1)
        if sel==sels[0]:
            mxx=tpiv[0]
            mix=tpiv[0]
            mxy=tpiv[1]
            miy=tpiv[1]
            mxz=tpiv[2]
            miz=tpiv[2]
            continue
        if tpiv[0]>mxx:
            mxx=tpiv[0]
        if tpiv[1]>mxy:
            mxy=tpiv[1]
        if tpiv[2]>mxz:
            mxz=tpiv[2]
        if tpiv[0]<mix:
            mix=tpiv[0]
        if tpiv[1]<miy:
            miy=tpiv[1]
        if tpiv[2]<miz:
            miz=tpiv[2]
    pt=[(mxx+mix)*0.5,(mxy+miy)*0.5,(mxz+miz)*0.5]
    cmds.select(osels)
    return pt