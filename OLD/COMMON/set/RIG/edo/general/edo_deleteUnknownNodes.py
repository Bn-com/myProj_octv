import maya.cmds as cmds
def edo_deleteUnknownNodes():
    unknow=cmds.ls(type='unknown')
    for u in unknow:
        try:
            #u=unknow[3]
            cmds.lockNode(u,l=0)
            cmds.delete(u)
            print 'delete --- '+u
        except:
            print 'something wrong.pass it!'
    unknowDag=cmds.ls(type='unknownDag')
    for u in unknowDag:
        try:
            #u=unknow[3]
            cmds.lockNode(u,l=0)
            cmds.delete(u)
            print 'delete --- '+u
        except:
            print 'something wrong.pass it!'