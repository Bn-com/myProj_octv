import maya.cmds as cmds
def edo_addHeadSquashRig():
	cmds.select(hi=1)
	sels=cmds.ls(sl=1,type='joint')
	dis=cmds.getAttr(sels[1]+'.tx')
	endjnt=sels[len(sels)-1]
	tmp=endjnt.split('_')
	ctrl=''
	for t in tmp[1:-1]:
		ctrl+=t+'_'
	ctrl=ctrl+'CTRL'
	edo_gdcfrig2012_createCtrl(ctrl)
	edo_gdcfrig2012_ctrlLocation('GRP_'+ctrl,endjnt)
	cmds.group(ctrl,n='DIV_'+ctrl)
	cmds.xform('DIV_'+ctrl,os=1,piv=[0,0,0])
	iks=cmds.ikHandle(sol='ikSplineSolver',sj=sels[0],ee=endjnt,n=ctrl.replace('CTRL','SPLINEIKHANDLE'))
	ikh=iks[0]
	ike=iks[1]
	ikc=cmds.rename(iks[2],ctrl.replace('CTRL','IKCURVE'))
	sksj=cmds.duplicate(sels[0],n=sels[0].replace('JNT_','SKIN_'),po=1)
	skej=cmds.duplicate(endjnt,n=endjnt.replace('JNT_','SKIN_'),po=1)
	cmds.parent(skej[0],ctrl)
	cmds.skinCluster([skej[0],sksj[0]],ikc,mi=2,dr=4.0)
	cinfo=cmds.createNode('curveInfo',n=ikc.replace('IKCURVE','CURVEINFO'))
	cmds.connectAttr(ikc+'.worldSpace',cinfo+'.inputCurve',f=1)
	exname=ctrl.replace('CTRL','EXRESSION')
	exts='//'+exname+'\n'
	exts+=('float $aclen='+cinfo+'.arcLength;\n')
	orglen=cmds.getAttr(cinfo+'.arcLength')
	exts+=('float $orglen='+str(orglen)+';\n')
	exts+=('float $stretch=$aclen/$orglen;\n')
	exts+=('float $squash=1/sqrt($stretch);\n')
	for jnt in sels[1:]:
		print jnt
		#jnt=sels[1]
		cmds.addAttr(jnt,ln='squash',at='double')
		cmds.setAttr(jnt+'.squash',e=1,k=1)
		exts+=(jnt+'.tx='+str(dis)+'*$stretch;\n')
		exts+=(jnt+'.sy=pow($squash,'+jnt+'.squash'+');\n')
		exts+=(jnt+'.sz=pow($squash,'+jnt+'.squash'+');\n')
	cmds.expression(n=exname,s=exts)



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