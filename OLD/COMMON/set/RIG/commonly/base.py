#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.nurbsCurveCon import *
import pickle
import math
from RIG.commonly.addFingerJoint import SK_createFingers 

		
def SK_combineJoint():
	# before refresh Temp #
	try:
		rig.select('waist1_jnt')
	except:
		#chest#
		rig.delete('chest3_jnt')
		rig.parent('neck1_refer','chest2_jnt')
	
		#head#
		rig.parent('head_end_jnt','neck2_refer')
		rig.parent('orient_jaw_drv','neck2_refer')
		rig.delete('head_jnt')
	
		#waist#
		rig.parent('chest2_jnt','waist2_refer')
		rig.delete('chest1_jnt')

		#arm#
		rig.parent('Lf_upArm_drv','Lf_clavicle1_jnt')
		rig.delete('Lf_clavicle2_jnt')
		rig.parent('Lf_clavicle1_jnt','chest2_jnt')

		#leg#
		rig.parent('Lf_hip_drv','waist1_refer')


	# after refresh Temp #
	try:
		rig.select('waist1_refer')
	except:
		#chest#
		rig.select('waist*_jnt')
		waistSel=rig.ls(sl=True)
		maxWaist = len(waistSel)
		rig.parent('chest2_jnt','waist'+str(maxWaist)+'_jnt')
		rig.delete('chest1_jnt')

		#chest#
		rig.delete('chest3_jnt')
		rig.parent('neck1_jnt','chest2_jnt')

		#head#
		rig.select('neck*_jnt')
		neckSel=rig.ls(sl=True)
		maxNeck = len(neckSel)
		rig.parent('head_end_jnt','neck'+str(maxNeck)+'_jnt')
		rig.parent('orient_jaw_drv','neck'+str(maxNeck)+'_jnt')
		rig.delete('head_jnt')

		#arm#
		rig.parent('Lf_upArm_drv','Lf_clavicle1_jnt')
		rig.delete('Lf_clavicle2_jnt')
		rig.parent('Lf_clavicle1_jnt','chest2_jnt')
		
		try:
			rig.parent('Rt_upArm_drv','Rt_clavicle1_jnt')
			rig.delete('Rt_clavicle2_jnt')
			rig.parent('Rt_clavicle1_jnt','chest2_jnt')
		except:
			pass		

		#leg#
		rig.parent('Lf_hip_drv','waist1_jnt')

		try:
			rig.parent('Rt_hip_drv','waist1_jnt')
		except:
			pass			


def SK_separateJoint():
	# before refresh Temp #
	try:
		rig.select('waist1_jnt')
	except:
		#chest#
		chest3 = rig.duplicate('neck1_refer' , n = 'chest3_jnt' , parentOnly=True)
		rig.parent('neck1_refer','Character')
	
		#head#
		head = rig.duplicate('neck2_refer' , n = 'head_jnt' , parentOnly=True)
		rig.parent(head,'Character')
		rig.parent('orient_jaw_drv',head)
		rig.parent('head_end_jnt',head)
	
		#waist#
		chest1 = rig.duplicate('waist2_refer' , n = 'chest1_jnt' , parentOnly=True)
		rig.parent(chest1 ,'Character')
		rig.parent('chest2_jnt','chest1_jnt')

		#arm#
		clavicle2 = rig.duplicate('Lf_upArm_drv' , n = 'Lf_clavicle2_jnt' , parentOnly=True)
		rig.parent('Lf_clavicle1_jnt','Character')
		rig.parent('Lf_upArm_drv','Character')

		#leg#
		rig.parent('Lf_hip_drv','Character')


	# after refresh Temp #
	try:
		rig.select('waist1_refer')
	except:
		#chest#
		chest3 = rig.duplicate('neck1_jnt' , n = 'chest3_jnt' , parentOnly=True)
		rig.parent('neck1_jnt','Character')

		#head#
		rig.select('neck*_jnt')
		neckSel=rig.ls(sl=True)
		maxNeck = len(neckSel)
		head = rig.duplicate('neck'+str(maxNeck)+'_jnt' , n = 'head_jnt' , parentOnly=True)
		rig.parent(head,'Character')
		rig.parent('orient_jaw_drv',head)
		rig.parent('head_end_jnt',head)

		#waist#
		rig.select('waist*_jnt')
		waistSel=rig.ls(sl=True)
		maxWaist = len(waistSel)
		chest1 = rig.duplicate('waist'+str(maxWaist)+'_jnt' , n = 'chest1_jnt' , parentOnly=True)
		rig.parent(chest1 ,'Character')
		rig.parent('chest2_jnt',chest1)

		#arm#
		LfClavicle2 = rig.duplicate('Lf_upArm_drv' , n = 'Lf_clavicle2_jnt' , parentOnly=True)
		rig.parent('Lf_clavicle1_jnt','Character')
		rig.parent('Lf_upArm_drv','Character')

		try:
			RtClavicle2 = rig.duplicate('Rt_upArm_drv' , n = 'Rt_clavicle2_jnt' , parentOnly=True)
			rig.parent('Rt_clavicle1_jnt','Character')
			rig.parent('Rt_upArm_drv','Character')	
		except:
			pass		

		#leg#
		rig.parent('Lf_hip_drv','Character')

		try:
			rig.parent('Rt_hip_drv','Character')
		except:
			pass

		##------------ if have the assemblage in the scene ------------##
		# clavicle #
		rig.select('Lf*_clavicle1_jnt')
		allArm=rig.ls(sl=True)
		allArm.remove('Lf_clavicle1_jnt')
		dupArm=allArm
		rig.select(cl=True)

		if dupArm==[]:
			pass
		else:
			for eachDup in dupArm:
				queryIndex = eachDup[2]

				#-- separate joint --#

				clavicle2 = rig.duplicate('Lf'+ queryIndex + '_upArm_drv' , n = 'Lf'+ queryIndex + '_clavicle2_jnt' , parentOnly=True)
				rig.parent('Lf'+ queryIndex + '_clavicle1_jnt','Character')
				rig.parent('Lf'+ queryIndex +'_upArm_drv','Character')

				clavicle2 = rig.duplicate('Rt'+ queryIndex + '_upArm_drv' , n = 'Rt'+ queryIndex + '_clavicle2_jnt' , parentOnly=True)
				rig.parent('Rt'+ queryIndex + '_clavicle1_jnt','Character')
				rig.parent('Rt'+ queryIndex +'_upArm_drv','Character')


		# leg #
		rig.select('Lf*_hip_drv')
		allLeg=rig.ls(sl=True)
		allLeg.remove('Lf_hip_drv')
		dupLeg=allLeg
		rig.select(cl=True)

		if dupLeg==[]:
			pass
		else:
			for eachDup in dupLeg:
				queryIndex = eachDup[2]

				#-- separate joint --#

				rig.parent('Lf'+ queryIndex +'_hip_drv','Character')

				rig.parent('Rt'+ queryIndex +'_hip_drv','Character')


