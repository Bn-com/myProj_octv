#-*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
def edo_calimeroFeetRiggingMainUI():
    if cmds.window('calimeroFeetRiggingMainUI',q=1,ex=1):
        cmds.deleteUI('calimeroFeetRiggingMainUI')
    cmds.window('calimeroFeetRiggingMainUI')
    cmds.formLayout('calimeroFeetRiggingMainUI_FL01',w=300,h=500)
    cmds.tabLayout('calimeroFeetRiggingMainUI_TB01',innerMarginWidth=5, innerMarginHeight=5)
    cmds.columnLayout('calimeroFeetRiggingMainUI_CL01',cw=300,rs=5,p='calimeroFeetRiggingMainUI_TB01')
    cmds.button('calimeroFeetRiggingMainUI_CL01_BT01',l='import feet skeleton template',w=300,p='calimeroFeetRiggingMainUI_CL01',c='edo_calimeroFeetRiggingMainCmd()')
    cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG01',field=True,label='number of front toe',minValue=1, maxValue=5, fieldMinValue=1, fieldMaxValue=10, value=2,cw3=[100,60,130])
    cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG02',field=True,label='number of skeleton',minValue=1, maxValue=12, fieldMinValue=1, fieldMaxValue=12, value=7,cw3=[100,60,130])
    #cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG03',field=True,label='±Ç×Ó¹Ç÷ÀÊý',minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    #cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG04',field=True,label='¶ú¶ä¹Ç÷ÀÊý',minValue=0, maxValue=10, fieldMinValue=0, fieldMaxValue=10, value=3,cw3=[80,60,130])
    #cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG05',field=True,label='ÉàÍ·¹Ç÷ÀÊý',minValue=0, maxValue=12, fieldMinValue=0, fieldMaxValue=12, value=7,cw3=[80,60,130])
    cmds.rowLayout('calimeroFeetRiggingMainUI_CL01_RL01',numberOfColumns=2, columnWidth2=(150,150))
    #cmds.button('calimeroFeetRiggingMainUI_CL01_RL01_BT01',l='refresh template',w=150)
    cmds.button('calimeroFeetRiggingMainUI_CL01_RL01_BT02',l='mirror template',w=150,c='edo_miirorCalimeroToeTemplate()')
    cmds.setParent('calimeroFeetRiggingMainUI_CL01')
    cmds.button('calimeroFeetRiggingMainUI_CL01_BT02',l='create front toe rig',w=300,h=40,c='edo_calimeroFeetRiggingCreationCmd()')
    cmds.tabLayout('calimeroFeetRiggingMainUI_TB01',e=True,tabLabel=('calimeroFeetRiggingMainUI_CL01','calimeroFeet'))
    cmds.showWindow('calimeroFeetRiggingMainUI')
    cmds.window('calimeroFeetRiggingMainUI',e=1,w=300,h=200)

def edo_calimeroFeetRiggingMainCmd():
    toenum=cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG01',q=True,v=1)
    sknum=cmds.intSliderGrp('calimeroFeetRiggingMainUI_CL01_IFG02',q=True,v=1)+2
    edo_imoirtFrontToeSkeletonTmplate(toenum,sknum)

def edo_calimeroFeetAddAttribute(list):
    #list=['LfLeg_Leg_IK','RtLeg_Leg_IK']
    for l in list:
        #l=list[0]
        if not cmds.objExists(l):
            continue
        sl=l.replace('Leg_IK','Switch')
        rst=l.replace('Leg_Leg_IK','_ball_toe_con_Grp')
        inp=cmds.listConnections(rst+'.ry',s=1,d=0,p=1)
        if not inp==None:
            cmds.setAttr(rst+'.ry',e=1,l=0)
            cmds.disconnectAttr(inp[0],rst+'.ry')
        inp=cmds.listConnections(rst+'.rz',s=1,d=0,p=1)
        if not inp==None:
            cmds.setAttr(rst+'.rz',e=1,l=0)
            cmds.disconnectAttr(inp[0],rst+'.rz')
        cmds.addAttr(l,ln='Open_Toe',at='double')
        cmds.setAttr(l+'.Open_Toe',e=1,k=1)
        cmds.addAttr(l,ln='UpLegth',at='double')
        cmds.setAttr(l+'.UpLegth',e=1,k=1)
        cmds.addAttr(l,ln='LowLength',at='double')
        cmds.setAttr(l+'.LowLength',e=1,k=1)
        cmds.connectAttr(l+'.UpLegth',sl+'.UpLegth',f=1)
        cmds.setAttr(sl+'.UpLegth',e=1,k=0)
        cmds.connectAttr(l+'.LowLength',sl+'.LowLength',f=1)
        cmds.setAttr(sl+'.LowLength',e=1,k=0)

