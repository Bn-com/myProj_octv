# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json
import tempfile



def runMayaBatch(file, command):
    mayabatchLocation = os.path.normpath(os.path.join(os.getenv('MAYA_LOCATION'), 'bin', 'mayabatch.exe'))
    cmd = '%s -command "%s" -file "%s"' %(mayabatchLocation, command, file)
    print cmd
    os.popen(cmd)


def checkoutAsset(desc):
    checkout(1, desc)

def checkoutAnim(desc):
    checkout(2, desc)

def checkout(checkType, desc = ''):
    fielName = mc.file(q = True, sn = True, shn = True)
    temp = os.path.join(tempfile.gettempdir(), fielName)
    mc.file(rename = temp)
    mc.file(save=1, force=1)

    userName = os.environ['USERNAME']
    
    fileInfo = '%d|%s|%s|%s'%(checkType,'XingJiCheShen1', fielName, userName)
    checkOutCmd = 'idmtService \"Checkout\" \"' + fileInfo + '\"'
    mel.eval(checkOutCmd)
    result = mc.idmtProject(checkin = True, description = desc)
    if result:
        print u'\n=== %s Chekcin Finished ===\n' % fielName


