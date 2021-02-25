# -*- coding: gbk -*-
import maya.cmds as rig


# -*- coding: gbk -*-
import maya.cmds as cmds
import maya.mel as mel
import sys
# print sys.argv[0]
# raise
def SL_GlobalScaleTool():    
    if cmds.window('SL_GlobalScale_W',ex=True):
        cmds.deleteUI('SL_GlobalScale_W')
          
    create=cmds.window(u'SL_GlobalScale_W',title="SL_GlobalScaleTool",iconName='shortName',w=80,h=50)
    cmds.columnLayout(adj=1)    
    cmds.text(l="[Select Master Ctrl] ",align="left")    

    cmds.button(l="--DO--",c='iimpsl_globalScale()',w=80,h=30,bgc=(0,0.6,0),annotation='select Master Ctrl,then Do')
    cmds.showWindow(create)

def sl_globalScale():
    #SQ= 'squashIKCurveInfoNormalize'
    M= rig.ls(sl=True)
    M='Master'
    #orgMain='Main'
    orgMainInfoNode= 'squashIKCurveInfoMainScale'
    sourse = rig.connectionInfo(orgMainInfoNode +'.input2X',sfd=True)
    orgMain = sourse.split('.')[0]
    
    InvScaleMD = cmds.createNode('multiplyDivide',n = 'InvScale_MD',ss = True)
    rig.disconnectAttr(orgMain+'.scaleY',orgMainInfoNode +'.input2X')
    #cmds.disconnectAttr(InvScaleMD+'.outputX',orgMainInfoNode +'.input2X')
    rig.connectAttr(M+'.scaleY',InvScaleMD +'.input1X',f=True)
    rig.connectAttr(orgMain+'.scaleY',InvScaleMD +'.input2X',f=True)
    rig.connectAttr(InvScaleMD+'.outputX',orgMainInfoNode +'.input2X',f=True)
    print 'f'
if __name__ == "__main__":
    SL_GlobalScaleTool()