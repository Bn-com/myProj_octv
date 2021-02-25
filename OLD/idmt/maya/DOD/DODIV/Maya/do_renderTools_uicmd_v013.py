#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-72013

@author: zhangben
'''
import maya.cmds as mc
import re,os
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp

def saveAsFile_btcmd():
    turtleNodes = mc.ls(u"Turtle*")
    
    for eachNode in turtleNodes:
        mc.lockNode(eachNode,l=False)
        mc.delete(eachNode)
    
    file_savePath = u'%s/scenes' %mc.workspace(q=True,fn=True)
    f_inf = docp.getShotInformation()
    
    new_fileName = "%s/%s_%s_%s_lr_%03d%s"%(file_savePath,f_inf[u'project_abbr'],f_inf[u'sq_num'],f_inf[u'sc_num'],001,f_inf[u'type'])
    
    mc.file(rn=new_fileName)
    mc.file(save=True,force=True,type=u'mayaAscii')




    
if __name__ == "__main__":
    pass