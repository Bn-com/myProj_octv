#!/usr/bin/env python
# -*- coding: utf-8 -*-
#### E:\study\script\ex_smalltools
import maya.cmds as cmds
import maya.mel as mel
import re,os,sys
# print('{}/ex_smalltools/lynn_CreateCtrl_Def.py'.format(local_dir))
# print('{}/ex_smalltools/lynn_CreateCtrl_Def.py'.format(local_dir))
#print('{}/ex_smalltools/lynn_CreateCtrl_Def.py'.format(local_dir))
execfile('//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/GDC/COMMON/set/RIG/lynn/ex_smalltools/lynn_CreateCtrl_Def.py')#.format(os.path.split(sys.argv[0])[0]))
execfile('//file-cluster/GDC/Resource/Development/Maya/GDC/Plug/Python/GDC/COMMON/set/RIG/lynn/ex_smalltools/lynn_CreatHairBeardIkCtrls_Def.py')#.format(os.path.split(sys.argv[0])[0]))
class myClass(object):
    def __init__(self):
        self.source = []
        self.target = []
        self.createUI()
    def createUI(self):
        if cmds.window('lynnToolWindow',ex=True):
            cmds.deleteUI('lynnToolWindow')
          
        window01=cmds.window(u'lynnToolWindow',title="RiggingTools",iconName='shortName',widthHeight=(200,400))
        cmds.columnLayout (columnAttach=('both',0.1),rowSpacing =0.5,adjustableColumn=True)
        #imag=cmds.internalVar(userPrefDir=True)+"icons/fan.jpg"
        #cmds.image(w=300,h=110,image=imag)
        cmds.text('welcome to the Lynn tools',backgroundColor=(1.5,0.5,0.1),font="boldLabelFont",recomputeSize=0,w=200,h=25)
        cmds.separator(h=5,style='in')
        cmds.text(l="Riging Common tools ",align="left")
        #cmds.text(l="choose the Radius",align="left")
        #cmds.separator(h=10)
        #myRadius=cmds.intSliderGrp(l="Radius",min=1,max=10,f=True)
        #cmds.button(l="sphere",c='s( )')
        cmds.button(l="CreateFollicleOn->polygons",c='createFollicleOnPolygons()',annotation='firstly select polygon,then select locator(modelFreezeAndUV)',h=30)
        cmds.button(l="CreateFollicleOn->surface",c='CreateFollicleOnsurface()',annotation='firstly select surface,then select locator',h=30)
        cmds.button(l="Create Joint Under Parent[Follicle/Group]",c='CreateJointUnderFollicle()',annotation='select follicle',h=30)
        cmds.button(l="Add a simple controller[Circle]",c='addAController()',annotation='Selecting an object,then do',h=30)
        cmds.button(l="Add a simple controller[Square]",c='addAControllerS()',annotation='Selecting an object,then do',h=30)
        cmds.button(l="Add a simple controller(skin)[Circle]",c='addAControllerSkin()',annotation='Selecting an object,then do',h=30)
        cmds.button(l="Add FK controller->JointChain",c='FK_Jointchain()',annotation='select Joint,then do',h=30)
        
        
        # lynn_addAController()
       # cmds.button(l="Like a beard IK Joint chain",c='createHairBeardIKCtrl()',annotation='select Joint,then do',h=30)
        cmds.button(l="GlobalSacle ",c='GlobalSacleConstrain()',annotation='select All + driver constrained objects,then do',h=30)

        #cmds.separator(h=10,style='in')
        #--------aotoStrech------------------
        cmds.text(l="AutoStretch[make sure the last joint is the first axis of x]",align="left")
        cmds.rowColumnLayout(nc = 1)
        cmds.button (label='Add aoto Stretch  [all IKJnt+IKCurve]',annotation='select all IKJoint and SplineCurveDO',c='aotoStrect()',align="left",w=280,h=25)
        cmds.setParent( '..' )
        cmds.separator(h=5,style='in')
        #---------*****-----fastConnectPostfix---------------------------
        #cmds.text(l="          ",align="left")
        cmds.text(l="*connecting the same postfix name object* ",align="left")
        cmds.rowColumnLayout(nc = 2)
        cmds.text('step  1: ',align="left")
        self.LoadButton =cmds.button(label= u' Load Connected OBJ ',c = lambda x:self.connectLoad(),align="left",w =240)
        cmds.text('step  2: ',align="left")
        self.LoadBeButton = cmds.button(label= u' Load Be Connected OBJ ',c = lambda x:self.BeConnectLoad(),align="left",w=240)
        cmds.text('step  3: ',align="left")
        cmds.button(label= u' *DO CONNECTION* ',c = lambda x:self.DoConnect(),w=240)
        cmds.setParent( '..' )
        cmds.separator(w = 322,h=10,style='in') 
        #----------------parent  -s ---add-------------------
        cmds.text(l="*parent shape add* ",align="left")
        myShape=cmds.textScrollList('shapeList',w=240,h=30,allowMultiSelection=True,deleteKeyCommand='delShapeList()')
        cmds.button(label= u'1. Load shape ',c='addShapeList()',align="left",w =240,annotation='You can select more than one shape nodes')
        cmds.button(label= u'2. Parent Shape to select Joint',c='parentShape()',align="left",w =240,annotation='select Jnt then DO')
        #-------------------------------------------
        #�������ţ���ת����ɫ
        cmds.text(l="Scale & Rotate & Color [Shape of the controller]",align="left")
        cmds.setParent( '..' )
        cmds.rowColumnLayout(nc = 4)
        self.scaleRadiu=cmds.textField(tx='0.1',fn='fixedWidthFont',w=40,h=30)
        cmds.button(l="-ReducedScale",c=lambda x:self.scaleJianShao(),w=100,h=30)
        self.scaleRadiu01=cmds.textField(tx='0.1',fn='fixedWidthFont',w=40,h=30)
        cmds.button(l="+ IncreaseScale",c=lambda x:self.scaleChengjia(),w=100,h=30)

        #rotate
        cmds.setParent( '..' )
        cmds.rowColumnLayout(nc = 6)
        self.rx=cmds.textField(tx='90',fn='fixedWidthFont',w=40,h=30)
        cmds.button(l="RotateX",c=lambda x:self.RotateX(),w=100,h=30)
        self.rz=cmds.textField('input05',tx='90',fn='fixedWidthFont',w=40,h=30)
        cmds.button(l="RotateZ  ",c=lambda x:self.RotateZ(),w=100,h=30)
        cmds.setParent( '..' )
        #------------��ɫ-------------------------
        cmds.separator(w = 322,h=2,style='in') 
        cmds.rowColumnLayout(nc = 5)
        cmds.button(l="Red",c='colorRed()',w=57,h=20,bgc=(1,0,0))
        cmds.button(l="Yellow",c='colorYellow()',w=56,h=20,bgc=(1,1,0))
        cmds.button(l="Blue",c='colorBlue()',w=55,h=20,bgc=(0,0,1))
        cmds.button(l="Purple",c='colorPurple()',w=55,h=20,bgc=(1,0,1))
        cmds.button(l="LightBlue",c='colorLightBlue()',w=57,h=20,bgc=(0,0.836,1))
        cmds.setParent( '..' )
        #--------------------------
        cmds.separator(h=10,style='in')
        cmds.text(l="Creates a variety of controller ",align="left")
        cmds.rowColumnLayout(nc = 3) 
        cmds.button(l="IKFKcircle",c='ctrlikfk()',annotation='chick',w=95,h=28)
        cmds.button(l="box",c='box_C()',annotation='chick',w=95,h=28)
        cmds.button(l="diomond",c='diamond_C()',annotation='chick',w=95,h=28)
        cmds.button(l="Double arrow",c='Door_C()',annotation='chick',w=95,h=28)
        cmds.button(l="Ball",c='Ball_C()',annotation='chick',w=95,h=28)
        cmds.button(l="pivot",c='Pivot_C()',annotation='chick',w=95,h=28)        
        cmds.showWindow(window01)      
