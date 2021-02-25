#-*- coding: utf-8 -*-
import maya.cmds as rig
import math

def SK_jointFitRoTr(temMatrix,hand = True):
    ankle = 'Lf_wrist_drv'
    ankleMid = 'Lf_hand_drv'
    Pos =  [8.7267887740249694, 18.63269166108023, -0.49451702984810358]     
    jointOrientDate = [-3.4310233626287698e-013, -8.3489560388417303e-015, 5.7061710203996496e-015]
    
    if(hand):
        ankle = 'Lf_foot_drv'
        ankleMid = 'Lf_foot_end_drv'
        Pos = [1.160582981201866, 0.14555530459733612, 0.84313350370823392] 
        jointOrientDate = [90.000000000000298, -85.696634155722947, -90.000000000000824]

    rig.select(cl = True)            
    temJoint = rig.joint(p = Pos,n = 'temTrRoJoint')
    rig.setAttr(temJoint+'.jointOrientX',jointOrientDate[0])
    rig.setAttr(temJoint+'.jointOrientY',jointOrientDate[1])
    rig.setAttr(temJoint+'.jointOrientZ',jointOrientDate[2])
    
    rig.setAttr(temMatrix+'.inPoint',Pos[0],Pos[1],Pos[2]) 
    jntPositionX = rig.getAttr(temMatrix+'.outputX')
    jntPositionY = rig.getAttr(temMatrix+'.outputY')        
    jntPositionZ = rig.getAttr(temMatrix+'.outputZ')
    rig.xform(temJoint,t = (jntPositionX,jntPositionY,jntPositionZ),ws = True)
    
    wristChildes = rig.listRelatives(ankle,c = True)
    wristChildes.remove(ankleMid)
    if(wristChildes):
        rig.parent(wristChildes,temJoint)
    
    transPos = rig.xform(ankle,q = True,t = True,ws = True)
    transRo = rig.xform(ankle,q = True,ro = True,ws = True) 
    rig.xform(temJoint,t = transPos,ws = True)  
    rig.xform(temJoint,ro = transRo,ws = True)
    if(wristChildes):
        rig.parent(wristChildes,ankle) 
    
    rig.delete(temJoint)    
    

def SK_builderFinger(info,temMatrix,scaleVal):
    fingerInfo = info
    allJnts = fingerInfo[0]
    jntPos = fingerInfo[1]
    jntOrient = fingerInfo[2]
    jntParent = fingerInfo[3]
 
    for i,jnt in enumerate(allJnts):
        rig.setAttr(temMatrix+'.inPoint',jntPos[i][0],jntPos[i][1],jntPos[i][2]) 
        jntPositionX = rig.getAttr(temMatrix+'.outputX')
        jntPositionY = rig.getAttr(temMatrix+'.outputY')        
        jntPositionZ = rig.getAttr(temMatrix+'.outputZ')

        jntName = rig.joint(p = [jntPositionX,jntPositionY,jntPositionZ],n = jnt)
        rig.setAttr(jntName+'.radius',scaleVal*0.5)
        rig.setAttr(jntName+'.jointOrientX',jntOrient[i][0])
        rig.setAttr(jntName+'.jointOrientY',jntOrient[i][1])   
        rig.setAttr(jntName+'.jointOrientZ',jntOrient[i][2])
        rig.select(cl = True)
        
    for i,jnt in enumerate(allJnts):
        if(jntParent[i][0]):
            rig.parent(jnt,jntParent[i][0])

    
