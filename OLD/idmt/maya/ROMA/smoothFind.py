# -*- coding: gbk -*-
import maya.mel as mel
import maya.cmds as cmds
import os
import time
import getpass

if __name__=='__main__':
    main()

def main():
    UI()



class smoothInfo:
    txtPath='\\\\file-cluster\GDC\Projects\WinxClubII\WinxClubII_Scratch\TD\zzj\SmoothInfo\\'
    sn=cmds.file(q=1,sn=1,shn=1)
    user=getpass.getuser()
    sign='▁▂▃▄▅'+40*'▅'+'▅▄▃▂▁'
#    sign='≥▂≤　　≥０≤　　≥＾≤　　≥ω≤　　≥﹏≤　　≥△≤　　≥▽≤'
#    sign=112*'='


    def currentTime(self):
        times=list(time.localtime())
        ct=''
        for i in range(len(times)-3):
            ct+='.'+str(times[i])
        return ct

    def currentTxtPath(self):
        cp=self.txtPath+self.sn+self.currentTime()+'__'+self.user+'__'+'.txt'
        return cp

    def allSmoothMesh(self):
        rv=[]
#        rv=[u'|.....|MSH_cornea_L_ShapeDeformed', u'polySmoothFace1', u'finalSmooth139']
        allMesh=cmds.ls(ni=1,type='mesh',l=1)
        for mesh in allMesh:
            his=cmds.listHistory(mesh)
            rvTMP=[]
            for h in his:
                if cmds.objectType(h)=='polySmoothFace':
                    rvTMP.append('mesh:')
                    rvTMP.append(mesh)
                    break
            if len(rvTMP)!=0:
                rvTMP.append('smooth:')
            for h in his:
                if cmds.objectType(h)=='polySmoothFace':
                    rvTMP.append(h)
            if len(rvTMP)!=0:
                rv.append(rvTMP)
        return rv

    def smoothHistory(self,mesh):
        rv=[]
        his=cmds.listHistory(mesh,pdo=1)
        for h in his:
            if cmds.objectType(h)=='polySmoothFace':
                rv.append(str(h))
        return rv

    def smoothFace(self,smooth):
        rv=''
        rv=str(cmds.getAttr(str(smooth)+'.ics'))[1:-1]
        return rv

    def smoothAttribute(self,smooth):
        rv=''
        if type(smooth)==unicode or type(smooth)==str:
             att=cmds.listAttr(smooth,multi=1,k=1)
             for a in att:
                av= str(cmds.getAttr(smooth+'.'+a))
                rv+=a+' '+av+' '
        return str(rv)

    def NS(self,mesh):
        rv=''
        nsSplit=mesh.split('|')
        nsSplit.reverse()
        for i in range(1,len(nsSplit)):
            pos=nsSplit[i].find('MSH_body')
            if (pos!=-1) and (nsSplit[i][pos-1]!=':') :
                rv=nsSplit[i].split('MSH_body')[0]
                break
            if nsSplit[i].find(':')!=1:
                rv=nsSplit[i].split(':')[0]
                break
        else:
            rv=mesh.split('|')[-2]
        return str(rv)

    def readTxt(self,path):
        file=open(path,'r')
        rv=file.read()
        file.close()
        return rv
    def writeTxt(self,path,content):
        print type(content)
        file=open(path,'w')
        file.write(content)
        file.close()

    def delTXT(self):
        dir=list(os.listdir(self.txtPath))
        allTxt=[]
        for a in dir:
            if a.find(self.sn)!=-1:
                allTxt.append(a)
        allTxt.sort()
        allTxt.reverse()
        size=len(allTxt)
        if size>7:
            for i in range(7,size):
                os.remove(self.txtPath+allTxt[i])

    def refresh(self):
        dir=list(os.listdir(self.txtPath))
        allTxt=[]
        for a in dir:
            if a.find(self.sn)!=-1:
                allTxt.append(a)
        allTxt.sort()
        allTxt.reverse()
        cmds.textScrollList('wxIISetSmoothInfoList',e=1,ra=1)
        cmds.textScrollList('wxIISetSmoothInfoList',e=1,append=allTxt)
        if len(allTxt)>0:
            cmds.textScrollList('wxIISetSmoothInfoList',e=1,sii=1)


    def lastFileName(self):
        dir=list(os.listdir(self.txtPath))
        allTxt=[]
        for a in dir:
                    if a.find(self.sn)!=-1:
                        allTxt.append(a)
        allTxt.sort()
        allTxt.reverse()
        if len(allTxt)!=0:
            return allTxt[0]
        else:
            return ''

    def lastFileInfo(self):
        lf = self.lastFileName()
        lf_longPath = self.txtPath + lf
        if len(lf)!=0:
            c=self.readTxt(lf_longPath)
            return c
        else:
            return ''

