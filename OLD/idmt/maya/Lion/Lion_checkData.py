# -*- coding: utf-8 -*-

'''
Created on 2015-11-16

@author: liangyu
'''

import maya.cmds as mc
import os
import maya.mel as mel

class Lion_meshData(object):
    def __init__(self):
        pass
    
    
    #渲染信息记录
    def Lion_meshattrData(self):
        
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
        Allmesh=mc.ls(type='mesh')
        cs=[]
        rs=[]   
        mb=[]
        pv=[]
        ss=[]
        vrl=[]
        vra=[]
        ds=[]
        
        if Allmesh:
            for obj in Allmesh:
                castsShadows=mc.getAttr(obj+'.castsShadows')
                receiveShadows=mc.getAttr(obj+'.receiveShadows')
                motionBlur=mc.getAttr(obj+'.motionBlur')
                primaryVisibility=mc.getAttr(obj+'.primaryVisibility')
                smoothShading=mc.getAttr(obj+'.smoothShading')
                visibleInReflections=mc.getAttr(obj+'.visibleInReflections')
                visibleInRefractions=mc.getAttr(obj+'.visibleInRefractions')
                doubleSided=mc.getAttr(obj+'.doubleSided')
                
                if castsShadows==0:
                    cs.append({obj+':castsShadows':castsShadows})
                if receiveShadows==0:    
                    rs.append({obj+':receiveShadows':receiveShadows})
                if motionBlur==0:         
                    mb.append({obj+':motionBlur':motionBlur})
                if primaryVisibility==0:         
                    pv.append({obj+':primaryVisibility':primaryVisibility})
                if smoothShading==0:                         
                    ss.append({obj+':smoothShading':smoothShading})
                if visibleInReflections==0:         
                    vrl.append({obj+':visibleInReflections':visibleInReflections})
                if visibleInRefractions==0:         
                    vra.append({obj+':visibleInRefractions':visibleInRefractions})
                if doubleSided==0:         
                    ds.append({obj+':doubleSided':doubleSided}) 
        
        DataChange=cs+rs+mb+pv+ss+vrl+vra+ds                                                                                                                                                                          
        ObjsDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        filename=ObjsDataServerPath+shotInfo[1]+'_'+'meshData.txt'
        if os.path.exists(filename):
            os.remove(filename)         
        
        servicepath=ObjsDataServerPath+shotInfo[1]
        if os.path.exists(servicepath)==0:
            os.makedirs(servicepath)    
        
        if os.path.exists(filename):
           os.remove(filename)         
        if DataChange:
            txt = open(filename, 'w')
            try:
                txt.writelines(str(a) + '\r\n' for a in DataChange)
                print('Writing........')
            finally:
                txt.close()  
                print u'--------渲染属性记录完成-----------'

    #渲染信息记录(checkin模式)
    def Lion_meshattrDataF(self):

        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()

        Allmesh=mc.ls(type='mesh')
        cs=[]
        rs=[]
        mb=[]
        pv=[]
        ss=[]
        vrl=[]
        vra=[]
        ds=[]

        if Allmesh:
            for obj in Allmesh:
                castsShadows=mc.getAttr(obj+'.castsShadows')
                receiveShadows=mc.getAttr(obj+'.receiveShadows')
                motionBlur=mc.getAttr(obj+'.motionBlur')
                primaryVisibility=mc.getAttr(obj+'.primaryVisibility')
                smoothShading=mc.getAttr(obj+'.smoothShading')
                visibleInReflections=mc.getAttr(obj+'.visibleInReflections')
                visibleInRefractions=mc.getAttr(obj+'.visibleInRefractions')
                doubleSided=mc.getAttr(obj+'.doubleSided')

                if castsShadows==0:
                    cs.append({obj+':castsShadows':castsShadows})
                if receiveShadows==0:
                    rs.append({obj+':receiveShadows':receiveShadows})
                if motionBlur==0:
                    mb.append({obj+':motionBlur':motionBlur})
                if primaryVisibility==0:
                    pv.append({obj+':primaryVisibility':primaryVisibility})
                if smoothShading==0:
                    ss.append({obj+':smoothShading':smoothShading})
                if visibleInReflections==0:
                    vrl.append({obj+':visibleInReflections':visibleInReflections})
                if visibleInRefractions==0:
                    vra.append({obj+':visibleInRefractions':visibleInRefractions})
                if doubleSided==0:
                    ds.append({obj+':doubleSided':doubleSided})

        DataChange=cs+rs+mb+pv+ss+vrl+vra+ds
        ObjsDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        temptha='D:/TempInfo/YAK/'
        sername=ObjsDataServerPath+shotInfo[1]+'_'+'meshData.txt'
        filename=temptha+shotInfo[1]+'_'+'meshData.txt'
        if os.path.exists(filename):
            mc.sysFile(filename, delete=True )

        servicepath=temptha+shotInfo[1]
        if os.path.exists(servicepath)==0:
            mc.sysFile(servicepath, makeDir=True)
            #os.makedirs(servicepath)

        if os.path.exists(filename):
            mc.sysFile(filename, delete=True )
           #os.remove(filename)
        if DataChange:
            txt = open(filename, 'w')
            try:
                txt.writelines(str(a) + '\r\n' for a in DataChange)
                print('Writing........')
            finally:
                txt.close()
                
        if os.path.exists(filename):
            mel.eval('zwSysFile "copy" \"' + filename + '\" \"' + sername + '\" 1')
            print u'--------渲染属性记录完成-----------'
        return 0
  
    
    #设置属性信息       
    def Lion_SetMeshData(self):
                                       
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        ObjsDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
        filename=ObjsDataServerPath+shotInfo[1]+'_'+'meshData.txt'
        
        if os.path.exists(filename):
            readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(filename)
            for obj in readInfos:    
                mesh=eval(obj).keys()[0].split(':')[0]
                meshattr=eval(obj).keys()[0].split(':')[1]
                meshvalue=eval(obj).values()
                
                if mc.ls('*:'+mesh):
                    try:
                        mc.setAttr(('*:'+mesh)+'.'+meshattr,meshvalue[0])
                    except:
                        pass
                    
                if mc.ls(mesh+'Deformed'):
                    try:
                        mc.setAttr((mesh+'Deformed')+'.'+meshattr,meshvalue[0])
                    except:
                        pass
            print u'---------------渲染属性设置完成-----------------------------'
    
    
                            
