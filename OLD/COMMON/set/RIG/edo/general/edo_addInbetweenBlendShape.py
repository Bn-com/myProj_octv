#-*- coding: utf-8 -*-
import maya.cmds as cmds
def edo_edo_addInbetweenBlendShape():
    bs=''
    bss=[]
    sels=cmds.ls(sl=1)
    obj=sels[len(sels)-1]
    objshape=cmds.listRelatives(obj,s=1,ni=1)[0]
    nodes=cmds.listHistory(objshape)
    if nodes==None:
        bs=cmds.deformer(obj,type='blendShape')[0]
    else:
        bss=edo_findNodeFromList(nodes,'blendShape')
        if len(bss)==0:
            bs=cmds.deformer(obj,type='blendShape')
        if len(bss)==1:
            bs=bss[0]
        if len(bss)>1:
            bs=cmds.confirmDialog(title='请指明加入到哪个blendShape节点中',message='请选择一个blendShape节点', button=bss, defaultButton='Yes', cancelButton='No', dismissString='No' )
    sels.remove(obj)
    n=len(sels)
    pw=1.0/n
    wc=cmds.blendShape(bs,q=1,wc=1)
    cmds.blendShape(bs,e=1,t=[obj,wc,sels[n-1],1.0])
    for i in range(0,n-1):
        #i=2
        s=sels[i]
        w=pw*(i+1)
        cmds.blendShape(bs,e=1,ib=1,t=[obj,wc,s,w])
    return True

def edo_findNodeFromList(nodes,type):
    bc=[]
    for node in nodes:
        if cmds.nodeType(node)==type:
            bc.append(node)
            print node
    return bc
edo_edo_addInbetweenBlendShape()