#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = assignShader2Mesh
__author__ = zhangben 
__mtime__ = 2019/3/14 : 20:35
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
"""

wantSg = pm.PyNode("An_XYZ")

allMeshs = pm.ls(type='mesh',io=False)
for ea_shp in allMeshs:
    #ea_shp = easel.getChildren(ni=True,type='mesh')[0]
    con_attrs = ea_shp.listConnections(d=True,type='shadingEngine',p=True)
    if not len(con_attrs): continue
    con_attr = con_attrs[0]
    con_attr.unlock()
    con_attr.disconnect()
mc.sets(allMeshs,e=True,forceElement=sgNd.name())