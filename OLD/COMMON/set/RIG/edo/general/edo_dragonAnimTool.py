import maya.cmds as cmds
import maya.mel as mel
execfile('//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_addContorlToJointChain.py')

def edo_dragonAnimToolUI():
    ui='//file-cluster/GDC/Resource/Support/Maya/extra/Rigging_Simulation/python/edo/general/edo_dragonAnimTool.myuis'
    if cmds.window('edo_dragonAnimToolUI',ex=1):
        cmds.deleteUI('edo_dragonAnimToolUI')
    mui=cmds.loadUI(f=ui)
    cmds.showWindow(mui)
    #add button cmd
    cmds.button('edo_dragonAnimToolUI_tab1_group1_bt1',e=1,c='edo_createSurfaceControlAndTransferSurface()')
    #cmds.button('edo_dragonAnimToolUI_tab1_group1_bt3',e=1,c='edo_transferDragonPath()')
    #cmds.button('edo_dragonAnimToolUI_tab1_group1_bt2',e=1,c='edo_createSurfaceControlAndTransferSurface()')
    cmds.button('edo_dragonAnimToolUI_tab1_group1_bt2',e=1,c='edo_resetDefualtDragonPath()')
    #cmds.button('edo_dragonAnimToolUI_tab1_group1_bt3',e=1,c='edo_transferDragonPath(cmds.ls(sl=1)[0])')
    #
    cmds.button('edo_dragonAnimToolUI_tab2_group1_bt1',e=1,c='edo_createNoneRollIkSpline()')
    cmds.button('edo_dragonAnimToolUI_tab2_group1_bt2',e=1,c='edo_createSurfaceControlPointCtrl(cmds.ls(sl=1)[0])')
edo_dragonAnimToolUI()

def edo_getNamespace(sel):
    #sel='aaa:bbb:ccc:ddd'
    ns=''
    if not sel:
        return ns
    sp=sel.split(':')
    if len(sp)<=1:
        return ns
    for i in range(0,len(sp)-1):
        #print i
        t=sp[i]
        ns=ns+t+':'
    return ns
    
def edo_transferDragonPath(sels):
    print 'edo_transferDragonPath'
    if not sels:
        sels=cmds.ls(sl=1)
    if sels:
        #newpath=directSuf
        #oldpath=sourceSuf
        newpath=sels[0]
        oldpath=sels[1]
        cmds.makeIdentity(newpath,apply=1,t=1,r=1,s=1,n=0)
        ns=edo_getNamespace(oldpath)
        midn=oldpath.split(':')[-1].split('_')[1]
        cmidn=midn.replace('surface','curve')
        lfc=ns+'DRAGON_'+cmidn+'_loft01'
        rtc=ns+'DRAGON_'+cmidn+'_loft02'
        lfnc=cmds.duplicateCurve(newpath+'.v[0]',ch=1,rn=0,local=0,n='new_DRAGON_'+cmidn+'_loft01')[0]
        rtnc=cmds.duplicateCurve(newpath+'.v[1]',ch=1,rn=0,local=0,n='new_DRAGON_'+cmidn+'_loft02')[0]
        cmds.connectAttr(lfnc+'.local',lfc+'.create',f=1)
        cmds.connectAttr(rtnc+'.local',rtc+'.create',f=1)
        edo_setCurvePointZero([lfc,rtc])
        rsg=cmds.ls('GRP_'+midn+'_rebuildSurace_*')
        if rsg:
            cmds.delete(rsg)
        grp=cmds.group([lfnc,rtnc],n='GRP_'+midn+'_rebuildSurace_')
        try:
            cmds.parent(newpath,grp)
        except:
            print 'something can not group'
        #cmds.delete(grp)
        cmds.setAttr(grp+'.v',0)
        refgrp=cmds.ls('*:GRP_'+midn+'_rebuildSurace_')
        if refgrp:
            cmds.setAttr(refgrp[0]+'.v',0)
        return grp
        
