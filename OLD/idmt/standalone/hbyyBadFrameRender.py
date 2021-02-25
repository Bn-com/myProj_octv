# -*- coding: utf-8 -*-
import os
import sys
import tkFileDialog
import tkMessageBox
import tempfile
from Tkinter import *
execfile("//file-cluster/GDC/Resource/Support/Python/2.6/Lib/site-packages/idmt/standalone/yyCheckBadFrame.py")
#YY提供坏帧数据

class Application(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.svDir = StringVar()
        self.svDir2 = StringVar()
        self.badFrameStr = StringVar()
        Label(self,
              text = "本工具注意事项：（有问题联系杨冶和黄壁）\n1:选择文件时,一定要选择区分是否是mr层渲染  \n2:暂时mr渲染,只支持一个层的文件                    \n3,文件不要放在桌面上                                        \n4,输出图片不要放在桌面上                                 \n5.工具暂时不支持ctrl+Z                                      "
              ).grid(row = 2, column = 2, sticky = W)
        Label(self,
              text = "当前文件的坏帧列表:"
              ).grid(row = 8, column = 2, sticky = W)
        Entry(self,w=50,textvariable=self.svDir
              ).grid(row = 4, column = 2, sticky = W)
        Entry(self,w=50,textvariable=self.svDir2
              ).grid(row = 5, column = 2, sticky = W)
        self.favorite = StringVar()
        Button(self,text="        选择文件       ",command=self.getDir).grid(row = 4, column = 4, sticky = W)
        Button(self,text="        输出路径       ",command=self.getDir2).grid(row = 5, column = 4, sticky = W)
        Button(self,text="                                                Render                                    ",command=self.HbRenderStart).grid(row = 13, column = 2, sticky = W)
        Button(self,text="        获取坏帧        " ,height=20,command=self.getBadFrame).grid(row = 9, column = 4, sticky = W)
        self.Frame_txt = Text(self, width = 38, height = 17, wrap = WORD)
        self.Frame_txt.grid(row = 9, column = 0, columnspan = 3)
        self.likes_mentalray = BooleanVar()
        Checkbutton(self,text = "Mental Ray",variable = self.likes_mentalray).grid(row = 12, column = 2, sticky = W)
        
        thisMachine = os.getenv("COMPUTERNAME")
        initPath = "Z:/Netrender/Maya/"+ thisMachine +"/scenes"
        
        if os.access(initPath, os.R_OK) == False:
            initPath = "Z:/Netrender/Maya/"
        
        
        self.file_opt = options = {}
        options['filetypes'] = [('maya files', '.mb')]
        options['initialdir'] = initPath
        options['title'] = 'Automatically jump to your file repository.'


    def getDir(self):
        self.dir = tkFileDialog.askopenfilename(**self.file_opt)
        self.svDir.set(self.dir)
        getFileName=self.dir.split("/")
        getDelete=getFileName[-1].split("_")
        project=""
        Number=""
        if getDelete[0]=="do2":
                project="DiveOllyDive2"
        elif getDelete[0]=="lv":
                project="Lionelville"
        elif getDelete[0]=="sk":
                project="Strawberry"
        if int(getDelete[1])%2==1:
                Number="Odd"
        elif int(getDelete[1])%2==0:
                Number="Even"
        NeedImageId='//file-cluster/gdc/netrender/scenes/'+project+'/'+Number+'/ep_'+getDelete[1]+'/sc_'+getDelete[2]
        self.svDir2.set(NeedImageId)

    def getDir2(self):
        self.dir2 = tkFileDialog.askdirectory()
        self.svDir2.set(self.dir2)


    def getBadFrame(self):
        inDir = self.svDir.get()
        if inDir!="":
            GetFileName=inDir.split("/")
            GetFileType=inDir.split(".")
            if GetFileType[-1].upper()=="MB":
                GetyyDate=yyCheckBadFrameWrapper(GetFileName[-1])
                print len(GetyyDate[0])
                AllYyData=""
                AllYyId=""
                for i in range(len(GetyyDate[0])):
                    AllYyId=AllYyId+GetyyDate[0][i]+"*"
                    GetLayerName=GetyyDate[0][i].split("/")
                    Need=GetLayerName[-1]+">>>"+GetyyDate[1][i]
                    AllYyData=AllYyData+Need+"\n"
                AllNeedDate=AllYyId+AllYyData
                self.Frame_txt.delete(0.0, END)
                self.badFrameStr.set(AllYyData)
                self.Frame_txt.insert(0.0, self.badFrameStr.get())
            else:
                tkMessageBox.showwarning(title = "提示", message = "文件类型不是MB！")
        else:
            tkMessageBox.showwarning(title = "提示", message = "请先选择Mb文件！")
            
    def HbRenderStart(self):
        tempDir = tempfile.gettempdir()
        a = self.Frame_txt.get("@0,0", "@8888,8888")
        print a
        inDir = self.svDir.get()
        outDir = self.svDir2.get()
        getFileName=inDir.split("/")
        getDelete=getFileName[-1].split("_")
        project=""
        Number=""
        if getDelete[0]=="do2":
                project="DiveOllyDive2"
        elif getDelete[0]=="lv":
                project="Lionelville"
        elif getDelete[0]=="sk":
                project="Strawberry"
        if int(getDelete[1])%2==1:
                Number="Odd"
        elif int(getDelete[1])%2==0:
                Number="Even"
        NeedImageTemp='//file-cluster/gdc/netrender/scenes/'+project+'/'+Number+'/ep_'+getDelete[1]+'/sc_'+getDelete[2]
        GetFileName=inDir.split("/")
        GetImagesName=GetFileName[-1].split(".")
        GetyyDate=yyCheckBadFrameWrapper(GetFileName[-1])
        AllYyData=""
        AllYyId=""
        for i in range(len(GetyyDate[0])):
            AllYyId=AllYyId+GetyyDate[0][i]+"*"
        finialId=AllYyId.replace(NeedImageTemp, outDir)
        AllNeedDate=finialId+a
        f=open(tempDir+"/YYBadFrameData.txt","w")
        f.write (AllNeedDate)
        f.close
        GetFileType=inDir.split(".")
        GetMrBadFrameId=AllYyId.split("*")

        if os.access(inDir, os.R_OK)  == True and GetFileType[-1].upper()=="MB":
            if a!="":
                if self.likes_mentalray.get():
                        getMrFrameA=a.split(">>>")
                        getMrFrameB=getMrFrameA[1].split(",")
                        allMrCommand=""
                        for ss in range (len(getMrFrameB)):
                                GetEveryFrame=getMrFrameB[ss].split("-")
                                if len(GetEveryFrame)==2:
                                        mrCommand='d:\Alias\MAYA2008\Bin\Render.exe  -r mr -proj d:\ -s '+GetEveryFrame[0].replace("\n", "")+' -e '+GetEveryFrame[1].replace("\n", "")+' -b 1.000 -rfs '+GetEveryFrame[0].replace("\n", "")+' -rfb 1 -pad 4  -rd ' +outDir+' '+inDir
                                        allMrCommand=allMrCommand+mrCommand+'\n'
                                else:
                                        mrCommand='d:\Alias\MAYA2008\Bin\Render.exe  -r mr -proj d:\ -s '+getMrFrameB[ss].replace("\n", "")+' -e '+getMrFrameB[ss].replace("\n", "")+' -b 1.000 -rfs '+getMrFrameB[ss].replace("\n", "")+' -rfb 1 -pad 4  -rd '+outDir+' '+inDir
                                        allMrCommand=allMrCommand+mrCommand+'\n'
                        if allMrCommand != "":
                            try:
                                f = open(tempDir + "/HbBadFrameRender.bat", "w")
                                f.write(allMrCommand)
                                f.close()
                            except:
                                pass
                            try:
                                os.system(tempDir + "/HbBadFrameRender.bat")
                            except:
                                pass

                else:
                        thisCommand = 'D:\Alias\MAYA2008\Bin\mayabatch -proj "C:" -file "'+inDir+'" -command "HbBadFrameRender"'
                        print thisCommand
                        if thisCommand != "":
                            try:
                                f = open(tempDir + "/HbBadFrameRender.bat", "w")
                                f.write(thisCommand)
                                f.close()
                            except:
                                pass
                            try:
                                os.system(tempDir + "/HbBadFrameRender.bat")
                            except:
                                pass
            else :
                tkMessageBox.showwarning(title = "提示", message = "清先获取坏帧！")
        else:
            tkMessageBox.showwarning(title = "提示", message = "请确认文件！")
if __name__ == "__main__":
    root=Tk()
    
    user = os.getenv("USERNAME")
    id = os.getenv("COMPUTERNAME")
    
    root.title(user + " " + id + " 坏帧渲染工具 beta 1.4")
    od = Application(root)
    root.geometry("420x500")
    root.mainloop()
