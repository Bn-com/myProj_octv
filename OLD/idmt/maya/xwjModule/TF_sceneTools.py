# -*- coding: utf-8 -*-
__author__ = 'xuweijian'

import maya.cmds as mc
from idmt.maya.commonCore.core_mayaCommon import sk_sceneTools
reload(sk_sceneTools)
from idmt.maya.commonCore.core_mayaCommon import sk_referenceConfig
reload(sk_referenceConfig)
from idmt.maya.commonCore.core_mayaCommon import sk_pyCommon
reload(sk_pyCommon)


class TF_sceneTools(sk_sceneTools.sk_sceneTools):
    def sk_sceneAssetNamespaceConfig(self):
        refInfos = sk_referenceConfig.sk_referenceConfig().checkReferenceListInfo()
        refNodes = refInfos[0][0]
        refPaths = refInfos[1][0]
        refNamespace = refInfos[2][0]

        allRefPaths = list(set(refPaths))

        for refPath in allRefPaths:
            assetInfo = refPath.split('/')[-1].split('_')
            if len(assetInfo) < 4:
                continue
            assetName = assetInfo[0] + '_' + assetInfo[1]
            # 只有一个时
            if refPaths.count(refPath) == 1:
                refIndex = refPaths.index(refPath)
                realRefPath = mc.referenceQuery(refNodes[refIndex], filename=1)
                newNamespace = assetName
                # 是否加载
                isRefLoad = mc.referenceQuery(refNodes[refIndex], isLoaded=1)
                if isRefLoad:
                    # 只处理非法名字
                    print '-------'
                    print newNamespace
                    print refNamespace[refIndex]
                    print realRefPath
                    if newNamespace != refNamespace[refIndex]:
                        try:
                            print '---000'
                            print realRefPath
                            mc.file(realRefPath, e=1, ns=newNamespace)
                        except:
                            print '\n'
                            print u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex])
                            print u'======有重复的namespace，重复编号往大处理======'
                            mc.error(u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex]))
            # 多个asset时
            else:
                allIndex = sk_pyCommon.sk_pyCommon().checkListSameAllIndex(refPaths, refPath)
                for i in range(len(allIndex)):
                    refIndex = allIndex[i]
                    realRefPath = mc.referenceQuery(refNodes[refIndex], filename=1)
                    newNamespace = assetName + '_' +  str(i + 1)
                    if i == 0:
                        newNamespace = assetName
                    # 是否加载
                    isRefLoad = mc.referenceQuery(refNodes[refIndex], isLoaded=1)
                    if isRefLoad:
                        # 只处理非法名字
                        if newNamespace != refNamespace[refIndex]:
                            try:
                                print '---001'
                                print realRefPath
                                mc.file(realRefPath, e=1, ns=newNamespace)
                            except:
                                print '\n'
                                print u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex])
                                print u'======有重复的namespace，重复编号往大处理======'
                                mc.error(u'======参考[%s]无法被编辑，请打开文件处理======' % (refNamespace[refIndex]))

