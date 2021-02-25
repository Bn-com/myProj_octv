# -*- coding: utf-8 -*-
import maya.cmds as mc

def logInfo(info):

    l = len(info)

    print '=' * l
    print info
    print '=' * l


def error(info):
    logInfo(info)
    mc.error(u'=== see more information ===')


def print_error(errorInfo):
    # print errorInfo
    decDot = '*' * 32
    print u'{0} 文件中存在以下错误 {0}\n'.format(decDot)
    if type(errorInfo) == list:
        errorInfo = map(lambda x: x.encode('gbk'), errorInfo)
        for idx, err in enumerate(errorInfo, 1):
            print '{}. {}'.format(idx, err)
    else:
        print errorInfo.encode('gbk')
    print u'\n{0} 文件中存在以上错误 {0}\n'.format(decDot)
    mc.error(u'=== see more information above ===')
