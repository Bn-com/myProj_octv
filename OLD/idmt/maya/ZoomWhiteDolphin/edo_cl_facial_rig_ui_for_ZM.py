#-*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import maya.OpenMaya as om

execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_autoConnectBlendShapeUI.py')
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_cl_checkRiggingFileUI.py')

def edo_cl_facial_rig_ui():
    ui='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_cl_facial_rig_ui.myuis'
    if mc.window('edo_cl_facial_rig_ui',ex=1):
        mc.deleteUI('edo_cl_facial_rig_ui')
    mui=mc.loadUI(f=ui)
    #import template
    mc.button('importTemplate_bt',e=1,c='edo_importFacialTemplate()',ann='�����沿����Ҫ��ģ��')
    #check model
    mc.button('facial_check_bt',e=1,c='edo_openDocumentFromPath(\'Z:/Resource/Support/Maya/extra/Rigging_Simulation/helpDocument/project/calimero/calimero_facial_rigging_tool_model_check.docx.docx\')',ann='�򿪹���ʹ��ǰ��ģ�ͼ���ĵ�')
    #start
    mc.button('facial_meshes_bt',e=1,c='edo_getComponentToTextEditor(\'facial_meshes_line\')',ann='��ͷ�����е�ģ�����뵽�б���')
    mc.button('create_meshes_bt',e=1,c='edo_createAllFcialMeshes(\'msh_\')',ann='�����沿��ʱ��Ҫ�����е�ͷ��ģ��')
    #tongue_tab
    mc.button('finish_tonguerig_bt',e=1,c='edo_finishTongueRig()')
    mc.button('get_tonguemeshes_bt',e=1,c='edo_getComponentToTextEditor(\'get_tonguemeshes_line\')')
    #jaw_tab
    mc.button('finish_jaw_bt',e=1,c='edo_finishJawRig()')
    #eye_rig
    mc.button('eyeball_autoloc_bt',e=1,c='edo_autoLocationEyeballsCenter()',ann='ѡ�������Բ�κ�Ĥִ��,��ס����ѡ�����۵ĺ�Ĥ����ѡ�����۵�')
    mc.button('eyeball_mirror_bt',e=1,c='edo_mirrorEyeballsSkeleton()',ann='������ߵ�����������ұ�')
    mc.button('lfeyelids_loop_bt',e=1,c='edo_getComponentToTextEditor(\'lfeyelids_loop_line\')',ann='����ѡ�����۴��ڵ������Ƥ��ִ��,�����ɹ�����Ҫʱ�̱����������������')
    mc.button('rteyelids_loop_bt',e=1,c='edo_getComponentToTextEditor(\'rteyelids_loop_line\')',ann='����ѡ�����۴��ڵ������Ƥ��ִ��,�����ɹ�����Ҫʱ�̱����������������')
    mc.button('finish_eyerig_bt',e=1,c='edo_finishEyeRig()',ann='�Ƚ���Ƥ����������Ŀ��ִ��')
    #mc.button('eyelids_autoloc_bt',e=1,c='edo_createEyslids_skeleton()',ann='�Ƚ���Ƥ����������Ŀ��ִ��')
    mc.button('mirrorEyelids_blendshape_bt',e=1,c='edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections()',ann='ֱ��ִ�д������ʹ����Ƥ������ģ��Ŀ���徵���ұ���Ƥ')
    mc.button('check_calimeroRig_bt',e=1,c='edo_cl_checkRiggingFileUI()',ann='calimero�������淶��鹤��')
    mc.showWindow(mui)

def edo_openDocumentFromPath(path):
    #path='Z:/Resource/Support/Maya/extra/Rigging_Simulation/helpDocument/project/calimero/calimero_facial_rigging_tool_model_check.docx.docx'
    cmd="system(\"load "+path+"\")"
    mel.eval(cmd)

def edo_importFacialTemplate():
    templatePath='//file-cluster/GDC/Resource/Support/Maya/projects/ZoomWhiteDolphin/Rigging_Simulation/mayaFile'
    mc.file(templatePath+'/eyeballs_rig.ma',i=1)
    mc.file(templatePath+'/pannel_rig.ma',i=1)
    mc.file(templatePath+'/jaw_rig.ma',i=1)
    mc.file(templatePath+'/tongue_rig.ma',i=1)
    mc.file(templatePath+'/frame_rig.ma',i=1)
    mc.file(templatePath+'/teeth_rig.mb',i=1)

def edo_chackAllFacialMeshes(meshes):
    #meshes=mc.ls(sl=1)
    for mesh in meshes:
        #mesh=meshes[0]
        if not 'msh_' in mesh:
            mel.eval('warning("All of the meshes of facial must have got prefix which name is <msh_> ")')
            return False
        if not mesh[-1]=='_':
            print mesh
            mel.eval('warning("All of the meshes of facial must have got <_> in the end of the name")')
            return False

