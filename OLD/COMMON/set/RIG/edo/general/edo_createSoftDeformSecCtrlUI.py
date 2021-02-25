import maya.cmds as cmds
def edo_createSoftDeformSecCtrlUI():
    if cmds.window('edo_createSoftDeformSecCtrlUI',q=1,ex=1):
        cmds.deleteUI('edo_createSoftDeformSecCtrlUI')
    ui=cmds.loadUI(f='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_createSoftDeformSecCtrlUI.myuis')
    cmds.showWindow(ui)
    #create
    cmds.button('edo_createSoftDeformSecCtrl_BT01',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TF01\')')
    cmds.button('edo_createSoftDeformSecCtrl_BT02',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TF02\')')
    cmds.button('edo_createSoftDeformSecCtrl_BT03',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TF03\')')
    cmds.button('edo_createSoftDeformSecCtrl_BT04',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TF04\')')
    cmds.button('edo_createSoftDeformSecCtrl_BT05',e=1,c='edo_createSoftDeformSecCtrlCmd()')
    #append
    cmds.button('edo_createSoftDeformSecCtrl_TBL01_BT01',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TBL01_TF01\')')
    cmds.button('edo_createSoftDeformSecCtrl_TBL01_BT02',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TBL01_TF02\')')
    cmds.button('edo_createSoftDeformSecCtrl_TBL01_BT03',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TBL01_TF03\')')
    cmds.button('edo_createSoftDeformSecCtrl_TBL01_BT04',e=1,c='edo_loadListToTF(\'edo_createSoftDeformSecCtrl_TBL01_TF04\')')
    cmds.button('edo_createSoftDeformSecCtrl_TBL01_BT05',e=1,c='edo_createSoftDeformSecCtrl_TBL01Cmd()')
    #transfer
    cmds.button('edo_transferToSkinCluster_bt',e=1,c='edo_transferSDHtoSKJ(0)')
    cmds.window(ui,e=1,wh=[350,230])
edo_createSoftDeformSecCtrlUI()

def edo_createSoftDeformSecCtrlCmd():
    skin=cmds.textField('edo_createSoftDeformSecCtrl_TF01',q=1,text=1)
    fo=cmds.textField('edo_createSoftDeformSecCtrl_TF02',q=1,text=1)
    locs=cmds.textField('edo_createSoftDeformSecCtrl_TF03',q=1,text=1).split(',')
    dfms=cmds.textField('edo_createSoftDeformSecCtrl_TF04',q=1,text=1).split(',')
    edo_createSoftDeformSecCtrl(skin,fo,locs,dfms)
    
def edo_createSoftDeformSecCtrl_TBL01Cmd():
    fo=cmds.textField('edo_createSoftDeformSecCtrl_TBL01_TF02',q=1,text=1)
    locs=cmds.textField('edo_createSoftDeformSecCtrl_TBL01_TF03',q=1,text=1).split(',')
    dfms=cmds.textField('edo_createSoftDeformSecCtrl_TBL01_TF04',q=1,text=1).split(',')
    edo_appendoftDeformSecCtrl(fo,locs,dfms)
    
def edo_appendoftDeformSecCtrl(fo,locs,dfms):
    print 'append soft deform secondary ctrl...'
    allfollicle=edo_addFollicleOnMeshByLocator(fo,locs)
    edo_addSoftDeformerSecCtrlOnAllMeshes(dfms,allfollicle)
    
def edo_listToStr(list):
    s=''
    for l in list:
        s+=(str(l)+',')
    return s[:len(s)-1]

def edo_loadListToTF(tfid):
    #tfid='edo_createSoftDeformSecCtrl_TF01'
    sels=cmds.ls(sl=1)
    t=edo_listToStr(sels)
    cmds.textField(tfid,e=1,text=t)

