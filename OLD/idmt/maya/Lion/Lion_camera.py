__author__ = 'liangyu'
import maya.cmds as mc

def Lion_SetCam():
    cameras=mc.ls(type='camera')
    cams=[]
    cameras.remove('frontShape')
    cameras.remove('perspShape')
    cameras.remove('sideShape')
    cameras.remove('topShape')

    if cameras:
        for cam in cameras:
            if mc.getAttr(cam+'.horizontalFilmAperture')!=1.078:
                mc.setAttr(cam+'.horizontalFilmAperture',1.078)
            if mc.getAttr(cam+'.verticalFilmAperture')!= 0.612:
                mc.setAttr(cam+'.verticalFilmAperture',0.612)
            if mc.getAttr(cam+'.lensSqueezeRatio')!= 1:
                mc.setAttr(cam+'.lensSqueezeRatio',1)

            if mc.getAttr(cam+'.hfa',lock=1)==0:
                mc.setAttr(cam+'.hfa',lock=1)
            if mc.getAttr(cam+'.vfa',lock=1)==0:
                mc.setAttr(cam+'.vfa',lock=1)
            if mc.getAttr(cam+'.lsr',lock=1)==0:
                mc.setAttr(cam+'.lsr',lock=1)
def Lion_CamCheck():
    cameras=mc.ls(type='camera')
    cams=[]
    print 'a'
    cameras.remove('frontShape')
    cameras.remove('perspShape')
    cameras.remove('sideShape')
    cameras.remove('topShape')
    if cameras:
        for cam in cameras:
            if mc.getAttr(cam+'.horizontalFilmAperture')!=1.078:
                mc.warning(u'====%s.horizontalFilmAperture!=1.078,please check===='%cam)
                mc.error(u'====%s.horizontalFilmAperture!=1.078,please check===='%cam)
            if mc.getAttr(cam+'.verticalFilmAperture')!= 0.612:
                mc.warning(u'====%s.verticalFilmAperture!=1.078,please check===='%cam)
                mc.error(u'====%s.verticalFilmAperture!=1.078,please check===='%cam)
            if mc.getAttr(cam+'.lensSqueezeRatio')!= 1:
                mc.warning(u'====%s.lensSqueezeRatio!=1.078,please check===='%cam)
                mc.error(u'====%s.lensSqueezeRatio!=1.078,please check===='%cam)
            if mc.getAttr(cam+'.hfa',lock=1)==0:
                mc.warning(u'====%s.hfa,lock==0,please check===='%cam)
                mc.error(u'====%s.hfa,lock==0,please check===='%cam)
            if mc.getAttr(cam+'.vfa',lock=1)==0:
                mc.warning(u'====%s.vfa,lock==0,please check===='%cam)
                mc.error(u'====%s.vfa,lock==0,please check===='%cam)
            if mc.getAttr(cam+'.lsr',lock=1)==0:
                mc.warning(u'====%s.lsr,lock==0,please check===='%cam)
                mc.error(u'====%s.lsr,lock==0,please check===='%cam)
    return 0
