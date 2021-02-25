import maya.cmds as cmds
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/GDC_facialRigging_2012/edo_facialCtrlUI.py')

#edo_gdcfrig2012_createCtrl('facialCtrlPanle_FRAME','square',6)
def edo_gdcfrig2012_createCtrl(name,shape='box',colorid=17):
    #name='ctrl'
    #colorid=17
    if shape=='box':
        cmds.curve(n=name,d=1,p=[[-0.5,-0.5,-0.5],[0.5,-0.5,-0.5],[0.5,-0.5,0.5],[-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,0.5,0.5],[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[-0.5,0.5,0.5],[-0.5,0.5,-0.5]])
    if shape=='circle':
        cmds.delete(cmds.circle(ch=1,o=1,nr=[0,1,0],n=name)[1])
    if shape=='square':
        cmds.curve(n=name,d=1,p=[[-10,-10,0],[-10,10,0],[10,10,0],[10,-10,0],[-10,-10,0]])
    cmds.group(name,n='GRP_'+name)
    ss=cmds.listRelatives(name,s=1)[0]
    cmds.rename(ss,name+'Shape')
    cmds.setAttr(name+'Shape.overrideEnabled',1)
    cmds.setAttr(name+'Shape.ovc',colorid)
    
def edo_addAttrToObject(object,attr,type,value,ka=0):
    #object='locator1'
    #attr='driven_up'
    #type='double'
    #value=0
    cmds.addAttr(object,ln=attr,attributeType=type)
    cmds.setAttr(object+'.'+attr,cb=1)
    cmds.setAttr(object+'.'+attr,k=ka)
    cmds.setAttr(object+'.'+attr,value)
    
def edo_gdcfrig2012_ctrlLocation(childobj,parentobj):
    #childobj='GRP_D_ear_l_ctrl'
    #parentobj='D_ear_l_driven'
    cmds.parent(childobj,parentobj)
    cmds.setAttr(childobj+'.tx',l=0)
    cmds.setAttr(childobj+'.ty',l=0)
    cmds.setAttr(childobj+'.tz',l=0)
    cmds.setAttr(childobj+'.rx',l=0)
    cmds.setAttr(childobj+'.ry',l=0)
    cmds.setAttr(childobj+'.rz',l=0)
    cmds.setAttr(childobj+'.sx',l=0)
    cmds.setAttr(childobj+'.sy',l=0)
    cmds.setAttr(childobj+'.sz',l=0)
    cmds.setAttr(childobj+'.tx',0)
    cmds.setAttr(childobj+'.ty',0)
    cmds.setAttr(childobj+'.tz',0)
    cmds.setAttr(childobj+'.rx',0)
    cmds.setAttr(childobj+'.ry',0)
    cmds.setAttr(childobj+'.rz',0)
    cmds.setAttr(childobj+'.sx',1)
    cmds.setAttr(childobj+'.sy',1)
    cmds.setAttr(childobj+'.sz',1)
    cmds.parent(childobj,w=1)   
     
def edo_gdcfrig2012_createEarRig():
    if cmds.objExists('D_ear_l_driven'):
        cmds.makeIdentity('D_ear_l_driven',apply=True,t=1,r=1,s=1,n=0)
        cmds.select('D_ear_l_driven')
        cmds.select(hi=1)
        earjnts=cmds.ls(sl=1,type='joint')
        parents='D_head_driven'
        for jnt in earjnts:
            #jnt=earjnts[0]
            ctrl=jnt.replace('driven','ctrl').replace('skin','ctrl')
            edo_gdcfrig2012_createCtrl(ctrl)
            edo_gdcfrig2012_ctrlLocation('GRP_'+ctrl,jnt)
            cmds.parent('GRP_'+ctrl,parents)
            cmds.parentConstraint(ctrl,jnt,mo=1)
            cmds.scaleConstraint(ctrl,jnt,mo=1)
            parents=ctrl
    if cmds.objExists('D_ear_r_driven'):
        cmds.makeIdentity('D_ear_r_driven',apply=True,t=1,r=1,s=1,n=0)
        cmds.select('D_ear_r_driven')
        cmds.select(hi=1)
        earjnts=cmds.ls(sl=1,type='joint')
        parents='D_head_driven'
        for jnt in earjnts:
            #jnt=earjnts[0]
            ctrl=jnt.replace('driven','ctrl').replace('skin','ctrl')
            edo_gdcfrig2012_createCtrl(ctrl)
            edo_gdcfrig2012_ctrlLocation('GRP_'+ctrl,jnt)
            cmds.parent('GRP_'+ctrl,parents)
            cmds.parentConstraint(ctrl,jnt,mo=1)
            cmds.scaleConstraint(ctrl,jnt,mo=1)
            parents=ctrl
            
def edo_gdcfrig2012_createFacialCtrlPanelFrame():
    edo_gdcfrig2012_createCtrl('facialCtrlPanle_FRAME','square',6)
    cmds.addAttr('facialCtrlPanle_FRAME',ln='frameDisplay',at='enum',en='normal:template:reference')
    cmds.setAttr('facialCtrlPanle_FRAME.frameDisplay',keyable=0)
    cmds.setAttr('facialCtrlPanle_FRAME.frameDisplay',channelBox=1)
    edo_gdcfrig2012_createCtrl('mouth_FRAME','square',6)
    cmds.setAttr('GRP_mouth_FRAME.tx',-3.5)
    cmds.setAttr('GRP_mouth_FRAME.ty',-5.5)
    cmds.setAttr('GRP_mouth_FRAME.sx',0.6)
    cmds.setAttr('GRP_mouth_FRAME.sy',0.4)
    cmds.parent('GRP_mouth_FRAME','facialCtrlPanle_FRAME')
    cmds.setAttr('mouth_FRAMEShape.overrideEnabled',1)
    cmds.connectAttr('facialCtrlPanle_FRAME.frameDisplay','mouth_FRAMEShape.overrideDisplayType',f=1)
    edo_gdcfrig2012_createCtrl('eyelids_FRAME','square',6)
    cmds.setAttr('GRP_eyelids_FRAME.tx',-3.5)
    cmds.setAttr('GRP_eyelids_FRAME.ty',2)
    cmds.setAttr('GRP_eyelids_FRAME.sx',0.6)
    cmds.setAttr('GRP_eyelids_FRAME.sy',0.3)
    cmds.parent('GRP_eyelids_FRAME','facialCtrlPanle_FRAME')
    cmds.setAttr('eyelids_FRAMEShape.overrideEnabled',1)
    cmds.connectAttr('facialCtrlPanle_FRAME.frameDisplay','eyelids_FRAMEShape.overrideDisplayType',f=1)
    edo_gdcfrig2012_createCtrl('eyebrows_FRAME','square',6)
    cmds.setAttr('GRP_eyebrows_FRAME.tx',-3.5)
    cmds.setAttr('GRP_eyebrows_FRAME.ty',7.5)
    cmds.setAttr('GRP_eyebrows_FRAME.sx',0.6)
    cmds.setAttr('GRP_eyebrows_FRAME.sy',0.2)
    cmds.parent('GRP_eyebrows_FRAME','facialCtrlPanle_FRAME')
    cmds.setAttr('eyebrows_FRAMEShape.overrideEnabled',1)
    cmds.connectAttr('facialCtrlPanle_FRAME.frameDisplay','eyebrows_FRAMEShape.overrideDisplayType',f=1)
    edo_gdcfrig2012_createCtrl('nonnasality_FRAME','square',6)
    cmds.setAttr('GRP_nonnasality_FRAME.tx',6)
    cmds.setAttr('GRP_nonnasality_FRAME.ty',-6.5)
    cmds.setAttr('GRP_nonnasality_FRAME.sx',0.35)
    cmds.setAttr('GRP_nonnasality_FRAME.sy',0.3)
    cmds.parent('GRP_nonnasality_FRAME','facialCtrlPanle_FRAME')
    cmds.setAttr('nonnasality_FRAMEShape.overrideEnabled',1)
    cmds.connectAttr('facialCtrlPanle_FRAME.frameDisplay','nonnasality_FRAMEShape.overrideDisplayType',f=1)
    edo_gdcfrig2012_createCtrl('others_FRAME','square',6)
    cmds.setAttr('GRP_others_FRAME.tx',6)
    cmds.setAttr('GRP_others_FRAME.ty',3.25)
    cmds.setAttr('GRP_others_FRAME.sx',0.35)
    cmds.setAttr('GRP_others_FRAME.sy',0.625)
    cmds.parent('GRP_others_FRAME','facialCtrlPanle_FRAME')
    cmds.setAttr('others_FRAMEShape.overrideEnabled',1)
    cmds.connectAttr('facialCtrlPanle_FRAME.frameDisplay','others_FRAMEShape.overrideDisplayType',f=1)
    cmds.makeIdentity('GRP_facialCtrlPanle_FRAME',apply=True,t=1,r=1,s=1,n=0)
    
def edo_gdcfrig2012_createFacialCtrlPanelMouthCtrl():
    edo_addFacialCtrlCmd('D_jaw','mouth_FRAME')
    cmds.setAttr('GRP_D_jaw_FRAME.tx',-3.5)
    cmds.setAttr('GRP_D_jaw_FRAME.ty',-7)
    cmds.setAttr('GRP_D_jaw_FRAME.sx',1.2)
    cmds.setAttr('GRP_D_jaw_FRAME.sy',1.2)
    edo_addFacialCtrlCmd('D_nose','mouth_FRAME')
    cmds.setAttr('GRP_D_nose_FRAME.tx',-3.5)
    cmds.setAttr('GRP_D_nose_FRAME.ty',-2.5)
    edo_addFacialCtrlCmd('D_mouthSide_l','mouth_FRAME')
    cmds.setAttr('GRP_D_mouthSide_l_FRAME.tx',-8.5)
    cmds.setAttr('GRP_D_mouthSide_l_FRAME.ty',-7)
    edo_addFacialCtrlCmd('D_mouthSide_r','mouth_FRAME')
    cmds.setAttr('GRP_D_mouthSide_r_FRAME.tx',1.5)
    cmds.setAttr('GRP_D_mouthSide_r_FRAME.ty',-7)
    edo_addFacialCtrlCmd('D_cheeck_l','mouth_FRAME')
    cmds.setAttr('GRP_D_cheeck_l_FRAME.tx',-8.5)
    cmds.setAttr('GRP_D_cheeck_l_FRAME.ty',-2.5)
    edo_addFacialCtrlCmd('D_cheeck_r','mouth_FRAME')
    cmds.setAttr('GRP_D_cheeck_r_FRAME.tx',1.5)
    cmds.setAttr('GRP_D_cheeck_r_FRAME.ty',-2.5)
    muplips=cmds.ls('D_uplip_m_skin')
    for lip in muplips:
        #lip=muplips[0]
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-3.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-5)  
    mdnlips=cmds.ls('D_dnlip_m_skin')
    for lip in mdnlips:
        #lip=mdnlips[0]
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-3.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-9)  
    lfuplips=cmds.ls('D_uplip_l_*_skin')
    size=float(len(lfuplips))
    weith=5.0
    pw=(5.0-size)/(size+1.0)
    stx=-3.5
    for lip in lfuplips:
        #lip=lfuplips[0]
        stx+=pw+1
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-5)
    rtuplips=cmds.ls('D_uplip_r_*_skin')
    stx=-3.5
    for lip in rtuplips:
        #lip=lfuplips[0]
        stx-=pw+1
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-5)
    lfdnlips=cmds.ls('D_dnlip_l_*_skin')
    stx=-3.5
    for lip in lfdnlips:
        #lip=lfuplips[0]
        stx+=pw+1
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-9)
    rtdnlips=cmds.ls('D_dnlip_r_*_skin')
    stx=-3.5
    for lip in rtdnlips:
        #lip=lfuplips[0]
        stx-=pw+1
        ctrlname=lip.replace('_skin','')
        edo_addFacialCtrlCmd(ctrlname,'mouth_FRAME')
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
        cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-9)
        