#-------#--------------*************------------------------------------  
#Fast connecting the same suffix name object  
#fast Connect Have Same Postfix
#�������Ӻ�׺����ͬ������---------------------------------------------------------------
    #1)ѡ�б�����OBJִ������
    def connectLoad(self):
        self.source = cmds.ls(sl=1,r=1)
        if self.source:
            cmds.button(self.LoadButton,e = True,label = u"Load successful")
            print u"Load object",self.source

        
    #2)ѡ�б�����dirvenOBJִ������
    def BeConnectLoad(self):
        self.target = cmds.ls(sl=True,r=1)
        if self.target:
            cmds.button(self.LoadBeButton,e = True,label = u"Load successful")
            print u"Load object",self.target
        
    #3)��ʼ�ȶ���������
    def DoConnect(self):
        cmds.button(self.LoadButton,e = True,label = u' Load Connected OBJ ')
        cmds.button(self.LoadBeButton,e = True,label = u' Load Be Connected OBJ ')
        
        for s in self.source:
            linkObject =  self.FindedConnectObject(s)
            if linkObject:
                cmds.connectAttr(s+".rotate",linkObject+".rotate")
                cmds.connectAttr(s+".translate",linkObject+".translate")
                cmds.connectAttr(s+".scale",linkObject+".scale")
                print u"connectAttr",s+"---------->",linkObject
        
    def FindedConnectObject(self,name):
        suffix = name.split('_')[-1]
        for d in self.target:
            if re.match(".*_"+suffix+"\Z", d):
                return d
        
    #-------------------------
    def scaleJianShao(self):
        ctrls=cmds.ls(sl=True)
        scaleR=cmds.textField(self.scaleRadiu,q=True,tx=True)
        scaleRr=1-float(scaleR)
        for cv in ctrls:
            
            cmds.select(cv+'.cv[*:*]')
            cmds.scale(scaleRr,scaleRr,scaleRr,r=True)
            #cmds.select(cv)
            cmds.select(ctrls)
    #-------------------------
    def scaleChengjia(self):
        ctrls=cmds.ls(sl=True)
        scaleR=cmds.textField(self.scaleRadiu01,q=True,tx=True)
        scaleRr=float(scaleR)+1
        for cv in ctrls:
            
            cmds.select(cv+'.cv[*:*]')
            cmds.scale(scaleRr,scaleRr,scaleRr,r=True)
            #cmds.select(cv)
            cmds.select(ctrls)
    
    #-------------------------
    def RotateX(self):
        ctrls=cmds.ls(sl=True)
        RXR=cmds.textField(self.rx,q=True,tx=True)
        RXRr=float(RXR)
        for cv in ctrls:        
            cmds.select(cv+'.cv[*:*]')
            cmds.rotate(RXRr,0,0,r=True)
            #cmds.select(cv)
            cmds.select(ctrls)

    #----------------------
    def RotateZ(self):
        ctrls=cmds.ls(sl=True)
        RXR=cmds.textField(self.rz,q=True,tx=True)
        RXRr=float(RXR)
        for cv in ctrls:
            
            cmds.select(cv+'.cv[*:*]')
            cmds.rotate(0,0,RXRr,r=True)
            #cmds.select(cv)
            cmds.select(ctrls)

