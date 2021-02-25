#from distutils.core import setup
#import py2exe
import os
import tkFileDialog
import tkMessageBox
import tempfile
import Tix
import time
from Tkinter import *
import sys
import pymssql
from win32com.client import Dispatch

execfile("//file-cluster/GDC/Resource/Support/Python/2.6/Lib/site-packages/idmt/standalone/yyGenerateBigImage.py")

class openDialog(Frame):
    def __init__(self, master=None):
        self.root=master
        self.createWidgets()

    def createWidgets(self):
        """ Create widgets
        """
        self.fFrame = Frame(self.root)
        
        optionList = ("DiveOllyDive2", "MonsterHigh", "Lionelville", "OKI", "PatchPillows", "SportLets", "Strawberry")
        self.projectName = StringVar()
        self.projectName.set(optionList[0])
        self.om = OptionMenu(self.fFrame, self.projectName, *optionList)
        self.om.pack(anchor = W)
        
        self.svDir = StringVar()
        self.eDir  = Entry(self.fFrame, width=30, textvariable=self.svDir)
        self.eDir.pack()
        
        #self.svPro = StringVar(value = "0 %")
        #self.eTxt  = Entry(self.fFrame, width=30, textvariable = self.svPro)
        #self.eTxt.pack()
        #self.cc = Tix.Meter(self.fFrame, value = .5)
        #self.cc.pack()
        
        
        Button(self.fFrame, text = "   Generate   ", command = self.getStart).pack()
        self.fFrame.pack()


    def getStart(self):
        project = self.projectName.get()
        episode = self.svDir.get()

        yyGenerateImageWrapper(project, episode)
        
        
if __name__ == "__main__":
    root=Tix.Tk()
    root.title("Update TGA Combo")
    od = openDialog(root)
    root.mainloop()

        

