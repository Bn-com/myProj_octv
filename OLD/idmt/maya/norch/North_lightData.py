# -*- coding: utf-8 -*-

'''
Created on 2015-6-5

@author: liangyu
'''

import maya.cmds as mc
import os

class north_lightData(object):
    def __init__(self):
        pass
    
    def north_LightUItools(self): 
        
        if mc.window ("north_LIghtUI", ex=1):
            mc.deleteUI("north_LIghtUI", window=True)
        mc.window("north_LIghtUI", title=u"灯光对位工具", widthHeight=(125,40), menuBar=0)
        mc.columnLayout()
        mc.rowLayout(numberOfColumns=2, columnWidth2=(125,30))
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.2], label=(u'灯光信息输出工具'), c='from idmt.maya.norch import North_lightData\nreload(North_lightData)\nNorth_lightData.north_lightData().north_lightsaveData()')
        mc.button(w=125 , h=30 , bgc=[0, 0.4, 0.5], label=(u'灯光属性设置工具'),c ='from idmt.maya.norch import North_lightData\nreload(North_lightData)\nNorth_lightData.north_lightData().north_LightGetData()')
        mc.setParent("..")
        mc.setParent("..")
        mc.showWindow("north_LIghtUI") 
    
    #灯光信息记录
    def north_lightsaveData(self):
        
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
            
        lightHgrp=mc.ls('human_light_GRP')
        lightAgrp=mc.ls('animal_light_GRP')
        TXchange=[]
        TYchange=[]   
        TZchange=[]
        RXchange=[]
        RYchange=[]
        RZchange=[]
        SXchange=[]
        SYchange=[]
        SZchange=[]
        VBchange=[]
        
        if lightHgrp:
            for obj in lightHgrp:
                TX=mc.getAttr(obj+'.tx')
                TY=mc.getAttr(obj+'.ty')
                TZ=mc.getAttr(obj+'.tz')
                RX=mc.getAttr(obj+'.rx')
                RY=mc.getAttr(obj+'.ry')
                RZ=mc.getAttr(obj+'.rz')
                SX=mc.getAttr(obj+'.sx')
                SY=mc.getAttr(obj+'.sy')
                SZ=mc.getAttr(obj+'.sz')
                VB=mc.getAttr(obj+'.visibility')
                
                TXchange.append({obj+':tx':TX})
                TYchange.append({obj+':ty':TY})
                TZchange.append({obj+':tz':TZ})
                RXchange.append({obj+':rx':RX})                
                RYchange.append({obj+':ry':RY})
                RZchange.append({obj+':rz':RZ})
                SXchange.append({obj+':sx':SX})
                SYchange.append({obj+':sy':SY}) 
                SZchange.append({obj+':sz':SZ}) 
                VBchange.append({obj+':visibility':VB})
                
            lightdown=mc.listRelatives('human_light_GRP', c=1, f=1, type='transform')
            if lightdown:
                for obj in lightdown:
                    TX=mc.getAttr(obj+'.tx')
                    TY=mc.getAttr(obj+'.ty')
                    TZ=mc.getAttr(obj+'.tz')
                    RX=mc.getAttr(obj+'.rx')
                    RY=mc.getAttr(obj+'.ry')
                    RZ=mc.getAttr(obj+'.rz')
                    SX=mc.getAttr(obj+'.sx')
                    SY=mc.getAttr(obj+'.sy')
                    SZ=mc.getAttr(obj+'.sz')
                    VB=mc.getAttr(obj+'.visibility')
                    
                    TXchange.append({obj+':tx':TX})
                    TYchange.append({obj+':ty':TY})
                    TZchange.append({obj+':tz':TZ})
                    RXchange.append({obj+':rx':RX})                
                    RYchange.append({obj+':ry':RY})
                    RZchange.append({obj+':rz':RZ})
                    SXchange.append({obj+':sx':SX})
                    SYchange.append({obj+':sy':SY}) 
                    SZchange.append({obj+':sz':SZ}) 
                    VBchange.append({obj+':visibility':VB})
                    
                    lightDown = mc.listRelatives(obj, c=1, f=1, type='transform')
                    if lightDown:
                        for obj in lightDown:
                            TX=mc.getAttr(obj+'.tx')
                            TY=mc.getAttr(obj+'.ty')
                            TZ=mc.getAttr(obj+'.tz')
                            RX=mc.getAttr(obj+'.rx')
                            RY=mc.getAttr(obj+'.ry')
                            RZ=mc.getAttr(obj+'.rz')
                            SX=mc.getAttr(obj+'.sx')
                            SY=mc.getAttr(obj+'.sy')
                            SZ=mc.getAttr(obj+'.sz')
                            VB=mc.getAttr(obj+'.visibility')
                            
                            TXchange.append({obj+':tx':TX})
                            TYchange.append({obj+':ty':TY})
                            TZchange.append({obj+':tz':TZ})
                            RXchange.append({obj+':rx':RX})                
                            RYchange.append({obj+':ry':RY})
                            RZchange.append({obj+':rz':RZ})
                            SXchange.append({obj+':sx':SX})
                            SYchange.append({obj+':sy':SY}) 
                            SZchange.append({obj+':sz':SZ}) 
                            VBchange.append({obj+':visibility':VB})
    
            DataChange=TXchange+TYchange+TZchange+RXchange+RYchange+RZchange+SXchange+SYchange+SZchange+VBchange                                                                                                                                                                                  
            ObjsDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            filename=ObjsDataServerPath+shotInfo[1]+'_'+shotInfo[2]+'_'+(shotInfo[3]).split('.')[0]+'_'+'lightData.txt'
            if os.path.exists(filename):
                os.remove(filename)         
            if DataChange:
                sk_infoConfig.sk_infoConfig().checkFileWrite(filename,DataChange)
                print u'--------完成-----------'
                    
        if lightAgrp:
            for obj in lightAgrp:
                TX=mc.getAttr(obj+'.tx')
                TY=mc.getAttr(obj+'.ty')
                TZ=mc.getAttr(obj+'.tz')
                RX=mc.getAttr(obj+'.rx')
                RY=mc.getAttr(obj+'.ry')
                RZ=mc.getAttr(obj+'.rz')
                SX=mc.getAttr(obj+'.sx')
                SY=mc.getAttr(obj+'.sy')
                SZ=mc.getAttr(obj+'.sz')
                VB=mc.getAttr(obj+'.visibility')
                
                TXchange.append({obj+':tx':TX})
                TYchange.append({obj+':ty':TY})
                TZchange.append({obj+':tz':TZ})
                RXchange.append({obj+':rx':RX})                
                RYchange.append({obj+':ry':RY})
                RZchange.append({obj+':rz':RZ})
                SXchange.append({obj+':sx':SX})
                SYchange.append({obj+':sy':SY}) 
                SZchange.append({obj+':sz':SZ}) 
                VBchange.append({obj+':visibility':VB})
            
            lightdown=mc.listRelatives('animal_light_GRP', c=1, f=1, type='transform')
            if lightdown:
                for obj in lightdown:
                    TX=mc.getAttr(obj+'.tx')
                    TY=mc.getAttr(obj+'.ty')
                    TZ=mc.getAttr(obj+'.tz')
                    RX=mc.getAttr(obj+'.rx')
                    RY=mc.getAttr(obj+'.ry')
                    RZ=mc.getAttr(obj+'.rz')
                    SX=mc.getAttr(obj+'.sx')
                    SY=mc.getAttr(obj+'.sy')
                    SZ=mc.getAttr(obj+'.sz')
                    VB=mc.getAttr(obj+'.visibility')
                    
                    TXchange.append({obj+':tx':TX})
                    TYchange.append({obj+':ty':TY})
                    TZchange.append({obj+':tz':TZ})
                    RXchange.append({obj+':rx':RX})                
                    RYchange.append({obj+':ry':RY})
                    RZchange.append({obj+':rz':RZ})
                    SXchange.append({obj+':sx':SX})
                    SYchange.append({obj+':sy':SY}) 
                    SZchange.append({obj+':sz':SZ}) 
                    VBchange.append({obj+':visibility':VB})
                    
                    lightDown = mc.listRelatives(obj, c=1, f=1, type='transform')
                    if lightDown:
                        for obj in lightDown:
                            TX=mc.getAttr(obj+'.tx')
                            TY=mc.getAttr(obj+'.ty')
                            TZ=mc.getAttr(obj+'.tz')
                            RX=mc.getAttr(obj+'.rx')
                            RY=mc.getAttr(obj+'.ry')
                            RZ=mc.getAttr(obj+'.rz')
                            SX=mc.getAttr(obj+'.sx')
                            SY=mc.getAttr(obj+'.sy')
                            SZ=mc.getAttr(obj+'.sz')
                            VB=mc.getAttr(obj+'.visibility')
                            
                            TXchange.append({obj+':tx':TX})
                            TYchange.append({obj+':ty':TY})
                            TZchange.append({obj+':tz':TZ})
                            RXchange.append({obj+':rx':RX})                
                            RYchange.append({obj+':ry':RY})
                            RZchange.append({obj+':rz':RZ})
                            SXchange.append({obj+':sx':SX})
                            SYchange.append({obj+':sy':SY}) 
                            SZchange.append({obj+':sz':SZ}) 
                            VBchange.append({obj+':visibility':VB})
                            
            DataChange=TXchange+TYchange+TZchange+RXchange+RYchange+RZchange+SXchange+SYchange+SZchange+VBchange                                                                                                                                                                                  
            ObjsDataServerPath = sk_infoConfig.sk_infoConfig().checkCacheServerPath(2)
            filename=ObjsDataServerPath+shotInfo[1]+'_'+shotInfo[2]+'_'+(shotInfo[3]).split('.')[0]+'_'+'lightData.txt'
            if os.path.exists(filename):
                os.remove(filename)         
            if DataChange:
                sk_infoConfig.sk_infoConfig().checkFileWrite(filename,DataChange)
                print u'--------完成-----------'   
    
    #灯光信息输入            
    def north_LightGetData(self):       
        if mc.window ("north_LightUITools", ex=1):
            mc.deleteUI("north_LightUITools", window=True)
        mc.window("north_LightUITools", title="LightData Tools", widthHeight=(500, 100), menuBar=0)
        mc.columnLayout( adjustableColumn=True )
        mc.text( label=u'\n请输入灯光文件路径下的文件名\n例如：Z:\\Projects\\North\\Project\data\\GeoCache\\999\\008\\999_008_an_lightData.txt' )
        mc.textField('textname')
        mc.button(label=u'设置灯光属性',c='North_lightData.north_lightData().north_transData()')
        mc.showWindow( "north_LightUITools" )   
         
    def north_transData(self):       
        from idmt.maya.norch import North_lightData
        reload(North_lightData) 
        checkdata=mc.textField('textname',q=1,tx=1)
        North_lightData.north_lightData().north_LightValue(checkdata)
        
    #灯光信息设置    
    def north_LightValue(self,data):    
        from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
        reload(sk_infoConfig)        
        checkdata = data
        if not checkdata:
            mc.confirmDialog( title='Confirm', message=u'请输入灯光文件', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if checkdata:
            readInfos = sk_infoConfig.sk_infoConfig().checkFileRead(checkdata)
            lightHgrp=mc.ls('human_light_GRP')
            lightAgrp=mc.ls('animal_light_GRP')
                
            if eval(readInfos[0]).keys()[0].split(':')[0]=='animal_light_GRP':
                if not lightAgrp:
                    mc.confirmDialog( title='Confirm', message=u'请导入动物灯光', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )            
                if lightAgrp:
                    for obj in readInfos:        
                        aaa = eval(obj)   
                        Ligt=aaa.keys()
                        Ligtname=Ligt[0].split(':')[0]
                        Ligtattr=Ligt[0].split(':')[-1]
                        Ligtvalue=aaa.values()
                                              
                        mc.setAttr(Ligtname+'.'+Ligtattr,Ligtvalue[0])   
            print u'---------------动物灯光属性设置完成-----------------------------'
            
            if eval(readInfos[0]).keys()[0].split(':')[0]=='human_light_GRP':
                if not lightHgrp:
                    mc.confirmDialog( title='Confirm', message=u'请导入人类灯光', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )            
                if lightHgrp:
                    for obj in readInfos:        
                        aaa = eval(obj)   
                        Ligt=aaa.keys()
                        Ligtname=Ligt[0].split(':')[0]
                        Ligtattr=Ligt[0].split(':')[-1]
                        Ligtvalue=aaa.values()
                                              
                        mc.setAttr(Ligtname+'.'+Ligtattr,Ligtvalue[0])                 
                print u'---------------人类灯光属性设置完成-----------------------------'
    
    
                            
