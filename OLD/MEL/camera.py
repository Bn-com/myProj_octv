# -*- coding: utf-8 -*-
import maya.mel
def CheckPosition(camera = None):
	rs = True

	if camera == None:
		maya.mel.eval('source "zwCameraImportExport.mel"')
		camera = maya.mel.eval('zwGetCameraEx ""')
	if not maya.cmds.objExists(camera):
		return rs
	cameraName = re.search(r'[^\|]+$', camera).group(0)

	project =  maya.mel.eval('zwGetProject ""')
	max = 15000
					
	translation = maya.cmds.xform(camera, query = True, worldSpace = True, translation = True)
	if abs(translation[0]) > max or abs(translation[1]) > max or abs(translation[2]) > max:
		if maya.cmds.about(batch = True):
			message = u'摄像机离原点过远（>%d），这可能会导致渲染问题，建议往原点靠拢\n%s: %.3f %.3f %.3f\n如有疑问请联系项目TD' % (max, cameraName, translation[0], translation[1], translation[2])
			maya.OpenMaya.MGlobal.displayError(message)
		else:
			message = u'摄像机离原点过远（>%d），这可能会导致渲染问题，建议往原点靠拢\n\n%s: %.3f %.3f %.3f\n\n如有疑问请联系项目TD\n' % (max, cameraName, translation[0], translation[1], translation[2])
			maya.cmds.confirmDialog(message = message, button = ["OK"])
		rs = False

	return rs
