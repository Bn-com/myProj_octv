class CopyProject(QtGui.QDialog):
# 发射完成比例
percent = QtCore.pyqtSignal('int')

def __init__(self, parent=None):
super(CopyProject, self).__init__(parent)
self.fileSName = mc.file(q=True, sn=True, shn=True)
self.CopyLocalPath = self.getCopyPath()
self.CpauLocalPath = self.getCPauPath()
self.worker1 = CopyJobThread(self)
self.worker2 = CopyJobThread(self)
self.percent.connect(self.EditProgressWindow)
self.stateMsg = ''
# copyType分三种模式
# 1 单纯拷贝模式
# 2 拷贝提交模式
# 3 单纯提交模式
self.copyType = 1
# 记录渲染层星系
self.myUseRender = []
self.ArnoldFlag = False

def __del__(self):
del self.worker1, self.worker2

def EditProgressWindow(self, i):
mc.progressWindow(edit=True, progress=i)

# 双线程拷贝
def CopyDataJob(self, myDict, OpenDoubleCopyFlag):
i = 0
for key in myDict.keys():
if mc.progressWindow(q=True, isCancelled=True):
    while True:
        if self.worker1.wait() and self.worker2.wait():
            break
    return False
mySourceFile = key
myDestFile = myDict[key]
if OpenDoubleCopyFlag:
    if i == 0:
        self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
    elif i == 1:
        self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
    else:
        while True:
            if self.worker1.isFinished():
                self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                break
            elif self.worker2.isFinished():
                self.worker2.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
                break
else:
    self.worker1.ready(self.CpauLocalPath, self.CopyLocalPath, mySourceFile, myDestFile)
    while True:
        if self.worker1.isFinished():
            break
i += 1
self.percent.emit(i)
while True:
if self.worker1.wait() and self.worker2.wait():
    break
return True

def fileCountIn(self, dir):
return sum([len(files) for root, dirs, files in os.walk(dir)])

# 拷贝fastcopy
def getCopyPath(self):
FCOPY_SPATH = r'\\octvision.com\cg\Tech\bin\FastCopy341\FastCopy.exe'
FCOPY_SPATH_BN = os.path.basename(FCOPY_SPATH)
FCOPY_SPATH_DN = os.path.dirname(FCOPY_SPATH)
FCOPY_LPATH_DN = r'C:\OCTVTools\fCopy'
cmd = ''
if os.path.isdir(FCOPY_LPATH_DN):
numSpath = self.fileCountIn(FCOPY_SPATH_DN)
numLpath = self.fileCountIn(FCOPY_LPATH_DN)
if numSpath != numLpath:
    cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (
    FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
else:
cmd = r'%s /cmd=update /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (
FCOPY_SPATH, FCOPY_SPATH_DN, FCOPY_LPATH_DN)
if cmd:
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while True:
    if not p.poll() is None:
        del p
        break
return os.path.join(FCOPY_LPATH_DN, FCOPY_SPATH_BN)

# 拷贝Cpau
def getCPauPath(self):
CPAY_SPATH = r'\\octvision.com\cg\Tech\bin\CPAU.exe'
CPAU_LPATH_DN = r'C:\OCTVTools\CPAU'
CPAU_LPATH_FP = r'C:\OCTVTools\CPAU\CPAU.exe'
cmd = ''
if not os.path.isfile(CPAU_LPATH_FP):
cmd = r'%s /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE "%s" /to="%s"' % (
self.CopyLocalPath, CPAY_SPATH, CPAU_LPATH_DN)
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while True:
    if not p.poll() is None:
        del p
        break
return CPAU_LPATH_FP

# 创建文件夹命令
def myCreateFolder(self, address):
try:
os.makedirs(address)
except:
cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
self.CpauLocalPath, REMOTE_USER, REMOTE_PWD, address)
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while True:
    if not p.poll() is None:
        del p
        break
    else:
        time.sleep(0.001)
time.sleep(0.1)

# 创建在W盘渲染deep的文件夹
def myCreateDeepFolder(self, address):
try:
os.makedirs(address)
except:
print address
cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
self.CpauLocalPath, r'octvision\rd', r'rd1234', address)
print cmd
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while True:
    if not p.poll() is None:
        del p
        break
    else:
        time.sleep(0.001)
time.sleep(0.1)

# 创建相应场景
def myCreateScenes(self):
fileSN = self.fileSName.split('_')
while '' in fileSN:
fileSN.remove('')
ProjectName = '_'.join(fileSN[:3])
if self.copyType == 2 or self.copyType == 4:
serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSN[0], fileSN[1], fileSN[2], USERNAME,
                            ProjectName)
elif self.copyType == 1:
result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
if result == 'OK':
    myPath = mc.promptDialog(q=True, t=True)
    if myPath[:2] == "z:":
        myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
    elif myPath[:2] == "Z:":
        myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
    if os.path.isdir(myPath):
        myPath = os.path.normpath(myPath)
        myLastPath = myPath.split("\\")[-1]
        myProjectName = os.path.splitext(self.fileSName)[0]
        if myLastPath.lower() == "work":
            ErrorFlag = True
            if len(fileSN) >= 3:
                # 判断服务器是否存在该工程
                serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1],
                                           fileSN[2])
                if os.path.isdir(serFilePath):
                    ErrorFlag = False
                    serveProject = os.path.join(myPath, fileSN[0], ProjectName)
            if ErrorFlag:
                fileResult = mc.confirmDialog(title=u'温馨提示',
                                              message=u'服务器找不到相应的工程目录!\n是否直接在输入路径下按照文件名创建项目?',
                                              button=['Yes', 'No'], defaultButton='Yes', cancelButton='No',
                                              dismissString='No')
                if fileResult == 'Yes':
                    serveProject = os.path.join(myPath, myProjectName)
                else:
                    return False
        else:
            serveProject = os.path.join(myPath, myProjectName)
    else:
        mc.confirmDialog(m=u'无效路径，请重新输入')
        return False
else:
    return False

elif self.copyType == 5:
myPath = r"\\file2.nas\share\ALL\transfer"
# myPath = r"E:\b"
if myPath[:2] == "z:":
    myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
elif myPath[:2] == "Z:":
    myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
if os.path.isdir(myPath):
    serveProject = os.path.join(myPath, fileSN[0], fileSN[1], fileSN[2])
else:
    mc.confirmDialog(m=u'%s无效路径，请检查网络！' % myPath)
    return False

self.worker1.myLocalFlag = True
self.worker2.myLocalFlag = True

if not os.path.isdir(serveProject):
self.myCreateFolder(serveProject)
exampleProject = os.path.join(r"\\octvision.com\cg\Tech", NEWPROJECT_NAME)
copyData = {exampleProject: serveProject}
self.CopyDataJob(copyData, True)
return serveProject

def myCreateImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1],
                        fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
self.myCreateFolder(serveProject)
return serveProject

# 创建deep输出素材的路径
def myCreateDeepImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(r"\\file.com\share\VFX\Images", fileSNameSplit[0], r'Deep', fileSNameSplit[1],
                        fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
self.myCreateDeepFolder(serveProject)
return serveProject

def myChangeNetPath(self, TempPath):
if TempPath.find('${OCTV_PROJECTS}') >= 0:
TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
elif TempPath.find('z:') >= 0:
TempPath = TempPath.replace('z:', OCT_DRIVE)
elif TempPath.find('Z:') >= 0:
TempPath = TempPath.replace('Z:', OCT_DRIVE)
elif TempPath.find('w:') >= 0:
TempPath = TempPath.replace('w:', OCT_FilePath)
elif TempPath.find('W:') >= 0:
TempPath = TempPath.replace('W:', OCT_FilePath)
elif TempPath.find('M:') >= 0:
TempPath = TempPath.replace('M:', OCT_MDRIVE)
elif TempPath.find('m:') >= 0:
TempPath = TempPath.replace('m:', OCT_MDRIVE)
return TempPath

def myJudeArnoldTxFile(self, texFileName):
PathSplitT = os.path.splitext(texFileName)
if len(PathSplitT) > 1:
LowerPathType = PathSplitT[1].lower()
if (LowerPathType != '.hdr') or (LowerPathType != '.tx'):
    ArnoldTxFileName = PathSplitT[0] + '.tx'
    if os.path.isfile(ArnoldTxFileName):
        return texFileName
else:
    return ArnoldTxFileName
return False

# 拷贝所有file节点的文件并改变节点
def myCopyType_Files(self):
tmpCopyFlag = True
# 判断是否有使用Arnold层
type_file = 'sourceimages'
serFileName = os.path.join(self.serveProject, type_file)
allfiles = mc.ls(type='file')
copyData = {}
setData = {}
if allfiles:
for eachfile in allfiles:
    texFileNameGroup = []
    try:
        texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
    except:
        pass
    else:
        texFirstFileName = self.myChangeNetPath(texFirstFileName)
        # 判断贴图是否开启了序列帧模式
        # 序列标识：
        UseSeqFlag = mc.getAttr('%s.useFrameExtension' % eachfile)

        # 获取选择uvTilingMode的模式
        UvSeqFlag = mc.getAttr('%s.uvTilingMode' % eachfile)

        if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
            # 当存在Arnold渲染器时
            if self.ArnoldFlag:
                # 当仅仅是复制模式时，需要把普通贴图也拷贝
                CopyHdrFlag = False
                if self.copyType == 1 or self.copyType == 5:
                    texFileNameGroup.append(texFirstFileName)
                    CopyHdrFlag = True
                PathSplitT = os.path.splitext(texFirstFileName)
                if len(PathSplitT) > 1:
                    LowerPathType = PathSplitT[1].lower()
                    # 当不是hdr贴图时，需要拷贝tx贴图
                    if LowerPathType != '.hdr':
                        ArnoldTxFileName = PathSplitT[0] + '.tx'
                        if os.path.isfile(ArnoldTxFileName):
                            texFileNameGroup.append(ArnoldTxFileName)
                    else:
                        if not CopyHdrFlag:
                            texFileNameGroup.append(texFirstFileName)
            else:
                texFileNameGroup.append(texFirstFileName)
        # 当开启了序列时
        elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2:
            myTexDirName = os.path.dirname(texFirstFileName)
            myTexBaseName = os.path.basename(texFirstFileName)
            myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
            myAllFileName = os.listdir(myTexDirName)
            for eachDirFileName in myAllFileName:
                if eachDirFileName.find(myTexFileTopName) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    # 当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        # 当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            # 当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                IndexArnoldTxFileName = IndexPathSplitT[0] + '.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)

        elif not UseSeqFlag and (UvSeqFlag == 2 or UvSeqFlag == 3):
            myTexDirName = os.path.dirname(texFirstFileName)
            myTexBaseName = os.path.basename(texFirstFileName)
            myTexFileTopName = myTexBaseName.split('_u')[0]
            if not myTexFileTopName:
                myTexFileTopName = myTexBaseName.split('_U')[0]
            myTexFileTopNames = re.findall(r'\D+', myTexBaseName)[0]

            myAllFileName = os.listdir(myTexDirName)
            for eachDirFileName in myAllFileName:
                if eachDirFileName.find(myTexFileTopName) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    # 当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        # 当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            # 当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr':
                                IndexArnoldTxFileName = IndexPathSplitT[0] + '.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)
                elif eachDirFileName.find(myTexFileTopNames) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    # 当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        # 当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            # 当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                IndexArnoldTxFileName = IndexPathSplitT[0] + '.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)

        # print texFileNameGroup
        if texFileNameGroup:
            for texFileName in texFileNameGroup:
                # print texFileName
                texFileName = os.path.normpath(texFileName)
                texFileNameS = texFileName.split('\\')
                try:
                    indexType = texFileNameS.index(type_file)
                except:
                    texFileNameBN = os.path.basename(texFileName)
                    serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                    copyFinalTexFilePath = serFileName
                else:
                    serLastTexFileName = '\\'.join(texFileNameS[indexType + 1::])
                    serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                    copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                if texFileName != serFinalTexFileName:
                    # 加入拷贝字典
                    # 设置拷贝标帜
                    tmpCopyFlag = True
                    if os.path.isdir(serFileName):
                        if os.path.isfile(serFinalTexFileName):
                            testMtime = os.path.getmtime(texFileName)
                            tmpMtime = os.path.getmtime(serFinalTexFileName)
                            if int(tmpMtime) >= int(testMtime):
                                tmpCopyFlag = False
                else:
                    tmpCopyFlag = False
                if tmpCopyFlag:
                    copyData.update({texFileName: copyFinalTexFilePath})
            # 加入设置字典，只设置第一帧
            if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                # 数组1是Arnold
                setData.update({eachfile: serFinalTexFileName})
            else:
                mySetTexDirName = os.path.dirname(serFinalTexFileName)
                serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
                serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
                if self.ArnoldFlag:
                    myFirstFileName = os.path.splitext(myTexBaseName)[0] + '.tx'
                    # serFinalSetTexFileName = os.path.splitext(serFinalSetTexFileName)[0] + '.tx'
                    serFinalSetTexFileName = os.path.join(mySetTexDirName, myFirstFileName)
                    setData.update({eachfile: serFinalSetTexFileName})
                else:
                    setData.update({eachfile: serFinalSetTexFileName})
if copyData:
    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData) + 1, status=u"正在拷贝相应的 file 贴图!")
    # 拷贝文件
    if not self.CopyDataJob(copyData, True):
        return False