def edo_calimeroFeetRiggingCreationCmd():
    jnts=cmds.ls('*_calimeroToe_*_tmplate_jnt1')
    msjnts=cmds.ls('MS_*_calimeroToe_*_tmplate_')
    if jnts==[] or jnts==None:
        return False
    if not cmds.objExists('GRP_calimeroFeetRigging'):
        cmds.createNode('transform',n='GRP_calimeroFeetRigging')
    if not cmds.objExists('GRP_calimeroFeetCluster'):
        cmds.createNode('transform',n='GRP_calimeroFeetCluster')
    if not cmds.objExists('GRP_calimeroFeetPlanes'):
        cmds.createNode('transform',n='GRP_calimeroFeetPlanes')
    if not cmds.objExists('GRP_calimeroFeetConstraintJoint'):
        cmds.createNode('transform',n='GRP_calimeroFeetConstraintJoint')
    if not cmds.objExists('GRP_calimeroFeetSkinJoint'):
        cmds.createNode('transform',n='GRP_calimeroFeetSkinJoint')
    if not cmds.objExists('GRP_calimeroFeetFollicleJoint'):
        cmds.createNode('transform',n='GRP_calimeroFeetFollicleJoint')
    if not cmds.objExists('Calimero_closestpointonmesh'):
        cmds.createNode('closestPointOnMesh',n='Calimero_closestpointonmesh')
    if not cmds.objExists('Influence_Joint'):
        cmds.createNode('objectSet',n='Influence_Joint')
    if not cmds.objExists('calimeroToe_Joint'):
        cmds.createNode('objectSet',n='calimeroToe_Joint')
    cmds.parent(['GRP_calimeroFeetCluster','GRP_calimeroFeetPlanes','GRP_calimeroFeetConstraintJoint','GRP_calimeroFeetSkinJoint','GRP_calimeroFeetFollicleJoint'],'GRP_calimeroFeetRigging')
    if cmds.objExists('DEFORMERS'):
        cmds.parent('GRP_calimeroFeetRigging','DEFORMERS')
    cmds.sets('calimeroToe_Joint',e=1,add='Influence_Joint')
    for jnt in jnts:
        #jnt=jnts[0]
        print jnt
        cmds.select(jnt,hi=1)
        alljnt=cmds.ls(sl=1,type='joint')
        planes=cmds.ls(sl=1,type='mesh')
        t=cmds.listRelatives(planes[0],p=1,pa=1)[0]
        fomesh=cmds.rename(t,t.replace('tmplate','follicleMesh'))
        try:
            cmds.connectAttr(fomesh+'.outMesh','Calimero_closestpointonmesh.inMesh',f=1)
        except:
            print 'something wrong!'
        cmds.parent(fomesh,'GRP_calimeroFeetPlanes')
        cmds.makeIdentity(fomesh,apply=True,t=1,r=1,s=1,n=0)
        cmds.DeleteHistory(fomesh)
        lenth=len(alljnt)
        skp='GRP_calimeroFeetSkinJoint'
        csp='GRP_calimeroFeetConstraintJoint'
        for j in alljnt:
            #j=alljnt[1]
            print j
            #add skeleton
            skjnt=cmds.createNode('joint',n=j.replace('tmplate','skin'))
            csjnt=cmds.createNode('joint',n=j.replace('tmplate','constraint'))
            fojnt=cmds.createNode('joint',n=j.replace('tmplate','follicle'))
            cmds.xform(skjnt,ws=1,t=cmds.xform(j,q=1,ws=1,t=1))
            cmds.xform(csjnt,ws=1,t=cmds.xform(j,q=1,ws=1,t=1))
            cmds.xform(fojnt,ws=1,t=cmds.xform(j,q=1,ws=1,t=1))
            cmds.connectAttr(fojnt+'.translate','Calimero_closestpointonmesh.inPosition',f=1)
            u=cmds.getAttr('Calimero_closestpointonmesh.parameterU')
            v=cmds.getAttr('Calimero_closestpointonmesh.parameterV')
            fo=edo_createFolicleByMeshAndUV(fomesh,u,v)
            cmds.parent(skjnt,skp)
            cmds.parent(csjnt,csp)
            cmds.parent(fojnt,fo)
            cmds.parent(fo,'GRP_calimeroFeetFollicleJoint')
            cmds.setAttr(fojnt+'.jointOrientX',0)
            cmds.setAttr(fojnt+'.jointOrientY',0)
            cmds.setAttr(fojnt+'.jointOrientZ',0)
            skp=skjnt
            csp=csjnt
        skjnts=jnt.replace('tmplate','skin')
        csjnts=jnt.replace('tmplate','constraint')
        cmds.joint(skjnts,e=1,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)
        cmds.joint(csjnts,e=1,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)
        skp='GRP_calimeroFeetSkinJoint'
        for j in alljnt:
            #j=alljnt[0]
            csjnt=j.replace('tmplate','constraint')
            fojnt=j.replace('tmplate','follicle')
            skjnt=j.replace('tmplate','skin')
            #addConstaint
            cmds.parentConstraint(fojnt,csjnt,mo=1)
            #addContorlor
            if j==jnt:
                cmds.connectAttr(csjnt+'.translate',skjnt+'.translate',f=1)
                cmds.connectAttr(csjnt+'.rotate',skjnt+'.rotate',f=1)
                skp=skjnt
                continue
            if cmds.listRelatives(j,c=1)==None:
                continue
            ctrl=j.replace('tmplate_jnt','ctrl')
            ctrlgrp='GRP_'+j.replace('tmplate_jnt','ctrl')
            edo_gdcfrig2012_createCtrl(ctrl,shape='circle',colorid=17)
            cmds.setAttr(ctrl+'.rz',90)
            cmds.makeIdentity(ctrl,apply=True,t=1,r=1,s=1,n=0)
            cmds.group(ctrl,n=ctrlgrp.replace('GRP','DIV'))
            cmds.group(ctrl,n=ctrlgrp.replace('GRP','EX'))
            cmds.parent(ctrlgrp,skjnt)
            edo_zeroTransform(ctrlgrp)
            cmds.parent(ctrlgrp,skp)
            cmds.addAttr(ctrl,ln='sumTranslateX',at='double')
            cmds.addAttr(ctrl,ln='sumTranslateY',at='double')
            cmds.addAttr(ctrl,ln='sumTranslateZ',at='double')
            cmds.addAttr(ctrl,ln='sumRotateX',at='double')
            cmds.addAttr(ctrl,ln='sumRotateY',at='double')
            cmds.addAttr(ctrl,ln='sumRotateZ',at='double')
            cmds.addAttr(ctrl,ln='sumScaleX',at='double')
            cmds.addAttr(ctrl,ln='sumScaleY',at='double')
            cmds.addAttr(ctrl,ln='sumScaleZ',at='double')
            #plustranslate
            plust=cmds.createNode('plusMinusAverage',n='PMA_translate'+ctrl)
            cmds.connectAttr(ctrl+'.tx',plust+'.input3D[0].input3Dx',f=1)
            cmds.connectAttr(ctrl+'.ty',plust+'.input3D[0].input3Dy',f=1)
            cmds.connectAttr(ctrl+'.tz',plust+'.input3D[0].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.tx',plust+'.input3D[1].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.ty',plust+'.input3D[1].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.tz',plust+'.input3D[1].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.tx',plust+'.input3D[2].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.ty',plust+'.input3D[2].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.tz',plust+'.input3D[2].input3Dz',f=1)
            cmds.connectAttr(csjnt+'.tx',plust+'.input3D[3].input3Dx',f=1)
            cmds.connectAttr(csjnt+'.ty',plust+'.input3D[3].input3Dy',f=1)
            cmds.connectAttr(csjnt+'.tz',plust+'.input3D[3].input3Dz',f=1)
            cmds.connectAttr(plust+'.output3Dx',ctrl+'.sumTranslateX',f=1)
            cmds.connectAttr(plust+'.output3Dy',ctrl+'.sumTranslateY',f=1)
            cmds.connectAttr(plust+'.output3Dz',ctrl+'.sumTranslateZ',f=1)
            #plusrotate
            plusr=cmds.createNode('plusMinusAverage',n='PMA_rotate'+ctrl)
            cmds.connectAttr(ctrl+'.rx',plusr+'.input3D[0].input3Dx',f=1)
            cmds.connectAttr(ctrl+'.ry',plusr+'.input3D[0].input3Dy',f=1)
            cmds.connectAttr(ctrl+'.rz',plusr+'.input3D[0].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.rx',plusr+'.input3D[1].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.ry',plusr+'.input3D[1].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.rz',plusr+'.input3D[1].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.rx',plusr+'.input3D[2].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.ry',plusr+'.input3D[2].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.rz',plusr+'.input3D[2].input3Dz',f=1)
            cmds.connectAttr(csjnt+'.rx',plusr+'.input3D[3].input3Dx',f=1)
            cmds.connectAttr(csjnt+'.ry',plusr+'.input3D[3].input3Dy',f=1)
            cmds.connectAttr(csjnt+'.rz',plusr+'.input3D[3].input3Dz',f=1)
            cmds.connectAttr(plusr+'.output3Dx',ctrl+'.sumRotateX',f=1)
            cmds.connectAttr(plusr+'.output3Dy',ctrl+'.sumRotateY',f=1)
            cmds.connectAttr(plusr+'.output3Dz',ctrl+'.sumRotateZ',f=1)
            #plusscale
            pluss=cmds.createNode('plusMinusAverage',n='PMA_scale'+ctrl)
            cmds.connectAttr(ctrl+'.sx',pluss+'.input3D[0].input3Dx',f=1)
            cmds.connectAttr(ctrl+'.sy',pluss+'.input3D[0].input3Dy',f=1)
            cmds.connectAttr(ctrl+'.sz',pluss+'.input3D[0].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.sx',pluss+'.input3D[1].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.sy',pluss+'.input3D[1].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','DIV')+'.sz',pluss+'.input3D[1].input3Dz',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.sx',pluss+'.input3D[2].input3Dx',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.sy',pluss+'.input3D[2].input3Dy',f=1)
            cmds.connectAttr(ctrlgrp.replace('GRP','EX')+'.sz',pluss+'.input3D[2].input3Dz',f=1)
            cmds.connectAttr(csjnt+'.sx',pluss+'.input3D[3].input3Dx',f=1)
            cmds.connectAttr(csjnt+'.sy',pluss+'.input3D[3].input3Dy',f=1)
            cmds.connectAttr(csjnt+'.sz',pluss+'.input3D[3].input3Dz',f=1)
            cmds.connectAttr(pluss+'.output3Dx',ctrl+'.sumScaleX',f=1)
            cmds.connectAttr(pluss+'.output3Dy',ctrl+'.sumScaleY',f=1)
            cmds.connectAttr(pluss+'.output3Dz',ctrl+'.sumScaleZ',f=1)
            #connectSkinJnt
            cmds.connectAttr(ctrl+'.sumTranslateX',skjnt+'.tx',f=1)
            cmds.connectAttr(ctrl+'.sumTranslateY',skjnt+'.ty',f=1)
            cmds.connectAttr(ctrl+'.sumTranslateZ',skjnt+'.tz',f=1)
            cmds.connectAttr(ctrl+'.sumRotateX',skjnt+'.rx',f=1)
            cmds.connectAttr(ctrl+'.sumRotateY',skjnt+'.ry',f=1)
            cmds.connectAttr(ctrl+'.sumRotateZ',skjnt+'.rz',f=1)
            skp=skjnt
        print alljnt
        for j in alljnt:
            #j=skjnts[0]
            skjnt=j.replace('tmplate','skin')
            inskjnt=cmds.createNode('joint',n=j.replace('tmplate','finalskin'),p=skjnt)
            cmds.setAttr(inskjnt+'.jointOrientX',0)
            cmds.setAttr(inskjnt+'.jointOrientY',0)
            cmds.setAttr(inskjnt+'.jointOrientZ',0)
            cmds.sets(inskjnt,e=1,add='calimeroToe_Joint')
    cmds.delete(jnts)
    cmds.delete(msjnts)
    stctrl=cmds.ls('*_calimeroToe_*_ctrl2Shape',type='nurbsCurve')
    for c in stctrl:
        #c=stctrl[0]
        tc=cmds.listRelatives(c,p=1,pa=1)[0]
        cmds.addAttr(tc,ln='clus_rotateX',at='double')
        cmds.setAttr(tc+'.clus_rotateX',e=1,k=1)
        cmds.addAttr(tc,ln='clus_rotateY',at='double')
        cmds.setAttr(tc+'.clus_rotateY',e=1,k=1)
        cmds.addAttr(tc,ln='clus_rotateZ',at='double')
        cmds.setAttr(tc+'.clus_rotateZ',e=1,k=1)
        planeobj=c.replace('_ctrl2Shape','_follicleMesh_msh')
        cmds.select(planeobj)
        cluss=mel.eval("newCluster \" -envelope 1\"")
        cmds.xform(cluss[1],ws=1,piv=cmds.xform(tc,q=1,ws=1,t=1))
        cmds.parent(cluss[1],'GRP_calimeroFeetCluster')
        cmds.connectAttr(tc+'.clus_rotateX',cluss[1]+'.rx',f=1)
        cmds.connectAttr(tc+'.clus_rotateY',cluss[1]+'.ry',f=1)
        cmds.connectAttr(tc+'.clus_rotateZ',cluss[1]+'.rz',f=1)
        cmds.rename(cluss[1],planeobj.replace('msh','clus'))
    edo_addCalimeroFeetGlobalScale('Lf_Leg9_jnt','Lf')
    edo_addCalimeroFeetGlobalScale('Rt_Leg9_jnt','Rt')
    edo_calimeroFeetAddAttribute(['LfLeg_Leg_IK','RtLeg_Leg_IK'])
        