def s():
    rr=cmds.intSliderGrp(myRadius,q=True,v=True)
    cmds.sphere(r=rr,n="ball")    
def createFollicleOnPolygons(): 
    #ģ��Ҫ���ᣬ������λ�����Բ��ܴ��׼ȷ���������Ҫ**
    #��ѡģ����ѡ��λ����locater��
    import maya.cmds as cmds 
    import maya.mel as mel
    objs=cmds.ls(sl=True)
    mun=len(objs)
    mesh=objs[0]
    meshShape=cmds.listRelatives(mesh)
    mshape=meshShape[0]
    for i in range(1,mun):
        #i=1
        loc=objs[i]
        fos=cmds.createNode('follicle')
        fosPers=cmds.listRelatives(fos,p=1)
        fosPersName=cmds.rename(fosPers,'FO#')
        fosnew=cmds.ls(sl=True)
        foshapenew=fosnew[0]
        cmds.connectAttr (mshape+".outMesh",fosPersName+".inputMesh",f=1)
        cmds.connectAttr (mshape+".worldMatrix[0]",foshapenew+".inputWorldMatrix",f=1)
        cmds.connectAttr (foshapenew+".outTranslate",fosPersName+".translate",f=1)#remenberThis
        cmds.connectAttr (foshapenew+".outRotate",fosPersName+".rotate",f=1)#remenberThis
        
        nodes=cmds.createNode ('closestPointOnMesh')
        cmds.connectAttr (mshape+".outMesh",nodes+".inMesh",f=1)
        cmds.connectAttr (loc+".translate",nodes+".inPosition",f=1)
        print loc
    
        U11=cmds.getAttr (nodes+".parameterU") 
        V11=cmds.getAttr (nodes+".parameterV")
        cmds.setAttr (foshapenew +".parameterU",U11) 
        cmds.setAttr (foshapenew +".parameterV",V11)
        cmds.delete (nodes)#delete"closestPointOnSurface"
        cmds.delete(objs[i])#delete locate
    