#edo_createSoftDeformSecCtrl(org,fo,locs,adm)
def edo_createSoftDeformSecCtrl(org,fo,locs,adm):
    #org='pSphere1_'
    #fo='pSphere2_fo_'
    #locs=['locator1']
    #adm='pSphere1_'
    tmp=edo_createSDsecctrlBlendshape(org,fo)
    org=tmp[0]
    scm=tmp[1]
    allfollicle=edo_addFollicleOnMeshByLocator(fo,locs)
    edo_addSoftDeformerSecCtrlOnAllMeshes(adm,allfollicle)
    
#edo_addSoftDeformerSecCtrlOnAllMeshes(adm,allfollicle)
def edo_addSoftDeformerSecCtrlOnAllMeshes(adm,allfollicle):
    #allfollicle=cmds.ls(sl=1)
    #adm=cmds.ls(sl=1)
    #adml=len(adm)
    aixsLoc=cmds.createNode('transform',n='SMC_AxisLoc')
    aixsLocShape=cmds.createNode('locator',n='SMC_AxisLocShape',p=aixsLoc)
    for follicle in allfollicle:
        #follicle = allfollicle[0]
        sf=cmds.deformer(adm,type='softMod',n='SD_'+follicle)
        g=cmds.createNode('transform',n='GRP_SDH_'+follicle,p=follicle)
        ga=cmds.createNode('transform',n='AXIS_SDH_'+follicle,p=g)
        fct=cmds.createNode('transform',n='FCT_SDH_'+follicle+'_CTRL',p=ga)
        fctc=cmds.circle(n=fct+'_tmp',ch=1,o=1,nr=[0,0,1],r=0.5)
        cmds.parent(fctc[0]+'Shape',fct,r=1,s=1)
        cmds.delete(fctc)
        cmds.setAttr(fct+'.overrideEnabled',1)
        cmds.setAttr(fct+'.ovc',17)
        lc=cmds.createNode('locator',n='DCT_LOC_'+follicle,p=fct)
        cmds.setAttr(lc+'.v',0)
        htg=cmds.createNode('transform',n='DRIVEN_SDH_'+follicle+'_CTRL',p=fct)
        ht=cmds.createNode('transform',n='SDH_'+follicle+'_CTRL',p=htg)
        hs=cmds.createNode('softModHandle',n='SDH_'+follicle+'_CTRLShape',p=ht)
        htc=cmds.circle(n=ht+'_tmp',ch=1,o=1,nr=[0,0,1],r=0.25)
        cmds.parent(htc[0]+'Shape',ht,r=1,s=1)
        cmds.delete(htc)
        cmds.setAttr(ht+'.overrideEnabled',1)
        cmds.setAttr(ht+'.ovc',6)
        cmds.connectAttr(ht+'.worldMatrix[0]',sf[0]+'.matrix',f=1)
        cmds.connectAttr(hs+'.softModTransforms[0]',sf[0]+'.softModXforms',f=1)
        cmds.connectAttr(lc+'.worldPosition',sf[0]+'.falloffCenter')
        cmds.connectAttr(fct+'.worldInverseMatrix[0]',sf[0]+'.bindPreMatrix',f=1)
        cmds.addAttr(ht,ln='deformType',at='enum',en='Volume:Surface:')
        cmds.setAttr(ht+'.deformType',e=1,k=1)
        cmds.addAttr(ht,ln='falloffRadius',at='double')
        cmds.setAttr(ht+'.falloffRadius',e=1,k=1)
        cmds.addAttr(ht,ln='falloffRadiusScale',at='double')
        cmds.setAttr(ht+'.falloffRadiusScale',e=1,k=1)
        cmds.setAttr(ht+'.falloffRadiusScale',1)
        cmds.addAttr(ht,ln='keepAxis',at='double',min=0,max=1)
        cmds.setAttr(ht+'.keepAxis',e=1,k=1)
        cmds.addAttr(ht,ln='parentCtrlVis',at='bool',min=0,max=1)
        cmds.setAttr(ht+'.parentCtrlVis',e=1,k=1)
        cmds.connectAttr(ht+'.deformType',sf[0]+'.falloffMode',f=1)
        mlt=cmds.createNode('multiplyDivide',n='MLT_'+sf[0])
        cmds.setAttr(mlt+'.input2X',0.01)
        cmds.connectAttr(ht+'.falloffRadius',mlt+'.input1X',f=1)
        mltgs=cmds.createNode('multiplyDivide',n='MLT_global_'+sf[0])
        cmds.connectAttr(mlt+'.outputX',mltgs+'.input1X',f=1)
        cmds.connectAttr(ht+'.falloffRadiusScale',mltgs+'.input2X',f=1)
        cmds.connectAttr(mltgs+'.outputX',sf[0]+'.falloffRadius',f=1)
        orient=cmds.orientConstraint(aixsLoc,ga,mo=0)
        acs=cmds.setKeyframe(ga)
        cmds.connectAttr(ht+'.keepAxis',ga+'.blendOrient1',f=1)
        ftcshape=cmds.listRelatives(fct,s=1,pa=1)[0]
        cmds.connectAttr(ht+'.parentCtrlVis',ftcshape+'.v',f=1)


