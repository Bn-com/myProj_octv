# -*- coding: utf-8 -*-
import sys
import os
import re
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import mtoa
import mtoa.cmds.registerArnoldRenderer


import tiBase as tiBase
reload(tiBase)

import tiRender as tiRender
reload(tiRender)

def xjcs():

    if not mc.pluginInfo('mtoa.mll', q = True, loaded = True):
        mc.loadPlugin('mtoa.mll')

    mtoa.core.createOptions()
    mtoa.cmds.registerArnoldRenderer.registerArnoldRenderer()

    tiBase.deleteTurtleNodes()
    tiBase.deleteNodesByType('unknownDag')
    tiBase.deleteNodesByType('unknown')


    mc.setAttr('defaultArnoldRenderOptions.autotx', 0)

    mc.currentUnit(linear = 'cm')
    mc.currentUnit(time = 'pal')

    tiBase.changeImageFileToDollarPath()
    # tiRender.xjcsDefaultRenderSettings()
    print '\nDo the xjcs scene open job......\n'
    sys.__stdout__.write('\nDo the xjcs scene open job......\n')
    