# -*- coding: utf-8 -*-
__author__ = ''
__modifier__ = 'zhaozhongjie'
__modifierN__ = 'HanHong'
__modify__ = '2014-1-4'
__modifyN__ = '2014-3-25'

import os
import re
import glob
import nuke
import datetime
import re
import socket
import pyodbc
import pyUtil3 as pyUtil
import idmt.pipeline.project


def importImages(imagesPath):
    imagesTypes = "jpg|jpge|tga|iff|dpx|tiff|tif|png"
    rule = r'(.*?)(\d+)(\.(?:%s))' % imagesTypes
    pattern = re.compile(rule)
    nuke_readSeqs = []
    imagesBaseName = []
    readSeqsDone = []
    readSeqsDone2 = []
    c = 0
    firstFrame = 0
    pathall = []
    for root, dirs, files in os.walk(imagesPath):
        imagesSeq = [x for x in files if x.split('.')[-1] in imagesTypes]
        if imagesSeq != []:
            imagesSeq.sort()
            for f in imagesSeq:
                rootR = root.replace("\\", "/")
                #  print rootR
                if pattern.findall(f) == []:
                    # nuke.createNode("Read",inpanel=False)["file"].setValue(root+'/'+f)
                    nuke_readSeqs.append([rootR + '/' + f, 1, 1])
                elif (rootR + pattern.findall(f)[0][0]) not in imagesBaseName:
                    firstFrame = int(pattern.findall(f)[0][1])
                    imagesBaseName.append(rootR + pattern.findall(f)[0][0])
                    nuke_readSeqs.append([rootR + '/' + pattern.findall(f)[0][0] + '#' * len(
                        pattern.findall(f)[0][1]) + pattern.findall(f)[0][2], firstFrame, firstFrame])
                    # else:nuke_readSeqs[-1][2] += 1
                else:
                    nuke_readSeqs[-1][2] = int(pattern.findall(f)[0][1])

    for readSeqsV in nuke_readSeqs:
        readSeqsPathT = readSeqsV[0].split("/")
        readSeqsPathT2 = ""
        for i in range(len(readSeqsPathT) - 1):
            readSeqsPathT2 += readSeqsPathT[i] + "/"

        if readSeqsPathT2.find("Left") >= 0:
            if os.path.isdir(readSeqsPathT2.replace("Left", "Right")) == 1:
                readSeqsV[0] = readSeqsV[0].replace("Left", "%V")
                c = 1

        elif readSeqsPathT2.find("Right") >= 0:
            if os.path.isdir(readSeqsPathT2.replace("Right", "Left")) == 1:
                readSeqsV[0] = readSeqsV[0].replace("Right", "%V")
                c = 1

        if readSeqsV not in readSeqsDone:
            readSeqsDone.append(readSeqsV)
#    print '5-',readSeqsDone,'-5'
#    return

    firstFrame = ''
    lastFrame = ''
    # add for DO3================================
    proName = imagesPath.split("/")[5]
    #=========================================
    for frameValue in readSeqsDone:
    # add for DO3================================
        if proName == "DiveollyDive3" or "DiveollyDive4":
            firstFrame = frameValue[1]
            lastFrame = frameValue[2]
    #=========================================
        if frameValue[1] == 1001:
            firstFrame = frameValue[1]
            lastFrame = frameValue[2]
            break
    nuke.root().knob('first_frame').setValue(firstFrame)
    nuke.root().knob('last_frame').setValue(lastFrame)

    if c == 1:
        setUpMultiView()
    r = nuke.allNodes('Read')
    for nod in r:
        pathall.append(nod['file'].value())

    for i in range(len(readSeqsDone)):

        seqs = readSeqsDone[i]

# modify by zzj   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#   original:
        # if seqs[0] not in pathall:
#   new:
        regex = re.compile('\\#{1,10}')
        readNodePath = regex.sub(
            lambda m: '%%0%dd' % (len(m.group(0))), seqs[0])
        if readNodePath not in pathall:
# modify by zzj   ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
            readSeqsDone2.append(readSeqsDone[i])
    for readSeqa in readSeqsDone2:
        n = nuke.createNode("Read", inpanel=False)
        n["file"].setValue(readSeqa[0])
        n["first"].setValue(readSeqa[1])
        n["last"].setValue(readSeqa[2])
        nuke.delete(nuke.thisNode())


def importImagesPanel():
    n = nuke.createNode("PanelNode")
    k1 = nuke.File_Knob("dirPath", "Path")
    k2 = nuke.PyScript_Knob("importImages", "importImages",
                            "importImages(nuke.thisNode()['dirPath'].value())")
    n.addKnob(k1)
    n.addKnob(k2)


