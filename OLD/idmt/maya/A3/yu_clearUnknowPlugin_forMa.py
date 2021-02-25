# -*- coding: utf-8 -*-
# 【通用】【清理Maya2016版本以下的Maya工程文件里的未知插件】
#  Author : 虞丰盛
#  Data   : 2018_04

from maya.cmds import *
import maya.mel as mel
import sys
import os
from idmt.maya.commonPerform.projectTools import sk_projTools_ddz
reload(sk_projTools_ddz)


def clearUnknowPlugin():

    sk_projTools_ddz.sk_projTools_ddz().GA_deleteUnknownNodes()
    fileName=file(q=1,sn=1,shn=1)
    scenesPath=workspace(q=1,fn=1)+'/scenes'
    tmpPath=scenesPath+'/tmp'
    if os.path.exists(tmpPath)==False:
        os.makedirs(tmpPath)
    desFileName=tmpPath+'/'+fileName.split('.')[0]+'.ma'
    file(rename=desFileName)
    file(s=1,force=1,type='mayaAscii')
    lines=[]
    with open(desFileName,'r') as f:
        lines=f.readlines()

    with open(desFileName,'w') as f_w:
        for line in lines:
            if 'requires' in line and not('nodeType' in line) and not('dataType' in line) and not('requires maya' in line):
                continue
            f_w.write(line)
        f_w.close()

    file(desFileName,open=1,force=1)
    mbFileName=tmpPath+'/'+fileName.split('.')[0]+'.mb'
    file(rename=mbFileName)
    file(s=1,force=1,type='mayaBinary')
