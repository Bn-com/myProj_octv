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
	cmds.window('wxIISetRenderLayerUI_III',title=u"wxII__渲染工具集3",mxb=False)

	cmds.paneLayout( configuration='bottom3',paneSize=[[1,50,28],[2,50,72] ])

	line_width=3

##zzj 	============Top===============
	line_color=[.7,0,0.7]
	form_T= cmds.formLayout(bgc=line_color)
	column_T = cmds.columnLayout(adjustableColumn=1,)

	cmds.formLayout(form_T,e=1,attachForm =[(column_T,'top',line_width),(column_T,'bottom',line_width),(column_T,'left',line_width),(column_T,'right',line_width),],)

##zzj	▲常用工具
	cmds.frameLayout( label=u'常用工具    (提示：可用鼠标中间拖拽下面的工具到自己的工具架上)', collapsable=0)

	cmds.shelfLayout(cw=37,ch=38,h=200)
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'建层',iol=u'建层',style='iconOnly',
		i=shelficons + 'wxII/rnd_white.xpm',
		#c='mel.eval("py_autoSetForRendering")')
		c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.autoSetForRendering()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'创建Shot Content',iol=u'       SC',style='iconOnly',
	#	i=shelficons + 'wxII/gen_createShotContent.xpm',
	#	c='mel.eval("source \\\"gen_wxII_commonTools.mel\\\";wxII_commonTools(1);")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'删除SaveNode、MayaManNuggetDeleteScript',iol=u'删SN',i=r'mi-cross.xpm',style='iconOnly',c = 'execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\ndeleteSNAll()')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Copy finishing HRS cache',iol=u'Cache',style='iconOnly',
		i=shelficons + 'wxII/rnd_white.xpm',
		c='mel.eval("source \\\"gen_wxII_copyHRSCache.mel\\\";wxIICopyHRSCache(\\\"finishing\\\");")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'save Lighting',iol=u'存文件',style='iconOnly',
		i=r'fileSave.xpm',
		c='mel.eval("py_saveLighting();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'导入渲染用摄像机',iol=u'导CAM',style='iconOnly',
		i=r'view.xpm',
		c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_ImportRenderCam();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'贴图尺寸转换',iol=u'       剪',i=shelficons + 'wxII/rnd._toogleMaps.xpm',style='iconOnly',c='mel.eval("source zwToggleMaps.mel; zwToggleMaps \\\"ROMA\\\";")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'设置smooth',iol=u'Smooth',i=r'polySmooth.xpm',style='iconOnly',c='mel.eval("zjTDSmooth")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'本地补',iol=u'本地补',i=r'menuIconAdd.xpm',style='iconOnly',
	c='mel.eval("source \\\"zwRbwFixRender.mel\\\"; zwRbwFixRender;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'网渲补',iol=u'网渲补',i=r'menuIconAdd.xpm',style='iconOnly',
	c='mel.eval("     source \\\"rnd_wxII_FixBeforeRender.mel\\\";wxII_FixBeforeRender(\\\"online\\\");       ")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'共用一个cacheFile节点，播放动画速度变快',iol=u'共用Cache',i=shelficons + 'wxII/rnd_white.xpm',style='iconOnly',
	c='mel.eval("zwOptimizeGeoCache;")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Shave补',iol=u'Shave',i=r'menuIconFur.xpm',style='iconOnly',
	c='mel.eval("eff_wxII_MShavePsets")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'渲染优化Hair&Fur',iol=u'Fur',i=r'menuIconFur.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wx2_ysSetFursDensity.mel\\\";rnd_wx2_ysSetFursDensity();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'提交网络渲染',iol=u'    网渲',i=shelficons + 'wxII/rnd_netRender.xpm',style='iconOnly',c='mel.eval("source MusterCheckin.mel; global int $zwMusterIsBatch; $zwMusterIsBatch = 0; MusterCheckin")')

	cmds.setParent('..' )
	cmds.setParent('..' )

