import maya.cmds as mc
# --- color
# red = 13
# yellow = 17
color = 17

selection = mc.ls(sl=True)
for sel in selection:
    shapeLs = mc.listRelatives(sel, s=True, f=True)
    for shape in shapeLs:
        mc.setAttr(shape+'.overrideEnabled', 1)
        mc.setAttr(shape+'.overrideColor', color)