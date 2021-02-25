# -*- coding: gbk -*-
import maya.mel	as mel
import maya.cmds as	cmds

class selectContent:
	def	assignDPMColor(self,obj,color):
		if not cmds.objExists('wxII_DPM_'+color):
			if color=='colorR':
				cmds.shadingNode('surfaceShader',asShader=1,n='wxII_DPM_colorR')
				cmds.setAttr("wxII_DPM_colorR.outColor",1,0,0,type='double3')
				cmds.setAttr("wxII_DPM_colorR.outMatteOpacity",0,0,0,type='double3')
			elif color=='colorG':
				cmds.shadingNode('surfaceShader',asShader=1,n='wxII_DPM_colorG')
				cmds.setAttr("wxII_DPM_colorG.outColor",0,1,0,type='double3')
				cmds.setAttr("wxII_DPM_colorG.outMatteOpacity",0,0,0,type='double3')
			elif color=='colorB':
				cmds.shadingNode('surfaceShader',asShader=1,n='wxII_DPM_colorB')
				cmds.setAttr("wxII_DPM_colorB.outColor",0,0,1,type='double3')
				cmds.setAttr("wxII_DPM_colorB.outMatteOpacity",0,0,0,type='double3')
			elif color=='colorA':
				cmds.shadingNode('surfaceShader',asShader=1,n='wxII_DPM_colorA')
				cmds.setAttr("wxII_DPM_colorA.outColor",0,0,0,type='double3')
				cmds.setAttr("wxII_DPM_colorA.outMatteOpacity",1,1,1,type='double3')
			elif color=='matte':
				cmds.shadingNode('lambert',asShader=1,n='wxII_DPM_matte')
				cmds.setAttr("wxII_DPM_matte.color",0,0,0,type='double3')
				cmds.setAttr("wxII_DPM_matte.matteOpacityMode",0)
		try:
			cmds.select(obj)
			if color=='colorR':
				cmds.hyperShade(assign='wxII_DPM_colorR')
			elif color=='colorG':
				cmds.hyperShade(assign='wxII_DPM_colorG')
			elif color=='colorB':
				cmds.hyperShade(assign='wxII_DPM_colorB')
			elif color=='colorA':
				cmds.hyperShade(assign='wxII_DPM_colorA')
			elif color=='matte':
				cmds.hyperShade(assign='wxII_DPM_matte')
		except:
			pass



	def assignColor(self,color):
		sl=cmds.ls(sl=1)
		pc=cmds.polyCube()
		cmds.select(cl=1)

		self.assignDPMColor(pc,color)
		if sl!=None and sl!=[]:
			cmds.select(sl)
		cmds.delete(pc)

	def getParent(self,obj):
		trans=''
		if cmds.nodeType(obj)=='transform':
			trans=obj
		if cmds.nodeType(obj)=='mesh':
			cmds.select(obj)
			trans=cmds.pickWalk(d='up')[0]
		return trans

	def selectObjCMD(self,shade,poly):
		sl=cmds.ls(sl=1)
		rv=[]
		poly=poly
		cmds.select(shade)
		cmds.hyperShade(objects='')
		slFace=cmds.ls(sl=1)
		if slFace!=None and slFace!=[]:
			for a in slFace:
				if cmds.ls(a,showType=1)[1]=='float3':
					if a.split('.')[0]==poly:
						rv.append(a)
				if cmds.ls(a,showType=1)[1]=='mesh':
					b=cmds.listRelatives(a,parent=1)[0]
					if b.split('.')[0]==poly:
						rv.append(b)
		if sl!=None and sl!=[]:
			cmds.select(sl)
			return rv

	def assignAllDPM(self,color):
		'''to use this method, you can give all object the same color'''
		sl=cmds.ls(sl=1)
		self.assignColor(color)
		outColor='wxII_DPM_'+color+'.outColor'

		for a in sl:
			shape=cmds.ls(a,dag=1,type=['mesh','nurbsSurface'],ni=1)
			if shape!=None and shape!=[]:
				shape=shape[0]
			sg=cmds.listConnections(shape,d=1,s=0,type='shadingEngine')

			for s in sg:
				sgSS=s+'.surfaceShader'
				if cmds.isConnected(outColor,sgSS)==0:
					cmds.connectAttr(outColor,sgSS,f=1)
		cmds.select(sl)

	def crossFace(self,list1,list2):
		rv=[]
		all=[]
		for l1 in list1:
			all.append(l1)
		for l2 in list2:
			all.append(l2)
		for a in all:
			if all.count(a)>1:
				rv.append(a)
		rv=list(set(rv))
		return rv

	def divideFace(self,list1,list2):
		rv=list(list1)
		for l2 in list2:
			try:
				rv.remove(l2)
			except:
				pass
		return rv

	def assignTMP(self,list):

		sd=cmds.shadingNode('blinn',asShader=1,name='zzj')
		cmds.select(list)
		cmds.hyperShade(assign=sd)
		sg=cmds.listConnections(sd,type='shadingEngine')[0]
		cmds.delete(sd)
		return sg

	def assignDPM(self,color):
		sl=tuple(cmds.ls(sl=1,fl=1))
		print color
		self.assignColor(color)
		outColor='wxII_DPM_'+color+'.outColor'
		DPMface=[]
		crossFace=[]
		poly= sl[0].split('.')[0]
		cmds.hyperShade(smn=1)
		DPMshader=cmds.ls(sl=1,type='displacementShader')
		if DPMshader!=None and DPMshader!=[]:
			for DPM in DPMshader:
				tempRV=self.selectObjCMD(DPM,poly)
				for t in tempRV:
					DPMface.append(t)
			DPMface=list(set(DPMface))
			cmds.select(DPMface)
			if len(DPMface)==1 and DPMface[0].find('.')==-1:
				tmp=cmds.polyListComponentConversion(toFace=1)
				DPMface=cmds.ls(tmp,flatten=1)
			else:
				DPMface=cmds.ls(sl=1,fl=1)
			finalDPMface=[]

			crossFace=self.crossFace(sl,DPMface)
			NoDPM=self.divideFace(sl,crossFace)
			cmds.select(crossFace)
			self.assignDPMColor(NoDPM,color)

			sg=self.assignTMP(crossFace)
			sgSS=sg+'.surfaceShader'
			if cmds.isConnected(outColor,sgSS)==0:
				cmds.connectAttr(outColor,sgSS,f=1)

			outDPM=DPMshader[0]+'.displacement'
			sgDPM=sg+'.displacementShader'
			if cmds.isConnected(outDPM,sgDPM)==0:
				cmds.connectAttr(outDPM,sgDPM,f=1)
		else:
			assign(sl,color)

		cmds.select(sl)

	def selectObj(self):
		mesh=''
		sl=cmds.ls(sl=1)
		if sl!=None and sl!=[]:
			if len(sl)!=2:
				cmds.confirmDialog(  message=u'选择物体必须为2个', button=[u'确认'])
			else:
				mat=cmds.ls(materials=1)
				if mat.count(sl[0])==0:
					cmds.confirmDialog(  message=u'第一个选中的必须是shader', button=[u'确认'])
				else:
					tmp=cmds.ls(sl[1],sl=1,dag=1,type='mesh',ni=1)
					if tmp!=None and tmp!=[] and (cmds.nodeType(sl[1])=='transform' or cmds.nodeType(sl[1])=='mesh'):
						trans=self.getParent(tmp[0])
						face=self.selectObjCMD(sl[0],trans)			####cmdLine<======
						cmds.select(face)
					else:
						cmds.confirmDialog(  message=u'第二个选中的必须是polygon物体', button=[u'确认'])
		else:
			cmds.confirmDialog(  message=u'请选择shader和polygon物体', button=[u'确认'])

