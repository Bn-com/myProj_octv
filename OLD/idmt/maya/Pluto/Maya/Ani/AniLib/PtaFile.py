#-*- coding: utf-8 -*-
'''
Created on 2014年9月15��

@author: zhaozhongjie
'''
import json

# json_file =r"D:\Pluto\workspace\PlutoPip\MyLib\PPanim\AnimLibrary\test.json"

# with open(json_file, "r") as f:
#     json_data = json.loads(f.read()) 

class PtaRW(json.JSONEncoder):
    '''
    写入Json文件的格式,以及读和写的函数
    '''
    def _iterencode(self, o, markers=None):
        if isinstance(o,  list ):
            rv = ''
            rv_list = []
            for a in o:
                tmp = []
                for b in a:
                    if isinstance(b, unicode ):
                        tmp.append('"'+str(b)+'"')
                    elif isinstance(b, bool ):
                        tmp.append(str(b).lower())
                    elif isinstance(b, float ):
                        tmp.append(b)
                    elif isinstance(b, int ):
                        tmp.append(b)
                    else:
                        tmp.append('null')
                rv_list.append( '\n                [' +','.join([str(c) for c in tmp]) + ']')
            rv = '['+','.join(rv_list)+'\n            ]'
            return (rv)
        return super(PtaRW, self)._iterencode(o, markers)
    
    def printData(self,json_data):
        print "----non_anim----"
        for a in json_data["zzj_non_anim"].keys():
            print a, json_data["zzj_non_anim"][a]
         
        print "----anim----"
        for a in json_data["zzj_anim"].keys():
            print a
            for b in json_data["zzj_anim"][a]:
                print b
    
    def readFile(self,path):
        with open(path, "r") as f:
            json_data = json.loads(f.read()) 
            return json_data
    
    def writeFile(self,path,json_data):
        with open(path, "w") as f:
            json.dump(json_data,f,indent=4,sort_keys=True, cls=PtaRW)
    

# j = PtaRW()        
# j.printData(json_data)       

# data = {'zzj_anim': {u'pSphere1.rotateZ': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.scaleY': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.scaleX': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.rotateY': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.rotateX': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.rotateZ': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.visibility': [[15.0, 1.0, u'spline', u'step', True, 0.0, 0.0, 1.0, 0.0]], u'pSphere1.rotateY': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.translateZ': [[15.0, -3.6043561630132857, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.translateY': [[15.0, 4.3219785709619707, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.translateX': [[15.0, 5.5726798181778925, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.translateZ': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.translateY': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.translateX': [[15.0, 0.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'pSphere1.visibility': [[15.0, 1.0, u'spline', u'step', True, 0.0, 0.0, 1.0, 0.0]], u'pSphere1.scaleZ': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.scaleZ': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.scaleY': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]], u'group5.scaleX': [[15.0, 1.0, u'auto', u'auto', True, 0.0, 0.0, 1.0, 1.0]]}, 'angularUnit': u'deg', 'zzj_non_anim': {u'group4.rotateX': 0.0, u'group4.rotateY': 0.0, u'group4.rotateZ': 0.0, u'group7.visibility': True, u'group8.translateX': 0.0, u'group8.translateY': 0.0, u'group8.translateZ': 0.0, u'group3.translateX': 0.0, u'group6.scaleZ': 1.0, u'group2.rotateZ': 0.0, u'pSphere1.rotateX': 1.2902398693116837, u'group7.scaleY': 1.0, u'group7.scaleX': 1.0, u'group2.rotateX': 0.0, u'group7.scaleZ': 1.0, u'group8.rotateX': 0.0, u'group8.rotateY': 0.0, u'group8.rotateZ': 0.0, u'group1.scaleZ': 1.0, u'group3.rotateZ': 0.0, u'group8.visibility': True, u'group3.rotateX': 0.0, u'group2.scaleZ': 1.0, u'group7.rotateZ': 0.0, u'group7.rotateY': 0.0, u'group7.rotateX': 0.0, u'group1.translateZ': 0.0, u'group1.translateY': 0.0, u'group1.translateX': 0.0, u'group6.translateZ': 0.0, u'group6.translateX': 0.0, u'group6.translateY': 0.0, u'group2.translateZ': 0.0, u'group2.translateX': 0.0, u'group2.translateY': 0.0, u'group1.rotateZ': 0.0, u'group3.rotateY': 0.0, u'group2.scaleX': 1.0, u'group8.scaleX': 1.0, u'group8.scaleY': 1.0, u'group8.scaleZ': 1.0, u'group4.scaleZ': 1.0, u'group3.translateY': 0.0, u'group1.scaleX': 1.0, u'group2.visibility': True, u'group2.scaleY': 1.0, u'group1.scaleY': 1.0, u'group3.visibility': True, u'group3.translateZ': 0.0, u'group4.scaleX': 1.0, u'group4.scaleY': 1.0, u'group4.visibility': True, u'group6.rotateZ': 0.0, u'group6.rotateX': 0.0, u'group6.rotateY': 0.0, u'group6.visibility': True, u'group1.visibility': True, u'group1.rotateY': 0.0, u'group1.rotateX': 0.0, u'group2.rotateY': 0.0, u'group3.scaleY': 1.0, u'group3.scaleX': 1.0, u'group3.scaleZ': 1.0, u'group4.translateX': 0.0, u'group4.translateY': 0.0, u'group4.translateZ': 0.0, u'group6.scaleY': 1.0, u'group7.translateY': 0.0, u'group7.translateX': 0.0, u'group6.scaleX': 1.0, u'group7.translateZ': 0.0}, 'linearUnit': u'cm', 'timeUnit': u'film', 'mayaVersion': u'2012 x64'}
# j.writeFile(r"E:\PTAnimLibrary\b\c.pta",data)       
# j.readFile(r"D:\Pluto\workspace\PlutoPip\MyLib\PPanim\AnimLibrary\test2.json")


