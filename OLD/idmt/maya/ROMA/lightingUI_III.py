# -*- coding: utf-8 -*-
import maya.cmds as	cmds
import maya.mel	as mel
import datetime

import sys
if sys.platform == 'win32':
	execfile(r'\\file-cluster\GDC\Resource\Support\Maya\Python\IDMT\Lib\yyWinx2LightingExtra.py')
	execfile(r'\\file-cluster\GDC\Resource\Support\Maya\Python\IDMT\Lib\zzjZoomerate.py')
else:
	execfile(r'/mnt/support/Maya/Python/IDMT/Lib/yyWinx2LightingExtra.py')
	execfile(r'/mnt/support/Maya/Python/IDMT/Lib/zzjZoomerate.py')

'''
import sys
try:
	reload(win32con)
except:
	import sys
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32\lib')
	import win32clipboard
	import win32con
'''
def	getClipboard():
	import sys
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32\lib')
	import win32clipboard
	import win32con
	win32clipboard.OpenClipboard()
	d=win32clipboard.GetClipboardData(win32con.CF_TEXT)
	win32clipboard.CloseClipboard()
	return d

def	setClipboard(aType,aString):
	import sys
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32')
	sys.path.append(r'\\file-cluster\gdc\Resource\Support\Maya\Python\win32com\2.4\win32\lib')
	import win32clipboard
	aString=unicode(aString)
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboardData(aType,aString)
	win32clipboard.CloseClipboard()





mel.eval('source "rnd_wxII_renameEnvLights.mel"')
mel.eval('source "zzjIdPassInfo.mel"')
def	lUI():
	shelficons = ''
	buttonicons = ''
	if sys.platform == 'win32':
		shelficons = ''
		buttonicons = '//file-cluster/gdc/Resource/Support/Maya/icons/'
	else:
		shelficons = '/mnt/support/Maya/icons/'
		buttonicons = '/mnt/support/Maya/icons/'

	start=float(str(datetime.datetime.now())[-9:])

	try:
		cmds.deleteUI("wxIISetRenderLayerUI_III")
	except:
		pass
	cmds.window('wxIISetRenderLayerUI_III',title=u"wxII__???????????????3",mxb=False)

	cmds.paneLayout( configuration='bottom3',paneSize=[[1,50,28],[2,50,72] ])

	line_width=3

##zzj 	============Top===============
	line_color=[.7,0,0.7]
	form_T= cmds.formLayout(bgc=line_color)
	column_T = cmds.columnLayout(adjustableColumn=1,)

	cmds.formLayout(form_T,e=1,attachForm =[(column_T,'top',line_width),(column_T,'bottom',line_width),(column_T,'left',line_width),(column_T,'right',line_width),],)

##zzj	???????????????
	cmds.frameLayout( label=u'????????????    (????????????????????????????????????????????????????????????????????????)', collapsable=0)

	cmds.shelfLayout(cw=37,ch=38,h=200)
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????',iol=u'??????',style='iconOnly',
		i=shelficons + 'wxII/rnd_white.xpm',
		#c='mel.eval("py_autoSetForRendering")')
		c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.autoSetForRendering()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????Shot Content',iol=u'       SC',style='iconOnly',
	#	i=shelficons + 'wxII/gen_createShotContent.xpm',
	#	c='mel.eval("source \\\"gen_wxII_commonTools.mel\\\";wxII_commonTools(1);")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????SaveNode???MayaManNuggetDeleteScript',iol=u'???SN',i=r'mi-cross.xpm',style='iconOnly',c = 'execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\ndeleteSNAll()')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Copy finishing HRS cache',iol=u'Cache',style='iconOnly',
		i=shelficons + 'wxII/rnd_white.xpm',
		c='mel.eval("source \\\"gen_wxII_copyHRSCache.mel\\\";wxIICopyHRSCache(\\\"finishing\\\");")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'save Lighting',iol=u'?????????',style='iconOnly',
		i=r'fileSave.xpm',
		c='mel.eval("py_saveLighting();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????????????????',iol=u'???CAM',style='iconOnly',
		i=r'view.xpm',
		c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_ImportRenderCam();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????????????????',iol=u'       ???',i=shelficons + 'wxII/rnd._toogleMaps.xpm',style='iconOnly',c='mel.eval("source zwToggleMaps.mel; zwToggleMaps \\\"ROMA\\\";")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????smooth',iol=u'Smooth',i=r'polySmooth.xpm',style='iconOnly',c='mel.eval("zjTDSmooth")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????',iol=u'?????????',i=r'menuIconAdd.xpm',style='iconOnly',
	c='mel.eval("source \\\"zwRbwFixRender.mel\\\"; zwRbwFixRender;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????',iol=u'?????????',i=r'menuIconAdd.xpm',style='iconOnly',
	c='mel.eval("     source \\\"rnd_wxII_FixBeforeRender.mel\\\";wxII_FixBeforeRender(\\\"online\\\");       ")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????cacheFile?????????????????????????????????',iol=u'??????Cache',i=shelficons + 'wxII/rnd_white.xpm',style='iconOnly',
	c='mel.eval("zwOptimizeGeoCache;")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Shave???',iol=u'Shave',i=r'menuIconFur.xpm',style='iconOnly',
	c='mel.eval("eff_wxII_MShavePsets")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????Hair&Fur',iol=u'Fur',i=r'menuIconFur.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wx2_ysSetFursDensity.mel\\\";rnd_wx2_ysSetFursDensity();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????????????????',iol=u'    ??????',i=shelficons + 'wxII/rnd_netRender.xpm',style='iconOnly',c='mel.eval("source MusterCheckin.mel; global int $zwMusterIsBatch; $zwMusterIsBatch = 0; MusterCheckin")')

	cmds.setParent('..' )
	cmds.setParent('..' )

