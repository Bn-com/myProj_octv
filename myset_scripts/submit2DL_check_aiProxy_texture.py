# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# '''
# __title__ = 'pc_checkinCommon'
# __author__ = zhangben
# __mtime__ = 2018/12/7:12:00
# # code is far away from bugs with the god animal protecting
# I love animals. They taste delicious.
# '''
#
#
# # 拷贝arnold代理文件和贴图
# def myCopy_Ar_Proxy(self):
# 判断arnold代理是否拷贝至服务器
# if self.copyType != 1:
# mValue = mc.radioButtonGrp('ArnoldProxy', q=True, sl=True)
# if mValue == 2:
# return True
#
# myType = 'aiStandIn'
# mtAttr = 'dso'
# tmpCopyFlag = True
# myLocalSourcePath = mc.workspace(en='sourceimages')
# try:
# allTypeShapes = mc.ls(type=myType)
# except:
# pass
# else:
# if allTypeShapes:
# copyData = {}
# setData = {}
# type_file = 'sourceimages'
# serFileName = os.path.join(self.serveProject, type_file)
# print serFileName
# print "\\n"
# for shapeEach in allTypeShapes:
# try:
# myFilepath = mc.getAttr('%s.dso' % shapeEach)
# except:
# pass
# else:
# if myFilepath:
# myFilepath = self.myChangeNetPath(myFilepath)
# # 获取文件名
# FileOkFlag = False
# if os.path.isfile(myFilepath):
#     FileOkFlag = True
# if not FileOkFlag:
#     myFilepath = myLocalSourcePath + '/%s' % myFilepath
#     if os.path.isfile(myFilepath):
#         FileOkFlag = True
# if FileOkFlag:
#     myFilepath = myFilepath.replace('/', '\\')
#     texFileNameS = myFilepath.split('\\')
#     indexType = texFileNameS.index(type_file)
#     # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
#     myFileBaseName = os.path.basename(myFilepath)
#
#     # 最终网络文件名
#     myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)
#     myFinalName = os.path.normpath(myFinalName)
#     # 原始的文件地址
#     myFilepath = os.path.normpath(myFilepath)
#     # 服务器地址
#     copyFinalTexFilePath = os.path.dirname(myFinalName)
#     copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
#     print copyFinalTexFilePath
#     if myFilepath != myFinalName:
#         # 加入拷贝文件
#         # 设置拷贝标帜
#         tmpCopyFlag = True
#         tempSetFlag = False
#         if os.path.isdir(serFileName):
#             if os.path.isfile(myFinalName):
#                 testMtime = os.path.getmtime(myFilepath)
#                 tmpMtime = os.path.getmtime(myFinalName)
#                 if int(tmpMtime) >= int(testMtime):
#                     tmpCopyFlag = False
#                     tempSetFlag = True
#         if tmpCopyFlag:
#             tempSetFlag = True
#             copyData.update({myFilepath: copyFinalTexFilePath})
#
#         if tempSetFlag:
#             # 加入设置字典
#             setData.update({shapeEach: myFinalName})
#
#     # 拷贝arnold贴图
#     myArFilePath = os.path.dirname(myFilepath)
#     myArFileName = os.path.basename(myFilepath)
#     myArImageFolder = myArFileName.split('_')[0]
#     # 原贴图文件夹
#     myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
#     myFinalImageFolder = os.path.join(serFileName, r'arnoldtex', myArImageFolder)
#     if os.path.isdir(myArFilePaths):
#         copyData.update({myArFilePaths: myFinalImageFolder})
#
# if self.copyType == 1 and not FileOkFlag:
#     # myFilepath = myFilepath.replace('/','\\')
#     # texFileNameS = myFilepath.split('\\')
#     # indexType = texFileNameS.index(type_file)
#     # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
#     myFileBaseName = os.path.basename(myFilepath)
#
#     # 最终网络文件名
#     # myFinalName = os.path.join(serFileName, myFileBaseName)
#     myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)
#
#     # 原始的文件地址
#     dirName = myFileBaseName.split('_')[0]
#     arProxyPathName = ''
#     proxyPaths = mc.getFileList(folder='%s' % OCT_ArnoldPathNew)
#     for i in proxyPaths:
#         paths = os.path.join(OCT_ArnoldPathNew, i, dirName, r'sourceimages', r'arnoldtex', myFileBaseName)
#         paths = paths.replace('/', '\\')
#         if os.path.isfile(paths):
#             arProxyPathName = paths
#             break
#
#     if arProxyPathName:
#         copyFinalTexFilePath = os.path.dirname(myFinalName)
#         copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
#         if arProxyPathName != myFinalName:
#             # 加入拷贝文件
#             # 设置拷贝标帜
#             tmpCopyFlag = True
#             tempSetFlag = False
#             if os.path.isdir(serFileName):
#                 if os.path.isfile(myFinalName):
#                     testMtime = os.path.getmtime(arProxyPathName)
#                     tmpMtime = os.path.getmtime(myFinalName)
#                     if int(tmpMtime) >= int(testMtime):
#                         tmpCopyFlag = False
#                         tempSetFlag = True
#             if tmpCopyFlag:
#                 tempSetFlag = True
#                 copyData.update({arProxyPathName: copyFinalTexFilePath})
#
#             if tempSetFlag:
#                 # 加入设置字典
#                 setData.update({shapeEach: myFinalName})
#
#     # 拷贝arnold贴图
#     myArFilePath = os.path.dirname(arProxyPathName)
#     myArFileName = os.path.basename(arProxyPathName)
#     myArImageFolder = myArFileName.split('_')[0]
#     # 原贴图文件夹
#     myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
#     myFinalImageFolder = os.path.join(copyFinalTexFilePath, myArImageFolder)
#     if os.path.isdir(myArFilePaths):
#         copyData.update({myArFilePaths: myFinalImageFolder})
#
# if copyData:
# mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 aiStandIn 文件!")
# # 拷贝文件
# if not self.CopyDataJob(copyData, True):
# return False
#
# if setData:
# for key in setData.keys():
# mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
# return True
#
# # #临时拷贝Arnold贴图文件夹
# # if mc.ls(type='aiStandIn'):
# #     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
# #     ArnoldProxyCopyData = {}
# #     if os.path.isdir(myLocalArnoldSourcePath):
# #         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
# #         serArnoldFileName = serFileName + '\\arnoldTex'
# #         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
# #         #拷贝文件
# #         if not self.CopyDataJob(ArnoldProxyCopyData, True):
# #             return False
# def myCopy_Proxy_OImagesModel(self, myType, mtAttr):
# tmpCopyFlag = True
# myLocalSourcePath = mc.workspace(en='sourceimages')
# try:
# allTypeShapes = mc.ls(type=myType)
# except:
# pass
# else:
# if allTypeShapes:
# copyData = {}
# setData = {}
# type_file = 'sourceimages'
# serFileName = os.path.join(self.serveProject, type_file)
# for shapeEach in allTypeShapes:
#     try:
#         myFilepath = mc.getAttr('%s.%s' % (shapeEach, mtAttr))
#     except:
#         pass
#     else:
#         if myFilepath:
#             myFilepath = self.myChangeNetPath(myFilepath)
#             # 获取文件名
#             FileOkFlag = False
#             if os.path.isfile(myFilepath):
#                 FileOkFlag = True
#             if not FileOkFlag:
#                 myFilepath = myLocalSourcePath + '/%s' % myFilepath
#                 if os.path.isfile(myFilepath):
#                     FileOkFlag = True
#             if FileOkFlag:
#                 myFileBaseName = os.path.basename(myFilepath)
#                 # 最终网络文件名
#                 myFinalName = os.path.join(serFileName, myFileBaseName)
#                 myFinalName = os.path.normpath(myFinalName)
#                 # 原始的文件地址
#                 myFilepath = os.path.normpath(myFilepath)
#                 # 服务器地址
#                 serFileName = os.path.normpath(serFileName)
#                 if myFilepath != myFinalName:
#                     # 加入拷贝文件
#                     # 设置拷贝标帜
#                     tmpCopyFlag = True
#                     if os.path.isdir(serFileName):
#                         if os.path.isfile(myFinalName):
#                             testMtime = os.path.getmtime(myFilepath)
#                             tmpMtime = os.path.getmtime(myFinalName)
#                             if int(tmpMtime) >= int(testMtime):
#                                 tmpCopyFlag = False
#                     if tmpCopyFlag:
#                         copyData.update({myFilepath: serFileName})
#                     # 加入设置字典
#                     setData.update({shapeEach: myFinalName})
# if copyData:
#     mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 %s 文件!" % myType)
#     # 拷贝文件
#     if not self.CopyDataJob(copyData, True):
#         return False
# for key in setData.keys():
#     mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
# return True
#
# # 拷贝arnold代理文件和贴图