def edo_setCurvePointZero(curves):
    #curves
    if curves:
        for c in curves:
            #c='dragon_path:DRAGON_curve_loft02'
            sp=cmds.getAttr(c+'.spans')
            dg=cmds.getAttr(c+'.degree')
            cvs=sp+dg
            for i in range(0,cvs):
                #i=0
                cv=c+'.controlPoints['+str(i)+']'
                cmds.setAttr(cv+'.xValue',0)
                cmds.setAttr(cv+'.yValue',0)
                cmds.setAttr(cv+'.zValue',0)
                
def edo_setSurfacePointZero(surfaces):
    #curves
    if surfaces:
        for s in surfaces:
            #s='DRAGON_surface_normal5'
            unum=cmds.getAttr(s+'.spansUV.spansU')+cmds.getAttr(s+'.degreeUV.degreeU')
            vnum=cmds.getAttr(s+'.spansUV.spansV')+cmds.getAttr(s+'.degreeUV.degreeV')
            for u in range(0,unum):
                #u=0
                for v in range(0,vnum):
                    #v=0
                    cv=s+'.controlPoints['+str(u)+']['+str(v)+']'
                    cmds.setAttr(cv+'.xValue',0)
                    cmds.setAttr(cv+'.yValue',0)
                    cmds.setAttr(cv+'.zValue',0)

def edo_resetDefualtDragonPath():
    sels=cmds.ls(sl=1)
    if sels:
        oldpath=sels[0]
        ns=edo_getNamespace(oldpath)
        lfrc=ns+'rebuildCurve1'
        rtrc=ns+'rebuildCurve2'
        lfc=ns+'DRAGON_curve_loft01'
        rtc=ns+'DRAGON_curve_loft02'
        cmds.connectAttr(lfrc+'.outputCurve',lfc+'.create',f=1)
        cmds.connectAttr(rtrc+'.outputCurve',rtc+'.create',f=1)
        edo_setCurvePointZero([lfc,rtc])
        
def edo_createCurvePointLoc(cv,space='local'):
    #cv='DRAGON_curve_loft0Shape1.controlPoints[51]'
    po=cmds.xform(cv,q=1,ws=1,t=1)
    loc=cmds.spaceLocator(n=cv)[0]
    grp=cmds.group(loc,n='GRP_'+loc)
    cmds.xform(grp,ws=1,t=po)
    if space=='locap':
        cmds.connectAttr(loc+'.translate',cv,f=1)
    if space=='world':
        cmds.connectAttr(loc+'.worldPosition',cv,f=1)
    return [loc,grp]

#def edo_createCurveCtrl(curves):
#    if cmds.objExists()
#    #curves=['DRAGON_curve_loft01','DRAGON_curve_loft02']
#    lfc=curves[0]
#    rtc=curves[1]
#    cvn=cmds.getAttr(lfc+'.spans')+cmds.getAttr(lfc+'.degree')
#    for i in range(0,cvn):
#        lfcv=lfc+'.controlPoints['+str(i)+']'
#        rtcv=lfc+'.controlPoints['+str(i)+']'
#

#
def edo_createSurfaceControlAndTransferSurface():
    print 'transfer surface and createRig'
    sels=cmds.ls(sl=1)
    if sels:
        if len(sels)==2:
            directSuf=sels[0]
            sourceSuf=sels[1]
            try:
                directSuf=edo_createSurfaceControlPointCtrl(directSuf)
                edo_transferDragonPath([directSuf,sourceSuf])
            except:
                mel.eval("error \"something was wrong!\"")
            
