# -*- coding: utf-8 -*-
# http://johnlev.com/?p=145
'''
Voici un script Python que j’ai fait afin de créer dans ma scène un asset, contenant le rig stéréoscopique de Maya. Le but étant d’accéder rapidement aux paramètres les plus utilisés tout en évitant de modifier ceux qu’il ne faut pas. Rien de compliqué, juste du pratique. Si celà peut vous facilitez un peu les choses, servez vous. Il vous suffit de le copier dans le script éditor sous l’onglet Python et de l’exécuter pour créer le rig.
'''

def StereoRigAsset():
	# Macro : Create a Stereo Rig Asset by John Lev | blog : johnlev.com
	from maya.app.stereo import stereoCameraUtil
	stereoCameraUtil.loadPlugin()
	from maya.app.stereo import stereoCameraInitStereo
	import maya.app.stereo.stereoCameraRig as mscr
	import maya.cmds as mc
	stereoCameraInitStereo.init()

	stereoRig = mscr.createStereoCameraRig()
	stereoContainer = mc.container(addNode=stereoRig, name='stereoCameras', type='dagContainer', includeHierarchyBelow=True)
	mc.setAttr('stereoCameras.blackBox',True)

	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.zeroParallaxPlane','zeroParallaxPlane'])
	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.safeViewingVolume','safeViewingVolume'])

	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.horizontalFilmAperture','horizontalFilmAperture'])
	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.verticalFilmAperture','verticalFilmAperture'])

	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.focalLength','focalLength'])
	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.interaxialSeparation','interaxialSeparation'])
	mc.container(stereoContainer,edit=True,publishAndBind=['stereoCameraCenterCamShape.zeroParallax','zeroParallax'])

	mc.xform(stereoContainer,pivots=(0.0,0.0,0.0))