# utf=8
'''
Created on 2012-11-152012

@author: zhangben
'''
import maya.cmds as mc
import re
import maya.mel as mel


def do3_vegeHMLTransWin_UI():
    if mc.window("do3_vegeHMLTransWin", q=True, exists=True):
        mc.deleteUI("do3_vegeHMLTransWin")

    mc.window("do3_vegeHMLTransWin", wh=[180, 150], t="H-M-L")
    mc.frameLayout(l="vegetableTrans H-M-L:")
    mc.columnLayout(columnAttach=('both', 2), rowSpacing=10, columnWidth=145, adj=False)
    mc.button("l_b", l="LOW_model", c="do3_vegetable_HML_transform(\"l\")")
    mc.button("l_m", l="MID_model", c="do3_vegetable_HML_transform(\"m\")")
    mc.button("l_h", l="HIG_model", c="do3_vegetable_HML_transform(\"h\")")

    mc.window("do3_vegeHMLTransWin", e=True, wh=[180, 150], s=False)

    mc.showWindow("do3_vegeHMLTransWin")


def do3_vegetable_HML_transform(modeDegree, projName=u'DiveollyDive5'):
    #modeDegree = "h"
    selectVegetables = mc.ls(sl=True, l=True)
    vegeTMoveGrp_A = []
    vegeTMoveGrp_B = []
    for selVege in selectVegetables:
        if(mc.listRelatives(selVege, children=True, s=True, type="mesh", ni=True) == None):
            mc.error("Must select vegetation Mesh transform node")
        # help(str)
        vegeStyle = selVege.split("_")[-3][-1]
        # print vegeStyle
        if vegeStyle == "A":
            vegeTMoveGrp_A.append(mc.listRelatives(selVege, p=True, type="transform", f=True)[0])
        if vegeStyle == "B":
            vegeTMoveGrp_B.append(mc.listRelatives(selVege, p=True, type="transform", f=True)[0])

    vegeTMoveGrp_A = [vegeTMoveGrp_A[i] for i in range(len(vegeTMoveGrp_A)) if vegeTMoveGrp_A[i] not in vegeTMoveGrp_A[:i]]
    vegeTMoveGrp_B = [vegeTMoveGrp_B[j] for j in range(len(vegeTMoveGrp_B)) if vegeTMoveGrp_B[j] not in vegeTMoveGrp_B[:j]]
    # ============reference corresponding style vegetable "L" "M" "H"=======================================================
    #modeDegree = "h"
    path = r"//file-cluster/GDC/Projects/%s/Project/scenes/props/p003001Vegetation1/master/do5_p003001Vegetation1_%s_ms_render.mb" % (projName, modeDegree)

    imModel = mc.file(path, i=True, typ="mayaBinary", ns="rp_", ra=False, options="v=0", pr=True)

    im_rp_RootGrp = mc.ls("rp_*:*MODEL*")
    im_rp_moveGrp_A = mc.ls("rp_*:*A*", type="transform", l=True)[0]
    im_rp_moveGrp_B = mc.ls("rp_*:*B", type="transform", l=True)[0]
    print u'Import Succeed!'
    mc.select(cl=True)
    do3_dupRefVegetableTransGrp(vegeTMoveGrp_A, im_rp_moveGrp_A)
    do3_dupRefVegetableTransGrp(vegeTMoveGrp_B, im_rp_moveGrp_B)
      
    mc.delete(im_rp_RootGrp)
    print u'DELETE Import Group \"PROP\" !!!'
    
    if modeDegree == "h":
        mc.delete(mc.ls("rp_*:*PROP*"))
    rp_nodes = mc.ls("rp_*:*")
    for each_rpN in rp_nodes:
        mc.rename(each_rpN, each_rpN.split(":")[-1])
    cleanUp_Namespace("rp_")

    mc.select(cl=True)
#mel.eval("cleanUpScene 1;")
#======================================dup geoGroup and move it =======================================


def do3_dupRefVegetableTransGrp(vegetableGrpName, dupGrpName):
    dupGrpNameConLs = dupGrpName.split("|")[:-1]
    if len(vegetableGrpName) != 0:
        duped_groups = []
        for k in range(len(vegetableGrpName)):
            # ============store select vegetable translate & rotate informations==========================================================
            storeTrans = mc.getAttr((vegetableGrpName[k] + ".translate"))[0]
            storeRot = mc.getAttr((vegetableGrpName[k] + ".rotate"))[0]
            storeScal = mc.getAttr((vegetableGrpName[k] + ".scale"))[0]
            print u" Trans DATA Recorded!"
            # ============find the corresponding group and trans it==============================================================
            parentNode = mc.listRelatives(vegetableGrpName[k], p=True, f=True)[0]
            dupResult_sn = mc.duplicate(dupGrpName, rr=True, upstreamNodes=True)[0]
            print  u'Duplicated Done!!!'
            dupResult_fn = "|".join(dupGrpNameConLs) + "|" + dupResult_sn
            mc.setAttr((dupResult_fn + ".translate"), storeTrans[0], storeTrans[1], storeTrans[2])
            mc.setAttr((dupResult_fn + ".rotate"), storeRot[0], storeRot[1], storeRot[2])
            mc.setAttr((dupResult_fn + ".scale"), storeScal[0], storeScal[1], storeScal[2])
            print u'move it !!!'
            duped_groups.append(dupResult_fn)
            mc.select(cl=True)
        mc.delete(vegetableGrpName)
        print u'Delete  source vegetable group'
        mc.parent(duped_groups, parentNode)
        print u'Parent dup group To ParentGroup'
    else:
        pass


# =================remove "rp_*" namespace that procreateed by several times oprate========================================
def cleanUp_Namespace(match_NSChar):
    mc.namespace(set=":")
    allNamespaces = mc.namespaceInfo(listOnlyNamespaces=True)
    p = re.compile(match_NSChar)

    idleNamespace = [allNamespaces[i] for i in range(len(allNamespaces)) if len(p.findall(allNamespaces[i])) != 0]
    for eachINS in idleNamespace:
        remove_namespace(eachINS)
    return(mc.namespaceInfo(listOnlyNamespaces=True))


def remove_namespace(removeNS):
    #removeNS = "rp_1"
    mc.namespace(set=removeNS)
    objsInNs = mc.namespaceInfo(listNamespace=True)
    mc.delete(objsInNs)
    mc.namespace(set=":")
    mc.namespace(removeNamespace=removeNS)
    # return(mc.namespaceInfo(listOnlyNamespaces=True))


if __name__ == "__main__":
    do3_vegeHMLTransWin_UI()
