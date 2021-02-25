# -*- coding: utf-8 -*-
# Copyright (C) 2000-2010 IDMT. All rights reserved.
'''
Functions for Mov Converter
'''
__author__	= 'huangzhongwei@idmt.com.cn'
__date__	= '2011-03-22'

__ffmpeg__	= "\\\\file-cluster\\GDC\\Resource\\Support\\ffmpeg-20140818-git-3c19744-win64-static\\bin\\ffmpeg.exe"
__ffprobe__	= "\\\\file-cluster\\GDC\\Resource\\Support\\ffmpeg-20140818-git-3c19744-win64-static\\bin\\ffprobe.exe"

import json
import os
import re
import sys
import subprocess

def GetFileTitle(path = '', projectLong = '', projectShort = '', scene = '', shot = '', pipline = '', version = '', approved = 1):
    '''
    根据输入文件路径、项目全称、项目简称、集数、镜头、环节、版本、normal或者final等获得输出文件名。不带后缀
    '''
    filename = os.path.basename(path)
    #(root, ext) = os.path.splitext(filename)
    root = re.search('[^\.]+', filename).group(0)
    if projectLong == 'Woodlies':
        buff = re.compile('_').split(root)
        root = buff[0]+'_'+buff[1]+'_'+buff[2]+'_'+buff[3]+'_re_v'+re.search(r'[0-9^]*$',buff[5]).group(0)
    #if projectLong == 'Strawberry':
    #    buff = re.compile('_').split(root)
    #    if len(buff) > 4:
    #        root = 'SK_e%s_s%s_t%d' % (buff[1], buff[2], int(re.search(r'[0-9]*$',buff[4]).group(0)))
    return root

def AddFrameNumber(input, output):
    if input.lower() == output.lower():
        print u'不允许直接覆盖原文件'
        return
    codecv = ""
    command = "%s -v quiet -print_format json -show_format -show_streams \"%s\"" % (__ffprobe__, input)
    p = subprocess.Popen(command, shell = True, stdout = subprocess.PIPE)
    info = p.stdout.read()
    codecv = None
    try:
        dt = json.loads(info)
        for stream in dt["streams"]:
            if stream["codec_type"] == "video":
                codecv = stream["codec_name"]
                break
    except:
        pass
    command = "%s -y -i \"%s\" -vf drawtext=\"fontfile=\'C\\:/Windows/Fonts/ARIAL.TTF\':fontsize=24:x=0:y=0:fontcolor=green:text=\'%%{eif\\:n\\:d\\:4}\'\" -c copy -c:v %s -q:v 0 -q:a 0 \"%s\"" % (__ffmpeg__, input, codecv, output)
    print command
    subprocess.Popen(command, shell = True)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "AddFrameNumber":
            AddFrameNumber(sys.argv[2], sys.argv[3])