##zzj   ▲成块：
    def toBlock(self,mesh):
        mesh=str(mesh)
        ns=self.NS(mesh)
        smooth=self.smoothHistory(mesh)
        behindSmooth=''
        for a in smooth:
            face=self.smoothFace(a)
            att=self.smoothAttribute(a)
            behindSmooth+='\r\n\t'+a+'\r\n\t'+face+'\r\n\t\t'+att+'\r\n'
        block=self.sign+'\r\n'+ns+'\r\nmesh:\r\n\t'+mesh+'\r\nsmooth:'+behindSmooth

        return block


def save():
    func=smoothInfo()
    sn=cmds.file(q=1,sn=1,shn=1)
    content=''
    if sn.split('_')[0]!='lighting':
        cmds.confirmDialog(  message=u'lighting文件才可以保存信息!!', button=[u'确认'])
    else:
        confirm=cmds.confirmDialog( title=u'', message=u'Are you sure?   ( ⊙ o ⊙ )', button=['Yes','No'], defaultButton='Yes', cancelButton='No', dismissString='No' )
        if (confirm=='Yes'):

            lastFileContent=func.lastFileInfo()
            lastFileBlock= lastFileContent.split(func.sign)
            lastFileBlock.pop(0)

            allSM=func.allSmoothMesh()

            newAddBlock=''

            for a in allSM:
                mesh=str(a[1])
                cmds.select(mesh)
                block=func.toBlock(mesh)


                for lfb in lastFileBlock:

                    if (block.find(lfb)!=-1):
#                        print u'已经有啦'
                        break
                else:
                    newAddBlock+=block
            newContent=lastFileContent+newAddBlock
            func.writeTxt(func.currentTxtPath(),newContent)

#            print newAddBlock.decode('gbk')



'''
            allSM=func.allSmoothMesh()
            lastFileContent=func.lastFileInfo()

            ifNameSpace=''
            for a in allSM:
#   a  Result: ['mesh:', u'|fish_default:mainCtrl|fish_default:MSH_all|fish_default:MSH_body_|MSH_body_ShapeDeformed', 'smooth:', u'finalSmooth254'] #
                print func.smoothAttribute(a[3])
                break






#   判断是否和上一版本属性一样

                ns=func.NS(a[1])
                content+=func.sign+'\r\n'+ns+'\r\n'
                content+=str(a[0])
                content+='\r\n\t'
                content+=str(a[1])
                content+='\r\n'
                content+=str(a[2])
                content+='\r\n'

                for b in range(3,len(a)):
                    content+='\t'
                    content+=str(a[b])
                    content+='\r\n\t'
                    face=str(cmds.getAttr(str(a[b])+'.ics'))[1:-1]
                    content+=face
                    att=func.smoothAttribute(a[b])
                    for c in att:
                        content+='\r\n\t\t'
                        content+=str(c)
                        size=int(len(c)/8)
                        content+=(3-size)*'\t'
                        content+=str(att[c])
                    content+='\r\n'
            rwTXT().writeTxt(func.currentTxtPath(),content)

            func.delTXT()
            func.refresh()
'''



def load():
    func=smoothInfo()
    print 'hhh'



def UI():
    func=smoothInfo()
    try:
        cmds.deleteUI("wxIISetSmoothInfoUI")
    except:
        pass
    cmds.window('wxIISetSmoothInfoUI',title="wxII__SmoothInfo",mxb=False)
##zzj   ▲formLayout`
    form = cmds.formLayout(numberOfDivisions=100)
##zzj       ▲columnLayout`
    column1 = cmds.columnLayout(adj=1)
##zzj           ▲save
    cmds.button(l=u'save',h=30,         c='import idmt.maya.ROMA.smoothFind as sF\nsF.save()')
    cmds.setParent( '..' )
##zzj       ▲columnLayout
    column2 = cmds.columnLayout(adj=1)
##zzj           ▲load
    cmds.button(l=u'load',h=30,         c='import idmt.maya.ROMA.smoothFind as sF\nsF.load()')
    cmds.setParent( '..' )

##zzj       ▲columnLayout
    column3 = cmds.columnLayout(adj=1)
##zzj           ▲列表
    cmds.textScrollList('wxIISetSmoothInfoList',numberOfRows=10,sii=1,append=['1', '2', '3', '4', '5', '6', '7',],)
    cmds.setParent( '..' )

    cmds.formLayout( form,
            edit=True,
            attachForm=     [
                                (column1, 'left', 5), (column1, 'top', 5),
                                (column2, 'right', 5),(column2, 'top', 5),
                                (column3, 'left', 5),(column3, 'right', 5),(column3, 'bottom', 5)
                            ]
                        ,
            attachPosition= [
                                (column1, 'left', -120, 50),
                                (column1, 'right', 10, 50),

                                (column2, 'left', 10, 50),
                                (column2, 'right', -120, 50)
                            ]
                        ,
			attachControl=	[
    							(column3, 'top', 5, column2)
						    ]
                )
    cmds.setParent( '..' )
    cmds.setParent( '..' )

    cmds.window('wxIISetSmoothInfoUI',e=1,width=560,height=170)

    cmds.showWindow("wxIISetSmoothInfoUI")
    func.refresh()


