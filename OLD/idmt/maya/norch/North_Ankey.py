# -*- coding: utf-8 -*-

import maya.cmds as mc
'''
Created on 2015-5-27

@author: liangyu
'''
import idmt.pipeline.db
#master大环key帧
def north_anKEY():
    from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
    reload(sk_infoConfig)
    
    shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
    shot = shotInfos[0] + '_' + shotInfos[1] + '_' + shotInfos[2] + '_' + shotInfos[3]
    anim = idmt.pipeline.db.GetAnimByFilename(shot)
    endFrame = anim.frmEnd
    
    Master = mc.ls('*:*SRT')
    Cmaster=mc.ls('*:*Master')
    
    mc.currentTime(endFrame)
    if endFrame:
        if Master:         
            for ctrl in Master:
                mc.currentTime(endFrame)
                TX=mc.getAttr(ctrl+'.tx')
                mc.setKeyframe((ctrl+'.tx'),t=endFrame)
                mc.setKeyframe((ctrl+'.tx'),t=endFrame+1)
                TY=mc.getAttr(ctrl+'.ty')
                mc.setKeyframe((ctrl+'.ty'),t=endFrame)
                mc.setKeyframe((ctrl+'.ty'),t=endFrame+1)
                TZ=mc.getAttr(ctrl+'.tz')
                mc.setKeyframe((ctrl+'.tz'),t=endFrame)
                mc.setKeyframe((ctrl+'.tz'),t=endFrame+1)
                
                mc.currentTime(endFrame+2)
                mc.setAttr((ctrl+'.tx'),(TX+10))
                mc.setKeyframe((ctrl+'.tx'),t=endFrame+2)
                mc.setAttr((ctrl+'.ty'),(TY+10))
                mc.setKeyframe((ctrl+'.ty'),t=endFrame+2)
                mc.setAttr((ctrl+'.tz'),(TZ+10))
                mc.setKeyframe((ctrl+'.tz'),t=endFrame+2)          
        if Cmaster:         
            for ctrl in Cmaster:
                mc.currentTime(endFrame)
                TX=mc.getAttr(ctrl+'.tx')
                mc.setKeyframe((ctrl+'.tx'),t=endFrame)
                mc.setKeyframe((ctrl+'.tx'),t=endFrame+1)
                TY=mc.getAttr(ctrl+'.ty')
                mc.setKeyframe((ctrl+'.ty'),t=endFrame+1)
                TZ=mc.getAttr(ctrl+'.tz')
                mc.setKeyframe((ctrl+'.tz'),t=endFrame+1)
                
                mc.currentTime(endFrame+2)
                mc.setAttr((ctrl+'.tx'),(TX+10))
                mc.setKeyframe((ctrl+'.tx'),t=endFrame+2)
                mc.setAttr((ctrl+'.ty'),(TY+10))
                mc.setKeyframe((ctrl+'.ty'),t=endFrame+2)
                mc.setAttr((ctrl+'.tz'),(TZ+10))
                mc.setKeyframe((ctrl+'.tz'),t=endFrame+2)                  
                
                
def north_anRender():
    #检测norender层，并打印物体名称
    if mc.ls('norender',type = 'displayLayer'):
        norOBJ=mc.editDisplayLayerMembers('norender',q=1)
        if norOBJ:
            print u'-----------norender层物体---------------------'
            for obj in norOBJ:
                print obj
            print u'-----------norender层物体---------------------'
        else:
            print(u'norender层内没有物体\n\n')
    else:
        print(u'文件没有norender层')
        mc.warning(u'文件没有norender层') #----20151106 张贲修改，不需要必须有norender 组
               
    #检测transformer层，并打印物体名称               
    #if mc.ls('transformer',type = 'displayLayer'):
        #transOBJ=mc.editDisplayLayerMembers('transformer',q=1)
        #if transOBJ:
            #print u'------------transformer层物体-----------------'
            #for obj in transOBJ:
                #print obj
            #print u'------------transforemer层物体----------------'
        #else:
            #print(u'transformer层内没有物体')
    #else:
        #print(u'文件没有transformer层')
        #mc.error(u'文件没有transformer层')                                                                                                                                   

