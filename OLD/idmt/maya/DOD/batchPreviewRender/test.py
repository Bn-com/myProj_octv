#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-9-252013

@author: zhangben
'''
import maya.cmds as mc

def saveAsTestFile():
    fileName = mc.file(q=True,sn=True)
    fn_split = os.path.split(fileName)
    
    mc.file(rn=u'%s/re_%s'%(fn_split[0],fn_split[1]))
    mc.file(save=True)


if __name__=="__main__"
    saveAsTestFile()