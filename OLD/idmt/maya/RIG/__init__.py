#-*- coding: utf-8 -*-
import maya.cmds as rig
import os
import maya.mel as MEL


#MEL.eval('source "'+os.path.join(__path__[0],'MEL/curveExport.mel').replace('\\','/')+'"')
#nodePath =  __path__[0]+'/Node/'
#
#for root, dirs, files in os.walk(nodePath):#加载插件
#    for f in files:
#        pluginPath =  os.path.join(root, f)
#        if not rig.pluginInfo(f, query=True, l = True ):
#            rig.loadPlugin(pluginPath)
#        else:
#            rig.unloadPlugin(f, f = True)
#            rig.loadPlugin(pluginPath)