# 设置路径
for key in setData.keys():
    mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')

# #临时拷贝Arnold贴图文件夹
# if mc.ls(type='aiStandIn'):
#     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
#     ArnoldProxyCopyData = {}
#     if os.path.isdir(myLocalArnoldSourcePath):
#         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
#         serArnoldFileName = serFileName + '\\arnoldTex'
#         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
#         #拷贝文件
#         if not self.CopyDataJob(ArnoldProxyCopyData, True):
#             return False
return True

def myCopy_Data(self):
# type_file = 'data'
types_file = ['data', 'cache']
other_file = 'otherCache'
setSercachePath = ''
# serFileName = os.path.join(self.serveProject, type_file)
allfiles = mc.ls(type='cacheFile')
copyData = {}
setData = {}
if allfiles:
for eachfile in allfiles:
    try:
        cachePath = mc.getAttr('%s.cachePath' % eachfile)
    except:
        pass
    else:
        cachePath = self.myChangeNetPath(cachePath)
        if OCT_MDRIVE in cachePath or OCT_FilePath in cachePath:
            continue
        cachePath = os.path.normpath(cachePath)
        cachePathS = cachePath.split('\\')
        for types in types_file:
            try:
                indexType = cachePathS.index(types)
                break
            except:
                pass
        if indexType:
            serLastcachePath = '\\'.join(cachePathS[indexType::])
            copyFinalcachePath = os.path.join(self.serveProject, serLastcachePath)
        else:
            copyFinalcachePath = os.path.join(self.serveProject, types, other_file)
        # try:
        #     indexType = cachePathS.index(type_file)
        # except:
        #     copyFinalcachePath = os.path.join(serFileName, other_file)
        # else:
        #     serLastcachePath = '\\'.join(cachePathS[indexType+1::])
        #     copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
        setSercachePath = '\\'.join(cachePathS[indexType::])
        copyFinalcachePath = os.path.normpath(copyFinalcachePath)
        if cachePath != copyFinalcachePath:
            # 整体文件夹拷贝
            if cachePath != copyFinalcachePath:
                copyData.update({cachePath: copyFinalcachePath})
            # 设置列表
            setData.update({eachfile: copyFinalcachePath})

if copyData:
    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 caChe 缓存!")
    # 拷贝文件
    if not self.CopyDataJob(copyData, False):
        return False
# 设置路径
for key in setData.keys():
    try:
        mc.setAttr('%s.cachePath' % key, setData[key], type='string')
    except:
        mc.warning(u'cacheFile设置文件出错！')
        return False
return True

# 拷贝Yeti缓存和贴图
def myCopy_YetiCache(self):
# 缓存
type_file = 'cache'
other_file = 'otherCache'
setSercachePath = ''
serFileName = os.path.join(self.serveProject, type_file)
serFileName = os.path.normpath(serFileName)
# 贴图
type_TexFile = 'sourceimages'
serTexFileName = os.path.join(self.serveProject, type_TexFile)
serFileName = os.path.normpath(serFileName)
allYetiCacheFiles = mc.ls(type='pgYetiMaya')
setTexData = {}
# 进行
setSerTexPath = ''
copyData = {}
setData = {}
if allYetiCacheFiles:
for myYetiCacheFile in allYetiCacheFiles:
    YetiFileMode = None
    try:
        YetiFileMode = mc.getAttr('%s.fileMode' % myYetiCacheFile)
    except:
        pass
    else:
        if YetiFileMode == 1:
            YetiCachePath = mc.getAttr('%s.cacheFileName' % myYetiCacheFile)
            if YetiCachePath:
                YetiCachePath = self.myChangeNetPath(YetiCachePath)
                YetiCachePath = os.path.normpath(YetiCachePath)
                cachePathS = YetiCachePath.split('\\')
                try:
                    indexType = cachePathS.index(type_file)
                except:
                    copyFinalcachePath = os.path.join(serFileName, other_file, '%s' % myYetiCacheFile)
                else:
                    serLastcachePath = '\\'.join(cachePathS[indexType + 1:-1])
                    copyFinalcachePath = os.path.join(serFileName, serLastcachePath)
                YetiCacheBasePath = os.path.basename(YetiCachePath)
                YetiCacheDirPath = os.path.dirname(YetiCachePath)
                setSercachePath = os.path.join(copyFinalcachePath, YetiCacheBasePath)
                copyFinalcachePath = os.path.normpath(copyFinalcachePath)
                # 整体文件夹拷贝
                if YetiCacheDirPath != copyFinalcachePath:
                    copyData.update({YetiCacheDirPath: copyFinalcachePath})
                    setSercachePath = setSercachePath.replace("\\", "/")
                    setData.update({myYetiCacheFile: setSercachePath})
        # 拷贝和设置贴图
        YetiTexPath = mc.getAttr('%s.imageSearchPath' % myYetiCacheFile)
        if YetiTexPath:
            YetiTexPath = self.myChangeNetPath(YetiTexPath)
            if os.path.isdir(YetiTexPath):
                copyFinalTexPath = os.path.join(serTexFileName, "Yeti")
                YetiTexPath = os.path.normpath(YetiTexPath)
                if YetiTexPath != copyFinalTexPath:
                    copyData.update({YetiTexPath: copyFinalTexPath})
                    setTexData.update({myYetiCacheFile: copyFinalTexPath})

        if copyData:
            mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData),
                              status=u"正在拷贝相应的 pgYetiMaya Yeti缓存!")
            # 拷贝文件
            if not self.CopyDataJob(copyData, False):
                return False
        # 设置路径
        for key in setData.keys():
            try:
                mc.setAttr('%s.cacheFileName' % key, setData[key], type='string')
            except:
                mc.warning(u'Yeti的缓存设置文件出错！')
                return False
        for key in setTexData.keys():
            try:
                mc.setAttr('%s.imageSearchPath' % key, setTexData[key], type='string')
            except:
                mc.warning(u'Yeti的贴图设置文件出错！')
                return False
return True

# 拷贝所有ABC的data节点的文件并改变节点
def myCopy_AbcData(self):
tmpCopyFlag = True
type_file = 'alembic'
serFileName = os.path.join(self.serveProject, 'cache\\' + type_file)
allfiles = mc.ls(type='AlembicNode')
copyData = {}
setData = {}
if allfiles:
for eachfile in allfiles:
    try:
        abcCachePath = mc.getAttr('%s.abc_File' % eachfile)
    except:
        pass
    else:
        abcCachePath = self.myChangeNetPath(abcCachePath)
        abcCachePath = os.path.normpath(abcCachePath)
        mc.setAttr('%s.abc_File' % eachfile, abcCachePath, type='string')
        abcCachePath_S = abcCachePath.split('\\')
        # 多层目录
        copyFinalAbcCachePath = ''
        try:
            indexType = abcCachePath_S.index(type_file)
        except:
            abcCachePathBN = os.path.basename(abcCachePath)
            serFinalAbcCachePath = os.path.join(serFileName, abcCachePathBN)
            copyFinalAbcCachePath = serFileName
            copyFinalAbcCachePath_dir = serFileName
        else:
            serLastAbcCachePath = '\\'.join(abcCachePath_S[indexType + 1::])
            copyFinalAbcCachePath = os.path.join(serFileName, serLastAbcCachePath)
            copyFinalAbcCachePath_dir = os.path.dirname(copyFinalAbcCachePath)
        if copyFinalAbcCachePath:
            copyFinalAbcCachePath = os.path.normpath(copyFinalAbcCachePath)
            copyFinalAbcCachePath_dir = os.path.normpath(copyFinalAbcCachePath_dir)
            if abcCachePath != copyFinalAbcCachePath:
                # 拷贝列表
                # 设置拷贝标帜
                tmpCopyFlag = True
                if os.path.isdir(serFileName):
                    if os.path.isfile(copyFinalAbcCachePath):
                        testMtime = os.path.getmtime(abcCachePath)
                        tmpMtime = os.path.getmtime(copyFinalAbcCachePath)
                        if int(tmpMtime) >= int(testMtime):
                            tmpCopyFlag = False
                if tmpCopyFlag:
                    copyData.update({abcCachePath: copyFinalAbcCachePath_dir})
                # 设置列表
                setData.update({eachfile: copyFinalAbcCachePath})
if copyData:
    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 Alembic caChe 缓存!")
    # 拷贝文件
    if not self.CopyDataJob(copyData, False):
        return False
# 设置路径
for key in setData.keys():
    if os.path.isfile(setData[key]):
        mc.setAttr('%s.abc_File' % key, setData[key], type='string')
return True

