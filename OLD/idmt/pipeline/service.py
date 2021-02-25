# -*- coding: utf-8 -*-

'''
Service class
'''
__author__	= 'huangzhongwei'
__date__	= '2011-12-05'

import json
import logging
import os
import re
import suds

class Service(object):
    def __init__(self, user = None):
        logging.getLogger('suds').setLevel(logging.CRITICAL)
        self.client = suds.client.Client('http://info-srv/TD/svc/idmtSvc.asmx?wsdl')
        if user == None:
            self.user = '%s\\%s' % (os.getenv('USERDOMAIN'), os.getenv('USERNAME'))
        else:
            self.user = user

    def RegQueryValue(self, key, default = None):
        argv = '%s|%s' % (self.user, key)
        reply = self.client.service.idmtServiceEx('RegQueryValue', argv)
        value = reply.result
        if value == None and default:
            value = default
        return value

    def RegSetValue(self, key, value):
        argv = '%s|%s|%s' % (self.user, key, str(value))
        self.client.service.idmtServiceEx('RegSetValue', argv)

    def GetEpisodes(self, projectName):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, "SELECT DISTINCT [anim_ep] FROM [TB_Anim] WHERE [active] = 1 ORDER BY [anim_ep]", None)
        dt = json.loads(reply)
        episodes = []
        for row in dt:
            episodes.append(row["anim_ep"])
        return episodes

    def GetShots(self, projectName, episode):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, "SELECT DISTINCT [anim_sc] FROM [TB_Anim] WHERE [anim_ep] = '%s' AND [active] = 1 ORDER BY [anim_sc]" % episode, None)
        dt = json.loads(reply)
        shots = []
        for row in dt:
            shots.append(row["anim_sc"])
        return shots

    def GetAssetsByCaption(self, projectName, FullPath):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, "SELECT [TB_Asset].[asset_name] FROM [TB_AssetMap] INNER JOIN [TB_Asset] ON [TB_AssetMap].[ID] = [TB_Asset].[map_id] WHERE [TB_AssetMap].[Fullpath] = '%s' AND [TB_Asset].[active] = 1 ORDER BY [TB_Asset].[asset_name]" % FullPath, None)
        dt = json.loads(reply)
        shots = []
        for row in dt:
            shots.append(row["asset_name"])
        return shots

    def GetAnimFileLib(self, projectName, filename):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, "SELECT * FROM [TB_AnimFileLib] WHERE [Anim_file] LIKE '%s%%' AND [Enable] = 1" % filename, None)
        dt = json.loads(reply)
        return dt

    def DDZGetTOD(self, episode, shot):
        TOD = ''
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.DouDiZhu", "SELECT ISNULL([pcpe_edit2], '') AS [TOD] FROM [tb_PageColumnProjectEdit] INNER JOIN [TB_Anim_Task] ON [tb_PageColumnProjectEdit].[pcpe_taskid] = [TB_Anim_Task].[task_id] AND [TB_Anim_Task].[task_mode] = 'composite' AND [TB_Anim_Task].[active] = 1 INNER JOIN [TB_Anim] ON [TB_Anim_Task].[anim_id] = [TB_Anim].[anim_id] WHERE [TB_Anim].[anim_ep] = '%s' AND [TB_Anim].[anim_sc] = '%s'" % (episode, shot), None)
        dt = json.loads(reply)
        for row in dt:
            TOD = row["TOD"]
        return TOD

    def GetAnimByRcState(self, projectName = "DouDiZhu", state_rc = u"可制作"):
        client = suds.client.Client("http://idmt-plex/plex/ws/daily.asmx?wsdl")
        reply = client.service.GetTB("DB.PLEX.%s" % projectName, u"SELECT [anim_ep], [anim_sc] FROM [View_SsomAnimTaskmodeState] WHERE [state_rc] = '%s'" % state_rc, None)
        dt = json.loads(reply)
        return dt

class SysFile(object):
    def __init__(self):
        logging.getLogger('suds').setLevel(logging.CRITICAL)
        self.client = suds.client.Client('http://cq-file02/CheckinService.asmx?wsdl')

    def sysFile(self, action, source, dest):
        print '%s \"%s\" \"%s\"' % (action, source, dest)
        source = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', source)
        source = re.compile(r'^([A-KM-Z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)
        ss = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), action, source, dest)
        reply = self.client.service.cmd(ss)
        if reply == 'True':
            return True
        else:
            print reply
            return False

    def md(self, dir):
        self.sysFile("md", dir, "")

    def copy(self, source, dest):
        source = re.compile(r'^Z:', re.IGNORECASE).sub(r'//file-cluster/GDC', source)
        source = re.compile(r'^([a-z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)
        self.sysFile("copy", source, dest)