def edo_createFolicleByMeshAndUV(mesh,u,v):
    #mesh='Lf_calimeroToe_1_follicleMesh_msh'
    #u=
    #v=
    foshape=cmds.createNode('follicle')
    fo=cmds.listRelatives(foshape,p=1,pa=1)[0]
    fo=cmds.rename(fo,mesh+'_follicle_1')
    foshape=cmds.listRelatives(fo,s=1,pa=1)[0]
    cmds.connectAttr(foshape+'.outTranslate',fo+'.translate',f=1)
    cmds.connectAttr(foshape+'.outRotate',fo+'.rotate',f=1)
    cmds.connectAttr(mesh+'.outMesh',foshape+'.inputMesh',f=1)
    cmds.connectAttr(mesh+'.worldMatrix[0]',foshape+'.inputWorldMatrix',f=1)
    cmds.setAttr(foshape+'.parameterU',u)
    cmds.setAttr(foshape+'.parameterV',v)
    return fo
    
    
    

def edo_imoirtFrontToeSkeletonTmplate(toenum,sknum):
    #toenum=2
    #sknum=8
    for i in range(1,toenum+1):
        #i=1
        print i
        jnt=edo_createCalimeroToeJointChain(i,sknum)
        if jnt==False:
            continue
        tmpmsh=cmds.polyPlane(ch=True,o=True,w=1,h=sknum-1,sw=1,sh=2*(sknum-1),cuv=2,n='Lf_calimeroToe_'+str(i)+'_tmplate_msh')
        cmds.delete(tmpmsh[1])
        cmds.setAttr(tmpmsh[0]+'.tx',i)
        cmds.setAttr(tmpmsh[0]+'.ty',0)
        cmds.setAttr(tmpmsh[0]+'.tz',sknum*0.5-0.5)
        cmds.parent(tmpmsh[0],jnt)
        c=cmds.listRelatives(jnt,c=1,pa=1)[0]
        ctrl='MS_'+jnt.replace('jnt1','')
        cmds.createNode('joint',n=ctrl)
        cmds.parent(ctrl,c)
        edo_zeroTransform(ctrl)
        cmds.setAttr(ctrl+'.jointOrientX',0)
        cmds.setAttr(ctrl+'.jointOrientY',0)
        cmds.setAttr(ctrl+'.jointOrientZ',0)
        cmds.parent(ctrl,w=1)
        cmds.parent(jnt,ctrl)
        tmp=cmds.circle(ch=1,o=1,nr=[1,0,0],r=1)
        cmds.delete(tmp[1])
        shape=cmds.listRelatives(tmp[0],s=1,pa=1)[0]
        cmds.rename(shape,ctrl+'Shape')
        cmds.parent(ctrl+'Shape',ctrl,s=1,r=1)
        cmds.setAttr(ctrl+'Shape.overrideEnabled',1)
        cmds.setAttr(ctrl+'Shape.ovc',13)
        cmds.delete(tmp[0])


