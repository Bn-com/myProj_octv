#-*- coding: utf-8 -*-
import maya.cmds as rig
import os
import pickle
import tempfile

def SK_creatConDefaultPos(savePos = True):
    filePath = tempfile.gettempdir()+'/PosFile.txt'
    if savePos:
        cons = rig.sets('bodySet',q = True)
        posData = []
        for con in cons:
            temPosData = []
            attrs = rig.listAttr(con,k = True)
            kattrs = rig.listAttr(con,cb = True)
            
            if kattrs:
                attrs.extend(kattrs)
            
            for attr in attrs:
                temAttrPosData = []
                datainfo = rig.getAttr(con+'.'+attr)
                temAttrPosData.append(con+'.'+attr)
                temAttrPosData.append(datainfo) 
                temPosData.append(temAttrPosData)                
            posData.append(temPosData) 
            
        newFile = open(filePath,'w')
        pickle.dump(posData,newFile)
        newFile.close()
        getData = open(filePath,'r')
        getDate = getData.read()
        getData.close()
        if not (rig.attributeQuery('conPos',node = 'CharacterShape',ex = True)):
            rig.addAttr('CharacterShape',ln = 'conPos',dt = 'string')
        rig.setAttr('CharacterShape.conPos',getDate,type = 'string')
        os.remove(filePath)    
        
    else:
        selControlers = rig.ls(sl = True)
        if selControlers:
            for slCon in selControlers:
                temPrefix = slCon.split(':')
                if (1 == len(temPrefix)):
                    prefix = ''
                else:
                    prefix = slCon.replace(temPrefix[-1],'')  
                          
                newFile = open(filePath,'w')
                newFile.write(rig.getAttr(prefix+'CharacterShape.conPos'))
                newFile.close()
                readFile = open(filePath,'r')
                posData = pickle.load(readFile)
                readFile.close()
                os.remove(filePath)
                for data in posData:
                    for attrdata in data:
                        rig.setAttr(prefix+attrdata[0],attrdata[1])     
                
            
    
