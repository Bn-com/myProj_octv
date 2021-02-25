# -*- coding: utf-8 -*-
import maya.cmds as mc
def CJW_resetShadingEngines():
    Comm = mc.confirmDialog(title=u'重新连接SG节点', message=u'严重警告：   运行本插件前请保存文件。\n警告：\n    本插件不能在有‘渲染层’的文件里运行。\n声明：\n    本插件为辅助前期材质人员批量刷新SG节点。\n运行此插件后可能导致材质异常，请使用后详细检查材质。',button=[u'确认',u'取消'], defaultButton=u'确认', cancelButton=u'取消', dismissString=u'取消')
    if Comm == u'确认':
        SGNodes =mc.ls(type = 'shadingEngine')
        for sgNode in SGNodes:
            if 'initialShadingGroup' not in sgNode and 'initialParticleSE' not in sgNode:
                print sgNode
                shaderAttr = mc.listConnections((sgNode + '.surfaceShader'),source = 1,plugs = 1)
                if shaderAttr:
                    meshs=mc.sets(sgNode,q=1)
                    mc.lockNode(sgNode, l=0)
                    mc.delete(sgNode)
                    newSGNode = mc.sets(renderable=True, noSurfaceShader=True, empty=True, name= (sgNode))
                    mc.connectAttr( shaderAttr[0], (newSGNode + '.surfaceShader'))
                    if meshs:
                        mc.sets( meshs, e=1, forceElement=newSGNode)
                        print (sgNode+'  ===Done===!')