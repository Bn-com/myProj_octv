# -*- coding: gbk -*-

#create a ctrl
import maya.cmds as cmds
import maya.mel as mel
import sys
def ctrlikfk():

    
    if cmds.window('Circle_W',ex=True):
        cmds.deleteUI('Circle_W')
          
    create=cmds.window(u'Circle_W',title="Circle_ctrl",iconName='shortName',w=150,h=100)
    cmds.columnLayout(adj=1)
    cmds.text(l="inputCtrlName ",align="left")

    myName=cmds.textField('input',tx='null',fn='fixedWidthFont',bgc=(0,0,0),w=150,h=30)
    cmds.button(l="cricle",c='circle_C()',w=150,h=30)
    
    cmds.showWindow(create)
        
def circle_C():
    name=cmds.textField('input',q=True,tx=True)
    cr=cmds.circle(n='fkCtrl_'+name,r=1.5)
    mel.eval('DeleteHistory')
    grpfk=cmds.group(n='GRPfkCtrl_'+name)
    cmds.pickWalk(d='down')
    s=cmds.ls(sl=True)
    print s
    cmds.setAttr(s[0]+'Shape'+".overrideEnabled",int(1))
    cmds.setAttr(s[0]+'Shape'+".overrideColor",6)
         
    crik=cmds.circle(n='ikCtrl_'+name,r=1)
    grpik=cmds.group(n='GRPikCtrl_'+name)
    cmds.pickWalk(d='down')
    sik=cmds.ls(sl=True)
    cmds.joint(n='ikJnt_'+name,radius=0.1)
    print sik
    cmds.setAttr(sik[0]+'Shape'+".overrideEnabled",int(1))
    cmds.setAttr(sik[0]+'Shape'+".overrideColor",13)
        
    cmds.select(grpfk)
    crobj=cmds.pickWalk(d='down')
    cmds.parent(grpik,crobj)
#-----------boxCtrl
def box_C():
    box=cmds.curve(d=1,p= [(-0.5,0.5, 0.5), ( 0.5, 0.5, 0.5) ,( 0.5, 0.5 ,-0.5),
(-0.5 ,0.5 ,-0.5 ),( -0.5 ,0.5 ,0.5),( -0.5 ,-0.5 ,0.5 ),( 0.5 ,-0.5, 0.5 ),(0.5, 0.5 ,0.5 ),
( 0.5, 0.5 ,-0.5) ,(0.5 ,-0.5 ,-0.5 ) ,(0.5 ,-0.5 ,0.5 ),( -0.5, -0.5 ,0.5 ),( -0.5, -0.5, -0.5 ),
( 0.5, -0.5, -0.5 ),( 0.5 ,0.5, -0.5),( -0.5, 0.5, -0.5 ),( -0.5, -0.5, -0.5 )],k=[0,1,2,3,4,5,6,7
,8,9,10,11,12,13,14,15,16])
    cmds.select(box)
    boxN=cmds.rename('boxCtrl_#')
    cmds.setAttr(boxN+".overrideEnabled",1)
    cmds.setAttr(boxN+".overrideColor",6)
    return boxN

    
def diamond_C():
    dm=cmds.curve(d=1,p=[(0,1,0),(0,0,1),(0,-1,0),(0,0,-1),(0,1,0),(1,0,0),(0,-1,0),
(-1,0,0),(0,1,0),(1,0,0),(0,0,1),(-1,0,0),(0,0,-1),(1,0,0)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13])
    cmds.select(dm)
    dmN= cmds.rename ('diamCtrl_#')
    cmds.setAttr(dmN+".overrideEnabled",1)
    cmds.setAttr(dmN+".overrideColor",13)
    return dmN

