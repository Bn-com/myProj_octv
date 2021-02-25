#-*- coding: utf-8 -*-
import maya.cmds as rig
from RIG.nurbsCurveCon import *
from RIG.commonly.base import *
import math

def SK_fingerCreatePose(obj,attribute):
    selObj = obj
    attrName = attribute
    ctrlAttr = rig.connectionInfo(selObj+'.ctrl',sfd = True)
    midJnt = ctrlAttr.split('.')[0]
    rootJnt = rig.listRelatives(midJnt,p = True)[0]
    ikCon = rig.connectionInfo(rootJnt+'.scale',sfd = True).split('.')[0]
    controlName = ikCon.split('_')[0]+'_Switch'
    
    if not (rig.attributeQuery('fingerPose',node = controlName,ex = True)):
        rig.addAttr(controlName,ln = 'fingerPose',at = 'enum',en = '-----------:',k = True)
        rig.setAttr(controlName+'.fingerPose',k = False,cb = True)
    
    rig.addAttr(controlName,ln = attrName,at = 'float',minValue = -1,maxValue = 1,dv = 1,k = True)
    ctrls = [ctrl.split('.')[0] for ctrl in rig.connectionInfo(midJnt+'.ctrl',dfs = True)]
    ctrls = [ctrl for ctrl in ctrls if not ('_End' in ctrl)]
    for ctrl in ctrls:
        attrs = rig.listAttr(ctrl,k = True)
        for attr in attrs:
            attrV = rig.getAttr(ctrl+'.'+attr)
            if(math.fabs(attrV) > 0.01):
                ctrlJnt = rig.listRelatives(ctrl,p = True)[0]
                attrJnt = attrName+'_'+attr
                rig.addAttr(ctrlJnt,ln = attrJnt,at = 'float',dv = attrV)
                
                lsConnectJnt = rig.listConnections(ctrlJnt+'.'+attr,s = True,d = False,scn = True,p = True)
                if lsConnectJnt:
                    lsConnectJnt = lsConnectJnt[0]
                    if 'plusMinusAverage' == rig.nodeType(lsConnectJnt.split('.')[0]):
                        existsMPA = lsConnectJnt.split('.')[0]
                        numMPA = len(rig.getAttr(existsMPA+'.input1D[*]'))
                        existsMD = SK_MDNode(controlName)
                        if existsMD:
                            inMD,inMD1,outMD = existsMD
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                            rig.connectAttr(controlName+'.'+attrName,inMD1)
                            rig.connectAttr(outMD,existsMPA+'.input1D['+str(numMPA)+']')
                        else:
                            jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                            rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                            rig.connectAttr(jntMD+'.outputX',existsMPA+'.input1D['+str(numMPA)+']')
                    else:
                        existsMD = SK_MDNode(controlName)
                        jntMPA = rig.createNode('plusMinusAverage',n = ctrl+'_MPA',ss = True)
                        
                        if existsMD:
                            inMD,inMD1,outMD = existsMD
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                            rig.connectAttr(controlName+'.'+attrName,inMD1)
                            rig.connectAttr(outMD,jntMPA+'.input1D[1]')
                        else:
                            jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                            rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                            rig.connectAttr(jntMD+'.outputX',jntMPA+'.input1D[1]')
                        rig.connectAttr(lsConnectJnt,jntMPA+'.input1D[0]')                    
                        rig.connectAttr(jntMPA+'.output1D',ctrlJnt+'.'+attr,f = True)
                                            
                else:
                    existsMD = SK_MDNode(controlName)
                    jntMPA = rig.createNode('plusMinusAverage',n = ctrl+'_MPA',ss = True)
                    
                    if existsMD:
                        inMD,inMD1,outMD = existsMD
                        rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                        rig.connectAttr(controlName+'.'+attrName,inMD1)
                        rig.connectAttr(outMD,jntMPA+'.input1D[1]')
                    else:
                        jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                        rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                        rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                        rig.connectAttr(jntMD+'.outputX',jntMPA+'.input1D[1]')
    #                rig.connectAttr(lsConnectJnt,jntMPA+'.input1D[0]')
                    if(rig.getAttr(ctrlJnt+'.'+attr,l = True)):
                        rig.setAttr(ctrlJnt+'.'+attr,l = False)                    
                        rig.connectAttr(jntMPA+'.output1D',ctrlJnt+'.'+attr,f = True)
                    
                    
                    
    for ctrl in ctrls:
        attrs = rig.listAttr(ctrl,k = True)
        for attr in attrs:
            attrV = rig.getAttr(ctrl+'.'+attr)
            if(math.fabs(attrV) > 0.01):
                rig.setAttr(ctrl+'.'+attr,0)