#检测ToRig组下被移动控制器的物体
def north_checkANGEO():
    print u'---------------开始查询------------------'
    needCurs=[] 
    curves = mc.ls(type='nurbsCurve',l=1)
    if curves:
        for cur in curves:          
            trans = mc.listRelatives(cur,p=1,ni=1,f=1)[0]
            needCurs.append(trans)
    
    GEONeed=[]
    geos=''                
    if needCurs:
        for cur in needCurs:
            try:     
                if ((cur.split('|')[-1]).split(':')[-2].split('_')[1][0]).lower()=='s':
                    if (mc.getAttr(cur+'.tx')!=0) or (mc.getAttr(cur+'.ty')!=0) or (mc.getAttr(cur+'.tz')!=0) or (mc.getAttr(cur+'.rx')!=0) or (mc.getAttr(cur+'.ry')!=0) or (mc.getAttr(cur+'.rz')!=0) or (mc.getAttr(cur+'.sx')!=1) or (mc.getAttr(cur+'.sy')!=1) or (mc.getAttr(cur+'.sz')!=1):                           
                        Joint=mc.listRelatives(cur, ad=1,type='joint')
                        if Joint:
                            for jot in Joint:                     
                                skin = mc.listConnections(jot+'.worldMatrix',s=0,d=1)[0]
                                geos=mc.listConnections(skin+'.outputGeometry',s=0,d=1)
                                if geos:
                                    for geo in geos:
                                        if mc.listRelatives(geo, ad=1, ni=1, type='mesh', f=1):
                                            GEONeed.append(geo)
                                        else:
                                            skinSet=mc.listConnections(skin+'.message',s=0,d=1)[0]
                                            geo=mc.listConnections(skinSet+'.memberWireframeColor',s=0,d=1)[0]
                                            GEONeed.append(geo)
            except:
                pass
    
    
    
    
    needSoft=[]
    softMos=mc.ls(type='softModHandle',l=1)
    if softMos:
        for softMo in softMos:          
            softtans = mc.listRelatives(softMo,p=1,ni=1,f=1)[0]
            needSoft.append(softtans)
    
    NeedGEO=[]        
    if needSoft:       
        for softMo in needSoft:
            if mc.getAttr(softMo+'.tx')!=0 or mc.getAttr(softMo+'.ty')!=0 or mc.getAttr(softMo+'.tz')!=0 or mc.getAttr(softMo+'.rx')!=0 or mc.getAttr(softMo+'.ry')!=0 or mc.getAttr(softMo+'.rz')!=0:
                softshape=mc.listRelatives(softMo, s=1, ni=1, f=1,type='softModHandle')[0]
                SoftDeformer=mc.listConnections(softshape+'.softModTransforms',s=0,d=1)[0]
                locaterSet=mc.listConnections(SoftDeformer+'.message',s=0,d=1)
                for set in locaterSet:
                    try:
                        geos=mc.listConnections(locaterSet+'.memberWireframeColor',s=0,d=1)
                        for geo in geos:
                            try:
                                shape=mc.listRelatives(geo, ad=1, ni=1, type='mesh', f=1)[0]
                                if shape:
                                    geo=mc.listRelatives(shape, p=1, type='transform', f=1)[0]
                                    NeedGEO.append(geo)
                            except:
                                pass 
                                                       
                    except:
                        pass
                    
    
    NeedGEO=[NeedGEO[i] for i in range(len(NeedGEO)) if NeedGEO[i] not in NeedGEO[:i]]
    GEONeed=[GEONeed[i] for i in range(len(GEONeed)) if GEONeed[i] not in GEONeed[:i]]
    NeedGEO=NeedGEO+GEONeed
    if NeedGEO:
        print u'------------ToRIG组下移动的物体----------------'
        for geo in NeedGEO:           
            print geo
        print u'------------ToRIG组下移动的物体----------------'

    print u'---------------查询完毕------------------'