# -*- coding: utf-8 -*-
'''
将数据块的第二个4字节转换成long整形数
'''
import re

import struct
def GetLong(s):
    if len(s) == 4:
        l = (struct.unpack('B', s[0])[0] << 24) + (struct.unpack('B', s[1])[0] << 16) + (struct.unpack('B', s[2])[0] << 8) + (struct.unpack('B', s[3])[0] << 0)
    elif len(s) == 8:
        l = (struct.unpack('B', s[0])[0] << 56) + (struct.unpack('B', s[1])[0] << 48) + (struct.unpack('B', s[2])[0] << 40) + (struct.unpack('B', s[3])[0] << 32) + (struct.unpack('B', s[4])[0] << 24) + (struct.unpack('B', s[5])[0] << 16) + (struct.unpack('B', s[6])[0] << 8) + (struct.unpack('B', s[7])[0] << 0)
    return l

'''
得到mb文件的Reference路径，返回数组
'''
def GetReferencesMB(path):
    references = []

    f = open(path, 'rb')     # 二进制方式打开文件

    bit = 4
    for4 = f.read(4)
    if for4 == 'FOR4':
        bit = 4
    elif for4 == 'FOR8':
        bit = 8
    else:
        raise Exception(u'文件格式跟文件后缀名不匹配')

    f.seek(bit)     # FOR4
    s = f.read(bit)     # 文件大小
    filesize = GetLong(s)
    f.seek(bit * 2 + 4)     # Maya
    findFrdi = False;
    while True:
        for4 = f.read(4)     # 读第一个4字节，FOR4
        if not (for4 == 'FOR4' or for4 == 'FOR8'):     # 不是正常的数据块结构，已经出错，跳出
            break
        f.read(bit - 4)
        s = f.read(bit)    # 读第二个4字节，数据的大小
        size = GetLong(s)     # 转成long整形数，得到数据的大小
        i = f.tell()
        s = f.read(4)    # 读第三个4字节，数据块的标签
        if s == 'FRDI':     # FRDI数据块，里面有Reference信息
            f.read(bit * 2 + 4)    # 跳过暂时未知何意义的12个字节
            s = f.read(size - 8 - bit * 2)    # 读Reference路径字符串
            s = s.split('\0')[0]
            references.append(s)
            findFrdi = True
        elif findFrdi:     # mb文件的头部已经读完，再也不会有FRDI数据块，跳出
            break
        f.seek(i+size)
    f.close()

    return references

def GetReferencesMA(path):
    references = []
    f = open(path, "r")
    line = f.readline()
    if re.search('^//Maya ', line) == None:
         raise Exception(u'文件格式跟文件后缀名不匹配')
    while True:
        line = f.readline()
        if not line:
            break
        if re.search('^requires ', line) != None:
            break
        m = re.search(r'\"([^\"]+\.m[ab])\"', line, re.IGNORECASE)
        if m != None:
            references.append(m.group(1))
    f.close()
    return references

def GetReferences(path):
    if re.search(r'\.mb', path, re.IGNORECASE):
        return GetReferencesMB(path)
    else:
        return GetReferencesMA(path)