def SK_TempSplitSelJoint(startJoint = 'waist1_refer',segments = 4):

    ##----------- freeze the startJoint ---------##
    rig.makeIdentity(startJoint, apply=True,t=1,r=1,s=1,n=0)
    rig.joint(startJoint ,e=True, oj='xyz', secondaryAxisOrient= 'yup', ch=True, zso=True)
    startJointRadius = rig.getAttr(startJoint +'.radius') 

    ##----------- get the length of the jointChain ----------##
    rig.select(startJoint)
    endPW = rig.pickWalk(d='down')
    endJoint = endPW [0]

    chainLength = rig.getAttr(endJoint +'.tx')

    eachSegDis = chainLength /segments 

    ##----------- create the new chain -----------##
    rig.delete(endJoint )
    insertStartJoint = startJoint
    for i in range(1,segments+1,1): 
        newJoint = rig.insertJoint(insertStartJoint)
        newJoint = rig.rename( newJoint ,startJoint+'_seg_'+ str(i) )
        rig.setAttr(newJoint +'.tx',eachSegDis )
        rig.setAttr(newJoint +'.radius',startJointRadius  )

        insertStartJoint  = newJoint 


def SK_refreshTemp():

    SK_separateJoint()

    ## deal with the global ctrl ##
    getScale = rig.getAttr('Character' + '.scaleY')
    AllJointList = rig.listRelatives('Character' , allDescendents=True , shapes=False)

    for eachTempJoint in (AllJointList):
        if 'Shape' in eachTempJoint :
            pass
        else:
            oldRadius = rig.getAttr(eachTempJoint + '.radius')
            rig.setAttr(eachTempJoint + '.radius' , oldRadius * getScale )

    rig.makeIdentity('Character' , apply = True ,t= False,r =False,s =True)
##--------------------------------------------------------------------------------------------##
    ## rebulid the basic joint,because want to refresh joint temp for many times ##
    try:
        rig.select('waist1_refer')
    except:
        ## rebuild waist ##
        waistRadius = rig.getAttr('waist1_jnt.radius')
        rig.select('waist1_jnt',hierarchy=True)
        waistChainList = rig.ls(sl=True)
        numOfWaistJoint = len(waistChainList)
        waistChainEndJoint = waistChainList[numOfWaistJoint -1]
    
        waistStartJntPosi = rig.xform('waist1_jnt',q=True,ws=True,rp=True)
        waistEndJntPosi = rig.xform(waistChainEndJoint,q=True,ws=True,rp=True)

        rig.select(cl=True)
        rig.joint( p=(waistStartJntPosi[0],waistStartJntPosi[1],waistStartJntPosi[2]),n ='waist1_refer',radius=waistRadius)
        rig.joint( p=(waistEndJntPosi[0],waistEndJntPosi[1],waistEndJntPosi[2]),n = 'waist2_refer',radius=waistRadius)
        rig.makeIdentity( 'waist1_refer', apply=True,t=1,r=1,s=1,n=0)
        rig.joint('waist1_refer' , e=True, zso=True, oj= 'xyz', sao= 'zdown' )
        rig.select(cl=True)

        rig.delete('waist1_jnt')
        rig.parent('waist1_refer','Character')

        ## rebuild neck ##
        neckRadius = rig.getAttr('neck1_jnt.radius')
        rig.select('neck1_jnt',hierarchy=True)
        neckChainList = rig.ls(sl=True)
        numOfNeckJoint = len(neckChainList)
        neckChainEndJoint = neckChainList[numOfNeckJoint -1]
    
        neckStartJntPosi = rig.xform('neck1_jnt',q=True,ws=True,rp=True)
        neckEndJntPosi = rig.xform(neckChainEndJoint,q=True,ws=True,rp=True)

        rig.select(cl=True)
        rig.joint( p=(neckStartJntPosi[0],neckStartJntPosi[1],neckStartJntPosi[2]),n ='neck1_refer',radius=neckRadius)
        rig.joint( p=(neckEndJntPosi[0],neckEndJntPosi[1],neckEndJntPosi[2]),n = 'neck2_refer',radius=neckRadius)
        rig.makeIdentity( 'neck1_refer', apply=True,t=1,r=1,s=1,n=0)
        rig.joint('neck1_refer' , e=True, zso=True, oj= 'xyz', sao= 'zdown' )
        rig.select(cl=True)

        rig.delete('neck1_jnt')
        rig.parent('neck1_refer','Character')




    ##--------------------------------------------------------------------------------------------##
    

    ########################### split each part of body ####################################

    ##------------- Split neck ------------##
    neckSegs = rig.intSliderGrp('neckSegsField' , q=True , value = True )

    SK_TempSplitSelJoint(startJoint = 'neck1_refer',segments = neckSegs )

    ##------------- Split torso ------------##
    waistSegs = rig.intSliderGrp('waistSegsField' , q=True , value = True )

    SK_TempSplitSelJoint(startJoint = 'waist1_refer',segments = waistSegs )



    ########################### rename each split torso jointChain #################################### 

    rig.rename( 'waist1_refer','waist1_jnt')    
    rig.select( 'waist1_jnt')
    waistList = rig.ls(sl=True)
    firstWaist = waistList [0]
    for numWaist in range(2,waistSegs+2,1):
        oldNextJoint = rig.pickWalk(firstWaist ,d='down')
        newNextJoint = rig.rename(oldNextJoint ,'waist' + str(numWaist) + '_jnt' )
        firstWaist = newNextJoint

    ########################### rename each split neck jointChain #################################### 

    rig.rename('neck1_refer','neck1_jnt')    
    rig.select( 'neck1_jnt')
    neckList = rig.ls(sl=True)
    firstNeck = neckList [0]
    for numNeck in range(2,neckSegs +2,1):
        oldNextJoint = rig.pickWalk(firstNeck ,d='down')
        newNextJoint = rig.rename(oldNextJoint ,'neck' + str(numNeck) + '_jnt' )
        firstNeck = newNextJoint            

    
    ##--------------------------------------------------------------------------------------------##

    ################ choose how many fingers or toes we want ###################### 
    
    fingerNums = rig.intSliderGrp('fingerNumsField', q=True , value=True )
#    if fingerNums == 4:
#        try:
#            rig.delete('Lf_pinkyRoot_jnt')
#        except:
#            pass
#    elif fingerNums == 3:
#        try:
#            rig.delete('Lf_pinkyRoot_jnt' , 'Lf_ringRoot_jnt')
#        except:
#            pass
#    elif fingerNums == 2:
#        try:
#            rig.delete('Lf_pinkyRoot_jnt' , 'Lf_ringRoot_jnt' , 'Lf_midRoot_jnt')
#        except:
#            pass
#    elif fingerNums == 1:
#        try:
#            rig.delete('Lf_pinkyRoot_jnt' , 'Lf_ringRoot_jnt' , 'Lf_midRoot_jnt' , 'Lf_indexRoot_jnt')
#        except:
#            pass
#    elif fingerNums == 0:
#        try:
#            rig.delete('Lf_pinkyRoot_jnt' , 'Lf_ringRoot_jnt' , 'Lf_midRoot_jnt' , 'Lf_indexRoot_jnt' , 'Lf_thumb1_jnt')
#        except:
#            pass
#    else:
#        pass
    

    ToeNums = rig.intSliderGrp('toesNumsField', q=True , value=True )
