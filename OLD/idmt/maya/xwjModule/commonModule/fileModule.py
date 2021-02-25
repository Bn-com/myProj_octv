__author__ = 'xuweijian'
import maya.cmds as mc
import json

class fileModule():
    def writeFile(self,filePath,text):
        try:
            f = open(filePath, "w")
            f.write(text)
            f.flush()
            f.close()
            print "file havs been saved in \"" + filePath + "\"."
        except:
            pass

    def saveFileDialog(self,type='txt'):
        thisWorkspace=mc.workspace(q=1,fn=1)
        senceName=mc.file(q=1,sn=1,shn=1)
        senceName=senceName.split('.')[0]
        storePath=thisWorkspace+'/data/'+senceName+'.txt'
        print storePath
        fileName=mc.fileDialog2(fileFilter='%s (*.%s)'%(type,type), dialogStyle=2,startingDirectory=storePath)[0]
        filePath = fileName
        if fileName.find(".%s"%type) < 0:
            filePath = '%s.%s'%(fileName,type)


        return filePath

    def loadFileDialog(self,type='txt'):
        thisWorkspace=mc.workspace(q=1,fn=1)
        senceName=mc.file(q=1,sn=1,shn=1)
        storePath='%s/data/*.%s'%(thisWorkspace,type)
        filePath = mc.fileDialog(m = 0, dm = storePath)

    def saveJson(self,filePath,dict):
        if filePath.find(".") != 0:
            try:
                f = open(filePath, "w")
                json.dump(dict,f)
                f.flush()
                f.close()
                print "file havs been saved in \"" + filePath + "\"."
            except:
                pass
        else:
            print "Operation has been cancelled."