# 拷贝所有Shave缓存
def myCopy_Shavedata(self):
tmpCopyFlag = True
type_file = 'shave'
serFileName = os.path.join(self.serveProject, 'cache\\' + type_file)
copyData = {}
setData = {}
allOnlyShaveShapes = []
allShaveShapes = mc.ls(type='shaveHair')
for eachShape in allShaveShapes:
allOnlyShaveShapes.append(eachShape.split("|")[-1])
allShaveOnlyNames = []
for OnlyShaveShape in allOnlyShaveShapes:
allShaveOnlyNames.append("shaveStatFile_%s" % OnlyShaveShape)
allOnlyShaveShapes = list(set(allOnlyShaveShapes))
myshaveGlobals = "shaveGlobals"
if allShaveShapes and myshaveGlobals:
shavePath = mc.getAttr("%s.tmpDir" % myshaveGlobals)
if shavePath:
    shavePath = self.myChangeNetPath(shavePath)
    if not os.path.isdir(shavePath):
        proPath = mc.workspace(q=True, rd=True)
        shavePath = os.path.normpath(os.path.join(proPath, shavePath))
    shavePath = self.myChangeNetPath(shavePath)
    if os.path.isdir(shavePath):
        allSahveDirs = os.listdir(shavePath)
        if allSahveDirs:
            # 多层目录
            shavePath = os.path.normpath(shavePath)
            shaveCachePath_S = shavePath.split('\\')
            try:
                indexType = shaveCachePath_S.index(type_file)
            except:
                shaveCachePathBN = os.path.basename(shavePath)
                serFinalShaveCachePath = os.path.join(serFileName, shaveCachePathBN)
                copyFinalShaveCacheDir = serFileName
            else:
                serLastShaveCachePath = '\\'.join(shaveCachePath_S[indexType + 1::])
                copyFinalShaveCacheDir = os.path.join(serFileName, serLastShaveCachePath)
            copyFinalShaveCacheDir = os.path.normpath(copyFinalShaveCacheDir)
            # 整体文件夹拷贝
            # 单文件，赛选时间重复拷贝
            if os.path.isdir(copyFinalShaveCacheDir):
                if copyFinalShaveCacheDir != copyFinalShaveCacheDir:
                    copyData.update({copyFinalShaveCacheDir: copyFinalShaveCacheDir})
            setData.update({myshaveGlobals: copyFinalShaveCacheDir})
    if copyData:
        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData),
                          status=u"正在拷贝相应的 Shave caChe 缓存!")
        # 拷贝文件
        if not self.CopyDataJob(copyData, False):
            return False
    # 设置路径
    for key in setData.keys():
        mc.setAttr('%s.tmpDir' % key, setData[key], type='string')
return True

# 拷贝粒子缓存
def myCopy_Particles(self):
tmpCopyFlag = True
type_file = 'particles'
type_cache = 'cache'
serFileName = os.path.join(self.serveProject, type_cache, type_file)
AllIsParFlag = False
myAllParticles = mc.ls(type='particle')
for eachP in myAllParticles:
if mc.nodeType(eachP) == 'particle':
    AllIsParFlag = True
    break
mydynGlobals = mc.dynGlobals(q=True, a=True)
copyData = {}
if mydynGlobals and AllIsParFlag:
fileShortName = os.path.splitext(self.fileSName)[0]
# parPath = mc.workspace(en='particles')
parPath = mc.workspace(fullName=True) + "/cache/particles"
cacheDirectory = mc.getAttr('%s.cacheDirectory' % mydynGlobals)
if not cacheDirectory:
    cacheDirectory = fileShortName
parCachePath = os.path.join(parPath, cacheDirectory)
parCachePath = os.path.normpath(parCachePath)
parCacheSPath = os.path.join(parPath, cacheDirectory + '_startup')
parCacheSPath = os.path.normpath(parCacheSPath)
# 粒子缓存文件
if mc.getAttr('%s.useParticleDiskCache' % mydynGlobals):
    if os.path.isdir(parCachePath):
        if cacheDirectory != 'untitled':
            serFinalPerPath = os.path.join(serFileName, cacheDirectory)
        else:
            serFinalPerPath = os.path.join(serFileName, fileShortName + '_' + cacheDirectory)
        serFinalPerPath = os.path.normpath(serFinalPerPath)
        # 整个文件拷贝方式
        if parCachePath != serFinalPerPath:
            copyData.update({parCachePath: serFinalPerPath})
# 拷贝初始化缓存方案
if not os.path.isdir(parCacheSPath):
    cacheDirectory = fileShortName
    parCacheSPath = os.path.join(parPath, cacheDirectory + '_startup')
# 粒子初始化文件
if os.path.isdir(parCacheSPath):
    if cacheDirectory != 'untitled':
        serFinalPerSPath = os.path.join(serFileName, cacheDirectory + '_startup')
    else:
        serFinalPerSPath = os.path.join(serFileName, fileShortName + '_' + cacheDirectory + '_startup')
    serFinalPerSPath = os.path.normpath(serFinalPerSPath)
    # 整个文件拷贝方式
    if parCacheSPath != serFinalPerSPath:
        copyData.update({parCacheSPath: serFinalPerSPath})
if copyData:
    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 particle缓存!")
    # 拷贝文件
    if not self.CopyDataJob(copyData, False):
        return False
# 设置粒子缓存的新文件名
if cacheDirectory == 'untitled':
    parCacheNName = fileShortName + '_' + cacheDirectory
    mc.setAttr('%s.cacheDirectory' % mydynGlobals, parCacheNName, type='string')
return True

# 拷贝Vray、Arnold代理、某些贴图节点的文件
def myCopy_Proxy_OImagesModel(self, myType, mtAttr):
tmpCopyFlag = True
myLocalSourcePath = mc.workspace(en='sourceimages')
try:
allTypeShapes = mc.ls(type=myType)
except:
pass
else:
if allTypeShapes:
    copyData = {}
    setData = {}
    type_file = 'sourceimages'
    serFileName = os.path.join(self.serveProject, type_file)
    for shapeEach in allTypeShapes:
        try:
            myFilepath = mc.getAttr('%s.%s' % (shapeEach, mtAttr))
        except:
            pass
        else:
            if myFilepath:
                myFilepath = self.myChangeNetPath(myFilepath)
                # 获取文件名
                FileOkFlag = False
                if os.path.isfile(myFilepath):
                    FileOkFlag = True
                if not FileOkFlag:
                    myFilepath = myLocalSourcePath + '/%s' % myFilepath
                    if os.path.isfile(myFilepath):
                        FileOkFlag = True
                if FileOkFlag:
                    myFileBaseName = os.path.basename(myFilepath)
                    # 最终网络文件名
                    myFinalName = os.path.join(serFileName, myFileBaseName)
                    myFinalName = os.path.normpath(myFinalName)
                    # 原始的文件地址
                    myFilepath = os.path.normpath(myFilepath)
                    # 服务器地址
                    serFileName = os.path.normpath(serFileName)
                    if myFilepath != myFinalName:
                        # 加入拷贝文件
                        # 设置拷贝标帜
                        tmpCopyFlag = True
                        if os.path.isdir(serFileName):
                            if os.path.isfile(myFinalName):
                                testMtime = os.path.getmtime(myFilepath)
                                tmpMtime = os.path.getmtime(myFinalName)
                                if int(tmpMtime) >= int(testMtime):
                                    tmpCopyFlag = False
                        if tmpCopyFlag:
                            copyData.update({myFilepath: serFileName})
                        # 加入设置字典
                        setData.update({shapeEach: myFinalName})
    if copyData:
        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData),
                          status=u"正在拷贝相应的 %s 文件!" % myType)
        # 拷贝文件
        if not self.CopyDataJob(copyData, True):
            return False
    for key in setData.keys():
        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
return True

# 拷贝arnold代理文件和贴图
def myCopy_Ar_Proxy(self):
# 判断arnold代理是否拷贝至服务器
if self.copyType != 1:
mValue = mc.radioButtonGrp('ArnoldProxy', q=True, sl=True)
if mValue == 2:
    return True

myType = 'aiStandIn'
mtAttr = 'dso'
tmpCopyFlag = True
myLocalSourcePath = mc.workspace(en='sourceimages')
try:
allTypeShapes = mc.ls(type=myType)
except:
pass
else:
if allTypeShapes:
    copyData = {}
    setData = {}
    type_file = 'sourceimages'
    serFileName = os.path.join(self.serveProject, type_file)
    print serFileName
    print "\\n"
    for shapeEach in allTypeShapes:
        try:
            myFilepath = mc.getAttr('%s.dso' % shapeEach)
        except:
            pass
        else:
            if myFilepath:
                myFilepath = self.myChangeNetPath(myFilepath)
                # 获取文件名
                FileOkFlag = False
                if os.path.isfile(myFilepath):
                    FileOkFlag = True
                if not FileOkFlag:
                    myFilepath = myLocalSourcePath + '/%s' % myFilepath
                    if os.path.isfile(myFilepath):
                        FileOkFlag = True
                if FileOkFlag:
                    myFilepath = myFilepath.replace('/', '\\')
                    texFileNameS = myFilepath.split('\\')
                    indexType = texFileNameS.index(type_file)
                    # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
                    myFileBaseName = os.path.basename(myFilepath)

                    # 最终网络文件名
                    myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)
                    myFinalName = os.path.normpath(myFinalName)
                    # 原始的文件地址
                    myFilepath = os.path.normpath(myFilepath)
                    # 服务器地址
                    copyFinalTexFilePath = os.path.dirname(myFinalName)
                    copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                    print copyFinalTexFilePath
                    if myFilepath != myFinalName:
                        # 加入拷贝文件
                        # 设置拷贝标帜
                        tmpCopyFlag = True
                        tempSetFlag = False
                        if os.path.isdir(serFileName):
                            if os.path.isfile(myFinalName):
                                testMtime = os.path.getmtime(myFilepath)
                                tmpMtime = os.path.getmtime(myFinalName)
                                if int(tmpMtime) >= int(testMtime):
                                    tmpCopyFlag = False
                                    tempSetFlag = True
                        if tmpCopyFlag:
                            tempSetFlag = True
                            copyData.update({myFilepath: copyFinalTexFilePath})

                        if tempSetFlag:
                            # 加入设置字典
                            setData.update({shapeEach: myFinalName})

                    # 拷贝arnold贴图
                    myArFilePath = os.path.dirname(myFilepath)
                    myArFileName = os.path.basename(myFilepath)
                    myArImageFolder = myArFileName.split('_')[0]
                    # 原贴图文件夹
                    myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
                    myFinalImageFolder = os.path.join(serFileName, r'arnoldtex', myArImageFolder)
                    if os.path.isdir(myArFilePaths):
                        copyData.update({myArFilePaths: myFinalImageFolder})

                if self.copyType == 1 and not FileOkFlag:
                    # myFilepath = myFilepath.replace('/','\\')
                    # texFileNameS = myFilepath.split('\\')
                    # indexType = texFileNameS.index(type_file)
                    # myFileBaseName = '\\'.join(texFileNameS[indexType+1::])
                    myFileBaseName = os.path.basename(myFilepath)

                    # 最终网络文件名
                    # myFinalName = os.path.join(serFileName, myFileBaseName)
                    myFinalName = os.path.join(serFileName, r'arnoldtex', myFileBaseName)

                    # 原始的文件地址
                    dirName = myFileBaseName.split('_')[0]
                    arProxyPathName = ''
                    proxyPaths = mc.getFileList(folder='%s' % OCT_ArnoldPathNew)
                    for i in proxyPaths:
                        paths = os.path.join(OCT_ArnoldPathNew, i, dirName, r'sourceimages', r'arnoldtex',
                                             myFileBaseName)
                        paths = paths.replace('/', '\\')
                        if os.path.isfile(paths):
                            arProxyPathName = paths
                            break

                    if arProxyPathName:
                        copyFinalTexFilePath = os.path.dirname(myFinalName)
                        copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                        if arProxyPathName != myFinalName:
                            # 加入拷贝文件
                            # 设置拷贝标帜
                            tmpCopyFlag = True
                            tempSetFlag = False
                            if os.path.isdir(serFileName):
                                if os.path.isfile(myFinalName):
                                    testMtime = os.path.getmtime(arProxyPathName)
                                    tmpMtime = os.path.getmtime(myFinalName)
                                    if int(tmpMtime) >= int(testMtime):
                                        tmpCopyFlag = False
                                        tempSetFlag = True
                            if tmpCopyFlag:
                                tempSetFlag = True
                                copyData.update({arProxyPathName: copyFinalTexFilePath})

                            if tempSetFlag:
                                # 加入设置字典
                                setData.update({shapeEach: myFinalName})

                    # 拷贝arnold贴图
                    myArFilePath = os.path.dirname(arProxyPathName)
                    myArFileName = os.path.basename(arProxyPathName)
                    myArImageFolder = myArFileName.split('_')[0]
                    # 原贴图文件夹
                    myArFilePaths = os.path.join(myArFilePath, myArImageFolder)
                    myFinalImageFolder = os.path.join(copyFinalTexFilePath, myArImageFolder)
                    if os.path.isdir(myArFilePaths):
                        copyData.update({myArFilePaths: myFinalImageFolder})

    if copyData:
        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData), status=u"正在拷贝相应的 aiStandIn 文件!")
        # 拷贝文件
        if not self.CopyDataJob(copyData, True):
            return False

    if setData:
        for key in setData.keys():
            mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
