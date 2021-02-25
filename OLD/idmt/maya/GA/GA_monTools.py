# -*- coding: utf-8 -*-

'''
Created on 2017-11-24

@author:
'''
import maya.cmds as mc
import sys
import os
os.environ['ANIPIPE_TOOLS_LOC']='C:/tools/LocalTools/tools'

sys.path.append( os.path.join(os.environ['ANIPIPE_TOOLS_LOC'], 'anipipe') )
#sys.path.append('C:/tools/LocalTools/tools/anipipe')
#sys.path.append('C:/tools/LocalTools/tools/anipipe/v1.0')
import setupAniPipe
import aniPipeMaya.model.publish as mdlPub
reload (mdlPub)
class GA_monTools(object):
    def __init__(self):
        pass

    #-------------#
    # 【mon项】模型检测打包
    #
    #-------------#
    def mon_modCheck(self):
        mdlPub.main()
    def mon_unknownNodesDel(self):
        unknownNodes = mc.ls(type='unknown')
        if unknownNodes:
            for node in unknownNodes:
                if mc.ls(node):
                    mc.lockNode(node, l=0)
                    mc.delete(node)
            print u'已删除unknown节点'
        return 0