# -*- coding: utf-8 -*-

'''
Created on 2015

GDC 相机相关工具【通用】

@author: hanhong

Data   : 2015_12_17
'''

# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import idmt.pipeline.db
import os
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
import sys

#----------------------------------------------------------------------------------------------------------#     
#GDC 相机相关工具【通用】
#@author: hanhong
#Data：2015/12/17
#----------------------------------------------------------------------------------------------------------#    
class GDC_CamTools(object):
    def __init__(self,pro='nj'):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        if pro=='nj':
            self.projectInfo='Ninjago'
            self.campath="//file-cluster/GDC/Projects/" + self.projectInfo + "/" + self.projectInfo + "_Scratch/Animation/Cam/" + shotInfo[1] + "/"+shotInfo[2] + "/"
            self.camServerBasePath =  "//file-cluster/GDC/Projects/" + self.projectInfo + "/Project/scenes/Animation/episode_" + shotInfo[1] + "/episode_camera/"
            self.EPNum=['Clancy','Duobloon','Flintlocke','Intro']
            self.user=['hanhong','xuguojia']
            self.width=720
            self.height=505
            self.soundpath='Z:/Projects/Ninjago/Ninjago_scratch/Animation/HalloweenSpecial/mov/'
#----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------#
#GDC 导出相机【通用】
#@author: hanhong
#Data：2015/12/17
#sl为1，是选择状态；sl为0,是非选择状态
#server为1，上传数据库，server为零不上传
#----------------------------------------------------------------------------------------------------------#
    def GDC_CamExr(self,sl=0,server=1,infotype=3):
        shotInfo=sk_infoConfig.sk_infoConfig().checkShotInfo()
        campath=self.campath
        mc.sysFile(campath, makeDir=True)
        camServerBasePath=self.camServerBasePath
        EP=''
        if infotype==2:
            EP=shotInfo[1]
        if infotype==3:
            EP=shotInfo[1]+'_'+shotInfo[2]
        objs=[]
        if sl==1:
            cams=mc.ls(sl=1,l=1)
            for ca in cams:
                cam=mc.listRelatives(ca,s=1,f=1,type = 'camera')
                if cam and 'cam_' in ca.split('|')[-1] and  shotInfo[1] in ca.split('|')[-1] and shotInfo[2] in ca.split('|')[-1]:
                    objs.append(ca)

        if sl==0:
            cams=mc.ls(ca=1,l=1)
            for ca in cams:
                cam=mc.listRelatives(ca,p=1,f=1)
                if cam and 'cam_' in ca.split('|')[-1] and  shotInfo[1] in ca.split('|')[-1] and shotInfo[2] in ca.split('|')[-1]:
                    objs.append(cam[0])
        if objs:
            for i in range(len(objs)):
                filename=EP+objs[i].slipt('_')[-1]
                filename=objs[i].slipt('_'）
                cambake=objs[i]+'_baked'
                mc.select(objs[i])
                mel.eval('source \"//file-cluster/GDC/Resource/Support/Maya/2013/zwCameraImportExport.mel\"')
                mel.eval('zwBakeCamera')
                mc.select(cambake)
                mc.file(campath + "/" + CamName_validCharactor + ".ma", type="mayaAscii", pr=1, es=1,force = 1))



