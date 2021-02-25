# -*- coding: utf-8 -*-
import traceback
import datetime
import maya.cmds as mc


def decorator(func):
    def wrapper(*args, **kw):
        startTime = datetime.datetime.now()
        timeFormat = '%Y-%m-%d %H:%M:%S'
        print u'\n开始处理 %s\n' % startTime.strftime(timeFormat)

        try:
            func(*args, **kw)
            endTime = datetime.datetime.now()
            print u'\n处理完成 %s 共花费%d秒\n' % (endTime.strftime(timeFormat), (endTime - startTime).seconds)
        except Exception, e:
            traceback.print_exc()
            endTime = datetime.datetime.now()
            print u'\n处理失败 %s 共花费%d秒\n' % (endTime.strftime(timeFormat), (endTime - startTime).seconds)
            mc.quit(force = True, exitCode = 6)
    return wrapper

@decorator
def autoFS():
    import tiAlembic as tiAlembic
    alm = tiAlembic.tiAlembic()
    alm.exportAlembicCache()
    alm.setupFsFile()

@decorator
def autoRenderLayer():
    import projects.xj.tiAutoRenderLayer as tiAutoRenderLayer
    tiAutoRenderLayer.tiAutoRenderLayer(preCheck = True).outputRenderFiles2()


# @decorator
# def xjAutoLayer():

        
