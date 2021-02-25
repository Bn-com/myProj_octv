#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Title:file_name

Created on 2014年10月22日

@author: zhangben

@Description:todo
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
from pymel.core import *
class dod_common_proc(object):
    def __init__(self):
        pass
    def setAll2RTNS(self):#=====set all obj to root namespace===================================
        namespace(set = ":")
        nsps = namespaceInfo(lon=True)
        for each in nsps:
            if each not in [u'UI',u'shared']:
                namespace(force=True,mv = (each,u':'))
                Namespace(each).remove()
    def sync_node_attr(self,sourceNode,targetNode,attr_matchStr):#========同步两个节点的某些属性，参数attr_matchStr支持通配符 “ * ”===========
        #attr_matchStr = u'ai*'
        #allAttr = listAttr(sh_node,string = u'ai*')
        #targetNode,sourceNode,eachAttr = sh_def_node,sh_node,allAttr[23]
        list_specAttr = listAttr(sourceNode,string = attr_matchStr)
        for eachAttr in list_specAttr:
            if targetNode.hasAttr(eachAttr):
                try:
                    #print u'++++++++++++++++++Synchronization attribute %s +++++++++++++++++++++++'%eachAttr
                    sync_attr_str = u'PyNode(\'%s\').%s.set(PyNode(\'%s\').%s.get())'%(targetNode,eachAttr,sourceNode,eachAttr)
                    exec(sync_attr_str)
                except:
                    #print u'====================ATTRIBUTE %s is not a simple value attribute' % eachAttr
                    pass 