import maya.cmds as mc
import re
selection = mc.ls(sl=True, l=True)
mc.select(cl=True)
for sel in selection:
    mc.makeIdentity(sel, a=True, t=False, r=False, s=True, n=False)
    selParent = mc.listRelatives(sel, p=True, f=True)
    if 'msh_' in sel.rpartition('|')[-1] or 'c_' in sel.rpartition('|')[-1]:
        grpName = sel.rpartition('|')[-1].replace('msh_', 'root_').replace('c_', 'GRP_')
    else:
        grpName = 'root_'+sel.rpartition('|')[-1]
    i = 1
    while mc.objExists(grpName):
        match = re.search('\d+$', grpName)
        grpName = grpName[:match.start()] + str(i)
        i += 1
    root = mc.group(em=True, n=grpName)
    selPos = mc.xform(sel, q=True, ws=True, t=True)
    selPiv = mc.xform(sel, q=True, r=True, piv=True)
    selRot = mc.xform(sel, q=True, ws=True, ro=True)
    mc.xform(root, ws=True, t=selPos[:3])
    mc.xform(root, ws=True, ro=selRot)
    mc.xform(root, r=True, piv=selPiv[:3])
    mc.parent(sel, root)
    if selParent:
        mc.parent(root, selParent[0])