def Door_C():
    DoorCtrl=cmds.curve(d=1,p=[(-0.0934356, 0, 0.883865),(0 ,0.23336 ,0.453394),(0,0.0783723 ,0.453394),(0.0358587, 0.0783723 ,0.418882),
    ( 0.0661714 ,0.0783723,0.320598),(0.0864256 ,0.0783723 ,0.173506 ),( 0.0935382 ,0.0783723 ,0),(0.0864256 ,0.0783723 ,-0.173506),
    ( 0.0661714 ,0.0783723,-0.320598),(0.0358587,0.0783723 ,-0.418882),( 0,0.0783723 ,-0.453394),(0 ,0.23336,-0.453394), (-0.0934356 ,0,-0.883865),
    (0,-0.23336,-0.453394),(0,-0.0783723,-0.453394),(0.0358587,-0.0783723,-0.418882),(0.0661714,-0.0783723,-0.320598),(0.0864256,-0.0783723,-0.173506),
    (0.0935382 ,-0.0783723 ,0),(0.0864256 ,-0.0783723 ,0.173506),(0.0661714, -0.0783723, 0.320598),(0.0358587 ,-0.0783723 ,0.418882),(0 ,-0.0783723, 0.453394),
    (0, -0.23336, 0.453394),(-0.0934356,0,0.883865)],k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    cmds.select(DoorCtrl)
    DoorCtrlN=cmds.rename('DoorCtrl_#')
    cmds.setAttr(DoorCtrlN+".overrideEnabled",1)
    cmds.setAttr(DoorCtrlN+".overrideColor",17)
    return DoorCtrlN
    
def Ball_C():
    BallCtrl=cmds.curve(d=1,p =[(0, 0.5, 0 ),(0 ,0.46194 ,0.191341),( 0, 0.353553 ,0.353553),(  0 ,0.191341 ,0.46194),(0 ,0 ,0.5 ),( 0 ,-0.191341, 0.46194),( 0, -0.353553, 0.353553 ),( 0 ,-0.46194, 0.191341 ),
    ( 0 ,-0.5 ,0 ),( 0, -0.46194 ,-0.191341),( 0, -0.353553, -0.353553 ),( 0, -0.191341, -0.46194),( 0, 0 ,-0.5 ),( 0 ,0.191341, -0.46194),( 0, 0.353553, -0.353553 ),( 0, 0.46194 ,-0.191341 ),
    ( 0 ,0.5, 0 ),( 0.191341, 0.46194 ,0),( 0.353553, 0.353553 ,0 ),( 0.46194, 0.191341, 0 ),( 0.5 ,0 ,0 ),( 0.46194 ,-0.191341, 0 ),( 0.353553 ,-0.353553, 0 ),( 0.191341, -0.46194 ,0 ),( 0 ,-0.5, 0),
    (-0.191341, -0.46194, 0 ),( -0.353553, -0.353553, 0),( -0.46194, -0.191341, 0),( -0.5, 0, 0 ),( -0.46194 ,0 ,-0.191341 ),( -0.353553 ,0 ,-0.353553 ),( -0.191341, 0 ,-0.46194 ),( 0, 0 ,-0.5 ),(0.191341,
     0 ,-0.46194 ),( 0.353553, 0 ,-0.353553 ),( 0.46194, 0 ,-0.191341 ),( 0.5, 0 ,0 ),(0.46194 ,0 ,0.191341 ),( 0.353553 ,0 ,0.353553 ),(0.191341, 0, 0.46194 ),(0, 0, 0.5 ),( -0.191341, 0 ,0.46194 ),
     ( -0.353553, 0, 0.353553 ), (-0.46194, 0 ,0.191341 ),(-0.5 ,0 ,0 ),(-0.46194, 0.191341, 0 ),( -0.353553, 0.353553, 0 ),( -0.191341 ,0.46194 ,0 ),( 0 ,0.5 ,0)], 
    k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48]);
    cmds.select(BallCtrl)
    BallCtrlN=cmds.rename('BallCtrl_#')
    cmds.setAttr(BallCtrlN+".overrideEnabled",1)
    cmds.setAttr(BallCtrlN+".overrideColor",13)
    return BallCtrlN

def Pivot_C():    
    pivotCtrl=cmds.curve(d=1,p=[(-1.00632,1.986874,0),(0.0134381,2.960697,0),(1.005635,1.977687,0),(0.0134381,2.960697,0),
(0,0,0),(3 ,0, 0),( 2 ,0 ,-1 ),( 3, 0, 0 ),( 2 ,0, 1 ),( 3,0,0 ),( 0,0,0 ),(0,0,3 ),(1,0, 2 ),(0,0,3),(-1,0,2 )],
k=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]);
    cmds.select(pivotCtrl)
    pivotCtrlN=cmds.rename('pivotCtrl_#')
    cmds.setAttr(pivotCtrlN+".overrideEnabled",1)
    cmds.setAttr(pivotCtrlN+".overrideColor",16)
    return pivotCtrlN
if __name__ == "__main__":
    print 'TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ===='
    print 'TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ====TEST  TD  ===='