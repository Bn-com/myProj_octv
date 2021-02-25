# -*- coding: utf-8 -*-

'''
Created on 2015

YD  专有工具【YD】

@author: hanhong
'''
import maya.cmds as mc
import maya.mel as mel
class yd_tools(object):
    def __init__(self):

        pass
#相机微动【YD】
#@author: hanhong
#Data：2015/12/08
#----------------------------------------------------------------------------------------------------------#
    def yd_skyKey(self,key=1):
        curs=mc.ls(type='nurbsCurve',l=1)
        skymaster=''
        skyimitate=''
        if curs:
            for cur in curs:
                obj =mc.listRelatives(cur,p=1,f=1)
                if obj and 'Space_EXT_CMU' in obj[0].split('|')[-1] and ':Master' in obj[0].split('|')[-1]:
                    skymaster=obj[0]
                if obj and 'YODA_SKY' in obj[0] and 'Master' in obj[0]:
                    skyimitate=obj[0]
        if skymaster and key==1:
            mc.selectKey((skymaster+'.rotateY'),clear=1)
            mc.currentTime(1001)
            mc.setAttr((skymaster+'.rotateY'),0)
            mc.setKeyframe((skymaster+'.rotateY'),t=1001)
            mc.currentTime(1072)
            mc.setAttr((skymaster+'.rotateY'),-1)
            mc.setKeyframe((skymaster+'.rotateY'),t=1072)
            mc.keyTangent((skymaster+'.rotateY'),itt='linear',ott='linear')
            mc.setInfinity((skymaster+'.rotateY'),poi='cycleRelative')
            print u'================客户天空已微动============'
        if skymaster and key==0:
            mc.cutKey(skymaster+'.rotateY')
            print u'================客户天空微动已删============'
        if skyimitate:
            mc.selectKey((skyimitate+'.rotateY'),clear=1)
            mc.currentTime(1001)
            mc.setAttr((skyimitate+'.rotateY'),0)
            mc.setKeyframe((skyimitate+'.rotateY'),t=1001)
            mc.currentTime(1072)
            mc.setAttr((skyimitate+'.rotateY'),-1)
            mc.setKeyframe((skyimitate+'.rotateY'),t=1072)
            mc.keyTangent((skyimitate+'.rotateY'),itt='linear',ott='linear')
            mc.setInfinity((skyimitate+'.rotateY'),poi='cycleRelative')
            print u'================GDC天空已微动============'
        if skyimitate and key==0:
            mc.cutKey(skyimitate+'.rotateY')
            print u'================GDC天空微动已删============'
        return 0
#导出客户BL相机【YD】
#@author: hanhong
#Data：2015/12/14
#----------------------------------------------------------------------------------------------------------#
    def yd_BLCExr(self,project='YODA',infoType=3):
        shotInfo=mc.file(q=1,shn=1,sn=1).split('_')
        pro=''
        if project=='YODA':
            pro='yd'
        campath='Z:/Projects/'+project+'/'+project+'_Scratch/TD/BLC/'+shotInfo[1]+'/episode_camera/'
        if infoType==3:
            camName=pro+'_'+shotInfo[1]+'_'+shotInfo[2]+'_'+shotInfo[3]+'_cam.ma'
        if infoType==2:
            camName=pro+'_'+shotInfo[1]+'_'+shotInfo[2]+'_cam.ma'
        mc.sysFile(campath, makeDir=True)
        cams=mc.ls(ca=1,l=1)
        camers=[]
        if cams:
            for cam in cams:
                ca=mc.listRelatives(cam, p=1, type='transform', f=1)
                if ca and '_' in ca[0] and shotInfo[2] in ca[0].split('|')[-1] and shotInfo[3] in ca[0].split('|')[-1] :
                    camers.append(ca[0])
        if camers and len(camers)==1:
            mc.select(camers)
            mc.file((campath+camName),options='v=0',f=1,type='mayaAscii',preserveReferences=1,es=1)
            print u'===============已导出相机文件==================='
            print u'===============【%s】========================='%(campath+camName)
        else:
            mc.warning(u'请确认客户BL文件是否正确，请检查相机是唯一')
            mc.error(u'文件中缺少正确相机，或者镜头相机不止一个，请检查文件')
        return 0


