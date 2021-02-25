__author__ = 'xuweijian'
import maya.cmds as mc
def export():
    path= mc.file(q=1,exn=1)
    root= mc.ls(assemblies=True)
    mc.select(root)
    mc.file(path,f=1,options='v=0',typ='mayaAscii',pr=1,es=1)

export()