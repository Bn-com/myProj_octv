__author__ = 'xuweijian'
import maya.cmds as mc
import sys

class xwjProcessWindow(object):
	def makeProcessWindow(self):
		mc.progressWindow(title='Waiting',progress=0,isInterruptable=True )

	def stateProcessWindow(self,index,amount):
		sign = False
		if mc.progressWindow( query=True, isCancelled=True ):
			sign = True
			mc.progressWindow(endProgress=1)
			sys.exit()
		if index >= amount :
			mc.progressWindow(endProgress=1)
			#sys.exit()
		processStatus= float(index)/float(amount) *100
		print 'status:' + str(int(processStatus))

		mc.progressWindow( edit=True, progress=int(processStatus) )

		return sign

	def endProcessWindow(self):
		mc.progressWindow(endProgress=1)
		sys.exit()