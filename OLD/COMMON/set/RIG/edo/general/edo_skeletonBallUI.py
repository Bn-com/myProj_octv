import maya.cmds as cmds
def edo_skeletonBallUI():
    if cmds.window("edo_skeletonBallUI",ex=1):
        cmds.deleteUI("edo_skeletonBallUI")
    cmds.window("edo_skeletonBallUI",title="edo_skeletonBallUI")
    cmds.columnLayout('edo_skeletonBallUI_CL01',columnAttach=('both', 5), rowSpacing=2, columnWidth=180)
    cmds.button('edo_skeletonBallUI_CL01_BT1',label='add skeleton driven ball',ann='select one joint first,then click this button',bgc=(0.9,0.7,0.1),c='edo_addSkeletonBallCmd()')
    cmds.button('edo_skeletonBallUI_CL01_BT2',label='mirror skeleton driven ball',ann='select one skeletonDrivenBall first,then click this button',bgc=(0.7,0.9,0.1),c='edo_mirrorSkeletonBallCmd()')
    cmds.button('edo_skeletonBallUI_CL01_BT3',label='add global scale locator',ann='select one skeletonDrivenBall first,then click this button',bgc=(0.1,0.2,0.05),c='edo_addAllSkeletonBallGlobalScaleLoc()')
    cmds.button('edo_skeletonBallUI_CL01_BT4',label='connect Visable attribute to Master',ann='if there is a ctrl named Master in the scence,you can connect the visable attribute of SKDB to Master by click this button.',bgc=(0.1,0.2,0.05),c='edo_createMasterVisableAttr()')
    cmds.showWindow("edo_skeletonBallUI")
    cmds.window("edo_skeletonBallUI",e=1,widthHeight=(180,100))


def edo_mirrorSkeletonBallCmd():
    sels=cmds.ls(sl=1)
    isdcdk=cmds.confirmDialog( title='do you want duplicate all the setDrivenKey?', message='do you want duplicate all the setDrivenKey?', button=['yes','no'], defaultButton='Yes', cancelButton='No', dismissString='No')
    for sel in sels:
        #sel=sels[0]
        edo_mirrorSkeletonBall(sel)
        if 'Lf' in sel:
            edo_duplicateSetDrivenKey(sel,'Lf','Rt')
        if 'Rt' in sel:
            edo_duplicateSetDrivenKey(sel,'Rt','Lf')
       
def edo_duplicateSetDrivenKey(driver,bstr,astr):
    #driver='Lf_jnt0_FRAME'
    #bstr='Lf'
    #astr='Rt'
    anac=[]
    allattr=cmds.listAttr(driver,k=1)
    for attr in allattr:
        #attr = allattr[9]
        aacs=cmds.listConnections(driver+'.'+attr,d=1,s=0,type='animCurve')
        if aacs==None or aacs==[]:
            continue
        for ac in aacs:
            #ac=aacs[0]
            nac=ac.replace(bstr,astr)
            if cmds.objExists(nac):
                print 'delete ... '+nac
                cmds.delete(nac)
            cmds.duplicate(ac,n=nac)
            anac.append(nac)
    return anac

def edo_addSkeletonBallCmd():
    sels=cmds.ls(sl=1)
    for sel in sels:
        #sel=sels[0]
        edo_addSkeletonBall(sel)

