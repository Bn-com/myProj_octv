#-*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
import maya.OpenMaya as om

execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_autoConnectBlendShapeUI.py')
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_cl_checkRiggingFileUI.py')

def edo_cl_facial_rig_ui():
    ui='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_cl_facial_rig_ui.myuis'
    if cmds.window('edo_cl_facial_rig_ui',ex=1):
        cmds.deleteUI('edo_cl_facial_rig_ui')
    mui=cmds.loadUI(f=ui)
    #import template
    cmds.button('importTemplate_bt',e=1,c='edo_importFacialTemplate()',ann='�����沿����Ҫ��ģ��')
    #check model
    cmds.button('facial_check_bt',e=1,c='edo_openDocumentFromPath(\'Z:/Resource/Support/Maya/extra/Rigging_Simulation/helpDocument/project/calimero/calimero_facial_rigging_tool_model_check.docx.docx\')',ann='�򿪹���ʹ��ǰ��ģ�ͼ���ĵ�')
    #start
    cmds.button('facial_meshes_bt',e=1,c='edo_getComponentToTextEditor(\'facial_meshes_line\')',ann='��ͷ�����е�ģ�����뵽�б���')
    cmds.button('create_meshes_bt',e=1,c='edo_createAllFcialMeshes(\'msh_\')',ann='�����沿��ʱ��Ҫ�����е�ͷ��ģ��')
    #tongue_tab
    cmds.button('finish_tonguerig_bt',e=1,c='edo_finishTongueRig()')
    cmds.button('get_tonguemeshes_bt',e=1,c='edo_getComponentToTextEditor(\'get_tonguemeshes_line\')')
    #jaw_tab
    cmds.button('finish_jaw_bt',e=1,c='edo_finishJawRig()')
    #eye_rig
    cmds.button('eyeball_autoloc_bt',e=1,c='edo_autoLocationEyeballsCenter()',ann='ѡ�������Բ�κ�Ĥִ��,��ס����ѡ�����۵ĺ�Ĥ����ѡ�����۵�')
    cmds.button('eyeball_mirror_bt',e=1,c='edo_mirrorEyeballsSkeleton()',ann='������ߵ�����������ұ�')
    cmds.button('lfeyelids_loop_bt',e=1,c='edo_getComponentToTextEditor(\'lfeyelids_loop_line\')',ann='����ѡ�����۴��ڵ������Ƥ��ִ��,�����ɹ�����Ҫʱ�̱����������������')
    cmds.button('rteyelids_loop_bt',e=1,c='edo_getComponentToTextEditor(\'rteyelids_loop_line\')',ann='����ѡ�����۴��ڵ������Ƥ��ִ��,�����ɹ�����Ҫʱ�̱����������������')
    cmds.button('finish_eyerig_bt',e=1,c='edo_finishEyeRig()',ann='�Ƚ���Ƥ����������Ŀ��ִ��')
    #cmds.button('eyelids_autoloc_bt',e=1,c='edo_createEyslids_skeleton()',ann='�Ƚ���Ƥ����������Ŀ��ִ��')
    cmds.button('mirrorEyelids_blendshape_bt',e=1,c='edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections()',ann='ֱ��ִ�д������ʹ����Ƥ������ģ��Ŀ���徵���ұ���Ƥ')
    cmds.button('check_calimeroRig_bt',e=1,c='edo_cl_checkRiggingFileUI()',ann='calimero�������淶��鹤��')
    cmds.showWindow(mui)

def edo_openDocumentFromPath(path):
    #path='Z:/Resource/Support/Maya/extra/Rigging_Simulation/helpDocument/project/calimero/calimero_facial_rigging_tool_model_check.docx.docx'
    cmd="system(\"load "+path+"\")"
    mel.eval(cmd)

def edo_importFacialTemplate():
    templatePath='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/mayaFile'
    cmds.file(templatePath+'/eyeballs_rig.ma',i=1)
    cmds.file(templatePath+'/pannel_rig.ma',i=1)
    cmds.file(templatePath+'/jaw_rig.ma',i=1)
    cmds.file(templatePath+'/tongue_rig.ma',i=1)
    cmds.file(templatePath+'/frame_rig.ma',i=1)

