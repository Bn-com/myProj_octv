#-*- coding: utf-8 -*-
'''
Created on 2014-1-27

@author: zhaozhongjie
@contact:     66372484@qq.com
@deffield    updated: Updated
'''
import traceback
import pymel.core as pm
def setAttr(attrs = '',onOff=1):
    '''
    setAttr('primaryVisibility',0)    #关闭可渲染属性
    '''
    for s in pm.ls(sl=1,dag=1,geometry=1):
        try:
            s.attr(attrs).set(onOff)
        except Exception as e:
            pm.warning(e)
            pass