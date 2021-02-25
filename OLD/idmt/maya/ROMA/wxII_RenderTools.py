# -*- coding: gbk -*-
import maya.mel as mel
import maya.cmds as cmds
import os
import time
import getpass
import decimal
import re
import sys
try:
	reload(win32con)
except:
	import sys
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Maya\Python\win32com\2.4')
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Maya\Python\win32com\2.4\win32')
	sys.path.append(r'\\file-cluster\GDC\Resource\Support\Maya\Python\win32com\2.4\win32\lib')
	import win32clipboard
	import win32con

class Materials:
	def ListMats(self):
		'''list all materials except lamber1 and particleCloud1'''
		mats=cmds.ls(materials=1)
		mats.remove('lambert1')
		mats.remove('particleCloud1')
		return mats

	def CreateZdpShader(self,name):
		'''return value===>[surfaceShader,SLCode,]'''
		rv=[]
		SS=cmds.shadingNode('surfaceShader',asShader=1,n=name)
		SLCode=cmds.shadingNode('SLCodeNode',asUtility=1, n=name)

		mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/MayaManHelpers.mel"')
		mel.eval('SLCodeNodeAddColorParam("'+SLCode+'","outColor", 0, 0, 0, 0, 0, 0, 1, 1, 1);')
		mel.eval('SLCodeNodeAddColorParam("'+SLCode+'","outTransp", 0, 0, 0, 0, 0, 0, 0, 0, 0);')
		mel.eval('SLCodeNodeAddColorParam("'+SLCode+'","transparencymap", 0, 0, 0, 0, 0, 0, 0, 0, 0);')

		cmds.setAttr(SLCode+'.SLOutputs',"outTransp outColor",type="string")
		code=	'\n'.join([
						'color $outTransp = color(1,1,1);',
						'color $outColor = color(1,1,1);',
						'{',
						'	color zdepth = depth(P);',
						'	$outTransp=$transparencymap;',
						'	$outColor = zdepth * (1-$outTransp);',
						'}',
					])
		cmds.setAttr(SLCode+'.SLCode',code,type='string')
		cmds.connectAttr(SLCode+'.outTransp',SS+'.outTransparency')
		cmds.connectAttr(SLCode+'.outColor',SS+'.outColor')
		rv=[SS,SLCode]
		return rv


def zDepth():
	mel.eval('source "D:/Alias/MAYA8.5/2013/others/showEditor.mel"')
	mel.eval('source "//file-cluster/GDC/Resource/Support/AnimalLogic/mayaman2.0.7/mel/AEMayaManCustomShaderTemplate.mel"')
	mmshr = cmds.ls(type='MayaManCustomShader')
	if mmshr!=None and mmshr!=[]:
		for item in mmshr:
			mel.eval('showEditor("'+item+'")')
			mel.eval('AEMayaManCustomShaderBrowseFile("'+item+'.ShaderFile", "//file-cluster/GDC/Resource/Support/Pixar/Shader/RBW_Zdepth_Hairs.slo", "RenderMan Shader")')


	Mats=Materials()
	mats=Mats.ListMats()
	for m in mats:
		if mel.eval('attributeExists "transparency" '+m)==1:
			MaterialName=m.split(':')[-1]
			ZdpShader=Mats.CreateZdpShader(MaterialName)
			cmds.connectAttr(m+'.transparency' ,ZdpShader[1]+'.transparencymap')
			SG=cmds.listConnections(m+'.outColor',s=0,d=1,p=1,t='shadingEngine')
			if SG!=None and SG!=[]:
				cmds.connectAttr(ZdpShader[0]+'.outColor' ,SG[0],f=1)

#	mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel";wxII_zDepth();')

def wxII_PY_OpenFinishingPath():
	proj = cmds.workspace(query = True, fullName = True)
	path = re.compile(r'^.*[\\/](roma_sq_([^_\\/]+)_sc_([^_\\/]+)+)[^_\\/]*$', re.IGNORECASE).sub(r'//file-cluster/GDC/Projects/ROMA/PRJ_roma/SHOT_roma/SQ_\2/\1/scenes/finishing', proj)
	if path != proj:
		path = path.replace('/', '\\')
		aString=unicode(path)
		win32clipboard.OpenClipboard()
		win32clipboard.EmptyClipboard()
		win32clipboard.SetClipboardData(13,aString)
		win32clipboard.CloseClipboard()






