# -*- coding: utf-8 -*-  
import codecs
import os
import re
import shutil
import sys
import tempfile

def collectFiles(nk):
    if not os.path.isfile(nk):
        return

    filename = os.path.basename(nk)
    m = re.search(r"^nj_([^_\.]+_[^_\.]+_[^_\.]+)", filename)
    if not m:
        m = re.search(r"^([^\.]+)", filename)
    shot = os.path.join(os.path.dirname(nk), m.group(1))
    footage = os.path.join(shot, "footage")

    files = os.listdir(os.path.dirname(nk))
    for file in files:
        source = os.path.join(os.path.dirname(nk), file)
        if os.path.isfile(source):
            if re.sub(r'\..*$', '', file).lower() == re.sub(r'\..*$', '', filename).lower():
                dest = os.path.join(shot, file)
                if not os.path.exists(dest):
                    if not os.path.exists(shot):
                        os.makedirs(shot)
                    shutil.copy(source, dest)
    
    f = codecs.open(nk, "r", encoding = "utf_8")
    lines = f.readlines()
    f.close()
    nodeType = None
    for i in range(len(lines)):
        m = re.search(r"^(\w+) {$", lines[i])
        if m:
            nodeType = m.group(1)
        m = re.search(r"^ file \"?([^\"\s]+)\"?$", lines[i])
        if m:
            if nodeType != "Write":
                file = m.group(1)
                file = file.replace('.####.', ".%04d.")
                if re.search(r"%", file):
                    first = None
                    last = None
                    success = False
                    for j in range(i + 1, len(lines)):
                        if re.search(r"^}$", lines[j]):
                            break
                        m = re.search(r"^ first (\d+)$", lines[j])
                        if m:
                            first = int(m.group(1))
                        m = re.search(r"^ last (\d+)$", lines[j])
                        if m:
                            last = int(m.group(1))
                    if first and last:
                        folder = os.path.join(footage, os.path.basename(os.path.dirname(file)))
                        for j in range(first, last + 1):
                            source = file % (j)
                            dest = os.path.join(folder, os.path.basename(source))
                            if os.path.isfile(source):
                                success = True
                                if not os.path.exists(dest):
                                    if not os.path.exists(folder):
                                        os.makedirs(folder)
                                    shutil.copy(source, dest)
                    if success:
                        lines[i] = re.sub(r"^ file \"?([^\"\s]+)\"?$", " file \"\\[file dirname \\[value root.name]]/footage/%s/%s\"" % (os.path.basename(os.path.dirname(file)), os.path.basename(file)), lines[i])
                else:
                    if os.path.isfile(file):
                        dest = os.path.join(footage, os.path.basename(file))
                        if not os.path.exists(dest):
                            if not os.path.exists(footage):
                                os.makedirs(footage)
                            shutil.copy(file, dest)
                        lines[i] = re.sub(r"^ file \"?([^\"\s]+)\"?$", " file \"\\[file dirname \\[value root.name]]/footage/%s" % (os.path.basename(file)), lines[i])

    f = codecs.open(os.path.join(shot, filename), "w", encoding = "utf_8")
    f.writelines(lines)
    f.close()

if __name__ == "__main__":
	nk = sys.argv[1]
	collectFiles(nk)