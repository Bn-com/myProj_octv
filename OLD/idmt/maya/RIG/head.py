#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.nurbsCurveCon import *
from RIG.commonly.base import *
import maya.mel as MEL

def SK_createMeasureTool (startAim = 'SlayeR_Lf_upArm_ik',endAim = 'SlayeR_Lf_wrist_ik',disName = 'SlayeR_Lf_armDis'):
    startPosi = rig.xform(startAim,q=True,ws=True,rp=True)
    endPosi = rig.xform(endAim , q=True,ws=True,rp=True)


    ##------------ create the locators by hand --------------##
    startLoc = rig.spaceLocator(n= startAim + '_dis_start')
    endLoc = rig.spaceLocator(n= endAim + '_dis_end')

    rig.move(startPosi[0] ,startPosi[1] ,startPosi[2] ,startLoc[0] ,a=True,ws=True)
    rig.move(endPosi[0] ,endPosi[1] ,endPosi[2] ,endLoc[0] ,a=True,ws=True)

    ##----------- create the dis node and connect It ------------##
    disNode = rig.createNode('distanceDimShape')
    oldDis = rig.listRelatives(disNode ,f=True ,p=True)
    newDis = rig.rename(oldDis ,disName)
    listDisShape = rig.listRelatives(newDis ,f=True ,s=True)
    newDisShape = listDisShape [0]


    rig.connectAttr(startLoc[0] + '.worldPosition[0]' , newDis + '.startPoint' , f=True)
    rig.connectAttr(endLoc[0] + '.worldPosition[0]' , newDis + '.endPoint' , f=True)

    ### you can choose anthor way to create the dis ##
    #dimension = (distanceDimension ,sp =startPosi[0],startPosi[1],startPosi[2], ep = endPosi[0] ,endPosi[1],endPosi[2])

    return(newDis)


