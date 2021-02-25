#-*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel

#插件里头的用户自定义参数,数值为1的时候即是2段

#调用FK N次d
def SK_neckRig():


#首先建立一个曲面     
    neckJntsA=('neck1_jnt') #函数引用
    cmds.select (neckJntsA ,hi=True)
    neckJntTA = cmds.ls( sl=True)
    num=len(neckJntTA)-1
    
    scalVal = cmds.getAttr('LfLeg_Leg_IK.scaleVal')  #10) globalScale 
    neckRadius = cmds.getAttr(neckJntsA + '.radius')
    pos = []
    for i in neckJntTA:
        p = cmds.xform(i,q=True,ws=True,rp=True)
        print p
        pos.append(p)
    print pos
    cv_org = cmds.curve(n="cv_org", d=1,p=pos )
    copyLf = cmds.duplicate(cv_org,rr=True)
    copyRt = cmds.duplicate(cv_org,rr=True)
    
    cmds.move(0.3*scalVal,0,copyLf)  #  宽度
    cmds.makeIdentity( copyLf,apply=True,t=True,r=True,s=True,n=True) 
    cmds.move(-0.3*scalVal,0,0,copyRt) #  宽度    
    cmds.makeIdentity( copyRt,apply=True,t=True,r=True,s=True,n=True) 
    cv_lf = cmds.rename(copyLf, 'cv_lf')
    cv_rt = cmds.rename(copyRt, 'cv_Rt')    
    palaneGrp=cmds.loft( cv_lf, cv_rt,ch=True, rn=0, ar=True,u=1 ,c= 0,d= 3,ss =True,rsn= True,po =0)
    
    palane = palaneGrp[0]
    mel.eval('DeleteHistory')  
    cmds.delete(cv_org,cv_lf,cv_rt)

#2)控制器 并于曲面skin one by one
   # sy="cluste_1"
    skinJnts = []
    fkctrlss = []
    ikctrls = []
    for sy in  range(num+1) :
        circle_C(scalVal)#import  def 
        cmds.rotate(-90,0,90,r=True)
        fkctrls =cmds.ls(sl=True)
        
        cmds.select(fkctrls,hierarchy = True)
        allhis= cmds.ls(sl=True)
        skinJnt = allhis[-1]
        ikctrl = allhis[-2]
        
    
        skinJnts.append(skinJnt)
        fkctrlss.append(fkctrls)
        ikctrls.append(ikctrl)
        print skinJnts
        print fkctrlss
        print ikctrls
    #cmds.select(skinJnts)
    #cmds.select(palane,add=True)    
    #cmds.skinCluster(toSelectedBones=True,maximumInfluences=1,skinMethod=3,dropoffRate=4,removeUnusedInfluence=True)
#2)控制器定位到身体插件上面去(按照反序号)
    aa = cmds.listRelatives('ikJnt_neck_1',ap=True)
    fkctrlssT = fkctrlss
    #neckJnts(neck='neck1_jnt') #函数引用 不想用反序先
    cmds.select (neckJntsA,hi=True)
    neckJntT = cmds.ls( sl=True)
    for c in range(len(neckJntT)):
        cmds.parent ( fkctrlssT[c],neckJntT[c],r=True) # GRPikCtrl_neck_4
        cmds.setAttr( fkctrlssT[c][0]+'.translateX', 0)
        cmds.setAttr( fkctrlssT[c][0]+".translateY", 0)
        cmds.setAttr( fkctrlssT[c][0]+".translateZ", 0)
        cmds.setAttr( fkctrlssT[c][0]+".rotateX" ,0)
        cmds.setAttr( fkctrlssT[c][0]+".rotateY", 0)
        cmds.setAttr( fkctrlssT[c][0]+".rotateZ", 0)
        cmds.parent ( fkctrlssT[c],w=True)  #parent to world
        
#3)曲面的处理
    Dpalane = cmds.duplicate( palane,rr=True,name='neck_nurbs')
    cmds.rebuildSurface(Dpalane, rt=0,end=1, kr =0,kcp= 0,dir=2, su=num, sv=0 ,kc=0,fr=0)
    #makeIdentity 的preserveNormals=True 标签maya2012,64位不能识别
    cmds.delete(palane)  #old palane delete  
