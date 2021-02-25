#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2013-12-112013

@author: zhangben
'''
import maya.cmds as mc
import re
import os
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp


allRNIterator = docp.list_valid_referenceNodes()
for eachRN in allRNIterator:
    if not mc.referenceQuery(eachRN, isLoaded=True):
        rf_file = mc.referenceQuery(eachRN, f=True)
        mc.file(rf_file, lr=eachRN)
    if imp_rfn:
        mc.file(ir=True, rfn=eachRN)
allMeshes_all = (d for d in mc.ls(typ=u'mesh', l=True) if not mc.referenceQuery(d, inr=True))
allMesheShapes_nrf = (d for d in mc.ls(typ=u'mesh', ni=True, l=True) if mc.getAttr(
    "%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)) and check_mesh_validity(d) and not mc.referenceQuery(d, inr=True))
allMesheShapes_rf = (d for d in mc.ls(typ='mesh', ni=True, l=True) if mc.getAttr(
    "%s.primaryVisibility" % d) and (docp.nodeIsVisible(d)) and check_mesh_validity(d) and mc.referenceQuery(d, inr=True))
allMeshes_nrf = []
allMeshes_rf = []
allMesheShapes_nrf_ls = []
allMeshes_rf_ls = []
for each_msh in allMesheShapes_nrf:
    allMesheShapes_nrf_ls.append(each_msh)
    allMeshes_nrf.append(mc.listRelatives(each_msh, parent=True, f=True, type=u'transform')[0])
for each_msh_rf in allMesheShapes_rf:
    allMeshes_rf_ls.append(each_msh_rf)
    allMeshes_rf.append(mc.listRelatives(each_msh_rf, parent=True, f=True, type=u'transform')[0])
lamShd = lmbMat_name
lamSG = u'%sSG' % lamShd
create_spec_MAT(lamShd)
for objShape in allMeshes_all:
    disconnect_shape_sg(objShape, lamSG)


def disconnect_shape_sg(objShape, assignNewSG=False, whole=True):  # ====断开指定物体与SG节点的连接（是否连接新的sg）
    objShape_par = u'|'.join(objShape.split(u'|')[:-1])
    if not whole:  # ===========（按面赋予材质的的物体，是否整体再指定材质----否）
        if assignNewSG:  # =====按照物体原赋予材质信息重新指定材质============
            con_sg_noSort = [eachSG for eachSG in mc.listConnections(objShape, type=u'shadingEngine') if not eachSG == u'initialShadingGroup']
            con_sg = [con_sg_noSort[i] for i in range(len(con_sg_noSort)) if con_sg_noSort[i] not in con_sg_noSort[:i]]
            con_members = []
            for each_sg in con_sg:
                mc.hyperShade(o=each_sg)
                members = [each_mem for each_mem in mc.ls(sl=True, l=True, fl=True) if each_mem.find(objShape_par) > -1]
                if len(members) != 0:
                    mc.sets(members, e=True, fe=assignNewSG)
        else:  # =============只是断开物体与SG的连接========================
            con_sg_plus = mc.listConnections(objShape, type=u'shadingEngine', c=True, p=True)
            if con_sg_plus:
                for i in range(0, len(con_sg_plus), 2):
                    try:
                        mc.disconnectAttr(con_sg_plus[i], con_sg_plus[i + 1])
                        print u'====Disconect %s and %s' % (con_sg_plus[i], con_sg_plus[i + 1])
                    except:
                        mc.disconnectAttr(con_sg_plus[i + 1], con_sg_plus[i])
                        print u'====Disconect %s and %s' % (con_sg_plus[i + 1], con_sg_plus[i])
    else:  # ==============整体赋予新的材质=================
        create_MatGrp = create_spec_MAT(assignNewSG)
        con_sg_plus = mc.listConnections(objShape, type=u'shadingEngine', c=True, p=True)
        if con_sg_plus:
            for i in range(0, len(con_sg_plus), 2):
                try:
                    mc.disconnectAttr(con_sg_plus[i], con_sg_plus[i + 1])
                except:
                    mc.disconnectAttr(con_sg_plus[i + 1], con_sg_plus[i])
        try:
            mc.sets(objShape, e=True, fe=create_MatGrp[1])
        except:
            print u'%s,can not assign mat' % objShape

import maya.cmds as mc
import maya.mel as mel
import idmt.maya.DOD.DODIV.Maya.commonProperties as docp

allSetMeshShapes_nrf = (d for d in mc.ls(typ=u'mesh', ni=True, l=True) if mc.getAttr("%s.primaryVisibility" % d) and
                       (docp.nodeIsVisible(d)) and not (d) and not mc.referenceQuery(d, inr=True) and d.find(u'do4_s') > -1)
for each_set_mesh in allSetMeshShapes_nrf:
    mc.select(each_set_mesh, r=True)
    mel.eval('BakeNonDefHistory')


def check_cache_GEO(meshShape):
    cache_History = [each_hist for each_hist in mc.listHistory(meshShape, ac=True) if mc.nodeType(each_hist) == u'cacheFile']
    if cache_History:
        return True
    else:
        return False