#    if ToeNums == 4:
#        try:    
#            rig.delete('Lf_Toe_pinkyRoot_jnt')
#        except:
#            pass
#    elif ToeNums == 3:
#        try:
#            rig.delete('Lf_Toe_pinkyRoot_jnt' , 'Lf_Toe_ringRoot_jnt')
#        except:
#            pass
#    elif ToeNums == 2:
#        try:
#            rig.delete('Lf_Toe_pinkyRoot_jnt' , 'Lf_Toe_ringRoot_jnt' , 'Lf_Toe_midRoot_jnt')
#        except:
#            pass
#    elif ToeNums == 1:
#        try:
#            rig.delete('Lf_Toe_pinkyRoot_jnt' , 'Lf_Toe_ringRoot_jnt' , 'Lf_Toe_midRoot_jnt' , 'Lf_Toe_indexRoot_jnt')
#        except:
#            pass
#    elif ToeNums == 0:
#        try:
#            rig.delete('Lf_Toe_pinkyRoot_jnt' , 'Lf_Toe_ringRoot_jnt' , 'Lf_Toe_midRoot_jnt' , 'Lf_Toe_indexRoot_jnt' , 'Lf_Toe_thumb1_jnt')
#        except:
#            pass
#    else:
#        pass

    SK_createFingers(fingerNums,ToeNums)
    SK_combineJoint()

    
def SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = 'torso1_IK_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0)):
    rig.select(cl=True)
    rig.select(startJoint,hierarchy=True) 
    jointList = rig.ls(sl=True)
    numOfJoint = len(jointList)
    midJointIndex = numOfJoint//2
    
    ##-----     unParent the joint -------##
    for i in range(1,numOfJoint,1):
        rig.select(jointList[i])
        rig.parent(w=True)
    
    ##------ create the locator for upvector in the AimConstrain ------##
    rig.spaceLocator(name = 'AimLoc')
    rig.select(jointList[midJointIndex])
    rig.select('AimLoc',add=True)
    rig.pointConstraint(offset = (0 ,0 ,0) , weight = 1 ,n = 'pointConstraint_upLoc') 
    rig.delete('pointConstraint_upLoc')
    
    ##------ move the locator to get the upDirection ------##
    rig.setAttr('AimLoc.'+ AimLocMove ,20)

    ##------ AimConstraint the joint -------##
    for j in range(1,numOfJoint,1):
        rig.select(jointList[j])
        rig.select(jointList[j-1],add=True)
        rig.aimConstraint(mo=False, offset=(0,0,0), weight =1, aimVector=JointAimVector, upVector=JointUpVector, worldUpType= 'object', worldUpObject ='AimLoc', name ='Jnt'+ str(j) + '_'+'aimConstraint' ) 
        rig.select(jointList [j])
        rig.delete(cn=True)
    
        ##------ connect JointChain ------##
        rig.parent(jointList[j],jointList[j-1])

    ##------ freeze Transformations to the rootJnt ------##     
    rig.makeIdentity(startJoint, apply=True,t=1,r=1,s=1,n=0)

    ##------- Orient the endJnt --------##
    rig.select(jointList[numOfJoint-1]) 
    rig.joint(e=True,oj='none',secondaryAxisOrient='yup',ch=True,zso=True)

    ##------ delete the 'AimLoc' -------##
    rig.delete('AimLoc')
    rig.select(cl=True)

##--------------------------------------------------------------------------------##


