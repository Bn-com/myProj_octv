# -*- coding: utf-8 -*-

'''
Created on 2015-12-04

@author: Justin_CHan
'''
import maya.cmds as mc
import maya.mel as mel

def yd_rigging_Mend_selectOBJ():
    selectOBJs= mc.ls(sl=1,l=1)
    if len(selectOBJs)>0:
        selectOBJ = selectOBJs[-1]
        selectNub = yd_rigging_CHR_Mend(selectOBJ)
        if selectNub ==0:
            yd_rigging_Mend_selectOBJ()
    else:
        mc.error(u'======【！！！请选择模型！！！】======')

def yd_rigging_CHR_Mend(selectOBJ):
    shapes = mc.listRelatives(selectOBJ,s=1,fullPath=1)
    for shape in shapes:
        shapeAttr = mc.getAttr(shape+'.intermediateObject')
        if shapeAttr == 0:
            objectSets = mc.listConnections(shape,s=1,d=0,type='objectSet')
            selectNub = 0
            for objectSet in objectSets:
                deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
                if mc.nodeType(deformNode)=='skinCluster':
                    selectNub = 1
            if selectNub ==1:
                #################
                objectSets = mc.listConnections(shape,s=1,d=0,type='objectSet')
                for objectSet in objectSets:
                    deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
                    mc.setAttr((deformNode+'.envelope'),0)
                transformOBJ = mc.listRelatives(shape,p=1,fullPath=1,type = 'transform')[0]
                #nameSpace = transformOBJ.split('|')[-1].split(':')[0]
                TraName = transformOBJ.split('|')[-1].split(':')[-1]
                nameSpace = transformOBJ.split('|')[-1].split(TraName)[0]
                newTraName = nameSpace + TraName
                renameOBJ = newTraName+'rig_'
                renameNode = TraName+'rig_'
                newOBJ = mc.duplicate(transformOBJ,name = renameNode)[0]
                for objectSet in objectSets:
                    deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
                    mc.setAttr((deformNode+'.envelope'),1)
                renameFfdLattice = newOBJ+'ffdLattice'
                ffdLattice = mc.lattice( newOBJ,dv=(4, 5, 3),ldv=(2,2,2), oc=True,name = renameFfdLattice)
                renameCluster_L = newOBJ +'LCluster'
                renameCluster_R = newOBJ +'RCluster'
                newCluster_L = mc.cluster((ffdLattice[1]+'.pt[3][3][2]'),name = renameCluster_L)
                newCluster_R = mc.cluster((ffdLattice[1]+'.pt[0][3][2]'),name = renameCluster_R)
                xformCluster_L = mc.xform(newCluster_L[1],q=1,ws=1,piv=1)
                xformCluster_R = mc.xform(newCluster_R[1],q=1,ws=1,piv=1)
                L_ClusterCtrlName = newOBJ+'lf_Ctrl'
                R_ClusterCtrlName = newOBJ+'rt_Ctrl'
                L_ClusterCtrl = mc.circle(c=(0,0,0),nr=(0,1,0),name=L_ClusterCtrlName,r=0.2)[0]
                R_ClusterCtrl = mc.circle(c=(0,0,0),nr=(0,1,0),name=R_ClusterCtrlName,r=0.2)[0]
                mc.setAttr(L_ClusterCtrl+'.overrideEnabled',1)
                mc.setAttr(L_ClusterCtrl+'.overrideColor',17)
                mc.setAttr(R_ClusterCtrl+'.overrideEnabled',1)
                mc.setAttr(R_ClusterCtrl+'.overrideColor',17)
                GRP_L_ClusterCtrl = mc.group(L_ClusterCtrl,name = L_ClusterCtrlName+'_GRP')
                GRP_R_ClusterCtrl = mc.group(R_ClusterCtrl,name = R_ClusterCtrlName+'_GRP')
                mc.setAttr(GRP_L_ClusterCtrl+'.translate',xformCluster_L[0],xformCluster_L[1],xformCluster_L[2])
                mc.setAttr(GRP_R_ClusterCtrl+'.translate',xformCluster_R[0],xformCluster_R[1],xformCluster_R[2])
                GRP_ClusterCtrl = mc.group(empty=1,name = newOBJ+'GRP_ClusterCtrl')
                mc.parent(GRP_L_ClusterCtrl,GRP_R_ClusterCtrl,GRP_ClusterCtrl)
                #GRP_ClusterCtrl = mc.group(GRP_L_ClusterCtrl,GRP_R_ClusterCtrl,name = newOBJ+'GRP_ClusterCtrl')
                animCurveNode = mc.listConnections(nameSpace+'waist_Ctrl.ikfk_switch',s=1,d=0)
                if animCurveNode != None:
                    try:
                        mc.delete(animCurveNode)
                    except:
                        pass
                mc.setAttr(nameSpace+'waist_Ctrl.ikfk_switch',2)
                mc.parent(GRP_ClusterCtrl,nameSpace+'top_waist_ikCtrl')
                mc.setAttr(GRP_ClusterCtrl+'.translate',0,0.2-xformCluster_L[1],0)
                mc.setAttr(GRP_ClusterCtrl+'.rotate',0,0,0)
                mc.connectAttr(L_ClusterCtrl+'.translate',newCluster_L[1]+'.translate')
                mc.connectAttr(L_ClusterCtrl+'.rotate',newCluster_L[1]+'.rotate')
                mc.connectAttr(L_ClusterCtrl+'.scale',newCluster_L[1]+'.scale')
                mc.connectAttr(R_ClusterCtrl+'.translate',newCluster_R[1]+'.translate')
                mc.connectAttr(R_ClusterCtrl+'.rotate',newCluster_R[1]+'.rotate')
                mc.connectAttr(R_ClusterCtrl+'.scale',newCluster_R[1]+'.scale')
                GRP_temp = mc.group(newOBJ,ffdLattice[1],ffdLattice[2],newCluster_L[1],newCluster_R[1],name=newOBJ+'temp_GRP')
                mc.setAttr (GRP_temp+'.visibility',0)
                test = 0
                for objectSet in objectSets:
                    deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
                    if mc.nodeType(deformNode) == 'blendShape':
                        BS_Number = len(mc.getAttr(deformNode+'.weight')[0])
                        mc.blendShape(deformNode,e=1,t=(transformOBJ,BS_Number,newOBJ,1.0))
                        mc.setAttr(deformNode+'.'+newOBJ,1)
                        test = 1
                if test == 0:
                    blensShapeName = mc.blendShape(newOBJ,transformOBJ,frontOfChain=1,name = newOBJ +'rigBS')[0]
                    mc.setAttr(blensShapeName+'.'+newOBJ,1)

                mc.lockNode(L_ClusterCtrl,R_ClusterCtrl)
                mc.select(cl=1)
                ##################
            if selectNub ==0:
                for objectSet in objectSets:
                    deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
                    if mc.nodeType(deformNode)=='blendShape':
                        objMeshs = mc.listConnections(deformNode,s=1,d=0,type='mesh')
                        mc.select(objMeshs)
    return selectNub



