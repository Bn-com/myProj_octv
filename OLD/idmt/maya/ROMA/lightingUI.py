# -*- coding: gbk -*-
import maya.cmds as	cmds
import maya.mel	as mel
execfile(r'\\file-cluster\GDC\Resource\Support\Maya\Python\IDMT\Lib\zzjZoomerate.py')
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


mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_renameEnvLights.mel"')
mel.eval('source "//file-cluster/GDC/Resource/Support/Maya/2013/zzjIdPassInfo.mel"')
def	lUI():
	try:
		cmds.deleteUI("wxIISetRenderLayerUI")
	except:
		pass
	cmds.window('wxIISetRenderLayerUI',title="wxII__LightingTools",mxb=False)
	tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

##zzj  �����ù���
	child1 = cmds.columnLayout(adjustableColumn=1)
##zzj	       �����ù���
	cmds.frameLayout( label=u'���ù���',	labelAlign='top', collapsable=0)
#	����Ŀ¼
#	���ļ�
#	������Ⱦ�������
#	��

	cmds.shelfLayout(h=100)
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'����',iol=u'����',style='iconOnly',
		i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd_white.xpm',
		c='mel.eval(\"py_autoSetForRendering();rnd_wxII_setSpotLightFocus;\")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'����Shot Content',iol=u'       SC',style='iconOnly',
		i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\gen_createShotContent.xpm',
		c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/gen_wxII_commonTools.mel\\\";wxII_commonTools(1);")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'Copy finishing HRS cache',iol=u'Cache',style='iconOnly',
		i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd_white.xpm',
		c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/gen_wxII_copyHRSCache.mel\\\";wxIICopyHRSCache(\\\"finishing\\\");")')



	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'save Lighting',iol=u'���ļ�',style='iconOnly',
		i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd_white.xpm',
		c='mel.eval("py_saveLighting();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'������Ⱦ�������',iol=u'CAM',style='iconOnly',
		i1='view.xpm',
		c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_ImportRenderCam();")')


	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'��ͼ�ߴ�ת��',iol=u'       ��',i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd._toogleMaps.xpm',style='iconOnly',c='mel.eval("source zwToggleMaps.mel; zwToggleMaps \\\"WinxClubII\\\";")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'����smooth',iol=u'Smooth',i1='commandButton.xpm',style='iconOnly',c='mel.eval("zjTDSmooth")')

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'���ֲ���',iol=u'��',style='iconOnly',
		i1=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd_white.xpm',)
	cmds.popupMenu('wxrnd',button=1)
	cmds.menuItem(l=u'Shave��',parent='wxrnd',c='mel.eval("eff_wxII_MShavePsets")')
	cmds.menuItem(l=u'���ز�',parent='wxrnd',c='mel.eval("     source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_FixBeforeRender.mel\\\";wxII_FixBeforeRender(\\\"project\\\");       ")')
	cmds.menuItem(l=u'���ֲ�',parent='wxrnd',c='mel.eval("     source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_FixBeforeRender.mel\\\";wxII_FixBeforeRender(\\\"online\\\");       ")')


	cmds.setParent(	'..' )
	cmds.setParent(	'..' )




##zzj	       ����������
	cmds.frameLayout( label=u'�������� ', labelAlign='top',collapsable=0)
	cmds.columnLayout(adjustableColumn=1)
#	��ͼ�ߴ�ת��
#	����smooth
#	�������Far Clip Plane
#	RendermanԤ�����ߡ���it

	cmds.shelfLayout(h=100)

	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'�������Far Clip Plane',iol=u'Far Clip',i1='commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_SetFarClipOfCamera();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'RendermanԤ�����ߡ���it',iol=u'        It',i=r'\\file-cluster\gdc\Resource\Support\Maya\icons\wxII\rnd_it.xpm',style='iconOnly',c='import os\nos.system("start \\\\\\\\file-cluster/GDC/Resource/Support/Pixar/RenderMan-Studio-1.0.1-Maya8.5/bin/it.exe")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'�رյƹ��������',iol=u'��������',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'����Kiko��',iol=u'Kiko',i=r'commandButton.xpm',style='iconOnly',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";importKikoLight();")')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'�ҵ���finishing����cache����ʧ�Ĳ���',iol=u'Lost S',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostShader as fLS\nreload(fLS)\nfLS.fLS()')
	cmds.shelfButton(w=34,h=34,font='smallPlainLabelFont',l=u'�ҵ���finishing����cache����ʧ��cache',iol=u'Lost C',i=r'pythonFamily.xpm',style='iconOnly',c='import idmt.maya.ROMA.findLostCache as fLC\nreload(fLC)\nfLC.fLC(type=1)')


	cmds.setParent(	'..' )

	cmds.setParent(	'..' )
	cmds.setParent(	'..' )

