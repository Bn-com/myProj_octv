# -*- coding: utf-8 -*-
import codecs
import os
import re
import maya.mel as mel

def SubmitSingle4DDZ(sceneName):
    sceneName = sceneName.replace("/", "\\")
    shortName = os.path.basename(sceneName)
    sceneName = ""
    m = re.search(r"^([^\._]+_([^\._]+)_([^\._]+)_[^\._]+_lr)[^\.]+", shortName)
    if not m:
        return False
    jobName = m.group(0)
    pattern = m.group(1)
    episode = m.group(2)
    scene = m.group(3)
    folder = "\\\\file-cluster\\GDC\\Projects\\DouDiZhu\\Project\\scenes\\Animation\\episode_%s\\scene_%s\\lighting" % (episode, scene)
    if not os.path.isdir(folder):
        return False
    files = os.listdir(folder)
    for file in files:
        if re.search("^%s_" % pattern, file, re.IGNORECASE):
            sceneName = os.path.join(folder, file)
    if sceneName == "":
        return False

    parity = "Even"
    COMPUTERNAME = os.getenv("COMPUTERNAME")
    if re.search("[13579]$", COMPUTERNAME):
        parity = "Odd"
    ProjectPath = "\\\\file-cluster\\GDC\\Netrender\\Maya_%s\\%s" % (parity, COMPUTERNAME)

    OutputDirectory = mel.eval("zwGetPath \"ImageOutputDir\" \"%s\"" % sceneName.replace("\\", "/"))
    OutputDirectory = OutputDirectory.replace("/", "\\")
    if not os.path.exists(OutputDirectory):
        os.makedirs(OutputDirectory)

    timeLine = [1001]
    try:
        timeLine = cmds.idmtProject(sceneName, timeLine = True, echo = False)
    except:
        pass

    JobInfo = os.path.join(os.getenv("TEMP"), "JobInfo.txt")
    f = codecs.open(JobInfo, "w", "gbk")
    f.write(u"Name=%s\r\n" % jobName)
    f.write(u"UserName=%s\r\n" % os.getenv("USERNAME"))
    f.write(u"Region=\r\n")
    f.write(u"Frames=%d\r\n" % timeLine[0])
    f.write(u"ChunkSize=10\r\n")
    f.write(u"Pool=maya\r\n")
    f.write(u"Blacklist=\r\n")
    f.write(u"OverrideTaskExtraInfoNames=False\r\n")
    f.write(u"Plugin=MayaBatch\r\n")
    f.write(u"OutputDirectory0=%s\r\n" % OutputDirectory)
    f.write(u"Priority=90\r\n")
    f.write(u"EventOptIns=\r\n")
    f.close()

    PluginInfo = os.path.join(os.getenv("TEMP"), "PluginInfo.txt")
    f = codecs.open(PluginInfo, "w", "gbk")
    f.write(u"Version=2016\r\n")
    f.write(u"Build=None\r\n")
    f.write(u"ProjectPath=%s\r\n" % ProjectPath)
    f.write(u"StrictErrorChecking=True\r\n")
    f.write(u"UseLegacyRenderLayers=0\r\n")
    f.write(u"LocalRendering=False\r\n")
    f.write(u"MaxProcessors=0\r\n")
    f.write(u"FrameNumberOffset=0\r\n")
    f.write(u"OutputFilePath=%s\r\n" % OutputDirectory)
    f.write(u"Renderer=Redshift\r\n")
    f.write(u"RedshiftGPUsPerTask=0\r\n")
    f.write(u"RedshiftGPUsSelectDevices=\r\n")
    f.write(u"StartupScript=\r\n")
    f.write(u"CommandLineOptions=\r\n")
    f.write(u"UseOnlyCommandLineOptions=0\r\n")
    f.write(u"SceneFile=%s\r\n" % sceneName)
    f.write(u"IgnoreError211=False\r\n")
    f.close()

    submission = os.path.join(os.getenv("TEMP"), "submission.txt")
    f = codecs.open(submission, "w", "gbk")
    f.write(u"%s\JobInfo.txt\r\n" % os.getenv("TEMP"))
    f.write(u"%s\PluginInfo.txt\r\n" % os.getenv("TEMP"))
    f.close()

    command = "%s\\CallDeadlineCommand.bat %s %s %s" % (os.path.dirname(__file__), COMPUTERNAME, OutputDirectory, submission)
    result = os.popen(command).read()
    os.remove(JobInfo)
    os.remove(PluginInfo)
    os.remove(submission)
    if re.search(r"JobID=([0-9a-z]{24})", result, re.MULTILINE):
        return True
    return result