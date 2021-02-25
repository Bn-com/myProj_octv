#edo_createFacialInfluenceFormSelectedCurve(19)
def edo_createFacialInfluenceFormSelectedCurve(colors):
    sels=cmds.ls(sl=1)
    if sels==None:
        cmds.confirmDialog( title='error', message='you must select two curves', button='god it', defaultButton='Yes', cancelButton='No', dismissString='No')
        return False
    if len(sels)==2:
        edo_convertCurveToInfluence(sels[0],sels[1],colors)


#edo_convertCurveToInfluence('eyebrows_l_sourceCurve','eyebrows_l_directCurve')
def edo_convertCurveToInfluence(sc,dc,colors):
    #sc='eyebrow_r_sourceCurve'
    #dc='eyebrow_dirvectCurve '
    dsc=cmds.duplicate(dc,n=sc+'_original')
    cmds.connectAttr(dsc[0]+'.worldSpace',dc+'.create',f=1)
    cmds.setAttr(dsc[0]+'.v',0)
    lofts=cmds.loft(sc,dc,ch=1,u=1,c=0,ar=1,d=3,ss=1,rn=0,po=1,rsn=1,n=dc.replace('_directCurve','_influence'))
    tess=edo_findNodeFromHis(lofts[0],'nurbsTessellate')
    cmds.setAttr(tess+'.uType',3)
    cmds.setAttr(tess+'.uNumber',3)
    cmds.setAttr(tess+'.vType',3)
    cmds.setAttr(tess+'.vNumber',1)
    cmds.setAttr(tess+'.polygonType',1)
    cmds.setAttr(tess+'.format',2)

    edo_addFafialInfluenceCtrl(dc,colors,0.05)

#edo_addFafialInfluenceCtrl('eyebrows_l_directCurve',17,0.05)
def edo_addFafialInfluenceCtrl(dc,colors,radio):
    #dc='eyebrows_r_directCurve'
    #colors=7
    #radio=0.05
    sp=cmds.getAttr(dc+'.spans')
    dg=cmds.getAttr(dc+'.degree')
    cvnum=sp+dg
    ctrls=[]
    for i in range(0,cvnum):
        #i=0
        ctrl=cmds.sphere(n=dc+'_ctrl_'+str(i),r=radio)
        cmds.delete(ctrl[1])
        #cmds.setAttr(ctrl[0]+'.overrideEnabled',1)
        #cmds.setAttr(ctrl[0]+'.overrideColor',colors)
        ctrlshape=cmds.listRelatives(ctrl[0],s=1,ni=1)
        sg=cmds.listConnections(ctrlshape[0]+'.instObjGroups[0]',s=0,d=1,p=1)
        if not sg==None:
            cmds.disconnectAttr(ctrlshape[0]+'.instObjGroups[0]',sg[0])
        grp=cmds.group(ctrl[0],n='GRP_'+ctrl[0])
        cmds.setAttr(dc+'.controlPoints['+str(i)+'].xValue',0)
        cmds.setAttr(dc+'.controlPoints['+str(i)+'].yValue',0)
        cmds.setAttr(dc+'.controlPoints['+str(i)+'].zValue',0)
        po=cmds.xform(dc+'.cv['+str(i)+']',q=1,ws=1,t=1)
        cmds.xform(grp,ws=1,t=po)
        cmds.connectAttr(ctrl[0]+'.tx',dc+'.controlPoints['+str(i)+'].xValue')
        cmds.connectAttr(ctrl[0]+'.ty',dc+'.controlPoints['+str(i)+'].yValue')
        cmds.connectAttr(ctrl[0]+'.tz',dc+'.controlPoints['+str(i)+'].zValue')
        ctrls.append(grp)
    agrp=cmds.group(ctrls,n='GRP_'+dc+'_cvCtrls')
    cmds.setAttr(agrp+'.overrideEnabled',1)
    cmds.setAttr(agrp+'.overrideColor',colors)

#example:
#edo_findNodeFromHis('object','skinCluster')
#return 'skinCluster1'

def edo_findNodeFromHis(name,type):
    #name='twodline_curve'
    #type='tweak'
    node=''
    hiss=cmds.listHistory(name)
    for his in hiss:
        if cmds.nodeType(his)==type:
            node=his
    return node