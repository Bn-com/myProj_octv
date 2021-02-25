#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.nurbsCurveCon import *
from RIG.commonly.base import *
import maya.mel as MEL

def SK_stretchSplineIK (preFixName = '',part='waist',jointChainStartJoint = 'waist1_jnt',FKChainStartJoint = 'waist1_FK',kind = 'human',masterCtrl = 'Character'):
    scalVal = rig.getAttr('LfLeg_Leg_IK.scaleVal')



    ##----------  get the joint which one to be created IK ---------##

    rig.select(jointChainStartJoint,hierarchy=True)
    jointChainList = rig.ls(sl=True)
    numOfJoint = len(jointChainList )
    midJointIndex = numOfJoint //2
    jointChainEndJoint = jointChainList [numOfJoint -1]

    ##--------- create splineIK --------##
    try:
        rig.ikHandle(name= preFixName +'ikHandle_' +part,startJoint=jointChainStartJoint,endEffector=jointChainEndJoint ,numSpans=3,solver='ikSplineSolver',
    rootOnCurve=True,parentCurve=True,createCurve=True,simplifyCurve=False,twistType='linear')
    except:
        pass
    rig.rename('curve1',preFixName +'curve_'+part)
    rig.rename('effector1',preFixName + 'effector_'+part)

    rig.select(cl=True)
    ##--------- create CurveSkinJoint ----------##

    startJointPosi = rig.xform(jointChainStartJoint ,worldSpace=True,query=True,translation=True)
    midJointPosi = rig.xform(jointChainList [midJointIndex ] ,worldSpace=True,query=True,translation=True)
    endJointPosi = rig.xform(jointChainEndJoint ,worldSpace=True,query=True,translation=True)

    rootSkinJoint = preFixName + 'curve_root_SkinJoint_' + part
    midSkinJoint = preFixName + 'curve_mid_SkinJoint_' + part
    topSkinJoint = preFixName + 'curve_end_SkinJoint_' + part
   

    rig.joint(p=startJointPosi ,n=rootSkinJoint)
    rig.select(cl=True)
    rig.joint(p=midJointPosi ,n=midSkinJoint)
    rig.select(cl=True)
    rig.joint(p=endJointPosi ,n=topSkinJoint)
    rig.select(cl=True)
    
    ## ------ create hip_jnt ----- ##
    jntRadius = rig.getAttr(preFixName + 'waist1_jnt.radius')
    
    hipJnt = preFixName + 'hip_jnt'    
    
    rig.joint(p=startJointPosi,n=hipJnt)    
    rig.select(cl=True)

    rig.setAttr(preFixName + 'waist1_jnt.radius',jntRadius/5)
    rig.setAttr(hipJnt+'.radius',jntRadius)
    
    
    ##----------- skinBind the spIK's curve -----------##

    rig.select(rootSkinJoint ,midSkinJoint ,topSkinJoint,add=True)
    rig.select(preFixName + 'curve_' +part,add=True)
    rig.skinCluster(toSelectedBones=True,
            maximumInfluences=2,
            dropoffRate=4,
            removeUnusedInfluence=True,
            n=preFixName + 'skinCluster_' +part)

    ##----------- create circle for spIK's skinJoint ctrl ---------------##

    for eachSpIKctrlPosi in ('root','mid','top'):
        if kind == 'human':
    
            ikCtrlCircle = rig.rename(SK_b29(13), preFixName + eachSpIKctrlPosi +'_' +part+ '_ikCtrl')
            rig.setAttr(ikCtrlCircle+'.scale',0.25*scalVal,0.25*scalVal,0.25*scalVal)
            SK_freezeObj(ikCtrlCircle)
            rig.select(ikCtrlCircle)
            MEL.eval('DeleteHistory;')
            rig.group(n = ikCtrlCircle +'_GRP')

            HideAttrName = ('.sx','.sy','.sz')

            for eachAttrName in HideAttrName :
                rig.setAttr(ikCtrlCircle + eachAttrName ,lock=True,keyable=False,channelBox =False)
            rig.setAttr(ikCtrlCircle + '.visibility',keyable=False,channelBox =False)
            rig.select(cl=True)

        else:
            ikCtrlCircle = rig.rename(SK_b29(13), preFixName + eachSpIKctrlPosi +'_' +part+ '_ikCtrl')
            rig.select(ikCtrlCircle)  
            rig.setAttr(ikCtrlCircle+'.scale',0.25*scalVal,0.25*scalVal,0.25*scalVal)
            SK_freezeObj(ikCtrlCircle)      
            MEL.eval('DeleteHistory;')
            rig.group(n = ikCtrlCircle +'_GRP')

            HideAttrName = ('.sx','.sy','.sz')

            for eachAttrName in HideAttrName :
                rig.setAttr(ikCtrlCircle + eachAttrName ,lock=True,keyable=False,channelBox =False)
            rig.setAttr(ikCtrlCircle + '.visibility',keyable=False,channelBox =False)
            rig.select(cl=True)

    ##----------- parentConstraint each ctrl to the skinJoint -----------##

    topIKctrl = preFixName + 'top_' + part + '_ikCtrl'
    midIKctrl = preFixName + 'mid_' + part + '_ikCtrl'
    rootIKctrl = preFixName + 'root_' + part + '_ikCtrl'

    for eachSpIKctrlPosi in ('root','mid','top'):
        if eachSpIKctrlPosi == 'root':
            IKpointConst = rig.pointConstraint(rootSkinJoint ,  rootIKctrl  +'_GRP' ,mo=False)
            rig.delete(IKpointConst)
            rig.parentConstraint(rootIKctrl  , rootSkinJoint ,mo=True)

        elif eachSpIKctrlPosi == 'mid':
            IKpointConst = rig.pointConstraint(midSkinJoint ,  midIKctrl  +'_GRP' ,mo=False)
            rig.delete(IKpointConst)
            rig.parentConstraint(midIKctrl  , midSkinJoint,mo=True)

        elif eachSpIKctrlPosi == 'top':
            IKpointConst = rig.pointConstraint(topSkinJoint ,  topIKctrl  +'_GRP' ,mo=False)
            rig.delete(IKpointConst)
            rig.parentConstraint(topIKctrl  , topSkinJoint,mo=True)

    ## parentConst the hipJnt ##
    rig.parentConstraint(rootIKctrl , hipJnt , mo = True)


    ##----------- set ik advanced Twist Controls -----------##
    rig.setAttr(preFixName +'ikHandle_' +part + '.dTwistControlEnable' ,1)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpType', 4)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpAxis', 4)

    #if kind == 'human':
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVector', 1,0,0)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVectorEnd', 1,0,0)
    rig.connectAttr(rootIKctrl  +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrix')
    rig.connectAttr(topIKctrl  +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrixEnd')
    
    #else:
        #rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVector', 0,1,0)
        #rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVectorEnd', 0,1,0)
        #rig.connectAttr(rootIKctrl +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrix')
        #rig.connectAttr(topIKctrl  + 'ikCtrl_top_' +part +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrixEnd')


    ##----------- clean up the DAG ------------##
    partDoNotTouch = rig.group(jointChainStartJoint ,preFixName +'curve_'+part, preFixName +'ikHandle_' +part ,rootSkinJoint ,midSkinJoint ,topSkinJoint ,n=preFixName +part+'_doNotTouch_GRP')



    ##------------ create stretchIK system and use expr -----------##
    
    # create master refer GRP #
    masterRefer = rig.group(n=preFixName + 'master_refer_GRP',empty=True)
    rig.parent(masterRefer,partDoNotTouch)

    rig.arclen( preFixName +'curve_'+part ,ch=True,n=part+'_curveLenInfo')
    curveInfo = rig.rename('curveInfo1',preFixName + part + '_curveLenInfo')

    curveOrigLen = rig.getAttr(curveInfo +'.arcLength')


    ##### expr string ######
    NumtransJoint = numOfJoint-1
    exprStr = '$newDis ='+ curveInfo +'.arcLength/(Character.scaleX*master_refer_GRP.scaleX)' + '-' + str(curveOrigLen) + ';\n'
    exprStr += '$scale ='+ curveInfo +'.arcLength/(Character.scaleX*master_refer_GRP.scaleX*' + str(curveOrigLen)  + ');\n'
    
    exprStr += '$trans = $newDis/' + str(NumtransJoint) + ';\n'
    exprStr += '$invScale = 1/sqrt($scale);\n'

    for k in range(1,numOfJoint,1):
        origTx = rig.getAttr(jointChainList [k] + '.tx')        
        exprStr += jointChainList [k] +'.tx =' + str(origTx) + '+ $trans;\n'
        exprStr += jointChainList [k] +'.scaleY = pow($invScale,1);\n'
        exprStr += jointChainList [k] +'.scaleZ = pow($invScale,1);\n'

    rig.expression(s =exprStr , n =part+'_expr')
    

    ##------ correct Curve double transform ------##
    rig.setAttr(preFixName +'curve_'+part+'.inheritsTransform',0)



    ##---------- create FKchain ----------##
    
    startJointPosi = rig.xform(jointChainStartJoint,q=True,ws=True,rp=True)
    endJointPosi = rig.xform(jointChainEndJoint ,q=True,ws=True,rp=True)
    
    rig.select(cl=True)
    rig.joint( p=(startJointPosi[0],startJointPosi[1],startJointPosi[2]),n = preFixName +part +'1_FK_refer')
    rig.joint( p=(endJointPosi [0],endJointPosi [1],endJointPosi [2]),n = preFixName +part +'2_FK_refer')

    rig.select(preFixName +part +'1_FK_refer')
    SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = preFixName +part +'1_FK_refer',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    SK_TempSplitSelJoint(startJoint = preFixName +part +'1_FK_refer',segments = 2)

    # rename FK chain #
    rig.rename(preFixName +part +'1_FK_refer',preFixName +part +'1_FK')    
    rig.select(preFixName +part +'1_FK')
    FKList = rig.ls(sl=True)
    firstFK = FKList [0]
    for numFK in range(2,4,1):
        oldNextJoint = rig.pickWalk(firstFK ,d='down')
        newNextJoint = rig.rename(oldNextJoint ,preFixName + part + str(numFK) + '_FK' )
        firstFK = newNextJoint

    # orient FK chain #
    SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = preFixName +part +'1_FK',JointAimVector= (0,1,0),JointUpVector = (0,0,1))

    # create FK1 ctrl #
    rig.rename(SK_b01(6),'torso_anim')
    FK1Ctrl = rig.rename('torso_anim',preFixName +part + '_FK1_ctrl')
    rig.setAttr(FK1Ctrl+'.scale',2*scalVal,0.1*scalVal,2*scalVal)
    SK_freezeObj(FK1Ctrl)
    
    FK1CtrlGRP=rig.group(n=FK1Ctrl+'_GRP',empty=True)
    rig.parent(FK1Ctrl,FK1CtrlGRP)

    FK1PosiConst = rig.pointConstraint(preFixName +part +'2_FK' , FK1CtrlGRP , mo=False)
    rig.delete(FK1PosiConst)
    
    # create FK2 ctrl #
    rig.rename(SK_b01(6),'torso_anim')
    FK2Ctrl = rig.rename('torso_anim',preFixName +part + '_FK2_ctrl')
    rig.setAttr(FK2Ctrl+'.scale',2*scalVal,0.1*scalVal,2*scalVal)
    SK_freezeObj(FK1Ctrl)
    
    FK2CtrlGRP=rig.group(n=FK2Ctrl+'_GRP',empty=True)
    rig.parent(FK2Ctrl,FK2CtrlGRP)

    FK2PosiConst = rig.pointConstraint(preFixName +part +'3_FK' , FK2CtrlGRP , mo=False)
    rig.delete(FK2PosiConst)
    
    rig.parent(FK2CtrlGRP,FK1Ctrl)
    
    # hide attrs of FK #
    for eachFK in (FK1Ctrl,FK2Ctrl):
        for eachFKHideAttr in ('.sx','.sy','.sz'):
            rig.setAttr(eachFK + eachFKHideAttr ,keyable=False,channelBox=False,lock=True)
        rig.setAttr(eachFK + '.visibility' ,keyable=False,channelBox=False,lock=False)
        
    
    
    #-- delete fk chain --#
    rig.delete(preFixName +part +'1_FK')
    
       
    ## ------------------ clean Up the rig ----------------------##

    # hide things what we don't want to see  #
    rig.hide(preFixName +'ikHandle_' +part)
    rig.hide(rootSkinJoint,midSkinJoint)
    #rig.hide(topSkinJoint)
    rig.hide(preFixName + 'curve_' +part)

    ## correct orient Order , i hate gimbal lock >_<

    #FK
    rig.setAttr(FK1Ctrl + '.rotateOrder' , 4)
    rig.setAttr(FK2Ctrl + '.rotateOrder' , 4)

    #IK
    for eachIKctrl in(topIKctrl,midIKctrl,rootIKctrl):
        rig.setAttr(eachIKctrl + '.rotateOrder' , 3)

    # make a torsoGRP
    partGRP = rig.group( empty = True , n = preFixName + part + '_GRP' ,  world = True)
    ikGRP = rig.group( empty = True , n = preFixName + part + 'ikCtrl_GRP' ,  world = True)
    rig.parent(ikGRP,partGRP)
    rig.parent(partDoNotTouch , partGRP )
    rig.parent(hipJnt , partDoNotTouch)
    rig.parent(rootIKctrl +'_GRP' , ikGRP)
    rig.parent(midIKctrl +'_GRP' , ikGRP)
    rig.parent(topIKctrl +'_GRP' , ikGRP)
    rig.parent(FK1CtrlGRP, partGRP )
    
    ##--------- parentConstraint the ik by the FKctrl --------##
    rig.parentConstraint(FK1Ctrl,midIKctrl +'_GRP',mo=True)
    rig.parentConstraint(FK2Ctrl,topIKctrl +'_GRP',mo=True) 

    ## create torso GRP ##
    rig.rename(SK_b13(17),'circleArrow')
    partCtrl = rig.rename('circleArrow' ,preFixName + part + '_Ctrl')
    rig.setAttr(partCtrl+'.scale',0.7*scalVal,0.7*scalVal,0.7*scalVal)
    SK_freezeObj(partCtrl)
    partCtrlGRP = rig.group(partCtrl, n= partCtrl + '_GRP')

    #hide Attr
    for eachPartCtrlAttr in ('.sx','.sy','.sz'):
        rig.setAttr(partCtrl+ eachPartCtrlAttr ,keyable=False,channelBox=False,lock=True)
    rig.setAttr(partCtrl+ '.visibility' ,keyable=False,channelBox=False)

    partGRPpointConst = rig.pointConstraint(preFixName + 'waist1_jnt' , partCtrlGRP , mo =False)
    rig.delete(partGRPpointConst )
    rig.parent(partGRP ,partCtrl)

    ## create expr for the waist's IKFK switch ##
    rig.addAttr(partCtrl, longName = 'ikfk_switch' , attributeType = 'enum' , en = 'ik:fk:both:' , keyable = True)
    ####### connect by the expr ########

    ikfkExprStr = '$ikfk ='+ partCtrl +'.ikfk_switch; \n'
    ikfkExprStr += 'if($ikfk==0){\n'
    ikfkExprStr += 'waist_FK1_ctrl.visibility=0;\n'
    ikfkExprStr += 'waist_FK2_ctrl.visibility=0;\n'
    ikfkExprStr += 'mid_waist_ikCtrl.visibility=1;\n'
    ikfkExprStr += 'top_waist_ikCtrl.visibility=1;}\n'
    
    ikfkExprStr += 'if($ikfk==1){\n'
    ikfkExprStr += 'waist_FK1_ctrl.visibility=1;\n'
    ikfkExprStr += 'waist_FK2_ctrl.visibility=1;\n'
    ikfkExprStr += 'mid_waist_ikCtrl.visibility=0;\n'
    ikfkExprStr += 'top_waist_ikCtrl.visibility=0;}\n'
    
    ikfkExprStr += 'if($ikfk==2){\n'
    ikfkExprStr += 'waist_FK1_ctrl.visibility=1;\n'
    ikfkExprStr += 'waist_FK2_ctrl.visibility=1;\n'
    ikfkExprStr += 'mid_waist_ikCtrl.visibility=1;\n'
    ikfkExprStr += 'top_waist_ikCtrl.visibility=1;}\n'

    rig.expression(s =ikfkExprStr , n =part+'ikfk_switch_expr')
    
    rig.setAttr(preFixName+'waist_Ctrl.ikfk_switch',1)   
  
    #rename the waist_jnt
    rig.rename(preFixName + 'waist1_jnt' , preFixName + 'waist1_root')