##zzj	       �������ZoomIn
	cmds.frameLayout( label=u'�����ZoomIn',	labelAlign='top')

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
	cmds.setParent(	'..' )

##zzj	       ��Mayaman�û���Ⱦ����
	cmds.frameLayout( label=u'Mayaman�û���Ⱦ����',	labelAlign='top')


	cmds.columnLayout(adjustableColumn=1,adj=1)
	cmds.floatSliderButtonGrp( 'wxIImmQuality_floatSlider',buttonLabel=u'ѡ�������û��ڵ�',field =1, min=0, max=1, value=1, step=0.1 ,adj=2,
								columnWidth=[3,106],columnWidth2=[20,30],
								cc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmQuality()',
								bc='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.mmDPShaderSelect()')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )


	cmds.setParent(	'..' )

##zzj  ��Setting
	child2 = cmds.columnLayout(adjustableColumn=1)

##zzj	       ����
	cmds.frameLayout( label=u'��', labelAlign='top')

	cmds.columnLayout(adjustableColumn=1)

#	��FinishingĿ¼
#    ����Finishing·��
	form = cmds.formLayout(numberOfDivisions=100)
	path=r"\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\Shader"
	b1 = cmds.button(l=u'��Finishing�ļ�Ŀ¼',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_OpenFinishingPath();")')
	b2 = cmds.button(l=u"����Finishing·��",	c='import idmt.maya.ROMA.wxII_RenderTools as wRT\nreload(wRT)\nwRT.wxII_PY_OpenFinishingPath()' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])
	cmds.setParent( '..' )


#	��ͷ����Ӱ��ɫ��
	cmds.button(l=u'��ͷ����Ӱ��ɫ��',c='import os\nos.startfile(r"\\\\file-cluster\GDC\Resource\Support\Maya\Import\iRender\RenderInfo\ROMA\GDC_lights_ShadowColor.xls")')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )

##zzj	       ��Other tools
	cmds.frameLayout( label='Other tools', labelAlign='top')