def edo_removeAllSdmMeshes(sdmgrp):
    #sdmgrp='SDM_allDeformModel'
    cmds.select(sdmgrp,hi=1)
    sdms=cmds.ls(sl=1,type='mesh')
    for sdm in sdms:
        #sdm=sdms[0]
        s=cmds.listConnections(sdm+'.inMesh',s=1,d=0,p=1)[0]
        d=cmds.listConnections(sdm+'.worldMesh[0]',s=0,d=1,p=1)[0]
        cmds.connectAttr(s,d,f=1)
    cmds.delete(sdms)
        
def edo_addFollicleOnMeshByLocator(fo,locs):
    cn=cmds.createNode('closestPointOnMesh')
    cmds.connectAttr(fo+'.outMesh',cn+'.inMesh',f=1)
    allFollicle=[]
    if not cmds.objExists('FOL_secondaryCtrl'):
        cmds.createNode('transform',n='FOL_secondaryCtrl')
    for loc in locs:
        #loc=locs[0]
        cmds.connectAttr(loc+'.worldPosition',cn+'.inPosition',f=1)
        u=cmds.getAttr(cn+'.result.parameterU')
        v=cmds.getAttr(cn+'.result.parameterV')
        t=cmds.createNode('transform',n='FOL_'+loc,p='FOL_secondaryCtrl')
        f=cmds.createNode('follicle',n='FOL_'+loc+'Shape',p=t)
        cmds.setAttr(f+'.v',0)
        cmds.connectAttr(f+'.outTranslate',t+'.translate',f=1)
        cmds.connectAttr(f+'.outRotate',t+'.rotate',f=1)
        cmds.connectAttr(fo+'.outMesh',f+'.inputMesh',f=1)
        cmds.connectAttr(fo+'.worldMatrix',f+'.inputWorldMatrix',f=1)
        cmds.setAttr(f+'.parameterU',u)
        cmds.setAttr(f+'.parameterV',v)
        allFollicle.append(t)
    cmds.delete(cn,locs)
    return allFollicle
    
def edo_setBlendShapeAllValueOn(bs):
    #bs='BS_SFD_lfeyebrow'
    wc=cmds.blendShape(bs,q=1,wc=1)
    for i in range(0,wc):
        cmds.blendShape(bs,e=1,w=[i,1.0])

def edo_createSDsecctrlBlendshape(org,fo):
    ps=cmds.listRelatives(org,p=1)
    if not ps==None:
        cmds.parent(org,w=1)
    tmp=cmds.duplicate(org,n=org+'_tmp')[0]
    tmp_=org
    org=cmds.rename(org,org+'_skin')
    scm=cmds.rename(tmp,tmp_)
    fobs=cmds.blendShape(fo,n='FO_facial_blendshape')
    scbs=cmds.blendShape(scm,n='SD_facial_blendshape')
    cmds.blendShape(fobs[0],e=1,t=[fo,0,org,1.0],w=[0,1.0])
    cmds.blendShape(scbs[0],e=1,t=[scm,0,org,1.0],w=[0,1.0])
    if not ps==None:
        cmds.parent(scm,ps[0])
    cmds.setAttr(org+'.v',0)
    cmds.setAttr(fo+'.v',0)
    return [org,scm]