def edo_chackAllFacialMeshes(meshes):
    #meshes=cmds.ls(sl=1)
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
    if cmds.objExists('FACIAL_RIG_MESHES_FRAME'):
        edo_buildClFacialRigHierarchyNode()
        if cmds.getAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED')==1:
            print 'facial meshes have already been created!,do it again that is not safe'
            return False
        bound=cmds.xform('FACIAL_RIG_MESHES_FRAME',q=1,os=1,bb=1)
        h=bound[4]-bound[1]
        cmds.setAttr('FACIAL_RIG_MESHES_FRAME.ty',cmds.getAttr('FACIAL_RIG_MESHES_FRAME.ty')+(h*1.5))
        cmds.makeIdentity('FACIAL_RIG_MESHES_FRAME',apply=1,t=1,r=1,s=1,n=0)
        allmeshes=cmds.textField('facial_meshes_line',q=1,tx=1)
        if allmeshes:
            allmeshes=allmeshes.split(',')
            if allmeshes:
                check=edo_chackAllFacialMeshes(allmeshes)
                if check==False:
                    cmds.confirmDialog( title='models are not canonical', message='the polygone modles are not canonical (you can see the script editor for more detail ) ,please check it!', button=['ok,i got it'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    return False
                cmds.parent('FACIAL_RIG_MESHES_FRAME','GRP_CL_FACIALRIG_DEFORMER')
                edo_setLockTransform(allmeshes,0)
                if not cmds.objExists('GRP_FCIAL_MESHES'):
                    #cmds.delete('GRP_FCIAL_MESHES')
                    facialmeshesgrp=cmds.group(allmeshes,n='GRP_FCIAL_MESHES')
                    rp=cmds.xform(facialmeshesgrp,q=1,ws=1,rp=1)
                    cmds.xform(facialmeshesgrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                else:
                    try:
                        cmds.parent(allmeshes,'GRP_FCIAL_MESHES')
                    except:
                        print 'something is wrong!'
                allorg=[]
                #creaet org
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    #bs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    #fs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_ORIGINAL_MESHES'):
                    cmds.delete('GRP_FCIAL_ORIGINAL_MESHES')
                prggrp=cmds.group(allorg,n='GRP_FCIAL_ORIGINAL_MESHES')
                rp=cmds.xform(prggrp,q=1,ws=1,rp=1)
                cmds.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                cmds.parent(prggrp,'ORIGINAL_FRAME')
                cmds.delete(cmds.pointConstraint('ORIGINAL_FRAME',prggrp,mo=0))
                #creaet blendshape
                allorg=[]
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    #org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    #fs=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_BLENDSHAPE_MESHES'):
                    cmds.delete('GRP_FCIAL_BLENDSHAPE_MESHES')
                prggrp=cmds.group(allorg,n='GRP_FCIAL_BLENDSHAPE_MESHES')
                rp=cmds.xform(prggrp,q=1,ws=1,rp=1)
                cmds.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                cmds.parent(prggrp,'BLENDSHAPE_FRAME')
                cmds.delete(cmds.pointConstraint('BLENDSHAPE_FRAME',prggrp,mo=0))
                #creaet facial skin
                allorg=[]
                for mesh in allmeshes:
                    #mesh=allmeshes[0]
                    #org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'ORIGINAL_'))
                    #org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'BLENDSHAPE_'))
                    org=cmds.duplicate(mesh,n=mesh.replace(mshstr,mshstr+'FACIALSKIN_'))
                    allorg.append(org[0])
                if cmds.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
                    cmds.delete('GRP_FCIAL_FACIALSKIN_MESHES')
                prggrp=cmds.group(allorg,n='GRP_FCIAL_FACIALSKIN_MESHES')
                rp=cmds.xform(prggrp,q=1,ws=1,rp=1)
                cmds.xform(prggrp,ws=1,rp=[0,rp[1],rp[2]],sp=[0,rp[1],rp[2]])
                cmds.parent(prggrp,'FACIALSKIN_FRAME')
                cmds.delete(cmds.pointConstraint('FACIALSKIN_FRAME',prggrp,mo=0))
                bs=cmds.blendShape('GRP_FCIAL_BLENDSHAPE_MESHES','GRP_FCIAL_FACIALSKIN_MESHES',tc=1,foc=1,n='BS_FACIAL_BLENDSHAPE_OUTPUT')
                cmds.setAttr(bs[0]+'.GRP_FCIAL_BLENDSHAPE_MESHES',1)
                bs=cmds.blendShape('GRP_FCIAL_FACIALSKIN_MESHES','GRP_FCIAL_MESHES',tc=1,foc=1,n='BS_FACIAL_SKIN_OUTPUT')
                cmds.setAttr(bs[0]+'.GRP_FCIAL_FACIALSKIN_MESHES',1)
                cmds.setAttr('FACIAL_RIG_MESHES_FRAME.MESHES_WERE_ALREAD_CREATED',1)
                rp=cmds.xform('GRP_FCIAL_FACIALSKIN_MESHES',q=1,ws=1,rp=1)
                tx=cmds.getAttr('FACIAL_RIG_MESHES_FRAME.tx')
                cmds.setAttr('FACIAL_RIG_MESHES_FRAME.tx',tx-rp[0])
                zjnt=cmds.createNode('joint',n='FACIAL_ZERO_JOINT',p='GRP_FCIAL_FACIALSKIN_MESHES')
                cmds.setAttr(zjnt+'.inheritsTransform',0)
                cmds.parent(zjnt,'FACIALSKIN_FRAME')
                cmds.delete(cmds.pointConstraint('GRP_FCIAL_FACIALSKIN_MESHES',zjnt,mo=0))
                cmds.setAttr(zjnt+'.v',0)
                edo_setLockTransform([zjnt],1)
                skmeshes=cmds.listRelatives('GRP_FCIAL_FACIALSKIN_MESHES',c=1,pa=1)
                if skmeshes:
                    for skmesh in skmeshes:
                        #skmesh=skmeshes[0]
                        try:
                            sk=cmds.skinCluster(zjnt,skmesh,rfs=0,tsb=1,mi=10)
                            cmds.setAttr(sk[0]+'.skinningMethod',1)
                        except:
                            print 'there is something wrong with the  ...  '+ skmesh
                            edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME'],1)


def edo_setLockTransform(list,v):
    for l in list:
        #l='MSH_tongue_'
        cmds.setAttr(l+'.tx',e=1,l=v)
        cmds.setAttr(l+'.ty',e=1,l=v)
        cmds.setAttr(l+'.tz',e=1,l=v)
        cmds.setAttr(l+'.rx',e=1,l=v)
        cmds.setAttr(l+'.ry',e=1,l=v)
        cmds.setAttr(l+'.rz',e=1,l=v)
        cmds.setAttr(l+'.sx',e=1,l=v)
        cmds.setAttr(l+'.sy',e=1,l=v)
        cmds.setAttr(l+'.sz',e=1,l=v)
    
def edo_autoLocationEyeballsCenter():
    sels=cmds.ls(sl=1)
    if not sels:
        print 'you must select the eyeballs first!'
        return False
    template='GRP_EYEBALLS_TEMPLATE'
    mel.eval('newCluster " -envelope 1";')
    clus=cmds.ls(sl=1)[0]
    piv=cmds.xform(clus,q=1,ws=1,rp=1)
    cmds.xform(template,ws=1,t=piv)
    cmds.delete(clus)
    sel=sels[0]
    cmds.select(sel)
    mel.eval('newCluster " -envelope 1";')
    clus=cmds.ls(sl=1)[0]
    piv=cmds.xform(clus,q=1,ws=1,rp=1)
    cmds.delete(clus)
    cmds.xform('Lf_eyeballs_joint0',ws=1,t=piv)
    cmds.xform('Rt_eyeballs_joint0',ws=1,t=[piv[0]*-1,piv[1],piv[2]])

def edo_mirrorEyeballsSkeleton():
    t1=cmds.xform('Lf_eyeballs_joint0',q=1,ws=1,t=1)
    t2=cmds.xform('Lf_eyeballs_joint1',q=1,ws=1,t=1)
    t3=cmds.xform('Lf_eyeballs_highlight_joint1',q=1,os=1,t=1)
    cmds.xform('Rt_eyeballs_joint0',ws=1,t=[t1[0]*-1,t1[1],t1[2]])
    cmds.xform('Rt_eyeballs_joint1',ws=1,t=[t2[0]*-1,t2[1],t2[2]])
    cmds.xform('Rt_eyeballs_highlight_joint1',os=1,t=[t3[0],t3[1],t3[2]])

    
def edo_getComponentToTextEditor(texteditor):
    #texteditor='lfeyelids_loop_line'
    sels=cmds.ls(orderedSelection=1,fl=1)
    if sels:
        list=''
        for sel in sels:
            list=list+sel+','
        list=list[:len(list)-1]
        cmds.textField(texteditor,e=1,text=list)
    
def edo_createEyslids_skeleton():
    lfedges=cmds.textField('lfeyelids_loop_line',q=1,tx=1)
    lfedgelist=lfedges.split(',')
    rtedges=cmds.textField('rteyelids_loop_line',q=1,tx=1)
    rtedgelist=rtedges.split(',')
    lfeyelidsjnt=edo_createJointRingFromEdge(lfedgelist[0],'Lf_','GRP_EYEBALLS_TEMPLATE')
    rteyelidsjnt=edo_createJointRingFromEdge(rtedgelist[0],'Rt_','GRP_EYEBALLS_TEMPLATE')
    if cmds.objExists('eyelids_influence'):
        cmds.delete('eyelids_influence')
    cmds.sets(lfeyelidsjnt+rteyelidsjnt,n='eyelids_influence')
    

def edo_createJointRingFromEdge(edge,prefix,parentobj):
    jnts=[]
    cmds.select(edge,r=1)
    cmds.SelectEdgeLoopSp()
    curve=cmds.polyToCurve(form=2,degree=1,n=prefix+'eyelids_ring_curve')
    cmds.parent(curve[0],parentobj)
    cmds.delete(curve[1])
    spans=cmds.getAttr(curve[0]+'.spans')
    degree=cmds.getAttr(curve[0]+'.degree')
    cvnum=spans+degree
    for i in range(0,cvnum-1):
        #i=0
        jnt=cmds.createNode('joint',n=prefix+'eyelids_jnt'+str(i),p=curve[0])
        cmds.xform(jnt,ws=1,t=cmds.xform(curve[0]+'.cv['+str(i)+']',q=1,ws=1,t=1))
        jnts.append(jnt)
    return jnts

def edo_buildClEyelids_skeleton_drivenMesh(edge,prefix,parentobj):
    #edge=Lfedge
    #prefix='Lfeyelids_'
    #parentobj='FACIALSKIN_FRAME'
    cmds.select(edge,r=1)
    cmds.SelectEdgeLoopSp()
    curve=cmds.polyToCurve(form=2,degree=1,n=prefix+'_skeleton_drivenMesh_curve')
    cmds.delete(curve[1])
    dupcurve=cmds.duplicate(curve[0],n=curve[0]+'_OFFSET')
    cmds.setAttr(dupcurve[0]+'.tz',0.1)
    lofts=cmds.loft(curve[0],dupcurve[0],ch=1,u=1,c=0,ar=1,d=3,ss=1,rn=0,po=1,rsn=1,n=prefix+'_skeleton_dirvenMesh_')
    tess=edo_findNodeFromHis(lofts[0],'nurbsTessellate')
    cmds.setAttr(tess+'.uType',3)
    cmds.setAttr(tess+'.uNumber',1)
    cmds.setAttr(tess+'.vType',3)
    cmds.setAttr(tess+'.vNumber',1)
    cmds.setAttr(tess+'.polygonType',1)
    cmds.setAttr(tess+'.format',2)
    cmds.select(lofts[0],r=1)
    cmds.DeleteHistory()
    cmds.CenterPivot()
    cmds.parent(lofts[0],parentobj)
    rp=cmds.xform(parentobj,q=1,ws=1,rp=1)
    cmds.xform(lofts[0],ws=1,rp=rp,sp=rp)
    cmds.delete(curve[0],dupcurve[0])
    return lofts[0]

def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node=his
    return node

def edo_buildClFacialRigHierarchyNode():
    if not cmds.objExists('GRP_CL_FACIALRIG_DEFORMER'):
        cmds.createNode('transform',n='GRP_CL_FACIALRIG_DEFORMER')
    if not cmds.objExists('GRP_CL_FACIALRIG_FOLLOWHEAD_NODE'):
        cmds.createNode('transform',n='GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    if not cmds.objExists('GRP_CL_ALL_FACIALRIG_JOINTS'):
        cmds.createNode('transform',n='GRP_CL_ALL_FACIALRIG_JOINTS',p='GRP_CL_FACIALRIG_DEFORMER')
    if not cmds.objExists('GRP_CL_FACIALRIG_FOLLOWBODY_NODE'):
        cmds.createNode('transform',n='GRP_CL_FACIALRIG_FOLLOWBODY_NODE')

def edo_createEyeballsRig(mshstr):
    edo_buildClFacialRigHierarchyNode()
    if not cmds.objExists('GRP_EYEBALLS_TEMPLATE'):
        return False
    #createEyeballsRig
    cmds.joint('Lf_eyeballs_joint0',e=1,oj='xyz',sao='yup',zso=1)
    cmds.joint('Rt_eyeballs_joint0',e=1,oj='xyz',sao='yup',zso=1)
    #lf high light driven joint
    cmds.createNode('joint',n='Lf_eyeballs_highlight_DIV_joint0',p='Lf_eyeballs_joint0')
    cmds.xform('Lf_eyeballs_highlight_DIV_joint0',os=1,t=[0,0,0])
    #lf high light joint
    cmds.createNode('joint',n='Lf_eyeballs_highlight_joint0',p='Lf_eyeballs_highlight_DIV_joint0')
    cmds.xform('Lf_eyeballs_highlight_joint0',os=1,t=[0,0,0])
    cmds.parent('Lf_eyeballs_highlight_joint1','Lf_eyeballs_highlight_joint0')
    #rt high light driven joint
    cmds.createNode('joint',n='Rt_eyeballs_highlight_DIV_joint0',p='Rt_eyeballs_joint0')
    cmds.xform('Rt_eyeballs_highlight_DIV_joint0',os=1,t=[0,0,0])
    #rt high light joint
    cmds.createNode('joint',n='Rt_eyeballs_highlight_joint0',p='Rt_eyeballs_highlight_DIV_joint0')
    cmds.xform('Rt_eyeballs_highlight_joint0',os=1,t=[0,0,0])
    cmds.parent('Rt_eyeballs_highlight_joint1','Rt_eyeballs_highlight_joint0')
    #create eyeballs constraint
    uploc=cmds.spaceLocator(n='Loc_eyeballs_upVector',p=cmds.xform('GRP_EYEBALLS_TEMPLATE',q=1,ws=1,t=1))
    cmds.parent(uploc,'GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    cmds.aimConstraint('c_Lf_eye_M','Lf_eyeballs_joint0',mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='objectrotation',worldUpVector=[0,1,0],worldUpObject=uploc[0])
    cmds.aimConstraint('c_Rt_eye_M','Rt_eyeballs_joint0',mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='objectrotation',worldUpVector=[0,1,0],worldUpObject=uploc[0])
    #set parent
    cmds.parent('EYE_RIG','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    cmds.parent('Lf_eyeballs_joint0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    cmds.parent('Rt_eyeballs_joint0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    #set head follow
    bodyloc=cmds.spaceLocator(n='Loc_body_constraint',p=cmds.xform('GRP_EYEBALLS_TEMPLATE',q=1,ws=1,t=1))
    cmds.parent(bodyloc,'GRP_CL_FACIALRIG_FOLLOWBODY_NODE')
    cmds.parentConstraint(bodyloc[0],'EYE_RIG',mo=1)
    cmds.setKeyframe('EYE_RIG.tx')
    cmds.setKeyframe('EYE_RIG.ty')
    cmds.setKeyframe('EYE_RIG.tz')
    cmds.setKeyframe('EYE_RIG.rx')
    cmds.setKeyframe('EYE_RIG.ry')
    cmds.setKeyframe('EYE_RIG.rz')
    revers=cmds.createNode('reverse')
    bl=cmds.listConnections('EYE_RIG.tx',s=1,d=0)
    cmds.connectAttr('c_eye_M.follow',revers+'.inputX',f=1)
    cmds.connectAttr(revers+'.outputX',bl[0]+'.weight',f=1)
    cmds.delete('EYE_RIGShape')
    edo_setLockTransform(['c_eye_M'],0)
    #create high light rig
    cmds.connectAttr('MD_Lf_eyeballs_highlight.outputX','Lf_eyeballs_highlight_DIV_joint0.ry',f=1)
    cmds.connectAttr('MD_Lf_eyeballs_highlight.outputY','Lf_eyeballs_highlight_DIV_joint0.rz',f=1)
    cmds.connectAttr('MD_Rt_eyeballs_highlight.outputX','Rt_eyeballs_highlight_DIV_joint0.ry',f=1)
    cmds.connectAttr('MD_Rt_eyeballs_highlight.outputY','Rt_eyeballs_highlight_DIV_joint0.rz',f=1)
    ######c_Lf_spec_tempMod_M.tx  Lf_eyeballs_highlight_DIV_joint0
    ######c_Rt_spec_tempMod_M.tx  Rt_eyeballs_highlight_DIV_joint0
    #======================================================================================
    #createEyelidsRig
    #lf eyelids
    if cmds.objExists('Lf_eyelids_ring_curve'):
        jnts=cmds.listRelatives('Lf_eyelids_ring_curve',c=1,type='joint',pa=1)
        if jnts:
            cjnt=cmds.createNode('joint',n='Lf_eyelids_all_jnt0',p='Lf_eyeballs_highlight_joint0')
            cmds.xform('Lf_eyelids_all_jnt0',os=1,t=[0,0,0])
            cmds.parent('Lf_eyelids_all_jnt0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
            for jnt in jnts:
                #jnt=jnts[0]
                djnt=cmds.createNode('joint',n=jnt.replace('jnt','DIV_jnt'),p='Lf_eyelids_all_jnt0')
                rjnt=cmds.createNode('joint',n=jnt.replace('jnt','rotate_jnt'),p=djnt)
                cmds.parent(jnt,rjnt)
    #Rt eyelids
    if cmds.objExists('Rt_eyelids_ring_curve'):
        jnts=cmds.listRelatives('Rt_eyelids_ring_curve',c=1,type='joint',pa=1)
        if jnts:
            cjnt=cmds.createNode('joint',n='Rt_eyelids_all_jnt0',p='Rt_eyeballs_highlight_joint0')
            cmds.xform('Rt_eyelids_all_jnt0',os=1,t=[0,0,0])
            cmds.parent('Rt_eyelids_all_jnt0','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
            for jnt in jnts:
                #jnt=jnts[0]
                djnt=cmds.createNode('joint',n=jnt.replace('jnt','DIV_jnt'),p='Rt_eyelids_all_jnt0')
                rjnt=cmds.createNode('joint',n=jnt.replace('jnt','rotate_jnt'),p=djnt)
                cmds.parent(jnt,rjnt)
    if cmds.objExists('GRP_FCIAL_FACIALSKIN_MESHES'):
        edo_setLockTransform(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],1)
        cmds.parent(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],'GRP_FCIAL_FACIALSKIN_MESHES')
        edo_setLockTransform(['Lf_eyelids_all_jnt0','Rt_eyelids_all_jnt0'],0)
    #add skin
    Lfedges=cmds.textField('lfeyelids_loop_line',q=1,tx=1)
    Rtedges=cmds.textField('rteyelids_loop_line',q=1,tx=1)
    edges=Lfedges+','+Rtedges
    if edges:
        edges=edges.split(',')
        if edges:
            mesh=edges[0].split('.')[0].replace(mshstr,mshstr+'FACIALSKIN_')
            if not cmds.objExists(mesh):
                print 'there is no mesh that name is '+mesh+' . So the program cound not add skin to it.'
                return False
            sks=edo_findNodeFromHistory(mesh,'skinCluster')
            if sks:
                sk=sks[0]
                #jnts=cmds.ls(sl=1)
                if not cmds.objExists('eyelids_influence'):
                    print 'there is no set that name is eyelids_influence . So the program cound not add skin to it.'
                    return False
                jnts=cmds.sets('eyelids_influence',q=1)
                cmds.skinCluster(sk,e=1,ai=jnts,lw=1,wt=0)
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
                    cmds.select(lfedges[i],r=1)
                    cmds.SelectEdgeLoopSp()
                    cmds.ConvertSelectionToVertices()
                    alleyelids_vertex=cmds.ls(sl=1,fl=1)
                    #compute weight
                    #################
                    for v in alleyelids_vertex:
                        #v=alleyelids_vertex[5]
                        skv=v.replace(mshstr,mshstr+'FACIALSKIN_')
                        if cmds.objExists(skv):
                            #find closest skeleton
                            vp=cmds.xform(skv,q=1,ws=1,t=1)
                            mixdis=10000000.0
                            cjnt=''
                            for jnt in jnts:
                                #jnt=jnts[0]
                                jp=cmds.xform(jnt,q=1,ws=1,t=1)
                                vecter=om.MVector((vp[0]-jp[0]),(vp[1]-jp[1]),(vp[2]-jp[2]))
                                dis=vecter.length()
                                if dis<mixdis:
                                    mixdis=dis
                                    cjnt=jnt
                            vtx_cjnt_w.append([skv,cjnt,w])
                            print 'vetex: '+skv+'  ......  closestJoint: '+cjnt+'  ......  weight: '+str(w)
                            cmds.skinPercent(sk,skv,tv=(cjnt,w))
                #Right eyelids
                rtedges=Rtedges.split(',')
                count=len(rtedges)
                addw=1.0/(count-1)
                vtx_cjnt_w=[]
                for i in range(0,count):
                    #i=0
                    w=(count-i-1)*addw
                    print w
                    cmds.select(rtedges[i],r=1)
                    cmds.SelectEdgeLoopSp()
                    cmds.ConvertSelectionToVertices()
                    alleyelids_vertex=cmds.ls(sl=1,fl=1)
                    #compute weight
                    #################
                    for v in alleyelids_vertex:
                        #v=alleyelids_vertex[5]
                        skv=v.replace(mshstr,mshstr+'FACIALSKIN_')
                        if cmds.objExists(skv):
                            #find closest skeleton
                            vp=cmds.xform(skv,q=1,ws=1,t=1)
                            mixdis=10000000.0
                            cjnt=''
                            for jnt in jnts:
                                #jnt=jnts[0]
                                jp=cmds.xform(jnt,q=1,ws=1,t=1)
                                vecter=om.MVector((vp[0]-jp[0]),(vp[1]-jp[1]),(vp[2]-jp[2]))
                                dis=vecter.length()
                                if dis<mixdis:
                                    mixdis=dis
                                    cjnt=jnt
                            vtx_cjnt_w.append([skv,cjnt,w])
                            print 'vetex: '+skv+'  ......  closestJoint: '+cjnt+'  ......  weight: '+str(w)
                            cmds.skinPercent(sk,skv,tv=(cjnt,w))
                #add eyelids skeleton dirven mesh
                Lfedge=Lfedges.split(',')[0].replace(mshstr,mshstr+'FACIALSKIN_')
                Rtedge=Rtedges.split(',')[0].replace(mshstr,mshstr+'FACIALSKIN_')
                lfmesh=edo_buildClEyelids_skeleton_drivenMesh(Lfedge,'Lfeyelids','FACIALSKIN_FRAME')
                rtmesh=edo_buildClEyelids_skeleton_drivenMesh(Rtedge,'Rteyelids','FACIALSKIN_FRAME')
                lfmeshget=cmds.duplicate(lfmesh,n=lfmesh.replace('Lfeyelids','Lfeyelids_getbs'))[0]
                rtmeshget=cmds.duplicate(rtmesh,n=rtmesh.replace('Rteyelids','Rteyelids_getbs'))[0]
                cmds.setAttr(lfmeshget+'.sx',-1)
                cmds.setAttr(lfmeshget+'.v',0)
                cmds.setAttr(rtmeshget+'.sx',-1)
                cmds.setAttr(rtmeshget+'.v',0)
                wrapcmd='CreateWrap;'
                cmds.select(lfmeshget,r=1)
                cmds.select(rtmesh,add=1)
                mel.eval(wrapcmd)
                cmds.select(rtmeshget,r=1)
                cmds.select(lfmesh,add=1)
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
                if cmds.objExists('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE'):
                    cmds.delete('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                grp=cmds.group(fos,n='GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE')
                cmds.parent(grp,'FACIALSKIN_FRAME')
                cmds.setAttr('GRP_CL_FACIAL_ALLEYELIDS_CLOSEST_FOLLICLE.v',0)
                edo_setLockTransform(['FACIAL_RIG_MESHES_FRAME','FACIALSKIN_FRAME'],1)
    cmds.delete('GRP_EYEBALLS_TEMPLATE')
    
def edo_finishEyeRig():
    Lfedges=cmds.textField('lfeyelids_loop_line',q=1,tx=1)
    Rtedges=cmds.textField('rteyelids_loop_line',q=1,tx=1)
    if Lfedges and Rtedges:
        print 'finish eye rig!'
        edo_createEyslids_skeleton()
        edo_createEyeballsRig('msh_')
    else:
        cmds.confirmDialog( title='can not find the edges of eyelids', message='can not find the edges of eyelids,you must appoint the edges of eyelids to the textline editor', button=['ok,i got it'], defaultButton='Yes', cancelButton='No', dismissString='No')
                
def edo_finishTongueRig():
    edo_buildClFacialRigHierarchyNode()
    if not cmds.objExists('GRP_TONGUE_TEMPLATE'):
        return False
    ctrls=cmds.ls('c_tongue_joint*')
    for ctrl in ctrls:
        #ctrl=ctrls[0]
        tp=cmds.listRelatives(ctrl,p=1,pa=1)
        if tp:
            rp=cmds.listRelatives(tp[0],p=1,pa=1)
            if rp:
                if 'move' in rp[0]:
                   cmds.setAttr(rp[0]+'.tx',cmds.getAttr(ctrl+'.tx'))
                   cmds.setAttr(rp[0]+'.ty',cmds.getAttr(ctrl+'.ty'))
                   cmds.setAttr(rp[0]+'.tz',cmds.getAttr(ctrl+'.tz'))
                   cmds.setAttr(rp[0]+'.rx',cmds.getAttr(ctrl+'.rx'))
                   cmds.setAttr(rp[0]+'.ry',cmds.getAttr(ctrl+'.ry'))
                   cmds.setAttr(rp[0]+'.rz',cmds.getAttr(ctrl+'.rz'))
                   #setZero
                   cmds.setAttr(ctrl+'.tx',0)
                   cmds.setAttr(ctrl+'.ty',0)
                   cmds.setAttr(ctrl+'.tz',0)
                   cmds.setAttr(ctrl+'.rx',0)
                   cmds.setAttr(ctrl+'.ry',0)
                   cmds.setAttr(ctrl+'.rz',0)
    if cmds.objExists('tongue_influence'):
        infs=cmds.sets('tongue_influence',q=1)
        meshes=lfedges=cmds.textField('get_tonguemeshes_line',q=1,tx=1)
        meshs=meshes.split(',')
        if meshs:
            for mesh in meshs:    
                #mesh=meshs[0]
                cmds.skinCluster(infs,mesh,rfs=0,tsb=1,mi=len(infs))
                if cmds.objExists('tongue_skinMesh'):
                    cmds.copySkinWeights('tongue_skinMesh',mesh,noMirror=1,surfaceAssociation='closestPoint',influenceAssociation='closestJoint')
    #connect to tongue crtl
    if cmds.objExists('GRP_PANNEL_TEMPLATE'):
        cmds.connectAttr('c_tongue_CTRL.rotateWeight','Tongue_M.rotateWeight',f=1)
        cmds.connectAttr('c_tongue_CTRL.drivenJoint','Tongue_M.drivenJoint',f=1)
        cmds.connectAttr('c_tongue_CTRL.second_vis','Tongue_M.vis_second',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_tx','Tongue_M.tx',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_ty','Tongue_M.ty',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_stretch','Tongue_M.tz',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_rx','Tongue_M.rx',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_ry','Tongue_M.ry',f=1)
        cmds.connectAttr('c_tongue_CTRL.output_rz','Tongue_M.rz',f=1)
        cmds.setAttr('Tongue_MShape.v',0)
    cmds.parent('GRP_tongue_Rig_all','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    cmds.delete('GRP_TONGUE_TEMPLATE','GRP_Tongue_M_moveShape')


def edo_createFollicleToMeshByClosestObj(mesh,obj,addAimConstraint=0):
    #mesh=lfmesh
    #obj=jnt
    #addAimConstraint=1
    cn=cmds.createNode('closestPointOnMesh',n='CL_EYELIDS_CLOSEST_POINT_ON_MESH')
    cmds.connectAttr(mesh+'.outMesh',cn+'.inMesh',f=1)
    rp=cmds.xform(obj,q=1,ws=1,rp=1)
    cmds.setAttr(cn+'.inPositionX',rp[0])
    cmds.setAttr(cn+'.inPositionY',rp[1])
    cmds.setAttr(cn+'.inPositionZ',rp[2])
    #createFollicle
    fot=cmds.createNode('transform',n=obj+'_closestFollicle')
    fo=cmds.createNode('follicle',n=obj+'_closestFollicleShape',p=fot)
    cmds.connectAttr(fo+'.outTranslateX',fot+'.translateX',f=1)
    cmds.connectAttr(fo+'.outTranslateY',fot+'.translateY',f=1)
    cmds.connectAttr(fo+'.outTranslateZ',fot+'.translateZ',f=1)
    cmds.connectAttr(fo+'.outRotateX',fot+'.rotateX',f=1)
    cmds.connectAttr(fo+'.outRotateY',fot+'.rotateY',f=1)
    cmds.connectAttr(fo+'.outRotateZ',fot+'.rotateZ',f=1)
    cmds.connectAttr(mesh+'.outMesh',fo+'.inputMesh',f=1)
    cmds.connectAttr(mesh+'.worldMatrix',fo+'.inputWorldMatrix',f=1)
    cmds.setAttr(fo+'.parameterU',cmds.getAttr(cn+'.parameterU'))
    cmds.setAttr(fo+'.parameterV',cmds.getAttr(cn+'.parameterV'))
    cmds.delete(cn)
    if addAimConstraint==1:
        ps=cmds.listRelatives(obj,p=1,pa=1)
        if ps:
            ps=cmds.listRelatives(ps[0],p=1,pa=1)
            if ps:
                cmds.aimConstraint(fot,ps[0],mo=1,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='scene')
    return fot
    
def edo_findNodeFromHistory(node,type):
    #node=mesh
    find=[]
    his=cmds.listHistory(node)
    for h in his:
        #h=his[0]
        if cmds.nodeType(h)==type:
            find.append(h)
    return find
    

def edo_finishJawRig():
    edo_buildClFacialRigHierarchyNode()
    if not cmds.objExists('GRP_JAW_TEMPLATE') and not cmds.objExists('GRP_PANNEL_TEMPLATE'):
        return False
    #lower connect 
    cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_up','low_jaw_joint0.up_driven',f=1)
    cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_dn','low_jaw_joint0.dn_driven',f=1)
    cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_rt','low_jaw_joint0.lf_driven',f=1)
    cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_lf','low_jaw_joint0.rt_driven',f=1)
    #uper connect
    cmds.connectAttr('c_jaw_up_FRAME.fourAxis_up','up_jaw_joint0.up_driven',f=1)
    cmds.connectAttr('c_jaw_up_FRAME.fourAxis_dn','up_jaw_joint0.dn_driven',f=1)
    cmds.connectAttr('c_jaw_up_FRAME.fourAxis_rt','up_jaw_joint0.lf_driven',f=1)
    cmds.connectAttr('c_jaw_up_FRAME.fourAxis_lf','up_jaw_joint0.rt_driven',f=1)
    #create Jaw joint
    jnt=cmds.createNode('joint',n='JAW_ALL_JNT',p='GRP_JAW_TEMPLATE')
    cmds.xform('JAW_ALL_JNT',os=1,t=[0,0,0])
    cmds.parent('JAW_ALL_JNT','GRP_CL_FACIALRIG_FOLLOWHEAD_NODE')
    cmds.parent('low_jaw_inverse_joint0','JAW_ALL_JNT')
    cmds.parent('up_jaw_inverse_joint','JAW_ALL_JNT')
    cmds.delete('GRP_JAW_TEMPLATE')
    if cmds.objExists('GRP_tongueRig'):
        #cmds.parentConstraint('low_jaw_joint0','GRP_tongueRig',mo=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_up','c_tongue_joint1.up_driven',f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_dn','c_tongue_joint1.dn_driven',f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_rt','c_tongue_joint1.lf_driven',f=1)
        cmds.connectAttr('c_jaw_dn_FRAME.fourAxis_lf','c_tongue_joint1.rt_driven',f=1)

def edo_cl_mirrorFacialLfEyelidsDrivenMeshRoRightAndAutoConnections():
    rtbsmaker='Rteyelids_getbs_skeleton_dirvenMesh_'
    if not cmds.objExists(rtbsmaker):
        print 'error ! there is no object what name is '+rtbsmaker
        return False
    rteyelidsDrivenMesh='Rteyelids_skeleton_dirvenMesh_'
    if not cmds.objExists(rteyelidsDrivenMesh):
        print 'error ! there is no object what name is '+rteyelidsDrivenMesh
        return False
    lfctrl='c_Lf_up_eyelids_CTRL'
    if not cmds.objExists(lfctrl):
        print 'error ! there is no object what name is '+lfctrl
        return False
    rtctrl='c_Rt_up_eyelids_CTRL'
    if not cmds.objExists(rtctrl):
        print 'error ! there is no object what name is '+rtctrl
        return False
    lfdnctrl='c_Lf_dn_eyelids_CTRL'
    if not cmds.objExists(lfctrl):
        print 'error ! there is no object what name is '+lfdnctrl
        return False
    rtdnctrl='c_Rt_dn_eyelids_CTRL'
    if not cmds.objExists(rtctrl):
        print 'error ! there is no object what name is '+rtdnctrl
        return False
    print 'mirror eyelids start...'
    frames=['c_Lf_up_eyelids_CTRL_up','c_Lf_up_eyelids_CTRL_rtup','c_Lf_up_eyelids_CTRL_lfup','c_Lf_up_eyelids_CTRL_dn','c_Lf_up_eyelids_CTRL_rtdn','c_Lf_up_eyelids_CTRL_lfdn','c_Lf_up_eyelids_CTRL_lf','c_Lf_up_eyelids_CTRL_rt']
    for frame in frames:
        #frame=frames[0]
        if cmds.objExists(frame):
            if 'RL_up' == frame[-5:]:
                print 'make up blendshape'
                cmds.setAttr(lfctrl+'.ty',1)
                cmds.setAttr(lfctrl+'.tx',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.ty',0)
            if 'RL_dn' == frame[-5:]:
                print 'make dn blendshape'
                cmds.setAttr(lfctrl+'.ty',-1)
                cmds.setAttr(lfctrl+'.tx',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.ty',0)
            if 'RL_lf' == frame[-5:]:
                print 'make lf blendshape'
                cmds.setAttr(lfctrl+'.tx',-1)
                cmds.setAttr(lfctrl+'.ty',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
            if 'RL_rt' == frame[-5:]:
                print 'make rt blendshape'
                cmds.setAttr(lfctrl+'.tx',1)
                cmds.setAttr(lfctrl+'.ty',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
            if '_lfup' == frame[-5:]:
                print 'make lfup blendshape'
                cmds.setAttr(lfctrl+'.tx',-1)
                cmds.setAttr(lfctrl+'.ty',1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
                cmds.setAttr(lfctrl+'.ty',0)
            if '_lfdn' == frame[-5:]:
                print 'make lfdn blendshape'
                cmds.setAttr(lfctrl+'.tx',-1)
                cmds.setAttr(lfctrl+'.ty',-1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
                cmds.setAttr(lfctrl+'.ty',0)
            if '_rtup' == frame[-5:]:
                print 'make rtup blendshape'
                cmds.setAttr(lfctrl+'.tx',1)
                cmds.setAttr(lfctrl+'.ty',1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
                cmds.setAttr(lfctrl+'.ty',0)
            if '_rtdn' == frame[-5:]:
                print 'make rtdn blendshape'
                cmds.setAttr(lfctrl+'.tx',1)
                cmds.setAttr(lfctrl+'.ty',-1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfctrl+'.tx',0)
                cmds.setAttr(lfctrl+'.ty',0)
    #mirror down eyelids blendshape
    frames=['c_Lf_dn_eyelids_CTRL_up','c_Lf_dn_eyelids_CTRL_rtup','c_Lf_dn_eyelids_CTRL_lfup','c_Lf_dn_eyelids_CTRL_dn','c_Lf_dn_eyelids_CTRL_rtdn','c_Lf_dn_eyelids_CTRL_lfdn','c_Lf_dn_eyelids_CTRL_lf','c_Lf_dn_eyelids_CTRL_rt']
    for frame in frames:
        #frame=frames[0]
        if cmds.objExists(frame):
            if 'RL_up' == frame[-5:]:
                print 'make up blendshape'
                cmds.setAttr(lfdnctrl+'.ty',1)
                cmds.setAttr(lfdnctrl+'.tx',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.ty',0)
            if 'RL_dn' == frame[-5:]:
                print 'make dn blendshape'
                cmds.setAttr(lfdnctrl+'.ty',-1)
                cmds.setAttr(lfdnctrl+'.tx',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.ty',0)
            if 'RL_lf' == frame[-5:]:
                print 'make lf blendshape'
                cmds.setAttr(lfdnctrl+'.tx',-1)
                cmds.setAttr(lfdnctrl+'.ty',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
            if 'RL_rt' == frame[-5:]:
                print 'make rt blendshape'
                cmds.setAttr(lfdnctrl+'.tx',1)
                cmds.setAttr(lfdnctrl+'.ty',0)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
            if '_lfup' == frame[-5:]:
                print 'make lfup blendshape'
                cmds.setAttr(lfdnctrl+'.tx',-1)
                cmds.setAttr(lfdnctrl+'.ty',1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
                cmds.setAttr(lfdnctrl+'.ty',0)
            if '_lfdn' == frame[-5:]:
                print 'make lfdn blendshape'
                cmds.setAttr(lfdnctrl+'.tx',-1)
                cmds.setAttr(lfdnctrl+'.ty',-1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
                cmds.setAttr(lfdnctrl+'.ty',0)
            if '_rtup' == frame[-5:]:
                print 'make rtup blendshape'
                cmds.setAttr(lfdnctrl+'.tx',1)
                cmds.setAttr(lfdnctrl+'.ty',1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
                cmds.setAttr(lfdnctrl+'.ty',0)
            if '_rtdn' == frame[-5:]:
                print 'make rtdn blendshape'
                cmds.setAttr(lfdnctrl+'.tx',1)
                cmds.setAttr(lfdnctrl+'.ty',-1)
                bs=cmds.duplicate(rtbsmaker)
                cmds.setAttr(bs[0]+'.v',1)
                cmds.setAttr(bs[0]+'.sx',1)
                nbs=cmds.rename(bs[0],'BS__'+rteyelidsDrivenMesh+'__xxxx')
                edo_clearFacialBlendShapeInFrame(frame.replace('Lf','Rt'))
                cmds.parent(nbs,frame.replace('Lf','Rt'))
                cmds.setAttr(lfdnctrl+'.tx',0)
                cmds.setAttr(lfdnctrl+'.ty',0)
    edo_opBlendShapeByFacialCtrl(rtctrl)
    edo_addBlendShapeAndExpressionsByFacialCtrl(rtctrl)
    edo_opBlendShapeByFacialCtrl(rtdnctrl)
    edo_addBlendShapeAndExpressionsByFacialCtrl(rtdnctrl)
    
def edo_clearFacialBlendShapeInFrame(frame):
    #frame='c_Rt_up_eyelids_CTRL_up'
    cs=cmds.listRelatives(frame,c=1,pa=1)
    for c in cs:
        #c=cs[0]
        cc=cmds.listRelatives(c,shapes=1,pa=1)
        if cc:
            cshape=cc[0]
            if cmds.nodeType(cshape)=='mesh':
                print 'clear .. '+frame+' .. '+c
                cmds.delete(c)