#edo_mirrorSkeletonBall('Lf_jnt0_FRAME')
def edo_mirrorSkeletonBall(skball):
    #skball='Rt_joint1_FRAME'
    if 'Lf' in skball:
        gs=cmds.getAttr(skball+'.globalScale')
        ro=cmds.xform(skball,q=1,ws=1,ro=1)
        mro=[ro[0],ro[1]*-1,ro[2]*-1]
        mirrorjnt=skball.replace('Lf','Rt').replace('_FRAME','')
        if cmds.objExists(mirrorjnt):
            edo_addSkeletonBall(mirrorjnt)
            cmds.setAttr(mirrorjnt+'_FRAME.globalScale',gs)
            cmds.xform(mirrorjnt+'_FRAME',ws=1,ro=mro)
            cmds.orientConstraint(mirrorjnt,mirrorjnt+'_centerLoc',mo=1)
            cmds.setAttr(mirrorjnt+'_FRAME.direction',1)
    if 'Rt' in skball:
        gs=cmds.getAttr(skball+'.globalScale')
        ro=cmds.xform(skball,q=1,ws=1,ro=1)
        mro=[ro[0],ro[1]*-1,ro[2]*-1]
        mirrorjnt=skball.replace('Rt','Lf').replace('_FRAME','')
        if cmds.objExists(mirrorjnt):
            edo_addSkeletonBall(mirrorjnt)
            cmds.setAttr(mirrorjnt+'_FRAME.globalScale',gs)
            cmds.xform(mirrorjnt+'_FRAME',ws=1,ro=mro)
            cmds.orientConstraint(mirrorjnt,mirrorjnt+'_centerLoc',mo=1)
            cmds.setAttr(mirrorjnt+'_FRAME.direction',0)

