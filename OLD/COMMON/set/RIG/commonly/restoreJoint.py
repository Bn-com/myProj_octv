#-*- coding: utf-8 -*-
import maya.cmds as rig
import os
import pickle
import math
from RIG.selectJoint import SK_selectSkinJnt
import tempfile


def SK_restoreJoint(restore = False) :
    filePath = tempfile.gettempdir()+'/PosFile.txt'
    if not restore:
        dbase = []
        allJnts = rig.ls(rig.listRelatives('Character',c = True,ad = True),type = 'joint')
        jntPos = [rig.xform(jnt,q = True,t = True,ws = True) for jnt in allJnts]
        jntParent = [[rig.listRelatives(jnt,p = True)[0]] for jnt in allJnts]
        rig.parent(allJnts,w = True)
        jntOrient = [[rig.getAttr(jnt+'.jointOrientX'),rig.getAttr(jnt+'.jointOrientY'),rig.getAttr(jnt+'.jointOrientZ')] for jnt in allJnts]
        radiusList = [rig.getAttr(jnt+'.radius') for jnt in allJnts]

        for i,jnt in enumerate(allJnts):
            if(jntParent[i][0]):
                rig.parent(jnt,jntParent[i][0])
        
        dbase.append(allJnts)
        dbase.append(jntPos)
        dbase.append(jntOrient)
        dbase.append(jntParent)
        dbase.append(radiusList)
        newFile = open(filePath,'w')
        pickle.dump(dbase,newFile)
        newFile.close()
        getData = open(filePath,'r')
        getDate = getData.read()
        getData.close()
        rig.addAttr('CharacterShape',ln = 'pos',dt = 'string')
        rig.setAttr('CharacterShape.pos',getDate,type = 'string')
        os.remove(filePath)    
    
    else:
        newFile = open(filePath,'w')
        newFile.write(rig.getAttr('CharacterShape.pos'))
        newFile.close()
        readFile = open(filePath,'r')
        dbase = pickle.load(readFile)
        readFile.close()
        os.remove(filePath)
        allJnts = dbase[0]
        jntPos = dbase[1]
        jntOrient = dbase[2]
        jntParent = dbase[3]
        radiusList = dbase[4]
        rig.file(f = True,new = True)
        

        masterName = rig.circle(nr = (0,1,0),ch = False,o = True,r = 4.629333,n = 'Character')[0]
        rig.addAttr(masterName,ln = 'ctrl',at = 'float')
        rig.select(cl = True)
        for i,jnt in enumerate(allJnts):
            jntName = rig.joint(p = jntPos[i],n = jnt)
            rig.setAttr(jntName+'.radius',radiusList[i])
            rig.setAttr(jntName+'.jointOrientX',jntOrient[i][0])
            rig.setAttr(jntName+'.jointOrientY',jntOrient[i][1])   
            rig.setAttr(jntName+'.jointOrientZ',jntOrient[i][2])
            rig.select(cl = True)
            
        for i,jnt in enumerate(allJnts):
            if(jntParent[i][0]):
                rig.parent(jnt,jntParent[i][0])
                
    rig.select(cl = True)
        

def SK_skinBendJoint():
    nameBends = ['knee','leg','elbow','upArm']
    bendJnts = rig.ls('*_bend*_jnt')
    jntNum = len(rig.ls(bendJnts[0].replace('1_jnt','')+'*_jnt'))
    jntRadius = rig.getAttr(bendJnts[0]+'.radius')
    bendJntPos = [rig.xform(jnt,q = True,t = True,ws = True) for jnt in bendJnts]
    
    for i,jntpos in enumerate(bendJntPos):
        if(0 == i%jntNum):
            rig.select(cl = True)
        jointName = rig.joint(p = jntpos,n = bendJnts[i].replace('_jnt','_skinJnt'))
        rig.setAttr(jointName+'.radius',jntRadius)
        
       
        for newName in nameBends:
            if(newName+'_' in jointName):
                rig.rename(jointName , jointName.replace(newName+'_','_'+newName+'_'))

        
def SK_bodySkinJoint():
    filePath = tempfile.gettempdir()+'/PosFile.txt'
    newFile = open(filePath,'w')
    newFile.write(rig.getAttr('CharacterShape.pos'))
    newFile.close()
    readFile = open(filePath,'r')
    dbase = pickle.load(readFile)
    readFile.close()
    os.remove(filePath)
    allJnts = dbase[0]
    jntPos = dbase[1]
    jntOrient = dbase[2]
    jntParent = dbase[3]
    for i,jnt in enumerate(allJnts): 
        jntName = rig.joint(p = jntPos[i],n = jnt+'_TemSkinJoint')
        rig.setAttr(jntName+'.radius',0.5)
        rig.setAttr(jntName+'.jointOrientX',jntOrient[i][0])
        rig.setAttr(jntName+'.jointOrientY',jntOrient[i][1])   
        rig.setAttr(jntName+'.jointOrientZ',jntOrient[i][2])
        rig.select(cl = True)
        
    for i,jnt in enumerate(allJnts):
        if(jntParent[i][0]):
            if not ('Character' in jntParent[i][0]):
                rig.parent(jnt+'_TemSkinJoint',jntParent[i][0]+'_TemSkinJoint')
                

def SK_createPaintJoint():
    SK_skinBendJoint()
    SK_bodySkinJoint()
    
    allBodyJnt = rig.ls('*_TemSkinJoint')
    for jnt in allBodyJnt:
        if('_jnt_TemSkinJoint' in jnt):
            rig.rename(jnt,jnt.replace('_jnt_TemSkinJoint','_skinJnt'))
        if('_drv_TemSkinJoint' in jnt):
            rig.rename(jnt,jnt.replace('_drv_TemSkinJoint','_skinJnt'))
            
####parent obj
#  body parent
    waistJnts = rig.ls('waist*_skinJnt')
    neckJnts = rig.ls('neck*_skinJnt')
    clavicle1jnts = rig.ls('*_clavicle1_skinJnt')
    legs = rig.ls('*_leg_skinJnt')
    wrists = rig.ls('*_wrist_skinJnt')
    chestJnts = rig.ls('chest*_skinJnt')
    arms = rig.ls('*_upArm_skinJnt')
    
    chestJnts.sort()
    waistJnts.sort()
    neckJnts.sort()
    
    #bend parent
    jntBends = rig.ls('*_bend1_skinJnt')
    nameBends = ['knee','leg','elbow','upArm']
    for jntbend in jntBends:
       for name in nameBends:
           if('_'+name+'_' in jntbend):
               bendSplit = jntbend.split('_')
               bends =  "rig.select(rig.ls("+"'"+bendSplit[0]+'_'+name+'_'+'bend'+'*'+bendSplit[-1]+"'"+"))"
               bendsStr = compile(bends,'','exec')
               exec bendsStr
               selBends = rig.ls(sl = True)
               rig.select(cl = True) 
            
               selBends.sort()
               upJnt = selBends[0].replace('_bend1','')
               lowJnt = rig.listRelatives(upJnt,c = True)[0]
               rig.parent(selBends[0],upJnt)
               rig.parent(lowJnt,selBends[-1])           
    
    rig.delete(rig.ls('*_foot_outside_refer_TemSkinJoint'),rig.ls('*_foot_inside_refer_TemSkinJoint'),rig.ls('*_heel_skinJnt'))
    rig.select(cl = True)
        
    
    
