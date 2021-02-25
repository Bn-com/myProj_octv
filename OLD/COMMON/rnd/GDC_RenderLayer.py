# -*- coding: utf-8 -*-
# 【通用】【创建层工具】
#  Author : 韩虹
#  Data   : 2015
import maya.cmds as mc
import maya.mel as mel
import re
import sys
sys.path.append('E:/GIT/GDC_Repository/COMMON/rnd')
import GDC_ProjectInfo
reload(GDC_ProjectInfo)
class GDC_RenderLayer(object):
    def __init__(self):
        pass

    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
# 【通用】【创建层面板】
#  Author : 韩虹
#  Data   : 2015

    def createlayerUI(self):
    # 窗口
        #    Create a window with a some fields for entering text.
        #
        if mc.window('RenderToolsWin', exists=True):
            mc.deleteUI('RenderToolsWin')
        mc.window('RenderToolsWin', title=u'创建渲染层',
                  width=200, height=100, sizeable=True)
        form = mc.formLayout()
        mc.rowColumnLayout( numberOfColumns=1)
        t=mc.text( label=u'层名',width=200)
        t=mc.text(label='',height=10)
        b1=mc.textField('RenderLayerName',width=200)
        t=mc.text(label='',height=10)
        b2=mc.button(label=u'建层',command='import GDC_RenderLayer\nreload(GDC_RenderLayer)\nGDC_RenderLayer.GDC_RenderLayer().createlayer(1)')
        mc.showWindow('RenderToolsWin')
    #----------------------------------------------------------------------------------------------------------#      #----------------------------------------------------------#
# 【通用】【创建层工具】
#  Author : 韩虹
#  Data   : 2015
    #type==1,读取建层面板的名字
    #type==0,只读取name
    def createlayer(self,type=1,name=''):
        layername=''
        if type==1:
            layername=mc.textField('RenderLayerName',q=1,tx=1)
            if name=='':
                layername=layername
            else:
                layername=layername+'_'+name
        else:
            layername=name
        objs=self.meshinfo()
        if objs:
            mc.createRenderLayer(objs,name=layername, noRecurse=1, makeCurrent=1)
            mc.setAttr("defaultRenderLayer.renderable", 0)
        return 0
    #----------------------------------------------------------------------------------------------------------#      #-------------------------
# 【辅助】【选择建层物体（灯光，多边形物体，nurbs物体，代理】
#  Author : 韩虹
#  Data   : 2015
    #type==1,读取建层面板的名字
    #type==0,只读取name
    def meshinfo(self):
        objs=mc.ls(sl=1,type='transform',l=1)
        sha=mc.ls(lt=1,l=1)+mc.ls(type='mesh',l=1)
        type=['nurbsSurface','aiSkyDomeLight','aiAreaLight','aiPhotometricLight','aiStandIn']
        meshinfo=[]
        if mc.ls(objs):
            for i in range(len(objs)):
                shape=mc.listRelatives(objs[i], s=1,f=1)
                if shape and mc.nodeType(shape[0]) in type:
                    meshinfo.append(objs[i])
                if shape and shape[0] in sha:
                    meshinfo.append(objs[i])
        else:
            mc.error(u'没有选择物体，请选择物体')
        return meshinfo








