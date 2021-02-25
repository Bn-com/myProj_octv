__author__ = 'xuweijian'

import maya.cmds as mc

class modelModule():
    def getClosetVertex(self,shape,pos=[0,0,0]):
        if mc.nodeType(shape)=='mesh':
            #mc.select("%s.vtx[*]"%shape)
            numVertex=mc.polyEvaluate(shape,v=1)
            closetVertex='%s.vtx[0]'%shape
            minDistance=9999
            for i in range(numVertex):
                vertexPos=mc.xform('%s.vtx[%s]'%(shape,i),q=1,t=1,ws=1)
                #distance=math.sqrt(vertexPos[0]-pos[0])+math.sqrt(vertexPos[1]-pos[1])+math.sqrt(vertexPos[2]-pos[2])
                distance=(vertexPos[0]-pos[0])*(vertexPos[0]-pos[0])+(vertexPos[1]-pos[1])*(vertexPos[1]-pos[1])+(vertexPos[2]-pos[2])*(vertexPos[2]-pos[2])
                if distance<minDistance:
                    minDistance=distance
                    closetVertex='%s.vtx[%s]'%(shape,i)
            return [closetVertex,minDistance]


    def getShapeCenterPos(self,obj):
        mc.select(obj)
        print obj
        cluster=mc.cluster(n='tempCluster',rel=True )
        pos=mc.xform(cluster[1],q=1,a=1,sp=1,ws=1)
        mc.delete(cluster)
        return pos
        #print '---'




##############################################
    def findMirrorVertex(self,vertex,plane='ZY',org=False):
        obj=vertex.split('.')[0]
        vertexId=vertex.split('[')[1][:-1]
        objshape=''
        objtr=''

        objAxesPos=[]
        vertexPos=[]

        if mc.nodeType(obj)=='mesh':
            objshape=obj
            objtr=mc.listRelatives(obj,p=1,type='transform')
        elif mc.listRelatives(obj,c=1,shapes=1):
            if org:
                shapes=mc.listRelatives(obj,c=1,shapes=1)
                nishape=mc.listRelatives(obj,c=1,shapes=1,ni=1)
                objshape=list(set(shapes).difference(set(nishape)))[0]
            else:
                objshape=mc.listRelatives(obj,c=1,shapes=1,ni=1)[0]
            objtr=obj
        else:
            mc.error('obj no shape')

        objAxesPos=self.getShapeCenterPos(obj)
        vertexPos=mc.xform('%s.vtx[%s]'%(objshape,vertexId),q=1,t=1,ws=1)


        if plane=='ZY':
            targetVertexPos=[(vertexPos[0]-objAxesPos[0])*-1+objAxesPos[0],vertexPos[1],vertexPos[2]]
        elif plane=='XY':
            targetVertexPos=[vertexPos[0],vertexPos[1],(vertexPos[2]-objAxesPos[2])*-1+objAxesPos[2]]
        target=self.getClosetVertex(objshape,targetVertexPos)
        return target

    def getHalfVertex(self,obj,plane='ZY'):
        if mc.nodeType(obj)=='mesh':
            shape=obj
        else:
            shape=mc.listRelatives(obj,c=1,shapes=1)[0]
        if mc.nodeType(shape)=='mesh':
            objAxesPos=mc.xform(obj,q=1,t=1,ws=1)
            numVertex=mc.polyEvaluate(shape,v=1)
            #mc.select("%s.vtx[*]"%shape)
            halfOfVertex=[0,1]
            halfOfVertex1=[]
            halfOfVertex2=[]
            for i in range(numVertex):
                vertex='%s.vtx[%s]'%(obj,i)
                vertexPos=mc.xform(vertex,q=1,t=1,ws=1)
                if plane=='XY':
                    if vertexPos[2]-objAxesPos[2]>0.001:
                        halfOfVertex1.append(vertex)
                    elif vertexPos[2]-objAxesPos[2]<-0.001:
                        halfOfVertex2.append(vertex)
                elif plane=='ZY':
                    if vertexPos[0]-objAxesPos[0]>0.001:
                        halfOfVertex1.append(vertex)
                    elif vertexPos[0]-objAxesPos[0]<-0.001:
                        halfOfVertex2.append(vertex)
                halfOfVertex[0]=halfOfVertex1
                halfOfVertex[1]=halfOfVertex2
            return halfOfVertex



