# -*- coding: gbk -*-
import maya.mel as mel
import maya.cmds as cmds

if __name__=='__main__':
	changeColor()

class chrLightName:
	color=['rim','extra','lgt']
	shadow=['eshd','lshd']

	R_light=['key']
	G_light=['fill','bounce']
	B_light=['rim','magic','extra']

	def allLights(self):
		rv=[]
		allLight=cmds.ls(type='light')
		for light in allLight:
			rv.append(cmds.listRelatives(light,p=1,f=1)[0])
		return rv

	def get_RGB_lights(self,RGB):
		rv=[]
		allLights=self.allLights()
		KW=''
		if RGB=='r':
			KW=self.R_light
		elif RGB=='g':
			KW=self.G_light
		elif RGB=='b':
			KW=self.B_light
		for light in allLights:
			for k in KW:
				if light.find(k)!=-1:
					rv.append(light)
		return rv

	def allLayers(self):
		rv=[]
		rv=cmds.ls( '*' ,type='renderLayer')
		rv.remove('defaultRenderLayer')
		return rv

	def getCSLayers(self,CS):
		rv=[]
		allLayers=self.allLayers()
		KW=''
		if CS=='color':
			KW=self.color
		elif CS=='shadow':
			KW=self.shadow
		for layer in allLayers:
			for k in KW:
				if layer.find(k)!=-1:
					rv.append(layer)
		return rv

def changeColor():
	chrLN=chrLightName()

	R_Lights=chrLN.get_RGB_lights('r')
	G_Lights=chrLN.get_RGB_lights('g')
	B_Lights=chrLN.get_RGB_lights('b')

	color_Layer=chrLN.getCSLayers('color')
	shadow_Layer=chrLN.getCSLayers('shadow')

	for cL in color_Layer:
		cmds.editRenderLayerGlobals( currentRenderLayer=cL )
		for r in R_Lights:
			try:
				cmds.editRenderLayerAdjustment(r+'.color',r+'.shadowColor')
				cmds.setAttr(r+'.color', 1, 0, 0, type="double3")
				cmds.setAttr(r+'.shadowColor', 0, 0, 0, type="double3")
			except:
				pass
		for g in G_Lights:
			try:
				cmds.editRenderLayerAdjustment(g+'.color',g+'.shadowColor')
				cmds.setAttr(g+'.color', 0, 1, 0, type="double3")
				cmds.setAttr(g+'.shadowColor', 0, 0, 0, type="double3")
			except:
				pass
		for b in B_Lights:
			try:
				cmds.editRenderLayerAdjustment(b+'.color',b+'.shadowColor')
				cmds.setAttr(b+'.color', 0, 0, 1, type="double3")
				cmds.setAttr(b+'.shadowColor', 0, 0, 0, type="double3")
			except:
				pass
	for sL in shadow_Layer:
		cmds.editRenderLayerGlobals( currentRenderLayer=sL )
		for r in R_Lights:
			try:
				cmds.editRenderLayerAdjustment(r+'.color',r+'.shadowColor')
				cmds.setAttr(r+'.color', 0, 0, 0, type="double3")
				cmds.setAttr(r+'.shadowColor', 1, 0, 0, type="double3")
			except:
				pass
		for g in G_Lights:
			try:
				cmds.editRenderLayerAdjustment(g+'.color',g+'.shadowColor')
				cmds.setAttr(g+'.color', 0, 0, 0, type="double3")
				cmds.setAttr(g+'.shadowColor', 0, 1, 0, type="double3")
			except:
				pass
		for b in B_Lights:
			try:
				cmds.editRenderLayerAdjustment(b+'.color',b+'.shadowColor')
				cmds.setAttr(b+'.color', 0, 0, 0, type="double3")
				cmds.setAttr(b+'.shadowColor', 0, 0, 1, type="double3")
			except:
				pass




