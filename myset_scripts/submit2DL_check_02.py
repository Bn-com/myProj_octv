class CopyJobThread(QtCore.QThread):
    # 发射完成比例
    # percent = QtCore.pyqtSignal('int')

    def __init__(self, parent=None):
        super(CopyJobThread, self).__init__(parent)
        self.myLocalFlag = False

    def __del__(self):
        self.wait()

    def ready(self, CpauPath, FcopyPath, source, dest):
        self.myFcopyPath = FcopyPath
        self.myCpauPath = CpauPath
        self.mySourceFile = source
        self.myDestFile = dest
        self.start()

    def run(self):
        if not self.myLocalFlag:
            cmd = r'%s -u %s -p %s -hide -wait -nowarn -ex "%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\""' % (
            self.myCpauPath, REMOTE_USER, REMOTE_PWD, self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break
        else:
            cmd = '%s  /cmd=diff /force_close /error_stop=FALSE /no_confirm_del /force_start=FALSE /bufsize=32 \"%s\" /to=\"%s\"' % (
            self.myFcopyPath, self.mySourceFile, self.myDestFile)
            cmd = str(cmd).encode("gb2312")
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
            while True:
                if not p.poll() is None:
                    del p
                    break

def outPutSets(nodes, name):
    if nodes:
        mc.select(nodes)
        if mc.objExists(name):
            mc.sets(cl=name)
            mc.sets(add=name)
        else:
            mc.sets(n=name)
    else:
        if mc.objExists(name):
            mc.delete(name)
