# -*- coding: utf-8 -*-
import datetime
import os
import re
import shutil
import stat
import sys

def Renderbus(repository, project):
    #start = (datetime.datetime.combine(datetime.date.today() -  datetime.timedelta(days = 1), datetime.time(16)) -  datetime.datetime(1970, 1, 1)).total_seconds() - 5
    d = datetime.datetime.combine(datetime.date.today() -  datetime.timedelta(days = 1), datetime.time(16)) -  datetime.datetime(1970, 1, 1)
    start = d.days * 86400 + d.seconds - 5
    #end = (datetime.datetime.combine(datetime.date.today(), datetime.time(16)) -  datetime.datetime(1970, 1, 1)).total_seconds()
    d = datetime.datetime.combine(datetime.date.today(), datetime.time(16)) -  datetime.datetime(1970, 1, 1)
    end = d.days * 86400 + d.seconds
    today = datetime.date.today().strftime('%Y-%m-%d')
    i = len(repository) + 1
    for root, dirs, files in os.walk(repository):
        for file in files:
            source = os.path.join(root, file)
            try:
                statinfo = os.stat(source)
                if statinfo.st_mtime > start and  statinfo.st_mtime < end:
                    #folder = r'\\idmt-files\share\scenes\Cloud\Renderbus_update\%s\data\%s\data\%s' % (project, today, root[i:])
                    #if project == 'DOD5':
                    #    folder = r'\\idmt-files\share\scenes\Cloud\Renderbus_update\%s\data\%s' % (project, root[i:])
                    folder = r'\\idmt-files\share\scenes\Cloud\Renderbus_update\%s\data\%s' % (project, root[i:])
                    if not os.path.isdir(folder):
                        os.makedirs(folder)
                    dest = os.path.join(folder, file)
                    shutil.copy(source, dest)
            except:
                pass

def Renderbus1(repository, project):
    cloud = "\\\\\\\\idmt-files\\share\\scenes\\Cloud\\Renderbus_update"
    for root, dirs, files in os.walk(repository):
        for file in files:
            source = os.path.join(root, file)
            try:
                statSource = os.stat(source)
                log = re.sub(r".*\\Project\\", "%s\\\\" % os.path.join(cloud, "AppData", project), source, re.IGNORECASE)
                isLatest = False
                if os.path.isfile(log):
                    statLog = os.stat(log)
                    delta = datetime.datetime.fromtimestamp(statSource.st_mtime) - datetime.datetime.fromtimestamp(statLog.st_mtime)
                    if abs(delta.total_seconds()) <= 3:
                        isLatest = True
                if not isLatest:
                    dest = re.sub(r".*\\Project\\", "%s\\\\" % os.path.join(cloud, project), source, re.IGNORECASE)
                    print "copy \"%s\" \"%s\"" % (source, dest)
                    folder = os.path.dirname(dest)
                    if not os.path.isdir(folder):
                        os.makedirs(folder)
                    if os.path.isfile(dest):
                        os.chmod(dest, stat.S_IWRITE)
                        os.remove(dest)
                    shutil.copy2(source, dest)
                    #os.utime(dest, (statSource.st_atime, statSource.st_mtime))
                    folder = os.path.dirname(log)
                    if not os.path.isdir(folder):
                        os.makedirs(folder)
                    f = open(log, "w")
                    f.close()
                    os.utime(log, (statSource.st_atime, statSource.st_mtime))
            except:
                pass

if __name__ == '__main__':
    #sync(r'\\file-cluster\GDC\Projects\Ninjago\Project\data', 'NJ')
    #sync(r'r'\\file-cluster\GDC\Projects\DomesticProject\YongTai\Project\data'', 'YT')
    if sys.argv[1] == "Renderbus1":
        Renderbus1(sys.argv[2], sys.argv[3])
    else:
        Renderbus(sys.argv[1], sys.argv[2])