__author__ = 'xuweijian'
import maya.cmds as mc
import os
from idmt.maya.commonPerform.projectTools import sk_projTools_mk


class mk_cleanlayout():
    path=''
    parentPath=''
    targetPath=''
    def __init__(self,inputPath):
        #self.path= mc.file(q=1,exn=1)
        self.path=inputPath
        self.name=self.path.split('/')[-1]
        #arr=self.path.split('/')[0:-1]
        #self.parentPath='/'.join(arr)
        self.targetPath='D:/transFiles'
        if not os.path.exists(self.targetPath):
            os.makedirs(self.targetPath)

    def export(self):
        lname='%s/%s'%(self.targetPath,self.name)
        #mc.file(lname,f=1,loadReferenceDepth='all',open=1)
        mc.file(lname,f=1,lnr=1,pmt=0,open=1)
        refs=mc.file(q=1,r=1)
        for ref in refs:
            if not mc.referenceQuery(ref,il=1):
                print 'Getting node -------%s-------'%ref
                rnode= mc.referenceQuery(ref,rfn=1)
                try:
                    mc.file(lr=rnode)
                except:
                    print ('--------------------------------------------------')
                    mc.error('-\n--------------------Can not find reference : %s --------------------\n'%ref)


        root= mc.ls(assemblies=True,rf=1)
        mc.select(root)
        print '------export running-------'
        mc.file(lname,f=1,options='v=0',typ='mayaAscii',pr=1,es=1)
        print ('new file created in %s'%self.targetPath)

    def transMa(self):
        mkT1=sk_projTools_mk.sk_projTools_mk()
        mkT1.transAssetPath(self.path,self.targetPath)





