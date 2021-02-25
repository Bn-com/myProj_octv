import maya.cmds as cmds
#edo_createCtrlOnSelectCurve('local',0.2,17)
def edo_createCtrlOnSelectCurve(space,radio,colors):
    #space='world'
    #radio=0.05
    #colors=11
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='you must select something', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if space=='local':
        for sel in sels:
            #sel=sels[0]
            org=cmds.duplicate(sel,n=sel+'_orig')[0]
            cmds.connectAttr(org+'.worldSpace',sel+'.create',f=1)
            selshape=cmds.listRelatives(sel,s=1,ni=1)
            spans=cmds.getAttr(selshape[0]+'.spans')
            degree=cmds.getAttr(selshape[0]+'.degree')
            cvnum=spans+degree
            ctrls=[]
            for n in range(0,cvnum):
                cv=selshape[0]+'.controlPoints['+str(n)+']'
                cmds.setAttr(cv+'.xValue',0)
                cmds.setAttr(cv+'.yValue',0)
                cmds.setAttr(cv+'.zValue',0)
            for i in range(0,cvnum):
                 #i=0
                 cv=selshape[0]+'.controlPoints['+str(i)+']'
                 cvpo=cmds.xform(cv,q=1,ws=1,t=1)
                 ctrl=cmds.sphere(n=sel+'_ctrl_'+str(i),r=radio)
                 cmds.delete(ctrl[1])
                 ctrlshape=cmds.listRelatives(ctrl[0],s=1,ni=1)
                 sg=cmds.listConnections(ctrlshape[0]+'.instObjGroups[0]',s=0,d=1,p=1)
                 if not sg==None:
                    cmds.disconnectAttr(ctrlshape[0]+'.instObjGroups[0]',sg[0])
                 grp=cmds.group(ctrl[0],n='GRP_'+ctrl[0])
                 cmds.xform(grp,ws=1,t=cvpo)
                 cmds.connectAttr(ctrl[0]+'.translate',cv,f=1)
                 ctrls.append(grp)
            agrp=cmds.group(ctrls,n='GRP_'+sel+'_cvCtrls')
            cmds.setAttr(agrp+'.overrideEnabled',1)
            cmds.setAttr(agrp+'.overrideColor',colors)
    if space=='world':
        for sel in sels:
            #sel=sels[0]
            selshape=cmds.listRelatives(sel,s=1,ni=1)
            orgshape=cmds.listConnections(selshape[0]+'.create',s=1,d=0,p=1)
            if not orgshape==None:
                cmds.delete(orgshape[0].split('.')[0])
            spans=cmds.getAttr(selshape[0]+'.spans')
            degree=cmds.getAttr(selshape[0]+'.degree')
            cvnum=spans+degree
            ctrls=[]
            for i in range(0,cvnum):
                 #i=0
                 cv=selshape[0]+'.controlPoints['+str(i)+']'
                 cvpo=cmds.xform(cv,q=1,ws=1,t=1)
                 ctrl=cmds.sphere(n=sel+'_ctrl_'+str(i),r=radio)
                 cmds.delete(ctrl[1])
                 ctrlshape=cmds.listRelatives(ctrl[0],s=1,ni=1)
                 sg=cmds.listConnections(ctrlshape[0]+'.instObjGroups[0]',s=0,d=1,p=1)
                 if not sg==None:
                    cmds.disconnectAttr(ctrlshape[0]+'.instObjGroups[0]',sg[0])
                 grp=cmds.group(ctrl[0],n='GRP_'+ctrl[0])
                 loc=cmds.createNode('locator',n='LOC_'+ctrl[0],p=ctrl[0])
                 cmds.setAttr(loc+'.v',0)
                 cmds.xform(grp,ws=1,t=cvpo)
                 cmds.connectAttr(loc+'.worldPosition',cv,f=1)
                 ctrls.append(grp)
            agrp=cmds.group(ctrls,n='GRP_'+sel+'_cvCtrls')
            cmds.setAttr(agrp+'.overrideEnabled',1)
            cmds.setAttr(agrp+'.overrideColor',colors)