def CreateJointUnderFollicle():
    #CreateJoint under the follicle or group
    import maya.cmds as cmds
    foll=cmds.ls(sl=True)
    #name=foll[0]+'_Jnt'
    name='Jnt'
    mun=len(foll)
    i=0
    for i in range(0,mun):
    
        jnt =cmds.createNode('joint' ,n= name+"#")
        cmds.parent (jnt ,foll[i])
        
        cmds.setAttr (jnt+ ".translateX",0)
        cmds.setAttr (jnt+ ".translateY",0)
        cmds.setAttr (jnt+ ".translateZ",0)
        
        cmds.setAttr (jnt+".jointOrientX",0)
        cmds.setAttr (jnt+".jointOrientY",0)
        cmds.setAttr (jnt+".jointOrientZ",0)   
      
#---------------------
# �����ë��follicel on surface
# ��ѡ��ģ����ѡ��λ��locater
def CreateFollicleOnsurface():
    import maya.cmds as cmds    
    objs=cmds.ls(sl=True)
    mesh=objs[0]
    cmds.rebuildSurface(mesh,ch=1,rpo=1,rt=0,end=1,kr=0,kcp=1,kc=0,su=4,du=3,sv=4,dv=3,tol=0.01,fr=0,dir=2)
        
    mun=len(objs)
    meshShape=cmds.listRelatives( mesh)
    msShape=meshShape[0]
    
    for i in range(1,mun):        
        loc=objs[i]
        fos=cmds.createNode('follicle')
        fosPers=cmds.listRelatives(fos,p=True)
        fosPersName=cmds.rename(fosPers,'surFO_#')
        fosnew=cmds.ls(sl=True)
        foshapenew=fosnew[0]
            
        cmds.connectAttr(msShape+'.local',fosPersName+'.inputSurface',f=1)
        cmds.connectAttr(msShape+'.worldMatrix[0]',foshapenew+'.inputWorldMatrix',f=1)
        cmds.connectAttr(foshapenew+'.outTranslate',fosPersName+'.translate',f=1)
        cmds.connectAttr(foshapenew+'.outRotate',fosPersName+'.rotate',f=1)
        nodes=cmds.createNode('closestPointOnSurface')
        cmds.connectAttr(msShape+'.worldSpace',nodes+'.inputSurface',f=1)
        cmds.connectAttr(loc+'.translate',nodes+'.inPosition',f=1)
        print loc
        Ul1=cmds.getAttr(nodes+'.parameterU')
        Vl1=cmds.getAttr(nodes+'.parameterV')
        cmds.setAttr(foshapenew+'.parameterU',Ul1)
        cmds.setAttr(foshapenew+'.parameterV',Vl1)
        cmds.delete (nodes)#delete"closestPointOnSurface"
        cmds.delete(objs[i])#delete locate
