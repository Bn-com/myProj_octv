# --- Unlock transforms
import maya.cmds as mc
for sel in mc.ls(tr=True, l=True):
    mc.setAttr(sel+'.translateX', l=False, k=True)
    mc.setAttr(sel+'.translateY', l=False, k=True)
    mc.setAttr(sel+'.translateZ', l=False, k=True)
    mc.setAttr(sel+'.rotateX', l=False, k=True)
    mc.setAttr(sel+'.rotateY', l=False, k=True)
    mc.setAttr(sel+'.rotateZ', l=False, k=True)
    mc.setAttr(sel+'.scaleX', l=False, k=True)
    mc.setAttr(sel+'.scaleY', l=False, k=True)
    mc.setAttr(sel+'.scaleZ', l=False, k=True)
    mc.setAttr(sel+'.visibility', l=False, k=True)