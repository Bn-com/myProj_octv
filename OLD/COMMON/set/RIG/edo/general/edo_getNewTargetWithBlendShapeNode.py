import maya.cmds as cmds
import maya.OpenMaya as om
def edo_getNewTargetWithBlendShapeNode():
    sel=cmds.ls(sl=1)[0]
    shape=cmds.listRelatives(sel,s=1,ni=1)[0]
    nodes=cmds.listHistory(shape)
    bs=edo_findNodeFromList(nodes,'blendShape')
    print ('get the target from '+bs[0])+'  :'
    attr=cmds.blendShape(bs[0],q=1,weight=1)
    num=len(attr)
    if not cmds.objExists('GRP_'+bs[0]+'_newBlendShape'):
        cmds.createNode('transform',n='GRP_'+bs[0]+'_newBlendShape')
    for u in range(0,num):
        attrname=bs[0]+'.weight['+str(u)+']'
        cmds.setAttr(attrname,0)
    for n in range(0,num):
        #n=0
        attrname=bs[0]+'.weight['+str(n)+']'
        longname=cmds.aliasAttr(attrname,q=1)
        print 'get '+longname+'  ...'
        cmds.setAttr(attrname,1)
        dup=cmds.duplicate(sel,n='new_'+longname)
        cmds.parent(dup,'GRP_'+bs[0]+'_newBlendShape')
        cmds.setAttr(attrname,0)

def edo_findNodeFromList(nodes,type):
    bc=[]
    for node in nodes:
        if cmds.nodeType(node)==type:
            bc.append(node)
            print node
    return bc

edo_getNewTargetWithBlendShapeNode()