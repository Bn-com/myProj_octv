import maya.cmds as cmds
def edo_addSkinBindingNode():
    print "edo_addSkinBindingNode..."
    sels=cmds.ls(sl=1)
    for sel in sels:
        #sel=sels[0]
        historytmp=cmds.listHistory(cmds.listRelatives(sel,s=1,ni=1,type='mesh')[0])
        historys=''
        for tmp in historytmp:
            if cmds.nodeType(tmp)=='skinCluster':
                historys=tmp
        sourceGeo=cmds.listConnections(historys+'.input[0].inputGeometry',s=1,d=0,p=1)[0]
        alljoints=cmds.listConnections(historys+'.matrix',p=1,s=1,d=0)
        bindingNode=cmds.listConnections(historys+'.bindVolume',s=1,d=0)
        if bindingNode==None:
            cmds.createNode('skinBinding',n=historys+'_BD')
            cmds.connectAttr(historys+'_BD.updateWeights',historys+'.bindVolume',f=1)
            cmds.connectAttr(sourceGeo,historys+'_BD.inputGeometry',f=1)
            for joint in alljoints:
                #joint=alljoints[0]
                alldir=cmds.listConnections(joint,s=0,d=1,p=1)
                connectSkinPlug=''
                for dir in alldir:
                    if historys[0] in dir:
                        connectSkinPlug=dir
                splitPlugs=connectSkinPlug.split('.')
                bindSkinPlug=historys+'_BD.'+splitPlugs[1].replace('matrix','parentMatrix')
                cmds.connectAttr(joint,bindSkinPlug,f=1)
                matrix=cmds.getAttr(bindSkinPlug)
                cmds.setAttr(bindSkinPlug.replace('parentMatrix','bindPreMatrix'),matrix,type='matrix')
        else:
            cmds.confirmDialog( title='error', message=historys+'.bindVolume  is already connected!you need not add skinBinding node any more!', button='got it!', defaultButton='Yes', cancelButton='YES', dismissString='YES')

def edo_removeSkinBindingNode():
    print "removeSkinBindingNode..."
    sels=cmds.ls(sl=1)
    for sel in sels:
        #sel=sels[0]
        historytmp=cmds.listHistory(cmds.listRelatives(sel,s=1,ni=1,type='mesh')[0])
        historys=''
        for tmp in historytmp:
            if cmds.nodeType(tmp)=='skinCluster':
                historys=tmp
        bindingNode=cmds.listConnections(historys+'.bindVolume',s=1,d=0)
        if not bindingNode==None:
            cmds.delete(bindingNode[0])
        else:
            cmds.confirmDialog( title='error', message=historys+' have no skinBinding node connected to!you need not remove skinBinding node any more!', button='got it!', defaultButton='Yes', cancelButton='YES', dismissString='YES')
            
def edo_SkinBindingUI():
    if cmds.window("edo_SkinBindingWindow",ex=1):
        cmds.deleteUI("edo_SkinBindingWindow")
    cmds.window("edo_SkinBindingWindow",title="edo_SkinBindingWindow")
    cmds.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=190)
    cmds.button('edo_SkinBindingBT1',label='addSkinBinding',h=27,bgc=(0.8,0.2,0.1),c='edo_addSkinBindingNode()')
    cmds.button('edo_SkinBindingBT2',label='removeSkinBinding',h=27,bgc=(0.9,0.9,0.1),c='edo_removeSkinBindingNode()')
    cmds.showWindow("edo_SkinBindingWindow")