return True

# #临时拷贝Arnold贴图文件夹
# if mc.ls(type='aiStandIn'):
#     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
#     ArnoldProxyCopyData = {}
#     if os.path.isdir(myLocalArnoldSourcePath):
#         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
#         serArnoldFileName = serFileName + '\\arnoldTex'
#         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
#         #拷贝文件
#         if not self.CopyDataJob(ArnoldProxyCopyData, True):
#             return False

# 拷贝Vr光子贴图、焦散贴图
def myCopy_VrSetFilesModel(self, typeOn, typeModel, typeFuleAttr, numModel):
tmpCopyFlag = True
copyData = {}
typeName = ''
type_file = 'sourceimages'
serFileName = os.path.join(self.serveProject, type_file)
try:
if mc.getAttr("vraySettings.%s" % typeOn):
    if mc.getAttr('vraySettings.%s' % typeModel) == numModel:
        localFile = mc.getAttr('vraySettings.%s' % typeFuleAttr)
        if localFile:
            localFile = self.myChangeNetPath(localFile)
            locaFileBaseName = os.path.basename(localFile)
            serFileFinalName = os.path.join(serFileName, locaFileBaseName)
            serFileFinalName = os.path.normpath(serFileFinalName)
            serFileName = os.path.normpath(serFileName)
            localFile = os.path.normpath(localFile)
            if os.path.isfile(localFile):
                if localFile != serFileFinalName:
                    # 设置拷贝标帜
                    tmpCopyFlag = True
                    if os.path.isdir(serFileName):
                        if os.path.isfile(serFileFinalName):
                            testMtime = os.path.getmtime(localFile)
                            tmpMtime = os.path.getmtime(serFileFinalName)
                            if int(tmpMtime) >= int(testMtime):
                                tmpCopyFlag = False
                    if tmpCopyFlag:
                        copyData.update({localFile: serFileName})
                    if typeModel == 'imap_mode':
                        typeName = u'Irradiance map光子贴图'
                    elif typeModel == 'imap_mode':
                        typeName = u'Light cache map光子贴图'
                    else:
                        typeName = u'Caustics的焦散贴图'
                    if copyData:
                        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData),
                                          status=u"正在拷贝相应的Vray的 %s!" % typeName)
                        if not self.CopyDataJob(copyData, True):
                            return False
                    mc.setAttr('vraySettings.%s' % typeFuleAttr, serFileFinalName, type='string')
except:
pass
return True

def myCopy_Mr(self):
# 拷贝mentalrayIblShape节点的贴图
mrIbType = 'mentalrayIblShape'
mrIbAttr = 'texture'
if not self.myCopy_Proxy_OImagesModel(mrIbType, mrIbAttr):
return False
# 拷贝mentalrayTexture节点的贴图
mrTxType = 'mentalrayTexture'
mrTxAttr = 'fileTextureName'
if not self.myCopy_Proxy_OImagesModel(mrTxType, mrTxAttr):
return False
return True

def myCopy_Vr(self):
# 拷贝Vray的代理
VrType = 'VRayMesh'
VrAttr = 'fileName'
if not self.myCopy_Proxy_OImagesModel(VrType, VrAttr):
return False
# 检查Vray的VRayLightIESShape灯光贴图
VrIesLType = 'VRayLightIESShape'
VrIesLAttr = 'iesFile'
if not self.myCopy_Proxy_OImagesModel(VrIesLType, VrIesLAttr):
return False
# Irradiance map光子贴图
IrrMap_typeOn = 'giOn'
IrrMap_typeModel = 'imap_mode'
IrrMap_typeFuleAttr = 'imap_fileName'
IrrMap_numModel = 2
if not self.myCopy_VrSetFilesModel(IrrMap_typeOn, IrrMap_typeModel, IrrMap_typeFuleAttr, IrrMap_numModel):
return False
# Light cache map光子贴图
LightC_typeOn = 'giOn'
LightC_typeModel = 'mode'
LightC_typeFuleAttr = 'fileName'
LightC_numModel = 2
if not self.myCopy_VrSetFilesModel(LightC_typeOn, LightC_typeModel, LightC_typeFuleAttr, LightC_numModel):
return False
# Caustics的焦散贴图
Caustics_typeOn = 'causticsOn'
Caustics_typeModel = 'causticsMode'
Caustics_typeFuleAttr = 'causticsFile'
Caustics_numModel = 1
if not self.myCopy_VrSetFilesModel(Caustics_typeOn, Caustics_typeModel, Caustics_typeFuleAttr,
                               Caustics_numModel):
return False
return True

def myCopy_Ar(self):
# 拷贝Arnold代理与代理贴图
if not self.myCopy_Ar_Proxy():
return False
# ArType = 'aiStandIn'
# ArAttr = 'dso'
# if not self.myCopy_Proxy_OImagesModel(ArType, ArAttr):
#     return False
# 拷贝Arnold的aiPhotometricLight灯光贴图
###################
# 改完路径后，显示的路径却没有改变，用脚本查询到时改了~~~~Arnold的Bug
####################
ArIesLType = 'aiPhotometricLight'
ArIesLAttr = 'aiFilename'
if not self.myCopy_Proxy_OImagesModel(ArIesLType, ArIesLAttr):
return False
return True

# 拷贝mrIb贴图、mrTex节点的贴图路径、摄像机投影贴图、检查Vray的VRayLightIESShape灯光贴图
def myCopy_OtherImages(self):
# 检查摄像机投影贴图
camImType = 'imagePlane'
camImAttr = 'imageName'
if not self.myCopy_Proxy_OImagesModel(camImType, camImAttr):
return False
return True

# 拷贝Realflow缓存的模块
def myCopy_rfCacheModel(self, myType, mtAttr):
tmpCopyFlag = True
try:
allRfNodes = mc.ls(type=myType)
except:
pass
else:
copyData = {}
setData = {}
type_file = 'cache'
type_data = 'realflowCache'
serFileName = os.path.join(self.serveProject, type_file, type_data)
if allRfNodes:
    for RfNode in allRfNodes:
        myFileFullpath = mc.getAttr('%s.%s' % (RfNode, mtAttr))
        if myFileFullpath:
            myFileFullpath = self.myChangeNetPath(myFileFullpath)
            if myType == 'RealflowEmitter':
                rfbaseName = 'particles'
                myFilepath = myFileFullpath
                myFilePreName = mc.getAttr('%s.Prefixes[0]' % RfNode)
                myFinalName = os.path.join(serFileName, rfbaseName)
                myFinalSName = myFinalName
            else:
                rfbaseName = 'meshes'
                myFilepath = os.path.dirname(myFileFullpath)
                myFileBasePath = os.path.basename(myFileFullpath)
                FramePadding = mc.getAttr('%s.framePadding' % RfNode)
                myFileBasePathText = os.path.splitext(myFileBasePath)[0]
                myFilePreName = myFileBasePathText[:-FramePadding]
                myFinalName = os.path.join(serFileName, rfbaseName)
                myFinalSName = os.path.join(myFinalName, myFileBasePath)
            # 获取文件名
            myFinalName = os.path.normpath(myFinalName)
            myFinalSName = os.path.normpath(myFinalSName)
            myFilepath = os.path.normpath(myFilepath)
            # 网络盘存在标帜
            tmpSerPathFlag = os.path.isdir(myFinalName)
            if os.path.isdir(myFilepath):
                if myFilepath != myFinalName:
                    # 整体文件夹拷贝
                    copyData.update({myFilepath: myFinalName})
                    setData.update({RfNode: myFinalSName})
    if copyData:
        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData),
                          status=u"正在拷贝相应的 %s 文件!" % myType)
        # 拷贝文件
        if not self.CopyDataJob(copyData, True):
            return False
    for key in setData.keys():
        mc.setAttr('%s.%s' % (key, mtAttr), setData[key], type='string')
return True

# 拷贝Realflow的particles粒子和Meshs缓存
def myCopy_rfCache(self):
# 拷贝particles缓存
rfParType = 'RealflowEmitter'
rfParAttr = 'Paths[0]'
if not self.myCopy_rfCacheModel(rfParType, rfParAttr):
return False
# 拷贝meshs缓存
rfMeshType = 'RealflowMesh'
rfMeshAttr = 'Path'
if not self.myCopy_rfCacheModel(rfMeshType, rfMeshAttr):
return False
return True

# 保存文件
def mySaveFile(self):
# try:
#    mc.deleteUI("hyperShadePanel1Window")
# except:
#    pass
# mm.eval('setNamedPanelLayout "Single Perspective View"; updateToolbox();')
# myactivePlane = ''
# i = 1
# while(i):
#     try:
#         tmp = mc.modelEditor('modelPanel%d' % i, q=True, av=True)
#     except:
#         pass
#     else:
#         if tmp:
#             myactivePlane = 'modelPanel%d' % i
#             break
#     i += 1
# if myactivePlane:
#     mc.modelEditor(myactivePlane, e=True, da='boundingBox')
driveFlag = False
myDrives = ['D:', 'E:', 'C:']
type_file = 'scenes'
myFileFullpath = mc.file(q=True, sn=True)
fileSize = os.path.getsize(myFileFullpath)
for drive in myDrives:
freeSV = mm.eval('strip(system("wmic LogicalDisk where Caption=\'%s\' get FreeSpace /value"))' % drive)
freeMV = re.sub("\D", "", freeSV)
if freeMV:
    freeLV = long(freeMV)
    if freeLV > fileSize:
        driveFlag = True
        break
if driveFlag:
localTempPath = r'%s\octvTemp' % drive
if not os.path.isdir(localTempPath):
    os.mkdir(localTempPath)
locaoFileName = os.path.join(localTempPath, self.fileSName)
myTyprName = 'mayaBinary'
if self.fileSName.lower().find('mb') >= 0:
    myTyprName = 'mayaBinary'
else:
    myTyprName = 'mayaAscii'
