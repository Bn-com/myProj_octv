# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import time
import json
import tiProjectConfig as tiProjectConfig
reload(tiProjectConfig)


class tiFile(object):
    
    def __init__(self, *args):

        if not os.environ.has_key('IDMT_PROJECTS'):
            os.environ['IDMT_PROJECTS'] = 'Z:/Projects'
            print '=== 设置 IDMT_PROJECTS =  Z:/Projects ==='

        self.IDMT_PROJECTS = os.environ.get('IDMT_PROJECTS')

        ffname = args[0] if args else mc.file(query=1, exn=1)

        self._filename = os.path.splitext(os.path.basename(ffname))[0]

        animMatch = re.match('^\w{2,5}_\w{3,15}_\d{3,5}_\d{3,5}', self._filename, re.I)
        assetMatch = re.match('^\w{2,5}_[cps]\w{4,50}_[hl]', self._filename, re.I)

        if  animMatch or assetMatch:
            self._nameInfos = self._filename.split('_')
            if tiProjectConfig.PROJECTS.has_key(self._nameInfos[0].lower()):
                self._config = tiProjectConfig.PROJECTS[self._nameInfos[0].lower()]
                self.projRootPath = os.path.normpath(os.path.join(self.IDMT_PROJECTS, self._config['fullName'], 'Project'))
                self.localTemp = os.path.normpath(os.path.join(self._config['localTemp'], self._config['fullName']))

            else:
                raise Exception(u'项目配置文件中没有该项目: %s' % self._nameInfos[0])

        
        else:

            print u'\n\n前期文件命名规范:'
            print u'项目_编号_精度_环节.格式\n'

            print u'动画文件命名规范:'
            print u'项目_集数_场次_镜头号_环节_版本号.格式\n' #\n项目_场次_镜头号_环节_版本号.格式
            
            raise Exception(u'文件名不规范: %s, 请打开Script Editor查看详细信息' % self._filename)

    


    @property
    def rgtxIgnoreDate(self):
        f = os.path.join(self.projRootPath, 'data\\rgtxIgnore.txt')
        if not os.path.lexists(f):
            fo = open(f, 'w')
            fo.close()
        fh = open(f, 'r')
        data = []
        for line in fh.readlines():
            data.append(line.strip())
        return data

    # @property
    # def fileType(self):
    #     return self._fileType

    # def fileM(self):
    #     return self._fileM

    # @property
    # def proj(self):
    #     return self._proj

    # @property
    # def id(self):
    #     return self._id

    # @property
    # def mode(self):
    #     return self._mode

    # @property
    # def type(self):
    #     return self._type


    # @property
    # def fullName(self):
    #     return self._config['fullName']

    # @property
    # def width(self):
    #     return self._config['width']

    # @property
    # def height(self):
    #     return self._config['height']


class tiAnimFile(tiFile):
    def __init__(self, *args):
        super(tiAnimFile, self).__init__(*args)

        animTypes = self._config['animTypes']

        for key, val in animTypes.items():
            if re.search(key, self._filename):
                self.type = val
                break

        for layer in self._config['renderLayers']:
            if re.search(layer, self._filename):
                self.renderLayer = layer
                break

        self.proj = self._nameInfos[0]
        self.ep = self._nameInfos[1]
        self.scene = self._nameInfos[2]
        self.shot = self._nameInfos[3]

    @property
    def lightingExcelFile(self):
        f =  os.path.join(self.projRootPath, 'data\\MS\\Lighting\\excel', self.ep + '.xls')
        return f


    
    @property
    def alembicInfoPath(self):
        name = '_'.join([self.proj,self.ep,self.scene,self.shot, 'alembic.json'])
        f =  os.path.join(self.projRootPath, 'data\\alembic', self.ep, self.scene, self.shot, name)
        return f
 
    def serverAlembicPath(self, fileName):
        f =  os.path.join(self.projRootPath, 'data\\alembic', self.ep, self.scene, self.shot, fileName)
        return f


    def localAlembicPath(self, fileName):
        name = '_'.join([self.proj,self.ep,self.scene,self.shot, (fileName + '.abc')])

        local =  os.path.join(self.localTemp, 'data\\alembic', self.ep, self.scene, self.shot, name)
        local = local.replace('\\', '/')
        localDirPath = os.path.dirname(local)
        if not os.path.exists(localDirPath):
            os.makedirs(localDirPath)


        server =  os.path.join(self.projRootPath, 'data\\alembic', self.ep, self.scene, self.shot, name)
        server = server.replace('\\', '/')
        # try:
        #     serverDirPath = os.path.dirname(server)
        #     if not os.path.exists(serverDirPath):
        #         os.makedirs(serverDirPath)
        # except:
        #     pass

        return local, server


