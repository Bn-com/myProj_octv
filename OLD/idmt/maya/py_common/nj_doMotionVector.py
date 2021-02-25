# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)

class nj_doMotionVector(object):
    def __init__(self):
        pass

    def nj_addMotionVectorPass(self,selectedObjs):
        
        sn = mc.file(q = True, sceneName = True, shortName = True).split('_')
        cams = pm.ls(type = 'camera')
    
        for c in cams:
            result = re.search(sn[1] + '_' + sn[2] + '_' + sn[3], c.name())
            if result:
                if pm.referenceQuery( c,isNodeReferenced=True ):
                    ref = pm.system.FileReference(pm.referenceQuery( c,referenceNode=True ))
                    ref.importContents()
                c.shutterAngle.unlock()        
                c.shutterAngle.set(360)
                c.renderable.set(1)
                c.farClipPlane.set(100000)

            
        motionVectorLayer = mc.createRenderLayer(selectedObjs, name='motionVector', number = 1, noRecurse=True)
        mc.editRenderLayerGlobals(currentRenderLayer=motionVectorLayer)
    
        #mel.eval('optionMenuGrp -edit -sl 1 miKeyframeLocCtrl')
        #mel.eval('miSetKeyframeLocValue()')
        mc.setAttr('mentalrayGlobals.exportMotionOffset', 0)
    
        mc.setAttr('miDefaultOptions.shutterDelay', 0)
        mc.setAttr('miDefaultOptions.shutter', 0)
        
        mv2DToxik = mc.shadingNode('renderPass',asRendering = True,name = 'mv2DToxik')
        mc.setRenderPassType(mv2DToxik,type = 'MV2E')
        mc.setAttr(mv2DToxik + '.passGroupName', 'CGPost', type = 'string')
        mc.connectAttr(motionVectorLayer + '.renderPass', mv2DToxik + '.owner', nextAvailable = True)
        mc.editRenderLayerAdjustment('miDefaultFramebuffer.datatype')
        mc.setAttr('miDefaultFramebuffer.datatype', 16)
        
        mc.editRenderLayerAdjustment('defaultRenderGlobals.imageFormat')
        mc.setAttr('defaultRenderGlobals.imageFormat', 51)
        mc.setAttr('defaultRenderGlobals.imfPluginKey', 'exr', type = 'string')

    def nj_doMotionVectorPassProc(self):
        #mc.setAttr('miDefaultOptions.forceMotionVectors', 1)
        
        #mc.select(all = True)
        selNodes = mc.ls(sl = True)
        if selNodes:
            self.nj_addMotionVectorPass(selNodes)
        else:
            print r'请选择需要添加到MOTION VECTOR PASS的物体'

