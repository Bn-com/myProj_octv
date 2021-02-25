#-*- coding: gbk -*-
'''
Created on 2013-8-7

@author: zhaozhongjie
@contact:    power_zzj@163.com
@deffield    updated: Updated
'''

import maya.cmds as cmds
def disconnectAttr( source , type='', sourceDestOrBoth = 2):
    '''
    source = 'pSphere1' , source = 'pSphere1.tx'
    type = 'transform'
    sourceDestOrBoth = 0,1,2 (0=source , 1=dest , 2=both)
    usage:
    #    delete all type of 'transforms' from 'pSphere1.tx' :
        util.disconnectAttr('pSphere1.tx' , type = 'transform')
    #    delete all from 'pSphere1':
        util.disconnectAttr('pSphere1' )
    '''

#    query dest list of input:
    destAttrs = []
    if sourceDestOrBoth == '':
        destAttrs = cmds.listConnections( source , plugs=1 , type = type )
    elif sourceDestOrBoth == 0:
        destAttrs = cmds.listConnections( source , plugs=1 , type = type , source =1 , destination = 0)
    elif sourceDestOrBoth == 1:
        destAttrs = cmds.listConnections( source , plugs=1 , type = type , source =0 , destination = 1)
    elif sourceDestOrBoth == 2:
        destAttrs = cmds.listConnections( source , plugs=1 , type = type , source =1 , destination = 1)    

#    query the source's attribute from dest's attribute
    for dest in destAttrs:
        connections = cmds.listConnections( dest , plugs=1)

        for c in connections:
#    query if the connections is the same node of source
            if isTheSameNode(c , source):
                if cmds.isConnected( c , dest ):
                    cmds.disconnectAttr( c , dest )
                    print "Result:    Disconnect %s from %s." %(c,dest)
                elif cmds.isConnected( dest , c ):
                    cmds.disconnectAttr( dest , c )
                    print "Result:    Disconnect %s from %s." %(dest,c)
        
def isTheSameNode(nodeA,nodeB):    
    '''
    usage:
    #    query if nodeA and nodeB is the same node :
        util.isTheSameNode('pSphere1.tx' , '|XXX|pSphere1')
    #    Result:    1
    '''    
    longA = cmds.ls(nodeA , long=1)[0]
    longB = cmds.ls(nodeB , long=1)[0]
    
    if longA in longB  or longB in longA:
        return True
    else:
        return False
    
    
    
    