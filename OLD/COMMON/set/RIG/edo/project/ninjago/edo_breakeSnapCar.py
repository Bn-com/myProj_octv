import maya.cmds as cmds
import maya.mel as mel
def edo_breakSnapCar():
    nameSpace=''
    sels=[]
    sels=cmds.ls(sl=1)
    if sels==[]:
        print 'you must select one MIS'
        return False
    for sel in sels:
        #sel=sels[0]
        nameSpace=sel.split(':')[0]
        locs=[]
        locs=cmds.ls(nameSpace+':*_LOC_Geometry')
        for loc in locs:
            #loc=locs[0]
            gc=cmds.listConnections(loc+'.geometry',s=1,d=0,type='geometryConstraint')
            if not gc==None:
                print 'delete  ......  '+gc[0]
                cmds.delete(gc)
        pcg=[]
        pcg=cmds.ls(nameSpace+':*Path_Car_Grp')
        for pc in pcg:
            #pc=pcg[0]
            mp=cmds.listConnections(pc+'.rotateOrder',s=1,d=0,type='motionPath')
            if not mp==None:
                print 'delete  ......  '+mp[0]
                cmds.delete(mp)
        itx=cmds.listConnections(pc+'.tx',s=1,d=0,p=1)
        if not itx==None:
            cmds.disconnectAttr(itx[0],pc+'.tx')
        ity=cmds.listConnections(pc+'.ty',s=1,d=0,p=1)
        if not ity==None:
            cmds.disconnectAttr(ity[0],pc+'.ty')
        itz=cmds.listConnections(pc+'.tz',s=1,d=0,p=1)
        if not itz==None:
            cmds.disconnectAttr(itz[0],pc+'.tz')
        irx=cmds.listConnections(pc+'.rx',s=1,d=0,p=1)
        if not irx==None:
            cmds.disconnectAttr(irx[0],pc+'.rx')
        iry=cmds.listConnections(pc+'.ry',s=1,d=0,p=1)
        if not iry==None:
            cmds.disconnectAttr(iry[0],pc+'.ry')
        irz=cmds.listConnections(pc+'.rz',s=1,d=0,p=1)
        if not irz==None:
            cmds.disconnectAttr(irz[0],pc+'.rz')
        ncs=[]
        ncs=cmds.ls(nameSpace+':*normal_Car_Grp')
        for nc in ncs:
            #nc=ncs[0]
            ncc=cmds.listConnections(nc+'.rotateX',s=1,d=0,scn=False,type='normalConstraint')
            if not ncc==None:
                print 'delete  ......  '+ncc[0]
                cmds.delete(ncc)
    print 'this car is break connecions.'
edo_breakSnapCar()