#	��Ⱦ�Ż�Hair&Fur
#	ɾ������
#	ɾ������MM��
#	zdepth
#	mblur
#	MMmatte
#	sss����ƹ�
#	hairs<==>hairsmblur
	cmds.columnLayout(adjustableColumn=1)
	cmds.button(l=u'��Ⱦ�Ż�Hair &&	Fur',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wx2_ysSetFursDensity.mel\\\";rnd_wx2_ysSetFursDensity();")')
	cmds.button(l=u'ɾ������',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";lighting_DeleteUnusedNode();")')
	cmds.button(l=u'ɾ������MM��',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_DeleteMMExtraChannels();")')
#	 cmds.button(l=u'zdepth',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_zDepth();")')
	cmds.button(l=u'zdepth',c='import idmt.maya.ROMA.wxII_RenderTools as RT\nreload(RT)\nRT.zDepth()')
#	cmds.button(l=u'mblur',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_mBlur();")')
	cmds.button(l=u'mblur',c='import idmt.maya.ROMA.ysRmMblurTrans as ysRmMblur\nreload(ysRmMblur)\nysRmMblur.assignMVshaderOnNonTransObj()')
	cmds.button(l=u'�������崴��MMmatte����������ͷ����',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_MMmatte();")')
	cmds.button(l=u'sss����ƹ�',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.sssAim()')
	cmds.button(l=u'hairs<==>hairsmblur',c='import idmt.maya.ROMA.wxII_RenderTools	as RT\nreload(RT)\nRT.hairsmblur()')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )

	cmds.setParent(	'..' )

##zzj  ���ƹ⹤��
	child3 = cmds.columnLayout(adjustableColumn=1)
##zzj	       ���ƹ������ɫ
	cmds.frameLayout( label=u'�ƹ������ɫ', labelAlign='top')
	form = cmds.formLayout(numberOfDivisions=100)
#	columnLayout`
	column1	= cmds.columnLayout(adj=1)
#	�Ľ�ɫ����
	cmds.button(l=u'�����ɫ��', h=30 ,	c='mel.eval("source	\\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_ImportLGTLight();")')
	cmds.button(l=u'�Ľ�ɫ����', h=52 ,	c='import idmt.maya.ROMA.renameChrLights as renameChrLights\nreload(renameChrLights)\nrenameChrLights.main()')
	cmds.setParent(	'..' )
#	columnLayout
	column2	= cmds.columnLayout(adj=1)
#	����_key
#	����_fill
#	����_bounce
#	����_rim
	cmds.button(l=u'����_key	   ', bgc=[1,0,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("key")')
	cmds.button(l=u'����_fill		  ', bgc=[0,1,0], h=20,	c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("fill")')
	cmds.button(l=u'����_bounce', bgc=[0,1,0], h=20, c='import idmt.maya.ROMA.renameEnvLights as renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("bounce")')
	cmds.button(l=u'����_rim	   ', bgc=[0,0.4,1], h=20, c='import idmt.maya.ROMA.renameEnvLights as	renameEnvLights\nreload(renameEnvLights)\nrenameEnvLights.rename("rim")')
	cmds.setParent(	'..' )
	column3	= cmds.columnLayout(adj=1)
#	columnLayout
#	�ƹ���ɫ
	cmds.button(l=u'�ƹ���ɫ',bgc=[1,1,1],	c='import idmt.maya.ROMA.changeLightColor as changeLGTcolor\nreload(changeLGTcolor)\nchangeLGTcolor.changeColor()')

	cmds.setParent(	'..' )

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
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )
##zzj	       ��Other tools
	cmds.frameLayout( label='Other tools ',	labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)
	form = cmds.formLayout(numberOfDivisions=100)
#	columnLayout`
	column1	= cmds.columnLayout(adj=1)
#	������	 ��/��
	cmds.button(l=u'������	��/��',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitDiffuse();")')

	cmds.setParent(	'..' )
#	columnLayout
	column2	= cmds.columnLayout(adj=1)
#	�߹�  ��/��
	cmds.button(l=u'�߹�  ��/��',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnOffEmitSpecular();")')

	cmds.setParent(	'..' )

	cmds.formLayout( form,
			edit=True,
			attachForm=		[
								(column1, 'left', 5), (column1,	'top', 5),
								(column2, 'right', 5),(column2,	'top', 5)
							]
						,
			attachPosition=	[
								(column1, 'right', 5, 50),
								(column2, 'left', 5, 50)
							]
				)
	cmds.setParent(	'..' )

#	����
#	�ƹ��ף���Ӱ���
#	����kiko ר�õ�
#	�������ݿ⣬��ͷ������Ӱ��ɫ
	cmds.button(l=u'����',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_eyeTools();")')
	cmds.button(l=u'�ƹ��ף���Ӱ���',c='mel.eval("source	\\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_TurnBackLightColor();")')
	cmds.button(l=u'����kiko ר�õ�',c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";importKikoLight();")')
	cmds.button(l=u'�������ݿ⣬��ͷ������Ӱ��ɫ',bgc=[1,1,1],c='import	idmt.maya.ROMA.GDC_lights_ShadowColor as GDC_Sc\nreload(GDC_Sc)\nGDC_Sc.ChangeColor()')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )


##zzj  �������ʹ���
	child4 = cmds.columnLayout(adjustableColumn=1)

##zzj	       �����ʹ���
	cmds.frameLayout( label=u'���ʹ���', labelAlign='top')
	cmds.columnLayout()
#	rCLayout
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	ColorR
#	ColorG
#	ColorB
#	Color
#	Matte
	cmds.symbolButton(ann="ColorR",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorR.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorR\\\")")')
	cmds.symbolButton(ann="ColorG",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorG.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorG\\\")")')
	cmds.symbolButton(ann="ColorB",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorB.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorB\\\")")')
	cmds.symbolButton(ann="ColorA",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorA.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"colorA\\\")")')
	cmds.symbolButton(ann="Matte",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\matte.xpm",		c='mel.eval("zzjIDPass_Material_Assign(\\\"matte\\\")")')
	cmds.setParent(	'..' )
#	rCLayout
	cmds.columnLayout()
	cmds.separator(style='out',height=10,w=1000)
	cmds.setParent(	'..' )
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	Depth
#	Shadow
#	AO
#	Lambert
	cmds.symbolButton(ann="Depth",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\depth.bmp",		c='mel.eval("zzjIDPass_Material_Assign(\\\"depth\\\")")')
	cmds.symbolButton(ann="Shadow",	image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\shadow.bmp",	c='mel.eval("zzjIDPass_Material_Assign(\\\"shadow\\\")")')
	cmds.symbolButton(ann="AO",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\AO.bmp",		c='mel.eval("zzjIDPass_Material_Assign(\\\"AO\\\")")')
	cmds.symbolButton(ann="Lambert",	image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\lambert.xpm",	c='mel.eval("zzjIDPass_Material_Assign(\\\"lambert\\\")")')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )
##zzj	       ���û�ר��
	cmds.frameLayout( label=u'�û�ר��', labelAlign='top')
	cmds.columnLayout()
#	rCLayout
	cmds.rowColumnLayout(numberOfRows=1,rh=(1,40))
#	ColorR
#	ColorG
#	ColorB
#	Color
#	Matte
	cmds.symbolButton(ann="ColorR",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorR.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorR")')
	cmds.symbolButton(ann="ColorG",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorG.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorG")')
	cmds.symbolButton(ann="ColorB",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorB.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorB")')
	cmds.symbolButton(ann="ColorA",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\colorA.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("colorA")')
	cmds.symbolButton(ann="Matte",		image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\matte.xpm",		c='import idmt.maya.ROMA.idpass4mm	as idpMM\nreload(idpMM)\nidpMM.FinalAssign("matte")')
	cmds.symbolButton(ann="",  vis=0 ,	 image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\matte.xpm",		 c='')
	cmds.symbolButton(ann=u"MayaMan-Matte",		 image="\\\\file-cluster\\GDC\\Resource\\Support\\Maya\icons\\wxII\\idpass\\matte.xpm",		 c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/rnd_wxII_RenderTools.mel\\\";wxII_selected_MMmatte();")')

	cmds.setParent(	'..' )
	cmds.button(l=u'ͨ��ѡ��Ĳ������polygon��ѡ����Ӧ����',c='import idmt.maya.ROMA.idpass4mm as	idpMM\nreload(idpMM)\nidpMM.selectFace()')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )


	cmds.setParent(	'..' )

##zzj  ��RBW ����
	child5 = cmds.columnLayout(adjustableColumn=1)
##zzj	       ��Setting
	cmds.frameLayout( label='Setting ',	labelAlign='top')
#	Create	Light Rig
#	Create	Hairs Light	Rig
#	Neutralize	Color
#	Create	Occlusion
#	Create	SSS	Shader
	cmds.columnLayout(adjustableColumn=1)
	cmds.button(l='Create Light	Rig',		c='mel.eval("py_createLightRig")')
	cmds.button(l='Create Hairs	Light Rig',	c='mel.eval("py_createHairsLightRig")')
	cmds.button(l='Neutralize Color',		c='mel.eval("py_neutralizeColor")')
	cmds.button(l='Create Occlusion',		c='mel.eval("source \\\"//file-cluster/GDC/Resource/Support/Maya/projects/ROMA/lzyRomaChrOcc.mel\\\";lzyRomaChrOcc();")')
	cmds.button(l='Create SSS Shader',	c='mel.eval("py_createSSSShader")')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )
##zzj	       ��MM	Shader Path
	cmds.frameLayout( label='MM	Shader Path	', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)
	cmds.textField(text=r'\\file-cluster\GDC\Resource\Support\Pixar\Shader',editable=0)

#	��MM�ļ���
#	����·��
	form = cmds.formLayout(numberOfDivisions=100)
	path=r"\\\\file-cluster\\GDC\\Resource\\Support\\Pixar\\Shader"
	b1 = cmds.button(l=u'��MM�ļ���',c='os.startfile(path)')
	b2 = cmds.button(l=u"����·��",	c='import idmt.maya.ROMA.lightingUI as	lUI\nreload(lUI)\nlUI.setClipboard(13,"'+path+'")' )
	cmds.formLayout(form,edit=1,	attachForm=[(b1,'left',0),(b2,'right',0)],	attachPosition=[(b1,'right',0,50),(b2,'left',0,50)])
	cmds.setParent(	'..' )

	cmds.setParent(	'..' )
	cmds.setParent(	'..' )

##zzj	       ��Help
	cmds.frameLayout( label='Help ', labelAlign='top')
	cmds.columnLayout(adjustableColumn=1)
#	����II������־
	cmds.button(l=u'����II������־',c=u'os.startfile(r"\\\\file-cluster\\GDC\\Resource\\Support\\Maya\\Import\\iRender\\RenderInfo\\WinxClubII\\����II����˵��.txt")')
	cmds.setParent(	'..' )
	cmds.setParent(	'..' )

	cmds.setParent(	'..' )

	cmds.tabLayout(	tabs, edit=True, tabLabel=(
										(child1, u'���ù���'),
										(child2, u'Setting'),
										(child3, u'�ƹ⹤��'),
										(child4, u'�����ʹ���'),
										(child5, u'RBW����')
									))
	cmds.window('wxIISetRenderLayerUI',e=1,width=400,height=385)

	cmds.showWindow("wxIISetRenderLayerUI")
