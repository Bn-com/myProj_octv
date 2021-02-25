#-*- coding: utf-8 -*-
import maya.cmds as cmds

def edo_multiplyItSelfsWeightUI():
    ui='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_multiplyItSelfsWeightUI.myuis'
    if cmds.window('edo_multiplyItSelfsWeightUI',ex=1):
        cmds.deleteUI('edo_multiplyItSelfsWeightUI')
    mui=cmds.loadUI(f=ui)
    cmds.showWindow(mui)
    cmds.button('gettargets_bt',e=1,c='edo_getSelectToTextEditor(\'gettargets_line\',1)',ann='��ȡҪ�Գ�Ȩ�صĹ���')
    cmds.button('getunlocks_bt',e=1,c='edo_getSelectToTextEditor(\'getunlocks_line\',1)',ann='��ȡҪ����Ȩ�صĹ���')
    cmds.floatSliderGrp('multiplyWeight_fsg',label='multiplyWeightValue',pre=3,cl3=['left','left','left'],cw3=[90,50,50],field=True,minValue=-0,maxValue=1.5,fieldMinValue=0,fieldMaxValue=1.5,value=1,p='multiplyWeight_grp')
    cmds.button('multiplyWeight_bt',c='edo_multiplyThemselvesWeight()',p='multiplyWeight_grp')

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
            
def edo_multiplyThemselvesWeight():
    sels=cmds.ls(sl=1,fl=1)
    if not sels:
        return False
    tj=cmds.textField('gettargets_line',q=1,text=1)
    if not tj:
        return False
    uj=cmds.textField('getunlocks_line',q=1,text=1)
    if not uj:
        return False
    mv=cmds.floatSliderGrp('multiplyWeight_fsg',q=1,v=1)
    ujs=uj.split(',')
    sel=sels[0]
    mesh=sel.split('.')[0]
    sks=edo_findNodesFromHis(mesh,'skinCluster')
    sk=sks[0]
    #if sks>1:
    #    sk=cmds.confirmDialog( title='more than one skincluster found!', message='more than one skincluster found,plsease select one of them', button=sks, defaultButton='Yes', cancelButton='No', dismissString='No' )
    edo_lockAllInfluence(sk)
    edo_unlockInfluenceFromList(ujs)
    infs=cmds.skinCluster(sk,q=1,inf=1)
    for s in sels:
        #s=sels[0]
        ow=cmds.skinPercent(sk,s,q=1,v=1)
        for i in range(0,len(ow)):
            #i=2
            #print 'original influence weight:  ..  '+infs[i]+'   is   '+str(ow[i])
            if infs[i] in tj:
                mw=ow[i]*mv
                #print 'new influence weight:  ..  '+infs[i]+'   is   '+str(mv)
                cmds.skinPercent(sk,s,tv=[infs[i],mw])

def edo_lockAllInfluence(skincluster):
    #skincluster=sk
    infs=cmds.skinCluster(skincluster,q=1,inf=1)
    for jnt in infs:
        cmds.setAttr(jnt+'.lockInfluenceWeights',1)

def edo_unlockInfluenceFromList(list):
    if list:
        for l in list:
            cmds.setAttr(l+'.lockInfluenceWeights',0)

def edo_findNodesFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=[]
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node.append(his)
    return node

edo_multiplyItSelfsWeightUI()