def SK_FingerOrientJoint(startJoint = 'torso1_IK_jnt',endJoint = 'torso4_IK_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0)):
    rig.select(cl=True)
    rig.select(startJoint,hierarchy=True) 
    jointList = rig.ls(sl=True)
    numOfJoint = len(jointList)
        
    ##-----     unParent the joint -------##
    for i in range(1,numOfJoint,1):
        rig.select(jointList[i])
        rig.parent(w=True)
    
    ##------ create the locator for upvector in the AimConstrain ------##
    rig.spaceLocator(name = 'AimLoc')
    rig.select(startJoint ,endJoint ,add=True)
    rig.select('AimLoc',add=True)
    rig.pointConstraint(offset = (0 ,0 ,0) , weight = 1 ,n = 'pointConstraint_upLoc') 
    rig.delete('pointConstraint_upLoc')
    

    ##------ AimConstraint the joint -------##
    for j in range(1,numOfJoint,1):
        rig.select(jointList[j])
        rig.select(jointList[j-1],add=True)
        rig.aimConstraint(mo=False, offset=(0,0,0), weight =1, aimVector=JointAimVector, upVector=JointUpVector, worldUpType= 'object', worldUpObject ='AimLoc', name ='Jnt'+ str(j) + '_'+'aimConstraint' ) 
        rig.select(jointList [j])
        rig.delete(cn=True)
    
        ##------ connect JointChain ------##
        rig.parent(jointList[j],jointList[j-1])

    ##------ freeze Transformations to the rootJnt ------##     
    rig.makeIdentity(startJoint, apply=True,t=1,r=1,s=1,n=0)

    ##------- Orient the endJnt --------##
    ##  here! we don't orient the end Joint ,because the end JointOrient in the Temp must be controled by us !!
    ##  rig.select(jointList[numOfJoint-1]) 
    ##  rig.joint(e=True,oj='none',secondaryAxisOrient='yup',ch=True,zso=True)

    ##------ delete the 'AimLoc' -------##
    rig.delete('AimLoc')
    rig.select(cl=True)


#######################################
##
## orient and mirror the joint Temp
##
#######################################


def orientAndMirrorJoint ():


    SK_separateJoint()
    
    ## deal with the global ctrl ##
    getScale = rig.getAttr('Character' + '.scaleY')
    AllJointList = rig.listRelatives('Character' , allDescendents=True , shapes=False)

    for eachTempJoint in (AllJointList):
        if 'Shape' in eachTempJoint :
            pass
        else:
            oldRadius = rig.getAttr(eachTempJoint + '.radius')
            rig.setAttr(eachTempJoint + '.radius' , oldRadius * getScale )

    rig.makeIdentity('Character' , apply = True ,t= False ,r =False ,s =True)    



    ## -------------------------- unparent the joint ------------------------------##

    # unparent hand
    rig.parent('Lf_hand_drv' , world = True)

    # unparent foot
    rig.parent('Lf_foot_drv' , world = True)

    # unparent heel
    rig.parent('Lf_heel_drv' , world = True)

    # unparent fingers
    for eachFinger in ('thumb','index','mid','ring','pinky'):
        if eachFinger == 'thumb':
            try:
                rig.parent('Lf_' + eachFinger + '1_jnt' , world = True)
            except:
                pass
        else:
            try:
                rig.parent('Lf_' + eachFinger + 'Root_jnt' , world = True)
            except:
                pass

    # unparent toes
    for eachToe in ('Toe_thumb','Toe_index','Toe_mid','Toe_ring','Toe_pinky'):
        if eachToe == 'Toe_thumb':
            try:
                rig.parent('Lf_' + eachToe + '1_jnt' , world = True)
            except:
                pass
        else:
            try:
                rig.parent('Lf_' + eachToe + 'Root_jnt' , world=True)
            except:
                pass


    ## -------------------------- orient the joint ------------------------------##

    #---- orient upArm 2 wrist ----#
    SK_FingerOrientJoint(startJoint = 'Lf_upArm_drv' , endJoint = 'Lf_wrist_drv',JointAimVector= (1,0,0),JointUpVector = (0,0,1))
    

    #---- orient finger's root ----#
    ## freeze the root ##
    for eachFingerRoot in ('indexRoot','midRoot','ringRoot','pinkyRoot'):
        try:
            rig.makeIdentity('Lf_'+eachFingerRoot+'_jnt' , apply = True ,t= False,r =True,s =False)
        except:
            pass
            
    ## unparent eachFinger ##
    for eachFinger in ('index','mid','ring','pinky'):
        try:
            rig.parent('Lf_'+eachFinger+'1_jnt',world=True)
        except:
            pass

    ## orient fingers ##
    try:
        SK_FingerOrientJoint(startJoint = 'Lf_thumb1_jnt' , endJoint = 'Lf_thumb3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_index1_jnt' , endJoint = 'Lf_index3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_mid1_jnt' , endJoint = 'Lf_mid3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_ring1_jnt' , endJoint = 'Lf_ring3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_pinky1_jnt' , endJoint = 'Lf_pinky3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    except:
        pass

    ## parnet fingers to the root ##
    for eachFinger in ('index','mid','ring','pinky'):
        try:
            rig.parent('Lf_'+eachFinger+'1_jnt','Lf_'+eachFinger+'Root_jnt')
        except:
            pass


    #---- orient leg 2 ankle ----#
    SK_FingerOrientJoint(startJoint = 'Lf_leg_drv' , endJoint = 'Lf_ankle_drv',JointAimVector= (1,0,0),JointUpVector = (0,0,-1))
    #rig.joint('Lf_ankle_drv' , e=True,oj='none',secondaryAxisOrient='yup',ch=True,zso=True)
    rig.setAttr('Lf_ankle_drv.jointOrientX',0)
    rig.setAttr('Lf_ankle_drv.jointOrientY',0)
    rig.setAttr('Lf_ankle_drv.jointOrientZ',0)
    ## orient toe's root ##
    ## freeze the root ##
    for eachToeRoot in ('Toe_indexRoot','Toe_midRoot','Toe_ringRoot','Toe_pinkyRoot'):
        try:
            rig.makeIdentity('Lf_'+eachToeRoot+'_jnt' , apply = True ,t= False,r =True,s =False)
        except:
            pass
            
    ## unparent eachToe ##
    for eachToe in ('Toe_index','Toe_mid','Toe_ring','Toe_pinky'):
        try:
            rig.parent('Lf_'+eachToe+'1_jnt',world=True)
        except:
            pass

    ## orient toes ##
    try:
        SK_FingerOrientJoint(startJoint = 'Lf_Toe_thumb1_jnt' , endJoint = 'Lf_Toe_thumb3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_Toe_index1_jnt' , endJoint = 'Lf_Toe_index3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_Toe_mid1_jnt' , endJoint = 'Lf_Toe_mid3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_Toe_ring1_jnt' , endJoint = 'Lf_Toe_ring3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
        SK_FingerOrientJoint(startJoint = 'Lf_Toe_pinky1_jnt' , endJoint = 'Lf_Toe_pinky3_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    except:
        pass

    ## parnet toes to the root ##
    for eachToe in ('Toe_index','Toe_mid','Toe_ring','Toe_pinky'):
        try:
            rig.parent('Lf_'+eachToe+'1_jnt','Lf_'+eachToe+'Root_jnt')
        except:
            pass

    #---- free foot ----#
    rig.makeIdentity('Lf_foot_drv', apply=True,t=1,r=1,s=1,n=0)

    #---- orient waist ----#
    SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = 'waist1_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    #---- orient neck ----#
    SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = 'neck1_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    #---- orient chest ----#
    SK_SpikOrientJoin(AimLocMove = 'tz',startJoint = 'chest1_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

    #---- free clavicle ----#
    SK_FingerOrientJoint(startJoint = 'Lf_clavicle1_jnt',endJoint = 'Lf_clavicle2_jnt',JointAimVector= (1,0,0),JointUpVector = (0,1,0))

    ##rig.makeIdentity('Lf_clavicle1_jnt', apply=True,t=1,r=1,s=1,n=0)

    #---- free jaw ----#
    rig.makeIdentity('upper_jaw_jnt', apply=True,t=1,r=1,s=1,n=0)    
    rig.makeIdentity('lower_jaw_jnt', apply=True,t=1,r=1,s=1,n=0)    

    ## -------------------------- parent the joint ------------------------------##

    # parent hand
    rig.parent('Lf_hand_drv' , 'Lf_wrist_drv')
    
    #---- orient wrist 2 hand ----#
    SK_FingerOrientJoint(startJoint = 'Lf_wrist_drv',endJoint = 'Lf_hand_drv',JointAimVector= (1,0,0),JointUpVector = (0,1,0))
    
    #---- orient hand 2 handEnd ----#
    SK_FingerOrientJoint(startJoint = 'Lf_hand_drv',endJoint = 'Lf_handEnd_drv',JointAimVector= (1,0,0),JointUpVector = (0,1,0))

    # parent foot
    rig.parent('Lf_foot_drv' , 'Lf_ankle_drv')

    # parent heel
    rig.parent('Lf_heel_drv' , 'Lf_ankle_drv')

    # parent fingers
    for eachFinger in ('thumb','index','mid','ring','pinky'):
        if eachFinger == 'thumb':
            try:
                rig.parent('Lf_'+eachFinger+'1_jnt','Lf_wrist_drv')
            except:
                pass
        else:        
            try:
                rig.parent('Lf_' + eachFinger + 'Root_jnt' , 'Lf_wrist_drv')
            except:
                pass

    # parent toes
    for eachToe in ('Toe_thumb','Toe_index','Toe_mid','Toe_ring','Toe_pinky'):
        if eachToe == 'Toe_thumb':
            try:
                rig.parent('Lf_'+eachToe+'1_jnt','Lf_foot_drv')
            except:
                pass
        else:        
            try:
                rig.parent('Lf_' + eachToe+ 'Root_jnt' , 'Lf_foot_drv')
            except:
                pass


    SK_combineJoint()


    ## -------------------------- mirror the joint ------------------------------##

    try:
        rig.delete('Rt_clavicle1_jnt','Rt_hip_drv')    
    except:
        pass

    rig.mirrorJoint('Lf_clavicle1_jnt' , mirrorYZ = True ,  mirrorBehavior = True ,  searchReplace = ('Lf', 'Rt'))

    rig.mirrorJoint('Lf_hip_drv' , mirrorYZ = True ,  mirrorBehavior = True ,  searchReplace = ('Lf', 'Rt'))


    rig.select(cl = True)
    
    ## --------------if the master have translate and rotate value,we must get that to be 0 ---------------##
    rig.parent('waist1_jnt',world=True)
    for eachTRattr in ('X','Y','Z'):
        rig.setAttr('Character.translate'+eachTRattr,0)
        rig.setAttr('Character.rotate'+eachTRattr,0)
        
    rig.parent('waist1_jnt','Character')








######################################################################################################################################################


def SK_duplicateJnt ():

    DupIndex = rig.intField('numOfduplicate' , q=True , value=1 )

    ## select what you want to duplicate ##
    SelObj = rig.ls(sl=True)

    SelObjList = rig.listRelatives(SelObj[0] ,allDescendents=True,shapes=False)
    numOfObjList = len(SelObjList)


    for eachDupIndex in range(DupIndex):
        rootObjCut = SelObj[0][2:]
        newRootObj = 'Lf' + str(eachDupIndex+1) + rootObjCut 

        sysDup = rig.duplicate(SelObj,n=newRootObj ,renameChildren=True)
        rig.move(-1 * (eachDupIndex+1), sysDup [0] , z=True , relative=True , worldSpace = True)
        dup = rig.listRelatives(sysDup[0] ,allDescendents=True,shapes=False)
    
        dupList = []
        for eachObjIndex in range(numOfObjList):
            eachObj = SelObjList[eachObjIndex]
            eachObjCut = eachObj[2:]
            newObj = 'Lf' + str(eachDupIndex+1) +  eachObjCut
            dupList.append (newObj)
        

    
        for eachDupList in range(numOfObjList):
            rig.rename(dup[eachDupList] , dupList[eachDupList])


def SK_mirrorDupJoint ():

	#------------------------------------------------------- arm ------------------------------------------------------------------#

	rig.select('Lf*_clavicle1_jnt')
	allArm=rig.ls(sl=True)
	allArm.remove('Lf_clavicle1_jnt')
	dupArm=allArm
	rig.select(cl=True)

	if dupArm==[]:
		pass
	else:
		for eachDup in dupArm:
			queryIndex = eachDup[2]

			#-- separate joint --#

			clavicle2 = rig.duplicate('Lf'+ queryIndex + '_upArm_drv' , n = 'Lf'+ queryIndex + '_clavicle2_jnt' , parentOnly=True)
			rig.parent('Lf'+ queryIndex + '_clavicle1_jnt','Character')
			rig.parent('Lf'+ queryIndex +'_upArm_drv','Character')

	
			##-- unparent the joint --##

			try:
				# unparent hand
				rig.parent('Lf'+ queryIndex + '_hand_drv' , world = True)
			except:
				pass


	   
			# unparent fingerRoot
			for eachFingerRoot in ('indexRoot','midRoot','ringRoot','pinkyRoot'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachFingerRoot + '_jnt' , world = True)
				except:
					pass	   


			# unparent fingers
			for eachFinger in ('thumb1','index1','mid1','ring1','pinky1'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachFinger + '_jnt' , world = True)
				except:
					pass


			## ----------- orient the joint ---------------##
			try:
				#---- orient upArm 2 wrist ----#
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_upArm_drv' , endJoint = 'Lf' + queryIndex + '_wrist_drv',
						JointAimVector= (1,0,0),JointUpVector = (0,0,1))
			except:
				pass
			#---- orient fingers ----#
			try:
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_thumb1_jnt' , endJoint = 'Lf' + queryIndex + '_thumb4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_index1_jnt' , endJoint = 'Lf' + queryIndex + '_index4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_mid1_jnt' , endJoint = 'Lf' + queryIndex + '_mid4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_ring1_jnt' , endJoint = 'Lf' + queryIndex + '_ring4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_pinky1_jnt' , endJoint = 'Lf' + queryIndex + '_pinky4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

			except:
				pass


			#---- freeze clavicle ----#
			try:	
				rig.makeIdentity('Lf' + queryIndex + '_clavicle1_jnt', apply=True,t=1,r=1,s=1,n=0)
			except:
				pass


			## ------------ parent the joint ---------------##

			# parent hand
			try:
				rig.parent('Lf' + queryIndex + '_hand_drv' , 'Lf' + queryIndex + '_wrist_drv')
			except:
				pass

			# parent fingerRoot
			for eachFingerRoot in ('indexRoot','midRoot','ringRoot','pinkyRoot'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachFingerRoot + '_jnt' , 'Lf' + queryIndex + '_wrist_drv')
				except:
					pass

			# parent fingers
			for eachFinger in ('thumb1','index1','mid1','ring1','pinky1'):
				if eachFinger == 'thumb1':
					try:
						rig.parent('Lf' + queryIndex + '_' + eachFinger + '_jnt' , 'Lf' + queryIndex + '_wrist_drv')
					except:
						pass
				else:
					try:
						rig.parent('Lf' + queryIndex + '_' + eachFinger + '_jnt' , 'Lf' + queryIndex + '_' + eachFinger[:-1] + 'Root_jnt')
					except:
						pass



			## -------------------------- mirror the joint ------------------------------##

			try:
				rig.delete('Rt' + queryIndex + '_clavicle1_jnt','Rt' + queryIndex + '_upArm_drv')	
			except:
				pass

			try:
				rig.mirrorJoint('Lf' + queryIndex + '_clavicle1_jnt' , mirrorYZ = True ,  mirrorBehavior = True ,  searchReplace = ('Lf', 'Rt'))
			except:
				pass

			try:
				rig.mirrorJoint('Lf' + queryIndex + '_upArm_drv' , mirrorYZ = True ,  mirrorBehavior = True ,  searchReplace = ('Lf', 'Rt'))
			except:
				pass


			#-- combine joint --#

			#arm#
			rig.parent('Lf'+ queryIndex +'_upArm_drv','Lf'+ queryIndex +'_clavicle1_jnt')
			rig.delete('Lf'+ queryIndex +'_clavicle2_jnt')
			rig.parent('Lf'+ queryIndex +'_clavicle1_jnt','chest2_jnt')
		
			try:
				rig.parent('Rt'+ queryIndex +'_upArm_drv','Rt'+ queryIndex +'_clavicle1_jnt')
				rig.delete('Rt'+ queryIndex +'_clavicle2_jnt')
				rig.parent('Rt'+ queryIndex +'_clavicle1_jnt','chest2_jnt')
			except:
				pass


	#------------------------------------------------------- leg ------------------------------------------------------------------#

	rig.select('Lf*_hip_drv')
	allLeg=rig.ls(sl=True)
	allLeg.remove('Lf_hip_drv')
	dupLeg=allLeg
	rig.select(cl=True)

	if dupLeg==[]:
		pass
	else:
		for eachDup in dupLeg:
			queryIndex = eachDup[2]

			#-- separate joint --#

			rig.parent('Lf'+ queryIndex +'_hip_drv','Character')
		
		
			##-------- unparent the joint --------##

			try:
				# unparent foot
				rig.parent('Lf'+ queryIndex + '_foot_drv' , world = True)
			except:
				pass

			try:		
				# unparent heel
				rig.parent('Lf'+ queryIndex + '_heel_drv' , world = True)
			except:
				pass

	   
			# unparent toeRoot
			for eachToeRoot in ('Toe_indexRoot','Toe_midRoot','Toe_ringRoot','Toe_pinkyRoot'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachToeRoot + '_jnt' , world = True)
				except:
					pass	   

			# unparent toes
			for eachToe in ('Toe_thumb1','Toe_index1','Toe_mid1','Toe_ring1','Toe_pinky1'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachToe + '_jnt' , world = True)
				except:
					pass

		

			##------------------ orient the joint -----------------##
			#---- orient leg 2 ankle ----#
			try:
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_leg_drv' , endJoint = 'Lf' + queryIndex + '_ankle_drv',
							JointAimVector= (1,0,0),JointUpVector = (0,0,-1))
				rig.joint('Lf' + queryIndex + '_ankle_drv' , e=True,oj='none',secondaryAxisOrient='yup',ch=True,zso=True)
			except:
				pass

			#---- orient toes ----#
			try:
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_Toe_thumb1_jnt' , endJoint = 'Lf' + queryIndex + '_Toe_thumb4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_Toe_index1_jnt' , endJoint = 'Lf' + queryIndex + '_Toe_index4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_Toe_mid1_jnt' , endJoint = 'Lf' + queryIndex + '_Toe_mid4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_Toe_ring1_jnt' , endJoint = 'Lf' + queryIndex + '_Toe_ring4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))
				SK_FingerOrientJoint(startJoint = 'Lf' + queryIndex + '_Toe_pinky1_jnt' , endJoint = 'Lf' + queryIndex + '_Toe_pinky4_jnt',JointAimVector= (1,0,0),JointUpVector = (0,-1,0))

			except:
				pass


			#---- freeze fingerRoot ----#
			for eachFingerRoot in ('indexRoot','midRoot','ringRoot','pinkyRoot'):
				try:
					rig.makeIdentity('Lf' + queryIndex + '_' + eachFingerRoot + '_jnt', apply=True,t=1,r=1,s=1,n=0)
				except:
					pass


			#---- freeze foot ----#
			try:
				rig.makeIdentity('Lf' + queryIndex + '_foot_drv', apply=True,t=1,r=1,s=1,n=0)
			except:
				pass


			#---- freeze toeRoot ----#
			for eachToeRoot in ('Toe_indexRoot','Toe_midRoot','Toe_ringRoot','Toe_pinkyRoot'):
				try:
					rig.makeIdentity('Lf' + queryIndex + '_' + eachToeRoot + '_jnt', apply=True,t=1,r=1,s=1,n=0)
				except:
					pass




			##--------------------- parent the joint ----------------------##
	
			try:
				# parent foot
				rig.parent('Lf' + queryIndex + '_foot_drv' , 'Lf' + queryIndex + '_ankle_drv')

				# parent heel
				rig.parent('Lf' + queryIndex + '_heel_drv' , 'Lf' + queryIndex + '_ankle_drv')
			except:
				pass


			# parent toeRoot
			for eachToeRoot in ('Toe_indexRoot','Toe_midRoot','Toe_ringRoot','Toe_pinkyRoot'):
				try:
					rig.parent('Lf' + queryIndex + '_' + eachToeRoot + '_jnt','Lf' + queryIndex + '_foot_drv')
				except:
					pass


			# parent toes
			for eachToe in ('Toe_thumb1','Toe_index1','Toe_mid1','Toe_ring1','Toe_pinky1'):
				if eachToe == 'Toe_thumb1':
					try:
						rig.parent('Lf' + queryIndex + '_' + eachToe + '_jnt' , 'Lf' + queryIndex + '_foot_drv')
					except:
						pass
				else:	
					try:
						rig.parent('Lf' + queryIndex + '_' + eachToe + '_jnt' , 'Lf' + queryIndex + '_' + eachToe[:-1] + 'Root_jnt')
					except:
						pass


			## -------------------------- mirror the joint ------------------------------##

			try:
				rig.delete('Rt' + queryIndex + '_hip_drv')	
			except:
				pass

			try:
				rig.mirrorJoint('Lf' + queryIndex + '_hip_drv' , mirrorYZ = True ,  mirrorBehavior = True ,  searchReplace = ('Lf', 'Rt'))
			except:
				pass


			#-- combine joint --#

			rig.parent('Lf'+ queryIndex + '_hip_drv','waist1_jnt')

			try:
				rig.parent('Rt'+ queryIndex +'_hip_drv','waist1_jnt')
			except:
				pass	


def SK_duplicateJoint(joints = [],suffix = ''):
    rig.select(cl = True)
    returnJoints = []
    for i,jnt in enumerate(joints):
        copyJnt = rig.duplicate(jnt,parentOnly = True,n = jnt+suffix)[0]
        if not (0 == i):
            rig.parent(copyJnt,returnJoints[-1])
        returnJoints.append(copyJnt)
    rig.select(cl = True)
    return returnJoints
    

def SK_hideLockAll(obj,Tr = True,Ro = True,Sc = True,removeAttr = []):
    attrs = rig.listAttr(obj,k = True)  
    transAttr = [u'translateX', u'translateY', u'translateZ']
    scaleAttr = [u'scaleX', u'scaleY', u'scaleZ']
    rotateAttr = [u'rotateX', u'rotateY', u'rotateZ']
    
    if not (Tr):
        for AttrName in transAttr:
           if(AttrName in attrs): 
               attrs.remove(AttrName)

    if not (Ro):
        for AttrName in rotateAttr:
           if(AttrName in attrs):
               attrs.remove(AttrName)
               
    if not (Sc):
        for AttrName in scaleAttr:
           if(AttrName in attrs):
               attrs.remove(AttrName)               
    if attrs:
        if not removeAttr:
	        for attr in attrs:
	            rig.setAttr(obj+'.'+attr,cb = False,k = False,l = True)
	        if(rig.attributeQuery('radius',node = obj,ex = True)):
	            rig.setAttr(obj+'.radius',cb = False,k = False,l = True)    
        	
        else:
	        for attr in attrs:
	        	if (not (attr in removeAttr)) and (not ('.' in attr)):	        	
		            rig.setAttr(obj+'.'+attr,cb = False,k = False,l = True)
	        if(rig.attributeQuery('radius',node = obj,ex = True)):
	            rig.setAttr(obj+'.radius',cb = False,k = False,l = True)  


def SK_showLockAll(obj):
     attrs = rig.listAttr(obj,l = True)
     for attr in attrs:
     	rig.setAttr(obj+'.'+attr,k = True,l = False)
	            
	                
def SK_averagePos(num,startPos,endPos,CreateCurve = False):
    pos = []
    if(len(startPos) == 3 and len(endPos) == 3):
        tempCurve = rig.curve(d = 1,p =[(startPos[0],startPos[1],startPos[2]),(endPos[0],endPos[1],endPos[2])],k = [0,1])
        addNum = 1.0/num

        tempNum = addNum
        for i in range(num+1):
            if(0 == i):
                pos.append(startPos)
            elif(num == i):
                pos.append(endPos)
            else:
               posPoint = rig.pointOnCurve(tempCurve,pr = tempNum,p = True)
               pos.append(posPoint)
               tempNum +=  addNum
    rig.delete(tempCurve)
    if CreateCurve:
        midPos = []
        midPos.append((startPos[0] + endPos[0])/2)
        midPos.append((startPos[1] + endPos[1])/2)
        midPos.append((startPos[2] + endPos[2])/2)
        rig.curve(n = 'split_Curve_CreateOjb',d = 2,p =[(startPos[0],startPos[1],startPos[2]),(midPos[0],midPos[1],midPos[2]),(endPos[0],endPos[1],endPos[2])],k = [0,0,1,1])
        rig.select(cl = True)

        
        
    return pos     
            

def SK_splitJoint(name,num,startJoint,endJoint,Curve = False):
    createJoint = []
    startPos = rig.xform(startJoint,q = True,ws = True,rp = True)
    endPos = rig.xform(endJoint,q = True,ws = True,rp = True)    
    getPos = SK_averagePos(num,startPos,endPos,Curve)
    for i,pos in enumerate(getPos):
        if(0 == i):
                createJoint.append(rig.joint(n = name+'_bend'+str(i)+'_startJnt',p = pos))
        elif(len(getPos)-1 == i):
                createJoint.append(rig.joint(n = name+'_bend'+str(i)+'_endJnt',p = pos))  
        else:             
             createJoint.append(rig.joint(n = name+'_bend'+str(i)+'_jnt',p = pos))

    return  createJoint


def SK_freezeObj(obj):
    rig.makeIdentity(apply = True,s = True,r = True,t = True)
    
    
def SK_snapToObj(sourObj,targetObj):
    constraintNode = rig.parentConstraint(sourObj,targetObj)
    rig.delete(constraintNode)


def SK_createCompoundAttrs(outName,num):
    setStrs = []
    upName = 'Boss'
    midName = 'data'
    lowName = 'bess'
    
    outDataName = 'inData'
    suffix = 0
    
    objSC = rig.createNode('choice',n = outName.split('_')[0]+'_SC',ss = True)
    rig.addAttr(objSC,longName=upName, numberOfChildren=num, attributeType='compound' )
    rig.addAttr(outName,longName=outDataName, numberOfChildren=num, attributeType='compound')

    for i in range(num):
        rig.addAttr(outName, longName='out'+lowName+str(i), attributeType='double') 
        rig.addAttr(outName, longName=lowName+str(i), attributeType='double',parent = outDataName) 
        rig.addAttr(objSC,longName=midName+str(i), numberOfChildren=num, attributeType='compound',p = upName )
        for j in range(num):
            suffix += 1
            if(i == j):
                setStrs.append('.'+upName+'.'+midName+str(i)+'.'+lowName+str(suffix))
                rig.addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )
            else:
                rig.addAttr(objSC, longName=lowName+str(suffix), attributeType='double',parent=midName+str(i) )            

    for i,attrName in enumerate(setStrs):
        rig.connectAttr(outName+'.'+outDataName+'.'+lowName+str(i),outName+'.out'+lowName+str(i))
        rig.connectAttr(objSC+'.'+upName+'.'+midName+str(i),objSC+'.input['+str(i)+']')
        rig.setAttr(objSC+attrName,1)
        
    rig.connectAttr(objSC+'.output',outName+'.'+outDataName)
        
    return objSC

        
