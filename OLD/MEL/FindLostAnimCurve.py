# -*- coding: gbk -*-
import re
import sys
import maya.cmds as cmds

if __name__=='__main__':
	UI()

class FindLostAnimCurveCLS:
	AnimCurveList=[]
	AnimCurveList_NoRepeat=[]
	RedString = ''
	try:
		RedString = cmds.text('PlutoFindLostAnimCurveRedText',q=1,l=1)
	except:
		pass
	RedNamespace=''
	if RedString.find(':')!=-1:
		RedNamespace = re.findall('.+:',RedString)[0][:-1]

	def returnSlContrlText(self):
		keyword = cmds.textFieldButtonGrp('PlutoFindLostAnimCurve_KeyWord',q=1,tx=1)
		if keyword != 'None':
			kw_list=keyword.split(' ')

			animCurve=cmds.ls(type='animCurve')
			matchedCurveName=animCurve

			for kw in kw_list:
				tmp=[]
				for mc in matchedCurveName:
					if mc.find(kw)!=-1:
						tmp.append(mc)
				matchedCurveName=tmp


			self.AnimCurveList=matchedCurveName

			for a in matchedCurveName:
				tmp=re.findall('.+_',a)[0][:-1]
				self.AnimCurveList_NoRepeat.append(tmp)

			self.AnimCurveList_NoRepeat = list(set(self.AnimCurveList_NoRepeat))
#	===============排序=================
			tmp=self.AnimCurveList_NoRepeat
			tmp.sort()
			self.AnimCurveList_NoRepeat=tmp

			tmp=self.AnimCurveList
			tmp.sort()
			self.AnimCurveList = tmp
#	===============排序=================
			self.changeAnimCurveList()

	def changeAnimCurveList(self):
		dis_Attr=cmds.checkBox('PlutoFindLostAnimCurveList_DisAttr',q=1,v=1)
		AnimCurve_List=[]
		if dis_Attr==1:
			AnimCurve_List=self.AnimCurveList
		else:
			AnimCurve_List=self.AnimCurveList_NoRepeat


		if AnimCurve_List==[]:
			AnimCurve_List=[' ']
		cmds.textScrollList('PlutoFindLostAnimCurveList', e=1,removeAll=1, append=AnimCurve_List,selectIndexedItem = 1, )

	def fillInText(self):
		si = cmds.textScrollList('PlutoFindLostAnimCurveList', q=1,selectItem=1 )[0]
		cmds.text('PlutoFindLostAnimCurveBlueText',e=1,l=si,)
		if si!=' ':
			autoFillIn()

	def autoFillIn(self):
		AC=cmds.text('PlutoFindLostAnimCurveBlueText',q=1,l=1,)
		OBJ=cmds.text('PlutoFindLostAnimCurveRedText',q=1,l=1,)
		Connect_resemble = cmds.checkBox('PlutoFindLostAnimCurveList_ConnectResemble',q=1,v=1)
		if Connect_resemble==1:
			if AC.find(':')!=-1:
				AC=re.findall('.+:',AC)[0][:-1]
				AC+=':*'
			else:
				AC+='*'
			if OBJ.find(':')!=-1:
				OBJ=re.findall('.+:',OBJ)[0][:-1]
				OBJ+=':*'
			else:
				OBJ+='*'
		else:
			AC+='*'

		cmds.textFieldGrp('PlutoFindLostAnimCurve_AC',e=1,tx=AC)
		cmds.textFieldGrp('PlutoFindLostAnimCurve_OBJ',e=1,tx=OBJ)

	def connectCMD(self):
		AC=cmds.textFieldGrp('PlutoFindLostAnimCurve_AC',q=1,tx=1,)
		OBJ=cmds.textFieldGrp('PlutoFindLostAnimCurve_OBJ',q=1,tx=1,)

		AC_List=cmds.ls(AC,type='animCurve',)
		final_AC_list=[]
		dic={}

		for a in AC_List:
			if not 47<ord(a[-1])<58:
				final_AC_list.append(a)
			else:
				no_d=a[:-1]
				if 47<ord(no_d[-1])<58:
					no_d=no_d[:-1]
				d= int(a.split(no_d)[-1])
				if dic.keys().count(no_d):
					if d > dic[no_d]:
						dic.update({no_d:d})
				else:
					dic.update({no_d:d})

		for a in dic:
			final_AC_list.append(a+str(dic[a]))
			try:
				final_AC_list.remove(a)
			except:
				pass
#		print final_AC_list

		for ac in final_AC_list:
			obj=ac

			if 47<ord(obj[-1])<58:
				obj=obj[:-1]
				if 47<ord(obj[-1])<58:
					obj=obj[:-1]
			if obj.find('_')!=-1:

				obj_pri=re.findall('.+_',obj)[0][:-1]
				obj_ext=obj.split('_')[-1]
				obj=obj_pri+'.'+obj_ext
				print 'xxxxx'
				print obj_pri
				print 'xxxxx'
			if OBJ.find(':')!=-1:
				obj_pri=re.findall('.+:',OBJ)[0][:-1]
				obj_ext=obj.split(':')[-1]
				obj= obj_pri+':'+obj_ext


			print ac
			print '==========================>'
			print obj
			try:
				cmds.connectAttr(ac+'.output',obj,force=1,)
				print 'Done'
			except:
				print 'Failed'
				pass



