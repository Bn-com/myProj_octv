# -*- coding: utf-8 -*-
__author__ = 'chenjiawei'
__date__	= '2016-05-24'
import maya.cmds as mc
import maya.mel as mel
def xiong_window():
  if mc.window('Aanimation_window', exists=True):
     mc.deleteUI('Aanimation_window', window=True)

  AanimationWindow = mc.window('Aanimation_window',title="animation_Tool", iconName='Short Name', widthHeight=(255, 100))
  mc.columnLayout( adjustableColumn=True)
  mc.text ( label=u'先选择带动画对象，在加选被传递的对象' )
  mc.button('fir',w=200,bgc=[1,0,0],l=u'对象定位',ann='',c='trance_animation_testA.XIONG_Loc_worldSpace()')
  mc.button('sec',w=200,bgc=[1,0,0],l=u'传递动画曲线位置动态',ann='',c='XIONG_animation()')
  mc.button( label='Close',c=('XIONG_DelWindow()'))
  mc.setParent( '..' )
  mc.showWindow( AanimationWindow )


def XIONG_Loc_worldSpace():
    selCtrl=mc.ls( selection=True )
    ctrFir=mc.select(selCtrl[0],r=1)
    ctrSEC=mc.select(selCtrl[1],tgl=1)
    COS=mc.parentConstraint(weight=1)
    mc.select(cl=1)
    bb=mc.select(COS)
    mc.Delete(bb)
def XIONG_animation():
    selCtrlT=mc.ls( selection=True )
    ctrFirB=mc.select(selCtrlT[0],r=1)
    ctrSECB=mc.select(selCtrlT[1],tgl=1)
    COST=mc.parentConstraint( mo=1,weight=1)
    mc.select(cl=1)

    time = mc.keyframe(selCtrlT[0], q=1, tc=1)
    #print time
    newTime = list(set(time))
    newTime.sort(key=time.index)
    mc.setKeyframe( selCtrlT[1], t=[newTime[0]])

    name=selCtrlT[1]+'.blendParent1'
    #print name
    mc.setAttr(name, 1,)
    #print newTime
    for BB in newTime:
      mc.currentTime (BB)
      mc.setKeyframe( selCtrlT[1], t=[BB])
    bb=mc.select(COST)
    mc.Delete(bb)
def XIONG_DelWindow():
  delw= mc.deleteUI('Aanimation_window', window=True)