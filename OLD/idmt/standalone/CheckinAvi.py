# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2011-12-27'

import glob
import os
import re
import socket
import sys
import win32wnet

import pyUtil2 as pyUtil

def GetUNC(path):
    try:
        path = win32wnet.WNetGetUniversalName(path)
    except:
        pass
    return path

'''
def mySysFile(action, source, dest):
    print '%s \"%s\" \"%s\"' % (action, source, dest)

    source = GetUNC(source)
    source = re.compile(r'^([a-z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    sock.connect(('192.168.168.152', 2345))
    ss = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), action, source, dest)
    sock.send(ss)
    sr = sock.recv(1024)
    sock.close()
    if sr == ss:
        return True
    else:
        sr = re.sub(r'^#\d+', '', sr)
        sr = re.sub(r' at \w:.*$', '', sr)
        print sr
        return False
'''

def mySysFile(action, source, dest):
    print '%s \"%s\" \"%s\"' % (action, source, dest)

    source = GetUNC(source)
    source = re.compile(r'^([a-z]):', re.IGNORECASE).sub(r'//%s/\g<1>$' % os.getenv('COMPUTERNAME'), source)

    ss = '%s%%%%%s%%%%%s%%%%%s' % (os.getenv('USERNAME'), action, source, dest)
    
    import suds
    client = suds.client.Client('http://cq-file02/CheckinService.asmx?wsdl')
    reply = client.service.cmd(ss)

    if reply == 'True':
        return True
    else:
        print reply
        return False

def Checkin(source):
    filename = os.path.basename(source)
    m = re.search('\.(avi|mov|mp4)$', filename, re.IGNORECASE)
    if m == None:
        print u'// Error: 只能更新avi或者mov'
        sys.exit(-1)
    ext = m.group(1).lower()

    filename = re.sub('([^\.]+).*', '\g<1>.ma', filename)
    mayafilename = re.sub(r'^(mi_.*)_(left|right)_(sd[\._])', '\g<1>_\g<3>', filename, re.IGNORECASE)
    s = pyUtil.idmtService('GetPathByAvi', mayafilename)
    if s == '':
        print u'// Error: 网上找不到相对应的maya文件'
        sys.exit(-1)

    renderCnt = 1

    (project, file_id, dest) = s.split('|')
    if project == 'MayaTheBee' or  project == 'ROMA':
        dest = re.sub('[^\.]+$', ext, dest)
    else:
        m = re.search(r'^mi_.*_(left|right)_sd[\._]', filename, re.IGNORECASE)
        if m != None:
            renderCnt = 2
            lr = m.group(1).lower()
            if lr == "left":
                lr = '0001.'
            else:
                lr = '0002.'
            for renderMime in ['avi', 'mov', 'mp4']:
                avi = re.sub('[^\.]+$', lr + renderMime, dest)
                if os.path.isfile(avi):
                    mySysFile('del', avi, '')
            dest = re.sub('[^\.]+$', lr + ext, dest)
        else:
            for renderMime in ['avi', 'mov', 'mp4']:
                avi = re.sub('[^\.]+$', '0001.' + renderMime, dest)
                if os.path.isfile(avi):
                    mySysFile('del', avi, '')
            dest = re.sub('[^\.]+$', '0001.' + ext, dest)
    if not mySysFile('copy', source, dest):
        sys.exit(-1)

    pyUtil.idmtService('UpdateAvi1', '%s|%s|%s|%d' % (project, file_id, ext, renderCnt))

if __name__ == "__main__":
    path = sys.argv[1]
    print path
    Checkin(path)