serFileName = os.path.join(self.serveProject, type_file)
fileserName = os.path.join(serFileName, self.fileSName)
# 判断是否有用Vray渲染器和是否是渲染动画帧
VrayFlag = False
VrayAnimationFlag = False
ChangeFlag = False
if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
    if mc.objExists('vraySettings'):
        VrayFlag = True
        VrayAnimationFlag = mc.getAttr("defaultRenderGlobals.animation")
if VrayFlag and VrayAnimationFlag:
    try:
        mc.setAttr("defaultRenderGlobals.animation", False)
    except:
        pass
    else:
        ChangeFlag = True
        time.sleep(1)
if not self.worker1.myLocalFlag or self.copyType == 5:
    mc.file(rename=locaoFileName)
    mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
    time.sleep(1)
    copyData = {locaoFileName: serFileName}
    self.CopyDataJob(copyData, True)
    # myProjectAddress = self.serveProject.replace('\\', '/')
    # mm.eval('setProject "%s"' % myProjectAddress)
    if self.copyType != 5:
        os.remove(locaoFileName)
else:
    print fileserName
    mc.file(rename=fileserName)
    mc.file(force=True, save=True, options='v=1;p=17', type=myTyprName)
    time.sleep(1)
if self.copyType == 1 or self.copyType == 5:
    myProjectAddress = self.serveProject.replace('\\', '/')
    mm.eval('setProject "%s"' % myProjectAddress)
if ChangeFlag:
    try:
        mc.setAttr("defaultRenderGlobals.animation", True)
    except:
        pass
return fileserName
else:
mc.confirmDialog(title=u'温馨提示：', message=u'本地盘符不够空间来临时存储文件！\n请清理空间', button=['OK'], defaultButton='Yes',
                 dismissString='No')
return False

def delDefaultRenderLayer(self):
layers = mc.ls(exactType='renderLayer')
count = 0
pattern = re.compile('^[a-zA-Z0-9_\:-]*defaultRenderLayer$')
for eachLayer in layers:
if pattern.match(eachLayer):
    if not eachLayer == 'defaultRenderLayer':
        try:
            mc.delete(eachLayer)
        except:
            om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
        else:
            count += 1
del pattern

resolutions = mc.ls(exactType='resolution')
count = 0
patternS = re.compile('^[a-zA-Z0-9_\:-]*defaultResolution$')
for each in resolutions:
if patternS.match(each):
    if not each == 'defaultResolution':
        try:
            mc.delete(each)
        except:
            om.MGlobal.displayWarning(u'注意...%s节点无法删除.')
        else:
            count += 1
del patternS

allmylayers = mc.listConnections("renderLayerManager.renderLayerId")
for layer in layers:
if not layer in allmylayers:
    try:
        mc.delete(layer)
    except:
        pass
    else:
        count += 1
om.MGlobal.displayInfo(u'一共清除了%d 个defaultRenderLayer' % count)

def writeInfo(self):
# 输出job_info文件：
#       Plugin
#       Name
#       Frames
#       OutputDirectory0
#       如果界面的Frames里为空的话，这里的Frames会读取渲染设置
# 输出plugin_info文件：
#       SceneFile
#       Renderer
#       UsingRenderLayers
#       RenderLayer
#       ImageWidth
#       ImageHeight
#       AspectRatio
#       ProjectPath
#       OutputFilePath
#       OutputFilePrefix
#       如果没有渲染层的话，Renderer设为File， UsingRenderLayers/RenderLayer/ImageWidth/ImageHeight/AspectRatio可以不写
layers = mc.ls(exactType='renderLayer')
pattern = re.compile('^defaultRenderLayer')
for eachLayer in layers:
if pattern.match(eachLayer):
    if not eachLayer == 'defaultRenderLayer':
        try:
            mc.select(eachLayer, r=True)
            mc.lockNode(l=False)
            mc.delete(eachLayer)
        except:
            self.stateMsg += u'注意,%s节点无法删除.\n'
            om.MGlobal.displayWarning(u'注意,%s节点无法删除.\n')
del pattern

imgFormat = {23: 'avi', 11: 'cin', 35: 'dds', 9: 'eps', 0: 'gif', 8: 'jpg', 7: 'iff', 10: 'iff', 31: 'psd',
         36: 'psd', 32: 'png', 12: 'yuv', 2: 'rla', 5: 'sgi', 13: 'sgi', 1: 'pic', 19: 'tga', 3: 'tif',
         4: 'tif', 20: 'bmp', \
         2: 'rla', 5: 'rgb', 51: 'tif', 6: 'als'}
getTempFolderScriptFile = r'\\192.168.5.38\td\APP\RenderFarm\getDeadlineTemp.py'
p = os.popen(r'deadlinecommand -executescript %s' % getTempFolderScriptFile, 'r')
tempFolder = p.read()
p.close()
del p
tempFolder = tempFolder[:-1]
key = ['Version', 'Build', 'Name', 'StartFrames', 'EndFrames', 'FrameStep', 'OutputDirectories0', 'SceneFile',
   'Renderer', 'RenderLayer', 'ImageWidth',
   'ImageHeight', 'AspectRatio', 'ProjectPath', 'OutputFilePath', 'OutputFilePrefix', 'RenderableLayers']

renderGlobal = mc.ls(et='renderGlobals')
resolution = mc.ls(et='resolution')
if len(renderGlobal) > 1:
self.stateMsg += u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n'
om.MGlobal.displayError(u'有多于一个RenderGlobals节点,请检查场景删除多余的节点.\n')
return

if not len(resolution) == 1 and len(resolution) > 0:
self.stateMsg += u'有多于一个Resolution节点,请检查场景删除多余的节点.\n'
om.MGlobal.displayError(u'有多于一个Resolution节点,请检查场景删除多余的节点.\n')
return

# filePrefixName = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
fileNameWithExt = mc.file(q=True, sn=True, shn=True)
fileName = [os.path.splitext(fileNameWithExt)[0]]
hostFile = ['%s\\scenes\\%s' % (self.serveProject, fileNameWithExt)]
outputDir = [self.serveImages]
projPath = [self.serveProject]
version = [mc.about(version=True)]
build = ['32bit']
allCam = mc.ls(et='camera')

if mc.about(is64=True):
build[0] = '64bit'

allLayer = []
renderable = []

currentLayer = mc.editRenderLayerGlobals(q=True, currentRenderLayer=True)
if len(layers):
for eachLayer in layers:
    if 'defaultRenderLayer' == eachLayer:
        mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)
        # continue
    allLayer.append(eachLayer)

renCam = []
renderer = []
filePrefix = []
# resolveName = []
format = []
startFrame = []
endFrame = []
frameStep = []
width = []
height = []
ratio = []

if len(allLayer):
for eachLayer in allLayer:
    mc.editRenderLayerGlobals(currentRenderLayer=eachLayer)

    if mc.getAttr('%s.renderable' % eachLayer):
        renderable.append(eachLayer)

    for eachCam in allCam:
        if mc.getAttr('%s.renderable' % eachCam):
            renCam.append(eachCam)

    if not len(renCam):
        # om.MGlobal.displayError(u'%s渲染层没有渲染摄像机,终止操作.' % eachLayer)
        pass
    currentRenderName = mc.getAttr('%s.currentRenderer' % renderGlobal[0])
    renderer.append(currentRenderName.capitalize())
    if currentRenderName.find('vray') >= 0:
        prefix = mc.getAttr('vraySettings.fileNamePrefix')
        frameStep.append(int(mc.getAttr('vraySettings.fileNamePadding')))
    else:
        prefix = mc.getAttr('%s.imageFilePrefix' % renderGlobal[0])
        frameStep.append(int(mc.getAttr('defaultRenderGlobals.byFrameStep')))
    filePrefix.append(prefix)
    # prefix = prefix.replace(u'<Scene>', fileName[0])
    # prefix = prefix.replace(u'<RenderLayer>', eachLayer)
    # prefix = prefix.replace(u'<Camera>', renCam[0])
    # resolveName.append(prefix)

    formatIndex = mc.getAttr('%s.imageFormat' % renderGlobal[0])
    format.append(imgFormat[formatIndex])
    startFrame.append(int(mc.getAttr('%s.startFrame' % renderGlobal[0])))
    endFrame.append(int(mc.getAttr('%s.endFrame' % renderGlobal[0])))
    width.append(mc.getAttr('%s.width' % resolution[0]))
    height.append(mc.getAttr('%s.height' % resolution[0]))
    ratio.append(mc.getAttr('%s.deviceAspectRatio' % resolution[0]))

all = []
all.append(version)
all.append(build)
all.append(fileName)
all.append(startFrame)
all.append(endFrame)
all.append(frameStep)
all.append(outputDir)
all.append(hostFile)
all.append(renderer)
all.append(allLayer)
all.append(width)
all.append(height)
all.append(ratio)
all.append(projPath)
all.append(outputDir)
all.append(filePrefix)
all.append(renderable)

mc.editRenderLayerGlobals(currentRenderLayer=currentLayer)

writeStr = ''
for i in range(len(key)):
writeStr += '[%s]\n' % key[i]
for eachItem in all[i]:
    writeStr += '%s\n' % eachItem
writeStr += '[/%s]\n\n' % key[i]

fPath = os.path.join(tempFolder, 'fileSettings.cfg')
f = file(fPath, 'w')
try:
f.writelines(writeStr)
except:
self.stateMsg += u'%s写入信息时出错,终止操作.\n' % fPath
om.MGlobal.displayError(u'%s写入信息时出错,终止操作.\n' % fPath)
else:
f.close()
self.stateMsg += u'成功写入信息文件.\n'
om.MGlobal.displayInfo(u'成功写入信息文件.\n')
del all[:]
del fileName[:]
del startFrame[:]
del endFrame[:]
del outputDir[:]
del hostFile[:]
del renderer[:]
del allLayer[:]
del width[:]
del height[:]
del ratio[:]
del projPath[:]
del filePrefix[:]
del renderable[:]
del writeStr

def executeScript(self):
try:
str = os.popen(
    r'"deadlinecommand.exe" -ExecuteScript \\octvision.com\cg\td\APP\RenderFarm\MayaSubmission.py').read()
except:
pass
else:
sys.stdout.write(str)

def changeMrLayer(self):
if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
if not mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
    allLayers = mc.listConnections('renderLayerManager.renderLayerId')
    if allLayers:
        for Layer in allLayers:
            if mc.getAttr('%s.renderable' % Layer):
                mc.editRenderLayerGlobals(currentRenderLayer=Layer)
                if mc.getAttr('defaultRenderGlobals.currentRenderer') == 'mentalRay':
                    break

def Cancelsimulation(self):
# 关闭布料和毛发动力解算
try:
AllNucleus = mc.ls(type='nucleus')
except:
pass
else:
if AllNucleus:
    for eachNucleu in AllNucleus:
        try:
            mc.setAttr('%s.enable' % eachNucleu, 0)
        except:
            pass
# Yeti毛发缓存
try:
AllYetiCahces = mc.ls(type='pgYetiGroom')
except:
pass
else:
if AllYetiCahces:
    for eachYetiCahce in AllYetiCahces:
        try:
            mc.setAttr('%s.doSimulation' % eachYetiCahce, 0)
        except:
            pass

def main(self, *args):
copyType = args[0]
self.ArnoldFlag = False
if len(args) > 1:
if args[1]:
    self.myUseRender = args[1]
    if len(self.myUseRender[2]) > 0:
        self.ArnoldFlag = True
