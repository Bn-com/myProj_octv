# -*- coding: utf-8 -*-
# Copyright (C) 2000-2015 IDMT. All rights reserved.
'''
'''
__author__    = 'huangzhongwei@idmt.com.cn'
__date__    = '2015-03-19'

from functools import partial
import hashlib
import os
import re
import maya.cmds
import maya.mel
import idmt.pipeline.db

class AssetsInAnim(object):
    def __init__(self):
        if maya.cmds.window('AssetsInAnim', exists = True):
            maya.cmds.deleteUI('AssetsInAnim')
        maya.cmds.window('AssetsInAnim', title = u'镜头 - 素材', resizeToFitChildren  = True, height = 600)
        formLayout1 = maya.cmds.formLayout()
        sceneName = maya.cmds.file(query = True, sceneName = True, shortName = True)
        self.textFieldGrpFilename = maya.cmds.textFieldButtonGrp(columnWidth = (1, 80), label = u'文件名：', adjustableColumn = 2, text = sceneName, buttonLabel = u'搜索', buttonCommand = partial(self.OnBnClickedButtonSearch))
        tabLayout1 = maya.cmds.tabLayout(tabsVisible = False, scrollable = True, childResizable = True)
        maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.frameLayout(label = u'未参考', collapsable = True)
        maya.cmds.columnLayout(adjustableColumn = True)
        self.columnLayoutRequired = maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.setParent('..')
        maya.cmds.separator()
        maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.rowLayout(numberOfColumns = 2, columnWidth = (1, 20))
        maya.cmds.checkBox(label = '', onCommand = partial(self.OnBnClickedButtonSelectAll, self.columnLayoutRequired, True), offCommand = partial(self.OnBnClickedButtonSelectAll, self.columnLayoutRequired, False))
        maya.cmds.iconTextButton(image1 = 'createReference.png', width = 26, height = 26, annotation = 'Create selected reference', command = partial(self.OnBnClickedButtonCreateSelected))
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.frameLayout(label = u'多余或不正确', collapsable = True)
        maya.cmds.columnLayout(adjustableColumn = True)
        self.columnLayoutRedundant = maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.setParent('..')
        maya.cmds.separator()
        maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.rowLayout(numberOfColumns = 2, columnWidth = (1, 20))
        maya.cmds.checkBox(label = '', onCommand = partial(self.OnBnClickedButtonSelectAll, self.columnLayoutRedundant, True), offCommand = partial(self.OnBnClickedButtonSelectAll, self.columnLayoutRedundant, False))
        maya.cmds.iconTextButton(image1 = 'removeReference.png', width = 26, height = 26, annotation = 'Remove selected reference', command = partial(self.OnBnClickedButtonRemoveSelected))
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.setParent('..')
        maya.cmds.frameLayout(label = u'已参考', collapsable = True)
        self.columnLayoutReferenced = maya.cmds.columnLayout(adjustableColumn = True)
        maya.cmds.formLayout(formLayout1, edit = True, attachForm = ((self.textFieldGrpFilename, 'left', 0), (self.textFieldGrpFilename, 'top', 0), (self.textFieldGrpFilename, 'right', 0), (tabLayout1, 'left', 0), (tabLayout1, 'right', 0), (tabLayout1, 'bottom', 0)), attachControl = ((tabLayout1, 'top', 0, self.textFieldGrpFilename)))
        self.OnBnClickedButtonSearch()
        maya.cmds.showWindow('AssetsInAnim')

    def OnBnClickedButtonSearch(self):
        layouts = [self.columnLayoutReferenced, self.columnLayoutRequired, self.columnLayoutRedundant]
        for layout in layouts:
            ctrls = maya.cmds.columnLayout(layout, query = True, childArray = True)
            if ctrls != None:
                maya.cmds.deleteUI(ctrls)
        filename = maya.cmds.textFieldGrp(self.textFieldGrpFilename, query = True, text = True)
        if filename == '':
            return
        anim = idmt.pipeline.db.GetAnimByFilename(filename)
        if anim == None:
            return
        repository = anim.repository
        if os.path.isdir(os.getenv('IDMT_PROJECTS', '')):
            repository = repository.replace('\\\\file-cluster\\GDC\\Projects', '${IDMT_PROJECTS}')
        else:
            repository = repository.replace('\\\\file-cluster\\GDC', 'Z:')
        references = maya.cmds.file(query = True, reference = True)
        assets = anim.GetAssetNameInAnim()
        for asset in assets:
            sep = ''
            if asset.asset_sep != '':
                sep = '_%s' % asset.asset_sep
            find = False
            pattern = '/%s/Project/scenes/%s/%s/master/%s_%s%s_h_ms_anim.mb' % (anim.projectName, asset.asset_type, asset.asset_name, anim.shortName, asset.asset_name, sep)
            for i in range(len(references)):
                if i >= len(references):
                    break
                reference = references[i]
                if re.search(pattern, reference, re.IGNORECASE) != None:
                    find = True
                    maya.cmds.setParent(self.columnLayoutReferenced)
                    md5 = self.md5(reference)
                    maya.cmds.rowLayout('rowLayout_%s' % md5, numberOfColumns = 5, columnWidth5 = [20, 200, 26, 26, 26], adjustableColumn = 2, columnAlign = (2, 'left'), columnAttach = (1, 'right', 0))
                    rowLayouts = maya.cmds.columnLayout(self.columnLayoutReferenced, query = True, childArray = True)
                    maya.cmds.text(label = '%s.' % len(rowLayouts))
                    filename = maya.cmds.referenceQuery(reference, filename = True, shortName = True)
                    maya.cmds.text(label = filename, annotation = reference)
                    maya.cmds.iconTextButton(image1 = 'selectFileContents.png', width = 26, height = 26, annotation = 'Select file contents', command = partial(self.OnBnClickedButtonSelect, reference))
                    maya.cmds.iconTextButton(image1 = 'fileOpen.png', width = 26, height = 26, annotation = 'Explore', command = partial(self.OnBnClickedButtonExplore, reference))
                    references.pop(i)
                    i = i - 1
            if not find:
                path = r'%s\Project\scenes\%s\%s\master\%s_%s%s_h_ms_anim.mb' % (repository, asset.asset_type, asset.asset_name, anim.shortName, asset.asset_name, sep)
                reference = maya.cmds.workspace(expandName = path)
                enable = os.path.isfile(reference)
                maya.cmds.setParent(self.columnLayoutRequired)
                md5 = self.md5(path)
                maya.cmds.rowLayout('rowLayout_%s' % md5, numberOfColumns = 5, columnWidth5 = [20, 200, 26, 26, 26], adjustableColumn = 2, columnAlign = (2, 'left'))
                maya.cmds.checkBox(enable = enable, label = '', docTag = path)
                maya.cmds.text(label = asset.asset_name, annotation = reference)
                maya.cmds.iconTextButton(enable = enable, image1 = 'createReference.png', width = 26, height = 26, annotation = 'Create reference', command = partial(self.OnBnClickedButtonCreate, path))
                maya.cmds.iconTextButton(enable = enable, image1 = 'fileOpen.png', width = 26, height = 26, annotation = 'Explore', command = partial(self.OnBnClickedButtonExplore, path))
        for i in range(len(references)):
            reference = references[i]
            if re.search(r'_cam\.', reference, re.IGNORECASE) == None:
                maya.cmds.setParent(self.columnLayoutRedundant)
                md5 = self.md5(reference)
                maya.cmds.rowLayout('rowLayout_%s' % md5, numberOfColumns = 5, columnWidth5 = [20, 200, 26, 26, 26], adjustableColumn = 2, columnAlign = (2, 'left'))
                maya.cmds.checkBox(label = '', docTag = reference)
                filename = maya.cmds.referenceQuery(reference, filename = True, shortName = True)
                maya.cmds.text(label = filename, annotation = reference)
                maya.cmds.iconTextButton(image1 = 'removeReference.png', width = 26, height = 26, annotation = 'Remove reference', command = partial(self.OnBnClickedButtonRemove, reference))
                maya.cmds.iconTextButton(image1 = 'selectFileContents.png', width = 26, height = 26, annotation = 'Select file contents', command = partial(self.OnBnClickedButtonSelect, reference))
                maya.cmds.iconTextButton(image1 = 'fileOpen.png', width = 26, height = 26, annotation = 'Explore', command = partial(self.OnBnClickedButtonExplore, reference))

    def OnBnClickedButtonSelectAll(self, columnLayout, value, xxx):
        rowLayouts = maya.cmds.columnLayout(columnLayout, query = True, childArray = True)
        if rowLayouts != None:
            for rowLayout in rowLayouts:
                ctrls = maya.cmds.rowLayout(rowLayout, query = True, childArray = True)
                checkBox = ctrls[0]
                if maya.cmds.checkBox(checkBox, query = True, enable = True):
                    maya.cmds.checkBox(ctrls[0], edit = True, value = value)

    def OnBnClickedButtonCreateSelected(self):
        rowLayouts = maya.cmds.columnLayout(self.columnLayoutRequired, query = True, childArray = True)
        if rowLayouts != None:
            for rowLayout in rowLayouts:
                ctrls = maya.cmds.rowLayout(rowLayout, query = True, childArray = True)
                checkBox = ctrls[0]
                if maya.cmds.checkBox(checkBox, query = True, value = True):
                    path = maya.cmds.checkBox(checkBox, query = True, docTag = True)
                    self.OnBnClickedButtonCreate(path)

    def OnBnClickedButtonCreate(self, path):
        reference = maya.cmds.workspace(expandName = path)
        if not os.path.isfile(reference):
            return
        namespace = re.search('^[^_]+_[^_]+', os.path.basename(path)).group()
        mel = '''
        global proc string zwValidateNamespaceAssetsInAnim(string $name)
        {
            string $namespace = $name;

            //catch(`zwRemoveUnusedNamespace ":"`);

            namespace -setNamespace ":";

            if (`namespace -exists $namespace` || size(`ls $namespace`) > 0 || size(`ls ($namespace + ":*")`) > 0)
            {
                for ($i=1; ; $i++)
                {
                    $namespace = $name + "_" + $i;
                    if (!(`namespace -exists $namespace` || size(`ls $namespace`) > 0 || size(`ls ($namespace + ":*")`) > 0))
                    {
                        break;
                    }
                }
            }

            return $namespace;
        }
        '''
        maya.mel.eval(mel)
        namespace = maya.mel.eval('zwValidateNamespaceAssetsInAnim "%s"' % namespace)
        maya.cmds.namespace(setNamespace = ':')
        reference = maya.cmds.file(path, reference = True, groupReference = True, namespace = namespace)
        maya.cmds.namespace(setNamespace = ':')
        md5 = self.md5(path)
        maya.cmds.deleteUI('rowLayout_%s' % md5)
        maya.cmds.setParent(self.columnLayoutReferenced)
        md5 = self.md5(reference)
        maya.cmds.rowLayout('rowLayout_%s' % md5, numberOfColumns = 5, columnWidth5 = [20, 200, 26, 26, 26], adjustableColumn = 2, columnAlign = (2, 'left'), columnAttach = (1, 'right', 0))
        rowLayouts = maya.cmds.columnLayout(self.columnLayoutReferenced, query = True, childArray = True)
        maya.cmds.text(label = '%s.' % len(rowLayouts))
        filename = maya.cmds.referenceQuery(reference, filename = True, shortName = True)
        maya.cmds.text(label = filename, annotation = reference)
        maya.cmds.iconTextButton(image1 = 'selectFileContents.png', width = 26, height = 26, annotation = 'Select file contents', command = partial(self.OnBnClickedButtonSelect, reference))
        maya.cmds.iconTextButton(image1 = 'fileOpen.png', width = 26, height = 26, annotation = 'Explore', command = partial(self.OnBnClickedButtonExplore, reference))

    def OnBnClickedButtonExplore(self, path):
        folder = os.path.dirname(maya.cmds.workspace(expandName = path))
        if os.path.isdir(folder):
            os.system('explorer.exe "%s"' % re.sub(r'[/\\]', '\\\\', folder))

    def OnBnClickedButtonRemoveSelected(self):
        rowLayouts = maya.cmds.columnLayout(self.columnLayoutRedundant, query = True, childArray = True)
        if rowLayouts != None:
            for rowLayout in rowLayouts:
                ctrls = maya.cmds.rowLayout(rowLayout, query = True, childArray = True)
                checkBox = ctrls[0]
                if maya.cmds.checkBox(checkBox, query = True, value = True):
                    reference = maya.cmds.checkBox(checkBox, query = True, docTag = True)
                    self.OnBnClickedButtonRemove(reference)

    def OnBnClickedButtonRemove(self, reference):
        maya.cmds.file(reference, removeReference = True, force = True)
        md5 = self.md5(reference)
        maya.cmds.deleteUI('rowLayout_%s' % md5)

    def OnBnClickedButtonSelect(self, reference):
        maya.cmds.file(reference, selectAll = True)

    def md5(self, decodeStr):
        m = hashlib.md5()
        m.update(decodeStr)
        encodeStr = m.hexdigest()
        return encodeStr