class tiAssetFile(tiFile):
    def __init__(self, *args):
        super(tiAssetFile, self).__init__(*args)

        assetNameRules = self._config['assetNameRules']
        if re.match('^c|p|s', self._nameInfos[assetNameRules['id']], re.IGNORECASE): #len(self._nameInfos == len(assetNameRules) and self._nameInfos[assetNameRules['type']].lower() in self._config['assetType']:
            
            if re.match('^c', self._nameInfos[1], re.IGNORECASE):
                self.assetType = 'characters'
            elif re.match('^p', self._nameInfos[1], re.IGNORECASE):
                self.assetType = 'props'
            elif re.match('^s', self._nameInfos[1], re.IGNORECASE):
                self.assetType = 'sets'
            else:
                self.assetType = 'UNKNOWN'
             
            self.proj = self._nameInfos[assetNameRules['proj']]
            self.id = self._nameInfos[assetNameRules['id']] 
            self.mode = self._nameInfos[assetNameRules['mode']]
            self.type = self._nameInfos[assetNameRules['type']]
            if re.search('_ms_render', self._filename, re.IGNORECASE):
                self.type = 'ms_render'

            if re.search('_ms_anim', self._filename, re.IGNORECASE):
                self.type = 'ms_anim'


        else:
            mc.error(u'file name illegal')
    
 
    def rgbInfoFile(self, name):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_RGB_%s.json' % name)
        return f


    @property
    def vertexInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_VTX.json')
        return f

    @property
    def moVertexInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_VTX_MO.json')
        return f

    @property
    def rgVertexInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_VTX_RG.json')
        return f

    @property
    def txVertexInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_VTX_TX.json')
        return f

    @property
    def moAssetInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_MO.json')
        return f

    @property
    def txAssetInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_TX.json')
        return f

    @property
    def rgAssetInfoFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_RG.json')
        return f


    @property
    def assetInfoMaterialFile(self):
        f = os.path.join(self.projRootPath, 'data\\AssetInfos', self.assetType, self.id, self.mode, self.id + '_MAT.mb')
        return f

    @property
    def msRenderFile(self):
        f = os.path.join(self.projRootPath, 'Scenes', self.assetType, self.id, 'master', '%s_%s_%s_ms_render.mb' % (self.proj,self.id,self.mode))
        return f

    @property
    def msAnimFile(self):
        f = os.path.join(self.projRootPath, 'Scenes', self.assetType, self.id, 'master', '%s_%s_%s_ms_anim.mb' % (self.proj,self.id,self.mode))
        return f

    @property
    def txFile(self):
        f = os.path.join(self.projRootPath, 'Scenes', self.assetType, self.id, 'texture', '%s_%s_%s_tx.mb' % (self.proj,self.id,self.mode))
        return f

    @property
    def rgFile(self):
        f = os.path.join(self.projRootPath, 'Scenes', self.assetType, self.id, 'rigging', '%s_%s_%s_rg.mb' % (self.proj,self.id,self.mode))
        return f

    @property
    def moFile(self):
        f = os.path.join(self.projRootPath, 'Scenes', self.assetType, self.id, 'model', '%s_%s_%s_mo.mb' % (self.proj,self.id,self.mode))
        return f

    @property
    def rgtxIgnore(self):
        return self.id in self.rgtxIgnoreDate
    
    
