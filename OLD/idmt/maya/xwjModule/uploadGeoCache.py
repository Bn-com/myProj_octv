#-*- coding: utf-8 -*-
__author__ = 'xuweijian'

import idmt.maya.commonCore.core_mayaCommon.sk_infoConfig
import maya.cmds as mc
import maya.mel as mm
import os
import shutil
import thread



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

	def creatGeoCache(self):
		try:
			#获取本地工程目录并生成geoCache
			filename=mc.file(query=1, exn=1)
			scencePath = os.path.dirname(filename)
			projectPath=os.path.dirname(scencePath)
			cachPath=projectPath +'/cache/geoCache/%s/'%(os.path.basename(filename)).split('.')[0]
			print 'cachPath:' + cachPath
			if os.path.exists(cachPath):
				shutil.rmtree(cachPath)
			print '1--------%s'%cachPath
			mc.sysFile(cachPath, makeDir=1)
			print '2----------'
			#pythonCachPath=changePathType(cachPath)
			childrenMesh=mc.ls( mc.listRelatives(mc.ls(sl=1),ad=1,typ='mesh',f=1),ni=1)
			if childrenMesh !=[]:
				mc.select(childrenMesh,add=1)
			cmd=''
			cmd='doCreateGeometryCache 6 { "2", "1", "10", "OneFilePerFrame", "1", '+'"'+ cachPath + '"'+'  ,"0","","0", "add", "0", "1", "1","0","1","mcc","0" }'
			print cmd
			mm.eval(cmd)
			self.uploadGeoCache(cachPath)
		except Exception,e:
			print 'error in creatGeoCache'
			print Exception,":",e
			#thread.start_new_thread(pr,())
		#finally:
			#self.uploadGeoCache(cachPath)
			#print 'cachPath:%s'%cachPath
			#thread.start_new_thread(self.uploadGeoCache,(cachPath))
			#thread.start_new_thread(self.test,())
		#except:
			#print "Error: unable to start thread"
		#thread.exit()


	def uploadGeoCache(self,cachPath):
		try:
			#print '1----------'
			import idmt.maya.xwjModule.xwjProcessWindow as pw
			reload(pw)

			from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
			shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
			serverPath=''
			#print '2-------------'
			if len(shotInfos)>4 :
			#    localPath='D:/Info_Temp/gcash'
			#    mc.sysFile(localPath, makeDir=1)
				serverPath='\\\\file-cluster\GDC\Projects\ToothFairies\Project\data' + '\episode_' + shotInfos[1] + '\sequence_' + shotInfos[2] + '\scene_' + shotInfos[3] + '\geoCache'
				print serverPath
				print shotInfos

			#上传
				files=os.listdir(cachPath)
				print files
				i=0
				pw.xwjProcessWindow().makeProcessWindow()
				for f in files:
					print f
					cmd=''
					cmd='zwSysFile("copy","%s","%s",1)'%(cachPath + f,self.changePathType(serverPath) + f)
					print cmd
					mm.eval(cmd)
					if pw.xwjProcessWindow().stateProcessWindow(i,len(files)-1):
						break
					i=i+1
		except Exception,e:
			print Exception,":",e


	def test(self):
		print 'test---------'