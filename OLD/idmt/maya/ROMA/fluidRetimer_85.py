#! /usr/bin/env python
# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import maya.cmds as cmd
import maya.mel as mel

def fluidRetimer():
    sel = cmd.ls(sl=1)
    temp = []
    fluid = []
    fluidShape = []
    if (len(sel) < 1):
        mel.eval('warning ("Please selected a fluid transform or a fluid shape.")')
    else:
        if (cmd.nodeType(sel[0]) == 'transform'):
            temp = cmd.listRelatives(sel[0], s=1)
            if (cmd.nodeType(temp[0]) == 'fluidShape'):
                fluid = sel[0]
                fluidShape = temp[0]
        if (cmd.nodeType(sel[0]) == 'fluidShape'):
            temp = cmd.listRelatives(sel[0], p=1)
            fluid = temp[0]
            fluidShape = sel[0]
        temp = []
        if (cmd.isConnected('time1.outTime', (fluidShape + '.currentTime')) != 1):
            mel.eval(('warning ("It appears there is a different connection to %s .currentTime")' % fluidShape))
            get = cmd.confirmDialog(title=(('Re-Connect ' + fluidShape) + 'to time.outTime'), ma='center', message=(('Do you want to restore the original connections to ' + fluidShape) + '.currentTime'), button=('Yes', 'No'), defaultButton='No')
            if (get == 'Yes'):
                fluidUnretimer(fluid, fluidShape)
            else:
                mel.eval(('print ("Leaving %s alone")' % fluid))
        else:
            if (cmd.attributeQuery('fluidRetime', node=fluid, ex=1) != 1):
                cmd.addAttr(fluid, ln='fluidRetime', at='double')
                cmd.setAttr((fluid + '.fluidRetime'), e=1, keyable=1)
            cmd.disconnectAttr('time1.outTime', (fluidShape + '.currentTime'))
            cmd.connectAttr((fluid + '.fluidRetime'), (fluidShape + '.currentTime'), f=1)
            mel.eval(('print ("Keyframe %s .fluidRetime to animate your fluid!")' % fluid))
    sel = []



def fluidUnretimer(node, shape):
    temp = cmd.listConnections((shape + '.currentTime'), p=1)
    if (len(temp) > 0):
        cmd.disconnectAttr(temp[0], (shape + '.currentTime'))
        cmd.connectAttr('time1.outTime', (shape + '.currentTime'), f=1)


