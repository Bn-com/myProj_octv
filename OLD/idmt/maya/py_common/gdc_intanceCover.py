# -*- coding: utf-8 -*-

'''
Created on 2015-5-16

@author: hanhong
'''

import maya.cmds as mc
import maya.mel as mel


class GDC_InstanceCover(object):
    def __init__(self):
        pass

    
    
    def GDC_InstanceCover(self):
        objselect=mc.ls(sl=1,l=1)
        for obj in objselect:
            xforms=mc.xform(obj, q =1,m=1)
            objn=mc.duplicate (obj,rr=1)
            mc.xform(objn,m=xforms)
            if mc.ls(obj) and mc.ls(objn):
                try:
                    mc.delete(obj)
                    mc.rename(objn,obj)
                except:
                    print u'===有物体无法删除或改名==='
                    print obj
                    print objn
                    mc.error(u'===有物体无法删除或改名===') 
        print u'已将选择物体转化为非Instance物体'           
        return   0           