##zzj	▲其他工具
	cmds.frameLayout( label=u'其他工具 ',collapsable=0,)
	cmds.shelfLayout(cw=37,ch=38,h=200,)

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'关闭灯光的漫反射',iol=u'关漫反射',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'找到因finishing更新cache而丢失的材质',iol=u'Lost S',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostShader as fLS\nreload(fLS)\nfLS.fLS()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'找到因finishing更新cache而丢失的cache',iol=u'Lost C',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostCache as fLC\nreload(fLC)\nfLC.fLC(type=1)')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'删除MayaManNugget、MayaManNuggetDeleteScript',iol=u'删Nugget',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source zwWinxDelNugget.mel; zwWinxDelNugget;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'删除材质',iol=u'删材质',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";lighting_DeleteUnusedNode();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'删除所有MM额外层',iol=u'删MM层',i=r'mi-cross.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_DeleteMMExtraChannels();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'为所有物体创建MMmatte，（适用于头发）',iol=u'遮罩',i=r'pythonFamily.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_MMmatte();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'zDepth',iol=u'zDepth',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools as RT\nreload(RT)\nRT.zDepth()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'mblur',iol=u'mblur',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.ysRmMblurTrans as ysRmMblur\nreload(ysRmMblur)\nysRmMblur.assignMVshaderOnNonTransObj()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'SSS对齐灯光',iol=u'sss对齐',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.sssAim()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'hairs<==>hairsmblur',iol=u'',i=shelficons + 'wxII/rnd_hairs2hairsmb.xpm',style='iconOnly',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.hairsmblur()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'camera, 左到右，右到左',iol=u'cam左右',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nWinx2L2RCamWrapper()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'本地“补”，但不改参数',iol=u'本补2',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nlocalFix2()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'网渲“补”，但不改参数',iol=u'网补2',i=r'pythonFamily.xpm',style='iconOnly',c='execfile(\"//file-cluster/GDC/Resource/Support/Maya/Python/IDMT/yyScripts/yyWinx2LightingExtra.py\")\nnetFix2()')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'camera, 左到右，右到左',iol=u'cam左右',i=r'pythonFamily.xpm',style='iconOnly',c='raise Exception("not avaliable.")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'添加MayaManModelAttributes',iol=u'MayaManSmooth',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"lzyMMSubdiv.mel\\\";lzyMMSubdiv();")')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'添加RiFilters:MotionBeginRif',iol=u'MVRif',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.AddMotionBeginRif()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'添加RiFilters: HairRiF',iol=u'HairRiF',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.HairRiF()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'修改摄像机',iol=u'改CAM',i=r'view.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.StereoCamSolve()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Unlock',iol=u'Unlock',i=r'unlock.xpm',style='iconOnly')
	cmds.popupMenu(button = 1)
	cmds.menuItem(label = u'选择物体', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform()')
	cmds.menuItem(label = u'选择物体及其子物体', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform(leaf = True)')
	cmds.popupMenu(button = 3)
	cmds.menuItem(label = u'选择物体', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform()')
	cmds.menuItem(label = u'选择物体及其子物体', command = 'try:\n\treload(idmt.maya.cmds)\nexcept:\n\timport idmt.maya.cmds\nidmt.maya.cmds.UnlockTransform(leaf = True)')

	



	cmds.setParent('..' )
	cmds.setParent('..' )


##zzj	▲渲染工具
	cmds.frameLayout( label=u'渲染工具 ',collapsable=0)
	cmds.shelfLayout(cw=37,ch=38,h=200)

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'摄像机的Far Clip Plane',iol=u'Far Clip',i=r'boxZoom.xpm',style='iconOnly',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_SetFarClipOfCamera();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Renderman预览工具——it',iol=u'        It',i=shelficons + 'wxII/rnd_it.xpm',style='iconOnly',c='import os\nos.system("start \\\\\\\\file-cluster/GDC/Resource/Support/Pixar/RenderMan-Studio-1.0.1-Maya8.5/bin/it.exe")\ntry:\n cmds.setAttr("MayaManNugget.CustomDisplay","it",type="string")\nexcept:\n pass')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'MayaMan预渲染',iol=u'MM预渲',i=shelficons + 'wxII/rnd_preRender.xpm',style='iconOnly',c='mel.eval("doMayaManRender(0)")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Set MayaMan Extra Output Channels\' Driver = ""',iol=u'去it',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwMayaManSetData \\\"EODriver\\\" \\\"\\\"")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Set MayaMan Extra Output Channels\' Driver = "it"',iol=u'设it',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwMayaManSetData \\\"EODriver\\\" \\\"it\\\"")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'PranaHair, tweakShader.py',iol=u'Timo发',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(idmt.maya.ROMA.tweakHairShader)\nexcept:\n\timport idmt.maya.ROMA.tweakHairShader\nidmt.maya.ROMA.tweakHairShader.tweakShader("Timo")')
	#cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'切换fol贴图的大小',iol=u'fol图',i=r'commandButton.xpm',style='iconOnly')
	#cmds.popupMenu(button = 1)
	#cmds.menuItem(label = u'全部贴图', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = True)')
	#cmds.menuItem(label = u'原始贴图', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = False)')
	#cmds.setParent('..', menu = True)
	#cmds.menuItem(label = u'选择物体', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = True)')
	#cmds.menuItem(label = u'原始贴图', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = False)')
	#cmds.popupMenu(button = 3)
	#cmds.menuItem(label = u'全部贴图', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = True)')
	#cmds.menuItem(label = u'原始贴图', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = False, nosize = False)')
	#cmds.setParent('..', menu = True)
	#cmds.menuItem(label = u'选择物体', subMenu = True)
	#cmds.menuItem(label = u'nosize', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = True)')
	#cmds.menuItem(label = u'原始贴图', command = 'try:\n\treload(idmt.maya.roma)\nexcept:\n\timport idmt.maya.roma\nidmt.maya.roma.ToggleFolTexture(selected = True, nosize = False)')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'选择一个摄像机',iol=u'lodGroup',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("string $cam[] = `ls -dag -sl -ni -cameras`; string $nodes[] = `ls -type lodGroup`; for ($item in $nodes) { connectAttr -f ($cam[0]+\\".worldMatrix[0]\\") ($item + \\".cameraMatrix\\"); } ")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'添加RiFilters:MotionBeginRif',iol=u'MVRif',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.AddMotionBeginRif()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'ptc 文件contactOcc On',iol=u'contactOcc',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.contactOccOn()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'设置贴图的MayaManTexture 属性',iol=u'tex',i=r'commandButton.xpm',style='iconOnly',c='try:\n\treload(roma)\nexcept:\n\timport idmt.maya.roma as roma\nroma.MayaManTexture()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'ptc工具...',iol=u'ptc工具',i=r'commandButton.xpm',style='iconOnly',c='import subprocess\nsubprocess.Popen("ptc.1.exe", shell=True)')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'复杂ShaveRib输出',iol=u'出杂毛',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"zjRomaShaveExport.mel\\\"; zjRomaExShaveExportByObj;")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'bypassMayaDisp',iol=u'BPD',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("zwSetIntAttrAll \\\"displacementShader\\\" \\\"bypassMayaDisp\\\" 1")')

	cmds.setParent('..' )
	cmds.setParent('..' )


	cmds.setParent('..' )
	cmds.setParent('..' )






##zzj 	============Right===============
	column_R = cmds.columnLayout(adjustableColumn=1,)

##zzj	▲灯光改名上色
	line_color=[0.7,.7,0]
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',line_width),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'灯光改名上色', labelAlign='top')
	form = cmds.formLayout(numberOfDivisions=100)
#	columnLayout`
	column1	= cmds.columnLayout(adj=1)
#	改角色灯名
	cmds.button(l=u'导入角色灯', h=30 ,	c='mel.eval("source	\\\"rnd_wxII_RenderTools.mel\\\";wxII_ImportLGTLight();")')
	cmds.button(l=u'改角色灯名', h=52 ,	c='import idmt.maya.ROMA.renameChrLights as renameChrLights\nreload(renameChrLights)\nrenameChrLights.main()')
	cmds.setParent('..' )
#	columnLayout
	column2	= cmds.columnLayout(adj=1)
#	场景_key
#	场景_fill
#	场景_bounce
#	场景_rim
	cmds.button(l=u'场景_key	   ', bgc=[1,0,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("key")')
	cmds.button(l=u'场景_fill		  ', bgc=[0,1,0], h=20,	c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("fill")')
	cmds.button(l=u'场景_bounce', bgc=[0,1,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("bounce")')
	cmds.button(l=u'场景_rim	   ', bgc=[0,0.4,1], h=20, c='import idmt.maya.ROMA.renameEnvLights as	renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("rim")')
	cmds.setParent('..' )
	column3	= cmds.columnLayout(adj=1)
#	columnLayout
#	灯光上色
	cmds.button(l=u'灯光上色',bgc=[1,1,1],	c='import idmt.maya.ROMA.changeLightColor as changeLGTcolor\nreload(changeLGTcolor)\nchangeLGTcolor.changeColor()')

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





##zzj	▲灯光工具
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'灯光工具',	labelAlign='top')
	form = cmds.formLayout(numberOfDivisions=100)


#	漫反射	 开/关
#	高光  开/关
	column1	= cmds.columnLayout(adj=1)
	b1=cmds.button(l=u'漫反射	开/关',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')
	cmds.setParent('..' )

	column2	= cmds.columnLayout(adj=1)
	b2=cmds.button(l=u'高光  开/关',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitSpecular();")')
	cmds.setParent('..' )

	column3	= cmds.columnLayout(adj=1)
#	眼球
#	灯光变白，阴影变黑
#	导入kiko 专用灯

	cmds.button(l=u'眼球',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_eyeTools();")')
	cmds.button(l=u'灯光变白，阴影变黑',c='mel.eval("source	\\\"rnd_wxII_RenderTools.mel\\\";wxII_TurnBackLightColor();")')
	cmds.button(l=u'导入kiko 专用灯',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";importKikoLight();")')

	cmds.setParent('..' )
#	根据数据库，改头发灯阴影颜色
#	查看头发阴影颜色表
	column4	= cmds.columnLayout(adj=1)
	cmds.button(l=u'根据数据库，改头发灯阴影颜色',bgc=[1,1,1],c='import	idmt.maya.ROMA.GDC_lights_ShadowColor as GDC_Sc\nreload(GDC_Sc)\nGDC_Sc.ChangeColor()')
	cmds.setParent('..' )
	column5	= cmds.columnLayout(adj=1)
#	cmds.button(l=u'查看头发阴影颜色表',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\GDC_lights_ShadowColor.xls")')
	cmds.button(l=u'查看头发阴影颜色表',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Projects\ROMA\ROMA_Scratch\Lighting&Comp\RenderInfo\GDC_lights_ShadowColor.xls")')
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





##zzj	▲赋材质工具
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',line_width),(column,'left',line_width),(column,'right',line_width),],)
##zzj	       ▲材质工具
	cmds.frameLayout( label=u'材质工具', labelAlign='top')
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
##zzj	       ▲置换专用
	cmds.frameLayout( label=u'置换专用', labelAlign='top')
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
	cmds.button(l=u'通过选择的材质球和polygon，选中相应的面',c='import idmt.maya.ROMA.idpass4mm as	idpMM\nreload(idpMM)\nidpMM.selectFace()')
	cmds.setParent('..' )
	cmds.setParent('..' )



	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )








	cmds.setParent('..' )



##zzj 	============Left===============
	column_L = cmds.columnLayout(adjustableColumn=1,)

##zzj	▲Finishing目录
	line_color=[0,0.7,0.7]
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',line_width),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'Finishing目录(根据当前工程目录判断)', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)

	form = cmds.formLayout(numberOfDivisions=100)
#	打开Finishing目录
#	复制Finishing路径
	b1 = cmds.button(l=u'打开Finishing文件目录',c='mel.eval("source \\\"rnd_wxII_RenderTools.mel\\\";wxII_OpenFinishingPath();")')
	b2 = cmds.button(l=u"复制Finishing路径",	c='import idmt.maya.ROMA.wxII_RenderTools as wRT\nreload(wRT)\nwRT.wxII_PY_OpenFinishingPath()' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])

	cmds.setParent( '..' )

	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )

##zzj	▲MM Shader Path
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label='MM Shader Path	', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1,)
	cmds.textField(text=r'\\file-cluster\GDC\Resource\Support\Pixar\Shader',editable=1,w=300)


	form = cmds.formLayout(numberOfDivisions=100)
	path=r"\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\Shader"
#	打开MM文件夹
#	复制路径
	b1 = cmds.button(l=u'打开MM文件夹',c='os.startfile(path)')
	b2 = cmds.button(l=u"复制路径",	c='import idmt.maya.ROMA.lightingUI as lUI\nreload(lUI)\nlUI.setClipboard(13,"'+path+'")' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])

	cmds.setParent('..' )



	cmds.setParent('..' )
	cmds.setParent('..' )

	cmds.setParent('..' )
	cmds.setParent('..' )



##zzj	▲RBW 工具
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'客户的工具',	labelAlign='top')
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



##zzj	▲Mayaman置换渲染质量
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'Mayaman置换渲染质量',	labelAlign='top')

	cmds.floatSliderButtonGrp( 'wxIImmQuality_floatSlider',buttonLabel=u'选择所有置换节点',field =1, min=0, max=1, value=1, step=0.1 ,adj=2,
								columnWidth=[3,106],columnWidth2=[20,30],
								cc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmQuality()',
								bc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmDPShaderSelect()')

	cmds.setParent('..' )
	cmds.setParent('..' )
	cmds.setParent('..' )





##zzj	▲摄像机ZoomIn
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',0),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label=u'摄像机ZoomIn',	labelAlign='top')
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



##zzj	▲Help
	form= cmds.formLayout(bgc=line_color)
	column = cmds.columnLayout(adjustableColumn=1,)
	cmds.formLayout(form,e=1,attachForm =[(column,'top',0),(column,'bottom',line_width),(column,'left',line_width),(column,'right',line_width),],)

	cmds.frameLayout( label='Help ', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)
#	工具II更新日志
	cmds.button(l=u'工具3更新日志',c=u'os.startfile(r"\\\\file-cluster\\GDC\\Resource\\Support\\Maya\\Import\\iRender\\RenderInfo\\WinxClubII\\工具II更改说明.txt")')
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