##zzj	???????????????
	cmds.frameLayout( label=u'???????????? ',collapsable=0,)
	cmds.shelfLayout(cw=37,ch=38,h=200,)

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????????????????',iol=u'????????????',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????finishing??????cache??????????????????',iol=u'Lost S',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostShader as fLS\nreload(fLS)\nfLS.fLS()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????finishing??????cache????????????cache',iol=u'Lost C',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostCache as fLC\nreload(fLC)\nfLC.fLC(type=1)')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????MayaManNugget???MayaManNuggetDeleteScript',iol=u'???Nugget',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source zwWinxDelNugget.mel; zwWinxDelNugget;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????',iol=u'?????????',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";lighting_DeleteUnusedNode();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????MM?????????',iol=u'???MM???',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_DeleteMMExtraChannels();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????????????????MMmatte????????????????????????',iol=u'??????',i=r'pythonFamily.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_MMmatte();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'zDepth',iol=u'zDepth',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools as RT\nreload(RT)\nRT.zDepth()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'mblur',iol=u'mblur',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.ysRmMblurTrans as ysRmMblur\nreload(ysRmMblur)\nysRmMblur.assignMVshaderOnNonTransObj()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'SSS????????????',iol=u'sss??????',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.sssAim()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'hairs<==>hairsmblur',iol=u'',i=shelficons + 'wxII/rnd_hairs2hairsmb.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.hairsmblur()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'camera, ?????????????????????',iol=u'cam??????',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nWinx2L2RCamWrapper()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????????????????????????????',iol=u'??????2',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nlocalFix2()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????????????????????????????',iol=u'??????2',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nnetFix2()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'camera, ?????????????????????',iol=u'cam??????',i=r'pythonFamily.xpm',style='iconOnly',c='raise Exception("not avaliable.")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????MayaManModelAttributes',iol=u'MayaManSmooth',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"lzyMMSubdiv.mel\\\";lzyMMSubdiv();")')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????RiFilters:MotionBeginRif',iol=u'MVRif',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.AddMotionBeginRif()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????RiFilters: HairRiF',iol=u'HairRiF',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.HairRiF()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'???????????????',iol=u'???CAM',i=r'view.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.StereoCamSolve()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Unlock',iol=u'Unlock',i=r'unlock.xpm',style='iconOnly')
	cmds.popupMenu(button = 1)
	cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform()')
	cmds.menuItem(label = u'???????????????????????????', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform(leaf = True)')
	cmds.popupMenu(button = 3)
	cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform()')
	cmds.menuItem(label = u'???????????????????????????', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform(leaf = True)')

	



	cmds.setParent('..' )
	cmds.setParent('..' )


##zzj	???????????????
	cmds.frameLayout( label=u'???????????? ',collapsable=0)
	cmds.shelfLayout(cw=37,ch=38,h=200)

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'????????????Far Clip Plane',iol=u'Far Clip',i=r'boxZoom.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_SetFarClipOfCamera();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Renderman??????????????????it',iol=u'        It',i=shelficons + 'wxII/rnd_it.xpm',style='iconOnly',c='import os\nos.system("start \\\\\\\\file-cluster/GDC/Resource/Support/Pixar/RenderMan-Studio-1.0.1-Maya8.5/bin/it.exe")\ntry:\n cmds.setAttr("MayaManNugget.CustomDisplay","it",type="string")\nexcept:\n pass')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'MayaMan?????????',iol=u'MM??????',i=shelficons + 'wxII/rnd_preRender.xpm',style='iconOnly',c='mel.eval("doMayaManRender(0)")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Set MayaMan Extra Output Channels\' Driver = ""',iol=u'???it',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwMayaManSetData \\\"EODriver\\\" \\\"\\\"")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Set MayaMan Extra Output Channels\' Driver = "it"',iol=u'???it',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwMayaManSetData \\\"EODriver\\\" \\\"it\\\"")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'PranaHair, tweakShader.py',iol=u'Timo???',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(idmt.maya.ROMA.tweakHairShader)\nexcept:\n\timport idmt.maya.ROMA.tweakHairShader\nidmt.maya.ROMA.tweakHairShader.tweakShader("Timo")')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????fol???????????????',iol=u'fol???',i=r'commandButton.xpm',style='iconOnly')
	#cmds.popupMenu(button = 1)
	#cmds.menuItem(label = u'????????????', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = True)')
	#cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = False)')
	#cmds.setParent('..', menu = True)
	#cmds.menuItem(label = u'????????????', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = True)')
	#cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = False)')
	#cmds.popupMenu(button = 3)
	#cmds.menuItem(label = u'????????????', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = True)')
	#cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = False)')
	#cmds.setParent('..', menu = True)
	#cmds.menuItem(label = u'????????????', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = True)')
	#cmds.menuItem(label = u'????????????', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = False)')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'?????????????????????',iol=u'lodGroup',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("string $cam[] = `ls -dag -sl -ni -cameras`; string $nodes[] = `ls -type lodGroup`; for ($item in $nodes) { connectAttr -f ($cam[0]+\\".worldMatrix[0]\\") ($item + \\".cameraMatrix\\"); } ")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????RiFilters:MotionBeginRif',iol=u'MVRif',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.AddMotionBeginRif()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'ptc ??????contactOcc On',iol=u'contactOcc',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.contactOccOn()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'???????????????MayaManTexture ??????',iol=u'tex',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.MayaManTexture()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'ptc??????...',iol=u'ptc??????',i=r'commandButton.xpm',style='iconOnly',c='import subprocess\nsubprocess.Popen("ptc.1.exe", shell=True)')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'??????ShaveRib??????',iol=u'?????????',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"zjRomaShaveExport.mel\\\"; zjRomaExShaveExportByObj;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'bypassMayaDisp',iol=u'BPD',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwSetIntAttrAll \\\"displacementShader\\\" \\\"bypassMayaDisp\\\" 1")')

	cmds.setParent('..' )
	cmds.setParent('..' )


	cmds.setParent('..' )
	cmds.setParent('..' )






