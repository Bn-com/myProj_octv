#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'proK_run'
__author__ = zhangben
__mtime__ = 2018/12/10:17:54
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''


sys.stdin = maya.app.baseUI.StandardInput()
# Replace sys.stdout and sys.stderr with versions that can output to Maya's
# GUI
sys.stdout = maya.utils.Output()
sys.stderr = maya.utils.Output( error=1 )



import maya.cmds as mc

import pymel.core as pm