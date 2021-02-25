import maya.cmds as cmds
import maya.OpenMayaAnim as oma
def edo_bakeMustacheDynCtrl():
    nameSpace=cmds.ls(sl=1)[0].split(':')[0]
    set=nameSpace+':'+'mustache_dyn_ctrl_set'
    ma=oma.MAnimControl()
    st=ma.minTime().value()
    et=ma.maxTime().value()
    if cmds.objExists(set):
        allctrls=cmds.sets(set,q=1)
        cmds.bakeSimulation(allctrls,t=(st,et),sb=1,at=['tx','ty','tz','rx','ry','rz'],hi='none')
        cmds.setAttr(nameSpace+':'+'GRP_mustache_dyn.ctrl_type',1)
    
def edo_rebakeMustacheDynCtrl():
    nameSpace=cmds.ls(sl=1)[0].split(':')[0]
    set=nameSpace+':'+'mustache_dyn_ctrl_set'
    if cmds.objExists(set):
        allctrls=cmds.sets(set,q=1)
        for c in allctrls:
            #c=allctrls[0]
            input=cmds.listConnections(c,s=1,d=0)
            if not input==None:
                for i in input:
                    #i=input[1]
                    if 'animCurve' in cmds.nodeType(i):
                        cmds.delete(i)

edo_bakeMustacheDynCtrl()