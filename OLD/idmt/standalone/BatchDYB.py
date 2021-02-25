import os
import sys
sys.path.append("//file-cluster/gdc/Resource/Support/Python26/Lib/site-packages/PIL")
import PIL
import tkFileDialog
import tkMessageBox
from Tkinter import *
import Image, ImageTk 
import  ImageDraw, ImageFont

class Application(Frame):
        
  
        def __init__(self, master = None):
                Frame.__init__(self, master)
                self.grid()
                self.create_widgets()

        def create_widgets(self):
                self.svDir = StringVar()
                self.svDir2 = StringVar()
                self.svDir3 = StringVar()
                self.svDir4 = StringVar()
                self.svDir5 = StringVar()

                self.svDir6 = StringVar()
                self.svDir7 = StringVar()
                self.svDir8 = StringVar()
                self.svDir9 = StringVar()
                
                self.badFrameStr = StringVar()
                Label(self,
                      text = "图片地址"
                      ).grid(row = 1, column = 2, sticky = W)
                Label(self,
                      text = "环节"
                      ).grid(row = 9, column = 4, sticky = W)
                Label(self,
                      text = "名字"
                      ).grid(row = 10, column = 4, sticky = W)
                Label(self,
                      text = "编号"
                      ).grid(row = 11, column = 4, sticky = W)
                
                Entry(self,w=50,textvariable=self.svDir
                      ).grid(row = 4, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir3
                      ).grid(row = 5, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir4
                      ).grid(row = 6, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir5
                      ).grid(row = 7, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir2
                      ).grid(row = 8, column = 2, sticky = W)


                Entry(self,w=50,textvariable=self.svDir6
                      ).grid(row = 9, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir7
                      ).grid(row = 10, column = 2, sticky = W)
                Entry(self,w=50,textvariable=self.svDir8
                      ).grid(row = 11, column = 2, sticky = W)
                
                Entry(self,w=50,textvariable=self.svDir9
                      ).grid(row = 2, column = 2, sticky = W)
                
                
                self.favorite = StringVar()
                Button(self,text="        Persp       ",command=self.getDir).grid(row = 4, column = 4, sticky = W)
                Button(self,text="        Front       ",command=self.getDir3).grid(row = 5, column = 4, sticky = W)
                Button(self,text="        Side       ",command=self.getDir4).grid(row = 6, column = 4, sticky = W)
                Button(self,text="        Back       ",command=self.getDir5).grid(row = 7, column = 4, sticky = W)
                Button(self,text="        参考      ",command=self.getDir9).grid(row = 2, column = 4, sticky = W)
                
                Button(self,text="        outpath       ",command=self.getDir2).grid(row = 8, column = 4, sticky = W)
                Button(self,text="                                                          Start                                            ",command=self.HbStart).grid(row = 13, column = 2, sticky = W)

                self.svDir6.set("Prop Model")
                self.svDir.set("H:/work/SK2/daily/test.jpg")
                self.svDir3.set("H:/work/SK2/daily/test.jpg")
                #self.svDir4.set("H:/work/SK2/daily/test.jpg")
                #self.svDir5.set("H:/work/SK2/daily/test.jpg")

                self.svDir2.set("D:/test.tga")
                self.svDir7.set("Name")
                self.svDir8.set("Number")
                self.svDir9.set("H:/work/SK2/daily/sk_sp004048rake_co_h_2d.0001.jpg")

                
        def getDir(self):
                self.dir = tkFileDialog.askopenfilename()
                self.svDir.set(self.dir)
        def getDir2(self):
                self.dir2 = tkFileDialog.asksaveasfilename()
                self.svDir2.set(self.dir2)        
        def getDir3(self):
                self.dir3 = tkFileDialog.askopenfilename()
                self.svDir3.set(self.dir3)
        def getDir4(self):
                self.dir4 = tkFileDialog.askopenfilename()
                self.svDir4.set(self.dir4)      
        def getDir5(self):
                self.dir5 = tkFileDialog.askopenfilename()
                self.svDir5.set(self.dir5)
        def getDir9(self):
                self.dir9 = tkFileDialog.askopenfilename()
                self.svDir9.set(self.dir9)
                TheName=self.dir9.split("/")[-1].split("_")[1]
                TheMassage=""
                TheMassage2=""
                if TheName[1]=="p":
                        TheMassage="SP"+TheName[2]+TheName[3]+TheName[4]+"_"+TheName[5]+TheName[6]+TheName[7]
                        TheMassage2="Props Texture"
                if TheName[1]=="c":
                        TheMassage="SC"+TheName[2]+TheName[3]+TheName[4]+"_"+TheName[5]+TheName[6]+TheName[7]
                        TheMassage2="Characters Texture"
                if TheName[1]=="s":
                        TheMassage="SS"+TheName[2]+TheName[3]+TheName[4]+"_"+TheName[5]+TheName[6]+TheName[7]
                        TheMassage2="environment Texture"
                self.svDir6.set(TheMassage2)
                self.svDir8.set(TheMassage) 
        def HbStart(self):



                inDir = self.svDir.get()
                inDir3 = self.svDir3.get()
                inDir4 = self.svDir4.get()
                inDir5 = self.svDir5.get()


                inDir6 = self.svDir6.get()
                inDir7 = self.svDir7.get()
                inDir8 = self.svDir8.get()
                inDir9 = self.svDir9.get()

                
                outDir = self.svDir2.get()
		print inDir
		print inDir3
		print inDir4
		print inDir5

                if outDir=="":
                        tkMessageBox.showwarning(title = "提示", message = "请选择输出路径")
                if outDir!="":
                        if inDir=="" and inDir3=="" and inDir4=="" and inDir5=="" :
                                tkMessageBox.showwarning(title = "提示", message = "请选择需要拼的图片")
                                return
                        if inDir6=="" or inDir7=="" or inDir8=="":
                                tkMessageBox.showwarning(title = "提示", message = "请输入环节,名字,编号的必要信息")
                                return
                        if inDir!="" and inDir3=="" and inDir4=="" and inDir5=="":
                                TheNormalDaily="Z:/Resource/Support/Maya/projects/Strawberry2/daiyNormal/Scenes&Props_Daily_Nromal.jpg"
                                NormalIm=Image.open(TheNormalDaily)
                                DailyIm=Image.open(inDir)
                                referenceIm=Image.open(inDir9)

                                
                                if referenceIm.size[0]/referenceIm.size[1]>=1.337979:
                                        out = referenceIm.resize((1536, 1536*referenceIm.size[1]/referenceIm.size[0]))
                                if referenceIm.size[0]/referenceIm.size[1]<1.337979:
                                        out = referenceIm.resize((1148*referenceIm.size[0]/referenceIm.size[1], 1148))


                                if DailyIm.size[0]/DailyIm.size[1]>=1.478:
                                        DailyIm = DailyIm.resize((1345, 1345*DailyIm.size[1]/DailyIm.size[0]))
                                if referenceIm.size[0]/referenceIm.size[1]<1.478:
                                        DailyIm= DailyIm.resize((910*DailyIm.size[0]/DailyIm.size[1], 910))                                        
                                        
                                if NormalIm.mode!="RGBA":
                                        NormalIm=NormalIm.convert("RGBA")

                                        layer = Image.new("RGBA",NormalIm.size,(0,0,0,0))
                                        layer.paste(DailyIm,(1900,195))
                                        newim = Image.composite(layer,NormalIm,layer)

                                        layer2 = Image.new("RGBA",newim.size,(0,0,0,0))
                                        layer2.paste(out,(15,15))
                                        newim = Image.composite(layer2,newim,layer2)

                                        text = inDir6
                                        im=newim
                                        img = im
                                        FONT = "c:/windows/fonts/verdana.ttf"
                                        watermark = Image.new("RGBA", (15*len(text), 30))
                                        watermark.paste('white', (0, 0,1000,1000))
                                        draw = ImageDraw.ImageDraw(watermark, "RGBA")
                                        size = 0
                                        while True:
                                               size += 1
                                               nextfont = ImageFont.truetype(FONT, size)
                                               nexttextwidth, nexttextheight = nextfont.getsize(text)
                                               if nexttextwidth+nexttextheight/3 > watermark.size[0]:
                                                   break
                                               font = nextfont
                                               textwidth, textheight = nexttextwidth-3, nexttextheight-3

                                        draw.setfont(font)
                                        draw.ink = 0
                                        draw.text(((watermark.size[0]-textwidth)/2,(watermark.size[1]-textheight)/2), text)
                                        mask = watermark.convert("L").point(lambda x: min(x, 100))
                                        watermark.putalpha(mask)
                                        img.paste(watermark, (1920,38))


                        if inDir!="" and inDir3!="" and inDir4!="" and inDir5!="":
                                TheNormalDaily="Z:/Resource/Support/Maya/projects/Strawberry2/daiyNormal/Characters_Daily_Nromal.jpg"
                                NormalIm=Image.open(TheNormalDaily)
                                DailyIm=Image.open(inDir)
                                DailyIm3=Image.open(inDir3)
                                DailyIm4=Image.open(inDir4)
                                DailyIm5=Image.open(inDir5)
                              
                                referenceIm=Image.open(inDir9)

                                
                                if referenceIm.size[0]/referenceIm.size[1]>=1.337979:
                                        out = referenceIm.resize((1536, 1536*referenceIm.size[1]/referenceIm.size[0]))
                                if referenceIm.size[0]/referenceIm.size[1]<1.337979:
                                        out = referenceIm.resize((1148*referenceIm.size[0]/referenceIm.size[1], 1148))


                                if DailyIm.size[0]/DailyIm.size[1]>=1:
                                        DailyIm = DailyIm.resize((460, 460*DailyIm.size[1]/DailyIm.size[0]))
                                if DailyIm.size[0]/DailyIm.size[1]<1:
                                        DailyIm= DailyIm.resize((460*DailyIm.size[0]/DailyIm.size[1], 460))                                        

                                if DailyIm3.size[0]/DailyIm3.size[1]>=1:
                                        DailyIm3 = DailyIm3.resize((460, 460*DailyIm3.size[1]/DailyIm3.size[0]))
                                if DailyIm3.size[0]/DailyIm3.size[1]<1:
                                        DailyIm3= DailyIm3.resize((460*DailyIm3.size[0]/DailyIm3.size[1], 460))     
 

                                if DailyIm4.size[0]/DailyIm4.size[1]>=1:
                                        DailyIm4= DailyIm4.resize((460, 460*DailyIm4.size[1]/DailyIm4.size[0]))
                                if DailyIm4.size[0]/DailyIm4.size[1]<1:
                                        DailyIm4= DailyIm4.resize((460*DailyIm4.size[0]/DailyIm4.size[1], 460))     
 
                                if DailyIm5.size[0]/DailyIm5.size[1]>=1:
                                        DailyIm5= DailyIm5.resize((460, 460*DailyIm5.size[1]/DailyIm5.size[0]))
                                if DailyIm5.size[0]/DailyIm5.size[1]<1:
                                        DailyIm5= DailyIm5.resize((460*DailyIm5.size[0]/DailyIm5.size[1], 460))    
                                        
                                if NormalIm.mode!="RGBA":
                                        NormalIm=NormalIm.convert("RGBA")

                                        layer = Image.new("RGBA",NormalIm.size,(0,0,0,0))
                                        layer.paste(DailyIm,(1831,165))
                                        newim = Image.composite(layer,NormalIm,layer)
                                        
                                        

                                        layer2 = Image.new("RGBA",newim.size,(0,0,0,0))
                                        layer2.paste(out,(15,15))
                                        newim = Image.composite(layer2,newim,layer2)
                                        
                                        
                                        layer3 = Image.new("RGBA",newim.size,(0,0,0,0))
                                        layer3.paste(DailyIm3,(2385,165))
                                        newim = Image.composite(layer3,newim,layer3)     
     

                                        layer4 = Image.new("RGBA",newim.size,(0,0,0,0))
                                        layer4.paste(DailyIm4,(1832,670))
                                        newim = Image.composite(layer4,newim,layer4)   
                                        
                                        layer5 = Image.new("RGBA",newim.size,(0,0,0,0))
                                        layer5.paste(DailyIm5,(2385,670))
                                        newim = Image.composite(layer5,newim,layer5)   
                                        
                                        text = inDir6
                                        im=newim
                                        img = im
                                        FONT = "c:/windows/fonts/verdana.ttf"
                                        watermark = Image.new("RGBA", (15*len(text), 30))
                                        watermark.paste('white', (0, 0,1000,1000))
                                        draw = ImageDraw.ImageDraw(watermark, "RGBA")
                                        size = 0
                                        while True:
                                               size += 1
                                               nextfont = ImageFont.truetype(FONT, size)
                                               nexttextwidth, nexttextheight = nextfont.getsize(text)
                                               if nexttextwidth+nexttextheight/3 > watermark.size[0]:
                                                   break
                                               font = nextfont
                                               textwidth, textheight = nexttextwidth-3, nexttextheight-3

                                        draw.setfont(font)
                                        draw.ink = 0
                                        draw.text(((watermark.size[0]-textwidth)/2,(watermark.size[1]-textheight)/2), text)
                                        mask = watermark.convert("L").point(lambda x: min(x, 100))
                                        watermark.putalpha(mask)
                                        img.paste(watermark, (1920,38))


                        text = inDir7
                        im=newim
                        img = im
                        FONT = "c:/windows/fonts/verdana.ttf"
                        watermark = Image.new("RGBA", (15*len(text), 30))
                        watermark.paste('white', (0, 0,1000,1000))
                                        
                        draw = ImageDraw.ImageDraw(watermark, "RGBA")
                        size = 0
                        while True:
                                size += 1
                                nextfont = ImageFont.truetype(FONT, size)
                                nexttextwidth, nexttextheight = nextfont.getsize(text)
                                if nexttextwidth+nexttextheight/3 > watermark.size[0]:
                                        break
                                font = nextfont
                                textwidth, textheight = nexttextwidth, nexttextheight

                        draw.setfont(font)
                        draw.ink = 0
                        draw.text(((watermark.size[0]-textwidth)/2,(watermark.size[1]-textheight)/2), text)
                        mask = watermark.convert("L").point(lambda x: min(x, 55))
                        watermark.putalpha(mask)
                        img.paste(watermark, (1900,75))
                                        


                        text = inDir8
                        im=newim
                        img = im
                        FONT = "c:/windows/fonts/verdana.ttf"
                        watermark = Image.new("RGBA", (15*len(text), 30))
                        watermark.paste('white', (0, 0,1000,1000))
                                        
                        draw = ImageDraw.ImageDraw(watermark, "RGBA")
                        size = 0
                        while True:
                                size += 1
                                nextfont = ImageFont.truetype(FONT, size)
                                nexttextwidth, nexttextheight = nextfont.getsize(text)
                                if nexttextwidth+nexttextheight/3 > watermark.size[0]:
                                        break
                                font = nextfont
                                textwidth, textheight = nexttextwidth, nexttextheight

                        draw.setfont(font)
                        draw.ink =0
                        draw.text(((watermark.size[0]-textwidth)/2,(watermark.size[1]-textheight)/2), text)
                        mask = watermark.convert("L").point(lambda x: min(x, 55))
                        watermark.putalpha(mask)
                        img.paste(watermark, (2320,60))                                        

                        img.show()


                
                        newim = newim.convert("RGBA") 
                        newim.save(outDir, "TGA")



if __name__ == "__main__":
	HbFishRenderGUI = Tk()
	HbFishRenderGUI.title("前期daily拼图")
	app = Application(HbFishRenderGUI)
	HbFishRenderGUI.geometry("450x250")
	HbFishRenderGUI.mainloop()