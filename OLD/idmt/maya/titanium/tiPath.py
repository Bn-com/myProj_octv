# -*- coding: utf-8 -*-
import os
import maya.cmds as cmds
import os
import re


def exists(path):
    return os.path.exists(getFullPath(path))

def getFullPath(path):
    return os.path.expandvars(path)

def getDollarPath(path):
    return changePathType('D', path)
    # pattern = re.compile(r'[\\/]{2}file-cluster[\\/]gdc[\\/]projects|z:[\\/]projects|l:[\\/]projects', re.I)

    # fullPath = getFullPath(path)


    # fullPath = pattern.sub('${IDMT_PROJECTS}', fullPath)

    # if exists(fullPath):
    #     # fullPath = re.sub(r'\\', r'/', fullPath)
    #     return fullPath
    
    # return path


def changePathType(p, path):

    pattern = re.compile(r'[\\/]{2}file-cluster[\\/]gdc[\\/]projects|z:[\\/]projects|l:[\\/]projects', re.I)

    fullPath = getFullPath(path)

    pathDic = {
        'L': 'L:\\Projects',
        'Z': 'Z:\\Projects',
        'D': '${IDMT_PROJECTS}',

    }

    fullPath = os.path.normpath(pattern.sub(pathDic.get(p.upper()), fullPath))
    if exists(fullPath):
        
        # fullPath = re.sub(r'\\', r'/', fullPath)
        return fullPath
    
    return path