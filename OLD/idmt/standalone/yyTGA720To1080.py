# -*- coding: utf-8 -*-
#from distutils.core import setup
#import py2exe
import os
import tkFileDialog
import tkMessageBox
import tempfile
from Tkinter import *

class openDialog(Frame):
    def __init__(self, master=None):
        self.root=master
        self.createWidgets()

    def createWidgets(self):
        """ Create widgets
        """
        self.fFrame = Frame(self.root)

        self.bSelDir = Button(self.fFrame, text="  Please Select a Target ")
        self.bSelDir["command"] =  self.getDir
        self.bSelDir.pack(anchor = W)

        self.svDir = StringVar()
        self.eDir  = Entry(self.fFrame, width=70, textvariable=self.svDir)
        self.eDir.pack()

        Button(self.fFrame, text = "  Select a Destination Folder  ", command = self.getDir2).pack(anchor = W)
        
        self.svDir2 = StringVar()
        self.eDir = Entry(self.fFrame, width = 70, textvariable = self.svDir2)
        self.eDir.pack()
        
        Button(self.fFrame, text = "  Start Transform  ", command = self.getStart).pack()
        
        self.fFrame.pack()

    def getDir(self):
        self.dir = tkFileDialog.askdirectory()
        self.svDir.set(self.dir)
        
    def getDir2(self):
        self.dir2 = tkFileDialog.askdirectory()
        self.svDir2.set(self.dir2)
        
    def getStart(self):
        inDir = self.svDir.get()
        outDir = self.svDir2.get()
        tempDir = tempfile.gettempdir()
        
        if os.access(inDir, os.R_OK) == True and os.access(outDir, os.R_OK) == True:
            
            if inDir != outDir:
                allFiles = os.listdir(inDir)
                batFile = ""
                for i in range(len(allFiles)):
                    if allFiles[i].upper().find(".TGA")>0:
                        #C:\Shake2.5\shake.exe "Z:/scratch/wumin/720/do2_102_048_cp_c001.0001.tga" -resize 1920 1080 "sinc" 0 -fo "D:/DO2_e201_s027_t1.tga" "tga" 2 0 -v
                        thisCommand = u'C:\Shake2.5\shake.exe "' + inDir + u'/' + allFiles[i] + u'" -resize 1920 1080 "sinc" 0 -fo "' + outDir + u'/' + allFiles[i] + u'" "tga" 2 0 -v \r\n'
                        batFile += thisCommand
                
                if batFile != "":
                    try:
                        f = open(tempDir + u"/temp_idmt720To1080.bat", "w")
                        f.write(batFile)
                        f.close()
                    except:
                        pass
                    try:
                        os.system(tempDir + u"/temp_idmt720To1080.bat")
                    except:
                        pass
                    
                else:
                    tkMessageBox.showwarning(title = "Warning", message = "No found images.")
            else:
                tkMessageBox.showwarning(title = "Warning", message = "Not support same directory.")
        else:
            tkMessageBox.showerror(title = "Error", message = "Not correct directory!")

if __name__ == "__main__":
    root=Tk()
    root.title("720p To 1080p Batch")
    od = openDialog(root)
    root.mainloop()