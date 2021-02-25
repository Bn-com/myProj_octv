# -*- coding: utf-8 -*-

'''
database class
'''
__author__    = 'huangzhongwei'
__date__    = '2014-10-31'

import os
import re
import sqlite3
import json
import urllib2

import idmt.pipeline.project

__database__ = os.path.join(os.path.dirname(__file__), 'idmtPlex.db')
if os.path.isfile(__database__):
    __database__ = __database__.replace('\\', '/')
else:
    __database__ = None

def Execute(sql, argv):
    cx = None
    c = None
    r = None
    try:
        cx = sqlite3.connect(__database__)
        cx.row_factory = sqlite3.Row
        c = cx.cursor()
        c.execute(sql, argv)
        r = c.fetchall()
    finally:
        if c != None:
            c.close()
        if cx != None:
            cx.close()
    return r

def GetProjectByFile(filepath):
    if __database__ != None:
        filename = os.path.basename(filepath)
        shortName = re.search(r'^[^_\.]+', filename).group()
        r = Execute('SELECT * FROM TB_Project WHERE shortName = (?)', (shortName, ))
        if len(r) == 1:
            project = idmt.pipeline.project.project()
            project.projectId = r[0]['id']
            project.projectName = r[0]['name']
            project.shortName = r[0]['shortName']
            project.repository = r[0]['repository']
            project.fps = r[0]['fps']
            if project.projectName == 'Strawberry' and re.search(r'\.m(a|b)$', filename) != None:
                project.resolutionW = 1280
                project.resolutionH = 720
            else:
                resolution = r[0]['resolution']
                m = re.search(r'(\d+)x(\d+)', resolution)
                if m != None:
                    project.resolutionW = m.group(1)
                    project.resolutionH = m.group(2)
            return project
        else:
            raise Exception(u'找不到对应的项目')
    else:
        import pyUtil3 as pyUtil
        s = pyUtil.idmtService('GetProjectByFile', filepath)
        if s != '':
            project = idmt.pipeline.project.project()
            buf = s.split('|')
            project.projectId = int(buf[0])
            project.projectName = buf[1]
            project.shortName = buf[2]
            project.repository = buf[3]
            project.fps = int(buf[4])
            project.resolutionW = int(buf[5])
            project.resolutionH = int(buf[6])
            return project
    return None

def GetAnimByFilename(filepath):
    if __database__ != None:
        project = GetProjectByFile(filepath)
        if project == None:
            raise Exception(u'找不到对应的项目')
            return project
        filename = os.path.basename(filepath)
        if project.HasSeq():
            m = re.search(r'[^_\.]+_([^_\.]+)_([^_\.]+)_([^_\.]+)', filename)
            if m == None:
                raise Exception(u'文件命名不规范')
                return project
            anim_ep = m.group(1)
            Tag = m.group(2)
            anim_sc = m.group(3)
            r = Execute('SELECT * FROM TB_Anim WHERE pid = (?) AND anim_ep = (?) AND Tag = (?) AND anim_sc = (?)', (project.projectId, anim_ep, Tag, anim_sc,))
        else:
            m = re.search(r'[^_\.]+_([^_\.]+)_([^_\.]+)', filename)
            if m == None:
                raise Exception(u'文件命名不规范')
                return project
            anim_ep = m.group(1)
            anim_sc = m.group(2)
            r = Execute('SELECT * FROM TB_Anim WHERE pid = (?) AND anim_ep = (?) AND anim_sc = (?)', (project.projectId, anim_ep, anim_sc,))
        if len(r) == 1:
            anim = idmt.pipeline.project.anim(project)
            anim.anim_id = r[0]['anim_id']
            anim.anim_ep = r[0]['anim_ep']
            anim.Tag = r[0]['Tag']
            anim.anim_sc = r[0]['anim_sc']
            anim.frmStart = r[0]['frmStart']
            anim.frmEnd = r[0]['frmEnd']
        else:
            raise Exception(u'找不到对应的镜头')
        return anim
    else:
        project = GetProjectByFile(filepath)
        if project == None:
            return project
        anim = idmt.pipeline.project.anim(project)
        import pyUtil3 as pyUtil
        s = pyUtil.idmtService('GetAnimByFilename3', filepath)
        if s != '':
            buf = s.split('|')
            anim.anim_id = int(buf[0])
            anim.anim_ep = buf[3]
            if anim.HasSeq():
                anim.Tag = buf[4]
            anim.anim_sc = buf[5]
            anim.frmStart = int(buf[6])
            anim.frmEnd = int(buf[7])
        return anim

