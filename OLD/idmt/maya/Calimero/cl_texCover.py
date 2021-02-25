# -*- coding: utf-8 -*-
'''
Created on 2014-8-20

@author: hanhong
'''
import os
import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
class cl_toolsAdd(object):
    def __init__(self):
        # namespace清理
        pass
#将选择Tex 转为map格式，并设置为椭圆过滤（解决闪动问题）        
    def cl_mapcover(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        files=mc.ls(sl=1,type='file')
        for node in files:
            path = mc.getAttr(node + '.fileTextureName')
            shortname=path.split('/')[-1].split('.')[0]
            texname=path.replace('${IDMT_PROJECTS}','//file-cluster/gdc/Projects')
            format = path.split('.')[-1]
            newtexpath='D:/Info_Temp/texCover/'+shotInfos[1]+'/'+shotInfos[2]+'/'
            projectpath='//file-cluster/gdc/Projects/Ninjago/Project/sourceimages/map/'+shotInfos[1]+'/'+shotInfos[2]+'/'
            newtexname=newtexpath+shortname+'.map'
            projectname=projectpath+shortname+'.map'
            netmap='//idmt-files/share/scenes/Cloud/Renderbus_update/NJ/sourceimages/map'+shotInfos[1]+'/'+shotInfos[2]+'/'+shortname+'.map'
            # 小写化
            if format.lower() in [ 'tga','iff']:
                if shotInfos[0] not in ['nj']:
                    mc.sysFile(newtexpath, makeDir=True)
                    mel.eval('source \"zwImgcvt\"')
                    mel.eval('zwImgcvt \"' + texname + '\" \"' + newtexname + '\"') 
                    mc.setAttr((node + '.fileTextureName'),newtexname,type="string")
                    mc.setAttr((node + '.filterType'),1)
                    mc.setAttr((node + '.miOverrideConvertToOptim'),1)
                    mc.setAttr((node + '.miUseEllipticalFilter'),1)
                    mc.setAttr((node + '.miConvertToOptim'),1)
                else:
                    mc.sysFile(newtexpath, makeDir=True)
                    mel.eval('source \"zwImgcvt\"')
                    mel.eval('zwImgcvt \"' + texname + '\" \"' + newtexname + '\"') 
                    mel.eval('source \"zwSysFile\"')
                    mel.eval('zwSysFile "copy" \"' + newtexname + '\" \"' + projectname + '\" 1') 
                    mel.eval('zwSysFile "copy" \"' + newtexname + '\" \"' + netmap + '\" 1')                       
                    mc.setAttr((node + '.fileTextureName'),projectname,type="string")
                    mc.setAttr((node + '.filterType'),1)
                    mc.setAttr((node + '.miOverrideConvertToOptim'),1)
                    mc.setAttr((node + '.miUseEllipticalFilter'),1)
                    mc.setAttr((node + '.miConvertToOptim'),1)
                    mc.sysFile(newtexname,delete=1) 
                    
                print(u'=====================【转换】完毕=====================')
            
            

            
        
            
            
            
         