def edo_createCalimeroToeJointChain(id,sknum):
    #sknum=7
    #id=1
    p=''
    s=''
    e=''
    for i in range(1,sknum+1):
        #i=1
        print i
        if i==1:
            if cmds.objExists('Lf_calimeroToe_'+str(id)+'_tmplate_jnt'+str(i)):
                print 'Lf_calimeroToe_'+str(id)+'_tmplate_jnt'+str(i)+'  is already exists!'
                return False
            jnt=cmds.createNode('joint',n='Lf_calimeroToe_'+str(id)+'_tmplate_jnt'+str(i))
            cmds.setAttr(jnt+'.tx',id)
            p=jnt
            s=jnt
            cmds.setAttr(jnt+'.segmentScaleCompensate',0)
        else:
            jnt=cmds.createNode('joint',n='Lf_calimeroToe_'+str(id)+'_tmplate_jnt'+str(i))
            cmds.parent(jnt,p)
            cmds.setAttr(jnt+'.tx',0)
            cmds.setAttr(jnt+'.ty',0)
            cmds.setAttr(jnt+'.tz',1)
            p=jnt
            cmds.setAttr(jnt+'.segmentScaleCompensate',0)
        if i==sknum:
            e=jnt
    cmds.joint(s,e=1,oj='xyz',secondaryAxisOrient='yup',ch=True,zso=True)
    cmds.setAttr(e+'.jointOrientX',0)
    cmds.setAttr(e+'.jointOrientY',0)
    cmds.setAttr(e+'.jointOrientZ',0)
    return s      

          
