#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-10-29

@author: zhangben
'''
import maya.cmds as mc
import maya.mel as mel
import re
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp


def do4_config_rnd_parameter():
    if not mc.file(sn=True, shn=True, q=True).find(u'Arn') > -1:
        mel.eval("source \"channelBoxCommand.mel\"")
        mel.eval("miLoadMayatomr()")
        mel.eval("miCreateDefaultNodes()")
        mc.setAttr(u"defaultRenderGlobals.currentRenderer", u"mentalRay", type=u'string')
        mel.eval("mentalrayUI \"\"")
        mel.eval("zwQueryCameraTime \"defaultRenderGlobals\"")
        startFrame = mc.getAttr("defaultRenderGlobals.startFrame")
        endFrame = mc.getAttr("defaultRenderGlobals.endFrame")
        mc.playbackOptions(min=startFrame)
        mc.playbackOptions(max=endFrame)
        docp.config_shotFile_cameraParameter()
        execfile('//file-cluster/gdc/Resource/Support/Maya/projects/DODIII/do3_setFacialControlSecondOn.py')
        # zzjSetMentalrayQuality("production"))
        mc.setAttr(u"miDefaultOptions.rayTracing", 1)
        mc.setAttr(u"miDefaultOptions.globalIllum", 0)
        mc.setAttr(u"miDefaultOptions.maxReflectionRays", 1)
        mc.setAttr(u"miDefaultOptions.maxRefractionRays", 1)
        mc.setAttr(u"miDefaultOptions.maxRayDepth", 1)
        mc.setAttr(u"miDefaultOptions.maxShadowRayDepth", 2)
        mc.setAttr(u"miDefaultOptions.scanline", 1)
        mc.setAttr(u"miDefaultOptions.faces", 2)
        mc.setAttr(u"miDefaultOptions.shadowMethod", 1)
        mc.setAttr(u"miDefaultOptions.shadowMaps", 1)
        mc.setAttr(u"miDefaultOptions.biasShadowMaps", 0)
        mc.setAttr(u"miDefaultOptions.traceShadowMaps", 0)
        mc.setAttr(u"miDefaultOptions.windowShadowMaps", 0)
        mc.setAttr(u"miDefaultOptions.motionBlurShadowMaps", 1)
        mc.setAttr(u"miDefaultOptions.rebuildShadowMaps", 2)
        mc.setAttr(u"miDefaultOptions.motionBlur", 0)
        mc.setAttr(u"miDefaultOptions.caustics", 0)
        mc.setAttr(u"miDefaultOptions.finalGather", 0)
        mc.setAttr(u"miDefaultOptions.contrastR", 0.1)
        mc.setAttr(u"miDefaultOptions.contrastG", 0.1)
        mc.setAttr(u"miDefaultOptions.contrastB", 0.1)
        mc.setAttr(u"miDefaultOptions.contrastA", 0.1)
        mc.setAttr(u"miDefaultOptions.minSamples", 0)
        mc.setAttr(u"miDefaultOptions.maxSamples", 2)
        mc.setAttr(u"miDefaultOptions.sampleLock", 1)
        mc.setAttr(u"miDefaultOptions.jitter", 0)
        mc.setAttr(u"miDefaultOptions.filter", 2)
        mc.setAttr(u"miDefaultOptions.volumeSamples", 1)
    # new,add==============================
        mc.setAttr(u"miDefaultFramebuffer.datatype", 2)
        mc.setAttr(u"defaultRenderGlobals.imageFormat", 7)
        # mc.setAttr(mentalrayGlobals.accelerationMethod,0)
        # mc.setAttr(u"mentalrayGlobals.bspSize",20)
        # mc.setAttr(u"mentalrayGlobals.bspDepth",60)
        mc.setAttr(u"defaultRenderLayer.renderable", 0)
        mc.setAttr(u'defaultRenderGlobals.preMel', "cycleCheck -e off", type="string")
        # mc.cycleCheck(e=False)
        docp.rp_zPath2FileCluster()
        docp.del_unknownNodes()
    else:
        pass

if __name__ == "__main__":
    do4_config_rnd_parameter()