#edo_createSurfaceControlPointCtrl(cmds.ls(sl=1)[0])
def edo_createSurfaceControlPointCtrl(suf):
    #suf=directSuf
    try:
        suf=cmds.parent(suf,w=1)[0]
    except:
        print 'this surface has been in the world!'
    midn=suf.split('_')[1]
    if cmds.objExists('GRP_'+midn+'_controlPoint_ctrl'):
        cmds.delete('GRP_'+midn+'_controlPoint_ctrl')
    if cmds.objExists('GRP_'+midn+'_controlPoint_loc'):
        cmds.delete('GRP_'+midn+'_controlPoint_loc')
    if cmds.objExists('DRAGON_'+midn+'_duplicate_'):
        cmds.delete('DRAGON_'+midn+'_duplicate_')
    try:
        suf=cmds.rename(suf,'DRAGON_'+midn+'_duplicate_')
    except:
        print 'this is reference surface,can not add rig'
        return False
    suf_rig=cmds.ls('GRP_DRAGON_'+midn+'_rig*')
    if suf_rig:
        cmds.delete(suf_rig)
    cmds.makeIdentity(suf,apply=1,t=1,r=1,s=1,n=0)
    ccurve=cmds.duplicateCurve(suf+'.v[0.5]',ch=1,rn=0,local=0)[0]
    cmds.createNode('transform',n='GRP_'+midn+'_controlPoint_ctrl')
    cmds.createNode('transform',n='GRP_'+midn+'_controlPoint_loc')
    cmds.parent('GRP_'+midn+'_controlPoint_loc','GRP_'+midn+'_controlPoint_ctrl')
    uspans=cmds.getAttr(suf+'.spansUV.spansU')
    udegree=cmds.getAttr(suf+'.degreeUV.degreeU')
    vspans=cmds.getAttr(suf+'.spansUV.spansV')
    vdegree=cmds.getAttr(suf+'.degreeUV.degreeV')
    unum=uspans+udegree
    vnum=vspans+vdegree
    #cid=int(vnum/2)
    firstjnt=''
    pjnt=''
    for iu in range(0,unum):
        #u=0
        u=(unum-1)-iu
        #ccv=suf+'.cv['+str(u)+']['+str(cid)+']'
        po1=cmds.xform(suf+'.cv['+str(u)+'][0]',q=1,ws=1,t=1)
        po2=cmds.xform(suf+'.cv['+str(u)+']['+str(vnum-1)+']',q=1,ws=1,t=1)
        po=[(po1[0]+po2[0])*0.5,(po1[1]+po2[1])*0.5,(po1[2]+po2[2])*0.5]
        jnt=cmds.createNode('joint',n=suf+'_jnt_cv'+str(u))
        upjnt=cmds.createNode('joint',n=suf+'_jnt_cv'+str(u))
        cmds.xform(jnt,ws=1,t=po)
        cmds.xform(upjnt,ws=1,t=po)
        cmds.delete(cmds.normalConstraint(suf,upjnt,aimVector=[0,-1,0]))
        cmds.delete(cmds.tangentConstraint(ccurve,jnt,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='objectrotation',worldUpObject=upjnt))
        cmds.delete(upjnt)
        if pjnt=='':
            cmds.parent(jnt,'GRP_'+midn+'_controlPoint_loc')
            pjnt=jnt
            firstjnt=jnt
        else:
            cmds.parent(jnt,pjnt)
            pjnt=jnt
        for v in range(0,vnum):
            #v=0
            cv=suf+'.cv['+str(u)+']['+str(v)+']'
            locs=edo_createCurvePointLoc(cv,'world')
            cmds.parent(locs[1],jnt)
    cmds.makeIdentity(firstjnt,apply=1,t=1,r=1,s=1,n=0)
    cmds.delete(ccurve)
    nsuf=cmds.duplicate(suf)[0]
    grp=cmds.group(suf,nsuf,n='GRP_DRAGON_'+midn+'_rig')
    cmds.parent(grp,'GRP_'+midn+'_controlPoint_ctrl')
    cmds.connectAttr(suf+'.local',nsuf+'.create',f=1)
    edo_setSurfacePointZero([nsuf])
    cmds.setAttr(suf+'.v',0)
    cmds.setAttr('GRP_'+midn+'_controlPoint_loc.v',0)
    cmds.select(firstjnt)
    firstCtrl=edo_addContorlToJointChain()
    cmds.parent(firstCtrl,'GRP_'+midn+'_controlPoint_ctrl')
    refctrls=cmds.ls('*:GRP_'+midn+'_controlPoint_ctrl')
    if refctrls:
        cmds.setAttr(refctrls[0]+'.v',0)
    return suf
    