#edo_addSkeletonBall('joint1')
def edo_addSkeletonBall(jnt,parents=None):
	#jnt='joint1'
	dbs=cmds.sphere(ch=1,o=1,po=0,ax=[1,0,0],r=1.0,nsp=4,esw=180,n=jnt+'_dn_drivenBall')
	dnball=dbs[0]
	cmds.delete(dbs[1])
	dbs=cmds.sphere(ch=1,o=1,po=0,ax=[1,0,0],r=1.0,nsp=4,ssw=180,esw=360,n=jnt+'_up_drivenBall')
	upball=dbs[0]
	cmds.delete(dbs[1])
	edo_gdcfrig2012_createCtrl(jnt+'_FRAME',shape='box',colorid=17)
	cmds.setAttr(jnt+'_FRAME.sx',2)
	cmds.setAttr(jnt+'_FRAME.sy',2)
	cmds.setAttr(jnt+'_FRAME.sz',2)
	cmds.makeIdentity(jnt+'_FRAME',apply=1,t=1,r=1,s=1,n=0)
	cmds.connectAttr(jnt+'_FRAME.sy',jnt+'_FRAME.sx',f=1)
	cmds.connectAttr(jnt+'_FRAME.sy',jnt+'_FRAME.sz',f=1)
	cmds.setAttr(jnt+'_FRAME.sx',e=1,k=0)
	cmds.setAttr(jnt+'_FRAME.sz',e=1,k=0)
	cmds.aliasAttr('globalScale',jnt+'_FRAME.sy')
	cmds.addAttr(jnt+'_FRAME',ln='front',at='double')
	cmds.setAttr(jnt+'_FRAME.front',e=1,k=0)
	cmds.addAttr(jnt+'_FRAME',ln='back',at='double')
	cmds.setAttr(jnt+'_FRAME.back',e=1,k=0)
	cmds.addAttr(jnt+'_FRAME',ln='left',at='double')
	cmds.setAttr(jnt+'_FRAME.left',e=1,k=0)
	cmds.addAttr(jnt+'_FRAME',ln='right',at='double')
	cmds.setAttr(jnt+'_FRAME.right',e=1,k=0)
	cmds.addAttr(jnt+'_FRAME',ln='tip',at='double')
	cmds.setAttr(jnt+'_FRAME.tip',e=1,k=1)
	cmds.addAttr(jnt+'_FRAME',ln='frontValue',at='double')
	cmds.setAttr(jnt+'_FRAME.frontValue',e=1,k=1)
	cmds.addAttr(jnt+'_FRAME',ln='backValue',at='double')
	cmds.setAttr(jnt+'_FRAME.backValue',e=1,k=1)
	cmds.addAttr(jnt+'_FRAME',ln='leftValue',at='double')
	cmds.setAttr(jnt+'_FRAME.leftValue',e=1,k=1)
	cmds.addAttr(jnt+'_FRAME',ln='rightValue',at='double')
	cmds.setAttr(jnt+'_FRAME.rightValue',e=1,k=1)
	cmds.addAttr(jnt+'_FRAME',ln='maxAngle',at='double',min=45,max=180)
	cmds.setAttr(jnt+'_FRAME.maxAngle',e=1,k=1)
	cmds.setAttr(jnt+'_FRAME.maxAngle',90)
	cmds.addAttr(jnt+'_FRAME',ln='maxAngleRange',at='double')
	cmds.setAttr(jnt+'_FRAME.maxAngleRange',e=1,k=0)
	ar=cmds.createNode('multiplyDivide',n=jnt+'_angleMultiplyDivide')
	cmds.setAttr(jnt+'_angleMultiplyDivide.input1X',180)
	cmds.connectAttr(jnt+'_FRAME.maxAngle',jnt+'_angleMultiplyDivide.input2X',f=1)
	cmds.setAttr(jnt+'_angleMultiplyDivide.operation',2)
	cmds.connectAttr(jnt+'_angleMultiplyDivide.outputX',jnt+'_FRAME.maxAngleRange',f=1)
	#addLoactor
	fl=cmds.spaceLocator(n=jnt+'_frontLoc',p=[0,0,1])[0]
	bl=cmds.spaceLocator(n=jnt+'_backLoc',p=[0,0,-1])[0]
	ll=cmds.spaceLocator(n=jnt+'_leftLoc',p=[1,0,0])[0]
	rl=cmds.spaceLocator(n=jnt+'_rightLoc',p=[-1,0,0])[0]
	tl=cmds.spaceLocator(n=jnt+'_tipLoc',p=[0,1,0])[0]
	dbl=cmds.spaceLocator(n=jnt+'_dnBallLoc',p=[0,-1,0])[0]
	ubl=cmds.spaceLocator(n=jnt+'_upBallLoc',p=[0,0,1])[0]
	cl=cmds.spaceLocator(n=jnt+'_centerLoc',p=[0,0,0])[0]
	cmds.select([fl,bl,ll,rl,tl,dbl,ubl,cl],r=1)
	cmds.CenterPivot()
	cmds.geometryConstraint(dnball,dbl)
	cmds.parentConstraint(cl,dbl,mo=1)
	cmds.setAttr(cl+'.rx',-90)
	cmds.geometryConstraint(upball,ubl)
	cmds.parentConstraint(cl,ubl,mo=1)
	cmds.setAttr(cl+'.rx',0)
	tdis=edo_createDistanceNode(ubl,tl,disname=jnt+'_tipDis')
	fdis=edo_createDistanceNode(dbl,fl,disname=jnt+'_frontDis')
	bdis=edo_createDistanceNode(dbl,bl,disname=jnt+'_backDis')
	ldis=edo_createDistanceNode(dbl,ll,disname=jnt+'_leftDis')
	rdis=edo_createDistanceNode(dbl,rl,disname=jnt+'_rightDis')
	#addTipSetRangeValue
	tdism=cmds.createNode('multiplyDivide',n=jnt+'_tipDisMultiply')
	dis=cmds.getAttr(tdis+'.distance')
	tiprange=cmds.createNode('setRange',n=jnt+'_tipRange')
	cmds.connectAttr(tdis+'.distance',tiprange+'.valueX',f=1)
	cmds.setAttr(tiprange+'.minX',2)
	cmds.setAttr(tiprange+'.maxX',1)
	cmds.connectAttr(tiprange+'.outValueX',jnt+'_FRAME.tip')
	cmds.connectAttr(jnt+'_FRAME.sy',tdism+'.input1Y',f=1)
	cmds.setAttr(tdism+'.input2Y',dis)
	cmds.connectAttr(tdism+'.outputY',tiprange+'.oldMaxX',f=1)
	#addFrontSetRangeValue
	fdism=cmds.createNode('multiplyDivide',n=jnt+'_frontDisMultiply')
	dis=cmds.getAttr(fdis+'.distance')
	frontrange=cmds.createNode('setRange',n=jnt+'_frontRange')
	cmds.connectAttr(fdis+'.distance',frontrange+'.valueX',f=1)
	cmds.setAttr(frontrange+'.minX',1)
	cmds.connectAttr(frontrange+'.outValueX',jnt+'_FRAME.front',f=1)
	fm=cmds.createNode('multiplyDivide',n=jnt+'_frontMultiply')
	cmds.connectAttr(jnt+'_FRAME.front',fm+'.input1X',f=1)
	cmds.connectAttr(jnt+'_FRAME.tip',fm+'.input2X',f=1)
	cmds.connectAttr(fm+'.outputX',frontrange+'.valueY',f=1)
	cmds.setAttr(frontrange+'.oldMinY',0)
	cmds.setAttr(frontrange+'.oldMaxY',2)
	cmds.connectAttr(frontrange+'.outValueY',jnt+'_FRAME.frontValue',f=1)
	cmds.connectAttr(jnt+'_FRAME.maxAngleRange',frontrange+'.maxY',f=1)
	cmds.connectAttr(jnt+'_FRAME.sy',fdism+'.input1Y',f=1)
	cmds.setAttr(fdism+'.input2Y',dis)
	cmds.connectAttr(fdism+'.outputY',frontrange+'.oldMaxX',f=1)
	#addBackSetRangeValue
	bdism=cmds.createNode('multiplyDivide',n=jnt+'_backDisMultiply')
	dis=cmds.getAttr(bdis+'.distance')
	backrange=cmds.createNode('setRange',n=jnt+'_backRange')
	cmds.connectAttr(bdis+'.distance',backrange+'.valueX',f=1)
	cmds.setAttr(backrange+'.minX',1)
	cmds.connectAttr(backrange+'.outValueX',jnt+'_FRAME.back',f=1)
	bm=cmds.createNode('multiplyDivide',n=jnt+'_backMultiply')
	cmds.connectAttr(jnt+'_FRAME.back',bm+'.input1X',f=1)
	cmds.connectAttr(jnt+'_FRAME.tip',bm+'.input2X',f=1)
	cmds.connectAttr(bm+'.outputX',backrange+'.valueY',f=1)
	cmds.setAttr(backrange+'.oldMinY',0)
	cmds.setAttr(backrange+'.oldMaxY',2)
	cmds.connectAttr(backrange+'.outValueY',jnt+'_FRAME.backValue',f=1)
	cmds.connectAttr(jnt+'_FRAME.maxAngleRange',backrange+'.maxY',f=1)
	cmds.connectAttr(jnt+'_FRAME.sy',bdism+'.input1Y',f=1)
	cmds.setAttr(bdism+'.input2Y',dis)
	cmds.connectAttr(bdism+'.outputY',backrange+'.oldMaxX',f=1)
	#addLeftSetRangeValue
	ldism=cmds.createNode('multiplyDivide',n=jnt+'_leftDisMultiply')
	dis=cmds.getAttr(ldis+'.distance')
	leftrange=cmds.createNode('setRange',n=jnt+'_leftRange')
	cmds.connectAttr(ldis+'.distance',leftrange+'.valueX',f=1)
	cmds.setAttr(leftrange+'.minX',1)
	cmds.connectAttr(leftrange+'.outValueX',jnt+'_FRAME.left',f=1)
	lm=cmds.createNode('multiplyDivide',n=jnt+'_leftMultiply')
	cmds.connectAttr(jnt+'_FRAME.left',lm+'.input1X',f=1)
	cmds.connectAttr(jnt+'_FRAME.tip',lm+'.input2X',f=1)
	cmds.connectAttr(lm+'.outputX',leftrange+'.valueY',f=1)
	cmds.setAttr(leftrange+'.oldMinY',0)
	cmds.setAttr(leftrange+'.oldMaxY',2)
	leftblend=cmds.createNode('blendColors',n=leftrange+'_blend')
	cmds.connectAttr(leftrange+'.outValueY',leftblend+'.color2R',f=1)
	cmds.connectAttr(leftblend+'.outputR',jnt+'_FRAME.leftValue',f=1)
	cmds.connectAttr(jnt+'_FRAME.maxAngleRange',leftrange+'.maxY',f=1)
	cmds.connectAttr(jnt+'_FRAME.sy',ldism+'.input1Y',f=1)
	cmds.setAttr(ldism+'.input2Y',dis)
	cmds.connectAttr(ldism+'.outputY',leftrange+'.oldMaxX',f=1)
	#addRightSetRangeValue
	rdism=cmds.createNode('multiplyDivide',n=jnt+'_rightDisMultiply')
	dis=cmds.getAttr(rdis+'.distance')
	rightrange=cmds.createNode('setRange',n=jnt+'_rightRange')
	cmds.connectAttr(rdis+'.distance',rightrange+'.valueX',f=1)
	cmds.setAttr(rightrange+'.minX',1)
	cmds.connectAttr(rightrange+'.outValueX',jnt+'_FRAME.right',f=1)
	rm=cmds.createNode('multiplyDivide',n=jnt+'_rightMultiply')
	cmds.connectAttr(jnt+'_FRAME.right',rm+'.input1X',f=1)
	cmds.connectAttr(jnt+'_FRAME.tip',rm+'.input2X',f=1)
	cmds.connectAttr(rm+'.outputX',rightrange+'.valueY',f=1)
	cmds.setAttr(rightrange+'.oldMinY',0)
	cmds.setAttr(rightrange+'.oldMaxY',2)
	rightblend=cmds.createNode('blendColors',n=rightrange+'_blend')
	cmds.connectAttr(rightrange+'.outValueY',rightblend+'.color2R',f=1)
	cmds.connectAttr(rightblend+'.outputR',jnt+'_FRAME.rightValue',f=1)
	cmds.connectAttr(jnt+'_FRAME.maxAngleRange',rightrange+'.maxY',f=1)
	cmds.connectAttr(jnt+'_FRAME.sy',rdism+'.input1Y',f=1)
	cmds.setAttr(rdism+'.input2Y',dis)
	cmds.connectAttr(rdism+'.outputY',rightrange+'.oldMaxX',f=1)
	#addYZplaneMirrorAttr
	cmds.addAttr(jnt+'_FRAME',ln='direction',at='enum',en='left:right')
	cmds.setAttr(jnt+'_FRAME.direction',e=1,k=1)
	cmds.connectAttr(rightrange+'.outValueY',leftblend+'.color1R',f=1)
	cmds.connectAttr(leftrange+'.outValueY',rightblend+'.color1R',f=1)
	cmds.connectAttr(jnt+'_FRAME.direction',leftblend+'.blender',f=1)
	cmds.connectAttr(jnt+'_FRAME.direction',rightblend+'.blender',f=1)
	#Dag
	cmds.parent(jnt+'_FRAME',w=1)
	cmds.delete('GRP_'+jnt+'_FRAME')
	cmds.parent(fl,jnt+'_FRAME')
	cmds.parent(bl,jnt+'_FRAME')
	cmds.parent(ll,jnt+'_FRAME')
	cmds.parent(rl,jnt+'_FRAME')
	cmds.parent(tl,jnt+'_FRAME')
	cmds.parent(ubl,jnt+'_FRAME')
	cmds.parent(dbl,jnt+'_FRAME')
	cmds.parent(cl,jnt+'_FRAME')
	cmds.parent(upball,jnt+'_FRAME')
	cmds.parent(dnball,jnt+'_FRAME')
	cmds.select(jnt+'_FRAME',r=1)
	#hideLocator
	cmds.setAttr(upball+'.v',0)
	cmds.setAttr(dnball+'.v',0)
	cmds.setAttr(fl+'.v',0)
	cmds.setAttr(bl+'.v',0)
	cmds.setAttr(ll+'.v',0)
	cmds.setAttr(rl+'.v',0)
	cmds.setAttr(tl+'.v',0)
	cmds.setAttr(ubl+'.v',0)
	cmds.setAttr(dbl+'.v',0)
	cmds.setAttr(cl+'.overrideEnabled',1)
	cmds.setAttr(cl+'.ovc',13)
	#position
	cmds.parent(jnt+'_FRAME',jnt)
	cmds.setAttr(jnt+'_FRAME.tx',0)
	cmds.setAttr(jnt+'_FRAME.ty',0)
	cmds.setAttr(jnt+'_FRAME.tz',0)
	cmds.parent(jnt+'_FRAME',w=1)
	#addglobalScaleAttr
	edo_addSkeletonBallGlobalScaleAttr(jnt+'_FRAME')
	
