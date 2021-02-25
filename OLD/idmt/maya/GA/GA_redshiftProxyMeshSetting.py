# -*- coding: utf-8 -*-

'''
Created on 2017-8-9

@author:韩虹

改自CG365
'''
import maya.cmds as mc
from idmt.maya.GA import GA_template as tp

def existsListConnections(object, nodeType):
    global RedshiftProxyMeshNode
    tempNode = mc.listConnections(object, s=1, d=0, p=0)
    if tempNode:
        for temp in tempNode:
            if mc.nodeType(temp) == nodeType:
                RedshiftProxyMeshNode = temp
            else:
                existsListConnections(object=temp, nodeType=nodeType)


class win(tp.templateWindow):

    def __init__(self):
        tp.templateWindow.__init__(self)
        self.uiContent['window'] = 'jn_redshiftProxyMeshSettingWindow'
        self.uiContent['title'] = u'Redshift Proxy Mesh Setting'
        self.uiContent['size'] = (367, 145)
        self.uiContent['commonButton'] = True

    def displayOptions(self, *args):
        self.uiContent['columnLayout'] = mc.columnLayout(adj=True)
        self.mode = mc.checkBoxGrp(numberOfCheckBoxes=1, label='Mode', label1='Select', v1=0)
        mc.separator(parent=self.uiContent['columnLayout'], style='in', h=5)
        self.group1 = mc.radioButtonGrp(vertical=1, select=1, numberOfRadioButtons=2, label='Display Mode', labelArray2=['Bounding Box', 'Preview Mesh'])
        mc.separator(parent=self.uiContent['columnLayout'], style='in', h=5)
        self.group2 = mc.radioButtonGrp(vertical=1, select=1, numberOfRadioButtons=2, label='Materials', labelArray2=['From Proxy', 'From Scene'])
        mc.formLayout(self.uiContent['optionsForm'], e=True, attachForm=([self.uiContent['columnLayout'], 'top', 0],
         [self.uiContent['columnLayout'], 'left', 2],
         [self.uiContent['columnLayout'], 'right', 2],
         [self.uiContent['columnLayout'], 'bottom', 0]))
        mc.window(self.uiContent['window'], widthHeight=self.uiContent['size'], resizeToFitChildren=1, sizeable=1, edit=True)

    def doIt(self, *args):
        global RedshiftProxyMeshNode
        nodes = []
        RedshiftProxyMeshNode = ''
        if mc.checkBoxGrp(self.mode, value1=True, query=True):
            sels = mc.ls(sl=1)
            if sels:
                for sel in sels:
                    shapes = mc.listRelatives(sel, shapes=1)
                    if shapes:
                        for shape in shapes:
                            existsListConnections(object=shape, nodeType='RedshiftProxyMesh')
                            nodes.append(RedshiftProxyMeshNode)

        else:
            nodes = mc.ls(type='RedshiftProxyMesh')
        selectItem1 = mc.radioButtonGrp(self.group1, select=1, q=1)
        selectItem2 = mc.radioButtonGrp(self.group2, select=1, q=1)
        print nodes
        if nodes:
            size = len(nodes)
            step = 100 / size
            amount = 0
            mc.progressWindow(title='Progress', progress=amount, status='completed:', isInterruptable=True)
            for index in range(0, size):
                if mc.getAttr(nodes[index] + '.displayMode') != selectItem1 - 1:
                    mc.setAttr(nodes[index] + '.displayMode', selectItem1 - 1)
                    mc.refresh()
                if mc.getAttr(nodes[index] + '.useSceneMaterials') != selectItem2 - 1:
                    mc.setAttr(nodes[index] + '.useSceneMaterials', selectItem2 - 1)
                if mc.progressWindow(query=True, isCancelled=True):
                    break
                if mc.progressWindow(query=True, progress=True) >= 100:
                    break
                amount += step
                mc.progressWindow(edit=True, progress=amount)

            mc.progressWindow(endProgress=1)


def main():
    win.showUI()


if __name__ == '__main__':
    main()