'''
copyType分三种模式
1 单纯拷贝模式
2 拷贝提交模式
3 单纯提交模式
'''
self.copyType = copyType
# 创建素材输入文件夹
if copyType == 2 or copyType == 3:
self.serveImages = self.myCreateImagesFolder()
# 设置deep层输出的路径
elif copyType == 4:
self.serveImages = self.myCreateDeepImagesFolder()

# 当模式为1和2时工程目录，3时为读取当前工程目录
if copyType == 1 or copyType == 2 or copyType == 4 or copyType == 5:
self.serveProject = self.myCreateScenes()
elif copyType == 3:
self.serveProject = mc.workspace(q=True, rd=True)
myFileFullName = mc.file(q=True, sn=True)
if self.serveProject.find('z:') >= 0:
self.serveProject = self.serveProject.replace('z:', OCT_DRIVE)
elif self.serveProject.find('Z:') >= 0:
self.serveProject = self.serveProject.replace('Z:', OCT_DRIVE)

# 检查当前工程是否有读写权限
checkAccessFile = os.path.join(self.serveProject, 'myTest_TD')
try:
os.makedirs(checkAccessFile)
except:
pass
try:
os.removedirs(checkAccessFile)
except:
self.worker1.myLocalFlag = False
self.worker2.myLocalFlag = False
else:
self.worker1.myLocalFlag = True
self.worker2.myLocalFlag = True

# 去掉检查参考
# if copyType == 2 or copyType == 3 or copyType == 4:
#     if mc.file(q=True, reference=True):
#         om.MGlobal.displayInfo(u'文件含有参考，请导入后再继续！\n')
#         mc.confirmDialog(title=u'温馨提示：', message=u'文件含有参考，请导入后再继续！', button=['OK'], defaultButton='Yes', dismissString='No')
#         return False

if (copyType == 2 or copyType == 4) and self.ArnoldFlag:
if mc.objExists("defaultArnoldRenderOptions"):
    mc.setAttr("defaultArnoldRenderOptions.use_existing_tiled_textures", 1)
    mc.setAttr("defaultArnoldRenderOptions.absoluteTexturePaths", 0)
    mc.setAttr("defaultArnoldRenderOptions.absoluteProceduralPaths", 1)
    mc.setAttr("defaultArnoldRenderOptions.textureMaxOpenFiles", 200)
    # mc.setAttr("defaultArnoldRenderOptions.absoluteProceduralPaths", 0)
    myArnoldLocalPath = mc.getAttr("defaultArnoldRenderOptions.texture_searchpath")
    # myArnoldProxyPath = mc.getAttr("defaultArnoldRenderOptions.procedural_searchpath")
    if myArnoldLocalPath:
        if myArnoldLocalPath[-1] != ';':
            mc.setAttr("defaultArnoldRenderOptions.texture_searchpath",
                       myArnoldLocalPath + ';' + self.serveProject + '\\sourceimages;', type="string")
        else:
            mc.setAttr("defaultArnoldRenderOptions.texture_searchpath",
                       myArnoldLocalPath + self.serveProject + '\\sourceimages;', type="string")
    else:
        mc.setAttr("defaultArnoldRenderOptions.texture_searchpath", self.serveProject + '\\sourceimages;',
                   type="string")
    # if myArnoldProxyPath:
    #     if myArnoldProxyPath[-1] != ';':
    #          mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", myArnoldProxyPath+';'+self.serveProject+'sourceimages;', type="string")
    #     else:
    #         mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", myArnoldProxyPath+self.serveProject+'sourceimages;', type="string")
    # else:
    #     mc.setAttr("defaultArnoldRenderOptions.procedural_searchpath", self.serveProject+'sourceimages;', type="string")
# 运行主程序
if self.serveProject:
mc.progressWindow(title=u'提交文件', status=u'即将开始', isInterruptable=True)
if copyType == 1 or copyType == 2 or copyType == 4 or copyType == 5:
    i = 0
    j = 1
    k = 10
    mrFlag = False
    vrFlag = False
    arFlag = False
    if mc.pluginInfo('Mayatomr.mll', query=True, loaded=True):
        mrFlag = True
        i += 1
    if mc.pluginInfo('vrayformaya.mll', query=True, loaded=True):
        vrFlag = True
        i += 1
    if mc.pluginInfo('mtoa.mll', query=True, loaded=True):
        arFlag = True
        i += 1
    k = k + i
    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 file 贴图文件' % (k, j))
    if self.myCopyType_Files():
        j += 1
        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 cacheFile 缓存文件' % (k, j))
        if self.myCopy_Data():
            j += 1
            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Alembic cacheFile 缓存文件' % (k, j))
            if self.myCopy_AbcData():
                j += 1
                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Shave cacheFile 缓存文件' % (k, j))
                if self.myCopy_Shavedata():
                    j += 1
                    mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 particle 缓存文件' % (k, j))
                    if self.myCopy_Particles():
                        j += 1
                        mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传 Realflow 缓存' % (k, j))
                        if self.myCopy_rfCache():
                            j += 1
                            mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传Yeti毛发缓存' % (k, j))
                            if self.myCopy_YetiCache():
                                j += 1
                                mc.progressWindow(edit=True, title=u'共%s步, 第 %s 步,正在上传摄像机投影贴图' % (k, j))
                                if self.myCopy_OtherImages():
                                    if mrFlag:
                                        j += 1
                                        mc.progressWindow(edit=True,
                                                          title=u'共%s步, 第 %s 步,正在上传Mr渲染器的相关文件' % (k, j))
                                        if not self.myCopy_Mr():
                                            mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！',
                                                             button=[u'确认'], icn='critical',
                                                             defaultButton='ok', dismissString='No')
                                            mc.progressWindow(endProgress=True)
                                            return False
                                    if vrFlag:
                                        j += 1
                                        mc.progressWindow(edit=True,
                                                          title=u'共%s步, 第 %s 步,正在上传Vr渲染器的相关文件' % (k, j))
                                        if not self.myCopy_Vr():
                                            mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！',
                                                             button=[u'确认'], icn='critical',
                                                             defaultButton='ok', dismissString='No')
                                            mc.progressWindow(endProgress=True)
                                            return False
                                    if arFlag:
                                        j += 1
                                        mc.progressWindow(edit=True,
                                                          title=u'共%s步, 第 %s 步,正在上传Ar渲染器的相关文件' % (k, j))
                                        if not self.myCopy_Ar():
                                            mc.confirmDialog(title=u'警告：', message=u'上传文件被中断！',
                                                             button=[u'确认'], icn='critical',
                                                             defaultButton='ok', dismissString='No')
                                            mc.progressWindow(endProgress=True)
                                            return False
                                    j += 1
                                    mc.progressWindow(edit=True, progress=1, min=0, max=1,
                                                      status=u"正在保存文件!",
                                                      title=u'共%s步, 第 %s 步,正在保存文件' % (k, j))
                                    self.delDefaultRenderLayer()
                                    self.Cancelsimulation()
                                    myFileFullName = self.mySaveFile()
                                    if myFileFullName:
                                        mm.eval('autoUpdateAttrEd;')
                                        om.MGlobal.displayWarning(u'\n文件上传成功！')
                                        j += 1
                                        mc.progressWindow(edit=True, status=u'上传完毕!',
                                                          title=u'共%s步, 第 %s 步,上传完毕！' % (k, j))
if copyType == 2 or copyType == 3 or copyType == 4:
    if copyType == 3:
        self.delDefaultRenderLayer()
    self.changeMrLayer()
    myfileBaseName = os.path.splitext(self.fileSName)[0]
    mm.eval(r'global string $myFileName = "%s"' % myfileBaseName)
    mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
    mm.eval(r'global string $myDeadlineImagesPath = "%s"' % self.serveImages.replace('\\', '/'))
    mm.eval(r'global string $myDeadlineSceneFile = "%s"' % myFileFullName.replace('\\', '/'))
    mm.eval(r'global string $myDeadlineProjectPath= "%s"' % self.serveProject.replace('\\', '/'))
    mm.eval('source "SubmitMayaToDeadline_zwz";')
    mm.eval('SubmitMayaToDeadline_zwz')
    if mc.radioButtonGrp('AutoSubmit', q=True, sl=True) == 1:
        mm.eval('evalDeferred "SetupSubmission()"')
    # self.writeInfo()
    # self.executeScript()
mc.progressWindow(endProgress=True)
return True


#创建相应场景
def myCreateScenes(self):
fileSN = self.fileSName.split('_')
while '' in fileSN:
    fileSN.remove('')
ProjectName = '_'.join(fileSN[:3])
if self.copyType == 2 or self.copyType == 4:
    serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSN[0], fileSN[1], fileSN[2], USERNAME, ProjectName)
elif self.copyType == 1:
    result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel', ds='Cancel')
    if result == 'OK':
        myPath = mc.promptDialog(q=True, t=True)
        if myPath[:2] == "z:":
            myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
        elif myPath[:2] == "Z:":
            myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
        if os.path.isdir(myPath):
            myPath = os.path.normpath(myPath)
            myLastPath = myPath.split("\\")[-1]
            myProjectName = os.path.splitext(self.fileSName)[0]
            if myLastPath.lower() == "work":
                ErrorFlag = True
                if len(fileSN) >= 3:
                    #判断服务器是否存在该工程
                    serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation', fileSN[1], fileSN[2])
                    if os.path.isdir(serFilePath):
                        ErrorFlag = False
                        serveProject = os.path.join(myPath, fileSN[0], ProjectName)
                if ErrorFlag:
                    fileResult = mc.confirmDialog(title=u'温馨提示', message=u'服务器找不到相应的工程目录!\n是否直接在输入路径下按照文件名创建项目?', button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
                    if fileResult == 'Yes':
                        serveProject = os.path.join(myPath, myProjectName)
                    else:
                        return False
            else:
                serveProject = os.path.join(myPath, myProjectName)
        else:
            mc.confirmDialog(m=u'无效路径，请重新输入')
            return False
    else:
        return False

elif self.copyType == 5:
    myPath = r"\\file2.nas\share\ALL\transfer"
    #myPath = r"E:\b"
    if myPath[:2] == "z:":
        myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
    elif myPath[:2] == "Z:":
        myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
    if os.path.isdir(myPath):
        serveProject = os.path.join(myPath, fileSN[0], fileSN[1], fileSN[2])
    else:
        mc.confirmDialog(m=u'%s无效路径，请检查网络！'%myPath)
        return False

    self.worker1.myLocalFlag = True
    self.worker2.myLocalFlag = True

if not os.path.isdir(serveProject):
    self.myCreateFolder(serveProject)
    exampleProject = os.path.join(r"\\octvision.com\cg\Tech", NEWPROJECT_NAME)
    copyData = {exampleProject: serveProject}
    self.CopyDataJob(copyData, True)
return serveProject

def myCreateImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1], fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
    self.myCreateFolder(serveProject)
return serveProject

