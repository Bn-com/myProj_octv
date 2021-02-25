# -*- coding: utf-8 -*-
import os
import sys
import maya.cmds as mc
import maya.mel as mel
import idmt.maya.camera
from  idmt.maya.py_common.cam_far  import *

def zorro_getAudioAndCam( audio = True):
    allCamA = mc.ls(type = 'camera')
    sn = mc.file( q = True, sceneName = True, shortName = True)
    snEP = sn[0:2].upper()
    
    if snEP == 'VV':
        snEP = sn[3:5].upper()
        audioName = sn[3:14]
        camSn = snEP + sn[6:9]
        camShot = sn[10:14]
        camFileName = sn[3:14] + '.mb'
        path = 'Z:/Projects/Zorro/Reference/Animation_production/'
    
        eps = os.listdir('Z:/Projects/Zorro/Reference/Animation_production/005_CF_Ylva_in_Charge/Layout_exports/CF010/0230/v001/camera/')
        eps = os.listdir(path)
    
        for ep in eps:
            ep.upper()
            if ep.find(snEP) > -1:
                
                if audio:
                    audioPath = path + ep + '/Audio/' + audioName + '.wav'
                    if os.path.isfile(audioPath):
                        impAudio = 'doSoundImportArgList ("1", {"' + audioPath + '","0.0"})'
                        audioNode = mel.eval(impAudio)
                        offset = mel.eval('idmtProject -timeLine -echo off')
                        mc.setAttr( audioNode + '.offset', offset[0])
                        print '======================   audio import done !!!!!   ========================='
                    else:
                        print ''
                        print 'this path is not correct, pls check it -----> ' , audioPath
                    #================================================
    
                camPath = path + ep + '/Layout_exports/' + camSn + '/' + camShot + '/v001/camera/' + camFileName
                if os.path.isfile(camPath):
                    mc.file (camPath, i = True, type = "mayaBinary", ra = True, loadReferenceDepth = "all")
                    
                    cs = mc.ls(sn[3:14] + '*:CAM')
    
                    for c in cs:
                        mc.setAttr (c + '.tx', lock = True)
                        mc.setAttr (c + '.ty', lock = True)
                        mc.setAttr (c + '.tz', lock = True)
                        mc.setAttr (c + '.rx', lock = True)
                        mc.setAttr (c + '.ry', lock = True)
                        mc.setAttr (c + '.rz', lock = True)
                        mc.setAttr (c + '.sx', lock = True)
                        mc.setAttr (c + '.sy', lock = True)
                        mc.setAttr (c + '.sz', lock = True)
        
        
                    print '======================   camera  import done !!!!!   =========================',
                    if idmt.maya.camera.CheckPosition() == True:
                        mc.confirmDialog(message = u'相机位置合格', button = ['OK'])
                    else:
                        cam_farWin()
    
                else:
                    print 'this path is not correct, pls check it -----> ' , camPath
                    print ''
                    print u'没能找到正确的文件，请打开script editor 查看更多信息，或联系TD！！！！！！',
                break
                
                
                
    allCamB = mc.ls(type = 'camera')
    
    cam = list( set(allCamB) - set(allCamA))
    
    
    mc.setAttr(cam[0] +'.hfa', lock = True)
    mc.setAttr(cam[0] +'.vfa', lock = True)
    mc.setAttr(cam[0] +'.fl', lock = True)
    mc.setAttr(cam[0] +'.lsr', lock = True)
    mc.setAttr(cam[0] +'.fs', lock = True)
    mc.setAttr(cam[0] +'.fd', lock = True)
    mc.setAttr(cam[0] +'.sa', lock = True)
    mc.setAttr(cam[0] +'.coi', lock = True)
    
    tran = mc.pickWalk(cam[0], d = 'up')
    mc.setAttr(tran[0] +'.tx', lock = True)
    mc.setAttr(tran[0] +'.ty', lock = True)
    mc.setAttr(tran[0] +'.tz', lock = True)
    mc.setAttr(tran[0] +'.rx', lock = True)
    mc.setAttr(tran[0] +'.ry', lock = True)
    mc.setAttr(tran[0] +'.rz', lock = True)
    mc.setAttr(tran[0] +'.sx', lock = True)
    mc.setAttr(tran[0] +'.sy', lock = True)
    mc.setAttr(tran[0] +'.sz', lock = True)