def main():
	'''only for test'''
	classSC=selectContent()
	classSC.selectObj()

def FinalAssign(color):
	classSC=selectContent()
	sl=tuple(cmds.ls(sl=1))
	if cmds.nodeType(sl[0])=='transform':
		classSC.assignAllDPM(color)
	if cmds.nodeType(sl[0])=='mesh':
		classSC.assignDPM(color)
		pass

def selectFace():
	classSC=selectContent()
	classSC.selectObj()

def	assign(obj,color):
	if not cmds.objExists('idmt_IDPass_'+color):
		if color=='colorR':
			cmds.shadingNode('surfaceShader',asShader=1,n='idmt_IDPass_colorR')
			cmds.setAttr("idmt_IDPass_colorR.outColor",1,0,0,type='double3')
			cmds.setAttr("idmt_IDPass_colorR.outMatteOpacity",0,0,0,type='double3')
		elif color=='colorG':
			cmds.shadingNode('surfaceShader',asShader=1,n='idmt_IDPass_colorG')
			cmds.setAttr("idmt_IDPass_colorG.outColor",0,1,0,type='double3')
			cmds.setAttr("idmt_IDPass_colorG.outMatteOpacity",0,0,0,type='double3')
		elif color=='colorB':
			cmds.shadingNode('surfaceShader',asShader=1,n='idmt_IDPass_colorB')
			cmds.setAttr("idmt_IDPass_colorB.outColor",0,0,1,type='double3')
			cmds.setAttr("idmt_IDPass_colorB.outMatteOpacity",0,0,0,type='double3')
		elif color=='colorA':
			cmds.shadingNode('surfaceShader',asShader=1,n='idmt_IDPass_colorA')
			cmds.setAttr("idmt_IDPass_colorA.outColor",0,0,0,type='double3')
			cmds.setAttr("idmt_IDPass_colorA.outMatteOpacity",1,1,1,type='double3')
		elif color=='matte':
			cmds.shadingNode('lambert',asShader=1,n='idmt_IDPass_matte')
			cmds.setAttr("idmt_IDPass_matte.color",0,0,0,type='double3')
			cmds.setAttr("idmt_IDPass_matte.matteOpacityMode",0)
	try:
		cmds.select(obj)
		if color=='colorR':
			cmds.hyperShade(assign='idmt_IDPass_colorR')
		elif color=='colorG':
			cmds.hyperShade(assign='idmt_IDPass_colorG')
		elif color=='colorB':
			cmds.hyperShade(assign='idmt_IDPass_colorB')
		elif color=='colorA':
			cmds.hyperShade(assign='idmt_IDPass_colorA')
		elif color=='matte':
			cmds.hyperShade(assign='idmt_IDPass_matte')
	except:
		pass