def sssAim():
	light=cmds.ls('GRP_*_light_rig')
	contrl=cmds.ls('CRC_*_main_ctrl')
	if cmds.objExists('Rendercam')==0:
		cmds.confirmDialog(  message=u'文件中没有Rendercam', button=[u'确认'])
	else:
		if light==None or light==[]:
			cmds.confirmDialog(message=u'文件中没有GRP_*_light_rig这个组', button=[u'确认'])
		else:
			lightShape=cmds.ls('GRP_*_light_rig',dag=1,type='light')
			lightName=[]
			rim_light=[]
			for a in lightShape:
				lightName.append(cmds.listRelatives(a,p=1)[0])
			for a in lightName:
				if a.find('rim_light_')!=-1:
					cmds.setAttr(a+".visibility",1)
					rim_light.append(a)
					continue
				cmds.setAttr(a+".visibility",0)

			ctrlsParent=cmds.listRelatives(contrl[0],p=1,f=1)
			if ctrlsParent!=None and ctrlsParent!=[]:
				cmds.parent(contrl[0],w=1)
			tx=cmds.getAttr(contrl[0]+'.tx')
			ty=cmds.getAttr(contrl[0]+'.ty')
			tz=cmds.getAttr(contrl[0]+'.tz')
			cmds.setAttr(contrl[0]+'.translate',0,0,0,type='double3')

			pyramid=cmds.polyPyramid(w=1,ns=4,sh=1,sc=1,ax=[0,0,-1],cuv=3,ch=1)[0]
			cmds.setAttr(pyramid+'.sz',10)
			cmds.setAttr(pyramid+'.rz',90)
			cmds.makeIdentity(apply=1,t=1,r=1,s=1,n=0)
			cmds.orientConstraint( 'Rendercam', pyramid, w=1)
#			cmds.xform(pyramid[0]+'.vtx[4]',q=1,ws=1,t=1,)
#			cmds.xform(pyramid[0]+'.vtx[5]',q=1,ws=1,t=1,)
			cylinder=cmds.polyCylinder(r=1,h =2.0,sx=4,sy=1,sz=1,ax=[1,0,0],rcp=0,cuv=3,ch=1)[0]
			cmds.orientConstraint(pyramid, cylinder,w=1)
			cmds.setAttr(cylinder+'.scale',300,300,300,type='double3')
			cmds.rotate(-70,0,0,r=1,os=1,)
#			cmds.spaceLocator( p=(cmds.xform(cylinder[0]+'.vtx[1]',q=1,ws=1,t=1,)) )
			p1=cmds.xform(cylinder+'.vtx[1]',q=1,ws=1,t=1,)
			p2=cmds.xform(cylinder+'.vtx[5]',q=1,ws=1,t=1,)
			cmds.spaceLocator( p=(0,0,0))
			locator1=cmds.ls(sl=1)[0]
			cmds.setAttr(locator1+'.translate',p1[0],p1[1],p1[2],type='double3')

			cmds.spaceLocator( p=(0,0,0))
			locator2=cmds.ls(sl=1)[0]
			cmds.setAttr(locator2+'.translate',p2[0],p2[1],p2[2],type='double3')

			cmds.select(rim_light[0])
			mel.eval('source zjLocLight.mel;zjLocLight;')
			lookAt1=cmds.ls(sl=1)[0]

			cmds.select(rim_light[1])
			mel.eval('source zjLocLight.mel;zjLocLight;')
			lookAt2=cmds.ls(sl=1)[0]

			lookAtLocator1=cmds.listConnections(lookAt1)[0]
			lookAtLocator2=cmds.listConnections(lookAt2)[0]

			cmds.pointConstraint(locator1, rim_light[0],w=1,offset=[0,0,0])
			cmds.pointConstraint(locator2, rim_light[1],w=1,offset=[0,0,0])

			cmds.delete(locator1,locator2,cylinder,pyramid,)
			cmds.evalDeferred("cmds.delete(\""+lookAtLocator1+"\")")
			cmds.evalDeferred("cmds.delete(\""+lookAtLocator2+"\")")

			cmd='cmds.setAttr(" '+contrl[0]+'.translate'+' ",'+str(tx)+','+str(ty)+','+str(tz)+',type="double3")'
			cmds.evalDeferred(cmd)
			cmds.evalDeferred('cmds.parent(\"'+contrl[0]+'\",\'Rendercam\')')