def edo_createNoneRollIkSpline():
    sels=cmds.ls(sl=1)
    tipjnt=cmds.ls(sels,type='joint')[0]
    sels.remove(tipjnt)
    suf=sels[0]
    ikjnt=cmds.duplicate(tipjnt,n=tipjnt.replace('_jnt','_ikjnt'))
    cmds.select(ikjnt[0],hi=1)
    mel.eval("searchReplaceNames \"_jnt\" \"_ikjnt\" \"hierarchy\";")
    alljnts=cmds.ls(sl=1,type='joint')
    tip=alljnts[0]
    tail=alljnts[len(alljnts)-1]
    #add ik spline curve
    ikcurve=cmds.duplicateCurve(suf+".v[0.5]",ch=1,rn=0,local=0,n=suf+'_iksplineCurve')
    ikc=ikcurve[0]
    #find bind pose
    poc=cmds.createNode('nearestPointOnCurve')
    cmds.connectAttr(ikc+'.local',poc+'.inputCurve',f=1)
    ploc=cmds.spaceLocator()
    cmds.delete(cmds.pointConstraint(tip,ploc[0],mo=0))
    cmds.connectAttr(ploc[0]+'.translate',poc+'.inPosition',f=1)
    pa=cmds.getAttr(poc+'.parameter')
    ikh=cmds.ikHandle(sj=tip,ee=tail,c=ikc,sol='ikSplineSolver',ccv=0,n=ikc+'_ikHandle')
    ikhandle=ikh[0]
    cmds.setAttr(ikhandle+'.offset',pa)
    cmds.delete(poc,ploc)
    cmds.addAttr(ikhandle,ln='motionOffset',at='double',min=-100,max=100,dv=0)
    cmds.setAttr(ikhandle+'.motionOffset',e=1,k=1)
    cmds.addAttr(ikhandle,ln='autoStreatch',at='double',min=0,max=1,dv=0)
    cmds.setAttr(ikhandle+'.autoStreatch',e=1,k=1)
    cmds.addAttr(ikhandle,ln='globalScale',at='double',dv=1)
    cmds.setAttr(ikhandle+'.globalScale',e=1,k=1)
    cif=cmds.createNode('curveInfo')
    cmds.connectAttr(ikc+'.worldSpace',cif+'.inputCurve',f=1)
    exstr=ikhandle+".offset=("+ikhandle+".motionOffset*0.01)+"+str(pa)+";"
    ex=cmds.expression(s=exstr,o=ikhandle,ae=1,uc=all)
    #add closestPointOnSurface
    print 'add closestPointOnSurface'
    if not cmds.objExists('GRP_NONEROLL_IKSPLINE_LOC'):
        cmds.createNode('transform',n='GRP_NONEROLL_IKSPLINE_LOC')
    for jnt in alljnts:
        #jnt=alljnts[0]
        djnt=jnt.replace('_ikjnt','_jnt')
        cmds.pointConstraint(jnt,djnt,mo=0)
        pos=cmds.createNode('closestPointOnSurface',n=jnt+'_CPOS')
        cmds.connectAttr(suf+'.worldSpace',pos+'.inputSurface',f=1)
        ploc=cmds.spaceLocator(n=jnt+'_LOC')
        cmds.parent(ploc,'GRP_NONEROLL_IKSPLINE_LOC')
        cmds.pointConstraint(jnt,ploc,mo=0)
        plocs=cmds.listRelatives(ploc,s=1,pa=1)[0]
        cmds.connectAttr(plocs+'.worldPosition',pos+'.inPosition',f=1)
        pocinfo=cmds.createNode('pointOnSurfaceInfo',n=jnt+'_CPOSIF')
        cmds.connectAttr(suf+'.worldSpace',pocinfo+'.inputSurface',f=1)
        cmds.connectAttr(pos+'.parameterU',pocinfo+'.parameterU',f=1)
        cmds.connectAttr(pos+'.parameterV',pocinfo+'.parameterV',f=1)
        print 'tangentConstraint ... '+ikcurve[0]+'  ...  '+djnt
        tanc=cmds.tangentConstraint(ikcurve[0],djnt,aimVector=[1,0,0],upVector=[0,1,0],worldUpType='vector')
        cmds.connectAttr(pocinfo+'.normal',tanc[0]+'.worldUpVector',f=1)
    cmds.setAttr('GRP_NONEROLL_IKSPLINE_LOC.v',0)
    #add as
    length=cmds.getAttr(cif+'.arcLength')
    m1=cmds.createNode('multiplyDivide')
    cmds.setAttr(m1+'.input1X',length)
    cmds.connectAttr(ikhandle+'.globalScale',m1+'.input2X',f=1)
    m2=cmds.createNode('multiplyDivide')
    cmds.setAttr(m2+'.operation',2)
    cmds.connectAttr(cif+'.arcLength',m2+'.input1X',f=1)
    cmds.connectAttr(m1+'.outputX',m2+'.input2X',f=1)
    for jnt in alljnts[1:]:
        #jnt=alljnts[1]
        tx=cmds.getAttr(jnt+'.tx')
        m=cmds.createNode('multiplyDivide')
        cmds.setAttr(m+'.input1X',tx)
        cmds.connectAttr(m2+'.outputX',m+'.input2X',f=1)
        bd=cmds.createNode('blendColors')
        cmds.setAttr(bd+'.color2R',tx)
        cmds.connectAttr(m+'.outputX',bd+'.color1R',f=1)
        cmds.connectAttr(bd+'.outputR',jnt+'.tx')
        cmds.connectAttr(ikhandle+'.autoStreatch',bd+'.blender',f=1)
        