def GetAssetByFilename(filepath):
    if __database__ != None:
        return None
    else:
        project = GetProjectByFile(filepath)
        if project == None:
            return project
        asset = idmt.pipeline.project.asset(project)
        import pyUtil3 as pyUtil
        s = pyUtil.idmtService('GetAssetByFilename', filepath)
        if s != '':
            buf = s.split('|')
            asset.asset_id = int(buf[0])
            asset.asset_type = buf[1]
            asset.asset_name = buf[2]
            asset.asset_sep = buf[3]
            asset.code = buf[4]
        return asset

def GetAssetNameInAnim(anim):
    assets = []
    if __database__ != None:
        sql = 'SELECT TB_Asset.asset_id, TB_Asset.asset_type, TB_Asset.asset_name, TB_AssetFileSer.asset_sep \
FROM TB_AssetFileSer INNER JOIN TB_Asset ON TB_AssetFileSer.pid = TB_Asset.pid AND TB_AssetFileSer.asset_id = TB_Asset.asset_id \
INNER JOIN TB_AssetFileSerInAnim ON TB_AssetFileSer.pid = TB_AssetFileSerInAnim.pid AND TB_AssetFileSer.fs_id = TB_AssetFileSerInAnim.fs_id \
INNER JOIN TB_Anim ON TB_Anim.pid = TB_AssetFileSerInAnim.pid AND TB_Anim.anim_id = TB_AssetFileSerInAnim.anim_id \
WHERE TB_Anim.pid = (?) AND TB_Anim.anim_id = (?) \
ORDER BY TB_Asset.asset_type, TB_Asset.asset_name, TB_AssetFileSer.asset_sep'
        r = Execute(sql, (anim.projectId, anim.anim_id,))
        for i in range(len(r)):
            asset = idmt.pipeline.project.asset()
            asset.asset_id = r[i]['asset_id']
            asset.asset_type = r[i]['asset_type']
            asset.asset_name = r[i]['asset_name']
            asset.asset_sep = r[i]['asset_sep']
            assets.append(asset)
    else:
        import pyUtil3 as pyUtil
        if anim.HasSeq():
            filename = '%s_%s_%s_%s' % (anim.shortName, anim.anim_ep, anim.Tag, anim.anim_sc)
        else:
            filename = '%s_%s_%s' % (anim.shortName, anim.anim_ep, anim.anim_sc)
        print filename
        s = pyUtil.idmtService('GetAssetNameInAnim3',  '%s|%d' % (anim.projectName, anim.anim_id))
        if s != '':
            buf = s.split('|')
            for i in range(0, len(buf), 5):
                asset = idmt.pipeline.project.asset()
                asset.asset_id = int(buf[i])
                asset.asset_type = buf[i+1]
                asset.asset_name = buf[i+2]
                asset.asset_sep = buf[i+3]
                asset.code = buf[i+4]
                assets.append(asset)
    return assets

def GetRcByEpsc(epsc):
    url = 'http://app-server/wa/Plex/ws/TD.ashx?method=usp_GetRcByEpsc&epsc=%s' % epsc
    response = urllib2.urlopen(url)
    ret = response.read()
    dt = json.loads(ret)
    if len(dt) != 1:
        return None
    return dt[0]