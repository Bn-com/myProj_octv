# -*- coding: utf-8 -*-

'''
project class
'''
__author__    = 'huangzhongwei'
__date__    = '2011-08-18'

import os
import re
import sys
import xml.dom.minidom

import idmt.pipeline.db

class project(object):
    def __init__(self):
        self.projectId = 0
        self.projectName = ''
        self.shortName = ''
        self.repository = ''
        self.fps = None
        self.resolutionW = None
        self.resolutionH = None

    def GetProjects(self):
        projects = []
        s = os.getenv('IDMT_ALL_PROJECTS', '')
        if s == '':
            if sys.platform == 'win32':
                import pyUtil3 as pyUtil
                s = pyUtil.idmtService('GetProjects', '')
                #import suds
                #client = suds.client.Client('http://app-server/ws/Support/Working/svc/idmtSvc.asmx?wsdl')
                #reply = client.service.idmtServiceEx('GetProjects', '')
                #s = reply.result
            else:
                s = '4|BubbleGuppies|bu|//file-cluster/GDC/Projects/BubbleGuppies|maya|8.5|2||37|BuzbyAndDizzy|bd|//file-cluster/gdc/Projects/SideProjects/TestProjects/BuzbyAndDizzy|maya|2011|2||31|CareBears|cb|//file-cluster/GDC/Projects/SideProjects/TestProjects/CareBears|maya|2009|2||10|DiveOllyDive2|do2|//file-cluster/GDC/Projects/DiveOllyDive2|maya|2009|2||7|Enyo|ey|//file-cluster/GDC/Projects/Enyo|maya|2008|2||36|GummiTarzan|gt|//file-cluster/GDC/Projects/GummiTarzan|maya|2009|2||20|HeartBroken|hb|//file-cluster/GDC/Projects/HeartBroken|maya|2010|2||11|Lionelville|lv|//file-cluster/GDC/Projects/Lionelville|maya|2008|2||33|Microfriends|mf|//file-cluster/gdc/Projects/SideProjects/TestProjects/Microfriends|maya|2009|2||30|MonsterHigh|mh|//file-cluster/GDC/Projects/SideProjects/TestProjects/MonsterHigh|maya|2009|2||34|Ninjago|nj|//file-cluster/GDC/Projects/Ninjago|maya|2011|2||26|OKI|oi|//file-cluster/GDC/Projects/OKI|maya|2009|2||21|PatchPillows|pp|//file-cluster/GDC/Projects/PatchPillows|maya|2008|2||23|Polly|py|//file-cluster/GDC/Projects/Polly|maya|2009|2||22|Pollypocketw|pw|//file-cluster/GDC/Projects/Pollypocketw|maya|2009|2||19|RainbowRiders|rr|//file-cluster/GDC/Projects/RainbowRiders|maya|2009|2||32|ROMA|rm|//file-cluster/GDC/Projects/ROMA|maya|2009|2||35|ShenShou|ss|//file-cluster/GDC/Projects/ShenShou|maya|2009|2||1|ShiXun|sx|//file-cluster/GDC/Projects/ShiXun|maya|2011|2||38|Slamdunk|hd|//file-cluster/GDC/Projects/Slamdunk|maya|2009|2||5|Strawberry|sk|//file-cluster/GDC/Projects/Strawberry|maya|2009|2||13|Tinpo|tp|//file-cluster/GDC/Projects/Tinpo|maya|2009|2||16|TTMS|ts|//file-cluster/GDC/Projects/TTMS|maya|2011|2||39|WAWA|wa|//file-cluster/GDC/Projects/WAWA|maya|2011|2||28|Wendy|wd|//file-cluster/GDC/Projects/Wendy|maya|2009|2||2|WinxClub|wi|//file-cluster/GDC/Projects/WinxClub|maya|8.5|2||6|WinxClubII|wn2|//file-cluster/GDC/Projects/WinxClubII|maya|2011|2||27|WinxTV|wt|//file-cluster/GDC/Projects/WinxTV|maya|2011|2||24|Woodlies|wo|//file-cluster/GDC/Projects/Woodlies|maya|2009|2||40|WuXing|fe|//file-cluster/GDC/Projects/WuXing|maya|2008|2||29|ZhuZhuPets|zz|//file-cluster/GDC/Projects/ZhuZhuPets|maya|2009|2'
            #os.putenv('IDMT_ALL_PROJECTS', s)
        if s <> '':
            os.environ['IDMT_ALL_PROJECTS'] = s
            buf = s.split('||')
            for s1 in buf:
                p = project()
                buf1 = s1.split('|')
                p.projectId = int(buf1[0])
                p.projectName = buf1[1]
                p.shortName = buf1[2]
                p.repository = buf1[3]
                projects.append(p)
        return projects
    
    def GetProjectByName(self, projectName):
        projects = self.GetProjects()
        for project in projects:
            if project.projectName.upper() == projectName.upper():
                return project
        return None

    def GetProjectByFile(self, filepath):
        import pyUtil3 as pyUtil
        s = pyUtil.idmtService('GetProjectByFile', filepath)
        if s != '':
            buf = s.split('|')
            self.projectId = int(buf[0])
            self.projectName = buf[1]
            self.shortName = buf[2]
            self.repository = buf[3]

    def HasSeq(self, projectName = None):
        rs = False
        if projectName == None:
            projectName = self.projectName
        if projectName in ['Woodlies', 'Ninjago', 'GummiTarzan', 'MayaTheBee', 'OTTO', 'LORDoftheRINGS', 'VickyTheViking', 'YODA', 'ShunLiu', 'AutoTest', 'ToothFairies', 'Xyj', 'XingJiCheShen1']:
            rs = True
        return rs

    def GetPlayblastResolution(self, projectName):
        import xpath
        resolution = [0, 0]

        dom = xml.dom.minidom.parse(r'\\file-cluster\GDC\Resource\Support\bin\projects.xml')
        doc = dom.documentElement
        widths = xpath.findvalues("//project[name='%s']/playblast/width" % projectName, doc)
        heights = xpath.findvalues("//project[name='%s']/playblast/height" % projectName, doc)
        if len(widths) == 1 and len(heights) == 1:
            resolution[0] = int(widths[0])
            resolution[1] = int(heights[0])

        return resolution

    def GetTextureFormat(self, projectName):
        import xpath
        f = 'iff'

        dom = xml.dom.minidom.parse(r'\\file-cluster\GDC\Resource\Support\bin\projects.xml')
        doc = dom.documentElement
        formats = xpath.findvalues("//project[name='%s']/texture/format" % projectName, doc)
        if len(formats) == 1:
            f = formats[0]

        return f

    def GetSetting(self, projectName, keyName):
        import xpath
        setting = ''

        dom = xml.dom.minidom.parse(r'\\file-cluster\GDC\Resource\Support\bin\projects.xml')
        doc = dom.documentElement
        settings = xpath.findvalues("//project[name='%s']/%s" % (projectName, keyName), doc)
        if len(settings) == 1:
            setting = settings[0]
        else:
            projectName = 'Default'
            settings = xpath.findvalues("//project[name='%s']/%s" % (projectName, keyName), doc)
            if len(settings) == 1:
                setting = settings[0]

        return setting

