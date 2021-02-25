# -*- coding: utf-8 -*-

'''
Description:
1)给选择的图片添加黑边，并表示版本及镜头号
2)黑边宽为50，版本去cp后字段最后一位，镜头号依据Woodlies项目(集场镜头)
'''

__author__  = 'WansHoulOng'
__date__  = '2011-2-16'


import os
import re
import Image
import ImageDraw
import ImageFont
import maya.cmds as mel

def addImageEdge (image):
    (folder,file) = os.path.split(image)
    newFolder = folder+"/sign"
    if(not os.path.isdir(newFolder)):
        os.makedirs(newFolder)
    
    buff = re.compile(r'_|\.').split(file)
    ep = buff[1]
    seq = buff[2]
    sc = buff[3]
    tk = int(buff[5][len(buff[5])-1])
    take = 'TK'+str(tk)
    shot = ep+"_"+seq+"_"+sc
    
    im = Image.open(image)
    (width,height) = im.size

    newImage = Image.new('RGB', (width+100, height+100), 0)
    newImage.paste(im,(50,50))
    newDraw = ImageDraw.Draw(newImage)
    font = ImageFont.truetype("ARIALBD.TTF", 15)
    newDraw.text((30,10),take,font=font)
    newDraw.text((30,30),shot,font=font)
    newImage.save(newFolder+'/'+file)

def selectFolderOrImage ():
    '''main '''
    files = mel.fileDialog2(fm=4,ds=2)
    for file in files :
        addImageEdge(file)