#	=====================================CMD===================================
def connect():
	f=FindLostAnimCurveCLS()
	f.connectCMD()

def findMatchCurve():
	f=FindLostAnimCurveCLS()
	f.returnSlContrlText()

def fillInBuluText():
	f=FindLostAnimCurveCLS()
	f.fillInText()

def autoFillIn():
	f=FindLostAnimCurveCLS()
	f.autoFillIn()

#	============================================================================

def UI():
	try:
		cmds.deleteUI("FindLostAnimCurve")
	except:
		pass
	window = cmds.window("FindLostAnimCurve")


	paneLayout = cmds.paneLayout( configuration='vertical2' ,paneSize=[1,45,1])
#	===============================左边==============================================
	form_left = cmds.formLayout(numberOfDivisions=100)

	columnName_l=cmds.columnLayout(adj=1)
	cmds.text(l=u"选择的  \"控制器\物体\"  名称:", align='left',)
	cmds.separator(height=6,style="none")
	lsName=cmds.ls(sl=1)
	if lsName!=None and lsName!=[]:
		lsName=lsName[0]
	else:
		cmds.confirmDialog( title='Confirm', message=u'请选择控制器或者物体', button=['OK',], defaultButton='Yes', )
	cmds.text('PlutoFindLostAnimCurveRedText',l=lsName,font='boldLabelFont', align='center',bgc=[1,0,.5])

	cmds.text(l=u"匹配的动画曲线:", align='left',)
	cmds.text('PlutoFindLostAnimCurveBlueText',l='',font='boldLabelFont', align='center',bgc=[.3,.5,1])

	cmds.separator(height=20,style="double")

	cmds.textFieldGrp('PlutoFindLostAnimCurve_AC',tx='',l=u'动画曲线:',bgc=[.3,.5,1],columnAttach=[1,'right',0],cw=[1,60],adj=2)

	cmds.text(l=u'====>',font='boldLabelFont', align='left',)

	cmds.textFieldGrp('PlutoFindLostAnimCurve_OBJ',l=u'连接到:',bgc=[1,0,.5],columnAttach=[1,'right',0],cw=[1,60],adj=2)

	cmds.separator(height=20,style="double")

	cmds.setParent('..')

	form_button = cmds.formLayout(numberOfDivisions=100)

	button_connect=cmds.button(l=u"连接",c='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.connect()')
	cmds.setParent('..')

	cmds.formLayout( form_button, edit=True,
				attachForm =	[
									(button_connect, 'top', 5),(button_connect, 'left', 5),
									(button_connect, 'right', 5),(button_connect, 'bottom', 5)
								] ,
					)
	cmds.setParent('..')

	cmds.formLayout( form_left , edit=True,
				attachForm =	[
									(columnName_l, 'top', 5), (columnName_l, 'left', 5),(columnName_l, 'right', 5),
									(form_button, 'left', 5), (form_button, 'bottom', 5),
								] ,
				attachControl =	[
									(form_button, 'top', 5, columnName_l),
								] ,
				attachPosition=	[
									(form_button, 'right', 5, 100),
								]
					)
#	===============================右边==============================================
	form_right = cmds.formLayout(numberOfDivisions=100)

	columnName_r=cmds.columnLayout(adj=1)
	cmds.text(l=u"请输入关键字:", align='left',)

	cmds.separator(height=3,style="none")

	lsName=cmds.ls(sl=1)
	if lsName!=None and lsName!=[]:
		lsName=lsName[0].split(':')[-1]

	cmds.textFieldButtonGrp ('PlutoFindLostAnimCurve_KeyWord',tx=lsName,bl=u' 搜索动画曲线 ',adj=1 , columnWidth2=[1,89],
	cc='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.findMatchCurve()',
	bc='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.findMatchCurve()')


	cmds.separator(height=15,style="double")
	cmds.text(l=u'动画曲线列表  (请选择其中一个)：',align='left',)
	cmds.textScrollList('PlutoFindLostAnimCurveList', numberOfRows=6, allowMultiSelection = 0,
			append=[' '],selectIndexedItem = 1,sc='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.fillInBuluText()')

	cmds.separator(height=20,style="double")

	cmds.setParent('..')


	shelfLayout_box=cmds.shelfLayout(cellWidthHeight=[120,15])

	cmds.checkBox('PlutoFindLostAnimCurveList_ConnectResemble',l=u'连接相似的',value=1,cc='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.fillInBuluText()')
	cmds.checkBox('PlutoFindLostAnimCurveList_DisAttr',l=u'显示属性',cc='import IDMT.Pluto.FindLostAnimCurve as FLAC\nreload(FLAC)\nFLAC.findMatchCurve()')
	cmds.checkBox(l=u'长名',en=0)


	cmds.setParent('..')

	cmds.formLayout( form_right , edit=True,
				attachForm=	[
								(columnName_r, 'top', 5), (columnName_r, 'left', 5),(columnName_r, 'right', 5),
								(shelfLayout_box, 'left', 1), (shelfLayout_box, 'right', 1),(shelfLayout_box, 'bottom', 1),
							],
				attachControl =	[
									(shelfLayout_box, 'top', 1, columnName_r),
								] ,
					)
#	=================================================================

	cmds.window(window,e=1,w=720,h=260,t=u'FindLostAnimCurve——001a by zzj')
	cmds.showWindow( window )

