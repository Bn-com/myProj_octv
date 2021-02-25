'''
variableKinematics.py

Created by: Dmitry Kryukov
website: www.linkedin.com/pub/dmitry-kryukov/86/5b7/7ba
email: dima.krukof@gmail.com
Version 1.0: December 2013
Thanks: to Jeff Brodsky (vimeo.com/72424469) and Vladimir Zabelin (CG Event 2012)

Script Summary: For the selected curve creates a chain of bones system VariableFK or VariableIK 
Each parametric control is responsible for rotation of the bones in his area of influence.
Position control along the chain can be changed. You can also change the falloff of influence.
Variable number of bones in the chain and the number of controls.

______________________________________________
Install: 
   just drop this file into your scripts folder or one any path
   that's on a python path. then in a Python ScriptEditor Tab :

Usage:    
   import variableKinematics
   variableKinematics.build_ui()

Select Nurbs curve and press IK or FK button 
______________________________________________
Variable Kinematics is released under a BSD-style license

Copyright (c) 2013, Dmitry Kryukov.
All Rights Reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. The name of the author may not be used to endorse or promote products
   derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY WEBBER HUANG "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY
WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

______________________________________________
'''

import maya.cmds as cmds
import OpenMayaHelper
import sys
import maya.mel as mel
import maya.cmds as mc

def linstep(min, max, x):
	"""
	Returns a value from 0 to 1 that represents a parameters proportional distance between a minimum and maximum value.
	"""
	if x < min:return 0
	if x > max:return 1
	if min == max:return 0
	return (x - min) / (max - min)

def get_curve():
	lls=cmds.listRelatives(s=1,type='nurbsCurve')
	res=cmds.listRelatives(lls,p=1)
	#test to see if user has selected curve components
	if not res:
		res=cmds.listRelatives(p=1,type='nurbsCurve')	
	res=list(set(res))
	return res

def cluster_on_curve(cu):
	#find number of CVs in curve
	numCVs = cmds.getAttr('%s.controlPoints' %cu, size=1)
	res=[]
	#make CV into a cluster
	for i in range(numCVs):
		cl=cmds.cluster('%s.cv[%s]' %(cu,i),relative=False,n='vk_cluster#')[1]
		res.append(cl)
	return res

def ik_stretch(ikhnd):
	'''
	
	'''
	jts = cmds.ikHandle(ikhnd,q=True,jl=True)
	cu_s = cmds.ikHandle(ikhnd,q=True,c=True)
	cu=cmds.listRelatives(cu_s,p=1)[0]
	cmds.addAttr(ikhnd, longName='ik_stretch', k=1, defaultValue=1.0, minValue=0.0, maxValue=1.)

	dcu=cmds.duplicate(cu,n=cu+'_base_scale')[0]
	dcu_s=cmds.listRelatives(dcu,c=1)[0]
	
	cf=cmds.createNode('curveInfo')	
	dcf=cmds.createNode('curveInfo')	
	bl=cmds.createNode('blendTwoAttr')
	md=cmds.createNode('multiplyDivide')

	cmds.connectAttr (cu_s+'.worldSpace', cf+'.inputCurve')	
	cmds.connectAttr (dcu_s+'.worldSpace', dcf+'.inputCurve')
	cmds.connectAttr (dcf+'.arcLength', bl+'.input[0]')
	cmds.connectAttr (cf+'.arcLength', bl+'.input[1]')
	cmds.connectAttr (ikhnd+'.ik_stretch', bl+'.attributesBlender')
	cmds.connectAttr (bl+'.output', md+'.input1X')

	cmds.setAttr(md+'.input2X', cmds.getAttr(cf+'.arcLength'),l=1)
	cmds.setAttr(md+'.operation',2)
	cmds.setAttr(dcu+'.v',0)
	
	for j in jts:cmds.connectAttr (md+'.outputX', j+'.sx')
	
	return dcu
		
def chain(cu,num,name='joint'):
	"""
	build a simple chain of joints equal to a defined length
	"""
	cmds.select(cl=True)
	length=cmds.arclen(cu,ch=0) 	
	jts=[];jts.append(cmds.joint(n='%s\#' %name,rad=1))	
	for j in range(num):
		rd = 1 - linstep(0., num+1, j+1)
		jtmp=cmds.joint(p=(length/num*(j+1),0, 0),rad=rd, n='%s\#' %name )
		jts.append(jtmp)		
	return jts
	
