#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
__title__ = 'addFunc'    
__author__ = zhangben
__mtime__ = 2018/12/13:9:59
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
'''



def add1(*variaties):
    sum = 0
    for i in variaties:
        sum += i
    return sum


def add2(coefficient,*variaties):
    sum = 0
    for i in variaties:
        sum += i
    return sum*coefficient