#创建deep输出素材的路径
def myCreateDeepImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(r"\\file.com\share\VFX\Images", fileSNameSplit[0], r'Deep', fileSNameSplit[1], fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
    self.myCreateDeepFolder(serveProject)
return serveProject

def myChangeNetPath(self, TempPath):
if TempPath.find('${OCTV_PROJECTS}') >= 0:
    TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
elif TempPath.find('z:') >= 0:
    TempPath = TempPath.replace('z:', OCT_DRIVE)
elif TempPath.find('Z:') >= 0:
    TempPath = TempPath.replace('Z:', OCT_DRIVE)
elif TempPath.find('w:') >= 0:
    TempPath = TempPath.replace('w:', OCT_FilePath)
elif TempPath.find('W:') >= 0:
    TempPath = TempPath.replace('W:', OCT_FilePath)
elif TempPath.find('M:') >= 0:
    TempPath = TempPath.replace('M:', OCT_MDRIVE)
elif TempPath.find('m:') >= 0:
    TempPath = TempPath.replace('m:', OCT_MDRIVE)
return TempPath

def myJudeArnoldTxFile(self, texFileName):
PathSplitT = os.path.splitext(texFileName)
if len(PathSplitT) > 1:
    LowerPathType = PathSplitT[1].lower()
    if (LowerPathType != '.hdr') or (LowerPathType != '.tx'):
        ArnoldTxFileName = PathSplitT[0]+'.tx'
        if os.path.isfile(ArnoldTxFileName):
            return texFileName
    else:
        return ArnoldTxFileName
return False

#拷贝所有file节点的文件并改变节点
def myCopyType_Files(self):
tmpCopyFlag = True
#判断是否有使用Arnold层
type_file = 'sourceimages'
serFileName = os.path.join(self.serveProject, type_file)
allfiles = mc.ls(type='file')
copyData = {}
setData = {}
if allfiles:
    for eachfile in allfiles:
        texFileNameGroup = []
        try:
            texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
        except:
            pass
        else:
            texFirstFileName = self.myChangeNetPath(texFirstFileName)
            #判断贴图是否开启了序列帧模式
            #序列标识：
            UseSeqFlag = mc.getAttr('%s.useFrameExtension' % eachfile)

            #获取选择uvTilingMode的模式
            UvSeqFlag = mc.getAttr('%s.uvTilingMode' % eachfile)

            if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                #当存在Arnold渲染器时
                if self.ArnoldFlag:
                    #当仅仅是复制模式时，需要把普通贴图也拷贝
                    CopyHdrFlag = False
                    if self.copyType == 1 or self.copyType == 5:
                        texFileNameGroup.append(texFirstFileName)
                        CopyHdrFlag = True
                    PathSplitT = os.path.splitext(texFirstFileName)
                    if len(PathSplitT) > 1:
                        LowerPathType = PathSplitT[1].lower()
                        #当不是hdr贴图时，需要拷贝tx贴图
                        if LowerPathType != '.hdr':
                            ArnoldTxFileName = PathSplitT[0]+'.tx'
                            if os.path.isfile(ArnoldTxFileName):
                                texFileNameGroup.append(ArnoldTxFileName)
                        else:
                            if not CopyHdrFlag:
                                texFileNameGroup.append(texFirstFileName)
                else:
                    texFileNameGroup.append(texFirstFileName)
            #当开启了序列时
            elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2 :
                myTexDirName = os.path.dirname(texFirstFileName)
                myTexBaseName = os.path.basename(texFirstFileName)
                myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
                myAllFileName = os.listdir(myTexDirName)
                for eachDirFileName in myAllFileName:
                    if eachDirFileName.find(myTexFileTopName) >= 0:
                        IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                        #当存在Arnold渲染器时
                        if self.ArnoldFlag:
                            #当仅仅是复制模式时，需要把普通贴图也拷贝
                            CopyHdrFlag = False
                            if self.copyType == 1 or self.copyType == 5:
                                texFileNameGroup.append(IndexTexName)
                                CopyHdrFlag = True
                            IndexPathSplitT = os.path.splitext(IndexTexName)
                            if len(IndexPathSplitT) > 1:
                                IndexLowerPathType = IndexPathSplitT[1].lower()
                                #当不是hdr贴图时，需要拷贝tx贴图
                                if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                    IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                    if os.path.isfile(IndexArnoldTxFileName):
                                        texFileNameGroup.append(IndexArnoldTxFileName)
                                else:
                                    if not CopyHdrFlag:
                                        texFileNameGroup.append(IndexTexName)
                        else:
                            texFileNameGroup.append(IndexTexName)

            elif not UseSeqFlag and (UvSeqFlag == 2 or UvSeqFlag == 3):
                myTexDirName = os.path.dirname(texFirstFileName)
                myTexBaseName = os.path.basename(texFirstFileName)
                myTexFileTopName = myTexBaseName.split('_u')[0]
                if not myTexFileTopName:
                    myTexFileTopName = myTexBaseName.split('_U')[0]
                myTexFileTopNames = re.findall(r'\D+', myTexBaseName)[0]

                myAllFileName = os.listdir(myTexDirName)
                for eachDirFileName in myAllFileName:
                    if eachDirFileName.find(myTexFileTopName) >= 0:
                        IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                        #当存在Arnold渲染器时
                        if self.ArnoldFlag:
                            #当仅仅是复制模式时，需要把普通贴图也拷贝
                            CopyHdrFlag = False
                            if self.copyType == 1 or self.copyType == 5:
                                texFileNameGroup.append(IndexTexName)
                                CopyHdrFlag = True
                            IndexPathSplitT = os.path.splitext(IndexTexName)
                            if len(IndexPathSplitT) > 1:
                                IndexLowerPathType = IndexPathSplitT[1].lower()
                                #当不是hdr贴图时，需要拷贝tx贴图
                                if IndexLowerPathType != '.hdr':
                                    IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                    if os.path.isfile(IndexArnoldTxFileName):
                                        texFileNameGroup.append(IndexArnoldTxFileName)
                                else:
                                    if not CopyHdrFlag:
                                        texFileNameGroup.append(IndexTexName)
                        else:
                            texFileNameGroup.append(IndexTexName)
                    elif eachDirFileName.find(myTexFileTopNames) >= 0:
                        IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                        #当存在Arnold渲染器时
                        if self.ArnoldFlag:
                            #当仅仅是复制模式时，需要把普通贴图也拷贝
                            CopyHdrFlag = False
                            if self.copyType == 1 or self.copyType == 5:
                                texFileNameGroup.append(IndexTexName)
                                CopyHdrFlag = True
                            IndexPathSplitT = os.path.splitext(IndexTexName)
                            if len(IndexPathSplitT) > 1:
                                IndexLowerPathType = IndexPathSplitT[1].lower()
                                #当不是hdr贴图时，需要拷贝tx贴图
                                if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                    IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                    if os.path.isfile(IndexArnoldTxFileName):
                                        texFileNameGroup.append(IndexArnoldTxFileName)
                                else:
                                    if not CopyHdrFlag:
                                        texFileNameGroup.append(IndexTexName)
                        else:
                            texFileNameGroup.append(IndexTexName)

            # print texFileNameGroup
            if texFileNameGroup:
                for texFileName in texFileNameGroup:
                    # print texFileName
                    texFileName = os.path.normpath(texFileName)
                    texFileNameS = texFileName.split('\\')
                    try:
                        indexType = texFileNameS.index(type_file)
                    except:
                        texFileNameBN = os.path.basename(texFileName)
                        serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                        copyFinalTexFilePath = serFileName
                    else:
                        serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
                        serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                        copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                    serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                    copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                    if texFileName != serFinalTexFileName:
                        #加入拷贝字典
                        #设置拷贝标帜
                        tmpCopyFlag = True
                        if os.path.isdir(serFileName):
                            if os.path.isfile(serFinalTexFileName):
                                testMtime = os.path.getmtime(texFileName)
                                tmpMtime = os.path.getmtime(serFinalTexFileName)
                                if int(tmpMtime) >= int(testMtime):
                                    tmpCopyFlag = False
                    else:
                        tmpCopyFlag = False
                    if tmpCopyFlag:
                        copyData.update({texFileName: copyFinalTexFilePath})
                #加入设置字典，只设置第一帧
                if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                    #数组1是Arnold
                    setData.update({eachfile: serFinalTexFileName})
                else:
                    mySetTexDirName = os.path.dirname(serFinalTexFileName)
                    serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
                    serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
                    if self.ArnoldFlag:
                        myFirstFileName = os.path.splitext(myTexBaseName)[0]+ '.tx'
                        #serFinalSetTexFileName = os.path.splitext(serFinalSetTexFileName)[0] + '.tx'
                        serFinalSetTexFileName = os.path.join(mySetTexDirName, myFirstFileName)
                        setData.update({eachfile: serFinalSetTexFileName})
                    else:
                        setData.update({eachfile: serFinalSetTexFileName})
    if copyData:
        mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData)+1, status=u"正在拷贝相应的 file 贴图!")
        #拷贝文件
        if not self.CopyDataJob(copyData, True):
            return False
    #设置路径
    for key in setData.keys():
        mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')

    # #临时拷贝Arnold贴图文件夹
    # if mc.ls(type='aiStandIn'):
    #     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
    #     ArnoldProxyCopyData = {}
    #     if os.path.isdir(myLocalArnoldSourcePath):
    #         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
    #         serArnoldFileName = serFileName + '\\arnoldTex'
    #         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
    #         #拷贝文件
    #         if not self.CopyDataJob(ArnoldProxyCopyData, True):
    #             return False
return True






























#创建文件夹命令
def myCreateFolder(self, address):
try:
os.makedirs(address)
except:
cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (self.CpauLocalPath, REMOTE_USER, REMOTE_PWD, address)
p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
while True:
    if not p.poll() is None:
        del p
        break
    else:
        time.sleep(0.001)
time.sleep(0.1)

# 创建在W盘渲染deep的文件夹
def myCreateDeepFolder(self, address):
try:
    os.makedirs(address)
except:
    print address
    cmd = r'%s -u %s -p %s -hide -wait -c -nowarn -ex "md %s"' % (
    self.CpauLocalPath, r'octvision\rd', r'rd1234', address)
    print cmd
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    while True:
        if not p.poll() is None:
            del p
            break
        else:
            time.sleep(0.001)
time.sleep(0.1)

# 创建相应场景
def myCreateScenes(self):
fileSN = self.fileSName.split('_')
while '' in fileSN:
    fileSN.remove('')
ProjectName = '_'.join(fileSN[:3])
if self.copyType == 2 or self.copyType == 4:
    serveProject = os.path.join(SERVE_PATH, MAYAFOLDER_NAME, fileSN[0], fileSN[1], fileSN[2], USERNAME,
                                ProjectName)
elif self.copyType == 1:
    result = mc.promptDialog(t=u"拷贝整个工程目录", m=u'请输入路径', b=['OK', 'Cancel'], db='OK', cb='Cancel',
                             ds='Cancel')
    if result == 'OK':
        myPath = mc.promptDialog(q=True, t=True)
        if myPath[:2] == "z:":
            myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
        elif myPath[:2] == "Z:":
            myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
        if os.path.isdir(myPath):
            myPath = os.path.normpath(myPath)
            myLastPath = myPath.split("\\")[-1]
            myProjectName = os.path.splitext(self.fileSName)[0]
            if myLastPath.lower() == "work":
                ErrorFlag = True
                if len(fileSN) >= 3:
                    # 判断服务器是否存在该工程
                    serFilePath = os.path.join(PROJECT_PATH, fileSN[0], r'Project\scenes\animation',
                                               fileSN[1], fileSN[2])
                    if os.path.isdir(serFilePath):
                        ErrorFlag = False
                        serveProject = os.path.join(myPath, fileSN[0], ProjectName)
                if ErrorFlag:
                    fileResult = mc.confirmDialog(title=u'温馨提示',
                                                  message=u'服务器找不到相应的工程目录!\n是否直接在输入路径下按照文件名创建项目?',
                                                  button=['Yes', 'No'], defaultButton='Yes',
                                                  cancelButton='No', dismissString='No')
                    if fileResult == 'Yes':
                        serveProject = os.path.join(myPath, myProjectName)
                    else:
                        return False
            else:
                serveProject = os.path.join(myPath, myProjectName)
        else:
            mc.confirmDialog(m=u'无效路径，请重新输入')
            return False
    else:
        return False

