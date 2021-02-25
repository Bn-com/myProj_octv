# -*- coding: utf-8 -*-
import maya.cmds as mc
import idmt.maya.camera
from pymel.core import *

def cam_far():
    if idmt.maya.camera.CheckPosition() == True:
        mc.confirmDialog(message = u'相机位置合格', button = ['OK'])
    else:
        cam_farWin()



def cam_farWin():
    if mc.window('cam_fixFar',exists = True):
    	mc.deleteUI('cam_fixFar')
    	
    mc.window('cam_fixFar', title = u'ZoomWhiteDolphin -- >手动修正相机太远的问题', width = 330, height = 180, sizeable = False)
    mc.columnLayout(rowSpacing=2, columnAttach = ['both',5],columnWidth = 330)
    mc.text( label='' )
    mc.button(label = u'1.修正相机位置', c = 'cam_backToZero()')
    
    mc.separator(h  = 50, st = 'in')
    mc.columnLayout(co = ['left',-80])
    mc.floatFieldGrp('moveTranlate', numberOfFields=3, label='translate',  value1=0.0, value2=0.0, value3=0.0, precision = 5)
    mc.setParent( '..' )
    
    mc.text( label='' )
    mc.button(label = u'2.手动修正位置(先选择要移动的物体)', c = 'cam_backToZeroBySelf()')
    mc.text( label='' )
    mc.showWindow( 'cam_fixFar' )

def cam_backToZeroBySelf():
    x = mc.floatFieldGrp('moveTranlate', q = True, value1 = True)
    y = mc.floatFieldGrp('moveTranlate', q = True, value2 = True)
    z = mc.floatFieldGrp('moveTranlate', q = True, value3 = True)
    sels = mc.ls(sl = True)
    
    
    for sel in sels:
        n_tx = mc.getAttr(sel + '.translateX') - x
        n_ty = mc.getAttr(sel + '.translateY') - y
        n_tz = mc.getAttr(sel + '.translateZ') - z
        
            
        mc.setAttr(sel + '.translateX',n_tx) 
        mc.setAttr(sel + '.translateY',n_ty) 
        mc.setAttr(sel + '.translateZ',n_tz) 

        key_channels = mc.keyframe( sel,  query=True,  name=True)
        if key_channels:
            for channel in key_channels:
                if channel.find('_translateX') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = x * -1)
                   
                if channel.find('_translateY') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = y * -1)
                    
                if channel.find('_translateZ') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = z * -1)

def cam_backToZero():
    cams = ls(type = 'camera')
    cam = ''
    camGrp = ''
    for ca in cams:
        if ca.find('cam_') > -1:
            cam = ca.getParent()
            camGrp = cam.root()
            cam = cam.name()
            camGrp = camGrp.name()
        
               
   
    cam_ctrls = mc.ls('*:mov_ctrl')
    toRemove = []
    for ctrl in cam_ctrls:

        m_ctrl = PyNode( ctrl ).listConnections( s = True ,d = False,)
        
        remove = True
        
        for cc in m_ctrl:
            if cc.nodeType() == 'parentConstraint' or cc.nodeType() == 'pointConstraint':
                toRemove.append(ctrl)
                #cam_ctrls.remove(ctrl)
                remove = False
                break
        if remove:
            constrains = PyNode( ctrl ).getParent().listConnections( s = True ,d = False,)
            for c in constrains:
                if c.nodeType() == 'parentConstraint' or c.nodeType() == 'pointConstraint':
                    toRemove.append(ctrl)
                    #cam_ctrls.remove(ctrl)
                    break
    
    for r in toRemove:
        cam_ctrls.remove(r)
    
    cam_master = mc.ls('*:Master')
    allToShift = cam_ctrls + cam_master
    
    if camGrp:
        allToShift.append(camGrp)
    else:
        allToShift.append(cam)
        
    mov_ctrls = list(set(allToShift))
    
    trans = mc.xform(cam,q = True , ws = True, a = True, t =True )
    tx = trans[0] #mc.getAttr(cam + '.translateX')
    ty = trans[1] #mc.getAttr(cam + '.translateY') 
    tz = trans[2] #mc.getAttr(cam+ '.translateZ')
    
    mc.floatFieldGrp('moveTranlate', e = True, value1 = tx, value2 = ty, value3 = tz )
    for mov in mov_ctrls:
        
        n_tx = mc.getAttr(mov + '.translateX') - tx
        n_ty = mc.getAttr(mov + '.translateY') - ty
        n_tz = mc.getAttr(mov + '.translateZ') - tz
        
        
        if PyNode( mov ).getShape():
            if PyNode( mov ).getShape().nodeType() == 'camera':
                mc.setAttr(mov + '.translateX', lock = False)
                mc.setAttr(mov + '.translateY', lock = False)
                mc.setAttr(mov + '.translateZ', lock = False)
        
        
        mc.setAttr(mov + '.translateX', n_tx)
        mc.setAttr(mov + '.translateY', n_ty)
        mc.setAttr(mov + '.translateZ', n_tz)
        
        if PyNode( mov ).getShape():
            if PyNode( mov ).getShape().nodeType() == 'camera':
                mc.setAttr(mov + '.translateX', lock = True)
                mc.setAttr(mov + '.translateY', lock = True)
                mc.setAttr(mov + '.translateZ', lock = True)
        
    
        key_channels = mc.keyframe( mov,  query=True,  name=True)
        if key_channels:
            for channel in key_channels:
                if channel.find('_translateX') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = tx * -1)
                   
                if channel.find('_translateY') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = ty * -1)
                    
                if channel.find('_translateZ') > -1:
                    mc.select(cl = True)
                    frames = mc.keyframe( channel,  query=True,  timeChange=True)
                    mc.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = tz * -1)
             