#---------------------
def aotoStrect():
    #�Զ����칦��
    #ѡ��������ҪIKJnt��ͷ�ټ�ѡ+ѡ��Ik����ȫѡ����һ��ִ�м���
    #ֻ��Ҫ��һ��locate������Լ���Ϳɽ��ȫ����������
    import maya.cmds as cmds
    #loadCurve="curve1"#֮����Ҫ��Ϊ����½
    JntCv=cmds.ls(sl=True)
    
    loadCurve=JntCv[-1]
    cmds.select(loadCurve)
    loadCurveS = cmds.pickWalk(d="down")[0]
    gloLoc = cmds.spaceLocator(n='GlobalLoc',p=(0,0,0))[0] #createLocater
    curveInfo=cmds.createNode("curveInfo")
    cmds.select(curveInfo,r=True)
    cmds.connectAttr(loadCurveS+".worldSpace",curveInfo+".inputCurve",f=1)
    arc=cmds.getAttr(curveInfo+".arcLength")
    #��loc �����һ�������л���aotoStrech����,�û�����Ҫ������ֱ�����ӹ����ͺ� 
    cmds.addAttr( gloLoc,longName='aotoStrech', attributeType='bool',keyable=1)
    aotustretch=gloLoc+'.aotoStrech'
    cmds.setAttr(aotustretch,0);
    cmds.select(cl=True)
    #Part 2 ѡ��Jntִ��
    
    ikJntsel=JntCv[0:-1]
    sum=len(ikJntsel)
    for i in range(1,sum):
        #tx :
        JntX=cmds.getAttr(ikJntsel[i]+'.tx') # Result: 3.0504778018443095 # 
        #m1 :muNode The No 1.
        x=cmds.createNode('multiplyDivide', n="x_#" )  
        cmds.setAttr(x+".operation",1)#
        cmds.connectAttr(gloLoc+".scaleX" , x+".input1X",f=1)
        cmds.connectAttr(gloLoc+".scaleY" , x+".input1Y",f=1)
        cmds.connectAttr(gloLoc+".scaleZ" , x+".input1Z",f=1)
        
        cmds.setAttr( x+".input2X",arc)
        cmds.setAttr( x+".input2Y",arc)
        cmds.setAttr( x+".input2Z",arc)
        #m2: muNode The No 2. 
        x1=cmds.createNode('multiplyDivide', n="x1_#" )
        cmds.setAttr(x1+".operation",2)
            
        cmds.connectAttr(x+".outputX" , x1+".input2X",f=1)
        cmds.connectAttr(curveInfo+".arcLength",x1+".input1X",f=1)
        #m3: muNode The No 3. 
        x2=cmds.createNode('multiplyDivide', n="x2_#" )
        cmds.setAttr(x+".operation",1)#
           
        cmds.setAttr(x2+".input1X",JntX)
        cmds.connectAttr(x1+".outputX" , x2+".input2X",f=1)
        #bc node    
        BC=cmds.createNode("blendColors",n="bc_#" )
        cmds.setAttr(BC+'.blender',1)  
        cmds.connectAttr(x2+".outputX" , BC+".color1R",f=1)
        
        cmds.setAttr(BC+".color2R",JntX)
        cmds.connectAttr(BC+".outputR",ikJntsel[i]+'.tx') 
        cmds.connectAttr(aotustretch,BC+".blender")#�����Ͽ��ط����л��Ƿ����� 
        
#----------------------
def  addAController():
    #��ÿһ��������һ������������������Լ��
    mesh=cmds.ls(sl=True)
    length=len(mesh)
    i=1
    for i in range(length):
        cvpo=cmds.xform(mesh[i],q=1,ws=1,t=1)
        cvName=cmds.circle(r=1,n='ctrl_'+mesh[i])
        mel.eval ('DeleteHistory')
        cvNameoo=cvName[0]
        cvGrp=cmds.group(r=1,n="grp_"+'ctrl_'+mesh[i])
        cmds.parentConstraint(mesh[i],cvGrp,mo=0,weight=1)
        cmds.select(cvGrp)
        cmds.pickWalk(d='down')
        cmds.pickWalk(d='right')
        cmds.delete()
        cmds.parentConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.scaleConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideEnabled',1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideColor',6)
        cmds.select(cvNameoo+'.cv[*:*]')
        cmds.rotate(90,0,0,r=True)
        cmds.select(cl=True)
        
        
