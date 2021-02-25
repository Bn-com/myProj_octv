import maya.cmds as cmds
def edo_connectSoftModCtrlEvalute(attr,list):
    #attr='Facial_CTRL_FRAME.facialSecondaryCtrl'
    #list=cmds.ls(sl=1)
    if list==None or list==[]:
        return False
    for l in list:
        #l=list[1]
        if cmds.nodeType(l)=='softModHandle':
            sfd=cmds.listConnections(l+'.softModTransforms[0]',s=0,d=1)
            if sfd==[] or sfd==None:
                return False
            if cmds.nodeType(sfd[0])=='softMod':
                print 'connect ... '+attr+' ... to ... '+sfd[0] 
                cmds.connectAttr(attr,sfd[0]+'.envelope',f=1)