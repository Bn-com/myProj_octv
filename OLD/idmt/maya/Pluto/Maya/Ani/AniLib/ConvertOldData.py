#-*- coding: utf-8 -*-
'''
Created on 2014年9月22日

@author: zhaozhongjie
'''
import json
import os

def convert(path,):
    
    rv = {
            "angularUnit": "degree", 
            "linearUnit": "centimeter", 
            "mayaVersion": "2012", 
            "timeUnit": "pal", 
            "zzj_anim": {}, 
            "zzj_non_anim": {}
        }
    with open(path, "r") as f:
        while True:
            line = f.readline().strip('\n')
            
            animName = '' 
            animValue = []            
            
            if line:
                if line[-1]==';':           line = line[:-1]                            #    去除最后一个";"
                if 'mayaVersion' in line:   rv['mayaVersion'] = line.split(' ')[-1]     #    mayaVersion
                elif 'linearUnit' in line:   rv['linearUnit'] = line.split(' ')[-1]     #    linearUnit
                elif 'angularUnit' in line:   rv['angularUnit'] = line.split(' ')[-1]   #    angularUnit
                elif 'timeUnit' in line:   rv['timeUnit'] = line.split(' ')[-1]         #    angularUnit
                 
                elif 'non-anim' in line:
                    name,value = line.split(' ')[1].split('\t')
                    aaa=''
                    cmd = 'aaa='+value
                    try:
                        exec(cmd)
                        rv['zzj_non_anim'][name]=aaa
                    except:
                        rv['zzj_non_anim'][name]=0
                    
                
                if line[:4] == 'anim':
                    animName = line.split(' ')[1]
                    
                    while True:
                        l = f.readline().strip('\n')
                        if '{' in l:
                            animValue = []
                            continue
                        elif '}' in l:
                            rv['zzj_anim'][animName] = []
                            frame=value=curveTypeI=curveTypeO=ifWeight=curveIV=curveOV=weightA=weightB = None
                            for a in animValue:
                                exec('frame = ' + a[0])
                                exec('value = ' + a[1])
                                exec('curveTypeI = "' + a[2]+'"')
                                exec('curveTypeO = "' + a[3]+'"')
                                exec('ifWeight = ' + a[4])
                                
                                if len(a) > 6:
                                    exec('curveIV = ' + a[5])
                                    exec('curveOV = ' + a[6])
                                if len(a) == 9:
                                    exec('weightA = ' + a[7])
                                    exec('weightB = ' + a[8])
                                rv['zzj_anim'][animName].append([frame,value,curveTypeI,curveTypeO,ifWeight,curveIV,curveOV,weightA,weightB])                                
                            
                            break
                        l = l.split('\t')[1]
                        if l[-1]==';':           l = l[:-1] 
                        animValue.append(l.split(' '))
            else:
                break
    newPath = path[:-4]+'.pta'
    mj = MyJesonRW()
    mj.writeFile(newPath, rv)

class MyJesonRW(json.JSONEncoder):
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
        return super(MyJesonRW, self)._iterencode(o, markers)
    
    def printData(self,json_data):
        print "----non_anim----"
        for a in json_data["zzj_non_anim"].keys():
            print a, json_data["zzj_non_anim"][a]
         
        print "----anim----"
        for a in json_data["zzj_anim"].keys():
            print a
            for b in json_data["zzj_anim"][a]:
                print b
                print type(b[4])
    
    def readFile(self,path):
        with open(path, "r") as f:
            json_data = json.loads(f.read()) 
            print json_data
    
    def writeFile(self,path,json_data):
        with open(path, "w") as f:
            json.dump(json_data,f,indent=4,sort_keys=True, cls=MyJesonRW)
            f.close()
    

def walk(path):
    for f in os.listdir(path):
        ff=os.path.join(path,f)
        
        if os.path.isfile(ff) :
            if os.path.splitext(ff)[1]=='.sla':
                print ff
                try:
                    convert(ff)
                except:
                    return
        else:
            pass
            walk(ff)


# convert(r'd:\FastRun.sla')    
# walk(u'Z:\\Projects\\YODA\\YODA_Scratch\\Animation\\动作库')
# walk(u'Z:\\Projects\\ShunLiu\\ShunLiu_Scratch\\Animation')

    