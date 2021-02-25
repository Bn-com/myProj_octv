#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-11-152013

@author: zhangben
'''
import maya.cmds as mc

def shift_allKeyframe(currentStart,newStart):
    mc.select(mc.ls(type="animCurve"))
    mc.selectKey()
    cst = int(currentStart)
    nst = int(newStart)
    mc.keyframe(animation="keys", option ="over",relative=True,timeChange = (nst - cst))
    mc.file(save=True)

if __name__ == "__main__":
    pass