#��һ���򵥿���������������״��������
def  addAControllerS():
    #��ÿһ��������һ������������������Լ��
    mesh=cmds.ls(sl=True)
    length=len(mesh)
    i=1
    for i in range(length):
        cvpo=cmds.xform(mesh[i],q=1,ws=1,t=1)
        #cvName=cmds.circle(r=1,n='ctrl_'+mesh[i])
        cvName_c = cmds.curve (d=1, p=[(-1 ,0, 1), ( -1, 0, -1),( 1, 0, -1,) ,( 1, 0, 1),( -1, 0, 1)],k=[ 0 ,1,2 ,3,4])
        cmds.select(cvName_c)
        cvName=cmds.rename('ctrl_'+mesh[i])
        cvNameoo=cvName
        cvGrp=cmds.group(r=1,n="grp_"+'ctrl_'+mesh[i])

        cmds.parentConstraint(mesh[i],cvGrp,mo=0,weight=1)
        cmds.select(cvGrp)
        cmds.pickWalk(d='down')
        cmds.pickWalk(d='right')
        cmds.delete()
        cmds.parentConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.scaleConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.select(cvNameoo)
        
        cvNameooS=cmds.pickWalk(d='down')
        cmds.setAttr(cvNameooS[0]+'.overrideEnabled',1)
        cmds.setAttr(cvNameooS[0]+'.overrideColor',6)
        cmds.select(cvNameooS[0]+'.cv[*:*]')
        #cmds.rotate(90,0,0,r=True)
        cmds.select(cl=True)        
        
#-------------------------

#---------------------------------
#FK Jointchain ѡ������Jointִ��
def FK_Jointchain():
    import maya.cmds as cmds
    import re
    mesh=cmds.ls(sl=True)
    length=len(mesh)
    i=1
    allGrp=[]
    allCtl=[]
    t=0
    for i in range(length):
        cvpo=cmds.xform(mesh[i],q=1,ws=1,t=1)
        cvName=cmds.circle(r=1,n='ctrlFK_'+mesh[i])
        cvNameoo=cvName[0]         
        allCtl.append(cvNameoo)        
        cvGrp=cmds.group(r=1,n="GRP_"+'ctrlFK_'+mesh[i])        
        allGrp.append(cvGrp)
        cmds.parentConstraint(mesh[i],cvGrp,mo=0,weight=1)
        cmds.select(cvGrp)
        cmds.pickWalk(d='down')
        cmds.pickWalk(d='right')
        cmds.delete()
        cmds.parentConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.scaleConstraint(cvNameoo,mesh[i],mo=1,weight=1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideEnabled',1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideColor',6)
        cmds.select(cvNameoo+'.cv[*:*]')
        cmds.rotate(0,90,0,r=True) 
        
    allCtl.sort(reverse=1)
    fKCtrl=allCtl[1:] 
    allGrp.sort(reverse=1)
    fkGrp=allGrp[:-1] 
    # Result: [u'grp_ctrl_joint6', u'grp_ctrl_joint5', u'grp_ctrl_joint4', u'grp_ctrl_joint3', u'grp_ctrl_joint2'] # 
    # Result: [u'ctrl_joint5', u'ctrl_joint4', u'ctrl_joint3', u'ctrl_joint2', u'ctrl_joint1'] # 
    t=0
    for t in range(0,len(allGrp)-1):
        cmds.parent(fkGrp[t],fKCtrl[t])    
        
#--------------*************------------------------------------  
#-----------changeColor--------17 red,13 yellow,6,blue---9,purple------------      
def colorRed():
    selctrl=cmds.ls(sl=True)
    selctrlS=cmds.pickWalk (d ='down')
    for o in selctrlS:    
        cmds.setAttr (o+".overrideEnabled", 1);
        cmds.setAttr (o+".overrideColor", 13);
def colorYellow():
    selctrl=cmds.ls(sl=True)
    selctrlS=cmds.pickWalk (d ='down')
    for o in selctrlS:    
        cmds.setAttr (o+".overrideEnabled", 1);
        cmds.setAttr (o+".overrideColor", 17);
def colorBlue():
    selctrl=cmds.ls(sl=True)
    selctrlS=cmds.pickWalk (d ='down')
    for o in selctrlS:    
        cmds.setAttr (o+".overrideEnabled", 1);
        cmds.setAttr (o+".overrideColor", 6);
