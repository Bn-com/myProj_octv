import maya.OpenMaya as om
import maya.cmds as cmds
#edo_renameDefualtRenderLayerName()
def edo_renameDefualtRenderLayerName(newname='defaultRenderLayer'):
    drl=cmds.listConnections('renderLayerManager.rlmi[0]',s=0,d=1)[0]
    if not drl=='defaultRenderLayer':
        try:
            cmds.delete('defaultRenderLayer')
        except:
            print 'defaultRenderLayer is not found!'
    cmds.select(drl,r=1)
    msl=om.MSelectionList()
    mg=om.MGlobal()
    mg.getActiveSelectionList(msl)
    msl.length()
    mobj=om.MObject()
    msl.getDependNode(0,mobj)
    mfndn=om.MFnDependencyNode(mobj)
    mfndn.setName(newname)
edo_renameDefualtRenderLayerName()