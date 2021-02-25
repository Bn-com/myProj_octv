# -*- coding: utf-8 -*-
import os
import re
import pymel.core as pm

def csl_fixedcamfar():

    bigScs = ['s010013CityWarZone','s011010MountainRoad','s007005SnowmountainAndGobi','s008004SnowRange']
    allRef = pm.system.listReferences()

    isMove = False
    unloadFiles = []

    for reff in allRef:
        if not reff.isLoaded():
          unloadFiles.append(reff)
          reff.load()


    for ref in allRef:
        for sc in bigScs:
           if str(ref).find(sc) > -1:
                isMove = True
                break
                 
    if isMove:
        
        s = pm.ls(type = 'transform')
        rootList = []
        for ss in s:
            r = ss.root()
            if r not in ['persp','top','front','side']:
                rootList.append( r)
            
        sels = list(set(rootList))

        #sels =  pm.ls(sl = True)
            
        sn = os.path.basename(pm.system.sceneName()).split('_')
        baseCamName = '_'.join(['cam',sn[1],sn[2],sn[3]])
          
        cams = pm.ls(type = 'camera')
        cam = ''

        for ca in cams:
           
            if re.search(baseCamName, ca.name(),re.IGNORECASE):
                cam = ca.getParent()
                print cam
                
           
        trans = pm.xform(cam,q = True , ws = True, a = True, t =True )
        x = trans[0] #pm.getAttr(cam + '.translateX')
        y = trans[1] #pm.getAttr(cam + '.translateY') 
        z = trans[2] #pm.getAttr(cam+ '.translateZ')
        for sel in sels:

            if sel.attr('tx').isLocked() or sel.attr('ty').isLocked() or sel.attr('tz').isLocked():
                papa = sel.getParent()
                if papa:
                    sel = papa
                else:
                    sel = pm.group(sel)

            w = pm.xform(sel,q = True, a = True, ws = True, t = True)
            o = sel.translateZ.get()
            mlt = 1
            if w[2] != o :
                mlt = w[2] / o
            
            mtx = x / mlt
            mty = y / mlt
            mtz = z / mlt
            
            n_tx = sel.translateX.get() - mtx
            n_ty = sel.translateY.get() - mty
            n_tz = sel.translateZ.get() - mtz
            
                
            sel.translateX.set(n_tx) 
            sel.translateY.set(n_ty) 
            sel.translateZ.set(n_tz) 

            key_channels = pm.keyframe( sel,  query=True,  name=True)
            if key_channels:
                for channel in key_channels:
                    if channel.find('_translateX') > -1:
                        pm.select(cl = True)
                        frames = pm.keyframe( channel,  query=True,  timeChange=True)
                        pm.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = mtx * -1)
                       
                    if channel.find('_translateY') > -1:
                        pm.select(cl = True)
                        frames = pm.keyframe( channel,  query=True,  timeChange=True)
                        pm.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = mty * -1)
                        
                    if channel.find('_translateZ') > -1:
                        pm.select(cl = True)
                        frames = pm.keyframe( channel,  query=True,  timeChange=True)
                        pm.keyframe(channel,e = True, iub = True, r = True, o = 'over', vc = mtz * -1)



    for un in unloadFiles:
        un.unload()