def parameter_attr(jts):
	"""
	adds an attribute to the joints, taking into account the curve parameterization
	this parameters is not proportional distance between 0 and 1
	"""
	pts=[cmds.xform(j,q=True,ws=True,t=True) for j in jts]
	tmp_cu = cmds.curve(p=pts)
	tmp_s=cmds.listRelatives(tmp_cu,c=1)[0]	
	for j in jts:
		pt = cmds.xform(j,q=True,ws=True,t=True)
		param = OpenMayaHelper.getParametrCurve(tmp_s,pt)
		cmds.addAttr(j,ln="parameter", at='double', min=0, max=1)
		cmds.setAttr('%s.parameter' %j, param, keyable=False, cb=True)
	cmds.delete(tmp_cu)
		
def create_loft(jts,name='loftedSurface'):
	"""
	Create skins a surface along a series of profile curves. 
	"""
	pts=[cmds.xform(j,q=True,ws=True,t=True) for j in jts]
	cuR = cmds.curve( p=pts)
	cmds.move(0,0,.5,cuR,ls=True)
	cuL = cmds.duplicate(cuR)
	cmds.move(0,0,-.5,cuL,ls=True)
	Nurbs=cmds.loft( cuR, cuL, ch=False, rn=True, n='%s#' %name)[0]
	cmds.setAttr('%s.template' %Nurbs, 1)
	sc_cl=cmds.skinCluster(jts[0],Nurbs,mi=1,sm=1)[0]
	#delete bindpose
	bind=cmds.listConnections('%s.bindPose' %sc_cl,c=0,d=1,p=0)
	if bind:cmds.delete(bind)
	cmds.delete(cuR,cuL)
	return Nurbs

def create_follicle(Nurbs, uPos=0.0, vPos=0.0,name='follice'):
	"""
	Creates follicle (without hair system) on the surface in a certain position
	"""
	Foll = cmds.createNode('follicle', name='%s#' %name)
	cmds.connectAttr('%s.local' %Nurbs, '%s.inputSurface' %Foll)
	cmds.connectAttr('%s.worldMatrix' %Nurbs, '%s.inputWorldMatrix' %Foll)
	FollTr = cmds.listRelatives(Foll,p=1)[0]

	cmds.connectAttr('%s.outTranslate' %Foll, '%s.translate' %FollTr)
	cmds.connectAttr('%s.outRotate' %Foll, '%s.rotate' %FollTr)
	cmds.setAttr('%s.translate' %FollTr,l=1)
	cmds.setAttr('%s.rotate' %FollTr,l=1)
	cmds.setAttr('%s.parameterU' %Foll,uPos)
	cmds.setAttr('%s.parameterV' %Foll,vPos)
	return Foll

