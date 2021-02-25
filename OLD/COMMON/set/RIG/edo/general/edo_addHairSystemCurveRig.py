import maya.cmds as cmds
import maya.mel as mel
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_addContorlToJointChain.py')

def edo_addHairSystemCurveRig():
    sels=cmds.ls(sl=1)
    #add group and joint
    pa=''
    tipjnt=''
    for sel in sels:
        #sel=sels[0]
        grp=''
        if not cmds.objExists('DYN_'+sel):
            grp=cmds.group(sel,n='DYN_'+sel)
        else:
            grp='DYN_'+sel
        cmds.xform(grp,ws=1,piv=cmds.xform(sel,q=1,ws=1,rp=1))
        n='Hair_'+sel.replace('ctrl','jnt').replace('CTRL','JNT')
        jnt=cmds.createNode('joint',n=n)
        cmds.parent(jnt,sel)
        cmds.setAttr(jnt+'.tx',0)
        cmds.setAttr(jnt+'.ty',0)
        cmds.setAttr(jnt+'.tz',0)
        cmds.setAttr(jnt+'.jox',0)
        cmds.setAttr(jnt+'.joy',0)
        cmds.setAttr(jnt+'.joz',0)
        if not pa=='':
            cmds.parent(jnt,pa)
        else:
            cmds.parent(jnt,w=1)
            tipjnt=jnt
        #cmds.parentConstraint(jnt,grp,mo=1)
        #cmds.connectAttr(jnt+'.translate',grp+'translate',f=1)
        cmds.connectAttr(jnt+'.rotate',grp+'.rotate',f=1)
        pa=jnt
        print tipjnt
    hcjs=cmds.duplicate(tipjnt)
    cmds.select(hcjs[0],r=1)
    mel.eval("searchReplaceNames \"Hair\" \"HairCt\" \"hierarchy\";")
    tipctjnt=hcjs[0].replace('Hair','HairCt')[:-1]+tipjnt[-1]
    tipctjnt=cmds.rename(hcjs[0].replace('Hair','HairCt'),tipctjnt)
    cmds.select(tipjnt,hi=1)
    alljnt=cmds.ls(sl=1)
    cmds.select(tipctjnt,hi=1)
    allctjnt=cmds.ls(sl=1)
    endjnt=alljnt[-1]
    cmds.select(tipctjnt,r=1)
    edo_addContorlToJointChain()
    iks=cmds.ikHandle(sj=tipjnt,ee=endjnt,sol='ikSplineSolver',ns=2)
    ikcurve=cmds.rename(iks[2],tipjnt+'_ikcurve')
    ikhandle=cmds.rename(iks[0],tipjnt+'_ikhandle')
    cmds.skinCluster(allctjnt,ikcurve,mi=2,mjm=0,tsb=1)
    cmds.group([ikcurve,ikhandle],n='HairSystem_'+tipjnt)
    cmds.select(ikcurve)
    mel.eval("makeCurvesDynamicHairs 1 0 1;")
    outputs=cmds.listConnections(ikcurve+'.worldSpace[0]',s=0,d=1)
    reb=cmds.ls(outputs,type='rebuildCurve')
    if reb:
        rec=cmds.listConnections(reb[0]+'.outputCurve',s=0,d=1,sh=1)
        if rec:
            fo=cmds.listConnections(rec[0]+'.worldSpace[0]',s=0,d=1,sh=1)
            if fo:
                dyc=cmds.listConnections(fo[0]+'.outCurve',s=0,d=1,sh=1)
                if dyc:
                    dyc=cmds.rename(dyc,'HRS_'+ikcurve)
                    cmds.connectAttr(dyc+'.worldSpace[0]',ikhandle+'.inCurve',f=1)
                    return True