def edo_miirorCalimeroToeTemplate():
    jnts=cmds.ls('MS_Lf_calimeroToe_*_tmplate_')
    for jnt in jnts:
        #jnt=jnts[0]
        rtname=jnt.replace('Lf','Rt')
        if cmds.objExists(rtname):
            cmds.delete(rtname)
        njnt=cmds.duplicate(jnt,n=rtname)
        cmds.select(njnt[0],r=1)
        mel.eval("searchReplaceNames \"Lf\" \"Rt\" \"hierarchy\"")
        cmds.setAttr(njnt[0]+'.tx',cmds.getAttr(njnt[0]+'.tx')*-1)
        cmds.setAttr(njnt[0]+'.ty',cmds.getAttr(njnt[0]+'.ty'))
        cmds.setAttr(njnt[0]+'.tz',cmds.getAttr(njnt[0]+'.tz'))
        cmds.setAttr(njnt[0]+'.rx',cmds.getAttr(njnt[0]+'.rx')*-1)
        cmds.setAttr(njnt[0]+'.ry',cmds.getAttr(njnt[0]+'.ry')*-1)
        cmds.setAttr(njnt[0]+'.rz',cmds.getAttr(njnt[0]+'.rz'))
        cmds.setAttr(njnt[0]+'.sx',cmds.getAttr(njnt[0]+'.sx'))
        cmds.setAttr(njnt[0]+'.sy',cmds.getAttr(njnt[0]+'.sy'))
        cmds.setAttr(njnt[0]+'.sz',cmds.getAttr(njnt[0]+'.sz'))