def create_control(flc,name='control'):
	"""
	The function creates a single vks control, as well as the necessary groups and attributes for further connection
	Args: 
		flc: A follicle
	Returns: 
		pctr,rctr,ctr: tuple new objects in the order of hierarchy, from top to bottom
	"""
	ctr=cmds.circle(name='%s#' %name,nr=(1,0,0),ch=0)[0]
	ctr_s=cmds.listRelatives(ctr,s=1)[0]
	cmds.setAttr("%s.overrideEnabled" %ctr_s,1)
	cmds.setAttr("%s.overrideColor" %ctr_s,14)
	
	rctr=cmds.group(name='%s_reverse_grp' %ctr)
	pctr=cmds.group(name='%s_parent_grp' %ctr)
	vPos=cmds.getAttr('%s.parameterV' %flc)
	
	flc_tr = cmds.listRelatives(flc,p=1)[0]
	cmds.pointConstraint(flc_tr,pctr,mo=0)
	cmds.orientConstraint(flc_tr,pctr,mo=1)
	mtp_r=cmds.createNode('multiplyDivide',n='multiplyReverce_%s' %ctr)
	cmds.connectAttr('%s.rotate' %ctr, '%s.input1' %mtp_r)
	cmds.connectAttr('%s.output' %mtp_r, '%s.rotate' %rctr)
	[cmds.setAttr('%s.input2%s' %(mtp_r,a),-1) for a in ('X','Y','Z')]
	
	cmds.addAttr(ctr,ln="falloff", at='double', min=0.0001, max=1, dv=0.2)
	cmds.addAttr(ctr,ln="position", at='double', min=0, max=1, dv=vPos)		
	cmds.addAttr(ctr,ln="minPos", at='double', min=0, max=1)
	cmds.addAttr(ctr,ln="maxPos", at='double', min=0, max=1)
	cmds.setAttr('%s.position' %ctr,k=True)
	cmds.setAttr('%s.falloff' %ctr,k=True)
	
	ppf = cmds.createNode('plusMinusAverage',n='PplusF_%s' %ctr)
	cmds.setAttr("%s.operation" %ppf ,1)
	cmds.connectAttr('%s.position' %ctr, '%s.input1D[0]' %ppf)
	cmds.connectAttr('%s.falloff' %ctr, '%s.input1D[1]' %ppf)
	
	pmf = cmds.createNode('plusMinusAverage',n='PminusF_%s' %ctr)
	cmds.setAttr("%s.operation" %pmf ,2)
	cmds.connectAttr('%s.position' %ctr, '%s.input1D[0]' %pmf)
	cmds.connectAttr('%s.falloff' %ctr, '%s.input1D[1]' %pmf)
	
	cmds.connectAttr('%s.output1D' %pmf, '%s.minPos' %ctr)
	cmds.connectAttr('%s.output1D' %ppf, '%s.maxPos' %ctr)
	
	cmds.connectAttr('%s.position' %ctr, '%s.parameterV' %flc) 
	return pctr,rctr,ctr

def connection(vks,jt,jgroup):
	"""
	Establishes a connection between the vks control and one of the joints in the chain
	"""
	linstepA=cmds.createNode('setRange',n='setRangeA_%s' %jt)
	cmds.setAttr('%s.minX' %linstepA, 1)
	cmds.connectAttr('%s.parameter' %jt, '%s.valueX' %linstepA)
	cmds.connectAttr('%s.position' %vks, '%s.oldMinX' %linstepA)
	cmds.connectAttr('%s.maxPos' %vks, '%s.oldMaxX' %linstepA)
	
	linstepB=cmds.createNode('setRange',n='setRangeB_%s' %jt)
	cmds.setAttr('%s.maxX' %linstepB, 1)
	cmds.connectAttr('%s.parameter' %jt, '%s.valueX' %linstepB)
	cmds.connectAttr('%s.minPos' %vks, '%s.oldMinX' %linstepB)
	cmds.connectAttr('%s.position' %vks, '%s.oldMaxX' %linstepB)
	
	cond=cmds.createNode('condition',n='condition_%s' %jt)
	cmds.setAttr('%s.operation' %cond, 2)
	cmds.connectAttr('%s.parameter' %jt, '%s.firstTerm' %cond)
	cmds.connectAttr('%s.position' %vks, '%s.secondTerm' %cond)
	cmds.connectAttr('%s.outValueX' %linstepA,'%s.colorIfTrueR' %cond)
	cmds.connectAttr('%s.outValueX' %linstepB,'%s.colorIfFalseR' %cond)
	
	mtp_r=cmds.createNode('multiplyDivide',n='multiplyRotate_%s' %jt)
	cmds.connectAttr('%s.rotate' %vks, '%s.input1' %mtp_r)
	cmds.connectAttr('%s.outColorR' %cond, '%s.input2X' %mtp_r)
	cmds.connectAttr('%s.outColorR' %cond, '%s.input2Y' %mtp_r)
	cmds.connectAttr('%s.outColorR' %cond, '%s.input2Z' %mtp_r)	
	cmds.connectAttr('%s.output' %mtp_r, '%s.rotate' %jgroup)

