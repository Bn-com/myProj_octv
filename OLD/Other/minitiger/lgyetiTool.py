# -*- coding: utf-8 -*-

__author__ = 'luogang'

import pymel.core as pm
import maya.mel as mel

def LgYetiToolWindow():
    if pm.window  ('yetiTool',exists = True):
        pm.deleteUI ('yetiTool',wnd = True)

    pm.window ('yetiTool',title = u'YETI工具')
    form = pm.formLayout()
    b1 = pm.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
    pm.button(h=50,l=u'将毛发转换成曲线',ann=u'选择pgYetiMaya节点',c=yetiConvertCurves)
    pm.button(h=50,l=u'将曲线转换成groom',ann=u'选择曲线set组和groom要生长的模型',c=curvesConvertGroom)
    pm.button(h=50,l=u'为Groom替换模型',ann=u'选择模型和groom',c=meshConnectingGroom)
    pm.button(h=50,l=u'YETI texture节点',ann=u'一键修改V Coordinate属性',c=setYetiTextrueNode)
    pm.button(h=50,l=u'aiHair属性修改',ann=u'一键修改材质球UVparamcoord属性',c=setAiHairUvparamcoord)

    pm.setParent( '..' )

    pm.formLayout( form, edit=True,
    attachForm=[(b1, 'top', 10)])

    pm.showWindow()
    pm.window ('yetiTool' ,edit=True, wh= (250 ,350) )

def yetiConvertCurves(*args):     #选择毛发转换成curves曲线
    oldSelect = pm.ls(type='transform')
    pgYetiMaya = pm.ls(sl = True)
    pm.pgYetiCommand(generateMayaObjects=1)
    newSelect = pm.ls(type='transform')
    for obj in oldSelect:
        newSelect.remove(obj)
    shapes = newSelect[-1].getChildren()
    curvesChilds = []
    n=1
    for shape in shapes:
        curvesChild = pm.group( empty = True,n= 'pgyeti_curves'+str(n))
        pm.parent(shape,'pgyeti_curves'+str(n),add=1,s=1)
        pm.rename(shape, 'pgyeti_curves'+ 'Shape' +str(n))
        n += 1
        curvesChilds.append(curvesChild)
    curves_groupName = pm.group(curvesChilds,n = str(pgYetiMaya[0])+'_curves')
    pm.delete (newSelect[0])
    pm.select(pm.PyNode(curves_groupName).getChildren())
    pm.sets(name= curves_groupName + '_set')

def setYetiTextrueNode(*args):     #u'批量修改yeti texture下的Vcoord属性'

    pgYetiMayaGraphs = pm.ls( type='pgYetiMaya')
    for pgYetiMayaGraph in pgYetiMayaGraphs:
        textureNodes = pm.pgYetiGraph (pgYetiMayaGraph.getParent(),listNodes= True,type="texture")
        for textureNode in textureNodes:
            pm.pgYetiGraph(pgYetiMayaGraph, node= textureNode, param= 'vCoord',setParamValueExpr = '1-$t')

def setAiHairUvparamcoord(*args):    #aihair材质球修改UV属性
    aiHairs = pm.ls( type='aiHair')
    for aiHair in aiHairs:
        pm.PyNode(aiHair).uparam.set('uparamcoord')
        pm.PyNode(aiHair).vparam.set('vparamcoord')

def meshConnectingGroom(*args):    #groom连接新的模型
    objs = pm.ls(sl=True)
    for obj in objs:
        if 'PgYetiGroom' in str(type(obj.getShape())):
            groom =  obj
        if 'Mesh' in str(type(obj.getShape())):
            mesh = obj
    mesh.worldMesh[0] >> groom.inputGeometry

def curvesConvertGroom(*args):    #曲线转换成groom
    objs = pm.ls(sl=True)
    curves = ''
    for obj in objs:
        if 'ObjectSet' in str(type(obj)):
            curves = obj
        if 'Transform' in str(type(obj)):
            mesh =  obj.getShape()
    mel.eval('pgYetiConvertGuideSetToGroom("%s","%s")'%(curves,mesh))

if __name__ == '__main__':
    LgYetiToolWindow()

