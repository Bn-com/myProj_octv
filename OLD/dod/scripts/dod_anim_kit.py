#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2014-7-302014

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel


class dod_anim_kit(object):

    def __init__(self):
        pass

    def list_all_ctrlCurves(self):
        nurbCurs = mc.ls(type='nurbsCurve')
        curs_p = []
        p_rig = re.compile(u'RIG')
        p_c = re.compile(u'_c[0-9]+[a-zA-Z]+')

        mel.eval(u'source \"zzjUtilityTools.mel\"')

        for each in nurbCurs:
            p_n = mc.listRelatives(each, p=True, f=True, typ="transform")
            if p_n != None and p_rig.search(p_n[0]) != None and p_c.search(p_n[0]) != None and mel.eval(u'nodeIsVisible(\"%s\")' % each):
                keyabelAttr = mc.listAttr(p_n[0], k=True)
                if keyabelAttr != None:
                    curs_p.append(p_n[0])
        return curs_p

    def key_all_ctrlCurves(self):
        all_ctrls = self.list_all_ctrlCurves()
        start_f = mc.playbackOptions(min=True, q=True)
        # mc.currentTime(start_f)
        mc.setKeyframe(all_ctrls, breakdown=0, hierarchy=False, controlPoints=False, shape=False, time=start_f)
        end_f = mc.playbackOptions(max=True, q=True)
        # mc.currentTime(end_f)
        mc.setKeyframe(all_ctrls, breakdown=0, hierarchy=False, controlPoints=False, shape=False, time=end_f)
