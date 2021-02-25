# -*- coding: utf-8 -*-
import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json
import tempfile
import tiFile as tiFile
reload(tiFile)

import tiBase as  tiBase
reload(tiBase)

import tiPath as  tiPath
reload(tiPath)

import tiBatchCmd as tiBatchCmd
reload(tiBatchCmd)

import tiLog as tiLog
reload(tiLog)

class tiAlembic(tiFile.tiAnimFile):
    """docstring for ClassName"""
    def __init__(self, *args):
        super(tiAlembic, self).__init__(*args)

        self.chrs = []
        self.props = []
        self.sets = []
        
        errorInfo = []

        refFiles = pm.system.listReferences()

        if not refFiles:
            errorInfo.append(u'场景中没有找到任何参考文件')

        chrPattern = re.compile('^%s_c' % self.proj, re.I)
        propPattern = re.compile('^%s_p' % self.proj, re.I)
        setPattern = re.compile('^%s_s' % self.proj, re.I)

        legalRefPattern = re.compile('%s_(c|p|s).+_h_(ms_anim|ms_render).(ma|mb)' % self.proj, re.I)
        rgMoPattern = re.compile('%s_(c|p|s).+_h_(rg|mo).(ma|mb)' % self.proj, re.I)

        for rf in refFiles:
            if rf.isLoaded():
                refPath =  rf.path
                baseName = os.path.basename(refPath)
                if legalRefPattern.match(baseName):
                    if chrPattern.match(baseName):
                        self.chrs.append(rf)
                    elif propPattern.match(baseName):
                        self.props.append(rf)
                    elif setPattern.match(baseName):
                        self.sets.append(rf)
                elif rgMoPattern.match(baseName):
                    
                    errorInfo.append(u'参考文件不应该是mo或者rg,请替换成ms_anim或ms_render文件: %s' % refPath)

            else:
                try:
                    print u'参考没有勾选，删除: %s' % ref.path
                    rf.remove()
                except:
                    pass

        try:
            self.renderCamera = self.getRenderCamera()

        except:
            shot = '_'.join([self.ep, self.scene, self.shot])
            camName = 'cam_%s' % shot
            errorInfo.append(u'场景中没有合法的相机: %s' % camName)

        for anim in self.chrs + self.props + self.sets:
            renderFile = self.animToRenderPath(anim.path)
            if not os.path.exists(renderFile):
                errorInfo.append(u'对应的渲染文件不存在: %s -> %s' % (os.path.basename(anim.path), renderFile))
                
            modelGrp = anim.namespace + ':MODEL'
            if not mc.objExists(modelGrp):
                errorInfo.append(u'MODEL组不存在: %s' % modelGrp)
                
        if errorInfo:
            tiLog.print_error(errorInfo)
        else:
            print u'=== File OK ==='


        self.start, self.end, self.duration = tiBase.timeLine()
        self.alembicInfo = {}

        self.unvisibleObjs = self.getUnvisibleLayerObjs()
        self.alembicInfo['hiddenObjs'] = self.unvisibleObjs
        mc.currentUnit(linear = 'cm')
        mc.currentUnit(time = 'pal')
        
        

    def exportAlembicCache(self):

        expAlembicObjs = self.chrs + self.props

        self.alembicInfo['alembic'] = []
        if expAlembicObjs:
            if not mc.pluginInfo('AbcImport',loaded = 1,q = 1):
                mc.loadPlugin('AbcImport')
            if not mc.pluginInfo('AbcExport',loaded = 1,q = 1):
                mc.loadPlugin('AbcExport')

            

            mc.cycleCheck(e = False)
            mc.renderThumbnailUpdate(False)
            mc.ikSystem(e = 1,sol = 1)


            # start, end, duration = tiBase.timeLine()

            abcExpCommand = ''
            
            for exp in expAlembicObjs:

                modelNode = exp.namespace + ':MODEL'
                local, server = self.localAlembicPath(exp.namespace)

                jstr = '-frameRange %d %d -uvWrite  -writeVisibility -worldSpace -root %s -file %s'  % (self.start, self.end, modelNode, local)
                abcExpCommand += ' -j "' + jstr + '"'

        
                self.alembicInfo['alembic'].append({
                    'ns': exp.namespace, 
                    'renderFile': self.animToRenderPath(exp.path),# if os.path.exists(self.animToRenderPath(exp.path)) else self.animToModelPath(exp.path),
                    'localAlembic': local,
                    'serverAlembic': server,
                })

            mel.eval( 'AbcExport -verbose ' + abcExpCommand)

            # copy alembic cache
            total = len(self.alembicInfo['alembic'])
            for idx,info in enumerate(self.alembicInfo['alembic'], 1):
                tiBase.sysMoveFile(info['localAlembic'], info['serverAlembic'], '(%d/%d)' % (idx, total))

        else:
            print '=== no objs need to export alembic cache ==='

        

        # content = json.dumps(self.alembicInfo, indent = 4)

        # print content

        # tiBase.writeFile(content, self.alembicInfoPath)


    def getRenderCamera(self):
        shot = '_'.join([self.ep, self.scene, self.shot])
        camName = 'cam_%s' % shot
        bakeCams = [ x for x in pm.ls(regex = '*:?(%s(?i))_bake' % camName, type = 'transform') if pm.nodeType(x.getShape()) == 'camera']
        
        if bakeCams:
            return bakeCams[0].name()

        cams = [ x for x in pm.ls(regex = '*:?(%s(?i))' % camName, type = 'transform') if pm.nodeType(x.getShape()) == 'camera']
        if cams:
            return cams[0].name()

        mc.error('=== not found legal camera ===')

    def setRenderCamera(self):
        shotCamera = self.getRenderCamera()
        if shotCamera:
            map(lambda x: x.renderable.set(False), pm.ls(type = 'camera'))
            mc.setAttr(shotCamera + '.renderable', True)



    # def getCam(self):
    #     cams = pm.ls(type = 'camera')
        
    #     shot = 'cam_%s' % '_'.join([self.ep, self.scene, self.shot])

    #     canNode = None
    #     for cam in cams:
    #         camParent = cam.getParent().name()
    #         if camParent.startswith(shot):
    #             cam.renderable.set(True)
    #             canNode = camParent
    #             break
    #         else:
    #             cam.renderable.set(False)

    #     else:
    #         mc.error(u'=== not found the right camera: %s ===' % shot )
    #     return canNode

    # def setRenderCamera(self):
    #     cams = pm.ls(type = 'camera')
        
    #     shot = 'cam_%s' % '_'.join([self.ep, self.scene, self.shot])

    #     for cam in cams:
    #         camParent = cam.getParent().name()
    #         cam.renderable.set(camParent.startswith(shot))

    def exportSets(self, newName):
        expObjs = []
        for rf in self.sets:
            rf.selectAll()
            expObjs += mc.ls(sl = True)

        expObjs.append(self.renderCamera)
        if expObjs:
            mc.select(expObjs)
            pm.exportSelected(newName, preserveReferences = True, force = True)


    def setupFsFile(self, checkout = True):
        
        self.cleanFile()

        mc.currentUnit(linear = 'cm')
        mc.currentUnit(time = 'pal')

        for setRef in self.sets:
            rndPath = tiPath.getDollarPath(self.animToRenderPath(setRef.path)) # if os.path.exists(self.animToRenderPath(setRef.path)) else self.moToRenderPath(setRef.path)
            setRef.replaceWith(rndPath)
        newName = self.getNewName()
        self.exportSets(newName)

        pm.openFile(newName, f = True)


        # data = tiBase.jsonRead(self.alembicInfoPath)
        newNamespace = []
        for info in self.alembicInfo['alembic']:
            mc.select(cl = True)
            renderFile = tiPath.getDollarPath(info['renderFile'])
            assetFile = tiFile.tiAssetFile(renderFile)
             
            ns = '_'.join([assetFile.proj, assetFile.id]) #info['ns']

            newNamespace.append(ns)
            newRefFile = pm.createReference(renderFile, namespace = ns)

            cacheRootNode = ns + ':MODEL'
            mc.AbcImport(info['serverAlembic'], mode='import', connect = cacheRootNode)

        self.setNoRenderLayer()



        self.setRenderCamera()

        defaultRenderGlobalsAttrs = {
            'startFrame': self.start,
            'endFrame': self.end
        }

        tiBase.batchSetAttrs('defaultRenderGlobals', defaultRenderGlobalsAttrs)


        pm.saveAs(newName, f = True)
        print u'=== 文件保存在: %s ===' % newName

        if not tiBase.isOEM() and checkout:
            print u'=== start checkout ==='
            tiBatchCmd.checkoutAnim('FinalLayout Base File ')

    def moToRenderPath(self, path):
        pathNew = re.compile(r'model', re.IGNORECASE).sub(r'master', path)
        pathNew = re.compile(r'_mo.(ma|mb)', re.IGNORECASE).sub(r'_ms_render.mb', pathNew)
        return pathNew


    def animToRenderPath(self, path):
        return re.compile(r'_ms_anim.(ma|mb)', re.I).sub(r'_ms_render.mb', path)

    def animToModelPath(self, path):
        newPath = re.compile(r'_ms_anim.(ma|mb)', re.I).sub(r'_mo.mb', path)
        newPath = re.compile(r'master', re.I).sub(r'model', newPath)
        return newPath

    def getUnvisibleLayerObjs(self):
        allHideObjs = []
        layers = pm.ls(type = 'displayLayer')
        for layer in layers:
            if not layer.visibility.get():
                hideObjs = layer.listMembers()
                allHideObjs += [ o.name().split(':')[-1] for o in hideObjs]
        return  allHideObjs

    def setNoRenderLayer(self):

        if self.unvisibleObjs:
            refFiles = pm.system.listReferences()
            toHideObjs = []
            for ref in refFiles:
                ns = ref.namespace
                for obj in self.unvisibleObjs:
                    newObj = '%s:%s' % (ns, obj)
                    if mc.objExists(newObj):
                        toHideObjs.append(newObj)
            if toHideObjs:
                mc.select(cl = True)
                layerName = 'norender'
                if not mc.objExists(layerName):
                    mc.createDisplayLayer(name = layerName, number = 1, nr =  True)
                
                mc.editDisplayLayerMembers(layerName, toHideObjs, nr = True)
                mc.setAttr(layerName + '.visibility', False)


    def cleanFile(self):
        mc.editRenderLayerGlobals(currentRenderLayer = 'defaultRenderLayer')
        layers = mc.ls(type = 'renderLayer')
        for lay in layers:
            if lay != 'defaultRenderLayer':
                try:
                    mc.delete(lay)
                except:
                    pass


        for dlayer in mc.ls(type = 'displayLayer'):
            if dlayer != 'defaultLayer':
                try:
                    mc.delete(dlayer)
                except:
                    pass
       


    def getNewName(self):
        fileName = '_'.join([self.proj,self.ep, self.scene, self.shot, 'base_fs_c001.mb'])
        path = os.path.join(self.localTemp, 'Scenes\\Animation\\fs', self.ep, self.scene)

        if not os.path.exists(path):
            os.makedirs(path)

        return os.path.join(path, fileName)

    
        
        