# -*- coding: utf-8 -*-

import maya.cmds as mc
import maya.mel as mel
import pymel.core as pm
import os
import re
import mtoa
import mtoa.cmds.registerArnoldRenderer

import xlrd
reload(xlrd)
import tiPre as tiPre
reload(tiPre)
import tiBase as tiBase
reload(tiBase)
import tiFile as tiFile
reload(tiFile)
import tiEgg as tiEgg
reload(tiEgg)



class tiCheck(object):
    """docstring for tiCheck"""
    def __init__(self, *args, **kw):

        checkType = kw.get('checkType', None)
        errorInfo = ''

        

        if checkType:
            if checkType == 'anim':
                start, end, duration = tiBase.timeLine()
                startFrame = mc.playbackOptions(q = True, min = True)
                endFrame = mc.playbackOptions(q = True, max = True)
                if start != startFrame:
                    errorInfo += u'文件中的开始帧与数据库不一致: 请从 %0.1f 改为 %d\n' % (startFrame, start)

                if end != endFrame:
                    errorInfo += u'文件中的结束帧与数据库不一致: 请从 %0.1f 改为 %d\n' % (endFrame, end) 
        

                fpsDic = {
                    'game': 15,
                    'film': 24,
                    'pal': 25,
                    'ntsc': 30,
                    'show': 48,
                    'palf': 50,
                    'ntscf': 60
                }

                curFps = mc.currentUnit(q = True, time = True)
                if curFps != 'pal':
                    errorInfo += u'文件帧速率不正确,请从 %d 改为: %d\n' % (fpsDic.get(curFps), 25)


                unit = mc.currentUnit(q = True, linear = True)
                if unit != 'cm':
                    errorInfo += u'文件单位不正确,请从 %s 改为: %s\n' % (unit, 'cm')  
                

                serverPathPattern = re.compile('//file-cluster/GDC/Projects|z:/projects|L:/Projects|${IDMT_PROJECT}', re.I)
                

                
                animPattern = re.compile('[A-Za-z0-9]+_(c|p|s).+_h_ms_anim.(ma|mb)', re.I)
                camPattern = re.compile('[A-Za-z0-9]+_[A-Za-z0-9]+_[A-Za-z0-9]+_[A-Za-z0-9]+_cam.(ma|mb)', re.I)
                refs = pm.listReferences()

                for ref in refs:    
                    if not serverPathPattern.match(ref.path):
                        errorInfo += u'参考的文件路径不正确: %s\n' % ref.path

                    else:
                        baseName = os.path.basename(ref.path)
                        if not animPattern.match(baseName) and not camPattern.match(baseName):
                            errorInfo += u'动画文件中只能参考ms_anim和相机文件: %s\n' % baseName

        if errorInfo:
            decDot = '*' * 32
            print u'{0} 文件中存在以下错误 {0}\n'.format(decDot)
            print errorInfo
            print u'{0} 文件中存在以上错误 {0}\n'.format(decDot)
            mc.error(u'=== see more infomation ===')
        else:
            print '=== file ok ==='