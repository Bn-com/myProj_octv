#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = mayaDeployingProc
__author__ = zhangben 
__mtime__ = 2021/3/16 : 16:27
__description__: 

THEOREM: A good programmer should wipe the butts of his predecessors in an amicable way,
    instead of reinventing a new butt.
        As long as this , code is far away from bugs, and with the god animal protecting
            I love animals. They taste delicious.
"""
import re,os,sys
class DeployProc(object):
    def __init__(self,mayaVerson):
        self.currendDir = os.path.dirname(__file__)
        self.mayaVersion = mayaVerson
        self.userDoc = os.path.join(os.environ['userprofile'],"documents")
        self.mayaDoc = os.path.join(self.userDoc,'maya',self.mayaVersion)
        self._mode = 'new'  #  obsolete default
    @property
    def mode(self):
        return self._mode
    @mode.setter
    def mode(self,mode):
        self._mode = mode
    def run(self):
        if self._mode == 'obsolete':
            self.obsolete_mode()
    def obsolete_mode(self):
        invoke_bat = self._exec_bat()
        # print(invoke_bat)
        import subprocess
        # subprocess.call(invoke_bat)
        p = subprocess.Popen(invoke_bat, stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout, stderr = p.communicate()
        for l in stdout:
            print(l)
        # print p.returncode  # is 0 if success
        # os.system("C:\Windows\System32\cmd.exe /c {}".format(invoke_bat))
        # os.system(invoke_bat)
    def _exec_bat(self):
        return os.path.abspath(os.path.join(self.currendDir,'exec/Maya{}.bat'.format(self.mayaVersion)))