def edo_creatNoneRollIkCtrl(noneRollIkJnt):
    #noneRollIkJnt=cmds.ls(sl=1)[0]
    skjnt=cmds.duplicate(noneRollIkJnt,n=noneRollIkJnt.replace('_jnt','_skjnt'))
    cmds.select(skjnt[0],hi=1)
    mel.eval("searchReplaceNames \"_jnt\" \"_skjnt\" \"hierarchy\";")
    allskjnts=cmds.ls(sl=1,type='joint')
    for jnt in allskjnts:
        #skjnt=allskjnts[0]
        jnt=skjnt.replace('_skjnt','_jnt')


def edo_findAllChildJnts(jnt):
    #jnt='DRAGON_tail_jnt0'
    cmds.select(jnt,hi=1)
    alljnts=cmds.ls(sl=1,type='joint')
    cmds.select(cl=1)
    return alljnts
    

def edo_sumJointChainTransform(jntA,jntB,fjnt):
    #jntA='DRAGON_tail_jnt0'
    #jntB='DRAGON_tail_control_jnt0'
    #fjnt='DRAGON_tail_skjnt0'
    alljntA=edo_findAllChildJnts(jntA)
    alljntB=edo_findAllChildJnts(jntB)
    alljntC=edo_findAllChildJnts(fjnt)
    if len(alljntA)==len(alljntB)==len(alljntC):
        for i in range(0,len(alljntA)-1):
            print i
            #i=0
            jnta=alljntA[i]
            jntb=alljntB[i]
            jntc=alljntC[i]
            plusT=cmds.createNode('plusMinusAverage',n=jntc+'_plusT')
            cmds.connectAttr(jnta+'.translate',plusT+'.input3D[0]',f=1)
            cmds.connectAttr(jntb+'.translate',plusT+'.input3D[1]',f=1)
            cmds.connectAttr(plusT+'.output3D',jntc+'.translate',f=1)
            plusR=cmds.createNode('plusMinusAverage',n=jntc+'_plusR')
            cmds.connectAttr(jnta+'.rotate',plusR+'.input3D[0]',f=1)
            cmds.connectAttr(jntb+'.rotate',plusR+'.input3D[1]',f=1)
            cmds.connectAttr(plusR+'.output3D',jntc+'.rotate',f=1)