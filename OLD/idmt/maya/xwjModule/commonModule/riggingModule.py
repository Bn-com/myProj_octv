__author__ = 'xuweijian'

import maya.cmds as mc


class riggingModule():
    def copyBlendShapeWeight(self,orgVertex,targetVertex,index=0):
        obj=orgVertex.split('.')[0]
        #print 'obj:'+obj
        orgId=orgVertex.split('[')[1][:-1]
        #print 'orgId:'+orgId
        targetId=targetVertex.split('[')[1][:-1]
        #shape=mc.listRelatives(obj,s=1,c=1,ni=1)[0]
        #BSnode=mc.listConnections(shape,d=0,type='blendShape')[0]
        relativeNode=mc.listHistory(obj,lv=1)
        #print relativeNode
        BSnodes=[]
        for oneNode in relativeNode:
            if mc.nodeType(oneNode)=="blendShape":
                BSnodes.append(oneNode)
        #print BSnodes
        if BSnodes:
            if len(BSnodes)==1:
                BSnode=BSnodes[0]
                #mc.setAttr('%s.envelope'%BSnode,0)
                #print 'BSnode:'+BSnode
                #weightList=[]
                weight=''
                if index==0:
                    weight=mc.getAttr("%s.it[0].bw[%s]"%(BSnode,orgId))
                    mc.setAttr("%s.it[0].bw[%s]"%(BSnode,targetId),weight)
                    #weightList.append(baseWeight)
                else:
                    weight=mc.getAttr('%s.it[0].itg[%s].tw[%s]'%(BSnode,index-1,orgId))
                    mc.setAttr('%s.it[0].itg[%s].tw[%s]'%(BSnode,index-1,targetId),weight)

            else:
                mc.error('more than one blendshape')
        else:
                mc.error('object no blendshape node')


    def getBlendShapeWeightDict(self,obj):
        weightDict={}
        numVertex=mc.polyEvaluate(obj,v=1)
        ######get blendshape node###########
        relativeNode=mc.listHistory(obj,lv=1)
        BSnodes=[]
        for oneNode in relativeNode:
            if mc.nodeType(oneNode)=="blendShape":
                BSnodes.append(oneNode)
        ####################################
        if BSnodes:
            if len(BSnodes)==1:
                BSnode=BSnodes[0]
                i=0
                while i <numVertex:
                    baseWeight=mc.getAttr("%s.it[0].bw[%s]"%(BSnode,i))
                    tagWeight=mc.getAttr("%s.it[0].tw[%s]"%(BSnode,i))
                    WeightList=[]
                    WeightList.append(baseWeight)
                    if tagWeight:
                        if type(tagWeight)==type(''):
                            WeightList.append(tagWeight)
                        elif type(tagWeight)==type([]):
                            WeightList.extend(tagWeight)
                    weightDict[i]=WeightList
                    i+=1
            else:
                mc.error('more than one blendshape node')
        return weightDict



    def setWeightToSkin(self,dict,obj):
        mirrorJoint=mc.joint()