def SK_pointOnCurveNode(name,curves,num):
    pointOnCurveNode = []
    curveShape = rig.listRelatives(curves,s = True)[0]
    addNum = 1.0/num
    tempNum = addNum
    for i in range(num+1):
        if(0 == i):
            pointNode = rig.createNode('pointOnCurveInfo',n = name+str(i)+'_POC')
            rig.setAttr(pointNode+'.turnOnPercentage',0)
            rig.setAttr(pointNode+'.parameter',0)
            rig.connectAttr(curveShape+'.worldSpace[0]',pointNode+'.inputCurve')
            pointOnCurveNode.append(pointNode)
        elif(num == i):
            pointNode = rig.createNode('pointOnCurveInfo',n = name+str(i)+'_POC')
            rig.setAttr(pointNode+'.turnOnPercentage',1)
            rig.setAttr(pointNode+'.parameter',1)
            rig.connectAttr(curveShape+'.worldSpace[0]',pointNode+'.inputCurve')
            pointOnCurveNode.append(pointNode)
        else:
            pointNode = rig.createNode('pointOnCurveInfo',n = name+str(i)+'_POC')
            rig.setAttr(pointNode+'.turnOnPercentage',1)
            rig.setAttr(pointNode+'.parameter',tempNum)
            rig.connectAttr(curveShape+'.worldSpace[0]',pointNode+'.inputCurve')
            pointOnCurveNode.append(pointNode)
            tempNum +=  addNum   
            
    return  pointOnCurveNode
    
    
