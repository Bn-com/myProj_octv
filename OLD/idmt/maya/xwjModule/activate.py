__author__ = 'sunliansheng'


import maya.cmds as mc

def active():
    scripts = mc.ls( type='script' )
    for script in scripts:
        if "Mxg_dagMenuProc" in script:
            mc.scriptNode(script, executeBefore=True )

active()