elif self.copyType == 5:
    myPath = r"\\file2.nas\share\ALL\transfer"
    # myPath = r"E:\b"
    if myPath[:2] == "z:":
        myPath = myPath.replace('z:', '\\\\octvision.com\\cg')
    elif myPath[:2] == "Z:":
        myPath = myPath.replace('Z:', '\\\\octvision.com\\cg')
    if os.path.isdir(myPath):
        serveProject = os.path.join(myPath, fileSN[0], fileSN[1], fileSN[2])
    else:
        mc.confirmDialog(m=u'%s无效路径，请检查网络！' % myPath)
        return False

    self.worker1.myLocalFlag = True
    self.worker2.myLocalFlag = True

if not os.path.isdir(serveProject):
    self.myCreateFolder(serveProject)
    exampleProject = os.path.join(r"\\octvision.com\cg\Tech", NEWPROJECT_NAME)
    copyData = {exampleProject: serveProject}
    self.CopyDataJob(copyData, True)
return serveProject

def myCreateImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(SERVE_PATH, IMAGESFLODER_NAME, fileSNameSplit[0], fileSNameSplit[1],
                            fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
    self.myCreateFolder(serveProject)
return serveProject

#创建deep输出素材的路径
def myCreateDeepImagesFolder(self):
fileSNameSplit = self.fileSName.split('_')
# ProjectName = os.path.splitext(self.fileSName)[0]
serveProject = os.path.join(r"\\file.com\share\VFX\Images", fileSNameSplit[0], r'Deep', fileSNameSplit[1], fileSNameSplit[2], USERNAME)
if not os.path.isdir(serveProject):
self.myCreateDeepFolder(serveProject)
return serveProject

def myChangeNetPath(self, TempPath):
if TempPath.find('${OCTV_PROJECTS}') >= 0:
TempPath = TempPath.replace('${OCTV_PROJECTS}', PROJECT_PATH)
elif TempPath.find('z:') >= 0:
TempPath = TempPath.replace('z:', OCT_DRIVE)
elif TempPath.find('Z:') >= 0:
TempPath = TempPath.replace('Z:', OCT_DRIVE)
elif TempPath.find('w:') >= 0:
TempPath = TempPath.replace('w:', OCT_FilePath)
elif TempPath.find('W:') >= 0:
TempPath = TempPath.replace('W:', OCT_FilePath)
elif TempPath.find('M:') >= 0:
TempPath = TempPath.replace('M:', OCT_MDRIVE)
elif TempPath.find('m:') >= 0:
TempPath = TempPath.replace('m:', OCT_MDRIVE)
return TempPath

def myJudeArnoldTxFile(self, texFileName):
PathSplitT = os.path.splitext(texFileName)
if len(PathSplitT) > 1:
LowerPathType = PathSplitT[1].lower()
if (LowerPathType != '.hdr') or (LowerPathType != '.tx'):
    ArnoldTxFileName = PathSplitT[0]+'.tx'
    if os.path.isfile(ArnoldTxFileName):
        return texFileName
else:
    return ArnoldTxFileName
return False

#拷贝所有file节点的文件并改变节点
def myCopyType_Files(self):
tmpCopyFlag = True
#判断是否有使用Arnold层
type_file = 'sourceimages'
serFileName = os.path.join(self.serveProject, type_file)
allfiles = mc.ls(type='file')
copyData = {}
setData = {}
if allfiles:
for eachfile in allfiles:
    texFileNameGroup = []
    try:
        texFirstFileName = mc.getAttr('%s.fileTextureName' % eachfile)
    except:
        pass
    else:
        texFirstFileName = self.myChangeNetPath(texFirstFileName)
        #判断贴图是否开启了序列帧模式
        #序列标识：
        UseSeqFlag = mc.getAttr('%s.useFrameExtension' % eachfile)

        #获取选择uvTilingMode的模式
        UvSeqFlag = mc.getAttr('%s.uvTilingMode' % eachfile)

        if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
            #当存在Arnold渲染器时
            if self.ArnoldFlag:
                #当仅仅是复制模式时，需要把普通贴图也拷贝
                CopyHdrFlag = False
                if self.copyType == 1 or self.copyType == 5:
                    texFileNameGroup.append(texFirstFileName)
                    CopyHdrFlag = True
                PathSplitT = os.path.splitext(texFirstFileName)
                if len(PathSplitT) > 1:
                    LowerPathType = PathSplitT[1].lower()
                    #当不是hdr贴图时，需要拷贝tx贴图
                    if LowerPathType != '.hdr':
                        ArnoldTxFileName = PathSplitT[0]+'.tx'
                        if os.path.isfile(ArnoldTxFileName):
                            texFileNameGroup.append(ArnoldTxFileName)
                    else:
                        if not CopyHdrFlag:
                            texFileNameGroup.append(texFirstFileName)
            else:
                texFileNameGroup.append(texFirstFileName)
        #当开启了序列时
        elif UseSeqFlag or UvSeqFlag == 3 and UvSeqFlag != 2 :
            myTexDirName = os.path.dirname(texFirstFileName)
            myTexBaseName = os.path.basename(texFirstFileName)
            myTexFileTopName = re.findall(r'\D+', myTexBaseName)[0]
            myAllFileName = os.listdir(myTexDirName)
            for eachDirFileName in myAllFileName:
                if eachDirFileName.find(myTexFileTopName) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    #当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        #当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            #当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)

        elif not UseSeqFlag and (UvSeqFlag == 2 or UvSeqFlag == 3):
            myTexDirName = os.path.dirname(texFirstFileName)
            myTexBaseName = os.path.basename(texFirstFileName)
            myTexFileTopName = myTexBaseName.split('_u')[0]
            if not myTexFileTopName:
                myTexFileTopName = myTexBaseName.split('_U')[0]
            myTexFileTopNames = re.findall(r'\D+', myTexBaseName)[0]

            myAllFileName = os.listdir(myTexDirName)
            for eachDirFileName in myAllFileName:
                if eachDirFileName.find(myTexFileTopName) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    #当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        #当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            #当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr':
                                IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)
                elif eachDirFileName.find(myTexFileTopNames) >= 0:
                    IndexTexName = '/'.join([myTexDirName, eachDirFileName])
                    #当存在Arnold渲染器时
                    if self.ArnoldFlag:
                        #当仅仅是复制模式时，需要把普通贴图也拷贝
                        CopyHdrFlag = False
                        if self.copyType == 1 or self.copyType == 5:
                            texFileNameGroup.append(IndexTexName)
                            CopyHdrFlag = True
                        IndexPathSplitT = os.path.splitext(IndexTexName)
                        if len(IndexPathSplitT) > 1:
                            IndexLowerPathType = IndexPathSplitT[1].lower()
                            #当不是hdr贴图时，需要拷贝tx贴图
                            if IndexLowerPathType != '.hdr' and not UseSeqFlag:
                                IndexArnoldTxFileName = IndexPathSplitT[0]+'.tx'
                                if os.path.isfile(IndexArnoldTxFileName):
                                    texFileNameGroup.append(IndexArnoldTxFileName)
                            else:
                                if not CopyHdrFlag:
                                    texFileNameGroup.append(IndexTexName)
                    else:
                        texFileNameGroup.append(IndexTexName)

        # print texFileNameGroup
        if texFileNameGroup:
            for texFileName in texFileNameGroup:
                # print texFileName
                texFileName = os.path.normpath(texFileName)
                texFileNameS = texFileName.split('\\')
                try:
                    indexType = texFileNameS.index(type_file)
                except:
                    texFileNameBN = os.path.basename(texFileName)
                    serFinalTexFileName = os.path.join(serFileName, texFileNameBN)
                    copyFinalTexFilePath = serFileName
                else:
                    serLastTexFileName = '\\'.join(texFileNameS[indexType+1::])
                    serFinalTexFileName = os.path.join(serFileName, serLastTexFileName)
                    copyFinalTexFilePath = os.path.dirname(serFinalTexFileName)
                serFinalTexFileName = os.path.normpath(serFinalTexFileName)
                copyFinalTexFilePath = os.path.normpath(copyFinalTexFilePath)
                if texFileName != serFinalTexFileName:
                    #加入拷贝字典
                    #设置拷贝标帜
                    tmpCopyFlag = True
                    if os.path.isdir(serFileName):
                        if os.path.isfile(serFinalTexFileName):
                            testMtime = os.path.getmtime(texFileName)
                            tmpMtime = os.path.getmtime(serFinalTexFileName)
                            if int(tmpMtime) >= int(testMtime):
                                tmpCopyFlag = False
                else:
                    tmpCopyFlag = False
                if tmpCopyFlag:
                    copyData.update({texFileName: copyFinalTexFilePath})
            #加入设置字典，只设置第一帧
            if not UseSeqFlag and UvSeqFlag != 2 and UvSeqFlag != 3:
                #数组1是Arnold
                setData.update({eachfile: serFinalTexFileName})
            else:
                mySetTexDirName = os.path.dirname(serFinalTexFileName)
                serFinalSetTexFileName = os.path.join(mySetTexDirName, myTexBaseName)
                serFinalSetTexFileName = os.path.normpath(serFinalSetTexFileName)
                if self.ArnoldFlag:
                    myFirstFileName = os.path.splitext(myTexBaseName)[0]+ '.tx'
                    #serFinalSetTexFileName = os.path.splitext(serFinalSetTexFileName)[0] + '.tx'
                    serFinalSetTexFileName = os.path.join(mySetTexDirName, myFirstFileName)
                    setData.update({eachfile: serFinalSetTexFileName})
                else:
                    setData.update({eachfile: serFinalSetTexFileName})
if copyData:
    mc.progressWindow(edit=True, progress=0, min=0, max=len(copyData)+1, status=u"正在拷贝相应的 file 贴图!")
    #拷贝文件
    if not self.CopyDataJob(copyData, True):
        return False
#设置路径
for key in setData.keys():
    mc.setAttr(u'%s.fileTextureName' % key, setData[key], type='string')

# #临时拷贝Arnold贴图文件夹
# if mc.ls(type='aiStandIn'):
#     myLocalArnoldSourcePath = mc.workspace(en='sourceimages')+'/arnoldTex'
#     ArnoldProxyCopyData = {}
#     if os.path.isdir(myLocalArnoldSourcePath):
#         myLocalArnoldSourcePath = os.path.normpath(myLocalArnoldSourcePath)
#         serArnoldFileName = serFileName + '\\arnoldTex'
#         ArnoldProxyCopyData.update({myLocalArnoldSourcePath: serArnoldFileName})
#         #拷贝文件
#         if not self.CopyDataJob(ArnoldProxyCopyData, True):
#             return False
return True





