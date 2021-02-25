import os
import tempfile
import pymel.core as pm
import maya.cmds as mc
import idmt.maya.unknownPlugin as rup

def MyRemoveUnknownPlugin(dest):
    filename = os.path.basename(dest)
    temp = os.path.join(tempfile.gettempdir(), filename)
    if os.path.isfile(temp):
        os.remove(temp)
    plugins = rup.RemoveUnknownPluginMb(dest, temp)

    if len(plugins) > 0:
        print(temp)
        mc.file(temp, open = True, force = True)
    else:
        print(dest)
        mc.file(dest, open = True, force = True)

    makeTextCurves = mc.ls(type='makeTextCurves')
    unknownDags = mc.ls(type='unknownDag')
    unknownNodes = mc.ls(type='unknown')
    toDels = makeTextCurves + unknownDags + unknownNodes
    for node in toDels:
        try:
            mc.lockNode( node, lock=False )
            mc.delete( node )
            print('delete %s' % node)
        except:
            print('can not delete %s' % node)
            pass

    os.remove(temp)



def OpenAndCleanUnknownPluginFile():
    multipleFilters = "Maya Files (*.ma *.mb);;Maya ASCII (*.ma);;Maya Binary (*.mb)"
    filePath = pm.fileDialog2(fileFilter=multipleFilters, dialogStyle=2, fileMode = 1)
    if filePath:
        MyRemoveUnknownPlugin(filePath[0])

    
    

    