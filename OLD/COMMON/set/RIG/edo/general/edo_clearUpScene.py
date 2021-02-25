import maya.cmds as cmds
#edo_clearUpScenes()
def edo_clearUpScenes(types=['groupParts','groupId','polyNormal']):
    cmds.undoInfo(state=False)
    for t in types:
        #t=types[0]
        Nodes=cmds.ls(type=t)
        if not Nodes:
            cmds.undoInfo(state=True)
            return False
        print t+' ... total is ... '+str(len(Nodes))
        clearNodes=[]
        for n in Nodes:
            #n=Nodes[1]
            out=cmds.listConnections(n,s=0,d=1)
            if not out:
                #print 'delete   ...  '+n
                #cmds.delete(gp)
                #print 'serching no output groupId'
                clearNodes.append(n)
                cmds.delete(n)
                if len(clearNodes)%1000==0 and len(clearNodes)>0:
                    print str(len(clearNodes))
            else:
                if t=='groupId':
                    #print 'serching shadding groupId'
                    isshadding=0
                    for o in out:
                        #o=out[1]
                        if cmds.nodeType(o)=='shadingEngine':
                            isshadding=1
                        else:
                            isshadding=0
                            break
                    if isshadding==1:
                        clearNodes.append(n)
                        cmds.delete(n)
                    if len(clearNodes)%1000==0 and len(clearNodes)>0:
                        print str(len(clearNodes))
        cl=len(clearNodes)
        #if cl>0:
        #    cmds.delete(clearNodes)
        print 'cleared ... '+str(cl)+'  of  '+t+'  ...  nodes'
    cmds.undoInfo(state=True)
    return True