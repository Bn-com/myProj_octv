# -*- coding: utf-8 -*-
import os
import shutil
import ctypes

def copyEnvFile():
    houdiniEnvPath=os.getenv("HOMEDRIVE")+os.getenv("HOMEPATH")+r'\Documents\houdini15.5'
    if os.path.exists(houdiniEnvPath)==1:
        shutil.copy(r'\\file-cluster\GDC\Resource\Development\Maya\GDC\Plug\Python\GDC\Houdini\Houdini15.5\env\houdini.env'
                    ,houdiniEnvPath+'\houdini.env')
        ctypes.windll.user32.MessageBoxW(0, u'已经配置完成', u'警告', 64)
    else:
        ctypes.windll.user32.MessageBoxW(0, u'配置未完成', u'警告', 64)

if __name__ == "__main__":
    copyEnvFile()