def SK_fingerEditPose(obj,attribute):
    selObj = obj
    attrName = attribute
    ctrlAttr = rig.connectionInfo(selObj+'.ctrl',sfd = True)
    midJnt = ctrlAttr.split('.')[0]
    rootJnt = rig.listRelatives(midJnt,p = True)[0]
    ikCon = rig.connectionInfo(rootJnt+'.scale',sfd = True).split('.')[0]
    controlName = ikCon.split('_')[0]+'_Switch'
    
    if not rig.objExists(controlName):
        scaleVal = rig.getAttr(ikCon+'.scaleVal')
        curveName = rig.rename(SK_b29(4),controlName)
        rig.setAttr(curveName+'.scale',0.1*scaleVal,0.1*scaleVal,0.1*scaleVal)
        rig.setAttr(curveName+'.rz',90)
        SK_freezeObj(curveName)
        SK_snapToObj(midJnt,curveName)
        rig.parent(curveName,midJnt)
        SK_hideLockAll(curveName)    
    
    if not (rig.attributeQuery(attrName,node = controlName,ex = True)):
        rig.addAttr(controlName,ln = attrName,at = 'float',minValue = -1,maxValue = 1,dv = 1,k = True)
    ctrls = [ctrl.split('.')[0] for ctrl in rig.connectionInfo(midJnt+'.ctrl',dfs = True)]
    ctrls = [ctrl for ctrl in ctrls if not ('_End' in ctrl)]
    for ctrl in ctrls:
        attrs = rig.listAttr(ctrl,k = True)
        for attr in attrs:
            attrV = rig.getAttr(ctrl+'.'+attr)
            if(math.fabs(attrV) > 0.01):
                ctrlJnt = rig.listRelatives(ctrl,p = True)[0]
                attrJnt = attrName+'_'+attr    
                
                if(rig.attributeQuery(attrJnt,node = ctrlJnt,ex = True)):
                    rig.setAttr(ctrlJnt+'.'+attrJnt,attrV)

                
                else:    
  
                    rig.addAttr(ctrlJnt,ln = attrJnt,at = 'float',dv = attrV)
                    
                    lsConnectJnt = rig.listConnections(ctrlJnt+'.'+attr,s = True,d = False,scn = True,p = True)
                    if lsConnectJnt:
                        lsConnectJnt = lsConnectJnt[0]
                        if 'plusMinusAverage' == rig.nodeType(lsConnectJnt.split('.')[0]):
                            existsMPA = lsConnectJnt.split('.')[0]
                            numMPA = len(rig.getAttr(existsMPA+'.input1D[*]'))
                            existsMD = SK_MDNode(controlName)
                            if existsMD:
                                inMD,inMD1,outMD = existsMD
                                rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                                rig.connectAttr(controlName+'.'+attrName,inMD1)
                                rig.connectAttr(outMD,existsMPA+'.input1D['+str(numMPA)+']')
                            else:
                                jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                                rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                                rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                                rig.connectAttr(jntMD+'.outputX',existsMPA+'.input1D['+str(numMPA)+']')
                        else:
                            existsMD = SK_MDNode(controlName)
                            jntMPA = rig.createNode('plusMinusAverage',n = ctrl+'_MPA',ss = True)
                            
                            if existsMD:
                                inMD,inMD1,outMD = existsMD
                                rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                                rig.connectAttr(controlName+'.'+attrName,inMD1)
                                rig.connectAttr(outMD,jntMPA+'.input1D[1]')
                            else:
                                jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                                rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                                rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                                rig.connectAttr(jntMD+'.outputX',jntMPA+'.input1D[1]')
                            rig.connectAttr(lsConnectJnt,jntMPA+'.input1D[0]')                    
                            rig.connectAttr(jntMPA+'.output1D',ctrlJnt+'.'+attr,f = True)
                                                
                    else:
                        existsMD = SK_MDNode(controlName)
                        jntMPA = rig.createNode('plusMinusAverage',n = ctrl+'_MPA',ss = True)
                        
                        if existsMD:
                            inMD,inMD1,outMD = existsMD
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,inMD)                
                            rig.connectAttr(controlName+'.'+attrName,inMD1)
                            rig.connectAttr(outMD,jntMPA+'.input1D[1]')
                        else:
                            jntMD = rig.createNode('multiplyDivide',n = ctrl+'_MD',ss = True)
                            rig.connectAttr(ctrlJnt+'.'+attrJnt,jntMD+'.input1X')                
                            rig.connectAttr(controlName+'.'+attrName,jntMD+'.input2X')
                            rig.connectAttr(jntMD+'.outputX',jntMPA+'.input1D[1]')
        #                rig.connectAttr(lsConnectJnt,jntMPA+'.input1D[0]')                    
                    if(rig.getAttr(ctrlJnt+'.'+attr,l = True)):
                        rig.setAttr(ctrlJnt+'.'+attr,l = False)                    
                        rig.connectAttr(jntMPA+'.output1D',ctrlJnt+'.'+attr,f = True)
                        
                    
                    
    for ctrl in ctrls:
        attrs = rig.listAttr(ctrl,k = True)
        for attr in attrs:
            attrV = rig.getAttr(ctrl+'.'+attr)
            if(math.fabs(attrV) > 0.01):
                rig.setAttr(ctrl+'.'+attr,0)

    