def hairsmblur():
	layer=cmds.ls('*',type='renderLayer')
	layer.remove('defaultRenderLayer')

	for l in layer:
		try:
			cmds.rename(l, re.sub('beauty','mblur',l))
		except:
			pass
	mel.eval('zzjDelAllExtraChanls')

	path = cmds.getAttr('MayaManNugget.ImageOutputDir')
	newpath=re.sub('beauty','mblur',path)
	cmds.setAttr('MayaManNugget.ImageOutputDir',newpath,type='string',)

	shaders=cmds.ls(type='MayaManCustomShader')

	for s in shaders:
#		if cmds.getAttr(s+'.ShaderFile')=='RBW_Hairs':
		slo='"\\\\file-cluster\\gdc/Resource/Support/AnimalLogic/mayaman2.0.7/shaders/prman13.5/RBW_MotionVectorHairs.slo"'
		mel.eval('source "AEMayaManCustomShaderTemplate.mel"')
		mel.eval('AEMayaManCustomShaderBrowseFile '+(s+'.ShaderFile') + ' '+ slo +' \"RenderMan Shader\"'  )

	shaders=cmds.ls(type='MayaManCustomShader')
	for s in shaders:
		if cmds.getAttr(s+'.ShaderFile')=='RBW_MotionVectorHairs':
			mel.eval('MayaManUpdateCustomShader ' +s+ ' RBW_MotionVectorHairs')

def mmQuality():
	v=cmds.floatSliderButtonGrp( 'wxIImmQuality_floatSlider',q=1,v=1)
	dpShader=cmds.ls(type='displacementShader')
	if dpShader!=None and dpShader!=[]:
		for dp in dpShader:
			try:
				cmds.setAttr(dp+'.displacementBound',v)
			except:
				pass
def mmDPShaderSelect():
	dpShader=cmds.ls(type='displacementShader')
	cmds.select(dpShader)



