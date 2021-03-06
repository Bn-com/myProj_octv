import maya.cmds as cmds
import maya.mel as mel
global edo_selectedObject
global edo_selectedSkinCluster
##execfile('Z:/Resource/Groups/Production/Modeling/gerenmulu/sunwang/sw_script/edo_rebuildBindPreMatrix.py');edo_rebuildBindPreMatrix();
def edo_connectBindPreMatrix():
    global edo_selectedSkinCluster
    sels=cmds.ls(type='joint',sl=1)
    if len(sels)==0 or len(sels)>1:
        cmds.confirmDialog( title='error', message='please select only one joint', button='Yes', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return 0
    skinClus=cmds.listConnections((sels[0]+'.worldMatrix'),s=0,d=1,p=1,type='skinCluster')
    if not edo_selectedSkinCluster==None:
        skinClus=edo_findSkinClusterMatrixAttrFromList(skinClus,edo_selectedSkinCluster)
    if not skinClus:
        #cmds.confirmDialog( title='error', message='this joint is not connected to skinCluster', button='passed', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return 0
    for i in skinClus:
        ##i=skinClus[0]
        attr=i.replace('.matrix[','.bindPreMatrix[')
        if not cmds.connectionInfo(attr, isDestination=True):
            cmds.connectAttr((sels[0]+'.worldInverseMatrix'),attr)
    return 1

######

def edo_findSkinClusterMatrixAttrFromList(skinClus,selectedSkinCluster):
    findout=[]
    if selectedSkinCluster:
        for ssc in selectedSkinCluster:
            if skinClus:
                for sc in skinClus:
                    if ssc==sc.split('.')[0]:
                        findout.append(sc)
    return findout
                


def edo_setBindPreMatrix():    
    sels=cmds.ls(type='joint',sl=1)
    if len(sels)==0 or len(sels)>1:
        cmds.confirmDialog( title='error', message='please select only one joint', button='Yes', defaultButton='Yes', cancelButton='No', dismissString='No' )
        return 0

    jp=cmds.listRelatives(sels[0],p=1,f=1)
    loc=cmds.createNode('locator')
    loct=cmds.listRelatives(loc,p=1)

    cmds.parent(loct[0],sels[0])
    cmds.setAttr(loct[0]+".tx",0)
    cmds.setAttr(loct[0]+".ty",0)
    cmds.setAttr(loct[0]+".tz",0)
    cmds.setAttr(loct[0]+".rx",0)
    cmds.setAttr(loct[0]+".ry",0)
    cmds.setAttr(loct[0]+".rz",0)
    if jp:
        cmds.parent(loct[0],jp[0])
    else:
        cmds.parent(loct[0],w=1)

    rx=cmds.getAttr(loct[0]+'.rx')
    ry=cmds.getAttr(loct[0]+'.ry')
    rz=cmds.getAttr(loct[0]+'.rz')
    if edo_selectedSkinCluster==None:
        try:
            jrx=cmds.setAttr(sels[0]+'.rx',0)
        except:
            print "canNotDoThis:jrx=cmds.setAttr(sels[0]+'.rx',0)"
        try:
            jry=cmds.setAttr(sels[0]+'.ry',0)
        except:
            print "canNotDoThis:jry=cmds.setAttr(sels[0]+'.ry',0)"
        try:
            jrz=cmds.setAttr(sels[0]+'.rz',0)
        except:
            print "canNotDoThis:jrz=cmds.setAttr(sels[0]+'.rz',0)"    

        cmds.setAttr(sels[0]+'.jointOrientX',rx)
        cmds.setAttr(sels[0]+'.jointOrientY',ry)
        cmds.setAttr(sels[0]+'.jointOrientZ',rz)

    skinClus=cmds.listConnections((sels[0]+'.worldInverseMatrix'),s=0,d=1,p=1,type='skinCluster')
    if not edo_selectedSkinCluster==None:
        skinClus=edo_findSkinClusterMatrixAttrFromList(skinClus,edo_selectedSkinCluster)
        print skinClus
    if not skinClus:
        #cmds.confirmDialog( title='error', message='this joint is not connected to skinCluster', button='Yes', defaultButton='Yes', cancelButton='No', dismissString='No' )
        cmds.delete(loct)
        return 0
    for i in skinClus:
        #i=skinClus[0]
        bindPreMatrix=cmds.getAttr(i)
        cmds.disconnectAttr((sels[0]+'.worldInverseMatrix'),i)
        evalcmd='setAttr '+i+' -type "matrix" '+str(bindPreMatrix[0])+' '+str(bindPreMatrix[1])+' '+str(bindPreMatrix[2])+' '+str(bindPreMatrix[3])+' '+str(bindPreMatrix[4])+' '+str(bindPreMatrix[5])+' '+str(bindPreMatrix[6])+' '+str(bindPreMatrix[7])+' '+str(bindPreMatrix[8])+' '+str(bindPreMatrix[9])+' '+str(bindPreMatrix[10])+' '+str(bindPreMatrix[11])+' '+str(bindPreMatrix[12])+' '+str(bindPreMatrix[13])+' '+str(bindPreMatrix[14])+' '+str(bindPreMatrix[15])
        mel.eval(evalcmd)
    cmds.delete(loct)


def edo_connectBindPreMatrixFor():
    global edo_selectedObject
    global edo_selectedSkinCluster
    edo_selectedSkinCluster=None
    cmds.select(hi=1)
    sels=cmds.ls(sl=1,type='joint',l=1)
    edo_selectedObject=sels
    csk=cmds.confirmDialog( title='choice', message='which skincluster do you want to rebuild?', button=['selectOnes','all of them'], defaultButton='Yes', cancelButton='No', dismissString='No' )
    if sels:
        print 'done'
        if csk=='all of them':
            for i in sels:
                #i='|joint1|joint2|joint3|joint8'
                print i
                cmds.select(i)
                edo_connectBindPreMatrix()
        if csk=='selectOnes':
            skins=cmds.ls(type='skinCluster',sl=1)
            if skins:
                edo_selectedSkinCluster=skins
                for i in sels:
                    #i=sels[0]
                    print i
                    cmds.select(i)
                    edo_connectBindPreMatrix()
    else:
            cmds.confirmDialog( title='error', message='please select one Joint', button='Yes', defaultButton='Yes', cancelButton='No', dismissString='No' )


def edo_setBindPreMatrixFor():
    global edo_selectedObject
    sels=edo_selectedObject
    if sels:
        print 'done'
        for i in sels:
            #i=sels[10]
            #i='|joint1|joint2|joint3'
            print i
            cmds.select(i)
            edo_setBindPreMatrix()
            print 'something wrong!'

def edo_rebuildBindPreMatrix():
    if cmds.window("edo_rebuildBindPreMatrixWindow",ex=1):
        cmds.deleteUI("edo_rebuildBindPreMatrixWindow")
    cmds.window("edo_rebuildBindPreMatrixWindow",title="edo_rebuildBindPreMatrixWindow")
    cmds.columnLayout( columnAttach=('both', 5), rowSpacing=5, columnWidth=190)
    cmds.button('edo_rebuildBindPreMatrixBT1',label='rebuil START',h=27,bgc=(0.1,0.9,0.7),c='edo_connectBindPreMatrixFor()')
    cmds.button('edo_rebuildBindPreMatrixBT2',label='rebuil END',h=27,bgc=(0.9,0.5,0.1),c='edo_setBindPreMatrixFor()')
    cmds.showWindow("edo_rebuildBindPreMatrixWindow");