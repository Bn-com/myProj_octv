# def myCreateFolder( address):
#     try:
#         os.makedirs(address)
#     except:
#         cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
#         CpauLocalPath, REMOTE_USER, REMOTE_PWD, address)
#         p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#         while True:
#             if not p.poll() is None:
#                 del p
#                 break
#             else:
#                 time.sleep(0.001)
#     time.sleep(0.1)
#
#     # 创建在W盘渲染deep的文件夹
#     def myCreateDeepFolder( address):
#         try:
#             os.makedirs(address)
#         except:
#             print address
#             cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
#                 CpauLocalPath, r'octvision\rd', r'rd1234', address)
#             print cmd
#             p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
#             while True:
#                 if not p.poll() is None:
#                     del p
#                     break
#                 else:
#                     time.sleep(0.001)
#         time.sleep(0.1)
#
#     # 创建相应场景
#     def myCreateScenes():
#         fileSN = fileSName.split('_')
#         while '' in fileSN:
#             fileSN.remove('')
#         ProjectName = '_'.join(fileSN[:3])
#         if copyType == 2 or copyType == 4:
#             serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSN[0], fileSN[1], fileSN[2], USERNAME,
#                                         ProjectName)
#         elif copyType == 1:
#             result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel',
#                                      ds='Cancel')
#             if result == 'OK':
#                 myPath = mc.promptDialog(q=True, t=True)
#                 if myPath[:2] == "z:":
#                     myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
#                 elif myPath[:2] == "Z:":
#                     myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
#                 if os.path.isdir(myPath):
#                     myPath = os.path.normpath(myPath)
#                     myLastPath = myPath.split("\\")[-1]
#                     myProjectName = os.path.splitext(fileSName)[0]
#                     if myLastPath.lower() == "work":
#                         ErrorFlag = True
#                         if len(fileSN) >= 3:
#                             # 判断服务器是否存在该工程
#                             serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation',
#                                                        fileSN[1], fileSN[2])
#                             if os.path.isdir(serFilePath):
#                                 ErrorFlag = False
#                                 serveProject = os.path.join(myPath, fileSN[0], ProjectName)
#                         if ErrorFlag:
#                             fileResult = mc.confirmDialog(title=u'温馨提示',
#                                                           message=u'服务器找不到相应的工程目录!\n是否直接在输入路径下按照文件名创建项目?',
#                                                           button=['Yes', 'No'], defaultButton='Yes',
#                                                           cancelButton='No', dismissString='No')
#                             if fileResult == 'Yes':
#                                 serveProject = os.path.join(myPath, myProjectName)
#                             else:
#                                 return False
#                     else:
#                         serveProject = os.path.join(myPath, myProjectName)
#                 else:
#                     mc.confirmDialog(m=u'无效路径，请重新输入')
#                     return False
#             else:
#                 return False
#
#         elif copyType == 5:
#             myPath = r"\\file2.nas\share\ALL\transfer"
#             # myPath = r"E:\b"
#             if myPath[:2] == "z:":
#                 myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
#             elif myPath[:2] == "Z:":
#                 myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
#             if os.path.isdir(myPath):
#                 serveProject = os.path.join(myPath, fileSN[0], fileSN[1], fileSN[2])
#             else:
#                 mc.confirmDialog(m=u'%s无效路径，请检查网络！' % myPath)
#                 return False
#
#             worker1.myLocalFlag = True
#             worker2.myLocalFlag = True
#
#         if not os.path.isdir(serveProject):
#             myCreateFolder(serveProject)
#             exampleProject = os.path.join(r"\\octvision.com\cg\Tech", NEWPROJECT_NAME)
#             copyData = {exampleProject: serveProject}
#             CopyDataJob(copyData, True)
#         return serveProject
#
#     def myCreateImagesFolder():
#         fileSNameSplit = fileSName.split('_')
#         # ProjectName = os.path.splitext(fileSName)[0]
#         serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1],
#                                     fileSNameSplit[2], USERNAME)
#         if not os.path.isdir(serveProject):
#             myCreateFolder(serveProject)
#         return serveProject
#
#
#
#
#
# def myCopyType_Files(self):
# tmpCopyFlag = True
# #判断是否有使用Arnold层
# type_file = 'sourceimages'
# serFileName = os.path.join(self.serveProject, type_file)
# allfiles = mc.ls(type='file')
# copyData = {}
# setData = {}
# if allfiles:
# for eachfile in allfiles:
# texFileNameGroup = []
# try:
# texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
# except:
# pass
# else:
# texFirstFileName = self.myChangeNetPath(texFirstFileName)
# #判断贴图是否开启了序列帧模式
# #序列标识：
# UseSeqFlag = mc.getAttr('%s.useFrameExtension' % eachfile)
#
# #获取选择uvTilingMode的模式
# UvSeqFlag = mc.getAttr('%s.uvTilingMode' % eachfile)
#
# if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
#     #当存在Arnold渲染器时
#     if self.ArnoldFlag:
#         #当仅仅是复制模式时，需要把普通贴图也拷贝
#         CopyHdrFlag = False
#         if self.copyType == 1 or self.copyType == 5:
#             texFileNameGroup.append(texFirstFileName)
#             CopyHdrFlag = True
#         PathSplitT = os.path.splitext(texFirstFileName)
#         if len(PathSplitT) > 1:
#             LowerPathType = PathSplitT[1].lower()
#             #当不是hdr贴图时，需要拷贝tx贴图
#             if LowerPathType != '.hdr':
#                 ArnoldTxFileName = PathSplitT[0]+'.tx'
#                 if os.path.isfile(ArnoldTxFileName):
#                     texFileNameGroup.append(ArnoldTxFileName)
#             else:
#                 if not CopyHdrFlag:
#                     texFileNameGroup.append(texFirstFileName)
#     else:
#         texFileNameGroup.append(texFirstFileName)
# #当开启了序列时
# elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2 :
#     myTexDirName = os.path.dirname(texFirstFileName)
#     myTexBaseName = os.path.basename(texFirstFileName)
#     myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
#     myAllFileName = os.listdir(myTexDirName)
#     for eachDirFileName in myAllFileName:
#         if eachDirFileName.find(myTexFileTopName) >= 0:
#             IndexTexName = '/'.join([myTexDirName, eachDirFileName])
#             #当存在Arnold渲染器时
#             if self.ArnoldFlag:
#                 #当仅仅是复制模式时，需要把普通贴图也拷贝
#                 CopyHdrFlag = False
#                 if self.copyType == 1 or self.copyType == 5:
#                     texFileNameGroup.append(IndexTexName)
#                     CopyHdrFlag = True
#                 IndexPathSplitT = os.path.splitext(IndexTexName)
#                 if len(IndexPathSplitT) > 1:
#                     IndexLowerPathType = IndexPathSplitT[1].lower()
#                     #当不是hdr贴图时，需要拷贝tx贴图
#                     if IndexLowerPathType != '.hdr' and not UseSeqFlag:
#                         IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
#                         if os.path.isfile(IndexArnoldTxFileName):
#                             texFileNameGroup.append(IndexArnoldTxFileName)
#                     else:
#                         if not CopyHdrFlag:
#                             texFileNameGroup.append(IndexTexName)
#             else:
#                 texFileNameGroup.append(IndexTexName)
#
# elif not UseSeqFlag and (UvSeqFlag == 2 or UvSeqFlag == 3):
#     myTexDirName = os.path.dirname(texFirstFileName)
#     myTexBaseName = os.path.basename(texFirstFileName)
#     myTexFileTopName = myTexBaseName.split('_u')[0]
#     if not myTexFileTopName:
#         myTexFileTopName = myTexBaseName.split('_U')[0]
#     myTexFileTopNames = re.findall(r'\D+', myTexBaseName)[0]
#
#     myAllFileName = os.listdir(myTexDirName)
#     for eachDirFileName in myAllFileName:
#         if eachDirFileName.find(myTexFileTopName) >= 0:
#             IndexTexName = '/'.join([myTexDirName, eachDirFileName])
#             #当存在Arnold渲染器时
#             if self.ArnoldFlag:
#                 #当仅仅是复制模式时，需要把普通贴图也拷贝
#                 CopyHdrFlag = False
#                 if self.copyType == 1 or self.copyType == 5:
#                     texFileNameGroup.append(IndexTexName)
#                     CopyHdrFlag = True
#                 IndexPathSplitT = os.path.splitext(IndexTexName)
#                 if len(IndexPathSplitT) > 1:
#                     IndexLowerPathType = IndexPathSplitT[1].lower()
#                     #当不是hdr贴图时，需要拷贝tx贴图
#                     if IndexLowerPathType != '.hdr':
#                         IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
#                         if os.path.isfile(IndexArnoldTxFileName):
#                             texFileNameGroup.append(IndexArnoldTxFileName)
#                     else:
#                         if not CopyHdrFlag:
#                             texFileNameGroup.append(IndexTexName)
#             else:
#                 texFileNameGroup.append(IndexTexName)
#         elif eachDirFileName.find(myTexFileTopNames) >= 0:
#             IndexTexName = '/'.join([myTexDirName, eachDirFileName])
#             #当存在Arnold渲染器时
#             if self.ArnoldFlag:
#                 #当仅仅是复制模式时，需要把普通贴图也拷贝
#                 CopyHdrFlag = False
#                 if self.copyType == 1 or self.copyType == 5:
#                     texFileNameGroup.append(IndexTexName)
#                     CopyHdrFlag = True
#                 IndexPathSplitT = os.path.splitext(IndexTexName)
#                 if len(IndexPathSplitT) > 1:
#                     IndexLowerPathType = IndexPathSplitT[1].lower()
#                     #当不是hdr贴图时，需要拷贝tx贴图
#                     if IndexLowerPathType != '.hdr' and not UseSeqFlag:
#                         IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
#                         if os.path.isfile(IndexArnoldTxFileName):
#                             texFileNameGroup.append(IndexArnoldTxFileName)
#                     else:
#                         if not CopyHdrFlag:
#                             texFileNameGroup.append(IndexTexName)
#             else:
#                 texFileNameGroup.append(IndexTexName)
#
# # print texFileNameGroup
# if texFileNameGroup:
#     for texFileName in texFileNameGroup:
#         # print texFileName
#         texFileName = os.path.normpath(texFileName)
#         texFileNameS = texFileName.split('\\')
#         try:
#             indexType = texFileNameS.index(type_file)
#         except:
#             texFileNameBN = os.path.basename(texFileName)
#             serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
#             copyFinalTexFilePath = serFileName
#         else:
#             serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
#             serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
#             copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
#         serFinalTexFileName = os.path.normpath(serFinalTexFileName)
#         copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
#         if texFileName != serFinalTexFileName:
#             #加入拷贝字典
#             #设置拷贝标帜
#             tmpCopyFlag = True
#             if os.path.isdir(serFileName):
#                 if os.path.isfile(serFinalTexFileName):
#                     testMtime = os.path.getmtime(texFileName)
#                     tmpMtime = os.path.getmtime(serFinalTexFileName)
#                     if int(tmpMtime) >= int(testMtime):
#                         tmpCopyFlag = False
#         else:
#             tmpCopyFlag = False
#         if tmpCopyFlag:
#             copyData.update({texFileName: copyFinalTexFilePath})
#     #加入设置字典，只设置第一帧
#     if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
#         #数组1是Arnold
#         setData.update({eachfile: serFinalTexFileName})
#     else:
#         mySetTexDirName = os.path.dirname(serFinalTexFileName)
#         serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
#         serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
#         if self.ArnoldFlag:
#             myFirstFileName = os.path.splitext(myTexBaseName)[0]+ '.tx'
#             #serFinalSetTexFileName = os.path.splitext(serFinalSetTexFileName)[0] + '.tx'
#             serFinalSetTexFileName = os.path.join(mySetTexDirName, myFirstFileName)
#             setData.update({eachfile: serFinalSetTexFileName})
#         else:
#             setData.update({eachfile: serFinalSetTexFileName})
# if copyData:
# mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData)+1, status=u"正在拷贝相应的 file 贴图!")
# #拷贝文件
# if not self.CopyDataJob(copyData, True):
# return False
# #设置路径
# for key in setData.keys():
# mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')
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
# return True
#
# if UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2:
#     print("HHHHH")
#     myTexDirName = os.path.dirname(texFirstFileName)
#     myTexBaseName = os.path.basename(texFirstFileName)
#
#     myTexBaseNameSpl = os.path.splitext(myTexBaseName)
#     re_isSeq = re.search('_\d+$|\.\d+$|_u\d+$|\.u\d+$', myTexBaseNameSpl[0])
#     if not re_isSeq:
#
#         texFileNameGroup = []
#
#         if UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2:
#             print("HHHHH")
#             myTexDirName = os.path.dirname(texFirstFileName)
#             myTexBaseName = os.path.basename(texFirstFileName)
#             myTexBaseNameSpl = os.path.splitext(myTexBaseName)
#             re_isSeq = re.search('_\d+$|\.\d+$|_u\d+$|\.u\d+$', myTexBaseNameSpl[0])
#             if not re_isSeq:
#                 texFileNameGroup.append(texFirstFileName)
#             else:
#                 myTexFileTopName = re.sub('_\d+$|\.\d+$|_u\d+$|\.u\d+$', '', myTexBaseNameSpl[0])
#                 myAllFileName = os.listdir(myTexDirName)
#                 for eachDirFileName in myAllFileName:
#                     # eachDirFileName = u'LYCB_ch001001Owner_head_1002.jpg'
#                     # eachDirFileName = u'LYCB_ch001001Owner_head_roughees_1001.tx'
#                     if eachDirFileName.find(myTexFileTopName) >= 0 and re.search(
#                             '{}(_\d+|\.\d+|_u\d+|\.u\d+)'.format(myTexFileTopName), eachDirFileName):
#                         IndexTexName = '/'.join([myTexDirName, eachDirFileName])
#                         # 当存在Arnold渲染器时
#                         if ArnoldFlag:
#                             # 当仅仅是复制模式时，需要把普通贴图也拷贝
#                             CopyHdrFlag = False
#                             if copyType == 1 or copyType == 5:
#                                 texFileNameGroup.append(IndexTexName)
#                                 print("append at ======1======")
#                                 CopyHdrFlag = True
#                             IndexPathSplitT = os.path.splitext(IndexTexName)
#                             if len(IndexPathSplitT) > 1:
#                                 IndexLowerPathType = IndexPathSplitT[1].lower()
#                                 # 当不是hdr贴图时，需要拷贝tx贴图
#                                 if IndexLowerPathType != '.hdr' and not UseSeqFlag:
#                                     IndexArnoldTxFileName = IndexPathSplitT[0] + '.tx'
#                                     if os.path.isfile(IndexArnoldTxFileName):
#                                         texFileNameGroup.append(IndexArnoldTxFileName)
#                                         print("append at =========2==========")
#                                 else:
#                                     if not CopyHdrFlag:
#                                         texFileNameGroup.append(IndexTexName)
#                                         print ("append at =============3===========")
#                         else:
#                             texFileNameGroup.append(IndexTexName)
#                             print("append at ======4===========")