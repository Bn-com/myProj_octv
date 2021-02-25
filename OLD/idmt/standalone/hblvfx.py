import os
import tkFileDialog
import tkMessageBox
import tempfile
from Tkinter import *
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.svDir = StringVar()
        Label(self,
              text = "This Is LV FX TOOLS :"
              ).grid(row = 2, column = 2, sticky = W)
        Entry(self,w=50,textvariable=self.svDir
              ).grid(row = 3, column = 2, sticky = W)
        self.svDir2 = StringVar()

        self.favorite = StringVar()
        Button(self,text="   File Folder Name ",command=self.getDir).grid(row = 3, column = 4, sticky = W)
        Button(self,text="        OK          ",command=self.HbRenderStart).grid(row = 8, column = 2, sticky = W)

        self.results_txt = Text(self, width = 50, height = 20, wrap = WORD)
        self.results_txt.grid(row = 5, column = 0, columnspan = 3)
        Radiobutton(self,
                     text = "all",
                     variable = self.favorite,
                     value = "all.",
                     command = self.update_text
                     ).grid(row = 6, column = 2, sticky = W)
        Radiobutton(self,
                     text = "select",
                     variable = self.favorite,
                     value = "select.",
                     ).grid(row = 7, column = 2, sticky = W)

    def getDir(self):
        self.dir = tkFileDialog.askdirectory()
        self.svDir.set(self.dir)
        self.update_text

    def update_text(self):
        print "ni hao ya"
        inDir = self.svDir.get()
        allFiles = os.listdir(inDir)
        mayaFile = ""
        for i in range(len(allFiles)):
                if allFiles[i].upper().find(".MB")>0:
                    mayaFile=mayaFile+allFiles[i]+"\n"
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, mayaFile)
    def getDir2(self):
        self.dir2 = tkFileDialog.askdirectory()
        self.svDir2.set(self.dir2)
    def HbRenderStart(self):
        inDir = self.svDir.get()
        outDir = self.svDir2.get()
        tempDir = tempfile.gettempdir()
        
        if os.access(inDir, os.R_OK) == True :
            allFiles = os.listdir(inDir)
            batFile = ""
            for i in range(len(allFiles)):
                if allFiles[i].upper().find(".MB")>0:
                    thisCommand = 'D:\Alias\MAYA2008\Bin\mayabatch -proj "D:" -file "'+inDir+'/'+allFiles[i]+'" -command "HBFXtest"'
                    batFile += thisCommand+'\n'
                    print thisCommand

            if batFile != "":
                try:
                    f = open(tempDir + "/HbFishRendering.bat", "w")
                    f.write(batFile)
                    f.close()
                except:
                    pass
                try:
                    os.system(tempDir + "/HbFishRendering.bat")
                except:
                    pass
                
            else:
                tkMessageBox.showwarning(title = "Warning", message = "No found maya.mb")

HbFishRenderGUI = Tk()
HbFishRenderGUI.title("LV FX TOOLS")
app = Application(HbFishRenderGUI)
HbFishRenderGUI.geometry("420x500")
HbFishRenderGUI.mainloop()