def edo_gdcfrig2012_createCtrl(name,shape='box',colorid=17):
    #name='ctrl'
    #colorid=17
    if shape=='box':
        cmds.curve(n=name,d=1,p=[[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0.5,-0.5,0.5],[-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,0.5,0.5],[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[-0.5,0.5,0.5],[-0.5,0.5,-0.5]])
    if shape=='circle':
        cmds.delete(cmds.circle(ch=1,o=1,nr=[0,1,0],n=name)[1])
    if shape=='square':
        cmds.curve(n=name,d=1,p=[[-10,-10,0],[-10,10,0],[10,10,0],[10,-10,0],[-10,-10,0]])
    cmds.group(name,n='GRP_'+name)
    ss=cmds.listRelatives(name,s=1)[0]
    cmds.rename(ss,name+'Shape')
    cmds.setAttr(name+'Shape.overrideEnabled',1)
    cmds.setAttr(name+'Shape.ovc',colorid)  
    
def edo_zeroTransform(obj):
    cmds.setAttr(obj+'.tx',0)
    cmds.setAttr(obj+'.ty',0)
    cmds.setAttr(obj+'.tz',0)
    cmds.setAttr(obj+'.rx',0)
    cmds.setAttr(obj+'.ry',0)
    cmds.setAttr(obj+'.rz',0)
    cmds.setAttr(obj+'.sx',1)
    cmds.setAttr(obj+'.sy',1)
    cmds.setAttr(obj+'.sz',1)
    
def edo_addCalimeroFeetGlobalScale(scaleCtrl,aim):
    #scaleCtrl='Lf_Leg9_jnt'
    #aim='Lf'
    if not cmds.objExists(scaleCtrl):
        return False
    lfclfo=cmds.ls(aim+'_calimeroToe_*_finalskin_jnt*',type='transform')
    if not (lfclfo==None or lfclfo==[]):
        #len(clfo)
        for fo in lfclfo:
            #fo=clfo[0]
            cmds.scaleConstraint(scaleCtrl,fo,mo=1)
        
    
edo_calimeroFeetRiggingMainUI()