def cube_curve(name):
	kv=range(16)
	pv=[[-0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,0.5,-0.5],[-0.5,0.5,-0.5],
	[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5], 
	[0.5,-0.5,0.5],[-0.5,-0.5,0.5],[0.5,-0.5,0.5],[0.5,0.5,0.5], 
	[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5]]
	ctr=cmds.curve(d=1,p=pv,k=kv)
	ctr=cmds.rename(ctr,name)
	ctr_s=cmds.listRelatives(ctr,s=1)[0]
	cmds.setAttr("%s.overrideEnabled" %ctr_s,1)
	cmds.setAttr("%s.overrideColor" %ctr_s,9)
	return ctr
	
def VK_system(num_ctr=1,num_jt=10,fk=True):
	"""
	final assembly of the entire system
	"""
	lock_attr = lambda node,b:[cmds.setAttr('%s.%s%s' %(node,a,aa),l=b) for a in 'trs' for aa in 'xyz']
	fk_hide_attr = lambda node,b:[cmds.setAttr('%s.%s%s' %(node,a,aa),l=b,k=not b) for a in 'ts' for aa in 'xyz']
	ik_hide_attr = lambda node,b:[cmds.setAttr('%s.%s%s' %(node,a,aa),l=b,k=not b) for a in 'trs' for aa in 'xyz' if '%s%s' %(a,aa) != 'rx']
	
	cu=get_curve()[0]
	jts = chain(cu,num_jt,'vks_orig_joint')
	d_jts = chain(cu,num_jt,'vks_skin_joint')
	parameter_attr(jts)
	#loft,skin
	surf = create_loft(jts,'vks_lofted_mesh')
	surf_s=cmds.listRelatives(surf,c=1)[0]
	#hierarchical groups
	vks_grp=cmds.group(surf, name='VariableKinematicsSystem#')
	flc_grp=cmds.group(em=True,parent=vks_grp,name='vks_follice_grp#')
	mov_grp=cmds.group(em=True,parent=vks_grp,name='vks_move_grp#')
	ctr_grp=cmds.group(em=True,parent=mov_grp,name='vks_control_grp#')	
	lock_attr(flc_grp,1)
	lock_attr(ctr_grp,1)
	#create vks control	
	vks_ctr=[]
	for i in range(num_ctr):
		#create follice
		vPos= linstep(0., num_ctr-1, i)
		flc = create_follicle(surf_s,0.5,vPos,'vks_follice')
		flc_tr = cmds.listRelatives(flc,p=1)[0]
		cmds.parent(flc_tr,flc_grp)
		#create control
		vkss = create_control(flc,'vks_parametric')
		cmds.parent(vkss[0],ctr_grp)
		vks_ctr.append(vkss[-1])
	#ikspline
	ikhnd=cmds.ikHandle(sj=jts[0], ee=jts[-1], c=cu, ccv=False, sol='ikSplineSolver')	
	#create joint orig group
	org_grp = cmds.group(jts[0],parent=vks_grp,n='vks_orig_grp#')
	rot=cmds.xform(jts[0],q=True,ws=True,ro=True)
	cmds.xform(org_grp,ws=True,ro=(rot[0],rot[1],rot[2]),piv=(0,0,0))
	cmds.hide(flc_grp,org_grp)
	
	#building explicit control
	m_ctr=cube_curve('vks_explicit#')
	cmds.parent(m_ctr,vks_grp)
	tr=cmds.xform(jts[0],q=True,ws=True,t=True)
	cmds.xform(m_ctr,ws=True,t=tr)
	cmds.makeIdentity(m_ctr,apply=1,t=1,r=1,s=1,n=0)
	cmds.parentConstraint(m_ctr,org_grp,mo=1)
	cmds.parentConstraint(m_ctr,mov_grp,mo=1)
	cmds.scaleConstraint(m_ctr,mov_grp)
	
	if fk:#FK module
		for c in vks_ctr:
			fk_hide_attr(c,1)
			for j in jts:
				jgroup = cmds.group(j,n='%s_%s' %(j,c))
				piv=cmds.xform(j,q=True,ws=True,piv=True)
				cmds.xform(jgroup,ws=True,piv=(piv[0],piv[1],piv[2]))		
				connection(c,j,jgroup)
		
		for n,j in enumerate(jts):
			cmds.parentConstraint(j,d_jts[n])

		cmds.scaleConstraint(m_ctr,org_grp)	
		cmds.parent(d_jts[0],mov_grp)
		cmds.delete(ikhnd)
	else:#IK module
		cmds.hide(surf)
		cmds.toggle(d_jts,localAxis=True)
		jj=[j for j in jts]
		for c in vks_ctr:
			ik_hide_attr(c,1)
			for n,j in enumerate(jts):
				jgroup=cmds.group( em=True, n='%s_%s' %(j,c), parent=jj[n])
				jj[n]=jgroup
				connection(c,j,jgroup)
		
		for n in range(num_jt):
			cmds.parentConstraint(jj[n],d_jts[n])
		
		cu_sc = ik_stretch(ikhnd[0])
		
		cls_grp=cmds.group(em=True,name='vks_cluster_grp#')
		ik_cls=cluster_on_curve(cu)
		cmds.parent(ik_cls,cls_grp)
		
		cmds.parent(d_jts[0],cls_grp,cu_sc,mov_grp)
		cmds.parent(cu,ikhnd[0],vks_grp)
	
	cmds.select(cl=True)

