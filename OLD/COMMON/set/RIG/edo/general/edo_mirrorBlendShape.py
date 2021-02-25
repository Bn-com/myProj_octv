import maya.cmds as cmds
import maya.mel as mel
#edo_mirrorBlendShape('BS_','MSH_')
def edo_mirrorBlendShape(sstr,dstr):
    #sstr='BS_'
    #dstr='MSH_'
    sels=cmds.ls(sl=1)
    s=sels[0]
    bd=cmds.xform(s,q=1,bb=1)
    w=bd[3]-bd[0]
    cmds.setAttr(s+'.sx',20)
    cmds.setAttr(s+'.sy',20)
    cmds.setAttr(s+'.sz',20)
    d=cmds.duplicate(s,n='edo_mirrorBlendShape_'+s)[0]
    cmds.setAttr(d+'.sx',-20)
    cmds.setAttr(d+'.v',0)
    cmds.select(d,r=1)
    cmds.select(s,add=1)
    mel.eval('CreateWrap')
    sels.remove(s)
    cmds.select(sels,r=1)
    cmds.select(s,add=1)
    bs=cmds.blendShape(n='edo_mirrorBlendShape')[0]
    for t in sels:
        #t=sels[0]
        print t
        wp=cmds.xform(t,q=1,ws=1,t=1)
        nwp=[wp[0]+w*0.5,wp[1],wp[2]]
        cmds.setAttr(bs+'.'+t,1)
        b=cmds.duplicate(d,n=t.replace(sstr,dstr))[0]
        cmds.setAttr(b+'.sx',1)
        cmds.setAttr(b+'.sy',1)
        cmds.setAttr(b+'.sz',1)
        cmds.setAttr(b+'.v',1)
        cmds.setAttr(bs+'.'+t,0)
        cmds.xform(b,ws=1,t=nwp)
    cmds.setAttr(s+'.sx',1)
    cmds.setAttr(s+'.sy',1)
    cmds.setAttr(s+'.sz',1)
    cmds.delete(bs,d)