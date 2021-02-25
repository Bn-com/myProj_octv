import maya.cmds as cmds
def edo_ConnectAllMissCacheBeModelRename():
    missobj=cmds.ls(sl=1)
    for m in missobj:
        edo_ConnectMissCacheBeModelRename(m)
def edo_ConnectMissCacheBeModelRename(missCacheObj):
    #missCacheObj='tj_c001001Jerry_2:HCO_body_'
    sp=missCacheObj.split(':')
    nnsname=sp[len(sp)-1]
    sws=cmds.ls(type='historySwitch')
    for s in sws:
        #s=sws[0]
        dr=cmds.listConnections(s+'.outputGeometry[0]',s=0,d=1,type='reference')
        if dr==None:
            continue
        so=cmds.listConnections(s,s=1,d=0,type='cacheFile')
        if len(so)>0:
           sourcenode=so[0]
           i=0
           c=cmds.getAttr(sourcenode+'.channel['+str(i)+']')
           if nnsname in c:
               shapes=cmds.listRelatives(missCacheObj,s=1,pa=1,ni=1)
               if shapes==None or shapes==[]:
                   continue
               shape=shapes[0]
               cmds.connectAttr(s+'.outputGeometry[0]',shape+'.inMesh')
               return True
           while not c==None:
               c=cmds.getAttr(sourcenode+'.channel['+str(i)+']')
               if nnsname in c:
                   shapes=cmds.listRelatives(missCacheObj,s=1,pa=1,ni=1)
                   if shapes==None or shapes==[]:
                       continue
                   shape=shapes[0]
                   cmds.connectAttr(s+'.outputGeometry[0]',shape+'.inMesh',f=1)
                   return True
               i+=1
               print c