#edo_createAllFcialMeshes('msh_')      
def edo_createAllFcialMeshes(mshstr):
    if mc.objExists('FACIAL_RIG_MESHES_FRAME'):
        edo_buildClFacialRigHierarchyNode()
        if mc.getAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED')==1:
            print 'facial meshes have already been created!,do it again that is not safe'
            return False
        bound=mc.xform('FACIAL_RIG_MESHES_FRAME',q=1,os=1,bb=1)
        h=bound[4]-bound[1]
        mc.setAttr('FACIAL_RIG_MESHES_FRAME.ty',mc.getAttr('FACIAL_RIG_MESHES_FRAME.ty')+(h*1.5))
        mc.makeIdentity('FACIAL_RIG_MESHES_FRAME',apply=1,t=1,r=1,s=1,n=0)
        allmeshes=mc.textField('facial_meshes_line',q=1,tx=1)
        if allmeshes:
            allmeshes=allmeshes.split(',')
            if allmeshes:
                check=edo_chackAllFacialMeshes(allmeshes)
                if check==False:
                    mc.confirmDialog( title='models are not canonical', message='the polygone modles are not canonical (you can see the script editor for more detail ) ,please check it!', button=['ok,i got it'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                mc.parent('FACIAL_RIG_MESHES_FRAME','GRP_CL_FACIALRIG_DEFORMER')
                edo_setLockTransform(allmeshes,0)
                if not mc.objExists('GRP_FCIAL_MESHES'):
                    #mc.delete('GRP_FCIAL_MESHES')
                    facialmeshesgrp=mc.group(allmeshes,n='GRP_FCIAL_MESHES')
                    rp=mc.xform(facialmeshesgrp,q=1,ws=1,rp=1)
                    mc.xform(facialmeshesgrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                else:
                    try:
                        mc.parent(allmeshes,'GRP_FCIAL_MESHES')
                    except:
                        print 'something is wrong!'
                allorg=[]
                #creaet org
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    #bs=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    #fs=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if mc.objExists('GRP_FCIAL_ORIGINAL_MESHES'):
                    mc.delete('GRP_FCIAL_ORIGINAL_MESHES')
                prggrp=mc.group(allorg,n='GRP_FCIAL_ORIGINAL_MESHES')
                rp=mc.xform(prggrp,q=1,ws=1,rp=1)
                mc.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                mc.parent(prggrp,'ORIGINAL_FRAME')
                mc.delete(mc.pointConstraint('ORIGINAL_FRAME',prggrp,mo=0))
                #creaet blendshape
                allorg=[]
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    #org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    #fs=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if mc.objExists('GRP_FCIAL_BLENDSHAPE_MESHES'):
                    mc.delete('GRP_FCIAL_BLENDSHAPE_MESHES')
                prggrp=mc.group(allorg,n='GRP_FCIAL_BLENDSHAPE_MESHES')
                rp=mc.xform(prggrp,q=1,ws=1,rp=1)
                mc.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                mc.parent(prggrp,'BLENDSHAPE_FRAME')
                mc.delete(mc.pointConstraint('BLENDSHAPE_FRAME',prggrp,mo=0))
                #creaet facial skin
                allorg=[]
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    #org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    #org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    org=mc.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if mc.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
                    mc.delete('GRP_FCIAL_FACIALSKIN_MESHES')
                prggrp=mc.group(allorg,n='GRP_FCIAL_FACIALSKIN_MESHES')
                rp=mc.xform(prggrp,q=1,ws=1,rp=1)
                mc.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                mc.parent(prggrp,'FACIALSKIN_FRAME')
                mc.delete(mc.pointConstraint('FACIALSKIN_FRAME',prggrp,mo=0))
                bs=mc.blendShape('GRP_FCIAL_BLENDSHAPE_MESHES','GRP_FCIAL_FACIALSKIN_MESHES',tc=1,foc=1,n='BS_FACIAL_BLENDSHAPE_OUTPUT')
                mc.setAttr(bs[0]+'.GRP_FCIAL_BLENDSHAPE_MESHES',1)
                bs=mc.blendShape('GRP_FCIAL_FACIALSKIN_MESHES','GRP_FCIAL_MESHES',tc=1,foc=1,n='BS_FACIAL_SKIN_OUTPUT')
                mc.setAttr(bs[0]+'.GRP_FCIAL_FACIALSKIN_MESHES',1)
                mc.setAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED',1)
                rp=mc.xform('GRP_FCIAL_FACIALSKIN_MESHES',q=1,ws=1,rp=1)
                tx=mc.getAttr('FACIAL_RIG_MESHES_FRAME.tx')
                mc.setAttr('FACIAL_RIG_MESHES_FRAME.tx',tx-rp[0])
                zjnt=mc.createNode('joint',n='FACIAL_ZERO_JOINT',p='GRP_FCIAL_FACIALSKIN_MESHES')
                mc.setAttr(zjnt+'.inheritsTransform',0)
                mc.parent(zjnt,'FACIALSKIN_FRAME')
                mc.delete(mc.pointConstraint('GRP_FCIAL_FACIALSKIN_MESHES',zjnt,mo=0))
                mc.setAttr(zjnt+'.v',0)
                edo_setLockTransform([zjnt],1)
                skmeshes=mc.listRelatives('GRP_FCIAL_FACIALSKIN_MESHES',c=1,pa=1)
                if skmeshes:
                    for skmesh in skmeshes:
                        #skmesh=skmeshes[0]
                        try:
                            sk=mc.skinCluster(zjnt,skmesh,rfs=0,tsb=1,mi=10)
                            mc.setAttr(sk[0]+'.skinningMethod',1)
                        except:
                            print 'there is something wrong with the  ...  '+ skmesh
                            edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME'],1)


def edo_setLockTransform(list,v):
    for l in list:
        #l='MSH_tongue_'
        mc.setAttr(l+'.tx',e=1,l=v)
        mc.setAttr(l+'.ty',e=1,l=v)
        mc.setAttr(l+'.tz',e=1,l=v)
        mc.setAttr(l+'.rx',e=1,l=v)
        mc.setAttr(l+'.ry',e=1,l=v)
        mc.setAttr(l+'.rz',e=1,l=v)
        mc.setAttr(l+'.sx',e=1,l=v)
        mc.setAttr(l+'.sy',e=1,l=v)
        mc.setAttr(l+'.sz',e=1,l=v)
    
def edo_autoLocationEyeballsCenter():
    sels=mc.ls(sl=1)
    if not sels:
        print 'you must select the eyeballs first!'
        return False
    template='GRP_EYEBALLS_TEMPLATE'
    mel.eval('newCluster " -envelope 1";')
    clus=mc.ls(sl=1)[0]
    piv=mc.xform(clus,q=1,ws=1,rp=1)
    mc.xform(template,ws=1,t=piv)
    mc.delete(clus)
    sel=sels[0]
    mc.select(sel)
    mel.eval('newCluster " -envelope 1";')
    clus=mc.ls(sl=1)[0]
    piv=mc.xform(clus,q=1,ws=1,rp=1)
    mc.delete(clus)
    mc.xform('Lf_eyeballs_joint0',ws=1,t=piv)
    mc.xform('Rt_eyeballs_joint0',ws=1,t=[piv[0]*-1,piv[1],piv[2]])

def edo_mirrorEyeballsSkeleton():
    t1=mc.xform('Lf_eyeballs_joint0',q=1,ws=1,t=1)
    t2=mc.xform('Lf_eyeballs_joint1',q=1,ws=1,t=1)
    t3=mc.xform('Lf_eyeballs_highlight_joint1',q=1,os=1,t=1)
    mc.xform('Rt_eyeballs_joint0',ws=1,t=[t1[0]*-1,t1[1],t1[2]])
    mc.xform('Rt_eyeballs_joint1',ws=1,t=[t2[0]*-1,t2[1],t2[2]])
    mc.xform('Rt_eyeballs_highlight_joint1',os=1,t=[t3[0],t3[1],t3[2]])

    
def edo_getComponentToTextEditor(texteditor):
    #texteditor='lfeyelids_loop_line'
    sels=mc.ls(orderedSelection=1,fl=1)
    if sels:
        list=''
        for sel in sels:
            list=list+sel+','
        list=list[:len(list)-1]
        mc.textField(texteditor,e=1,text=list)
    
def edo_createEyslids_skeleton():
    lfedges=mc.textField('lfeyelids_loop_line',q=1,tx=1)
    lfedgelist=lfedges.split(',')
    rtedges=mc.textField('rteyelids_loop_line',q=1,tx=1)
    rtedgelist=rtedges.split(',')
    lfeyelidsjnt=edo_createJointRingFromEdge(lfedgelist[0],'Lf_','GRP_EYEBALLS_TEMPLATE')
    rteyelidsjnt=edo_createJointRingFromEdge(rtedgelist[0],'Rt_','GRP_EYEBALLS_TEMPLATE')
    if mc.objExists('eyelids_influence'):
        mc.delete('eyelids_influence')
    mc.sets(lfeyelidsjnt+rteyelidsjnt,n='eyelids_influence')
    

def edo_createJointRingFromEdge(edge,prefix,parentobj):
    jnts=[]
    mc.select(edge,r=1)
    mc.SelectEdgeLoopSp()
    curve=mc.polyToCurve(form=2,degree=1,n=prefix+'eyelids_ring_curve')
    mc.parent(curve[0],parentobj)
    mc.delete(curve[1])
    spans=mc.getAttr(curve[0]+'.spans')
    degree=mc.getAttr(curve[0]+'.degree')
    cvnum=spans+degree
    for i in range(0,cvnum-1):
        #i=0
        jnt=mc.createNode('joint',n=prefix+'eyelids_jnt'+str(i),p=curve[0])
        mc.xform(jnt,ws=1,t=mc.xform(curve[0]+'.cv['+str(i)+']',q=1,ws=1,t=1))
        jnts.append(jnt)
    return jnts

def edo_buildClEyelids_skeleton_drivenMesh(edge,prefix,parentobj):
    #edge=Lfedge
    #prefix='Lfeyelids_'
    #parentobj='FACIALSKIN_FRAME'
    mc.select(edge,r=1)
    mc.SelectEdgeLoopSp()
    curve=mc.polyToCurve(form=2,degree=1,n=prefix+'_skeleton_drivenMesh_curve')
    mc.delete(curve[1])
    dupcurve=mc.duplicate(curve[0],n=curve[0]+'_OFFSET')
    mc.setAttr(dupcurve[0]+'.tz',0.1)
    lofts=mc.loft(curve[0],dupcurve[0],ch=1,u=1,c=0,ar=1,d=3,ss=1,rn=0,po=1,rsn=1,n=prefix+'_skeleton_dirvenMesh_')
    tess=edo_findNodeFromHis(lofts[0],'nurbsTessellate')
    mc.setAttr(tess+'.uType',3)
    mc.setAttr(tess+'.uNumber',1)
    mc.setAttr(tess+'.vType',3)
    mc.setAttr(tess+'.vNumber',1)
    mc.setAttr(tess+'.polygonType',1)
    mc.setAttr(tess+'.format',2)
    mc.select(lofts[0],r=1)
    mc.DeleteHistory()
    mc.CenterPivot()
    mc.parent(lofts[0],parentobj)
    rp=mc.xform(parentobj,q=1,ws=1,rp=1)
    mc.xform(lofts[0],ws=1,rp=rp,sp=rp)
    mc.delete(curve[0],dupcurve[0])
    return lofts[0]

def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=mc.listHistory(name)
    for his in hiss:
        if mc.nodeType(his)==type:
            node=his
    return node

def edo_buildClFacialRigHierarchyNode():
    if not mc.objExists('GRP_CL_FACIALRIG_DEFORMER'):
        mc.createNode('transform',n='GRP_CL_FACIALRIG_DEFORMER')
    if not mc.objExists('GRP_CL_FACIALRIG_FOLLOWHEAD_NODE'):
        mc.createNode('transform',n='GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    if not mc.objExists('GRP_CL_ALL_FACIALRIG_JOINTS'):
        mc.createNode('transform',n='GRP_CL_ALL_FACIALRIG_JOINTS',p='GRP_CL_FACIALRIG_DEFORMER')
    if not mc.objExists('GRP_CL_FACIALRIG_FOLLOWBODY_NODE'):
        mc.createNode('transform',n='GRP_CL_FACIALRIG_FOLLOWBODY_NODE')

def edo_createEyeballsRig(mshstr):
    edo_buildClFacialRigHierarchyNode()
    if not mc.objExists('GRP_EYEBALLS_TEMPLATE'):
        return False
    #createEyeballsRig
    mc.joint('Lf_eyeballs_joint0',e=1,oj='xyz',sao='yup',zso=1)
    mc.joint('Rt_eyeballs_joint0',e=1,oj='xyz',sao='yup',zso=1)
    #lf high light driven joint
    mc.createNode('joint',n='Lf_eyeballs_highlight_DIV_joint0',p='Lf_eyeballs_joint0')
    mc.xform('Lf_eyeballs_highlight_DIV_joint0',os=1,t=[0,0,0])
    #lf high light joint
    mc.createNode('joint',n='Lf_eyeballs_highlight_joint0',p='Lf_eyeballs_highlight_DIV_joint0')
    mc.xform('Lf_eyeballs_highlight_joint0',os=1,t=[0,0,0])
    mc.parent('Lf_eyeballs_highlight_joint1','Lf_eyeballs_highlight_joint0')
    #rt high light driven joint
    mc.createNode('joint',n='Rt_eyeballs_highlight_DIV_joint0',p='Rt_eyeballs_joint0')
    mc.xform('Rt_eyeballs_highlight_DIV_joint0',os=1,t=[0,0,0])
    #rt high light joint
    mc.createNode('joint',n='Rt_eyeballs_highlight_joint0',p='Rt_eyeballs_highlight_DIV_joint0')
    mc.xform('Rt_eyeballs_highlight_joint0',os=1,t=[0,0,0])
    mc.parent('Rt_eyeballs_highlight_joint1','Rt_eyeballs_highlight_joint0')
    #create eyeballs constraint
    uploc=mc.spaceLocator(n='Loc_eyeballs_upVector',p=mc.xform('GRP_EYEBALLS_TEMPLATE',q=1,ws=1,t=1))
    mc.parent(uploc,'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    mc.aimConstraint('c_Lf_eye_M','Lf_eyeballs_joint0',mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='objectrotation',worldUpVector=[0,1,0],worldUpObject=uploc[0])
    mc.aimConstraint('c_Rt_eye_M','Rt_eyeballs_joint0',mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='objectrotation',worldUpVector=[0,1,0],worldUpObject=uploc[0])
    #set parent
    mc.parent('EYE_RIG','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    mc.parent('Lf_eyeballs_joint0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    mc.parent('Rt_eyeballs_joint0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    #set head follow
    bodyloc=mc.spaceLocator(n='Loc_body_constraint',p=mc.xform('GRP_EYEBALLS_TEMPLATE',q=1,ws=1,t=1))
    mc.parent(bodyloc,'GRP_CL_FACIALRIG_FOLLOWBODY_NODE')
    mc.parentConstraint(bodyloc[0],'EYE_RIG',mo=1)
    mc.setKeyframe('EYE_RIG.tx')
    mc.setKeyframe('EYE_RIG.ty')
    mc.setKeyframe('EYE_RIG.tz')
    mc.setKeyframe('EYE_RIG.rx')
    mc.setKeyframe('EYE_RIG.ry')
    mc.setKeyframe('EYE_RIG.rz')
    revers=mc.createNode('reverse')
    bl=mc.listConnections('EYE_RIG.tx',s=1,d=0)
    mc.connectAttr('c_eye_M.follow',revers+'.inputX',f=1)
    mc.connectAttr(revers+'.outputX',bl[0]+'.weight',f=1)
    mc.delete('EYE_RIGShape')
    edo_setLockTransform(['c_eye_M'],0)
    #create high light rig
    mc.connectAttr('MD_Lf_eyeballs_highlight.outputX','Lf_eyeballs_highlight_DIV_joint0.ry',f=1)
    mc.connectAttr('MD_Lf_eyeballs_highlight.outputY','Lf_eyeballs_highlight_DIV_joint0.rz',f=1)
    mc.connectAttr('MD_Rt_eyeballs_highlight.outputX','Rt_eyeballs_highlight_DIV_joint0.ry',f=1)
    mc.connectAttr('MD_Rt_eyeballs_highlight.outputY','Rt_eyeballs_highlight_DIV_joint0.rz',f=1)
    ######c_Lf_spec_tempMod_M.tx  Lf_eyeballs_highlight_DIV_joint0
    ######c_Rt_spec_tempMod_M.tx  Rt_eyeballs_highlight_DIV_joint0
    #======================================================================================
    #createEyelidsRig
    #lf eyelids
    if mc.objExists('Lf_eyelids_ring_curve'):
        jnts=mc.listRelatives('Lf_eyelids_ring_curve',c=1,type='joint',pa=1)
        if jnts:
            cjnt=mc.createNode('joint',n='Lf_eyelids_all_jnt0',p='Lf_eyeballs_highlight_joint0')
            mc.xform('Lf_eyelids_all_jnt0',os=1,t=[0,0,0])
            mc.parent('Lf_eyelids_all_jnt0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
            for jnt in jnts:
                #jnt=jnts[0]
                djnt=mc.createNode('joint',n=jnt.replace('jnt','DIV_jnt'),p='Lf_eyelids_all_jnt0')
                rjnt=mc.createNode('joint',n=jnt.replace('jnt','rotate_jnt'),p=djnt)
                mc.parent(jnt,rjnt)
    #Rt eyelids
    if mc.objExists('Rt_eyelids_ring_curve'):
        jnts=mc.listRelatives('Rt_eyelids_ring_curve',c=1,type='joint',pa=1)
        if jnts:
            cjnt=mc.createNode('joint',n='Rt_eyelids_all_jnt0',p='Rt_eyeballs_highlight_joint0')
            mc.xform('Rt_eyelids_all_jnt0',os=1,t=[0,0,0])
            mc.parent('Rt_eyelids_all_jnt0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
            for jnt in jnts:
                #jnt=jnts[0]
                djnt=mc.createNode('joint',n=jnt.replace('jnt','DIV_jnt'),p='Rt_eyelids_all_jnt0')
                rjnt=mc.createNode('joint',n=jnt.replace('jnt','rotate_jnt'),p=djnt)
                mc.parent(jnt,rjnt)
    if mc.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
        edo_setLockTransform(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],1)
        mc.parent(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],'GRP_FCIAL_FACIALSKIN_MESHES')
        edo_setLockTransform(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],0)
    #add skin
    Lfedges=mc.textField('lfeyelids_loop_line',q=1,tx=1)
    Rtedges=mc.textField('rteyelids_loop_line',q=1,tx=1)
    edges=Lfedges+','+Rtedges
    if edges:
        edges=edges.split(',')
        if edges:
            mesh=edges[0].split('.')[0].replace(mshstr,mshstr+'FACIALSKIN_')
            if not mc.objExists(mesh):
                print 'there is no mesh that name is '+mesh+' . So the program cound not add skin to it.'
                return False
            sks=edo_findNodeFromHistory(mesh,'skinCluster')
            if sks:
                sk=sks[0]
                #jnts=mc.ls(sl=1)
                if not mc.objExists('eyelids_influence'):
                    print 'there is no set that name is eyelids_influence . So the program cound not add skin to it.'
                    return False
                jnts=mc.sets('eyelids_influence',q=1)
                mc.skinCluster(sk,e=1,ai=jnts,lw=1,wt=0)
                #auto compute the skin weight
                #find all vertex
                #Left eyelids
                lfedges=Lfedges.split(',')
                count=len(lfedges)
                addw=1.0/(count-1)
                vtx_cjnt_w=[]
                for i in range(0,count):
                    #i=0
                    w=(count-i-1)*addw
                    print w
                    mc.select(lfedges[i],r=1)
                    mc.SelectEdgeLoopSp()
                    mc.ConvertSelectionToVertices()
                    alleyelids_vertex=mc.ls(sl=1,fl=1)
                    #compute weight
                    #################
                    for v in alleyelids_vertex:
                        #v=alleyelids_vertex[5]
                        skv=v.replace(mshstr,mshstr+'FACIALSKIN_')
                        if mc.objExists(skv):
                            #find closest skeleton
                            vp=mc.xform(skv,q=1,ws=1,t=1)
                            mixdis=10000000.0
                            cjnt=''
                            for jnt in jnts:
                                #jnt=jnts[0]
                                jp=mc.xform(jnt,q=1,ws=1,t=1)
                                vecter=om.MVector((vp[0]-jp[0]),(vp[1]-jp[1]),(vp[2]-jp[2]))
                                dis=vecter.length()
                                if dis<mixdis:
                                    mixdis=dis
                                    cjnt=jnt
                            vtx_cjnt_w.append([skv,cjnt,w])
                            print 'vetex: '+skv+'  ......  closestJoint: '+cjnt+'  ......  weight: '+str(w)
                            mc.skinPercent(sk,skv,tv=(cjnt,w))
                #Right eyelids
                rtedges=Rtedges.split(',')
                count=len(rtedges)
                addw=1.0/(count-1)
                vtx_cjnt_w=[]
                for i in range(0,count):
                    #i=0
                    w=(count-i-1)*addw
                    print w
                    mc.select(rtedges[i],r=1)
                    mc.SelectEdgeLoopSp()
                    mc.ConvertSelectionToVertices()
                    alleyelids_vertex=mc.ls(sl=1,fl=1)
                    #compute weight
                    #################
                    for v in alleyelids_vertex:
                        #v=alleyelids_vertex[5]
                        skv=v.replace(mshstr,mshstr+'FACIALSKIN_')
                        if mc.objExists(skv):
                            #find closest skeleton
                            vp=mc.xform(skv,q=1,ws=1,t=1)
                            mixdis=10000000.0
                            cjnt=''
                            for jnt in jnts:
                                #jnt=jnts[0]
                                jp=mc.xform(jnt,q=1,ws=1,t=1)
                                vecter=om.MVector((vp[0]-jp[0]),(vp[1]-jp[1]),(vp[2]-jp[2]))
                                dis=vecter.length()
                                if dis<mixdis:
                                    mixdis=dis
                                    cjnt=jnt
                            vtx_cjnt_w.append([skv,cjnt,w])
                            print 'vetex: '+skv+'  ......  closestJoint: '+cjnt+'  ......  weight: '+str(w)
                            mc.skinPercent(sk,skv,tv=(cjnt,w))
                #add eyelids skeleton dirven mesh
                Lfedge=Lfedges.split(',')[0].replace(mshstr,mshstr+'FACIALSKIN_')
                Rtedge=Rtedges.split(',')[0].replace(mshstr,mshstr+'FACIALSKIN_')
                lfmesh=edo_buildClEyelids_skeleton_drivenMesh(Lfedge,'Lfeyelids','FACIALSKIN_FRAME')
                rtmesh=edo_buildClEyelids_skeleton_drivenMesh(Rtedge,'Rteyelids','FACIALSKIN_FRAME')
                lfmeshget=mc.duplicate(lfmesh,n=lfmesh.replace('Lfeyelids','Lfeyelids_getbs'))[0]
                rtmeshget=mc.duplicate(rtmesh,n=rtmesh.replace('Rteyelids','Rteyelids_getbs'))[0]
                mc.setAttr(lfmeshget+'.sx',-1)
                mc.setAttr(lfmeshget+'.v',0)
                mc.setAttr(rtmeshget+'.sx',-1)
                mc.setAttr(rtmeshget+'.v',0)
                wrapcmd='CreateWrap;'
                mc.select(lfmeshget,r=1)
                mc.select(rtmesh,add=1)
                mel.eval(wrapcmd)
                mc.select(rtmeshget,r=1)
                mc.select(lfmesh,add=1)
                mel.eval(wrapcmd)
                #lfmesh='Lfeyelids_skeleton_dirvenMesh' rtmesh='Rteyelids_skeleton_dirvenMesh'
                fos=[]
                for jnt in jnts:
                    if 'Lf_' in jnt:
                        fos.append(edo_createFollicleToMeshByClosestObj(lfmesh,jnt,1))
                for jnt in jnts:
                    if 'Rt_' in jnt:
                        fos.append(edo_createFollicleToMeshByClosestObj(rtmesh,jnt,1))
                print fos
                if mc.objExists('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE'):
                    mc.delete('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                grp=mc.group(fos,n='GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                mc.parent(grp,'FACIALSKIN_FRAME')
                mc.setAttr('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE.v',0)
                edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME','FACIALSKIN_FRAME'],1)
    mc.delete('GRP_EYEBALLS_TEMPLATE')
    
def edo_finishEyeRig():
    Lfedges=mc.textField('lfeyelids_loop_line',q=1,tx=1)
    Rtedges=mc.textField('rteyelids_loop_line',q=1,tx=1)
    if Lfedges and Rtedges:
        print 'finish eye rig!'
        edo_createEyslids_skeleton()
        edo_createEyeballsRig('msh_')
    else:
        mc.confirmDialog( title='can not find the edges of eyelids', message='can not find the edges of eyelids,you must appoint the edges of eyelids to the textline editor', button=['ok,i got it'], defaultButton='Yes', cancelButton='No', dismissString='No')
                
def edo_finishTongueRig():
    edo_buildClFacialRigHierarchyNode()
    if not mc.objExists('GRP_TONGUE_TEMPLATE'):
        return False
    ctrls=mc.ls('c_tongue_joint*')
    for ctrl in ctrls:
        #ctrl=ctrls[0]
        tp=mc.listRelatives(ctrl,p=1,pa=1)
        if tp:
            rp=mc.listRelatives(tp[0],p=1,pa=1)
            if rp:
                if 'move' in rp[0]:
                   mc.setAttr(rp[0]+'.tx',mc.getAttr(ctrl+'.tx'))
                   mc.setAttr(rp[0]+'.ty',mc.getAttr(ctrl+'.ty'))
                   mc.setAttr(rp[0]+'.tz',mc.getAttr(ctrl+'.tz'))
                   mc.setAttr(rp[0]+'.rx',mc.getAttr(ctrl+'.rx'))
                   mc.setAttr(rp[0]+'.ry',mc.getAttr(ctrl+'.ry'))
                   mc.setAttr(rp[0]+'.rz',mc.getAttr(ctrl+'.rz'))
                   #setZero
                   mc.setAttr(ctrl+'.tx',0)
                   mc.setAttr(ctrl+'.ty',0)
                   mc.setAttr(ctrl+'.tz',0)
                   mc.setAttr(ctrl+'.rx',0)
                   mc.setAttr(ctrl+'.ry',0)
                   mc.setAttr(ctrl+'.rz',0)
    if mc.objExists('tongue_influence'):
        infs=mc.sets('tongue_influence',q=1)
        meshes=lfedges=mc.textField('get_tonguemeshes_line',q=1,tx=1)
        meshs=meshes.split(',')
        if meshs:
            for mesh in meshs:    
                #mesh=meshs[0]
                mc.skinCluster(infs,mesh,rfs=0,tsb=1,mi=len(infs))
                if mc.objExists('tongue_skinMesh'):
                    mc.copySkinWeights('tongue_skinMesh',mesh,noMirror=1,surfaceAssociation='closestPoint',influenceAssociation='closestJoint')
    #connect to tongue crtl
    if mc.objExists('GRP_PANNEL_TEMPLATE'):
        mc.connectAttr('c_tongue_CTRL.rotateWeight','Tongue_M.rotateWeight',f=1)
        mc.connectAttr('c_tongue_CTRL.drivenJoint','Tongue_M.drivenJoint',f=1)
        mc.connectAttr('c_tongue_CTRL.second_vis','Tongue_M.vis_second',f=1)
        mc.connectAttr('c_tongue_CTRL.output_tx','Tongue_M.tx',f=1)
        mc.connectAttr('c_tongue_CTRL.output_ty','Tongue_M.ty',f=1)
        mc.connectAttr('c_tongue_CTRL.output_stretch','Tongue_M.tz',f=1)
        mc.connectAttr('c_tongue_CTRL.output_rx','Tongue_M.rx',f=1)
        mc.connectAttr('c_tongue_CTRL.output_ry','Tongue_M.ry',f=1)
        mc.connectAttr('c_tongue_CTRL.output_rz','Tongue_M.rz',f=1)
        mc.setAttr('Tongue_MShape.v',0)
    mc.parent('GRP_tongue_Rig_all','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    mc.delete('GRP_TONGUE_TEMPLATE','GRP_Tongue_M_moveShape')


def edo_createFollicleToMeshByClosestObj(mesh,obj,addAimConstraint=0):
    #mesh=lfmesh
    #obj=jnt
    #addAimConstraint=1
    cn=mc.createNode('closestPointOnMesh',n='CL_EYELIDS_CLOSEST_POINT_ON_MESH')
    mc.connectAttr(mesh+'.outMesh',cn+'.inMesh',f=1)
    rp=mc.xform(obj,q=1,ws=1,rp=1)
    mc.setAttr(cn+'.inPositionX',rp[0])
    mc.setAttr(cn+'.inPositionY',rp[1])
    mc.setAttr(cn+'.inPositionZ',rp[2])
    #createFollicle
    fot=mc.createNode('transform',n=obj+'_closestFollicle')
    fo=mc.createNode('follicle',n=obj+'_closestFollicleShape',p=fot)
    mc.connectAttr(fo+'.outTranslateX',fot+'.translateX',f=1)
    mc.connectAttr(fo+'.outTranslateY',fot+'.translateY',f=1)
    mc.connectAttr(fo+'.outTranslateZ',fot+'.translateZ',f=1)
    mc.connectAttr(fo+'.outRotateX',fot+'.rotateX',f=1)
    mc.connectAttr(fo+'.outRotateY',fot+'.rotateY',f=1)
    mc.connectAttr(fo+'.outRotateZ',fot+'.rotateZ',f=1)
    mc.connectAttr(mesh+'.outMesh',fo+'.inputMesh',f=1)
    mc.connectAttr(mesh+'.worldMatrix',fo+'.inputWorldMatrix',f=1)
    mc.setAttr(fo+'.parameterU',mc.getAttr(cn+'.parameterU'))
    mc.setAttr(fo+'.parameterV',mc.getAttr(cn+'.parameterV'))
    mc.delete(cn)
    if addAimConstraint==1:
        ps=mc.listRelatives(obj,p=1,pa=1)
        if ps:
            ps=mc.listRelatives(ps[0],p=1,pa=1)
            if ps:
                mc.aimConstraint(fot,ps[0],mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='scene')
    return fot
    
def edo_findNodeFromHistory(node,type):
    #node=mesh
    find=[]
    his=mc.listHistory(node)
    for h in his:
        #h=his[0]
        if mc.nodeType(h)==type:
            find.append(h)
    return find
    

def edo_finishJawRig():
    edo_buildClFacialRigHierarchyNode()
    if not mc.objExists('GRP_JAW_TEMPLATE') and not mc.objExists('GRP_PANNEL_TEMPLATE'):
        return False
    #lower connect 
    mc.connectAttr('c_jaw_dn_FRAME.fourAxis_up','low_jaw_joint0.up_driven',f=1)
    mc.connectAttr('c_jaw_dn_FRAME.fourAxis_dn','low_jaw_joint0.dn_driven',f=1)
    mc.connectAttr('c_jaw_dn_FRAME.fourAxis_rt','low_jaw_joint0.lf_driven',f=1)
    mc.connectAttr('c_jaw_dn_FRAME.fourAxis_lf','low_jaw_joint0.rt_driven',f=1)
    #uper connect
    mc.connectAttr('c_jaw_up_FRAME.fourAxis_up','up_jaw_joint0.up_driven',f=1)
    mc.connectAttr('c_jaw_up_FRAME.fourAxis_dn','up_jaw_joint0.dn_driven',f=1)
    mc.connectAttr('c_jaw_up_FRAME.fourAxis_rt','up_jaw_joint0.lf_driven',f=1)
    mc.connectAttr('c_jaw_up_FRAME.fourAxis_lf','up_jaw_joint0.rt_driven',f=1)
    #create Jaw joint
    jnt=mc.createNode('joint',n='JAW_ALL_JNT',p='GRP_JAW_TEMPLATE')
    mc.xform('JAW_ALL_JNT',os=1,t=[0,0,0])
    mc.parent('JAW_ALL_JNT','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    mc.parent('low_jaw_inverse_joint0','JAW_ALL_JNT')
    mc.parent('up_jaw_inverse_joint','JAW_ALL_JNT')
    mc.delete('GRP_JAW_TEMPLATE')
    if mc.objExists('GRP_tongueRig'):
        #mc.parentConstraint('low_jaw_joint0','GRP_tongueRig',mo=1)
        mc.connectAttr('c_jaw_dn_FRAME.fourAxis_up','c_tongue_joint1.up_driven',f=1)
        mc.connectAttr('c_jaw_dn_FRAME.fourAxis_dn','c_tongue_joint1.dn_driven',f=1)
        mc.connectAttr('c_jaw_dn_FRAME.fourAxis_rt','c_tongue_joint1.lf_driven',f=1)
        mc.connectAttr('c_jaw_dn_FRAME.fourAxis_lf','c_tongue_joint1.rt_driven',f=1)

def edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections():
    rtbsmaker='Rteyelids_getbs_skeleton_dirvenMesh_'
    if not mc.objExists(rtbsmaker):
        print 'error ! there is no object what name is '+rtbsmaker
        return False
    rteyelidsDrivenMesh='Rteyelids_skeleton_dirvenMesh_'
    if not mc.objExists(rteyelidsDrivenMesh):
        print 'error ! there is no object what name is '+rteyelidsDrivenMesh
        return False
    lfctrl='c_Lf_up_eyelids_CTRL'
    if not mc.objExists(lfctrl):
        print 'error ! there is no object what name is '+lfctrl
        return False
    rtctrl='c_Rt_up_eyelids_CTRL'
    if not mc.objExists(rtctrl):
        print 'error ! there is no object what name is '+rtctrl
        return False
    lfdnctrl='c_Lf_dn_eyelids_CTRL'
    if not mc.objExists(lfctrl):
        print 'error ! there is no object what name is '+lfdnctrl
        return False
    rtdnctrl='c_Rt_dn_eyelids_CTRL'
    if not mc.objExists(rtctrl):
        print 'error ! there is no object what name is '+rtdnctrl
        return False
    print 'mirror eyelids start...'
    frames=['c_Lf_up_eyelids_CTRL_up','c_Lf_up_eyelids_CTRL_rtup','c_Lf_up_eyelids_CTRL_lfup','c_Lf_up_eyelids_CTRL_dn','c_Lf_up_eyelids_CTRL_rtdn','c_Lf_up_eyelids_CTRL_lfdn','c_Lf_up_eyelids_CTRL_lf','c_Lf_up_eyelids_CTRL_rt']
    for frame in frames:
        #frame=frames[0]
        if mc.objExists(frame):
            if 'RL_up' == frame[-5:]:
                print 'make up blendshape'
                mc.setAttr(lfctrl+'.ty',1)
                mc.setAttr(lfctrl+'.tx',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.ty',0)
            if 'RL_dn' == frame[-5:]:
                print 'make dn blendshape'
                mc.setAttr(lfctrl+'.ty',-1)
                mc.setAttr(lfctrl+'.tx',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.ty',0)
            if 'RL_lf' == frame[-5:]:
                print 'make lf blendshape'
                mc.setAttr(lfctrl+'.tx',-1)
                mc.setAttr(lfctrl+'.ty',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
            if 'RL_rt' == frame[-5:]:
                print 'make rt blendshape'
                mc.setAttr(lfctrl+'.tx',1)
                mc.setAttr(lfctrl+'.ty',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
            if '_lfup' == frame[-5:]:
                print 'make lfup blendshape'
                mc.setAttr(lfctrl+'.tx',-1)
                mc.setAttr(lfctrl+'.ty',1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
                mc.setAttr(lfctrl+'.ty',0)
            if '_lfdn' == frame[-5:]:
                print 'make lfdn blendshape'
                mc.setAttr(lfctrl+'.tx',-1)
                mc.setAttr(lfctrl+'.ty',-1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
                mc.setAttr(lfctrl+'.ty',0)
            if '_rtup' == frame[-5:]:
                print 'make rtup blendshape'
                mc.setAttr(lfctrl+'.tx',1)
                mc.setAttr(lfctrl+'.ty',1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
                mc.setAttr(lfctrl+'.ty',0)
            if '_rtdn' == frame[-5:]:
                print 'make rtdn blendshape'
                mc.setAttr(lfctrl+'.tx',1)
                mc.setAttr(lfctrl+'.ty',-1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfctrl+'.tx',0)
                mc.setAttr(lfctrl+'.ty',0)
    #mirror down eyelids blendshape
    frames=['c_Lf_dn_eyelids_CTRL_up','c_Lf_dn_eyelids_CTRL_rtup','c_Lf_dn_eyelids_CTRL_lfup','c_Lf_dn_eyelids_CTRL_dn','c_Lf_dn_eyelids_CTRL_rtdn','c_Lf_dn_eyelids_CTRL_lfdn','c_Lf_dn_eyelids_CTRL_lf','c_Lf_dn_eyelids_CTRL_rt']
    for frame in frames:
        #frame=frames[0]
        if mc.objExists(frame):
            if 'RL_up' == frame[-5:]:
                print 'make up blendshape'
                mc.setAttr(lfdnctrl+'.ty',1)
                mc.setAttr(lfdnctrl+'.tx',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.ty',0)
            if 'RL_dn' == frame[-5:]:
                print 'make dn blendshape'
                mc.setAttr(lfdnctrl+'.ty',-1)
                mc.setAttr(lfdnctrl+'.tx',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.ty',0)
            if 'RL_lf' == frame[-5:]:
                print 'make lf blendshape'
                mc.setAttr(lfdnctrl+'.tx',-1)
                mc.setAttr(lfdnctrl+'.ty',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
            if 'RL_rt' == frame[-5:]:
                print 'make rt blendshape'
                mc.setAttr(lfdnctrl+'.tx',1)
                mc.setAttr(lfdnctrl+'.ty',0)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
            if '_lfup' == frame[-5:]:
                print 'make lfup blendshape'
                mc.setAttr(lfdnctrl+'.tx',-1)
                mc.setAttr(lfdnctrl+'.ty',1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
                mc.setAttr(lfdnctrl+'.ty',0)
            if '_lfdn' == frame[-5:]:
                print 'make lfdn blendshape'
                mc.setAttr(lfdnctrl+'.tx',-1)
                mc.setAttr(lfdnctrl+'.ty',-1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
                mc.setAttr(lfdnctrl+'.ty',0)
            if '_rtup' == frame[-5:]:
                print 'make rtup blendshape'
                mc.setAttr(lfdnctrl+'.tx',1)
                mc.setAttr(lfdnctrl+'.ty',1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
                mc.setAttr(lfdnctrl+'.ty',0)
            if '_rtdn' == frame[-5:]:
                print 'make rtdn blendshape'
                mc.setAttr(lfdnctrl+'.tx',1)
                mc.setAttr(lfdnctrl+'.ty',-1)
                bs=mc.duplicate(rtbsmaker)
                mc.setAttr(bs[0]+'.v',1)
                mc.setAttr(bs[0]+'.sx',1)
                nbs=mc.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                mc.parent(nbs,frame.replace('Lf','Rt'))
                mc.setAttr(lfdnctrl+'.tx',0)
                mc.setAttr(lfdnctrl+'.ty',0)
    edo_opBlendShapeByFacialCtrl(rtctrl)
    edo_addBlendShapeAndExpressionsByFacialCtrl(rtctrl)
    edo_opBlendShapeByFacialCtrl(rtdnctrl)
    edo_addBlendShapeAndExpressionsByFacialCtrl(rtdnctrl)
    
def edo_clearFacialBlendShapeInFrame(frame):
    #frame='c_Rt_up_eyelids_CTRL_up'
    cs=mc.listRelatives(frame,c=1,pa=1)
    for c in cs:
        #c=cs[0]
        cc=mc.listRelatives(c,shapes=1,pa=1)
        if cc:
            cshape=cc[0]
            if mc.nodeType(cshape)=='mesh':
                print 'clear .. '+frame+' .. '+c
                mc.delete(c)