def SK_jointOrientation(joint):
    arrorw = ''
    temT = []
    txv = rig.getAttr(joint+'.tx')
    temT.append(math.fabs(txv))
    tyv = rig.getAttr(joint+'.ty')
    temT.append(math.fabs(tyv))
    tzv = rig.getAttr(joint+'.tz')
    temT.append(math.fabs(tzv))
    
    num = max(temT)
    if(0 == temT.index(num)):
        arrorw = 'tx'
    if(1 == temT.index(num)):
        arrorw = 'ty'
    if(2 == temT.index(num)):
        arrorw = 'tz'
    return arrorw 

        
def SK_createSplitJoint():
    startJoint = rig.textFieldButtonGrp('SK_BT_textFieldButtonGrpLoadJnt',q = True,tx = True)
    endJoint = rig.listRelatives(startJoint,c = True)
    jointName = rig.textFieldGrp('SK_BT_textFieldGrpJointName',q = True,tx = True)+'_JNT'
    num = rig.intSliderGrp('SK_BT_intSliderGrpJointNum',q = True,v = True)
    if endJoint:
        joints = SK_splitJoint(jointName,num,startJoint,endJoint[0])    
        rig.joint(joints[0],e = True,oj = 'xyz',secondaryAxisOrient = 'yup',ch = True,zso = True)
        rig.joint(joints[-1],e = True,oj = 'none',secondaryAxisOrient = 'yup',ch = True,zso = True)
        
        getRadius =  rig.getAttr(endJoint[0]+'.radius')
        for jnt in joints:
            rig.setAttr(jnt+'.radius',getRadius)
  
    
