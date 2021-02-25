# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Tools for ROMA
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-07-22'

import maya.cmds as cmds
import maya.OpenMaya as OpenMaya

def parti_volume():
	'''
	wrote by huangzhongwei
	'''
	sl = cmds.ls(sl = True)
	if len(sl) != 4:
		OpenMaya.MGlobal.displayError(u'请依次选择Boundary、spotLight、medium、camera')
		return
	Boundary = sl[0]
	spotLight1 = sl[1]
	medium = sl[2]
	camera1 = sl[3]

	#Boundary = 'Boundary'
	transmat1 = cmds.createNode('transmat')
	transmat1SG = cmds.sets(renderable = True, noSurfaceShader = True, empty = True, name = transmat1 + 'SG')
	cmds.connectAttr(transmat1 + '.outValue', transmat1SG + '.miPhotonShader')
	cmds.connectAttr(transmat1 + '.outValue', transmat1SG + '.miMaterialShader')
	cmds.sets(Boundary, edit = True, forceElement = transmat1SG)
	parti_volume1 = cmds.createNode('parti_volume')
	cmds.connectAttr(parti_volume1 + '.outValue', transmat1SG + '.miVolumeShader')
	cmds.setAttr(parti_volume1 + '.scatter', 0.2, 0.2, 0.2, typ = 'double3')
	cmds.setAttr(parti_volume1 + '.extinction', 0.01)

	#spotLight1 = 'spotLight1'
	cmds.setAttr(spotLight1 + '.emitDiffuse', False)
	cmds.setAttr(spotLight1 + '.emitSpecular', False)
	cmds.setAttr(spotLight1 + '.emitPhotons', True)
	cmds.setAttr('miDefaultOptions.caustics', True)

	#medium = 'medium'
	dielectric_material1 = cmds.createNode('dielectric_material')
	dielectric_material1SG = cmds.sets(renderable = True, noSurfaceShader = True, empty = True, name = dielectric_material1 + 'SG')
	cmds.connectAttr(dielectric_material1 + '.outValue', dielectric_material1SG + '.miPhotonShader')
	cmds.connectAttr(dielectric_material1 + '.outValue', dielectric_material1SG + '.miMaterialShader')
	cmds.sets(medium, edit = True, forceElement = dielectric_material1SG)
	ocean1 = cmds.shadingNode('ocean', asTexture = True)
	place2dTexture1 = cmds.shadingNode('place2dTexture', asUtility = True)
	cmds.connectAttr(place2dTexture1 + '.outUV', ocean1 + '.uv')
	cmds.connectAttr(place2dTexture1 + '.outUvFilterSize', ocean1 + '.uvFilterSize')
	displacementShader1 = cmds.createNode('displacementShader')
	cmds.connectAttr(ocean1 + '.outAlpha', displacementShader1 + '.displacement')
	cmds.connectAttr(displacementShader1 + '.displacement', dielectric_material1SG + '.displacementShader')
	cmds.setAttr(ocean1 + '.alphaIsLuminance', True)
	cmds.connectAttr(parti_volume1 + '.outValue', dielectric_material1SG + '.miVolumeShader')
	parti_volume_photon1 = cmds.createNode('parti_volume_photon')
	cmds.connectAttr(parti_volume_photon1 + '.outValue', dielectric_material1SG + '.miPhotonVolumeShader')
	cmds.setAttr(parti_volume_photon1 + '.scatter', 0.2, 0.2, 0.2, typ = 'double3')
	cmds.setAttr(parti_volume_photon1 + '.extinction', 0.01)

	#camera1 = 'camera1'
	cmds.connectAttr(parti_volume1 + '.message', camera1 + '.miVolumeShader')