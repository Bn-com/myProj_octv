#-*- coding: utf-8 -*-
import maya.cmds as cmds

def edo_convertSoftSelectionToSkinClusterWeightUI():
    ui='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_convertSoftSelectionToSkinClusterWeightUI.myuis'
    if cmds.window('edo_convertSoftSelectionToSkinClusterWeightUI',ex=1):
        cmds.deleteUI('edo_convertSoftSelectionToSkinClusterWeightUI')
    mui=cmds.loadUI(f=ui)
    cmds.showWindow(mui)
    cmds.button('gettarget_bt',e=1,c='edo_getSelectToTextEditor(\'gettarget_line\',0)',ann='��ȡҪ����Ȩ�صĹ���')
    cmds.button('getunlock_bt',e=1,c='edo_getSelectToTextEditor(\'getunlock_line\',1)',ann='��ȡҪ����Ȩ�صĹ���')
    cmds.button('convert_bt',e=1,c='edo_convertSoftSelectionToSkinClusterWeight()',ann='��ѡ�������Χ��ִ�����ʼ����Ȩ��')
    
def edo_getSelectToTextEditor(texteditor,multiple):
    #texteditor='lfeyelids_loop_line'
    sels=cmds.ls(orderedSelection=1,fl=1)
    if sels:
        if multiple==1:
            list=''
            for sel in sels:
                list=list+sel+','
            list=list[:len(list)-1]
            cmds.textField(texteditor,e=1,text=list)
        if multiple==0:
            cmds.textField(texteditor,e=1,text=sels[0])
            
def edo_convertSoftSelectionToSkinClusterWeight():
    sels=cmds.ls(sl=1)
    if not sels:
        return False
    tj=cmds.textField('gettarget_line',q=1,text=1)
    if not tj:
        return False
    uj=cmds.textField('getunlock_line',q=1,text=1)
    if not uj:
        return False
    ujs=uj.split(',')
    sel=sels[0]
    mesh=sel.split('.')[0]
    sks=edo_findNodeFromHiss(mesh,'skinCluster')
    sk=sks[0]
    weights=edo_getSoftSelectionWeights(mesh)
    edo_lockAllInfluence(sk)
    edo_unlockInfluenceFromList(ujs)
    edo_unlockInfluenceFromList([tj])
    for i in range(0,len(weights)):
        #i=0
        w=weights[i]
        vtx=mesh+'.vtx['+str(i)+']'
        #clear target joint weight
        cmds.skinPercent(sk,vtx,tv=(tj,0))
        if w>0.001:
            print 'vetex: '+vtx+'  ......  closestJoint: '+tj+'  ......  weight: '+str(w)
            cmds.skinPercent(sk,vtx,tv=(tj,w))
    edo_lockAllInfluence(sk)

def edo_lockAllInfluence(skincluster):
    #skincluster=sk
    infs=cmds.skinCluster(skincluster,q=1,inf=1)
    for jnt in infs:
        cmds.setAttr(jnt+'.lockInfluenceWeights',1)

def edo_unlockInfluenceFromList(list):
    if list:
        for l in list:
            cmds.setAttr(l+'.lockInfluenceWeights',0)
        
    
def edo_findNodeFromHiss(name,type):
    #name='twodline_curve'
    #type='tweak'
    nodes=[]
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            nodes.append(his)
    return nodes
    
def edo_getSoftSelectionWeights(obj):
    #obj=mesh
    vtxlen=cmds.polyEvaluate(obj,v=1)
    pnt=[]
    for i in range(0,vtxlen):
        #i=0
        pnt.append(cmds.xform(obj+'.vtx['+str(i)+']',q=1,os=1,t=1))
    cmds.move(0,100,0,r=1,os=1,wd=1)
    npnt=[]
    for i in range(0,vtxlen):
        #i=0
        npnt.append(cmds.xform(obj+'.vtx['+str(i)+']',q=1,os=1,t=1))
    cmds.move(0,-100,0,r=1,os=1,wd=1)
    weight=[]
    for i in range(0,vtxlen):
        #i=0
        weight.append((npnt[i][1]-pnt[i][1])*0.01)
    return weight

edo_convertSoftSelectionToSkinClusterWeightUI()