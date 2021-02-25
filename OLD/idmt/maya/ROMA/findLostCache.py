import maya.mel as mel
import maya.cmds as cmds
import string
from maya.cmds import *
def fLC(type=1):
	transforms=ls(sl=1,type='transform')
	if transforms!=None and transforms!=[]:
		
		#----------------progressing win
		progressWin = window(title = "processing")
		columnLayout(adj = True)
		pointsNum = len(transforms)
		progressControl = progressBar(maxValue = pointsNum, width=300)
		setParent("..")
		showWindow( progressWin )
		#---------------- progressing win
		
		for trans in transforms:
			path=''
			meshs = ls(trans,type='mesh',dag=1)
			for m in meshs:
				his=listHistory(m)
				for h in his:
					if nodeType(h)=='cacheFile':
						path=getAttr(h+'.cachePath')+'\/' +getAttr(h+'.cacheName')+'.xml'
						break

			for m in meshs:
				setAttr((m+".intermediateObject"),1)

			if type==1:
				for m in meshs:
					if 'Shape' in m and 'Deformed' not in m and 'Orig' not in m:
						setAttr((m+".intermediateObject"),0)
						break
			if type==2:
				for m in meshs:
					if 'Shape' in m and 'Deformed' in m:
						setAttr((m+".intermediateObject"),0)
						break
			if type==3:
				for m in meshs:
					if 'Shape' in m and 'Orig' in m:
						setAttr((m+".intermediateObject"),0)
						break

			select(trans)
			mel.eval('source "D:/Alias/MAYA8.5/2013/others/doImportCacheArgList.mel"')
			cmd='importCacheFile '+'\"'+path+'\"'+' \"xml\"'
#			print cmd
			try:
				mel.eval(cmd)
			except:
				pass
			
			progressBar(progressControl, edit=True, step=1)
		deleteUI(progressWin)


#	importCacheFile "//Serverone/CONTENT_4_GLOBAL/PRJ_winxII/SHOT_winxII/SQ_050/winxII_sq_050_sc_017/data/cache/characters/skyRoyalKing/MSH/skyRoyalKing_MSH.xml" "xml";