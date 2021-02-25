#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-10-122013

@author: zhangben
'''
import maya.cmds as mc

def do4_Mb2Ma():
    turtleNodes = mc.ls(u"Turtle*")
    
    for eachNode in turtleNodes:
        mc.lockNode(eachNode,l=False)
        mc.delete(eachNode)
    fileFullName = mc.file(sn=True,shn=True,q=True)
    fileName = fileFullName.split(u'.')[0]
    mc.file(rn=fileName)
    
    if fileFullName.split(u'.')[1] =='mb':
        mc.file(save=True,type = u'mayaAscii')
    elif fileFullName.split(u'.')[1] =='ma':
        mc.file(save=True,type = u'mayaBinary')
    
if __name__ == "__main__":
    do4_Mb2Ma()