def SK_createFingers(handNum = 5,footNum = 5):
    endJntPos = rig.xform('head_end_jnt',q = True,t = True,ws = True)
    distanceJnt = math.sqrt(math.pow(endJntPos[0],2)+math.pow(endJntPos[1],2)+math.pow(endJntPos[2],2))
    scaleVal =  distanceJnt/23.0761871315
    temGrp = rig.group(empty = True,n = 'tempGroup')
    rig.setAttr(temGrp+'.scale',scaleVal,scaleVal,scaleVal)
    temMatrix = rig.createNode('pointMatrixMult',n = 'tem_matrix')
    rig.connectAttr(temGrp+'.matrix',temMatrix+'.inMatrix')
    
    temJnt = rig.ls('Lf_*Root_jnt')
    if temJnt:
        rig.delete(temJnt)

    temJnt = rig.ls('Lf_*thumb1_jnt')
    if temJnt:
        rig.delete(temJnt)
                  
    fingerInfos = [[[u'Lf_thumb1_jnt', u'Lf_thumb2_jnt', u'Lf_thumb3_jnt', u'Lf_thumb4_jnt'], [[9.3522012083227679, 18.568351916864479, 0.032560924652662138], [9.5998716774144448, 18.568351916864479, 0.29131826020986112], [9.8475421465061217, 18.568351916864479, 0.55007559576706067], [10.095212615597797, 18.568351916864479, 0.80883293132425704]], [[0.0, -46.254135726694379, 0.0], [0.0, -46.254135726694379, 0.0], [0.0, -46.254135726694379, 0.0], [0.0, -46.254135726694379, 0.0]], [[[u'Lf_wrist_drv']], [[u'Lf_thumb1_jnt']], [[u'Lf_thumb2_jnt']], [[u'Lf_thumb3_jnt']]]], [[u'Lf_indexRoot_jnt', u'Lf_index1_jnt', u'Lf_index2_jnt', u'Lf_index3_jnt', u'Lf_index4_jnt'], [[9.1290539082032431, 18.632691661080226, -0.21536848077372972], [10.020505431298163, 18.634754650724364, -0.19516930764343474], [10.362615580316104, 18.634754650724361, -0.090523850296771471], [10.704725729334042, 18.634754650724361, 0.014121607049891197], [11.046835878351981, 18.634754650724361, 0.11876706439655481]], [[0.0, -0.0, 0.0], [0.0, -17.007946955407267, 0.0], [0.0, -17.007946955407267, 0.0], [0.0, -17.007946955407267, 0.0], [0.0, -17.007946955407267, 0.0]], [[[u'Lf_wrist_drv']], [[u'Lf_indexRoot_jnt']], [[u'Lf_index1_jnt']], [[u'Lf_index2_jnt']], [[u'Lf_index3_jnt']]]], [[u'Lf_midRoot_jnt', u'Lf_mid1_jnt', u'Lf_mid2_jnt', u'Lf_mid3_jnt', u'Lf_mid4_jnt'], [[9.139896226716651, 18.632691661080226, -0.42064431710596384], [10.105026762232013, 18.634754650724368, -0.46684501421650371], [10.515558941053539, 18.634754650724368, -0.45275812572752955], [10.926091119875066, 18.634754650724368, -0.43867123723855539], [11.33662329869659, 18.634754650724368, -0.42458434874958129]], [[0.0, -0.0, 0.0], [0.0, -1.965260571920554, 0.0], [0.0, -1.965260571920554, 0.0], [0.0, -1.965260571920554, 0.0], [0.0, -1.965260571920554, 0.0]], [[[u'Lf_wrist_drv']], [[u'Lf_midRoot_jnt']], [[u'Lf_mid1_jnt']], [[u'Lf_mid2_jnt']], [[u'Lf_mid3_jnt']]]], [[u'Lf_ringRoot_jnt', u'Lf_ring1_jnt', u'Lf_ring2_jnt', u'Lf_ring3_jnt', u'Lf_ring4_jnt'], [[9.1369833650264827, 18.632691661080226, -0.64113176448686149], [10.056728858841243, 18.634754650724368, -0.75059519663726482], [10.42701278483713, 18.634754650724364, -0.8310917022885449], [10.79729671083302, 18.634754650724364, -0.91158820793982553], [11.167580636828909, 18.634754650724364, -0.99208471359110584]], [[0.0, -0.0, 0.0], [0.0, 12.264773727892408, 0.0], [0.0, 12.264773727892406, 0.0], [0.0, 12.264773727892406, 0.0], [0.0, 12.264773727892406, 0.0]], [[[u'Lf_wrist_drv']], [[u'Lf_ringRoot_jnt']], [[u'Lf_ring1_jnt']], [[u'Lf_ring2_jnt']], [[u'Lf_ring3_jnt']]]], [[u'Lf_pinkyRoot_jnt', u'Lf_pinky1_jnt', u'Lf_pinky2_jnt', u'Lf_pinky3_jnt', u'Lf_pinky4_jnt'], [[9.1067219685786078, 18.632691661080226, -0.84381839042783402], [9.8514627694304799, 18.634754650724368, -0.95586128604802756], [10.131188126568675, 18.634754650724364, -1.0705688066011008], [10.410913483706874, 18.634754650724364, -1.1852763271541762], [10.690638840845073, 18.634754650724364, -1.2999838477072503]], [[0.0, -0.0, 0.0], [0.0, 22.297157876787221, 0.0], [0.0, 22.297157876787221, 0.0], [0.0, 22.297157876787221, 0.0], [0.0, 22.297157876787221, 0.0]], [[[u'Lf_wrist_drv']], [[u'Lf_pinkyRoot_jnt']], [[u'Lf_pinky1_jnt']], [[u'Lf_pinky2_jnt']], [[u'Lf_pinky3_jnt']]]], [[u'Lf_Toe_thumb1_jnt', u'Lf_Toe_thumb2_jnt', u'Lf_Toe_thumb3_jnt', u'Lf_Toe_thumb4_jnt'], [[0.58398758865181477, 0.25770999537402828, 1.3914302311082767], [0.58282865741504641, 0.25770999463423733, 1.5907664038323928], [0.5816697261782785, 0.25770999389444643, 1.7901025765565097], [0.58051079494151026, 0.25770999315465543, 1.9894387492806263]], [[179.99996342525449, -89.666888756078563, -179.99996342587244], [179.99996342525424, -89.666888756078563, -179.99996342587229], [179.99996342525424, -89.666888756078563, -179.99996342587229], [179.99996342525424, -89.666888756078563, -179.99996342587229]], [[[u'Lf_foot_drv']], [[u'Lf_Toe_thumb1_jnt']], [[u'Lf_Toe_thumb2_jnt']], [[u'Lf_Toe_thumb3_jnt']]]], [[u'Lf_Toe_indexRoot_jnt', u'Lf_Toe_index1_jnt', u'Lf_Toe_index2_jnt', u'Lf_Toe_index3_jnt', u'Lf_Toe_index4_jnt'], [[0.91080619742042213, 0.25770999537402706, 1.1544111117054137], [0.91080619742042224, 0.25770999537402695, 1.3914302311082762], [0.9096472661836521, 0.25770999463423594, 1.590766403832393], [0.9084883349468823, 0.25770999389444504, 1.7901025765565095], [0.90732940371011217, 0.25770999315465404, 1.989438749280626]], [[179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312]], [[[u'Lf_foot_drv']], [[u'Lf_Toe_indexRoot_jnt']], [[u'Lf_Toe_index1_jnt']], [[u'Lf_Toe_index2_jnt']], [[u'Lf_Toe_index3_jnt']]]], [[u'Lf_Toe_midRoot_jnt', u'Lf_Toe_mid1_jnt', u'Lf_Toe_mid2_jnt', u'Lf_Toe_mid3_jnt', u'Lf_Toe_mid4_jnt'], [[1.2445783936096415, 0.25770999537402545, 1.1544111117054139], [1.244578393609642, 0.25770999537402528, 1.3914302311082758], [1.2434194623728718, 0.25770999463423433, 1.5907664038323925], [1.2422605311361012, 0.25770999389444343, 1.7901025765565091], [1.2411015998993309, 0.25770999315465232, 1.9894387492806256]], [[179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312]], [[[u'Lf_foot_drv']], [[u'Lf_Toe_midRoot_jnt']], [[u'Lf_Toe_mid1_jnt']], [[u'Lf_Toe_mid2_jnt']], [[u'Lf_Toe_mid3_jnt']]]], [[u'Lf_Toe_ringRoot_jnt', u'Lf_Toe_ring1_jnt', u'Lf_Toe_ring2_jnt', u'Lf_Toe_ring3_jnt', u'Lf_Toe_ring4_jnt'], [[1.5679202086679469, 0.25770999537402423, 1.1544111117054137], [1.5679202086679471, 0.25770999537402406, 1.3914302311082767], [1.5667612774311772, 0.25770999463423311, 1.5907664038323936], [1.5656023461944069, 0.25770999389444221, 1.7901025765565102], [1.5644434149576363, 0.2577099931546511, 1.9894387492806267]], [[179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312]], [[[u'Lf_foot_drv']], [[u'Lf_Toe_ringRoot_jnt']], [[u'Lf_Toe_ring1_jnt']], [[u'Lf_Toe_ring2_jnt']], [[u'Lf_Toe_ring3_jnt']]]], [[u'Lf_Toe_pinkyRoot_jnt', u'Lf_Toe_pinky1_jnt', u'Lf_Toe_pinky2_jnt', u'Lf_Toe_pinky3_jnt', u'Lf_Toe_pinky4_jnt'], [[1.919076373408688, 0.25770999537402278, 1.1544111117054137], [1.9190763734086882, 0.25770999537402267, 1.3914302311082767], [1.9179174421719174, 0.25770999463423166, 1.5907664038323934], [1.9167585109351475, 0.25770999389444077, 1.79010257655651], [1.9155995796983771, 0.25770999315464965, 1.9894387492806265]], [[179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312], [179.99996342525517, -89.666888756078038, -179.99996342587312]], [[[u'Lf_foot_drv']], [[u'Lf_Toe_pinkyRoot_jnt']], [[u'Lf_Toe_pinky1_jnt']], [[u'Lf_Toe_pinky2_jnt']], [[u'Lf_Toe_pinky3_jnt']]]]]


    for finger in range(handNum): 
        SK_builderFinger(fingerInfos[finger],temMatrix,scaleVal)

    for finger in range(footNum):
        SK_builderFinger(fingerInfos[5+finger],temMatrix,scaleVal)  
    
    
    rig.select(cl = True)   
#   手指可以跟随胳膊移动和旋转 
    SK_jointFitRoTr(temMatrix,True)
    SK_jointFitRoTr(temMatrix,False) 
    rig.xform('Lf_foot_outside_refer',t = (0.012155380429738405, -0.1450521391457899, -0.76829283869640608),ws = False ) 
    rig.xform('Lf_foot_inside_refer',t = (0.012155380429739626, -0.14505213914580478, 0.7894268584635582),ws = False )   
  
    rig.delete(temGrp,temMatrix) 
    