def edo_gdcfrig2012_createFacialCtrlPanelNonnasalityCtrl():
    if not cmds.objExists('D_tongue_driven'):
        return False
    ctrlname='D_tongue'
    edo_addFacialCtrlCmd(ctrlname,'nonnasality_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',6)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-6.5)
    if not cmds.objExists('D_upteeth_driven'):
        return False
    ctrlname='D_upteeth'
    edo_addFacialCtrlCmd(ctrlname,'nonnasality_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-4.5)
    ctrlname='D_upteeth_scale'
    edo_addFacialCtrlCmd(ctrlname,'nonnasality_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',7)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-4.5)
    if not cmds.objExists('D_dnteeth_driven'):
        return False
    ctrlname='D_dnteeth'
    edo_addFacialCtrlCmd(ctrlname,'nonnasality_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-8.5)
    ctrlname='D_dnteeth_scale'
    edo_addFacialCtrlCmd(ctrlname,'nonnasality_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',7)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',-8.5)
    
def edo_gdcfrig2012_createFacialCtrlPanelEyelidsCtrl():
    weith=5.0
    ctrlname='D_uplid_l'
    edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-0.5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',4)
    ctrlname='D_uplid_r'
    edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-6.5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',4)
    ctrlname='D_dnlid_l'
    edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-0.5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',0)
    ctrlname='D_dnlid_r'
    edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.8)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',-6.5)
    cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',0)
    lfeyelids=cmds.ls('D_uplid_l_*_skin')
    size=float(len(lfeyelids))
    pw=0
    if (size>1):
        pw=(5.0-size)/(size-1.0)  
        stx=-2.5
        for lflid in lfeyelids:
            #lflid=lfeyelids[0]
            ctrlname=lflid.replace('_skin','')
            edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',2.5)
            stx+=(pw+1)
    rteyelids=cmds.ls('D_uplid_r_*_skin')
    size=float(len(rteyelids))
    pw=0
    if (size>1):
        pw=(5.0-size)/(size-1.0)  
        stx=-4.5
        for lflid in rteyelids:
            #lflid=lfeyelids[0]
            ctrlname=lflid.replace('_skin','')
            edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',2.5)
            stx-=(pw+1)
    dnlfeyelids=cmds.ls('D_dnlid_l_*_skin')
    size=float(len(dnlfeyelids))
    pw=0
    if (size>1):
        pw=(5.0-size)/(size-1.0)  
        stx=-2.5
        for lflid in dnlfeyelids:
            #lflid=lfeyelids[0]
            ctrlname=lflid.replace('_skin','')
            edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',1.5)
            stx+=(pw+1)
    dnrteyelids=cmds.ls('D_dnlid_r_*_skin')
    size=float(len(rteyelids))
    pw=0
    if (size>1):
        pw=(5.0-size)/(size-1.0)  
        stx=-4.5
        for lflid in dnrteyelids:
            #lflid=lfeyelids[0]
            ctrlname=lflid.replace('_skin','')
            edo_addFacialCtrlCmd(ctrlname,'eyelids_FRAME')
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sx',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.sy',0.5)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.tx',stx)
            cmds.setAttr('GRP_'+ctrlname+'_FRAME.ty',1.5)
            stx-=(pw+1)
            