def run_command(b):
	n_jnts = cmds.intSliderGrp( 'intJoints_ISG_UI',q=1,v=1)
	n_ctrl = cmds.intSliderGrp( 'intControl_ISG_UI',q=1,v=1)	
	VK_system(n_ctrl,n_jnts,b)
	
def vk_makeSoftJointCurve():

    num_jt = cmds.intSliderGrp( 'intJoints_ISG_UI',q=1,v=1)
    cu = get_curve()[0]
    
    jts = chain(cu,num_jt,'snake_joint')
    
    ikhnd = cmds.ikHandle(sj=jts[0],ee=jts[-1],c=cu,ccv=False,sol='ikSplineSolver')
    
    m_ctr = cube_curve("SNAKE_CTRL#")
    cmds.parent(m_ctr,jts[0],r=True)
    cmds.move(-1,0,0,m_ctr,ls=True)
    
    vks_grp=cmds.group(em=True,name='SnakeGroup#')
    jts_grp=cmds.group(em=True,name='Snake_joints_grp#')
    
    cmds.parent(jts_grp,m_ctr,vks_grp)
    cmds.parent(jts,jts_grp)
    cmds.delete(ikhnd)
    jts.reverse()
    
    
    for i,j in enumerate(jts):
        if i == len(jts)-1:
            cmds.select(m_ctr,j)
        else:
            cmds.select(jts[i+1],j)
        mel.eval('sePushPullConstraint')
        cmds.aimConstraint(upVector=(0,1,0),mo=0,aimVector=(-1,0,0))
        
    cmds.select(m_ctr)

def build_ui():	
	name_ui = 'variableKinematicsUI'
	if cmds.window (name_ui,ex=1): cmds.deleteUI(name_ui)
	mainwin=cmds.window(name_ui, title='Variable Kinematics Window',w=100,h=50)
	cmds.formLayout(numberOfDivisions=100)
	cmds.columnLayout(adjustableColumn=True)
	cmds.intSliderGrp( 'intJoints_ISG_UI', field=True, label='joints', minValue=3, maxValue=100, fieldMaxValue=1000, value=10, step=1)	
	cmds.separator()
	cmds.intSliderGrp( 'intControl_ISG_UI', field=True, label='controls', minValue=1, maxValue=25, fieldMaxValue=1000, value=2, step=1)
	cmds.separator()
	cmds.rowLayout('rl',nc=3,adjustableColumn=3)
	cmds.iconTextButton(label='FK',w=300,h=100,style='textOnly',c=lambda:run_command(1))
	cmds.iconTextButton(label='IK',h=100,style='textOnly',c=lambda:run_command(0))
	cmds.iconTextButton(label='SOFT',h=100,style='textOnly',c=lambda:vk_makeSoftJointCurve())
	cmds.intSliderGrp( 'intJoints_ISG_UI',e=1,cw3=(50,30,500), adj=3,h=35)
	cmds.intSliderGrp( 'intControl_ISG_UI',e=1,cw3=(50,30,500), adj=3,h=35)
	cmds.showWindow(mainwin)