def edo_addSkeletonBallGlobalScaleAttr(framename):
    #framename=jnt+'_FRAME'
    print 'add global scale attribute to ... '+framename
    if cmds.attributeQuery('globalScale',n=framename,ex=1):
        if cmds.objExists(framename+'_globalScaleLoc'):
            return False
        gloc=cmds.spaceLocator(n=framename+'_globalScaleLoc')
        if not cmds.objExists('GRP_sleletonBallGlobalScaleLoc'):
            cmds.createNode('transform',n='GRP_sleletonBallGlobalScaleLoc')
        cmds.parent(gloc[0],'GRP_sleletonBallGlobalScaleLoc')
        cmds.parentConstraint(framename,gloc,mo=0)
        cmds.scaleConstraint(framename,gloc,mo=0)
        outputs=cmds.listConnections(framename+'.globalScale',s=0,d=1,p=1)
        for output in outputs:
            #output = outputs[0]
            if output.split('.')[0]==framename:
                continue
            print 'connectAttr ... '+gloc[0]+'.sy'+' ... to ... '+output
            cmds.connectAttr(gloc[0]+'.sy',output,f=1)
    
def edo_addAllSkeletonBallGlobalScaleLoc():
    sels=cmds.ls(sl=1)
    for sel in sels:
        edo_addSkeletonBallGlobalScaleAttr(sel)
    

def edo_createDistanceNode(locA,locB,disname='distanceBetween'):
    #locA='Lf_upArm_drv_jnt_upBallLoc'
    #locB='Lf_upArm_drv_jnt_tipLoc'
    disnode=cmds.createNode('distanceBetween',n=disname)
    cmds.connectAttr(locA+'.worldPosition',disnode+'.point1',f=1)
    cmds.connectAttr(locB+'.worldPosition',disnode+'.point2',f=1)
    return disnode

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
    
def edo_createMasterVisableAttr():
    if not cmds.attributeQuery('skdb_vis',n='Master',ex=1):
        cmds.addAttr('Master',ln='skdb_vis',at='bool')
        cmds.setAttr('Master.skdb_vis',e=1,cb=1,k=0)
    skdbs=cmds.ls("*_drivenBall")
    for skdb in skdbs:
        #skdb=skdbs[0]
        skdbp=cmds.listRelatives(skdb,p=1,pa=1)[0]
        if cmds.listConnections(skdbp+'.v',s=1,d=0)==None:
            print 'connect to Master'
            if not cmds.getAttr(skdbp+'.v',l=1):
               cmds.connectAttr('Master.skdb_vis',skdbp+'.v',f=1)