#4)fo and newNurbs skin
    CreateFollicleOnsurface(fkctrlssT,Dpalane[0],'neck','GrpNeckRigfo',neckRadius)
    cmds.select(skinJnts)
    cmds.select(Dpalane,add=True)
    cmds.skinCluster(toSelectedBones=True,maximumInfluences=1,skinMethod=3,dropoffRate=4,removeUnusedInfluence=True)
#5)headJnt P
    try:
        if "head_jnt":
            headJnt = "head_jnt"
            PfkCtrl = cmds.listRelatives( fkctrlss[-1], c=True)
            cmds.parent (headJnt,PfkCtrl)  #p
    except:
        pass
    allCflCtrl = []
    for v in range(len(fkctrlss)):
        CfkCtrl = cmds.listRelatives( fkctrlss[v][0], c=True)
        allCflCtrl.append(CfkCtrl)
    allCflCtrl.reverse()
    fkctrlss.reverse()
    parentP(allCflCtrl,fkctrlss)
    
    allCflCtrl.reverse()
    fkctrlss.reverse()

# Result: sle= [[u'fkCtrl_neck_4'], [u'fkCtrl_neck_3'], [u'fkCtrl_neck_2'], [u'fkCtrl_neck_1']] # 
# Result: grp =[[u'GRPfkCtrl_neck_4'], [u'GRPfkCtrl_neck_3'], [u'GRPfkCtrl_neck_2'], [u'GRPfkCtrl_neck_1']] # 
#6) clear Up
#fkctrlssT[-1] = 'GRPfkCtrl_neck_5'  ,DpalaneGrp='GrpNeckDpalane'
    fklastTras = fkctrlssT[0]
    neckGrp = cmds.group(empty = True,n = 'neck_GRP')
    cmds.parentConstraint(fklastTras,neckGrp,mo=0,weight=1)
    cmds.select(neckGrp )
    cmds.pickWalk(d ='down')  
    cmds.delete()
    cmds.parent(fklastTras,neckGrp)
    DpalaneGrp = cmds.group(Dpalane,n = 'GrpNeckDpalane')
    DeformerNeck = cmds.group(empty = True,n = 'DeformerNeck')
    cmds.parent(DpalaneGrp,DeformerNeck)
    cmds.parent('GrpNeckRigfo',DeformerNeck)
    cmds.setAttr(DpalaneGrp+'.visibility',0)
    for sk in skinJnts:
        cmds.setAttr(sk+'.visibility',0)

#7)head_ctrl addattr follow and reverseNode
#headLoc='headCtrlFollow_Loc'
    headCtrl = cmds.rename (allCflCtrl[-1]  ,'head_ctrl')  
    cmds.addAttr(headCtrl , longName = 'rotation' , attributeType = 'enum' , en = 'neck:body' , keyable = True)
    headLoc = cmds.spaceLocator(n='headCtrlFollow_Loc')
    headLocGrp = cmds.group(headLoc,name='GRP_'+headLoc[0])
    #cmds.parent (headLocGrp,neckGrp)
    cmds.parent (headLocGrp, 'waist_Ctrl')
    
    
    for eachattr in (".tx",'.ty','.tz',".rx",'.ry','.rz'):
        cmds.setAttr(headLocGrp+eachattr,0)
    headGrp = cmds.group(headCtrl ,name='GrpCon'+headCtrl)
    cmds.xform (os =True,piv=( 0 ,0, 0))        
    neckCon= cmds.parentConstraint(headLoc,headGrp,mo=1,weight=1,st=["x","y","z"])
    cmds.setAttr (headLoc[0] +".visibility" ,0)
    #reverNode = cmds.createNode ('reverse',name = 'neck_RV')
   # cmds.connectAttr(headCtrl+'.rotation' , reverNode+'.inputX')
   # cmds.connectAttr(reverNode+'.outputX' , neckCon[0]+'.'+headLoc[0] + 'W0')
    cmds.connectAttr(headCtrl+'.rotation' ,neckCon[0]+'.'+headLoc[0] + 'W0')
#8) parent the neckGrp  to Body
    try:
        if 'waist_Ctrl':
            cmds.parent( neckGrp, 'waist_Ctrl')
            #cmds.hide("neck1_jnt")  
                      
    except:
        pass
    try:
        if 'others_deformers':
            cmds.parent('DeformerNeck','others_deformers')
    except:
        pass