def setUpMultiView(views=[('left', (0, 1, 0)), ('right', (1, 0, 0))]):

    newViews = []
    for v in views:   # CYCLE THROUGH EACH REQUESTED VIEW
        name = v[0]   # GRAB THE CURRENT VIEWS NAME
        col = v[1]    # GRAB THE CURRENT VIEWS COLOUR
        # CONVERT FLOAT TO 8BIT INT AND RETURN A TUPLE
        rgb = tuple([int(v * 255) for v in col])
        # CONVERT INTEGER NUMBERS TO HEX CODE
        hexCol = '#%02x%02x%02x' % rgb
        # COMBINE NAME AND HEX COLOUR TO SCRIPT SYNTAX
        curView = '%s %s' % (name, hexCol)
        newViews.append(curView)      # COLLECT ALL REQUESTED VIEWS

    # COMBINE ALL VIEWS WITH LINE BREAK AND INITIALISE THE VIEWS KNOB WITH THE
    # RESULTING SCRIPT SYNTAX
    nuke.root().knob('views').fromScript('\n'.join(newViews))


def importI():

    ep = ""
    seq = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^gt_[0-9a-z]+_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        seq = buff2[2]
        sc = buff2[3]
    if ep == "" or seq == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/Projects/GummiTarzan/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/seq_" + seq + "/sc_" + sc + "/"
    importImages(folder)


def importOT():

    ep = ""
    seq = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^ot_[0-9a-z]+_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        seq = buff2[2]
        sc = buff2[3]
    if ep == "" or seq == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/Projects/OTTO/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/seq_" + seq + "/sc_" + sc + "/"
    importImages(folder)


def getParity(episode):
    parity = 'EVEN'
    episode = re.sub(r'[^0-9]+$', '', episode)
    m = re.search('[13579]$', episode)
    if(m != None):
        parity = 'ODD'
    return parity


def importEQ():
    ep = ""
    seq = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^eq_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        sc = buff2[2]
    if ep == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/Projects/Earthquake/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/sc_" + sc + "/lr/"
    importImages(folder)


def importSK():
    ep = ""
    seq = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^sk_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        sc = buff2[2]
    if ep == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/Projects/Strawberry/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/sc_" + sc + "/c001/lr/"
    importImages(folder)


def importDO(proj=u'DiveollyDive5', proj_abb=u'do5'):
    ep = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^%s_[0-9a-z]+_[0-9a-z]+_' % proj_abb, re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        sc = buff2[2]
    if ep == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    #folder = "//file-cluster/GDC/Projects/DiveollyDive3/Production/Render/Images/" + parity + "/ep_" + ep + "/sc_" + sc+"/lr/"

    folder = u"//file-cluster/GDC/Projects/%s/Production/Render/Images/%s/ep_%s/sc_%s/lr/" % (
        proj, parity, ep, sc)

    importImages(folder)


def importCH():
    ep = ""
    seq = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^eq_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        sc = buff2[2]
    if ep == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/DomesticProject/ChinaImage/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/sc_" + sc + "/lr/"
    importImages(folder)


def importQS():
    ep = ""
    sc = ""
    path = nuke.root().knob('name').value()
    buff1 = os.path.split(path)
    if re.compile(r'^qs_[0-9a-z]+_[0-9a-z]+_', re.IGNORECASE).match(buff1[1]) != None:
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        sc = buff2[2]
    if ep == "" or sc == "":
        nuke.message('can not catch the shot number form filename')
        return
    parity = getParity(ep)
    folder = "//file-cluster/GDC/Projects/Qsanguo/Production/Render/Images/" + \
        parity + "/ep_" + ep + "/sc_" + sc + "/lr/"
    importImages(folder)

# 通用导入素材，2014-03-26 韩虹添加修改


def commonimportImages():
    parity = ""
    ep = ""
    seq = ""
    sc = ""
    folder = ""
    path = nuke.root().knob('name').value()
    proj = idmt.pipeline.project.project()
    proj.GetProjectByFile(path)
    buff1 = os.path.split(path)    
    if proj.projectId != 0:
        filepath = r'%s\Production\Render\Images' % (proj.repository)
        filepathf = filepath.replace('\\', '/')
        buff2 = re.compile('_').split(buff1[1])
        ep = buff2[1]
        seq = buff2[2]
        sc = buff2[3]
        parity = getParity(ep)
        #if re.search(r'^\d+$', sc) != None:
        if proj.HasSeq(proj.projectName):   # 黄仲维20140930改
            folder = filepathf + "/" + parity + "/ep_" + \
                ep + "/seq_" + seq + "/sc_" + sc + "/"
        else:
            folder = filepathf + "/" + parity + \
                "/ep_" + ep + "/sc_" + seq + "/"
        importImages(folder)
    else:
        nuke.message('can not catch the shot number form filename')
