#-*- coding: utf-8 -*-
__author__ = 'xuweijian'

import idmt.maya.commonCore.core_mayaCommon.sk_infoConfig
import maya.cmds as mc
import maya.mel as mm
import os
import shutil



class uploadGeoCache(object):
	#\\转换为//方法
	def changePathType(self,path):
			pathInfo = []
			newPath = ''
			if '\\' in path:
				pathInfo = path.split('\\')
				for i in range(len(pathInfo)):
					if i == 0:
						newPath = pathInfo[i] + '//'
					else:
						if pathInfo[i]:
							newPath = newPath + pathInfo[i] + '/'
			return newPath

	def geoCache(self):
		#获取本地工程目录并生成geoCache
		filename=mc.file(query=1, exn=1)
		scencePath = os.path.dirname(filename)
		projectPath=os.path.dirname(scencePath)
		cachPath=projectPath +'/cache/geoCache/%s/'%(os.path.basename(filename)).split('.')[0]
		print 'cachPath:' + cachPath
		if os.path.exists(cachPath):
			shutil.rmtree(cachPath)
		mc.sysFile(cachPath, makeDir=1)
		#pythonCachPath=changePathType(cachPath)

		cmd=''
		cmd='doCreateGeometryCache 6 { "2", "1", "5", "OneFilePerFrame", "1", '+'"'+ cachPath + '"'+'  ,"0","","0", "add", "0", "1", "1","0","1","mcc","0" }'
		mm.eval(cmd)

		#由文件名获取服务器路径
		from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
		shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
		serverPath=''
		if len(shotInfos)>4 :
		#    localPath='D:/Info_Temp/gcash'
		#    mc.sysFile(localPath, makeDir=1)
			serverPath='\\\\file-cluster\GDC\Projects\ToothFairies\Project\data' + '\episode_' + shotInfos[1] + '\sequence_' + shotInfos[2] + '\scene_' + shotInfos[3] + '\geoCache'
			print serverPath
			print shotInfos

		#上传
			files=os.listdir(cachPath)
			for f in files:
				print f
				cmd=''
				cmd='zwSysFile("copy","%s","%s",1)'%(cachPath + f,self.changePathType(serverPath) + f)
				print cmd
				mm.eval(cmd)