def SK_createSplitJointRig(startJoint = 'True',jointName = 'True',num = 5):
    scalVal = rig.getAttr('LfLeg_Leg_IK.scaleVal')
    waistCon = 'waist_Ctrl'
    if not (rig.attributeQuery('second_vis',node = waistCon,ex = True)):
        rig.addAttr(waistCon,ln = 'second_vis',at = 'enum',en = 'off:on:',dv = 0,k = True)
    
    if('True' == startJoint):
        startJoint = rig.textFieldButtonGrp('SK_BT_textFieldButtonGrpLoadJnt',q = True,tx = True)
        jointName = rig.textFieldGrp('SK_BT_textFieldGrpJointName',q = True,tx = True)+'_JNT'
        num = rig.intSliderGrp('SK_BT_intSliderGrpJointNum',q = True,v = True)
    endJoint = rig.listRelatives(startJoint,c = True)
    if endJoint:
        joints = SK_splitJoint(jointName,num,startJoint,endJoint[0],True)    
        rig.joint(joints[0],e = True,oj = 'xyz',secondaryAxisOrient = 'yup',ch = True,zso = True)
        rig.joint(joints[-1],e = True,oj = 'none',secondaryAxisOrient = 'yup',ch = True,zso = True)
        

   
        curveName = rig.rename('split_Curve_CreateOjb',jointName+'_Curve') 
        rig.setAttr(curveName+'.visibility',0)
        pointOnCurveNods = SK_pointOnCurveNode(jointName,curveName,num)
        
        TwisterGRP = []
        xformGRP = []
        locatrorGRP = []
        controls = []
        vtxPosGRP = []
        
        for i , pocNode in enumerate(pointOnCurveNods):
            TwisterGrp = rig.group(empty = True,n = jointName+str(i)+'_Twister')
            TwisterGRP.append(TwisterGrp)
            contraintNode = rig.parentConstraint(joints[0],TwisterGrp)
            rig.delete(contraintNode)
            
            groupName = rig.group(empty = True,n = jointName+str(i)+'_xform')
            xformGRP.append(groupName)
            rig.connectAttr(pocNode+'.position',groupName+'.translate')
            rig.pointConstraint(groupName,joints[i])
            rig.tangentConstraint(curveName,joints[i],weight = 1,upVector = (0,1,0),worldUpType = 'objectrotation',worldUpVector = (0,1,0),worldUpObject = TwisterGrp)
#===============================================================================
# add Attribute        
#===============================================================================
        averageJointNum = 1.0/num
        temNum = 0
        getRadius =  rig.getAttr(endJoint[0]+'.radius')
        BTANode =  rig.createNode('blendTwoAttr',n = jointName+'_BTA',ss = True)
        
