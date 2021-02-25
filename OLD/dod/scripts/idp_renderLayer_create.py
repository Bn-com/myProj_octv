# -*- coding: utf-8 -*-

from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_infoConfig
reload(sk_infoConfig)
import maya.cmds as mc

def csl_IDRenderLayerCreatAll(type='chr'):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNamespace = mc.namespaceInfo(listOnlyNamespaces=1)
        if mc.objExists('CAM'):
            refNamespace .remove('CAM')
        if mc.objExists('UI'):
            refNamespace .remove('UI')
        if mc.objExists('shared'):
            refNamespace .remove('shared')
        serverPath = sk_infoConfig.sk_infoConfig().checkProjectServerPath()
        #self.csl_RefIm()
        mel.eval('source "zzjUtilityTools.mel";lighting_DeleteUnusedNode()')
        specialType = 0
        mc.select(clear=1)
        objselect = []
        objs = []
        if type == 'chr':
            for ns in refNamespace:
                if '_' not in ns:
                    continue
                if ns.split('_')[1][specialType] in ['c']:
                    objname = ns.split('_')[1]
                    if mc.objExists(ns + ':MSH_all'):
                        needMeshFull = mc.ls((ns + ':MSH_all'), l=1)[0]
                        for i in range(10):
                            idserpath = serverPath + 'data/RLayerInfo/RGB/id0' + str(i) + '/'
                            if idserpath.split('/')[-2] in mc.getFileList(folder=serverPath + 'data/RLayerInfo/RGB/')and objname in mc.getFileList(folder=idserpath):
                                idLayer = 'chaId0' + str(i)
                                if mc.objExists(idLayer):
                                    mc.editRenderLayerMembers(idLayer, needMeshFull, noRecurse=0)
                                    mc.editRenderLayerGlobals(currentRenderLayer=idLayer)
                                else:
                                    mc.createRenderLayer(needMeshFull, name=idLayer, noRecurse=1, makeCurrent=1)
                                comm = 'self.csl_RGBApply("id0' + str(i) + '")'
                                mc.select(needMeshFull)
                                eval(comm)
                            else:
                                pass

        if type == 'set':
            for ns in refNamespace:
                if '_' not in ns:
                    continue
                if ns.split('_')[1][specialType] in ['s']:
                    objname = ns.split('_')[1]
                    if mc.objExists(ns + ':MODEL'):
                        needMeshFull = mc.ls((ns + ':MODEL'), l=1)[0]
                        for i in range(10):
                            idserpath = serverPath + 'data/RLayerInfo/RGB/id1' + str(i) + '/'
                            if idserpath.split('/')[-2] in mc.getFileList(folder=serverPath + 'data/RLayerInfo/RGB/')and objname in mc.getFileList(folder=idserpath):
                                idLayer = 'setId1' + str(i)
                                if mc.objExists(idLayer):
                                    mc.editRenderLayerMembers(idLayer, needMeshFull, noRecurse=0)
                                    mc.editRenderLayerGlobals(currentRenderLayer=idLayer)
                                else:
                                    mc.createRenderLayer(needMeshFull, name=idLayer, noRecurse=1, makeCurrent=1)
                                comm = 'self.csl_RGBApply("id1' + str(i) + '")'
                                mc.select(needMeshFull)
                                eval(comm)
                            else:
                                pass
        mc.setAttr("defaultRenderLayer.renderable", 0)
        mc.editRenderLayerGlobals(currentRenderLayer="defaultRenderLayer")
        return 0