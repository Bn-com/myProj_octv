# -*- coding: utf-8 -*-
# Created on 2017
# @author: shenkang

import maya.cmds as mc
import maya.mel as mel

class sk_assemblyTools(object):

    def __init__(self):
        pass

    def switchReps(self,targetKey):
        needArNodes = []
        checkNodes = mc.ls(sl=1,l=1)
        if not checkNodes:
            return
        targetFormat = ''
        if targetKey in ['cache','gpu']:
            targetFormat = '.abc'
        if targetKey in ['rgb','clr']:
            targetFormat = '.mb'

        for checkNode in checkNodes:
            arNode = self.getArFromSel(checkNode)
            if not arNode:
                continue
            if arNode not in needArNodes:
                needArNodes.append(arNode)

        for arNode in needArNodes:
            modeNow = mc.assembly(arNode,q=1,active = 1)
            modePre = modeNow[:-1*(len(modeNow.split('_')[-1]))]
            modeReal = '%s%s%s'%(modePre,targetKey,targetFormat)
            if modeReal != modeNow:
                mc.assembly(arNode,e=1,active = modeReal)


    def getArFromSel(self,checkObj):
        needNode = ''
        assemblyNode = 'assemblyReference'
        pNode = checkObj
        checkInfos = checkObj.split('|')
        for num in range(len(checkInfos)-1):
            checkType = mc.nodeType(pNode)
            if checkType in [assemblyNode]:
                needNode = pNode
                break
            else:
                pNode = mc.listRelatives(pNode,p=1,f=1)
                if not pNode:
                    break
                else:
                    pNode = pNode[0]


        '''
        if checkType in [assemblyNode]:
            needNode = checkObj
        else:
            while checkType not in [assemblyNode]:
                checkGrp = mc.listRelatives(checkObj,p=1,f=1)
                if not checkGrp:
                    needNode = ''
                    break
                checkGrp = checkGrp[0]
                checkType = mc.nodeType(checkGrp)
                needNode = checkGrp
        '''
        return needNode


