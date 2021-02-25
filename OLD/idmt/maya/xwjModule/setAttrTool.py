__author__ = 'xuweijian'
import maya.cmds as mc
from functools import partial


class setAttrTool():
    def creatUI(self):
        winName='setAttrWindow'
        if mc.window(winName, q = True, ex = True):
                mc.deleteUI(winName)
        mc.window(winName,h=100,w=300)
        mc.columnLayout()
        mc.textFieldGrp('tfAttribute',l='attribute:',cw2=[50,200])
        mc.textFieldGrp('tfAttrValue',l='value:',cw2=[50,200])
        mc.button('btnSet',w=250,l='set',c=partial(self.setAttribute))
        mc.setParent('..')
        mc.showWindow(winName)



    def setAttribute(self,UI=''):
        objs=mc.ls(sl=1)
        objsShape=mc.listRelatives(shapes=1)
        attribute=mc.textFieldGrp('tfAttribute',q=1,tx=1)
        print attribute
        attrValue=mc.textFieldGrp('tfAttrValue',q=1,tx=1)
        print attrValue
        for objShape in objsShape:
            allShapeAttr=mc.listAttr(objShape)
            if attribute in allShapeAttr:
                mc.setAttr('%s.%s'%(objShape,attribute),float(attrValue))