def edo_gdcfrig2012_addFacialCtrlPanelAttribute():
    if cmds.objExists('D_nose_CTRL'):
        edo_addAttrToObject('D_nose_CTRL','stretch','double',0,1)
    if cmds.objExists('D_tongue_CTRL'):
        edo_addAttrToObject('D_tongue_CTRL','stretch','double',0,1)   


def edo_gdcfrig2012_createFacialCtrlPanel():
    edo_gdcfrig2012_createFacialCtrlPanelFrame()
    edo_gdcfrig2012_createFacialCtrlPanelMouthCtrl()
    edo_gdcfrig2012_createFacialCtrlPanelNonnasalityCtrl()
    edo_gdcfrig2012_createFacialCtrlPanelEyelidsCtrl()
    edo_gdcfrig2012_addFacialCtrlPanelAttribute()
    

def edo_gdcfrig2012_createFacialRig():
    edo_gdcfrig2012_createFacialCtrlPanel()
    edo_gdcfrig2012_createEarRig()
    edo_gdcfrig2012_createNoseRig()
    edo_gdcfrig2012_createTongueRig()

def edo_gdcfrig2012_createTongueRig():
    if cmds.objExists('D_tongue_driven'):
        cmds.makeIdentity('D_tongue_driven',apply=True,t=1,r=1,s=1,n=0)
        cmds.select('D_tongue_driven')
        cmds.select(hi=1)
        tonguejnts=cmds.ls(sl=1,type='joint')
        parents='D_jaw_driven'
        num=float(len(tonguejnts))
        twistValue=60/num
        driven_upValue=60/num
        driven_dnValue=60/num
        driven_lfValue=60/num
        driven_rtValue=60/num
        driven_stretchValue=5/num
        driven_stretchValue=5/num
        for jnt in tonguejnts:
            #jnt=tonguejnts[0]
            if jnt==tonguejnts[len(tonguejnts)-1]:
                cmds.setAttr(jnt+'.jointOrientX',0)
                cmds.setAttr(jnt+'.jointOrientY',0)
                cmds.setAttr(jnt+'.jointOrientZ',0)
            ctrl=jnt.replace('driven','ctrl').replace('skin','ctrl')
            edo_gdcfrig2012_createCtrl(ctrl)
            edo_gdcfrig2012_ctrlLocation('GRP_'+ctrl,jnt)
            cmds.group(ctrl,n='DIV_'+ctrl)
            cmds.xform('DIV_'+ctrl,os=1,piv=[0,0,0])
            cmds.parent('GRP_'+ctrl,parents)
            cmds.parentConstraint(ctrl,jnt,mo=1)
            cmds.scaleConstraint(ctrl,jnt,mo=1)
            parents=ctrl
            edo_addAttrToObject(ctrl,'driven_up','double',driven_upValue*-1.0)
            edo_addAttrToObject(ctrl,'driven_dn','double',driven_dnValue)
            edo_addAttrToObject(ctrl,'driven_lf','double',driven_lfValue*-1.0)
            edo_addAttrToObject(ctrl,'driven_rt','double',driven_rtValue)
            edo_addAttrToObject(ctrl,'driven_twist','double',twistValue)
            edo_addAttrToObject(ctrl,'driven_stretch','double',driven_stretchValue)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenUp')
            cmds.connectAttr('D_tongue_FRAME.fourAxis_up',multip+'.input1X',f=1)
            cmds.connectAttr('D_tongue_FRAME.fourAxis_lf',multip+'.input1Y',f=1)
            cmds.connectAttr(ctrl+'.driven_up',multip+'.input2X',f=1)
            cmds.connectAttr(ctrl+'.driven_lf',multip+'.input2Y',f=1)
            plus=cmds.createNode('plusMinusAverage',n='D_plus_'+ctrl+'_dirven')
            cmds.connectAttr(multip+'.outputX',plus+'.input3D[0].input3Dx',f=1)
            cmds.connectAttr(multip+'.outputY',plus+'.input3D[0].input3Dy',f=1)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenDn')
            cmds.connectAttr('D_tongue_FRAME.fourAxis_dn',multip+'.input1X',f=1)
            cmds.connectAttr('D_tongue_FRAME.fourAxis_rt',multip+'.input1Y',f=1)
            cmds.connectAttr(ctrl+'.driven_dn',multip+'.input2X',f=1)
            cmds.connectAttr(ctrl+'.driven_rt',multip+'.input2Y',f=1)
            cmds.connectAttr(multip+'.outputX',plus+'.input3D[1].input3Dx',f=1)
            cmds.connectAttr(multip+'.outputY',plus+'.input3D[1].input3Dy',f=1)
            cmds.connectAttr(plus+'.output3D.output3Dx','DIV_'+ctrl+'.rx',f=1)
            cmds.connectAttr(plus+'.output3D.output3Dy','DIV_'+ctrl+'.ry',f=1)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenTwist')
            cmds.connectAttr('D_tongue_CTRL.rz',multip+'.input1X',f=1)
            cmds.connectAttr(ctrl+'.driven_twist',multip+'.input2X',f=1)
            divide=cmds.createNode('multiplyDivide',n='D_divide_'+ctrl+'_dirvenTwist')
            cmds.connectAttr(multip+'.outputX',divide+'.input1X',f=1)
            cmds.setAttr(divide+'.input2X',30)
            cmds.setAttr(divide+'.operation',2)
            cmds.connectAttr(divide+'.outputX','DIV_'+ctrl+'.rz',f=1)
            cmds.connectAttr(ctrl+'.driven_stretch',multip+'.input1Y',f=1)
            cmds.connectAttr('D_tongue_CTRL.stretch',multip+'.input2Y',f=1)
            cmds.connectAttr(multip+'.outputY','DIV_'+ctrl+'.tz',f=1)
        