def pegSmoothProblem():
	model=cmds.ls('peg_default:MSH_square_','peg_default:MSH_square_1_')
	if model!=None and model!=[]:
		for m in model:
			if m=='peg_default:MSH_square_1_':
				his = cmds.listHistory(m)
				smoothLeval=0
				for s in his:
					if cmds.nodeType(s)=='polySmoothFace':
						smoothLeval += cmds.getAttr(s+'.divisions')
				if smoothLeval==0:
					cmds.setAttr('peg_default:MSH_flower1_.tx',1.921847913 	)
					cmds.setAttr('peg_default:MSH_flower1_.ty',96.48958472 	)
					cmds.setAttr('peg_default:MSH_flower1_.tz',-32.68927214	)
					cmds.setAttr('peg_default:MSH_flower1_.rx',-52.5607782 	)
					cmds.setAttr('peg_default:MSH_flower1_.ry',96.05892507 	)
					cmds.setAttr('peg_default:MSH_flower1_.rz',128.4689784 	)

					cmds.setAttr('peg_default:MSH_flower2_.tx',-9.278132151	)
					cmds.setAttr('peg_default:MSH_flower2_.ty',100.4201024 	)
					cmds.setAttr('peg_default:MSH_flower2_.tz',-27.89846369	)
					cmds.setAttr('peg_default:MSH_flower2_.rx',-58.45990721	)
					cmds.setAttr('peg_default:MSH_flower2_.ry',92.27786103 	)
					cmds.setAttr('peg_default:MSH_flower2_.rz',114.1604312 	)

				elif smoothLeval==1:
					cmds.setAttr('peg_default:MSH_flower1_.tx',2.204574844 	)
					cmds.setAttr('peg_default:MSH_flower1_.ty',96.47028148 	)
					cmds.setAttr('peg_default:MSH_flower1_.tz',-32.69273261	)
					cmds.setAttr('peg_default:MSH_flower1_.rx',-83.03291306	)
					cmds.setAttr('peg_default:MSH_flower1_.ry',94.85459971 	)
					cmds.setAttr('peg_default:MSH_flower1_.rz',78.73374986 	)

					cmds.setAttr('peg_default:MSH_flower2_.tx',-9.224148286 	)
					cmds.setAttr('peg_default:MSH_flower2_.ty',100.436625   	)
					cmds.setAttr('peg_default:MSH_flower2_.tz',-27.8972039  	)
					cmds.setAttr('peg_default:MSH_flower2_.rx',-43.47029632 	)
					cmds.setAttr('peg_default:MSH_flower2_.ry',92.7886159   	)
					cmds.setAttr('peg_default:MSH_flower2_.rz',127.1289765	)

				elif smoothLeval==2:
					cmds.setAttr('peg_default:MSH_flower1_.tx',2.192577389 	)
					cmds.setAttr('peg_default:MSH_flower1_.ty',96.45906667 	)
					cmds.setAttr('peg_default:MSH_flower1_.tz',-32.69197569	)
					cmds.setAttr('peg_default:MSH_flower1_.rx',-60.35154611	)
					cmds.setAttr('peg_default:MSH_flower1_.ry',95.76140946 	)
					cmds.setAttr('peg_default:MSH_flower1_.rz',102.9432062 	)

					cmds.setAttr('peg_default:MSH_flower2_.tx',-9.209064746 	)
					cmds.setAttr('peg_default:MSH_flower2_.ty',100.4367532  	)
					cmds.setAttr('peg_default:MSH_flower2_.tz',-27.89799774 	)
					cmds.setAttr('peg_default:MSH_flower2_.rx',-52.18994466 	)
					cmds.setAttr('peg_default:MSH_flower2_.ry',92.48489335  	)
					cmds.setAttr('peg_default:MSH_flower2_.rz',117.4087405 	)
				elif smoothLeval==3:
					cmds.setAttr('peg_default:MSH_flower1_.tx',2.157663477  	)
					cmds.setAttr('peg_default:MSH_flower1_.ty',96.474152    	)
					cmds.setAttr('peg_default:MSH_flower1_.tz',-32.69179863 	)
					cmds.setAttr('peg_default:MSH_flower1_.rx',-60.2451267  	)
					cmds.setAttr('peg_default:MSH_flower1_.ry',95.78914343  	)
					cmds.setAttr('peg_default:MSH_flower1_.rz',106.252903   	)

					cmds.setAttr('peg_default:MSH_flower2_.tx',-9.204182589 	)
					cmds.setAttr('peg_default:MSH_flower2_.ty',100.4356506  	)
					cmds.setAttr('peg_default:MSH_flower2_.tz',-27.89997734 	)
					cmds.setAttr('peg_default:MSH_flower2_.rx',-57.38801588 	)
					cmds.setAttr('peg_default:MSH_flower2_.ry',92.46352986  	)
					cmds.setAttr('peg_default:MSH_flower2_.rz',111.8750039  	)

			elif m=='peg_default:MSH_square_':
				his = cmds.listHistory(m)
				smoothLeval=0
				for s in his:
					if cmds.nodeType(s)=='polySmoothFace':
						smoothLeval += cmds.getAttr(s+'.divisions')
				if smoothLeval==0:
					cmds.setAttr('peg_default:MSH_flower5_.tx',9.278117206 )
					cmds.setAttr('peg_default:MSH_flower5_.ty',100.420155  )
					cmds.setAttr('peg_default:MSH_flower5_.tz',-27.89827933)
					cmds.setAttr('peg_default:MSH_flower5_.rx',-58.45846389)
					cmds.setAttr('peg_default:MSH_flower5_.ry',-92.27776995)
					cmds.setAttr('peg_default:MSH_flower5_.rz',-114.1618691)

					cmds.setAttr('peg_default:MSH_flower6_.tx',-1.921849268)
					cmds.setAttr('peg_default:MSH_flower6_.ty',96.48959304 )
					cmds.setAttr('peg_default:MSH_flower6_.tz',-32.68924605)
					cmds.setAttr('peg_default:MSH_flower6_.rx',-52.56065928)
					cmds.setAttr('peg_default:MSH_flower6_.ry',-96.05891681)
					cmds.setAttr('peg_default:MSH_flower6_.rz',-128.4690973)

				elif smoothLeval==1:
					cmds.setAttr('peg_default:MSH_flower5_.tx',9.22203922  )
					cmds.setAttr('peg_default:MSH_flower5_.ty',100.4362022 )
					cmds.setAttr('peg_default:MSH_flower5_.tz',-27.8971627 )
					cmds.setAttr('peg_default:MSH_flower5_.rx',-44.23814466)
					cmds.setAttr('peg_default:MSH_flower5_.ry',-92.73299464)
					cmds.setAttr('peg_default:MSH_flower5_.rz',-126.2253354)

					cmds.setAttr('peg_default:MSH_flower6_.tx',-2.205121789	)
					cmds.setAttr('peg_default:MSH_flower6_.ty',96.47044138 	)
					cmds.setAttr('peg_default:MSH_flower6_.tz',-32.69234657	)
					cmds.setAttr('peg_default:MSH_flower6_.rx',-82.76706755	)
					cmds.setAttr('peg_default:MSH_flower6_.ry',-94.82882187	)
					cmds.setAttr('peg_default:MSH_flower6_.rz',-78.99226887)

				elif smoothLeval==2:
					cmds.setAttr('peg_default:MSH_flower5_.tx',9.207368737 )
					cmds.setAttr('peg_default:MSH_flower5_.ty',100.4365393 )
					cmds.setAttr('peg_default:MSH_flower5_.tz',-27.89836297)
					cmds.setAttr('peg_default:MSH_flower5_.rx',-53.94102764)
					cmds.setAttr('peg_default:MSH_flower5_.ry',-92.40966046)
					cmds.setAttr('peg_default:MSH_flower5_.rz',-115.4747729)

					cmds.setAttr('peg_default:MSH_flower6_.tx',-2.191434171	)
					cmds.setAttr('peg_default:MSH_flower6_.ty',96.4598399  	)
					cmds.setAttr('peg_default:MSH_flower6_.tz',-32.69202181	)
					cmds.setAttr('peg_default:MSH_flower6_.rx',-60.8975104 	)
					cmds.setAttr('peg_default:MSH_flower6_.ry',-95.71991089	)
					cmds.setAttr('peg_default:MSH_flower6_.rz',-102.4746489)
				elif smoothLeval==3:
					cmds.setAttr('peg_default:MSH_flower5_.tx',9.20167053  	)
					cmds.setAttr('peg_default:MSH_flower5_.ty',100.4348663 	)
					cmds.setAttr('peg_default:MSH_flower5_.tz',-27.90045139	)
					cmds.setAttr('peg_default:MSH_flower5_.rx',-59.42362289	)
					cmds.setAttr('peg_default:MSH_flower5_.ry',-92.42020076	)
					cmds.setAttr('peg_default:MSH_flower5_.rz',-109.5993911	)

					cmds.setAttr('peg_default:MSH_flower6_.tx',-2.155386198 	)
					cmds.setAttr('peg_default:MSH_flower6_.ty',96.47492466  	)
					cmds.setAttr('peg_default:MSH_flower6_.tz',-32.69174925 	)
					cmds.setAttr('peg_default:MSH_flower6_.rx',-60.07591419 	)
					cmds.setAttr('peg_default:MSH_flower6_.ry',-95.80010276 	)
					cmds.setAttr('peg_default:MSH_flower6_.rz',-106.6763751 	)

