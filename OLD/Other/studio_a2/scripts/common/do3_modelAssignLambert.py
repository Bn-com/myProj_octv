# coding=utf8
"""
scriptName：
Author:zhangben
参照slModelAssignLamber 做了调整，修改了代码以能替换连接了mr材质球的物体

"""
import maya.cmds as mc
import maya.mel as mel
import re

#fileName = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]


def do3_modelAssignLambert(delUnuse=False):
    print "start to delete hypershader------------------------------"
    lamSh = "lambert_WHO"
    mat = mc.ls(lamSh, mat=True)
    # print mat
    if mat == []:
        mc.shadingNode("lambert", asShader=True, n=lamSh)
        mc.sets(name=(lamSh + "SG"), renderable=True, noSurfaceShader=True, empty=True)
        mc.connectAttr((lamSh + '.outColor'), (lamSh + 'SG.surfaceShader'), f=True)

    allSG = mc.ls(type="shadingEngine")
    userSG = [allSG[i] for i in range(len(allSG)) if allSG[i] not in ["initialParticleSE", "initialShadingGroup", "lambert_WHOSG"]]
    if delUnuse == True:
        allShader = []
        for eachSG in userSG:
            connectShader = getSG_connectMatAttr(eachSG, 1)
            if len(connectShader) != 0:
                allShader.append(mc.listConnections(connectShader))
                connet_SGNodeTospecifiedMateriaol(eachSG, lamSh)
        allShader = [allShader[n] for n in range(len(allShader)) if allShader[n] not in allShader[:n]]
        try:
            mc.delete(allShader)
        except:
            print "the shader %s is a reference file shader node" % (eachSG)
            pass
        mel.eval("MLdeleteUnused")
    else:
        for eachSG in userSG:
            connet_SGNodeTospecifiedMateriaol(eachSG, lamSh)
    delete_allLighter()


def getSG_connectMatAttr(SG_node, fullName=0):
    con_MT_attrsLs = mc.listAttr(SG_node, array=True, string="mi*")
    ex_con_MT_attrs=[]
    ex_con_MT_attrs_fn=[]
    if con_MT_attrsLs:
        con_MT_attrsLs.append("surfaceShader")
        ex_con_MT_attrs = [con_MT_attrsLs[l] for l in range(len(con_MT_attrsLs)) if (mc.listConnections((SG_node + "." + con_MT_attrsLs[l]), d=True)) != None]
        ex_con_MT_attrs_fn = [SG_node + "." + ex_con_MT_attrs[j] for j in range(len(ex_con_MT_attrs))]
    
    if fullName == 0:
        return ex_con_MT_attrs
    else:
        return ex_con_MT_attrs_fn


def delete_allShader():
    allSG = mc.ls(type="shadingEngine")
    userSG = [allSG[i] for i in range(len(allSG)) if allSG[i] not in ["initialParticleSE", "initialShadingGroup", "lambert_WHOSG"]]
    allShader = []
    for eachSG in userSG:
        allShader.append(mc.listConnections(getSG_connectMatAttr(eachSG, 1))[0])
    allShader = [allShader[n] for n in range(len(allShader)) if allShader[n] not in allShader[:n]]
    mc.delete(allShader)
    mel.eval("MLdeleteUnused")


def delete_allLighter():
    allLightes = mc.ls(type=u'light')
    if allLightes != None and len(allLightes) > 0:
        mc.delete(allLightes)


def connet_SGNodeTospecifiedMateriaol(SG_node, specMT):
#    SG_node = eachSG
#    specMT = lamSh
    p = re.compile("surfaceShader")
    for coned_attr in getSG_connectMatAttr(SG_node, 1):
        pass
        if len(p.findall(coned_attr)) != 0:
            try:
                mc.connectAttr((specMT + ".outColor"), coned_attr, f=True)
            except:
                pass
        else:
            try:
                mc.connectAttr((specMT + ".message"), coned_attr, f=True)
            except:
                pass

#===============================================================================
# def connet_SGNodeTospecifiedMateriaol(SG_node,specMT):
#    p = re.compile("surfaceShader")
#    for coned_attr in getSG_connectMatAttr(SG_node,1):
#        if len(p.findall(coned_attr)) != 0:
#            mc.connectAttr((specMT + ".outColor"),coned_attr,f=True)
#        else:
#            mc.connectAttr((specMT + ".message"),coned_attr,f=True)
#===============================================================================


if __name__ == "__main__":
    do3_modelAssignLambert(True)