#edo_transferSDHtoSKJ(0)
def edo_transferSDHtoSKJ(nl=0):
    #nl=0
    #cmds.undoInfo(undo=0)
    sl=0
    mesh=cmds.ls(sl=1)
    if mesh:
        if len(mesh)>1:
            sl=1
        if sl==0:
            cmds.undoInfo(state=False) 
        m=mesh[0]
        sfctrls=mesh[1:]
        cw=cmds.polyEvaluate(m,v=1)
        sh=cmds.listRelatives(m,s=1,pa=1)[0]
        connect=cmds.listConnections(sh,s=1,d=0,type='skinCluster')
        zj='SKJ_zeroJoint'
        sk='SECSKIN_'+m
        if not cmds.objExists('SKJ_zeroJoint'):
            zj=cmds.createNode('joint',n='SKJ_zeroJoint')
        if not connect:
            if not cmds.objExists(sk):
                if nl==0:
                    sk=cmds.skinCluster(zj,m,dr=4.5,nw=2,fnw=0,n=sk)[0]
        SDHs=cmds.ls('SDH_*',type='softModHandle')
        for s in SDHs:
            #s=SDHs[1]
            pa=cmds.listRelatives(s,p=1,pa=1)
            if pa:
                p=pa[0]
                print p
                if not p in sfctrls and sl==1:
                    continue
                ws=edo_calculateDeformWeight(m,p)
                cmds.delete(s)
                p=cmds.rename(p,p.replace('SDH_','SKJ_'))
                jnt=p.replace('SDH_','SKJ_')+'_JNT'
                if cmds.objExists(jnt):
                    cmds.delete(jnt)
                jnt=cmds.createNode('joint',n=jnt)
                cmds.parent(jnt,p)
                cmds.xform(jnt,os=1,m=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1])
                cmds.skinCluster(sk,edit=True,ai=jnt,wt=0)
                dm=cmds.listConnections(jnt+'.worldMatrix[0]',s=0,d=1,p=1,type='skinCluster')
                if dm:
                    d=dm[0]
                    bd=d.replace('.matrix','.bindPreMatrix')
                    cmds.connectAttr(p+'.parentInverseMatrix[0]',bd,f=1)
                for i in range(0,cw):
                    #i=0
                    if ws[i]<0.005:
                        continue
                    v=m+'.vtx['+str(i)+']'
                    cmds.skinPercent(sk,v,transformValue=([jnt,ws[i]]))
    cmds.undoInfo(state=True) 

def edo_calculateDeformWeight(m,ctrl):
    #m='MSH_c_hi_body_ca_'
    #ctrl='SDH_FOL_locator2_CTRL'
    cmds.xform(ctrl,os=1,t=[0,0,0])
    cw=cmds.polyEvaluate(m,v=1)
    orgpts=[]
    for i in range(0,cw):
        #i=950
        v=m+'.vtx['+str(i)+']'
        t=cmds.xform(v,q=1,ws=1,t=1)
        tz=t[2]
        orgpts.append(tz)
    wt=cmds.xform(ctrl,q=1,ws=1,t=1)
    cmds.xform(ctrl,ws=1,t=[wt[0],wt[1],wt[2]+10])
    ws=[]
    for i in range(0,cw):
        #i=950
        orgpt=orgpts[i]
        v=m+'.vtx['+str(i)+']'
        t=cmds.xform(v,q=1,ws=1,t=1)
        tz=t[2]
        w=(tz-orgpt)*0.1
        ws.append(w)
    cmds.xform(ctrl,os=1,t=[0,0,0])
    print ws
    return ws