def SK_fingerMirrorPose(obj):
    selObj = obj
    ctrlAttr = rig.connectionInfo(selObj+'.ctrl',sfd = True)
    midJnt = ctrlAttr.split('.')[0]
    ctrls = [ctrl.split('.')[0] for ctrl in rig.connectionInfo(midJnt+'.ctrl',dfs = True)]
    ctrls = [ctrl for ctrl in ctrls if not ('_End' in ctrl)]
    for ctrl in ctrls:
        attrs = rig.listAttr(ctrl,k = True)
        for attr in attrs:
            attrV = rig.getAttr(ctrl+'.'+attr)
            if(math.fabs(attrV) > 0.01):
                leftAttr = ctrl+'.'+attr
                rightAttr = leftAttr.replace('Lf','Rt')
                
                if(rig.objExists(rightAttr.split('.')[0])):                    
                    if('translate' in rightAttr):
                        rig.setAttr(rightAttr,-1*attrV)
                    else:
                        rig.setAttr(rightAttr,attrV)


def SK_fingerCopyData(obj,attribute):
    selObj = obj
    attrName = attribute
    ctrlAttr = rig.connectionInfo(selObj+'.ctrl',sfd = True)
    midJnt = ctrlAttr.split('.')[0]
    rootJnt = rig.listRelatives(midJnt,p = True)[0]
    ikCon = rig.connectionInfo(rootJnt+'.scale',sfd = True).split('.')[0]
    controlName = ikCon.split('_')[0]+'_Switch'   


    ctrls = [ctrl.split('.')[0] for ctrl in rig.connectionInfo(midJnt+'.ctrl',dfs = True)]
    ctrls = [ctrl for ctrl in ctrls if not ('_End' in ctrl)]
    parentCtrls = [rig.listRelatives(ctrl,p = True)[0] for ctrl in ctrls if not ('_End' in ctrl)]    
    for i,pctrl in enumerate(parentCtrls):
        attrs = rig.listAttr(pctrl,ud = True)
        if(attrs):
            for attr in attrs:
                if(attrName+'_' in attr):
                    attrV = rig.getAttr(pctrl+'.'+attr)    
                    rig.setAttr(ctrls[i]+'.'+attr.split('_')[1],attrV)
                    rig.setAttr(pctrl+'.'+attr,0)            


def SK_fingerAdd():                
    objs = rig.ls(sl = True)[0]
    attrName = rig.textField('aTF',q = True,text = True)
    
    SK_fingerMirrorPose(objs)
    SK_fingerCreatePose(objs,attrName)
    LfFingerJnt = rig.listConnections('Lf_index1'+'.ctrl',s = True,d = False,type = 'joint')[0]
    RtFingerJnt = LfFingerJnt.replace('Lf','Rt')
    if RtFingerJnt:
        rightObjs = rig.listConnections(RtFingerJnt+'.ctrl',s = False,d = True)[0]
        SK_fingerCreatePose(rightObjs,attrName)    
        
    
def SK_fingerEdit():                
    objs = rig.ls(sl = True)[0]
    attrName = rig.textField('aTF',q = True,text = True)
    rig.button('EditButton',e = True,en = False)
    rig.button('ResetButton',e = True,en = True)
    
    SK_fingerMirrorPose(objs)
    SK_fingerEditPose(objs,attrName)
    rightObjs = objs.replace('Lf','Rt')
    SK_fingerEditPose(rightObjs,attrName)    
    

def SK_fingerCopy():
    objs = rig.ls(sl = True)[0]
    attrName = rig.textField('aTF',q = True,text = True)
    rig.button('EditButton',e = True,en = True)
    rig.button('ResetButton',e = True,en = False)
    SK_fingerCopyData(objs,attrName)    

    rightObjs = objs.replace('Lf','Rt')
    SK_fingerCopyData(rightObjs,attrName)    


def SK_MDNode(obj):
    outputAttr = []
    inputs = ['input1X','input1Y','input1Z']
    Nodes = rig.listConnections(obj,s = False,d = True,scn = True,type = 'multiplyDivide')
    if Nodes:
        for md in Nodes:
            for inputValue in inputs:
                isCon = rig.connectionInfo(md+'.'+inputValue,sfd = True)
                if not isCon:
                    inputPlug = md+'.'+inputValue
                    inputPlug2 = md+'.'+inputValue.replace('1','2')
                    outputPlug = md+'.output'+inputValue[-1]
                    outputAttr.append(inputPlug)
                    outputAttr.append(inputPlug2)
                    outputAttr.append(outputPlug)                    
                    return outputAttr
    else:
        return outputAttr



    
 