def yd_rigging_CHR_Mend_TOol(mesh):
    objectSets = mc.listConnections(shape,s=1,d=0,type='objectSet')
    for objectSet in objectSets:
        deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
        mc.setAttr((deformNode+'.envelope'),0)
    transformOBJ = mc.listRelatives(shape,p=1,fullPath=1,type = 'transform')[0]
    nameSpace = transformOBJ.split('|')[-1].split(':')[0]
    TraName = transformOBJ.split('|')[-1].split(':')[-1]
    newTraName = nameSpace +':'+TraName
    renameOBJ = newTraName+'rig'
    renameNode = TraName+'rig'
    newOBJ = mc.duplicate(transformOBJ,name = renameNode)[0]
    for objectSet in objectSets:
        deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
        mc.setAttr((deformNode+'.envelope'),1)
    renameFfdLattice = newOBJ+'_ffdLattice'
    ffdLattice = mc.lattice( newOBJ,dv=(4, 5, 3),ldv=(2,2,2), oc=True,name = renameFfdLattice)
    renameCluster_L = newOBJ +'_LCluster'
    renameCluster_R = newOBJ +'_RCluster'
    newCluster_L = mc.cluster((ffdLattice[1]+'.pt[3][3][2]'),name = renameCluster_L)
    newCluster_R = mc.cluster((ffdLattice[1]+'.pt[0][3][2]'),name = renameCluster_R)
    xformCluster_L = mc.xform(newCluster_L[1],q=1,ws=1,piv=1)
    xformCluster_R = mc.xform(newCluster_R[1],q=1,ws=1,piv=1)
    L_ClusterCtrlName = newOBJ+'lf_Ctrl'
    R_ClusterCtrlName = newOBJ+'rt_Ctrl'
    L_ClusterCtrl = mc.circle(c=(0,0,0),nr=(0,1,0),name=L_ClusterCtrlName,r=0.2)[0]
    R_ClusterCtrl = mc.circle(c=(0,0,0),nr=(0,1,0),name=R_ClusterCtrlName,r=0.2)[0]
    mc.setAttr(L_ClusterCtrl+'.overrideEnabled',1)
    mc.setAttr(L_ClusterCtrl+'.overrideColor',17)
    mc.setAttr(R_ClusterCtrl+'.overrideEnabled',1)
    mc.setAttr(R_ClusterCtrl+'.overrideColor',17)
    GRP_L_ClusterCtrl = mc.group(L_ClusterCtrl,name = L_ClusterCtrlName+'_GRP')
    GRP_R_ClusterCtrl = mc.group(R_ClusterCtrl,name = R_ClusterCtrlName+'_GRP')
    mc.setAttr(GRP_L_ClusterCtrl+'.translate',xformCluster_L[0],xformCluster_L[1],xformCluster_L[2])
    mc.setAttr(GRP_R_ClusterCtrl+'.translate',xformCluster_R[0],xformCluster_R[1],xformCluster_R[2])
    GRP_ClusterCtrl = mc.group(empty=1,name = newOBJ+'GRP_ClusterCtrl')
    mc.parent(GRP_L_ClusterCtrl,GRP_R_ClusterCtrl,GRP_ClusterCtrl)
    #GRP_ClusterCtrl = mc.group(GRP_L_ClusterCtrl,GRP_R_ClusterCtrl,name = newOBJ+'GRP_ClusterCtrl')
    mc.parent(GRP_ClusterCtrl,nameSpace+':top_waist_ikCtrl')
    mc.setAttr(GRP_ClusterCtrl+'.translate',0,-1.8,0)
    mc.setAttr(GRP_ClusterCtrl+'.rotate',0,0,0)
    mc.connectAttr(L_ClusterCtrl+'.translate',newCluster_L[1]+'.translate')
    mc.connectAttr(L_ClusterCtrl+'.rotate',newCluster_L[1]+'.rotate')
    mc.connectAttr(L_ClusterCtrl+'.scale',newCluster_L[1]+'.scale')
    mc.connectAttr(R_ClusterCtrl+'.translate',newCluster_R[1]+'.translate')
    mc.connectAttr(R_ClusterCtrl+'.rotate',newCluster_R[1]+'.rotate')
    mc.connectAttr(R_ClusterCtrl+'.scale',newCluster_R[1]+'.scale')
    GRP_temp = mc.group(newOBJ,ffdLattice[1],ffdLattice[2],newCluster_L[1],newCluster_R[1],name=newOBJ+'_temp_GRP')
    mc.setAttr (GRP_temp+'.visibility',0)
    test = 0
    for objectSet in objectSets:
        deformNode = mc.listConnections(objectSet+'.usedBy',source=1,d=0)[0]
        if mc.nodeType(deformNode) == 'blendShape':
            mc.blendShape(deformNode,e=1,t=(transformOBJ,1,newOBJ,1))
            mc.setAttr(deformNode+'.'+newOBJ,1)
            test = 1
    if test == 0:
        blensShapeName = mc.blendShape(newOBJ,transformOBJ,frontOfChain=1,name = newOBJ +'rigBS')[0]
        mc.setAttr(blensShapeName+'.'+newOBJ,1)

    mc.select(cl=1)


