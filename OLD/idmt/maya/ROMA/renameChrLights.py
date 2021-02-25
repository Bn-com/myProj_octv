# -*- coding: gbk -*-
import maya.mel	as mel
import maya.cmds as	cmds
import os
import re


if __name__=='__main__':
	main()

def	main():
	wxII_chr_Rename_lightUI()


def	rename():
	groupName=cmds.ls(sl=1,l=1)
	if groupName ==	[] or groupName	== None:
		cmds.confirmDialog(	 message=u'请选择chr灯光所在组', button=[u'确认'])
	else:
		groupName= groupName[0].split('|')[1]
		ori_KW=groupName.split('_')[1]


		new_KW=cmds.textField('wxII_chr_Rename_lightTX',q=1,tx=1)
		slGroup=cmds.ls(groupName ,dag=1)
		slGroup.reverse()
		for	a in slGroup:
			temp= re.sub(ori_KW,new_KW,a)
			temp=temp.split('|')[-1]
			cmds.rename(a, temp)

#		setGroup=cmds.ls('SEL_*_lights',type='objectSet')
		setGroup=cmds.ls('SEL_'+ori_KW+'_lights',type='objectSet')
		for	a in setGroup:
			temp= re.sub(ori_KW,new_KW,a)
			temp=temp.split('|')[-1]
			cmds.rename(a, temp)

def	wxII_chr_Rename_lightUI():
	try:
		cmds.deleteUI("wxII_chr_Rename_lightUI")
	except:
		pass
	cmds.window('wxII_chr_Rename_lightUI',title=u"chr灯光重命名",mxb=False)
	cmds.columnLayout(adj=1,rs=5)
	cmds.textField('wxII_chr_Rename_lightTX')
	cmds.button(l=u'重命名',c='import idmt.maya.ROMA.renameChrLights as renameChrLights\nreload(renameChrLights)\nrenameChrLights.rename()')
	cmds.setParent(	'..' )
	cmds.window('wxII_chr_Rename_lightUI',e=1,w=168,h=80,)
	cmds.showWindow('wxII_chr_Rename_lightUI')

