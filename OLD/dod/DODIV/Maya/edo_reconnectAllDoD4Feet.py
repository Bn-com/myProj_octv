import maya.cmds as cmds
import maya.OpenMayaAnim as oma
# edo_reconnectAllDoD4Feet(0)


def edo_reconnectAllDoD4Feet(bake=1):
    # bake=0
    ma = oma.MAnimControl()
    startTime = ma.minTime().value()
    endTime = ma.maxTime().value()
    sins = []
    s0 = cmds.ls('*FEET_OFFSET')
    s1 = cmds.ls('*:FEET_OFFSET')
    s2 = cmds.ls('*:*:FEET_OFFSET')
    s3 = cmds.ls('*:*:*:FEET_OFFSET')
    sins = s0 + s1 + s2 + s3
    allsins = []
    if len(sins) != 0:
        for sin in sins:
            # sin=sins[0]
            ss = cmds.sets(sin, q=1)
            for s in ss:
                # s=ss[0]
                allsins.append(s)
        print allsins
    else:
        return
    if bake == 1:
        cmds.bakeSimulation(allsins, t=(startTime, endTime), at=['offset'])
    if bake == 0:
        for s in allsins:
            # s=allsins[0]
            if cmds.objExists(s + '.offset') and cmds.objExists(s + '.offset_ex'):
                try:
                    cmds.connectAttr(s + '.offset_ex', s + '.offset', f=1)
                except:
                    print "%s.offset_ex CAN'T Connect to %s.offset" % (s, s)