#9)add 'ikCtrlVis' attr to the fristFK and Connnection
    
    cmds.addAttr( headCtrl,longName='ikCtrlvis',attributeType ='bool',keyable=1)
    #skinJnts=[ikJnt_neck_2 ikJnt_neck_3 ikJnt_neck_4]
    if skinJnts:
    #headCtrl =' head_ctrl ' 
        for ik in ikctrls:
            cmds.connectAttr(headCtrl+'.ikCtrlvis',ik+'.visibility',f=True)
            
#10 connect neckJnt with  skinJnts
    for c in range(len(neckJntTA)):
        
        cmds.parentConstraint(skinJnts[c],neckJntTA[c],mo=1,weight=1)
        cmds.scaleConstraint(skinJnts[c],neckJntTA[c],mo=1,weight=1)
        
#11
    if 'Character':
        cmds.select("GrpNeckRigfo",hi=True)
        follices = cmds.ls( sl=True,s=True)
        fosPerss=cmds.listRelatives(follices ,p=True)
        scaleFO('Character',fosPerss)
    else:
        pass
#[u'neck1_jnt', u'neck2_jnt', u'neck3_jnt', u'neck4_jnt']
#[u'ikJnt_neck_1', u'ikJnt_neck_2', u'ikJnt_neck_3', u'ikJnt_neck_4']        
#  neckJntTA  skinJnts    
#siger DEF Air----，控制器的建立(到时候可以单独调)------
def circle_C(scalVal=0.5):
    #name=cmds.textField('input',q=True,tx=True)
    name="neck_#"
    cr=cmds.circle(n='fkCtrl_'+name,r=1.5)
    cmds.setAttr(cr[0]+'.scaleX',scalVal)
    cmds.setAttr(cr[0]+'.scaleY',scalVal)
    cmds.setAttr(cr[0]+'.scaleZ',scalVal)
    cmds.makeIdentity(apply = True,s = True,r = True,t = True)
    #add attr '.ctrl' for add bodySet ,remark
    cmds.addAttr( cr[0],longName='ctrl', attributeType='float',keyable=0,defaultValue=1,minValue=0,maxValue=1)  
    mel.eval('DeleteHistory')
    cmds.select(cr[0]+'.cv[*:*]')
    cmds.rotate(0,90,0,r=True)
    cmds.select(cl=True)
    cmds.select(cr[0])
    grpfk=cmds.group(n='GRPfkCtrl_'+name)
    cmds.pickWalk(d='down')
    s=cmds.ls(sl=True)
    print s
    cmds.setAttr(s[0]+'Shape'+".overrideEnabled",int(1))
    cmds.setAttr(s[0]+'Shape'+".overrideColor",6)
         
    crik=cmds.circle(n='ikCtrl_'+name,r=1)
    cmds.setAttr(crik[0]+'.scaleX',scalVal)
    cmds.setAttr(crik[0]+'.scaleY',scalVal)
    cmds.setAttr(crik[0]+'.scaleZ',scalVal)
    cmds.makeIdentity(apply = True,s = True,r = True,t = True)
   #add attr '.ctrl' for add bodySet ,remark
    cmds.addAttr( crik[0],longName='ctrl', attributeType='float',keyable=0,defaultValue=1,minValue=0,maxValue=1)  
    cmds.select(crik[0]+'.cv[*:*]')
    cmds.rotate(0,90,0,r=True)
    cmds.select(cl=True)
    cmds.select(crik[0])
    grpik=cmds.group(n='GRPikCtrl_'+name)
    cmds.pickWalk(d='down')
    sik=cmds.ls(sl=True)
    cmds.joint(n='ikJnt_'+name,radius=0.1)
    print sik
    cmds.setAttr(sik[0]+'Shape'+".overrideEnabled",int(1))
    cmds.setAttr(sik[0]+'Shape'+".overrideColor",13)
        
    cmds.select(grpfk)
    crobj=cmds.pickWalk(d='down')
    cmds.parent(grpik,crobj)
    cmds.select(grpfk)
    
    

    
def neckJnts(neck='neck1_jnt'):
    cmds.select (neck,hi=True)
    neckls = cmds.ls(sl=True)
    neckls.reverse()
    cmds.select( neckls,r=True)
    print neckls  #[u'neck4_jnt', u'neck3_jnt', u'neck2_jnt', u'neck1_jnt']