def colorPurple():
    selctrl=cmds.ls(sl=True)
    selctrlS=cmds.pickWalk (d ='down')
    for o in selctrlS:    
        cmds.setAttr (o+".overrideEnabled", 1);
        cmds.setAttr (o+".overrideColor", 9);
def colorLightBlue():
    selctrl=cmds.ls(sl=True)
    selctrlS=cmds.pickWalk (d ='down')
    for o in selctrlS:    
        cmds.setAttr (o+".overrideEnabled", 1);
        cmds.setAttr (o+".overrideColor", 18); 
#---------------------------------------
def addShapeList():
    listSel = cmds.textScrollList('shapeList',q= True,allItems=True )
    if (str(type(listSel)) == "<type 'NoneType'>"):#�û�û����ʱ��ִ��pass
        listSel = []
    else:
        pass
    shapeSel = cmds.ls(sl=True)
    for eachShape in shapeSel:#��ÿһ�����û���ѡ����ͷʱ��
        if eachShape in listSel:#���ÿһ���������ı��༭����ͷ�鵽ʱ��ֻ��pass�������append���ı��༭��
            pass
        else:
            cmds.textScrollList('shapeList',e= True,append=eachShape )   

def delShapeList():
    listSel = cmds.textScrollList('shapeList',q= True,selectItem=True )
    for eachListSel in listSel:
        cmds.textScrollList('shapeList',e= True,removeItem=eachListSel)#remove ʱ��ע��e=True�����Ա༭

def parentShape():
    sleJnt=cmds.ls(sl=True)
    shape= cmds.textScrollList('shapeList',q=True,allItems=True)
    for i in sleJnt:
        cmds.parent( shape,i , add=1 ,s=1)
#-------------------------------------------------------
#GlobalSacleConstraint������ȫ�����ţ���ѡmaster��ѡ����ë��ִ�У�
def GlobalSacleConstrain():
    import maya.cmds as cmds
    all=cmds.ls(sl=True)
    driver=all[-1]
    fos=all[0:-1]
    for fo in fos:
        cmds.scaleConstraint( driver,fo,mo=1, weight=1)  
        
        
#----
#˳����cache����,�����ӿ����� ʹ��Ȩ�ص�
#-#��ÿһ��������һ������������������Լ��(�����ר��Ϊ�˿��Լ�pivotCtrl�������һ��joint,
#���joint������Լ����Ĭ������)---------------------
import maya.cmds as cmds
def  addAControllerSkin():    
    mesh=cmds.ls(sl=True)
    length=len(mesh)
    i=1
    for i in range(length):
        cvpo=cmds.xform(mesh[i],q=1,ws=1,t=1)
        cvName=cmds.circle(r=1,n='ctrl_'+mesh[i])
        cvJnt=cmds.joint(r=1,n='Jnt_'+mesh[i])#add Jnt
        cmds.setAttr(cvJnt+".visibility",1)
        cvNameoo=cvName[0]
        cmds.pickWalk (d="up")
        cvGrp=cmds.group(r=1,n="grp_"+'ctrl_'+mesh[i])
        cmds.parentConstraint(mesh[i],cvGrp,mo=0,weight=1)
        cmds.select(cvGrp)
        cmds.pickWalk(d='down')
        cmds.pickWalk(d='right')
        cmds.delete()
        #cmds.parentConstraint(cvJnt,mesh[i],mo=1,weight=1)
        #cmds.scaleConstraint(cvJnt,mesh[i],mo=1,weight=1)
        cmds.skinCluster(cvJnt,mesh[i],bindMethod=0,normalizeWeights=1)    
        cmds.setAttr(cvNameoo+'Shape'+'.overrideEnabled',1)
        cmds.setAttr(cvNameoo+'Shape'+'.overrideColor',6)
        cmds.select(cvNameoo+'.cv[*:*]')
        cmds.rotate(90,0,0,r=True)
        cmds.select(cl=True)

      
if __name__ == "__main__":
    myClass()
#------------------------------------------------------------------------