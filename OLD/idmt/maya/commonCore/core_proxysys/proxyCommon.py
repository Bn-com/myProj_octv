# -*- coding: utf-8 -*-
# 【通用】【MR渲染代理工具】
#  Author : 韩虹
#  Data   : 2014_08
# import sys
# sys.path.append('D:\\food\pyp\common')

import maya.cmds as mc
import maya.mel as mel
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
import os
import re


class proxyCommon(object):
    def __init__(self):
        pass
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
    def MRProxyUI(self):
    # 窗口
        if mc.window('mr_ProxyWin', exists=True):
            mc.deleteUI('mr_ProxyWin')
        mc.window('mr_ProxyWin', title=u'NJ 高低模',width=310, height=350, sizeable=True)
        mc.columnLayout(adjustableColumn=True)
        
        mc.frameLayout(label=u'代理输出工具', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(l=u'输出高模代理',width=80,c="proxyCommon.proxyCommon().MRProxyCreat(h='h')")
        mc.button(l=u'输出低模代理',width=80,c="proxyCommon.proxyCommon().MRProxyCreat(h='l')")
        mc.setParent('..')
        mc.setParent('..')
                
        mc.frameLayout(label=u'参考状态下高低模转换', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=0)        
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(l=u'高模',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago/nj_SwichBG.py')\nnj_SwichBG('h')")
        mc.button(l=u'低模',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago/nj_SwichBG.py')\nnj_SwichBG('l')")
        mc.button(l=u'代理',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago/nj_SwichBG.py')\nnj_SwichBG('p')")
        mc.button(l=u'rgb',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago/nj_SwichBG.py')\nnj_SwichBG('a')")
        mc.button(l=u'Vray',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago/nj_SwichBG.py')\nnj_SwichBG('v')")
        mc.setParent('..')
        mc.setParent('..')

        mc.frameLayout(label=u'导入状态下高低模转换', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(l=u'高模',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/nj2015_switchMode.py')\nnj2015_witchHight()")
        mc.button(l=u'低模',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/nj2015_switchMode.py')\nnj2015_witchLow()")
        mc.button(l=u'代理',width=80,c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/nj2015_switchMode.py')\nnj2015_witchProxy()")
        mc.setParent('..')
        mc.setParent('..')        

        mc.frameLayout(label=u'渲染代理高低模转换', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=4)
        mc.button(l=u'高低模转换',width=80,c="from idmt.maya.py_common import nj_modSwitch\nreload(nj_modSwitch)\nnj_modSwitch.nj_modSwitch().nj_switchModeWin()")
        mc.setParent('..')
        mc.setParent('..')  
        
        mc.frameLayout(label=u'=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=4)  
        mc.button(l=u'断开P模代理路径All',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().breakeAllProxyPath()')  
        mc.button(l=u'断开P模代理路径Select',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().breakeSelectProxyPath()')       
        mc.setParent('..') 
        mc.setParent('..')
        
        mc.frameLayout(label=u'=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=4)  
        mc.button(l=u'把所有低模转为代理',width=120,bgc=[0.13, 0.15, 0.25],c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/nj2015_switchMode.py')\nnj2015_Low_Proxy()")  
        mc.button(l=u'把所有高模转为代理',width=120,bgc=[0, 0, 0],c="execfile('//File-cluster/GDC/Resource/Support/Maya/projects/Ninjago2015/nj2015_switchMode.py')\nnj2015_Low_Proxy()")       
        mc.setParent('..') 
        mc.setParent('..')

        mc.frameLayout(label=u'=====13集代理=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)                          
        mc.frameLayout(label=u'=====ALL=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'FX代理',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="Fx",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'FX RGB代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="frgb",sl=0,kdegree=0,kinfoType=0)')        
        mc.button(l=u'Color代理(夜晚,低模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="night",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'Color代理(白天，低模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="day",sl=0,kdegree=0,kinfoType=0)')
        mc.button(l=u'Color代理(夜晚,高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="night",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'Color代理(白天，高模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="day",sl=0,kdegree=0,kinfoType=0)')
        mc.setParent('..') 
        mc.setParent('..')   
    
        mc.frameLayout(label=u'=====Select=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'Color代理(低模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="night",sl=1,kdegree=0,kinfoType=1)')  
        mc.button(l=u'Color代理(高模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="night",sl=1,kdegree=0,kinfoType=1)')        
        mc.button(l=u'Color代理(夜晚)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="night",sl=1,kdegree=1,kinfoType=0)')  
        mc.button(l=u'Color代理(白天)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="day",sl=1,kdegree=1,kinfoType=0)')
        mc.button(l=u'Color代理(夜晚,低模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="night",sl=1,kdegree=0,kinfoType=0)')  
        mc.button(l=u'Color代理(白天，低模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="l",infoType="day",sl=1,kdegree=0,kinfoType=0)')    
        mc.button(l=u'Color代理(夜晚,高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="night",sl=1,kdegree=0,kinfoType=0)')
        mc.button(l=u'Color代理(白天，高模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="day",sl=1,kdegree=0,kinfoType=0)')    
        mc.button(l=u'ncolor代理(ncolor,相关)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="ncolor",sl=1,kdegree=1,kinfoType=0)') 
        mc.setParent('..') 
        mc.setParent('..')
    
        mc.frameLayout(label=u'=====Relevant=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'RGB代理',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="rgb",sl=0,kdegree=1,kinfoType=0)')
        mc.button(l=u'ncolor代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="ncolor",sl=0,kdegree=1,kinfoType=0)')          
        mc.button(l=u'Color代理(夜晚)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="night",sl=0,kdegree=1,kinfoType=0)')
        mc.button(l=u'roof RGB代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="roof",sl=0,kdegree=1,kinfoType=0)')   
        mc.button(l=u'Color代理(白天)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="day",sl=0,kdegree=1,kinfoType=0)') 
        mc.button(l=u'wood RGB代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="stake",sl=0,kdegree=1,kinfoType=0)')         
        mc.setParent('..') 
        mc.setParent('..')
        
        mc.frameLayout(label=u'=====高低模选择=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'选择低模代理',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxyHLSelect(degree="l")')  
        mc.button(l=u'选择高模代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxyHLSelect(degree="h")')       
        mc.setParent('..') 
        mc.setParent('..')
        
        mc.frameLayout(label=u'=====light=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'打开所有代理夜晚灯光',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSet_13(1,0)')
        mc.button(l=u'关闭所有代理夜晚灯光',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSet_13(0,0)')  
        mc.button(l=u'打开选择代理夜晚灯光',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSet_13(1,1)')   
        mc.button(l=u'关闭选择代理夜晚灯光',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSet_13(0,1)')            
        mc.button(l=u'打开所有代理面灯',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().proxyAreaLightSet_13(1,0)')
        mc.button(l=u'关闭所有代理面灯',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().proxyAreaLightSet_13(0,0)') 
        mc.button(l=u'选择所有代理面灯',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().proxyAreaLightSet_13(0,1)')          
        mc.setParent('..') 
        mc.setParent('..') 
        mc.setParent('..') 
        
        mc.frameLayout(label=u'=====19 20 集代理=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=1)
        mc.frameLayout(label=u'=====ALL=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)        
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'Color代理(白天,高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="day",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'',width=120,bgc=[0.13, 0.15, 0.25]) 
        mc.button(l=u'红房子(夜晚,高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="Rnight",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'绿房子(夜晚,高模)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="Gnight",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'RGB代理(房子，高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="rgb",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'RGB01代理(房子，高模)',width=120,bgc=[0,0, 0],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="rgb01",sl=0,kdegree=0,kinfoType=0)')           
        mc.button(l=u'RGB02代理(灯笼，高模)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="rgb02",sl=0,kdegree=0,kinfoType=0)')         
        mc.button(l=u'ncolor(高模)',width=120,bgc=[0,0, 0],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="ncolor",sl=0,kdegree=0,kinfoType=0)')         
        mc.button(l=u'FX代理',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="l",infoType="FX",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'FX RGB代理',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="l",infoType="FXrgb",sl=0,kdegree=0,kinfoType=0)') 
        mc.button(l=u'灯笼(显示)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxyMeshSet_019(info="lantern",sl=0,vis=1,p=1)')  
        mc.button(l=u'灯笼(隐藏)',width=120,bgc=[0,0,0],c='proxyCommon.proxyCommon().nj_proxyMeshSet_019(info="lantern",sl=0,vis=0,p=1)')
         
       
        mc.setParent('..') 
        mc.setParent('..') 

        mc.frameLayout(label=u'=====Select=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'Color代理(白天)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="day",sl=1,kdegree=0,kinfoType=0)')     
        mc.button(l=u'',width=120,bgc=[0.13, 0.15, 0.25])        
        mc.button(l=u'红房子(夜晚)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="Rnight",sl=1,kdegree=0,kinfoType=0)')  
        mc.button(l=u'绿房子(夜晚)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().MRProxySetNew_19(degree="h",infoType="Gnight",sl=1,kdegree=0,kinfoType=0)')        
        mc.button(l=u'灯笼(显示)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxyMeshSet_019(info="lantern",sl=1,vis=1,p=1)')  
        mc.button(l=u'灯笼(隐藏)',width=120,bgc=[0,0, 0],c='proxyCommon.proxyCommon().nj_proxyMeshSet_019(info="lantern",sl=1,vis=0,p=1)') 
        mc.setParent('..') 
        mc.setParent('..')
        
        mc.frameLayout(label=u'=====light=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=0,cl=1)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'打开代理灯光(all)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSet_019(c="g",sl=0,win=1,volum=1)')
        mc.button(l=u'关闭代理灯光(all)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSet_019(c="g",sl=0,win=0,volum=0)')  
        mc.button(l=u'打开代理灯光(select)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSet_019(c="g",sl=1,win=1,volum=1)')   
        mc.button(l=u'关闭代理灯光(select)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSet_019(c="g",sl=1,win=0,volum=0)')            
        mc.button(l=u'选择代理面灯光(all)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=0,win=1,volum=0)')
        mc.button(l=u'选择代理体积灯光(all)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=0,win=0,volum=1)') 
        mc.button(l=u'选择代理面灯光(select)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=1,win=1,volum=0)')
        mc.button(l=u'选择代理体积灯光(select)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=1,win=0,volum=1)')         
        mc.button(l=u'选择所有代理灯(all)',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=0,win=1,volum=1)')          
        mc.button(l=u'选择所有代理灯(select)',width=120,bgc=[0, 0, 0],c='proxyCommon.proxyCommon().nj_proxylightSelect_019(sl=1,win=1,volum=1)')          
        mc.setParent('..') 
        mc.setParent('..')  
        mc.setParent('..') 
                
        mc.frameLayout(label=u'=====Tree代理=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.frameLayout(label=u'=====ALL=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)        
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'Color',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="color",sl=0,kdegree=0,kinfoType=0)')  
        mc.button(l=u'ncolor',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="ncolor",sl=0,kdegree=0,kinfoType=0)')          
        mc.button(l=u'rgb01',width=120,bgc=[0,0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="rgb01",sl=0,kdegree=0,kinfoType=0)')           
        mc.button(l=u'rgb02',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="rgb02",sl=0,kdegree=0,kinfoType=0)')         
               
        mc.setParent('..') 
        mc.setParent('..') 

        mc.frameLayout(label=u'=====Select=====', bgc=[0, 0, 0.0], borderStyle='etchedIn', cll=1,cl=0)
        mc.rowColumnLayout(numberOfColumns=2)  
        mc.button(l=u'Color',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="color",sl=1,kdegree=0,kinfoType=0)')  
        mc.button(l=u'ncolor',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="ncolor",sl=1,kdegree=0,kinfoType=0)')          
        mc.button(l=u'rgb01',width=120,bgc=[0,0, 0],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="rgb01",sl=1,kdegree=0,kinfoType=0)')           
        mc.button(l=u'rgb02',width=120,bgc=[0.13, 0.15, 0.25],c='proxyCommon.proxyCommon().MRProxySetNew(degree="h",infoType="rgb02",sl=1,kdegree=0,kinfoType=0)')  
        mc.setParent('..') 
        mc.setParent('..')              
        mc.showWindow('mr_ProxyWin')   
#============================================
# 渲染代理创建（仅用于制作）韩虹
#=====================================			               

    def MRProxyCreat(self,h='h',server=1):
        #Proxy 设置
        objs=mc.ls(sl=1,l=1)
        meshh=''
        meshp=''
        mip=''
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        if objs and len(objs)==2 and '_' in objs[0]:
            meshh=objs[0]
            meshp=objs[1]
            shortname=meshh.split('|')[-1].split('_')[2]
            mip=shotInfos[0]+'_'+shotInfos[1]+'_'+shortname+"mip_binaryproxy"
            mipath='D:/Info_Temp/temp/proxy/'+shotInfos[0]+'/'+shotInfos[1]+'/'
            serverpahth=sk_infoConfig.sk_infoConfig().checkProjectServerPath()+'data/proxy/PorxyFiles/'+shotInfos[1]+'/'
            mc.sysFile(mipath, makeDir=True)
            miname=shotInfos[1]+'_'+shortname+'_'+h+'_ncolor.mi'
            if mc.ls(mip):
                mc.delete(mip)
            mc.createNode ('mip_binaryproxy',n=mip)
            mc.setAttr((mip+'.object_filename'),(mipath+miname),type='string')
            mc.setAttr((mip+'.write_geometry'),1)
            mc.setAttr((meshp+'.miExportGeoShader'),1)
            miNode=meshp+'.miGeoShader'
            GeoNode=mip+'.geometry'
            if miNode:
                cons=mc.listConnections(miNode,p=1,c=1)
                if cons:
                    mc.disconnectAttr(cons[0],cons[1])
                mc.connectAttr((mip+'.outValue'),(meshp+'.miGeoShader'),f=1)
            if GeoNode:
                conG=mc.listConnections(GeoNode,p=1,c=1)
                if conG:
                    mc.disconnectAttr(cons[1],cons[0])
                mc.connectAttr((meshh+'.miGeoShader'),GeoNode)
            #渲染一帧(出mi文件）
            mel.eval('source "renderWindowPanel.mel"')
            mel.eval('renderWindowRenderCamera "render" "renderView" "persp"')
        else:
            mc.error('no objs or more than 2')
        if server==1:
            updateAnimCMD = 'zwSysFile "copy" ' + '"' + (mipath+miname) + '"' + ' ' + '"' + (serverpahth + miname) + '"' + ' true'
            mel.eval(updateAnimCMD)
            mc.setAttr((mip+'.object_filename'),(serverpahth+miname),type='string')
        mc.setAttr((mip+'.write_geometry'),0)
        return [meshh,meshp,mip]
                
#参考导入
    def proxy_RefIm(self):
        refPath=mc.file(q=1,r=1)
        if len(refPath)!=0:
            for r in refPath:
                refRN=mc.file(r,q=1,rfn=1)
                if(mc.file(r,q=1,dr=1)):
                    mc.file(refRN,loadReference=1)
                mc.file(r,ir=1)
                
    def MRProxyRecord(self):
        RenderMi=[]
        RenderMesh=[]
        MipMi=[]
        MipObj=[]
        meshs=mc.ls(type='mesh',l=1)
        mips=mc.ls(type='mip_binaryproxy',l=1)
        if meshs:
            for mesh in meshs:
                mi=mc.getAttr(mesh+'.miProxyFile')
                if mi and re.search('.mi',mi)!=None and re.search('/',mi)!=None:
                    RenderMi.append(mi)
                    RenderMesh.append(mesh)
        if mips:
            for mip in mips:
                mi=mc.getAttr(mip+'.object_filename')
                cons=mc.listConnections((mip+'.outValue'),p=0,c=1)
                if mi and re.search('.mi',mi)!=None and re.search('/',mi)!=None and cons:
                    for j in range(1,len(cons),2):
                        MipMi.append(mi)
                        MipObj.append(mc.ls(cons[j],l=1)[0])
        return [RenderMi,RenderMesh,MipMi,MipObj] 

    def MRProxySet(self,infoType='fx'): 
        MiInfo=self.MRProxyRecord()
        RenderMi=MiInfo[0]
        RenderMesh=MiInfo[1]
        MipMi=MiInfo[2]
        MipObj=MiInfo[3]
        if infoType=='fx':
            meshs=self.proxy_GDMeshList(attrtype='GD')
            if meshs:
                for k in range(len(meshs[0])):
                    mc.setAttr((meshs[0][k]+'.castsShadows'),0)
                    mc.setAttr((meshs[0][k]+'.receiveShadows'),0)
                    mc.setAttr((meshs[0][k]+'.primaryVisibility'),0)         
        if infoType=='fx'and RenderMi :
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                mipath=RenderMi[i].replace(short,'')
                fxshort=''                
                if re.search('_',RenderMi[i])==None:
                    fxshort=short.replace('.mi','')+'_Fx.mi'
                else:
                    fxshort=short.split('_')[0]+'_Fx.mi'                    
                mc.setAttr((RenderMesh[i]+'.miProxyFile'),(mipath+fxshort),type='string')
        if infoType=='fx'and MipMi :
            for i in range(len(MipMi)):
                short=MipMi[i].split('/')[-1]
                mipath=MipMi[i].replace(short,'')
                fxshort=short.replace('_n','_Fx')
                mesh=mc.listRelatives(MipObj[i],s=1,f=1)[0]
                cons=mc.listConnections((MipObj[i]+'.miGeoShader'),p=0,c=1)
                if cons:
                    mc.delete(cons[1])
                mc.setAttr((MipObj[i]+'.miExportGeoShader'),0)
                mc.setAttr((mesh+'.miProxyFile'),(mipath+fxshort),type='string')
        if infoType=='tx'and RenderMi :
            for i in range(len(RenderMi)):
                if re.search('_',RenderMi[i])!=None:
                    short=RenderMi[i].split('/')[-1]
                    mipath=RenderMi[i].replace(short,'')
                    fxshort=short.split('_')[0]+'.mi'
                    mc.setAttr((RenderMesh[i]+'.miProxyFile'),(mipath+fxshort),type='string')
        if infoType=='tx'and MipMi :
            for i in range(len(MipMi)):
                short=MipMi[i].split('/')[-1]
                mipath=MipMi[i].replace(short,'')
                fxshort=short.replace('_n','')
                mesh=mc.listRelatives(MipObj[i],s=1,f=1)[0]
                cons=mc.listConnections((MipObj[i]+'.miGeoShader'),p=0,c=1)
                if cons:
                    mc.delete(cons[1])
                mc.setAttr((MipObj[i]+'.miExportGeoShader'),0)
                mc.setAttr((mesh+'.miProxyFile'),(mipath+fxshort),type='string')
        if infoType=='day'and RenderMi :
            for i in range(len(RenderMi)):
                if re.search('_',RenderMi[i])!=None:
                    short=RenderMi[i].split('/')[-1]
                    mipath=RenderMi[i].replace(short,'')
                    fxshort=short.split('_')[0]+'_day.mi'
                    mc.setAttr((RenderMesh[i]+'.miProxyFile'),(mipath+fxshort),type='string')
        if infoType=='day'and MipMi :
            for i in range(len(MipMi)):
                short=MipMi[i].split('/')[-1]
                mipath=MipMi[i].replace(short,'')
                fxshort=short.replace('_n','_day')
                mesh=mc.listRelatives(MipObj[i],s=1,f=1)[0]
                cons=mc.listConnections((MipObj[i]+'.miGeoShader'),p=0,c=1)
                if cons:
                    mc.delete(cons[1])
                mc.setAttr((MipObj[i]+'.miExportGeoShader'),0)
                mc.setAttr((mesh+'.miProxyFile'),(mipath+fxshort),type='string')                
        if infoType=='ncolor' and  RenderMi:
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                mipath=RenderMi[i].replace(short,'')
                nshort=''
                if re.search('_Fx',RenderMi[i])!=None:
                    nshort=short.replace('_Fx','_n')
                else:
                    nshort=short.replace('.mi','')+'_n.mi'
                mc.setAttr((RenderMesh[i]+'.miProxyFile'),'',type='string') 
                mesh=mc.listRelatives(RenderMesh[i],p=1,f=1)[0]
                mipnode=nshort.split('_n')[0]+'_mip_binaryproxy_'
                mc.createNode ('mip_binaryproxy',n=mipnode)
                mc.setAttr((mipnode+'.object_filename'),(mipath+nshort),type='string')
                mc.setAttr((mesh+'.miExportGeoShader'),1)
                cons=mc.listConnections((mesh+'.miGeoShader'),p=1,c=1)
                if cons:
                    mc.disconnectAttr(cons[0],cons[1])
                mc.connectAttr((mipnode+'.outValue'),(mesh+'.miGeoShader'),f=1)
        print    u'已经完成代理转换'
        return 0                              

    def proxy_GDMeshList(self,attrtype='GD'):
        setmesh=self.proxy_Attrlist(attrtype)
        meshshapes=[]
        errormesh=[]
        if setmesh:
            for mesh in setmesh:
                cmeshs=mc.listRelatives(mesh,c=1,f=1)
                if cmeshs:
                    for cmesh in cmeshs:
                        if mc.nodeType(cmesh)=='mesh':
                            meshshapes.append(cmesh)
                        if mc.nodeType(cmesh)=='transform':
                            mshapes=mc.listRelatives(cmesh,c=1,f=1)
                            for shape in mshapes:
                                if mc.nodeType(shape)=='mesh':
                                    meshshapes.append(shape)
                                if mc.nodeType(shape)=='transform':  
                                    shapes=mc.listRelatives(shape,c=1,f=1)
                                    for fshape in shapes:
                                        if mc.nodeType(fshape)=='mesh': 
                                             meshshapes.append(shape)
                                        else:
                                            errormesh.append(shape)
        return [meshshapes, errormesh]

    def proxy_Attrlist(self,attrtype='GD'):
        objList=[]
        objs=mc.ls(type='transform',l=1)
        if objs: 
            for obj in objs:
                if mc.objExists(obj+'.'+attrtype) and mc.getAttr(obj+'.'+attrtype)==1:
                     objList.append(obj)
        return objList 

    def MRProxyRecordSel(self):
        RenderMi=[]
        RenderMesh=[]
        MipMi=[]
        MipObj=[]
        meshs=mc.ls(sl=1,l=1)
        if meshs:
            for mesh in meshs:
                Ena=mesh+'.miExportGeoShader'
                GeoShader=mesh+'.miGeoShader'
                if mc.getAttr(Ena)==True and mc.objExists(GeoShader) and mc.listConnections(GeoShader,p=1,c=1)!=None:
                    mip=mc.listConnections(GeoShader,p=0,c=1)[1]
                    if mc.nodeType(mip)=='mip_binaryproxy':
                        mi=mc.getAttr(mip+'.object_filename')
                        if mi and re.search('.mi',mi)!=None and re.search('/',mi)!=None :
                            MipMi.append(mi)
                            MipObj.append(mesh)
                else:                   
                    shapes=mc.listRelatives(mesh,s=1,f=1)    
                    if shapes :
                        mi=mc.getAttr(shapes[0]+'.miProxyFile')
                        if mi and re.search('.mi',mi)!=None and re.search('/',mi)!=None:
                            RenderMi.append(mi)
                            RenderMesh.append(shapes[0])
        return [RenderMi,RenderMesh,MipMi,MipObj] 
#=================================================================================
#适用   代理转换
#Author : 韩虹
#=============================================================== 
    def MRProxySetNew(self,degree='h',infoType='Fx',sl=1,kdegree=1,kinfoType=1):
        MiInfo=[]
        if sl==1: 
            MiInfo=self.MRProxyRecordSel() 
        else:
            MiInfo=self.MRProxyRecord()   
        RenderMi=MiInfo[0]
        RenderMesh=MiInfo[1]
        MipMi=MiInfo[2]
        MipObj=MiInfo[3]
        if infoType in ['Fx','FX']:
            meshs=self.proxy_GDMeshList(attrtype='GD')[0]+self.proxy_GDMeshList(attrtype='FX')[0]
            if meshs:
                for k in range(len(meshs)):
                    if mc.ls(meshs[k]):
                        mc.setAttr((meshs[k]+'.castsShadows'),0)
                        mc.setAttr((meshs[k]+'.receiveShadows'),0)
                        mc.setAttr((meshs[k]+'.primaryVisibility'),0) 
        if infoType in ['frgb','FXrgb'] and degree=='l':
            self.nj_proxylightSet(1,0) 
            meshs=self.proxy_GDMeshList(attrtype='GD')[0]+self.proxy_GDMeshList(attrtype='FX')[0]
            objs=[]
            if meshs:
                for m in range(len(meshs)): 
                    if mc.objExists(meshs[m]+'.castsShadows'):
                        mc.setAttr((meshs[m]+'.castsShadows'),1)
                        mc.setAttr((meshs[m]+'.receiveShadows'),1)
                        mc.setAttr((meshs[m]+'.primaryVisibility'),1)                     
                        obj=mc.listRelatives(meshs[m],p=1,f=1) 
                        if mc.objExists(obj[0]):
                            objs.append(obj[0])                                    
            if objs:            
                shaderMatte = 'SHD_Matte_Shader'
                if mc.ls(shaderMatte):
                    mc.delete(shaderMatte)
                MatteSG = shaderMatte+'SG'
                if mc.ls(MatteSG):
                    mc.delete(MatteSG)
                shaderMatte = mc.shadingNode('lambert', asShader=True, name = shaderMatte)
                MatteSG = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name = MatteSG)
                
                mc.setAttr((shaderMatte + '.color'), 0, 0, 0, type='double3')
                mc.setAttr((shaderMatte + '.ambientColor'), 1, 1, 1, type='double3')
                mc.setAttr((shaderMatte + '.diffuse'), 1)
                mc.setAttr((shaderMatte + '.matteOpacityMode'), 0)
                mc.connectAttr((shaderMatte + '.outColor'), (MatteSG + '.surfaceShader'))
                
                try:
                    mc.sets(objs,e = 1 , forceElement = MatteSG)
                except:
                    for mesh in objs:
                        try:
                            mc.sets(mesh,e = 1 , forceElement = MatteSG)
                        except:
                            print mesh
                            print(u'===请检查本行上方，其无法正常着色===')
                            mc.error(u'===请检查本行上方，其无法正常着色===')
                            print '\n'                 
        if infoType=='night' and sl==0:
            self.nj_proxylightSet(1,0) 
        if infoType!='night' and sl==0:
            self.nj_proxylightSet(0,0) 
        if infoType=='night' and sl==1:
            self.nj_proxylightSet(1,1) 
        if infoType!='night' and sl==1:
            self.nj_proxylightSet(0,1)                                                                                                                                   
        if RenderMi and infoType!='ncolor':
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                mipath=RenderMi[i].replace(short,'')
                
                fxshort=''
                if kdegree==0 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+infoType+'.mi'
                if kdegree==1 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+short.split('_')[1]+'_'+infoType+'.mi' 
                if kdegree==0 and kinfoType==1:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+short.split('_')[2]                                        
                if fxshort not in mc.getFileList(folder=mipath) and short.split('_')[0][-1] in ['H']:
                    fxshort=mipath.split('/')[-2]+'_'+degree+'_'+infoType+'.mi'                
                if fxshort in mc.getFileList(folder=mipath):              
                    mc.setAttr((RenderMesh[i]+'.miProxyFile'),(mipath+fxshort),type='string')
        if  MipMi and infoType!='ncolor':
            for i in range(len(MipMi)):
                short=MipMi[i].split('/')[-1]
                mipath=MipMi[i].split(short)[0]
                
                fxshort=''
                if kdegree==0 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+infoType+'.mi'
                if kdegree==1 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+short.split('_')[1]+'_'+infoType+'.mi' 
                if kdegree==0 and kinfoType==1:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+short.split('_')[2]  
                
                if fxshort not in mc.getFileList(folder=mipath) and short.split('_')[0][-1] in ['H']:
                    fxshort=mipath.split('/')[-2]+'_'+degree+'_'+infoType+'.mi'   
                     
                if fxshort in mc.getFileList(folder=mipath):
                    mesh=mc.listRelatives(MipObj[i],s=1,f=1)[0]
                    cons=mc.listConnections((MipObj[i]+'.miGeoShader'),p=0,c=1)
                    if cons:
                        mc.delete(cons[1])
                    mc.setAttr((MipObj[i]+'.miExportGeoShader'),0)
                    mc.setAttr((mesh+'.miProxyFile'),(mipath+fxshort),type='string')           
        if infoType=='ncolor' and  MipMi:
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                mipath=RenderMi[i].replace(short,'')
                
                fxshort=''
                if kdegree==0 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+infoType+'.mi'
                if kdegree==1 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+short.split('_')[1]+'_'+infoType+'.mi' 
                if kdegree==0 and kinfoType==1:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+short.split('_')[2] 
                cons=[]                     
                if mc.objExists(MipObj[i]+'.miGeoShader'):                   
                
                    cons=mc.listConnections((MipObj[i]+'.miGeoShader'),p=0,c=1)
                
                if cons and mc.getAttr(MipObj[i]+'.miExportGeoShader')==True and fxshort in mc.getFileList(folder=mipath):
                    mipnode=cons[1]
                    mc.setAttr((mipnode+'.object_filename'),(mipath+fxshort),type='string')
                                    
        if infoType=='ncolor' and  RenderMi:
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                mipath=RenderMi[i].replace(short,'')
                
                fxshort=''
                if kdegree==0 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+infoType+'.mi'
                if kdegree==1 and kinfoType==0:
                    fxshort=short.split('_')[0]+'_'+short.split('_')[1]+'_'+infoType+'.mi' 
                if kdegree==0 and kinfoType==1:
                    fxshort=short.split('_')[0]+'_'+degree+'_'+short.split('_')[2]    
               
                if  fxshort in mc.getFileList(folder=mipath):
                    mc.setAttr((RenderMesh[i]+'.miProxyFile'),'',type='string') 
                    mesh=mc.listRelatives(RenderMesh[i],p=1,f=1)[0]
                    mipnode=fxshort.split('_n')[0]+'_mip_binaryproxy_'
                    mipnode=mc.createNode ('mip_binaryproxy',n=mipnode)
                    mc.setAttr((mipnode+'.object_filename'),(mipath+fxshort),type='string')
                    mc.setAttr((mesh+'.miExportGeoShader'),1)
                    try:
                        mc.connectAttr((mipnode+'.outValue'),(mesh+'.miGeoShader'),f=1)   
                    except:
                        pass                                 
        print    u'已经完成代理转换'
        return 0 
####================================
#============适用于19 20 集===========
    def MRProxySetNew_19(self,degree='h',infoType='Rnight',sl=1,kdegree=1,kinfoType=1):
        if infoType in ['FX','FXrgb']:
            self.nj_proxylightSet_019(c='r',sl=sl,win=0,volum=0) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=0,p=1)             
        self.MRProxySetNew(degree=degree,infoType=infoType,sl=sl,kdegree=kdegree,kinfoType=kinfoType)         
        if infoType=="Rnight" :
            self.nj_proxylightSet_019(c='r',sl=sl,win=1,volum=1) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=1,p=1)                     
        if infoType=="Gnight":
            self.nj_proxylightSet_019(c='g',sl=sl,win=1,volum=1) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=1,p=1)                  
        if infoType=="rgb":
            self.nj_proxylightSet_019(c='r',sl=sl,win=0,volum=0) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=0,p=1) 
        if infoType=="rgb01":
            self.nj_proxylightSet_019(c='r',sl=sl,win=0,volum=0) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=0,p=1)    
        if infoType=="rgb02":
            self.nj_proxylightSet_019(c='r',sl=sl,win=0,volum=0) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=0,p=1)                       
        if infoType=="day":          
            self.nj_proxylightSet_019(c='g',sl=sl,win=0,volum=0) 
            self.nj_proxyMeshSet_019(info='lantern',sl=sl,vis=1,p=1)         
        if infoType=="ncolor":          
            self.nj_proxylightSet_019(c='r',sl=sl,win=0,volum=0) 
                         

#暂时使用
    def lightExr(self):
        shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
        lightpath='D:/Info_Temp/temp/light/'+shotInfos[0]+'/'
        lightname=shotInfos[1]+'_light'
        constraints=mc.ls(type='parentConstraint',l=1)+mc.ls(type='scaleConstraint',l=1)
        mc.delete(constraints)
        lightGroup=mc.ls('*light',l=1)
        mc.sysFile(lightpath,makeDir=True)
        if lightGroup:
            mc.select(lightGroup)
            mc.parent(w=1)
            mc.file((lightpath+lightname),options='v=0',f=1,type='mayaBinary',preserveReferences=1,es=1)
            print u'已经导出灯光'
        else:
            print u'缺少灯光' 

    def proxyLightSet(self):
    	meshs=mc.ls(type='mesh',l=1)
    	shotInfos = sk_infoConfig.sk_infoConfig().checkShotInfo()
    	lightpath='D:/Info_Temp/temp/light/'+shotInfos[0]+'/'
    	lightname=shotInfos[1]+'_light.mb'
    	mc.file((lightpath+lightname),i=1,pr=1,namespace=shotInfos[1]) 
    	sk_sceneTools.sk_sceneTools().sk_sceneNoRefNamespaceClean()
    	lightGroup='light'
    	chacur='|SET|MODEL|Master_GRP|Master|Move_ctrl|Character'
    	mc.parent(lightGroup,chacur)
    	
    	
    	mipath='//file-cluster/GDC/Projects/Ninjago/Project//data/proxy/PorxyFiles/'
    	mi=mipath+shotInfos[1]+'_l_night.mi'
    	if meshs:
    		mc.setAttr((meshs[0]+'.miProxyFile'),mi,type='string')
    
    	mc.file(save=1,type = 'mayaBinary',f = 1)   

    def MRProxyHLSelect(self,degree='h'):
        MiInfo=self.MRProxyRecord()   
        RenderMi=MiInfo[0]
        RenderMesh=MiInfo[1]
        MipMi=MiInfo[2]
        MipObj=MiInfo[3]
        ModH=[]
        ModL=[]
        if RenderMi:
            for i in range(len(RenderMi)):
                short=RenderMi[i].split('/')[-1]
                if re.search('_h_',short):
                    mesh=mc.listRelatives(RenderMesh[i],p=1,f=1)[0]
                    ModH.append(mesh)
                if re.search('_l_',short):
                    mesh=mc.listRelatives(RenderMesh[i],p=1,f=1)[0]
                    ModL.append(mesh) 
        if MipMi:
            for j in range(len(MipMi)):
                short=MipMi[j].split('/')[-1]
                if re.search('_h_',short):
                    ModH.append(MipObj[j])
                if re.search('_l_',short):
                    ModL.append(MipObj[j]) 
        if degree=='h' and ModH: 
            mc.select(cl=1)
            mc.select(ModH)
        if degree=='h' and ModH==None: 
            mc.error('No proxy_h' )
        if degree=='l' and ModL: 
            mc.select(cl=1)
            mc.select(ModL)
        if degree=='l' and ModH==None: 
            mc.error('No proxy_l' )                                                      

    def nj_proxylightSet(self,key=0,sl=1):
        if sl==0:
            lightGroup=mc.ls('*:*:*light',type='transform',l=1)+mc.ls('*:*light',type='transform',l=1)+mc.ls('light',type='transform',l=1)
            if lightGroup:
                for light in lightGroup:
                    if re.search('Character',light)!=None and re.search('MODEL',light)!=None and re.search('Move_ctrl',light)!=None:
                        mc.setAttr((light+'.visibility'),key)                
        if sl==1:
            objs=mc.ls(sl=1,l=1,type='transform')
            if objs:
                for obj in objs:
                    if re.search('SET',obj)!=None and re.search('MODEL',obj)!=None and re.search('Master_GRP',obj)!=None and re.search('Character',obj)!=None and re.search('group',obj)!=None:
                        objshort= obj.split('|')[-1]
                        objPro=obj.split(obj.split('|')[-2])[0]
                        namespace=objshort.split(objshort.split(':')[-1])[0] 
                        light=objPro+namespace+'light'
                        if mc.ls(light):
                            mc.setAttr((light+'.visibility'),key) 
                            
    def nj_proxylightSet_13(self,key=0,sl=1):
        if sl==0:
            lightGroup=mc.ls('*:*:*light',type='transform',l=1)+mc.ls('*:*light',type='transform',l=1)+mc.ls('light',type='transform',l=1)
            if lightGroup:
                for light in lightGroup:
                    mc.setAttr((light+'.visibility'),key)                
        if sl==1:
            objs=mc.ls(sl=1,l=1,type='transform')
            if objs:
                for obj in objs:
                    objshort= obj.split('|')[-1]
                    objPro=obj.split(obj.split('|')[-2])[0]
                    namespace=objshort.split(objshort.split(':')[-1])[0] 
                    light=objPro+namespace+'light'
                    if mc.ls(light):
                        mc.setAttr((light+'.visibility'),key)
                            
    def nj_proxylightSet_019(self,c='r',sl=1,win=1,volum=0):
        winlight=[]
        volumlight=[]
        if sl==0:
            lightGroup=mc.ls(lt=1,l=1)
            if lightGroup:
                for light in lightGroup:
                    lightT=mc.listRelatives(light,p=1,f=1)
                    if lightT and mc.objExists(lightT[0]+'.winlight'):
                        winlight.append(lightT[0])
                    if lightT and mc.objExists(lightT[0]+'.volumeLight'):          
                        volumlight.append(lightT[0])
        if sl==1:
            objs=mc.ls(sl=1,l=1)
            lightGroup=mc.ls(lt=1,l=1)
            if objs:
                for obj in objs:
                    if '|' in obj and '_' in obj:
                        shotInfo=obj.split('|')
                        if lightGroup:
                            for light in lightGroup:
                                lightT=mc.listRelatives(light,p=1,f=1)
                                if lightT and shotInfo[0] in lightT[0] and shotInfo[1] in lightT[0] and shotInfo[2] in lightT[0] and mc.objExists(lightT[0]+'.winlight'):
                                    winlight.append(lightT[0])
                                if lightT and shotInfo[0] in lightT[0] and shotInfo[1] in lightT[0] and shotInfo[2] in lightT[0] and mc.objExists(lightT[0]+'.volumeLight'):
                                    volumlight.append(lightT[0])    
                                                                                        
            else:
                print u'请选择物体'
        if winlight:
            for light in winlight:
                mc.setAttr((light+'.visibility'),int(win))
        if volumlight:
            for light in volumlight:
                mc.setAttr((light+'.visibility'),int(volum)) 
    
        lights=winlight+volumlight
        if lights and c=='r':
            for light in lights:
                lightshape=mc.listRelatives(light,s=1,f=1) 
                if lightshape:
                    mc.setAttr((lightshape[0]+'.color'),1,0.263,0.144,type='double3')   
        if lights and c=='g':
            for light in lights:
                lightshape=mc.listRelatives(light,s=1,f=1) 
                if lightshape:
                    mc.setAttr((lightshape[0]+'.color'),0.4,1,0.4,type='double3')                                                   
        return [0]  

    def nj_proxylightSelect_019(self,sl=0,win=1,volum=0):
        winlight=[]
        volumlight=[]
        if sl==0:
            lightGroup=mc.ls(lt=1,l=1)
            if lightGroup:
                for light in lightGroup:
                    lightT=mc.listRelatives(light,p=1,f=1)
                    if lightT and mc.objExists(lightT[0]+'.winlight'):
                        winlight.append(lightT[0])
                    if lightT and mc.objExists(lightT[0]+'.volumeLight'):          
                        volumlight.append(lightT[0])
        if sl==1:
            objs=mc.ls(sl=1,l=1)
            lightGroup=mc.ls(lt=1,l=1)
            if objs:
                for obj in objs:
                    if '|' in obj and '_' in obj:
                        shotInfo=obj.split('|')
                        if lightGroup:
                            for light in lightGroup:
                                lightT=mc.listRelatives(light,p=1,f=1)
                                if lightT and shotInfo[0] in lightT[0] and shotInfo[1] in lightT[0] and shotInfo[2] in lightT[0] and mc.objExists(lightT[0]+'.winlight'):
                                    winlight.append(lightT[0])
                                if lightT and shotInfo[0] in lightT[0] and shotInfo[1] in lightT[0] and shotInfo[2] in lightT[0] and mc.objExists(lightT[0]+'.volumeLight'):
                                    volumlight.append(lightT[0])    
                                                                                        
            else:
                print u'请选择物体'
        if win==1 and volum==0 and winlight:
            mc.select(winlight)
        if  volum==1 and win==0 and volumlight:
            mc.select(volumlight)
        Alllights=winlight+volumlight
        if win==1  and volum==1  and  Alllights:
            mc.select(Alllights)                      
                                             
        return 0         
#======================================================
#===========适用于乐高19集================
#===========韩虹创建于2015/1/6==============
    def nj_proxyMeshSet_019(self,info='lantern',sl=1,vis=0,p=1):
        meshlist=self.nj_proxyMeshList(info=info,sl=sl)
        if meshlist:
            for mesh in meshlist:
                mc.setAttr((mesh+'.visibility'),vis)
        if p==1 and meshlist:
            MiInfo=[]
            MiMeshList=[]
            if sl==1: 
                MiInfo=self.MRProxyRecordSel() 
            else:
                MiInfo=self.MRProxyRecord()   
            RenderMi=MiInfo[0]
            RenderMesh=MiInfo[1]
            MipMi=MiInfo[2]
            MipObj=MiInfo[3] 
            if RenderMesh:
                for i in range(len(RenderMesh)):
                    obj=mc.listRelatives(RenderMesh[i],p=1,f=1)
                    if obj and mc.objExists(obj[0]+'.lantern')==False:
                        MiMeshList.append(RenderMesh[i])   
            if  MiMeshList : 
                for j in  range(len(MiMeshList)):
                    if '|' in MiMeshList[j] and '_' in mc.getAttr(MiMeshList[j]+'.miProxyFile'):
                        shortinfo=MiMeshList[j].split('|')
                        for k in range(len(meshlist)):
                            if  shortinfo[0] in meshlist[k] and shortinfo[1] in  meshlist[k]  and    shortinfo[2] in  meshlist[k] :
                                mesh=mc.listRelatives(meshlist[k],s=1,f=1)
                                if mesh and mc.objExists(mesh[0]+'.miProxyFile') and mc.getAttr(mesh[0]+'.miProxyFile')!=None:
                                    Mi=mc.getAttr(mesh[0]+'.miProxyFile')
                                    Mishot= Mi.split('_')[-1]
                                    bfMi= mc.getAttr(MiMeshList[j]+'.miProxyFile').split('_')[-1]
                                    Mif=Mi.replace(Mishot,bfMi)
                                    mc.setAttr((mesh[0]+'.miProxyFile'), Mif,type='string')                                                                       
#==============
    def nj_proxyMeshList(self,info='lantern',sl=1):
        meshlist=[]
        if sl==0:
            meshGroup=mc.ls(type='mesh',l=1)
            if meshGroup:
                for mesh in meshGroup:
                    obj=mc.listRelatives(mesh,p=1,f=1)
                    if obj and mc.objExists(obj[0]+'.'+info):
                        meshlist.append(obj[0])
        if sl==1:
            objs=mc.ls(sl=1,l=1)
            meshGroup=mc.ls(type='mesh',l=1)
            if objs:
                for obj in objs:
                    if '|' in obj and '_' in obj:
                        shotInfo=obj.split('|')
                        if meshGroup:
                            for mesh in meshGroup:
                                meshT=mc.listRelatives(mesh,p=1,f=1)
                                if meshT and shotInfo[0] in meshT[0] and shotInfo[1] in meshT[0] and shotInfo[2] in meshT[0] and mc.objExists(meshT[0]+'.'+info):
                                    meshlist.append(meshT[0])                                                                  
                                                                                        
            else:
                print u'没有选择物体，请选择物体'
        return  meshlist                                       
    def nj_mrproxyExr(self,infoType='roof'):
        shotInfo = sk_infoConfig.sk_infoConfig().checkShotInfo()
        proxypath='//file-cluster/gdc/Projects/Ninjago/Project/data/proxy/PorxyFiles/'
        proxyname=shotInfo[1]+'_'+shotInfo[2]+'_'+infoType+'.mi'
        meshAll=[]
        meshs=mc.ls(type='mesh',l=1)
        if meshs:
            for mesh in meshs:
                if re.search('|SET|MODEL|MSH_all',mesh)!=None and re.search('SET',mesh)!=None and re.search(shotInfo[1],mesh)!=None:
                    objs=mc.listRelatives(mesh,p=1,f=1)
                    if objs:
                       meshAll.append(objs[0]) 
        if meshAll:
            mc.select(meshAll)
            mc.file((proxypath+proxyname),options='binary=1;compression=0;tabstop=8;perframe=0;padframe=0;perlayer=0;pathnames=3313333333;assembly=1;fragment=1;fragsurfmats=1;fragsurfmatsassign=1;fragincshdrs=1;fragchilddag=1;passcontrimaps=1;passusrdata=0;filter=00000011010000001101000;overrideAssemblyRootName=0;assemblyRootName=',f=1,type='mentalRay',preserveReferences=1,es=1)    

    def proxyAreaLightSet(self,key=1,sel=0):
        areaLights=mc.ls(type='areaLight',l=1)
        Lights=[]
        for ares in areaLights:
            if re.search('MODEL',ares)!=None and re.search('Character',ares)!=None and re.search('light',ares.lower())!=None:
                art=mc.listRelatives(ares,p=1,f=1)
                if art:
                    Lights.append(art[0])
        if Lights and key==0 and sel==0:
            for i in range(len(Lights)):
                mc.setAttr((Lights[i]+'.visibility'),0)
        if Lights and key==1 and sel==0:
            for i in range(len(Lights)):
                mc.setAttr((Lights[i]+'.visibility'),1)    
        if Lights and key==0 and sel==1:
            mc.select(cl=1)
            mc.select(Lights)
        if not Lights:
            mc.error(u'代理文件中没有面光')                                            	                                                                                                                                                                                                                                                       
            
    def proxyAreaLightSet_13(self,key=1,sel=0):
        areaLights=mc.ls(type='areaLight',l=1)
        Lights=[]
        for ares in areaLights:
            art=mc.listRelatives(ares,p=1,f=1)
            if art:
                Lights.append(art[0])
        if Lights and key==0 and sel==0:
            for i in range(len(Lights)):
                mc.setAttr((Lights[i]+'.visibility'),0)
        if Lights and key==1 and sel==0:
            for i in range(len(Lights)):
                mc.setAttr((Lights[i]+'.visibility'),1)    
        if Lights and key==0 and sel==1:
            mc.select(cl=1)
            mc.select(Lights)
        if not Lights:
            mc.error(u'代理文件中没有面光') 
            
    def breakeAllProxyPath(self):
        Shapes = mc.ls(type='mesh',l=1)
        for shape in Shapes:
            mc.setAttr((shape+'.miProxyFile'),'',type='string')

    def breakeSelectProxyPath(self):       
        Transforms = mc.ls(sl=1,l=1)
        if len(Transforms) == 0:
            mc.warning(u'===请选择模型===')
        else:
            for transform in Transforms:
                shapes = mc.listRelatives (transform,children=1,type='mesh')
                for shape in shapes:
                    mc.setAttr((shape+'.miProxyFile'),'',type='string')   
   