##zzj 	============Right===============
	column_R = cmds.columnLayout(adjustableColumn=1,)

##zzj	?????????????????????
	line_color=[0.7,.7,0]
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',line_width),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'??????????????????', labelAlign='top')
	form = cmds.formLayout(numberOfDivisions=100)
#	columnLayout`
	column1	= cmds.columnLayout(adj=1)
#	???????????????
	cmds.button(l=u'???????????????', h=30 ,	c='mel.eval("source	\\\"rnd_wxII_RenderTools.mel\\\";wxII_ImportLGTLight();")')
	cmds.button(l=u'???????????????', h=52 ,	c='import idmt.maya.ROMA.renameChrLights as renameChrLights\nreload(renameChrLights)\nrenameChrLights.main()')
	cmds.setParent('..' )
#	columnLayout
	column2	= cmds.columnLayout(adj=1)
#	??????_key
#	??????_fill
#	??????_bounce
#	??????_rim
	cmds.button(l=u'??????_key	   ', bgc=[1,0,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("key")')
	cmds.button(l=u'??????_fill		  ', bgc=[0,1,0], h=20,	c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("fill")')
	cmds.button(l=u'??????_bounce', bgc=[0,1,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("bounce")')
	cmds.button(l=u'??????_rim	   ', bgc=[0,0.4,1], h=20, c='import idmt.maya.ROMA.renameEnvLights as	renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("rim")')
	cmds.setParent('..' )
	column3	= cmds.columnLayout(adj=1)
#	columnLayout
#	????????????
	cmds.button(l=u'????????????',bgc=[1,1,1],	c='import idmt.maya.ROMA.changeLightColor as changeLGTcolor\nreload(changeLGTcolor)\nchangeLGTcolor.changeColor()')

	cmds.setParent('..' )

	cmds.formLayout( form,
			edit=True,
			attachForm=		[
								(column1, 'left', 5), (column1,	'top', 5),
								(column2, 'right', 5),(column2,	'top', 5),
								(column3, 'left', 5),(column3, 'right',	5),(column3, 'bottom', 5)
							]
						,
			attachPosition=	[
								(column1, 'right', 5, 50),
								(column2, 'left', 5, 50)
							]
						,
			attachControl=	[
								(column3, 'top', 5,	column2)
							]

				)
	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )





##zzj	???????????????
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'????????????',	labelAlign='top')
	form = cmds.formLayout(numberOfDivisions=100)


#	?????????	 ???/???
#	??????  ???/???
	column1	= cmds.columnLayout(adj=1)
	b1=cmds.button(l=u'?????????	???/???',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')
	cmds.setParent('..' )

	column2	= cmds.columnLayout(adj=1)
	b2=cmds.button(l=u'??????  ???/???',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitSpecular();")')
	cmds.setParent('..' )

	column3	= cmds.columnLayout(adj=1)
#	??????
#	???????????????????????????
#	??????kiko ?????????

	cmds.button(l=u'??????',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_eyeTools();")')
	cmds.button(l=u'???????????????????????????',c='mel.eval("source	\\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnBackLightColor();")')
	cmds.button(l=u'??????kiko ?????????',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";importKikoLight();")')

	cmds.setParent('..' )
#	??????????????????????????????????????????
#	???????????????????????????
	column4	= cmds.columnLayout(adj=1)
	cmds.button(l=u'??????????????????????????????????????????',bgc=[1,1,1],c='import	idmt.maya.ROMA.GDC_lights_ShadowColor as GDC_Sc\nreload(GDC_Sc)\nGDC_Sc.ChangeColor()')
	cmds.setParent('..' )
	column5	= cmds.columnLayout(adj=1)
#	cmds.button(l=u'???????????????????????????',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\GDC_lights_ShadowColor.xls")')
	cmds.button(l=u'???????????????????????????',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Projects\ROMA\ROMA_Scratch\Lighting&Comp\RenderInfo\GDC_lights_ShadowColor.xls")')
	cmds.setParent('..' )


	cmds.formLayout( form,
			edit=True,
			attachForm=		[
								(column1, 'left', 5), (column1,	'top', 5),
								(column2, 'right', 5),(column2,'top', 5),
								(column3, 'left', 5), (column3,'right', 5),
								(column4,'left', 5),(column4,'bottom', 5),
								(column5,'right', 5),(column5,'bottom', 5),
							]
						,
			attachPosition=	[
								(column1, 'right', 5, 50),
								(column2, 'left', 5, 50),
								(column4, 'right', 5, 60),
								(column5, 'left', 5, 60),
							]
						,
			attachControl=	[
								(column3, 'top', 5,	column2),
								(column4, 'top', 5,	column3),
								(column5, 'top', 5,	column3),
							]
				)


	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )





##zzj	??????????????????
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',line_width),(column,'left',line_width),(column,'right',line_width),],)
##zzj	       ???????????????
	cmds.frameLayout( label=u'????????????', labelAlign='top')
	cmds.columnLayout()
#	rCLayout
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	ColorR
#	ColorG
#	ColorB
#	Color
#	Matte
	cmds.symbolButton(ann="ColorR",		i=buttonicons + "wxII/idpass/colorR.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorR\\\")")')
	cmds.symbolButton(ann="ColorG",		i=buttonicons + "wxII/idpass/colorG.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorG\\\")")')
	cmds.symbolButton(ann="ColorB",		i=buttonicons + "wxII/idpass/colorB.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorB\\\")")')
	cmds.symbolButton(ann="ColorA",		i=buttonicons + "wxII/idpass/colorA.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorA\\\")")')
	cmds.symbolButton(ann="Matte",			i=buttonicons + "wxII/idpass/matte.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"matte\\\")")')
	cmds.setParent('..' )
#	rCLayout
	cmds.columnLayout()
	cmds.separator(style='out',height=10,w=1000)
	cmds.setParent('..' )
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	Depth
#	Shadow
#	AO
#	Lambert
	cmds.symbolButton(ann="Depth",		i=buttonicons + "wxII/idpass/depth.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"depth\\\")")')
	cmds.symbolButton(ann="Shadow",	i=buttonicons + "wxII/idpass/shadow.xpm",	c='mel.eval("zzjIDPass_Material_Assign(\\\"shadow\\\")")')
	cmds.symbolButton(ann="AO",		i=buttonicons + "wxII/idpass/AO.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"AO\\\")")')
	cmds.symbolButton(ann="Lambert",	i=buttonicons + "wxII/idpass/lambert.xpm",	c='mel.eval("zzjIDPass_Material_Assign(\\\"lambert\\\")")')
	cmds.setParent('..' )
	cmds.setParent('..' )
	cmds.setParent('..' )
##zzj	       ???????????????
	cmds.frameLayout( label=u'????????????', labelAlign='top')
	cmds.columnLayout()
#	rCLayout
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	ColorR
#	ColorG
#	ColorB
#	Color
#	Matte
	cmds.symbolButton(ann="ColorR",		i=buttonicons + "wxII/idpass/colorR.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorR")')
	cmds.symbolButton(ann="ColorG",		i=buttonicons + "wxII/idpass/colorG.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorG")')
	cmds.symbolButton(ann="ColorB",		i=buttonicons + "wxII/idpass/colorB.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorB")')
	cmds.symbolButton(ann="ColorA",		i=buttonicons + "wxII/idpass/colorA.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorA")')
	cmds.symbolButton(ann="Matte",			i=buttonicons + "wxII/idpass/matte.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("matte")')
	cmds.symbolButton(ann="",  vis=0 ,		 i=buttonicons + "wxII/idpass/matte.xpm",		 c='')
	cmds.symbolButton(ann=u"MayaMan-Matte",		 i=buttonicons + "wxII/idpass/matte.xpm",		 c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_selected_MMmatte();")')

	cmds.setParent('..' )
	cmds.button(l=u'???????????????????????????polygon?????????????????????',c='import idmt.maya.ROMA.idpass4mm as	idpMM\nreload(idpMM)\nidpMM.selectFace()')
	cmds.setParent('..' )
	cmds.setParent('..' )



	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )








	cmds.setParent('..' )



##zzj 	============Left===============
	column_L = cmds.columnLayout(adjustableColumn=1,)

##zzj	???Finishing??????
	line_color=[0,0.7,0.7]
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',line_width),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'Finishing??????(??????????????????????????????)', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)

	form = cmds.formLayout(numberOfDivisions=100)
#	??????Finishing??????
#	??????Finishing??????
	b1 = cmds.button(l=u'??????Finishing????????????',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_OpenFinishingPath();")')
	b2 = cmds.button(l=u"??????Finishing??????",	c='import idmt.maya.ROMA.wxII_RenderTools as wRT\nreload(wRT)\nwRT.wxII_PY_OpenFinishingPath()' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])

	cmds.setParent( '..' )

	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )

##zzj	???MM Shader Path
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label='MM Shader Path	', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1,)
	cmds.textField(text=r'\\file-cluster\GDC\Resource\Support\Pixar\Shader',editable=1,w=300)


	form = cmds.formLayout(numberOfDivisions=100)
	path=r"\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\Shader"
#	??????MM?????????
#	????????????
	b1 = cmds.button(l=u'??????MM?????????',c='os.startfile(path)')
	b2 = cmds.button(l=u"????????????",	c='import idmt.maya.ROMA.lightingUI as lUI\nreload(lUI)\nlUI.setClipboard(13,"'+path+'")' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])

	cmds.setParent('..' )



	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )



##zzj	???RBW ??????
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'???????????????',	labelAlign='top')
#	Create	Light Rig
#	Create	Hairs Light	Rig
#	Neutralize	Color
#	Create	Occlusion
#	Create	SSS	Shader
	cmds.columnLayout(adjustableColumn=1)
	cmds.button(l='Create Light	Rig',		c='mel.eval("py_createLightRig")')
	cmds.button(l='Create Hairs	Light Rig',	c='mel.eval("py_createHairsLightRig")')
	cmds.button(l='Neutralize Color',		c='mel.eval("py_neutralizeColor")')
	cmds.button(l='Create Occlusion',		c='mel.eval("source \\\"lzyRomaChrOcc.mel\\\";lzyRomaChrOcc();")')
	cmds.button(l='Create SSS Shader',	c='mel.eval("py_createSSSShader")')
	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )



##zzj	???Mayaman??????????????????
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'Mayaman??????????????????',	labelAlign='top')

	cmds.floatSliderButtonGrp( 'wxIImmQuality_floatSlider',buttonLabel=u'????????????????????????',field =1, min=0, max=1, value=1, step=0.1 ,adj=2,
								columnWidth=[3,106],columnWidth2=[20,30],
								cc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmQuality()',
								bc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmDPShaderSelect()')

	cmds.setParent('..' )
	cmds.setParent('..' )
	cmds.setParent('..' )





##zzj	????????????ZoomIn
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'?????????ZoomIn',	labelAlign='top')
	pane = cmds.getPanel(wf=1)

	whichCam=''
	if cmds.modelPanel(pane,exists=1,):
		whichCam=cmds.modelPanel(pane,q=1,camera=1,)
	else:
		whichCam='persp'
	whichCamShape=cmds.ls(whichCam,dag=1,shapes=1,ap=1)

	cameras=cmds.ls(ca=1)
	perspCamera=[]
	for a in cameras:
		if not cmds.camera(a,q=1,orthographic=1):
			perspCamera.append(a)
	cameras=perspCamera
	diffCams=[]
	for a in cameras:
		if a not in whichCamShape:
			diffCams.append(a)

	formLayout=cmds.formLayout()
	cmds.optionMenuGrp('whichCam_P',l='Camera',columnAlign=[1,'right'],columnWidth=[1,100],changeCommand='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.changeCamera()')
	cmds.menuItem(l=whichCamShape[0])
	for a in diffCams:
		cmds.menuItem(l=a)

	camAttrX=whichCamShape[0]+ ".horizontalFilmOffset"
	camAttrY=whichCamShape[0]+ ".verticalFilmOffset"
	camAttrZ=whichCamShape[0]+ ".overscan"
	cmds.floatSliderGrp('offX_P',label='Horizontal',columnWidth=[1,100],v=cmds.getAttr(camAttrX),min=-3,max=3,fieldMinValue=-100,fieldMaxValue=100,precision=3,step=0.001,dc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',cc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',field=1,adjustableColumn=3)
	cmds.floatSliderGrp('offY_P',label='Vertical',columnWidth=[1,100],v=cmds.getAttr(camAttrY),min=-3,max=3,fieldMinValue=-100,fieldMaxValue=100,precision=3,step=0.001,dc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',cc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',field=1,adjustableColumn=3)
	cmds.floatSliderGrp('offZ_P',label='Zoom',columnWidth=[1,100],v=cmds.getAttr(camAttrZ),min=0.0001,max=2,fieldMinValue=0.0001,fieldMaxValue=100,precision=4,step=0.001,dc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',cc='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.zoomIt()',field=1,adjustableColumn=3)
	cmds.button('resetButton_P',l='Reset',c='import IDMT.Lib.zzjZoomerate as zoomCam\nzoomCam.resetCam()')

	cmds.setParent('..')
	cmds.formLayout(formLayout,e=1,
		attachForm =[
		('whichCam_P','top',5),('whichCam_P','left',5),('whichCam_P','right',5),
		('offX_P','left',5),('offX_P','right',5),
		('offY_P','left',5),('offY_P','right',5),
		('offZ_P','left',5),('offZ_P','right',5),
		('resetButton_P','left',5),('resetButton_P','right',5),
		],
		attachControl=[
		('offX_P','top',5,'whichCam_P' ),
		('offY_P','top',5,'offX_P' ),
		('offZ_P','top',5,'offY_P' ),
		('resetButton_P','top',5,'offZ_P' )
		],
	)
	cmds.setParent('..' )


	cmds.setParent('..' )
	cmds.setParent('..' )



##zzj	???Help
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',line_width),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label='Help ', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)
#	??????II????????????
	cmds.button(l=u'??????3????????????',c=u'os.startfile(r"\\\\file-cluster\\GDC\\Resource\\Support\\Maya\\Import\\iRender\\RenderInfo\\WinxClubII\\??????II????????????.txt")')
	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )






	cmds.setParent('..' )
	cmds.setParent('..' )
	cmds.setParent('..' )






	cmds.window('wxIISetRenderLayerUI_III',e=1,width=700,height=720)
	cmds.showWindow("wxIISetRenderLayerUI_III")



	end=float(str(datetime.datetime.now())[-9:])
	print (start-end)