def edo_gdcfrig2012_createNoseRig():
    if cmds.objExists('D_nose_driven'):
        cmds.makeIdentity('D_nose_driven',apply=True,t=1,r=1,s=1,n=0)
        cmds.select('D_nose_driven')
        cmds.select(hi=1)
        nosejnts=cmds.ls(sl=1,type='joint')
        parents='D_head_driven'
        num=float(len(nosejnts))
        twistValue=60/num
        driven_upValue=60/num
        driven_dnValue=60/num
        driven_lfValue=60/num
        driven_rtValue=60/num
        driven_stretchValue=5/num
        for jnt in nosejnts:
            #jnt=nosejnts[0]
            if jnt==nosejnts[len(nosejnts)-1]:
                cmds.setAttr(jnt+'.jointOrientX',0)
                cmds.setAttr(jnt+'.jointOrientY',0)
                cmds.setAttr(jnt+'.jointOrientZ',0)
            ctrl=jnt.replace('driven','ctrl').replace('skin','ctrl')
            edo_gdcfrig2012_createCtrl(ctrl)
            edo_gdcfrig2012_ctrlLocation('GRP_'+ctrl,jnt)
            cmds.group(ctrl,n='DIV_'+ctrl)
            cmds.xform('DIV_'+ctrl,os=1,piv=[0,0,0])
            cmds.parent('GRP_'+ctrl,parents)
            cmds.parentConstraint(ctrl,jnt,mo=1)
            cmds.scaleConstraint(ctrl,jnt,mo=1)
            parents=ctrl
            edo_addAttrToObject(ctrl,'driven_up','double',driven_upValue*-1.0)
            edo_addAttrToObject(ctrl,'driven_dn','double',driven_dnValue)
            edo_addAttrToObject(ctrl,'driven_lf','double',driven_lfValue*-1.0)
            edo_addAttrToObject(ctrl,'driven_rt','double',driven_rtValue)
            edo_addAttrToObject(ctrl,'driven_twist','double',twistValue)
            edo_addAttrToObject(ctrl,'driven_stretch','double',driven_stretchValue)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenUp')
            cmds.connectAttr('D_nose_FRAME.fourAxis_up',multip+'.input1X',f=1)
            cmds.connectAttr('D_nose_FRAME.fourAxis_lf',multip+'.input1Y',f=1)
            cmds.connectAttr(ctrl+'.driven_up',multip+'.input2X',f=1)
            cmds.connectAttr(ctrl+'.driven_lf',multip+'.input2Y',f=1)
            plus=cmds.createNode('plusMinusAverage',n='D_plus_'+ctrl+'_dirven')
            cmds.connectAttr(multip+'.outputX',plus+'.input3D[0].input3Dx',f=1)
            cmds.connectAttr(multip+'.outputY',plus+'.input3D[0].input3Dy',f=1)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenDn')
            cmds.connectAttr('D_nose_FRAME.fourAxis_dn',multip+'.input1X',f=1)
            cmds.connectAttr('D_nose_FRAME.fourAxis_rt',multip+'.input1Y',f=1)
            cmds.connectAttr(ctrl+'.driven_dn',multip+'.input2X',f=1)
            cmds.connectAttr(ctrl+'.driven_rt',multip+'.input2Y',f=1)
            cmds.connectAttr(multip+'.outputX',plus+'.input3D[1].input3Dx',f=1)
            cmds.connectAttr(multip+'.outputY',plus+'.input3D[1].input3Dy',f=1)
            cmds.connectAttr(plus+'.output3D.output3Dx','DIV_'+ctrl+'.rx',f=1)
            cmds.connectAttr(plus+'.output3D.output3Dy','DIV_'+ctrl+'.ry',f=1)
            multip=cmds.createNode('multiplyDivide',n='D_multip_'+ctrl+'_dirvenTwist')
            cmds.connectAttr('D_nose_CTRL.rz',multip+'.input1X',f=1)
            cmds.connectAttr(ctrl+'.driven_twist',multip+'.input2X',f=1)
            divide=cmds.createNode('multiplyDivide',n='D_divide_'+ctrl+'_dirvenTwist')
            cmds.connectAttr(multip+'.outputX',divide+'.input1X',f=1)
            cmds.setAttr(divide+'.input2X',30)
            cmds.setAttr(divide+'.operation',2)
            cmds.connectAttr(divide+'.outputX','DIV_'+ctrl+'.rz',f=1)
            cmds.connectAttr(ctrl+'.driven_stretch',multip+'.input1Y',f=1)
            cmds.connectAttr('D_nose_CTRL.stretch',multip+'.input2Y',f=1)
            cmds.connectAttr(multip+'.outputY','DIV_'+ctrl+'.tz',f=1)

#def edo_gdcfrig2012_createTongueRig():
  
#def edo_gdcfrig2012_createTeethRig():

#def edo_gdcfrig2012_createJawRig():

#def edo_gdcfrig2012_createEyesRig():

#def edo_gdcfrig2012_combineRig():