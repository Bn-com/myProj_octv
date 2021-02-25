#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-10-242013

@author: zhangben
'''
import maya.cmds as mc
import re,os

def  zb_del_redundantCam():
    ma_filePath = mc.file(q=True,sn=True)
    
    ma_filePath_shn = os.path.basename(ma_filePath)
    ma_filePath_shn_spl= os.path.splitext(os.path.basename(ma_filePath))[0].split(u'_')
    sq_num = ma_filePath_shn_spl[1]
    shot_num = ma_filePath_shn_spl[2]
    mode = ma_filePath_shn_spl[3]
    ves_numStr = ma_filePath_shn_spl[4]
    sq_shot = u'%s_%s'%(sq_num,shot_num)
    p_cam = re.compile(u'%s$'%sq_shot)
    unusedStereoTrans = [exactCam for exactCam in mc.ls(type = 'stereoRigTransform') if p_cam.search(exactCam) == None]
    for each in unusedStereoTrans:
        print "Now Handle CAM:__%s__"%each
        stereoTransParent = mc.listRelatives(each,p=True,f=True)
        
        if stereoTransParent != None:
            Grp_otherChild = [other_chil for other_chil in mc.listRelatives( stereoTransParent[0],c=True)   if other_chil != each]
            if len(Grp_otherChild) >1 :
                mc.warning(u'Camera [%s] has a SPECIAL PARENT'% each)
                continue
            elif len(Grp_otherChild)==1 and mc.nodeType(Grp_otherChild[0]) != u'parentConstraint' :
                mc.warning(u'Camera [%s] has a SPECIAL PARENT'% each)
                continue
            else:
                mc.delete(stereoTransParent)
                print u'CAM: %s___ DEL!!!!!'
        else:
            mc.delete(each)
            print u'CAM: %s___ DEL!!!!!'
if __name__ == "__main__":
    zb_del_redundantCam()