def hideLockAll(obj,removeAttr=[]):#锁定并隐藏jnt或是物体
    attrs = cmds.listAttr(obj,k = True)  
    transAttr = [u'translateX', u'translateY', u'translateZ']
    scaleAttr = [u'scaleX', u'scaleY', u'scaleZ']
    rotateAttr = [u'rotateX', u'rotateY', u'rotateZ']
    if attrs:
        if not removeAttr:
	        for attr in attrs:
	            cmds.setAttr(obj+'.'+attr,cb = False,k = False,l = True)
	        if(cmds.attributeQuery('radius',node = obj,ex = True)):
	            cmds.setAttr(obj+'.radius',cb = False,k = False,l = True)    
def showLockAll(obj):
     attrs = cmds.listAttr(obj,l = True)
     for attr in attrs:
     	cmds.setAttr(obj+'.'+attr,k = True,l = False)

#mesh= ["neck_nurbs2",]
#objs = [[u'GRPfkCtrl_neck_1'], [u'GRPfkCtrl_neck_2'], [u'GRPfkCtrl_neck_3'], [u'GRPfkCtrl_neck_4'], [u'GRPfkCtrl_neck_4']] #
#objs=[['locator1'],['locator2']]
#mesh= 'nurbsPlane1'
#namepix = 'c'
#fogrpName = 'GrpneckRigfo'
# numB = 3
def CreateFollicleOnsurface(objs,mesh,namepix,fogrpName,Radius):
    #objs=cmds.ls(sl=True)
    #mesh=objs[0]
    cmds.rebuildSurface(mesh,ch=1,rpo=1,rt=0,end=1,kr=0,kcp=1,kc=0,su=4,du=3,sv=4,dv=3,tol=0.01,fr=0,dir=2)
        
    mun=len(objs)
    meshShape=cmds.listRelatives( mesh)
    msShape=meshShape[0]
    neckGrp = cmds.group(empty = True,n =fogrpName)
    #i=1
    for i in range(mun):        
        loc=objs[i]
        fos=cmds.createNode('follicle')
        cmds.parent(fos,neckGrp)
        fosPers=cmds.listRelatives(fos,p=True)
        fosPersName=cmds.rename(fosPers,namepix+'sufo_#')
        fosnew=cmds.ls(sl=True)
        foshapenew=fosnew[0]
            
        cmds.connectAttr(msShape+'.local',fosPersName+'.inputSurface',f=1)
        cmds.connectAttr(msShape+'.worldMatrix[0]',foshapenew+'.inputWorldMatrix',f=1)
        cmds.connectAttr(foshapenew+'.outTranslate',fosPersName+'.translate',f=1)
        cmds.connectAttr(foshapenew+'.outRotate',fosPersName+'.rotate',f=1)
        nodes=cmds.createNode('closestPointOnSurface')
        cmds.connectAttr(msShape+'.worldSpace',nodes+'.inputSurface',f=1)
        cmds.connectAttr(loc[0]+'.translate',nodes+'.inPosition',f=1)  #add [0]
        print loc
        Ul1=cmds.getAttr(nodes+'.parameterU')
        Vl1=cmds.getAttr(nodes+'.parameterV')
        cmds.setAttr(foshapenew+'.parameterU',Ul1)
        cmds.setAttr(foshapenew+'.parameterV',Vl1)
        shape = cmds.listRelatives(foshapenew,s=True)
        cmds.setAttr(shape[0]+'.visibility',0)  #foshapenew='necksufo_1'
        cmds.delete (nodes)
        suJnt = cmds.createNode('joint',n=namepix+'suJnt_#')
        cmds.parent(suJnt,fosPersName)
        cmds.setAttr(suJnt + '.radius', 0.2*Radius)
        for attr in ('tx','ty','tz','rx','ry','rz'):
            cmds.setAttr(suJnt+'.'+attr,0)
            
        #delete"closestPointOnSurface"
        #cmds.delete(objs[i])#delete locate

def parentP(sle,grp):
# sle = ['nurbsCircle1',' nurbsCircle2',' nurbsCircle3']
# grp = [ 'group1','group2','group3']
    for i in range(len(sle)-1):
        zi = grp[i]
        fu = sle[i+1]
        cmds.parent (zi,fu)


def scaleFO(master,objs):
    for obj in objs:
        cmds.scaleConstraint(master,obj,mo=1,weight=1)
        
        
#createNeck()  #函数-----------------------------
 
