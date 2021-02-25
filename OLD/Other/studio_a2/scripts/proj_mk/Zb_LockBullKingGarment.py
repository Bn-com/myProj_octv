# -*- coding: utf-8 -*-
"""
__title__ = ''    
__author__ = 'zhangben'
__mtime__ = '2017/11/14:9:42'
# code is far away from bugs with the god animal protecting
I love animals. They taste delicious.
modify:'2017/11/27/14:15'
"""
import re, os
import pymel.core as pm
def locate_BK_worldPosition(locExpDir = ur'Z:\Projects\MonkeyKing\Project\data\BullKingGarmentLoc'):#export locator to server data directory!
    print "Export The Locator ::::::: Locate BullKingB's Position "
    BK_keyChar = 'mk_cBullKingBNew_h_ms_anim'
    if not os.path.isdir(locExpDir):os.mkdir(locExpDir)
    p_keyChar = re.compile(BK_keyChar)
    BK_ref = [eachRef for eachRef in pm.listReferences() if p_keyChar.search(eachRef.path)]
    if not BK_ref:return
    elif not BK_ref[0].isLoaded(): BK_ref[0].load()
    bk_wctl =pm.PyNode('{}:Master_Ctrl'.format(BK_ref[0].namespace))
    pinLocator_temp =  pm.spaceLocator(n='bk_loc_temp',p=[0,0,0])
    pm.parentConstraint(bk_wctl,pinLocator_temp,w=1)
    #pinLocator = pm.spaceLocator(n='bk_loc',p=[0,0,0])
    pinLocator2 = pm.spaceLocator(n='bk_loc',p=[0,0,0])
    loc_attrs = ['tx','ty','tz','rx','ry','rz']
    for eachAttr in loc_attrs:
        #bk_wctl.attr(eachAttr)>>pinLocator.attr(eachAttr)
        pinLocator2.attr(eachAttr).set(bk_wctl.attr(eachAttr).get())
        pinLocator2.attr(eachAttr).lock()
        print pinLocator2.attr(eachAttr).get()
    shotSN = pm.sceneName().basename()
    locExpFile = '{}_BKTrans_loc.mb'.format('_'.join(shotSN.split('_')[:3]))
    exp_file_fullPath = os.path.abspath(os.path.join(locExpDir,locExpFile))
    pm.select(pinLocator2)
    pm.exportSelected(exp_file_fullPath,type='mayaBinary')
    print "Locator Exported!!!!! ----------{}".format(exp_file_fullPath)
def dispose_DyfsFile(locExpDir = ur'Z:\Projects\MonkeyKing\Project\data\BullKingGarmentLoc'):
    #import BullKingB position locator
    shotSN = pm.sceneName().basename()
    locExpFile = '{}_BKTrans_loc.mb'.format('_'.join(shotSN.split('_')[:3]))
    exp_file_fullPath = os.path.abspath(os.path.join(locExpDir,locExpFile))
    if not os.path.isfile(exp_file_fullPath):pm.error(u"定位器还没有存在")
    pm.importFile(exp_file_fullPath,namespace = 'BK_loc')
    loc_node = pm.ls('BK_loc:*',type='locator')[0].getParent()
    #import TShirt
    im_Tshirt_ns = 'mk_cBullKingBnew_TShirt'
    BK_TShirt_file = ur'\\file-cluster\gdc\Projects\MonkeyKing\Project\data\outAdd\pTShirt\pTshirt.mb'
    pm.importFile(BK_TShirt_file,namespace =im_Tshirt_ns )
    #location TShirt and wrap them
    TShirt_transCtr = pm.ls('mk_cBullKingBnew_TShirt:*',type='nurbsCurve')[0].getParent()
    pm.group(TShirt_transCtr,n='TShirt_GRP',p='OTC_GRP')
    transAttrs = ['tx','ty','tz','rx','ry','rz']
    pm.currentTime(950,e=True)
    for eachAttr in transAttrs:
        TShirt_transCtr.attr(eachAttr).set(loc_node.attr(eachAttr).get())
    # wrapped
    wrap_mods = ['coat_mod','plant_mod','baiBu_mod']
    BK_keyChar = 'mk_cBullKingBNew_h_ms_'
    p_keyChar = re.compile(BK_keyChar)
    BK_ref = [eachRef for eachRef in pm.listReferences() if p_keyChar.search(eachRef.path)]
    if not BK_ref:return
    BK_ref_ns = BK_ref[0].namespace
    for eachWrap in wrap_mods:
        hideMod = '{}:{}'.format(BK_ref_ns,eachWrap)
        pm.PyNode(hideMod).visibility.set(0)
        wrap_mod = '{}_sysTemp_mesh:{}'.format(BK_ref_ns,eachWrap)
        TShirt_mod = '{}:{}'.format(im_Tshirt_ns,eachWrap)
        pm.select(cl=True)
        pm.select(TShirt_mod)
        pm.select(wrap_mod,add=True)
        pm.runtime.CreateWrap()
    #remove locator ,xgen relatives DAG node
    rm_XGen_nodes("(BK_loc)|(_xgen)")
    p_num = re.compile('\d{4}')
    my_version = pm.about(v=True)
    if p_num.findall(my_version) and int(p_num.findall(my_version)[0])>= 2016:
        validPlgs = ['mtoa','shaveNode','stereoCameraParallelView']
        import Other.studio_a2.scripts.common.BOptimizeBeforCheckin as bopt
        reload(bopt)
        ins_opt = bopt.BOptimizeBeforCheckin()
        ins_opt.remove_unk_plgs(False,*validPlgs)
        print("Unknown Plugins Removed")
def rm_XGen_nodes(rm_ns="_xgen"):#remove special namespace and contents
    pm.namespace(set=':')
    for each_ns in pm.namespaceInfo(lon=True):
        p_rmNs = re.compile(rm_ns)
        if p_rmNs.search(each_ns):
            DAGNodesIn = pm.namespaceInfo(each_ns,lod=True)
            pm.delete(DAGNodesIn)
            pm.namespace(removeNamespace =each_ns,deleteNamespaceContent=True)