def SK_neckRig (preFixName = '',part='neck',jointChainStartJoint = 'neck1_jnt',FKChainStartJoint = 'neck1_FK',kind = 'human',masterCtrl = 'Character'):
    scalVal = rig.getAttr('LfLeg_Leg_IK.scaleVal')
    neckRadius = rig.getAttr(jointChainStartJoint + '.radius')


    ## create head control ##
    headCtrl = rig.rename(SK_b29(6),preFixName + 'head_ctrl')
    rig.setAttr(headCtrl+'.rx',90)
    rig.setAttr(headCtrl+'.scale',0.15*scalVal,0.15*scalVal,0.15*scalVal)
    SK_freezeObj(headCtrl)
    MEL.eval('DeleteHistory;')
    headCtrlGRP = rig.group( empty = True , n= headCtrl + '_GRP' ,  world = True )
    rig.parent(headCtrl , headCtrlGRP )
    headCtrlConst = rig.pointConstraint(preFixName + 'head_jnt' , headCtrlGRP )

    rig.delete(headCtrlConst)

    rig.parent(preFixName + 'head_jnt' , headCtrl)

    # hide headCtrl attr #
    for eachHideAttr in ('.sx','.sy','.sz','.visibility'):
        rig.setAttr(headCtrl+eachHideAttr ,lock=True,keyable=False,channelBox =False)

    ##----------  get the joint which one to be created IK ---------##

    rig.select(jointChainStartJoint,hierarchy=True)
    jointChainList = rig.ls(sl=True)
    numOfJoint = len(jointChainList )
    midJointIndex = (numOfJoint //2)+1
    jointChainEndJoint = jointChainList [numOfJoint -1]

    ##--------- create splineIK --------##
    try:
        rig.ikHandle(name= preFixName +'ikHandle_' +part,startJoint=jointChainStartJoint,endEffector=jointChainEndJoint ,numSpans=3,solver='ikSplineSolver',
    rootOnCurve=True,parentCurve=True,createCurve=True,simplifyCurve=False,twistType='linear')
    except:
        pass
    rig.rename('curve1',preFixName +'curve_'+part)


    rig.select(cl=True)
    ##--------- create CurveSkinJoint ----------##

    startJointPosi = rig.xform(jointChainStartJoint ,worldSpace=True,query=True,translation=True)
    midJointPosi = rig.xform( jointChainList [midJointIndex-1],worldSpace=True,query=True,translation=True)
    endJointPosi = rig.xform(jointChainEndJoint ,worldSpace=True,query=True,translation=True)

    rootSkinJoint = preFixName + part + '_curve_root_SkinJoint' 
    midSkinJoint = preFixName + part + '_curve_mid_SkinJoint' 
    topSkinJoint = preFixName + part + '_curve_end_SkinJoint' 


    rig.joint( p=(startJointPosi[0],startJointPosi[1],startJointPosi[2]),n = rootSkinJoint,radius = neckRadius  )
    rig.joint( p=(midJointPosi [0],midJointPosi [1],midJointPosi [2]),n = midSkinJoint ,radius = neckRadius )
    rig.select(cl=True)
    rig.joint(p=endJointPosi ,n=topSkinJoint,radius=neckRadius )
    rig.select(cl=True)

    ##----------- skinBind the spIK's curve -----------##

    rig.select(rootSkinJoint ,topSkinJoint,add=True)
    rig.select(preFixName + 'curve_' +part,add=True)
    rig.skinCluster(toSelectedBones=True,
            maximumInfluences=2,
            dropoffRate=4,
            removeUnusedInfluence=True,
            n=preFixName + 'skinCluster_' +part)



    ## -------- parent the skinJoint to the right part -------------##
    rig.parent(rootSkinJoint , preFixName + 'top_waist_ikCtrl')
    rig.parent(topSkinJoint , headCtrl)




    ##----------- set ik advanced Twist Controls -----------##

   
    rig.setAttr(preFixName +'ikHandle_' +part + '.dTwistControlEnable' ,1)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpType', 4)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpAxis', 4)


    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVector', 1,0,0)
    rig.setAttr(preFixName +'ikHandle_' +part + '.dWorldUpVectorEnd', 1,0,0)
    rig.connectAttr(preFixName + 'top_waist_ikCtrl' +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrix')
    rig.connectAttr(headCtrl   +'.worldMatrix[0]' , preFixName +'ikHandle_' +part + '.dWorldUpMatrixEnd')




    ##------------ create stretchIK system and use expr -----------##

    rig.arclen( preFixName +'curve_'+part ,ch=True,n=part+'_curveLenInfo')
    curveInfo = rig.rename('curveInfo1',preFixName + part + '_curveLenInfo')

    curveOrigLen = rig.getAttr(curveInfo +'.arcLength')


    ##### expr string ######
    NumtransJoint = numOfJoint-1
    exprStr = '$newDis ='+ curveInfo +'.arcLength/(Character.scaleX*master_refer_GRP.scaleX)' + '-' + str(curveOrigLen) + ';\n'
    exprStr += '$scale ='+ curveInfo +'.arcLength/(Character.scaleX*master_refer_GRP.scaleX*' + str(curveOrigLen)  + ');\n'

    exprStr += '$trans = $newDis/' + str(NumtransJoint) + ';\n'


    for k in range(1,numOfJoint,1):
        origTx = rig.getAttr(jointChainList [k] + '.tx')        
        exprStr += jointChainList [k] +'.tx =' + str(origTx) + '+ $trans;\n'


    rig.expression(s =exprStr , n =part+'_expr')

    ##------ correct Curve double transform ------##
    rig.setAttr(preFixName +'curve_'+part+'.inheritsTransform',0)





    ##---------- create FKchain ----------##

    rootFKJoint = preFixName + part + 'root_FK'
    topFKJoint = preFixName + part + 'top_FK'

    rig.select(cl=True)
    neckRootFK = rig.joint( p=(startJointPosi[0],startJointPosi[1],startJointPosi[2]),n = rootFKJoint ,radius = neckRadius  )
    neckTopFK =rig.joint( p=(endJointPosi [0],endJointPosi [1],endJointPosi [2]),n = topFKJoint ,radius = neckRadius )

    rig.joint(rootFKJoint ,e=True,oj='yxz',secondaryAxisOrient='xup',ch=True,zso=True)
    
    rig.hide(neckRootFK)
    rig.parent(neckRootFK,'top_waist_ikCtrl')


    ##------- create rootSkinJoint ctrl ---------##
    rootCtrl = rig.group(n=preFixName + part + '_root_ctrl',empty=True)
    rig.setAttr(rootCtrl +'.scale',0.07*scalVal,0.07*scalVal,0.07*scalVal)
    SK_freezeObj(rootCtrl)
    rootCtrlGRP = rig.group(n=rootCtrl + '_GRP',empty=True)
    rig.parent(rootCtrl , rootCtrlGRP)

    rootCtrlGRPposiConst = rig.pointConstraint(neckRootFK , rootCtrlGRP , mo=False)
    rig.delete(rootCtrlGRPposiConst )
    rootCtrlorientConst = rig.orientConstraint(neckRootFK , rootCtrlGRP , mo=False)
    rig.delete(rootCtrlorientConst )

    rig.parentConstraint(rootCtrl,rootSkinJoint,mo=True)

    # hide rootCtrl Attr #
    for eachRoothideAttr in ('.sx','.sy','.sz'):
        rig.setAttr(rootCtrl + eachRoothideAttr ,lock=True,keyable=False,channelBox =False)


    #----------- create neck FK ctrl -------------#
    neckFKctrl = rig.rename(SK_b29(6), preFixName + part + '_FK_ctrl')
    rig.setAttr(neckFKctrl +'.scale',0.1*scalVal,0.1*scalVal,0.1*scalVal)
    SK_freezeObj(neckFKctrl)
    FKCtrlGRP = rig.group(n=neckFKctrl + '_GRP',empty=True)
    rig.parent(neckFKctrl ,FKCtrlGRP )

    FKGRPposiConst = rig.pointConstraint(neckRootFK , FKCtrlGRP , mo=False)
    rig.delete(FKGRPposiConst)
    FKGRPorientConst = rig.orientConstraint(neckRootFK , FKCtrlGRP , mo=False)
    rig.delete(FKGRPorientConst)


    rig.orientConstraint(neckFKctrl,neckRootFK,mo=True)
    rig.pointConstraint(neckFKctrl,rootCtrlGRP,mo=True)

    # hide FK Attr #
    for eachFKhideAttr in ('.sx','.sy','.sz','.visibility'):
        rig.setAttr(neckFKctrl + eachFKhideAttr ,lock=True,keyable=False,channelBox =False)


    ## create the  o sys ##

    rig.addAttr(headCtrl , longName = 'rotation' , attributeType = 'enum' , en = 'neck:body' , keyable = True)

    # create switch Loc
    headLoc = rig.spaceLocator(n=preFixName +'head_animGRP_Loc')

    Rneck = rig.spaceLocator(n=preFixName + part +'_R_neck_Loc')
    Rbody = rig.spaceLocator(n=preFixName + part +'_R_body Loc')


    for eachFollow in ('neck_','body_'):
        followLocPointConst = rig.pointConstraint(headCtrl  , preFixName + part + '_R_' + eachFollow + 'Loc', mo =False)
        rig.delete(followLocPointConst)

    headLocPointConst = rig.pointConstraint(headCtrl  , headLoc[0] , mo =False)
    rig.delete(headLocPointConst )

    rig.parent(headCtrlGRP , headLoc )


    # pointConst the head_animGRP_loc #
    rig.pointConstraint(neckTopFK , headLoc[0] , mo=False)

    Rconst = rig.orientConstraint(Rneck[0] , Rbody [0] ,headLoc[0],n=preFixName + part + 'Rconst')

    # connect the const switch #
    neckConstRe = rig.createNode('reverse',n=preFixName + 'neck_RV')
    rig.connectAttr(headCtrl+'.rotation' , neckConstRe+'.inputX')
    rig.connectAttr(neckConstRe+'.outputX' , Rconst[0]+'.'+Rneck[0] + 'W0')

    rig.connectAttr(headCtrl+'.rotation' , Rconst[0]+'.'+Rbody[0] + 'W1')




    # parent the T  in each different place

    rig.parent( Rneck [0],  preFixName + 'necktop_FK')
    rig.parent( Rbody [0] ,  preFixName + 'waist_Ctrl')



    ##------------- clean up the rig ------------##

    # hide things what we don't want to see  #
    rig.hide(preFixName + 'ikHandle_neck')
    rig.hide(rootSkinJoint)
    rig.hide(topSkinJoint) 
    rig.hide(preFixName +'curve_'+part)   

    # create the doNotTouch GRP #
    neckGRP = rig.group( empty = True , n= preFixName + part + '_GRP' ,  world = True )
    neckDoNotTouchGRP = rig.group( empty = True , n= preFixName + part + '_doNotTouch_GRP' ,  world = True )

    rig.parent(preFixName + 'ikHandle_neck' , neckDoNotTouchGRP )
    rig.parent(preFixName + 'neck1_jnt' , neckDoNotTouchGRP )
    rig.parent(preFixName + 'curve_neck' , neckDoNotTouchGRP ) 

    rig.parent(neckDoNotTouchGRP , neckGRP )
    rig.parent(headLoc[0] , neckGRP )
    
    rig.parent( FKCtrlGRP , neckGRP )
    rig.parent( rootCtrlGRP , preFixName + 'top_waist_ikCtrl')


    # hide the rubish
    rig.hide( Rneck[0] , Rbody[0] , headLoc[0]+'Shape')