def GetSetting(projectName, keyName):
        return project().GetSetting(projectName, keyName)

def GetParity(episode):
    parity = 'Even'
    if re.search(r'^[a-z]{2}$', episode, re.IGNORECASE) != None:    # VickyTheViking
        if re.search(r'[ACEGIKMOQSUWY]$', episode, re.IGNORECASE) != None:
            parity = 'Odd'
    #elif re.search(r'^[EM]\d{4}$', episode, re.IGNORECASE) != None:    # Ninjago, LORDoftheRINGS, YODA
    #    if re.search(r'^E6', episode) != None:
    #        if re.search(r'^E605[68]$', episode, re.IGNORECASE) != None:
    #            parity = 'Odd'
    #        elif re.search(r'^E6\d{2}[13479]$', episode, re.IGNORECASE) != None:
    #            parity = 'Odd'
    #    elif re.search(r'[13579]\d$', episode) != None:
    #        parity = 'Odd'
    else:
        m = re.search(r'^[0-9]+', episode)
        if m == None:
            m = re.search(r'[0-9]+$', episode)
        if m != None:
            episode = m.group(0)
        if re.search(r'[13579]$', episode) != None:
            parity = 'Odd'
    return parity

class anim(project):
    def __init__(self, project = None):
        if project:
            self.projectId = project.projectId
            self.projectName = project.projectName
            self.shortName = project.shortName
            self.repository = project.repository
            self.fps = project.fps
            self.resolutionW = project.resolutionW
            self.resolutionH = project.resolutionH
        self.anim_id = 0
        self.anim_ep = ''
        self.Tag = ''
        self.anim_sc = ''
        self.frmStart = 0
        self.frmEnd = 0

    #def GetAnimByFilename(self, filepath):
    #    import pyUtil
    #    anim = pyUtil.GetAnimByFilename(filepath)
    #    if 'id' in anim:
    #        self.projectId = anim['id']
    #    if 'name' in anim:
    #        self.projectName = anim['name']
    #    if 'shortName' in anim:
    #        self.shortName = anim['shortName']
    #    if 'fps' in anim:
    #        self.fps = anim['fps']
    #    if 'frmStart' in anim and 'frmEnd' in anim:
    #        self.frmStart = anim['frmStart']
    #        self.frmEnd = anim['frmEnd']
    #    if 'resolutionW' in anim and 'resolutionH' in anim:
    #        self.resolutionW = anim['resolutionW']
    #        self.resolutionH = anim['resolutionH']

    def GetAssetNameInAnim(self):
        return idmt.pipeline.db.GetAssetNameInAnim(self)

class asset(project):
    def __init__(self, project = None):
        if project:
            self.projectId = project.projectId
            self.projectName = project.projectName
            self.shortName = project.shortName
            self.repository = project.repository
            self.fps = project.fps
            self.resolutionW = project.resolutionW
            self.resolutionH = project.resolutionH
        self.asset_id = 0
        self.asset_type = ''
        self.asset_name = ''
        self.asset_sep = ''
        self.code = ''