#create rotate group
        rotateGrp = rig.group(empty = True,n = jointName+'_bendRotateGrp')
        SK_snapToObj(joints[0],rotateGrp)

        
        for i,jnt in enumerate(joints):
            rig.setAttr(jnt+'.radius',getRadius)
            rig.addAttr(jnt,ln = 'twist',at = 'float',min = 0,max = 1,dv = 0,k = True) 
            rig.setAttr(jnt+'.twist',temNum) 
            temNum +=  averageJointNum 
            
            MPANode =  rig.createNode('plusMinusAverage',n = jointName+'_'+str(i)+'_MPA',ss = True)
            rig.connectAttr(rotateGrp+'.rx',MPANode+'.input1D[0]')   
            
            MDNode = rig.createNode('multiplyDivide',n = jointName+'_'+str(i)+'_MD',ss = True) 
            rig.connectAttr(MPANode+'.output1D',MDNode+'.input1X')             
            rig.connectAttr(jnt+'.twist',MDNode+'.input2X')            
 
            rig.connectAttr(BTANode+'.output',MPANode+'.input1D[1]')                      
            rig.connectAttr(MDNode+'.outputX',TwisterGRP[i]+'.rx') 
              
#===============================================================================
#        creat locator
#===============================================================================
        vtxs = rig.ls(curveName+'.cv[*]',fl = True)
        for i,vtx in enumerate(vtxs):
            curveNameShape = rig.listRelatives(curveName,s = True)[0]
            vtxPos = rig.pointPosition(vtx)
            vtxPosGRP.append(vtxPos)
            locName = rig.spaceLocator(n = curveName+str(i)+'_Loc')[0]
            rig.setAttr(locName+'.visibility',0)
            locatrorGRP.append(locName)
            rig.setAttr(locName+'.translate',vtxPos[0],vtxPos[1],vtxPos[2])
            locNameShape = rig.listRelatives(locName,s = True)[0]        
            rig.connectAttr(locNameShape+'.worldPosition[0]',curveNameShape+'.controlPoints['+str(i)+']')
        
#===============================================================================
#        group obj
#===============================================================================
        TwisterName = rig.group(TwisterGRP,n = jointName+'_TwisterGRP')
        xformName = rig.group(xformGRP,n = jointName+'_xformGRP')
        locName = rig.group(locatrorGRP,n = jointName+'_locatrorGRP')
        
#===============================================================================
#        add Controllers
#===============================================================================
        controlGRP = rig.group(empty = True ,n = 'CTRL_'+jointName+'_GRP')
        
        rig.setAttr(controlGRP+'.translate',vtxPosGRP[0][0],vtxPosGRP[0][1],vtxPosGRP[0][2])        
        rig.parent(controlGRP,startJoint)
        rig.makeIdentity(controlGRP,apply = True,s = 1,t = 1,r = 1)
        for i,loc in enumerate(locatrorGRP):
            CurrentCurve = SK_b29(17)
            currntCurveName = rig.rename(CurrentCurve,jointName+str(i)+'_bend')
            controls.append(currntCurveName)
            rig.setAttr(currntCurveName+'.rz',90)
            rig.setAttr(currntCurveName+'.scale',0.1*scalVal,0.1*scalVal,0.1*scalVal)
            SK_freezeObj(currntCurveName)
            rig.setAttr(currntCurveName+'.translate',vtxPosGRP[i][0],vtxPosGRP[i][1],vtxPosGRP[i][2])
            pointConstraints = rig.orientConstraint(joints[0],currntCurveName)
            rig.delete(pointConstraints )
            
            rig.parent(loc,currntCurveName)
            rig.parent(currntCurveName,controlGRP)
            
        rig.makeIdentity(controlGRP,apply = True,s = True,r = True,t = True)
        rig.parent(joints[0],startJoint)
        rig.parent(TwisterName,startJoint)
        rig.parent(rotateGrp,startJoint)
        rig.delete(locName)
        
        BendDeformerGrp = rig.group(curveName,xformName,n = jointName+'_Bend_Grp')
        rig.setAttr(controls[0]+'.visibility',0)
        rig.setAttr(controls[2]+'.visibility',0)
        
#       create deformers
        if (rig.objExists('LegArm_deformers')):
            rig.parent(BendDeformerGrp,'LegArm_deformers')
        else:
            deformersGrp = rig.group(empty = True,n = 'LegArm_deformers')
            rig.parent(BendDeformerGrp,'LegArm_deformers')
            
#       pointConstraint
        controlMidGrp = rig.group(controls[1],n = controls[1]+'_Grp' )       
        MidEmptyGrp = rig.group(empty = True,n = jointName+'_Mid_Distance') 
        SK_snapToObj(controlGRP,MidEmptyGrp) 
        rig.parent(MidEmptyGrp,controlGRP)
        
        rig.pointConstraint(startJoint,endJoint[0],MidEmptyGrp,mo = True)
        rig.pointConstraint(endJoint[0],controls[2])

        rig.connectAttr(MidEmptyGrp+'.tx',controlMidGrp+'.tx')        
        rig.connectAttr(waistCon+'.second_vis',controls[1]+'.visibility')
        
        if(0 > rig.getAttr(endJoint[0]+'.tx')):
            rig.setAttr(controls[1]+'.rz',180)
            rig.setAttr(controls[1]+'.sz',-1)  
        SK_hideLockAll(controls[1],0)

   
def SK_AddAttributes(curveName,controlsCurve):
    if ('Leg' == controlsCurve): 
        rig.setAttr(curveName+'.sx',k = False,cb = False)  
        rig.setAttr(curveName+'.sy',k = False,cb = False) 
        rig.setAttr(curveName+'.sz',k = False,cb = False) 
        rig.addAttr(curveName,ln = 'raiseBall',at = 'float',dv = 0,k = True)
        rig.addAttr(curveName,ln = 'raiseToeTip',at = 'float',dv = 0,k = True)
        rig.addAttr(curveName,ln = 'side',at = 'float',dv = 0,k = True)        
        rig.addAttr(curveName,ln = 'swivel',at = 'float',dv = 0,k = True)        
        rig.addAttr(curveName,ln = 'roll',at = 'float',dv = 0,k = True)
        rig.addAttr(curveName,ln = 'raiseToe',at = 'float',dv = 0,k = True)
        rig.addAttr(curveName,ln = 'swivelToe',at = 'float',dv = 0,k = True)

        
        rig.addAttr(curveName,ln = 'scaleVal',at = 'float',dv = 0) 
        rig.addAttr(curveName,ln = 'swivelToeTip',at = 'float',dv = 0,k = False)
        rig.addAttr(curveName,ln = 'swivelBall',at = 'float',dv = 0,k = False)
        rig.addAttr(curveName,ln = 'LockKnee',at = 'float',dv = 0,k = False)
        rig.addAttr(curveName,ln = 'raiseHeel',at = 'float',dv = 0,k = False)
        rig.addAttr(curveName,ln = 'swivelHeel',at = 'float',dv = 0,k = False)
        
          
def SK_getSkinCluster(obj):
    skinCls = rig.ls(rig.listHistory(obj,pdo = True),type = 'skinCluster')
    if skinCls:
        return skinCls[0] 
    else:
        return False
