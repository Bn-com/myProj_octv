import pymel.core as pm
import os
import maya.OpenMaya as om


file_nd = pm.selected()[0]

mSel= om.MSelectionList()
mSel.add(file_nd.name())

file_obj = om.MObject()
mSel.getDependNode(0,file_obj)


imgs = om.MImage()

w = imgs.depth()
h = imgs.depth()


wScriptUtil = om.MScriptUtil(1)
wptr = wScriptUtil.asInt()

wScriptUtil_2 = om.MScriptUtil(1)
wScriptUtil_2.createFromInt(0)
wptr_2 = wScriptUtil_2.asInt()


hScriptUtil = om.MScriptUtil(0)
hPtr = hScriptUtil.asInt()

hScriptUti2 = om.MScriptUtil()
hScriptUti2.createFromInt(0)
hPtr_2 = hScriptUti2.asInt()

imgs.getSize(wptr_2,hPtr_2)

imgs.readFromTextureNode(file_obj)

imgs.getSize(w,h)

help(imgs.getSize)




#================================
import pymel.core as pm
import maya.OpenMaya as om



file_nd = pm.selected()

m_sel = om.MSelectionList()

m_sel.add(file_nd.name())

m_obj = om.MObject()

m_sel.getDependNode(0,m_obj)

oimg = om.MImage()

oimg.readFromTextureNode(m_obj)


w_scrpUtil = om.MScriptUtil(0)
#w_ptr = w_scrpUtil.asInt()
wPtr = w_scrpUtil.asUintPtr()

h_scrpUtil = om.MScriptUtil(0)
#hPtr = w_scrpUtil.asUintPtr()   # 这个错误可以帮助理解  错误情况下，返回的结果竟然都是 1200 1200   原本 w 1920  却是 1200 。
hPtr = h_scrpUtil.asUintPtr()

oimg.getSize(wPtr,hPtr)

util = om.MScriptUtil()
with_num = util.getUint(wPtr)
height_num = util.getUint(hPtr)



#================================
import pymel.core as pm
import maya.OpenMaya as om



file_nd = pm.selected()[0]
m_sel = om.MSelectionList()

m_sel.add(file_nd.name())

m_obj = om.MObject()

m_sel.getDependNode(0,m_obj)

oimg = om.MImage()
oimg.readFromTextureNode(m_obj)

w_scrpUtil = om.MScriptUtil(0)
wPtr = w_scrpUtil.asUintPtr()
h_scrpUtil = om.MScriptUtil(1)
hPtr = h_scrpUtil.asUintPtr()

oimg.getSize(wPtr,hPtr)

util = om.MScriptUtil()
with_num = util.getUint(wPtr)
height_num = util.getUint(hPtr)


txPath = file_nd.attr('fileTextureName').get()
tx_spl= os.path.split(txPath)
tx_nm = tx_spl[1]
tx_path = tx_spl[0]
tx_ext = os.path.splitext(tx_nm)[-1]
tx_bsnm = os.path.splitext(tx_nm)[0]


ratio = 0.5
oimg.resize(int(with_num*ratio),int(height_num*ratio))

res_txPath = os.path.abspath(os.path.join(tx_path,"1_2","1_2{}".format(tx_bsnm)))

oimg.writeToFile(res_txPath,tx_ext.strip('.'))
















