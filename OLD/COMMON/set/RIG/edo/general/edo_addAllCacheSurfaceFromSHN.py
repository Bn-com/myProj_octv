import maya.cmds as cmds
def edo_checkUnusedOutPutCurve(outputCurve):
    #outputCurve=allHairCurve
    unused=[]
    for oc in outputCurve:
        #oc=outputCurve[0]
        ocshapes=cmds.listRelatives(oc,s=1)
        if ocshapes==None:
            return None
        ocshape=ocshapes[0]
        input=cmds.listConnections(ocshape+'.create',s=1,d=0)
        if input==None:
            unused.append(oc)
    print unused
    return unused

def edo_addCacheSurfaceFromSHN():
    sels=cmds.ls(sl=1)
    sel=sels[0]
    shnshape=cmds.listRelatives(sel,s=1)[0]
    lofts=cmds.listConnections(shnshape+'.create',d=0,s=1)
    if lofts==None:
        return False
    loft=lofts[0]
    if cmds.nodeType(loft)=='rebuildSurface':
        lofts=cmds.listConnections(loft+'.inputSurface',d=0,s=1)
        if lofts==None:
            return False
        loft=lofts[0]
    if cmds.nodeType(loft)=='reverseSurface':
        lofts=cmds.listConnections(loft+'.inputSurface',d=0,s=1)
        if lofts==None:
            return False
        loft=lofts[0]
    allHairCurve=cmds.listConnections(loft+'.inputCurve',d=0,s=1)
    unused=edo_checkUnusedOutPutCurve(allHairCurve)
    if not unused==[]:
        cmds.delete(unused)
        allHairCurve=cmds.listConnections(loft+'.inputCurve',d=0,s=1)
    startCurves=[]
    for hairCurve in allHairCurve:
        #hairCurve = allHairCurve[1]
        if not cmds.objExists(hairCurve):
            continue
        fos=cmds.listConnections(hairCurve+'.create',d=0,s=1,sh=1)
        if fos==None:
            continue
        fo=fos[0]
        nodetype=cmds.nodeType(fo)
        if nodetype=='rebuildCurve':
            fos=cmds.listConnections(fo+'.inputCurve',d=0,s=1)
            if fos==None:
                continue
        fo=fos[0]
        startCurve=cmds.listConnections(fo+'.startPosition',d=0,s=1,sh=1)[0]
        inputs=cmds.listConnections(startCurve,s=1,d=0,sh=1)
        if inputs==None:
            continue
        input=inputs[0]
        if cmds.nodeType(input)=='rebuildCurve':
            inputs=cmds.listConnections(input,s=1,d=0,sh=1)
            if inputs==None:
                continue
            input=inputs[0]
            if cmds.nodeType(input)=='nurbsCurve':
                startCurves.append(input)
                continue
        if cmds.nodeType(input)=='nurbsCurve':
            startCurves.append(input)
    span=len(startCurves)-1
    cmds.select(startCurves,r=1)
    cmds.Loft()
    loftsurface=cmds.ls(sl=1)[0]
    cmds.rename(loftsurface,'CHS_'+sel)
    cmds.DeleteHistory()
    cs=0
    for startCurve in startCurves:
        #startCurve = startCurves[0]
        startCurveShape=startCurve
        iso=cmds.createNode('curveFromSurfaceIso',n='ISO_'+startCurve)
        cmds.connectAttr('CHS_'+sel+'.worldSpace',iso+'.inputSurface',f=1)
        cmds.connectAttr(iso+'.outputCurve',startCurveShape+'.create',f=1)
        cmds.setAttr(iso+'.isoparmValue',cs)
        cs=cs+1
    return True

def edo_addAllCacheSurfaceFromSHN():
    sels=cmds.ls(sl=1)
    for sel in sels:
        cmds.select(sel,r=1)
        edo_addCacheSurfaceFromSHN()

edo_addAllCacheSurfaceFromSHN()