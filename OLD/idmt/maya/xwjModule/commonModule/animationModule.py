__author__ = 'xuweijian'
import maya.cmds as mc
import sqlite3
from idmt.maya.xwjModule.commonModule import fileModule
from idmt.maya.xwjModule.commonModule import commonModule

class animationModule():
    def getAnimCurveDict(self,obj,tStart = 0, tEnd = 0,drvKey=False):
        attrDict={}
        channels = mc.listConnections(obj, t = "animCurve", c = True)
        if channels:
            for i in range(len(channels)/2):
                i=i*2
                keyInfoDict={}
                #keyInfoDict['name']=channels[i]
                keyInfoDict['wt'] = mc.getAttr(channels[i+1] + ".weightedTangents")
                keyInfoDict['preI'] = mc.getAttr(channels[i+1] + ".preInfinity")
                keyInfoDict['postI'] = mc.getAttr(channels[i+1] + ".postInfinity")
                if tStart==0 and tEnd == 0:
                    keys = mc.keyframe(channels[i+1], q = True,keyframeCount=1)
                else:
                    keys = mc.keyframe(channels[i+1], q = True, t = (tStart, tEnd),keyframeCount=1)
                keyList=[]
                j=0
                while(j<=keys-1):
                    detailDict={}
                    if drvKey==0:
                        detailDict['time']=mc.keyframe(channels[i+1],q=1,timeChange=1)[j]
                    else:
                        detailDict['time']=mc.keyframe(channels[i+1],q=1,floatChange=1)[j]
                    detailDict['value']=mc.keyframe(channels[i+1],q=1,valueChange=1)[j]
                    detailDict['inTanType'] = mc.keyTangent(channels[i+1], q = 1, itt = 1)[j]
                    detailDict['outTanType'] = mc.keyTangent(channels[i+1], q = 1, ott = 1)[j]
                    detailDict['tanLock'] = mc.keyTangent(channels[i+1], q = 1, lock = 1)[j]
                    detailDict['inAngle']=mc.keyTangent(channels[i+1],q=1,inAngle=1)[j]
                    detailDict['inWeight']=mc.keyTangent(channels[i+1],q=1,inWeight=1)[j]
                    detailDict['outAngle']=mc.keyTangent(channels[i+1],q=1,outAngle=1)[j]
                    detailDict['outWeight']=mc.keyTangent(channels[i+1],q=1,outWeight=1)[j]
                    j=j+1
                    keyList.append(detailDict)
                keyInfoDict['keyInfo']=keyList
                attrName=channels[i].split('.')[1]
                attrDict[attrName]=keyInfoDict
            return attrDict

    def setAnimCurveDict(self,obj,dict,drvKey=False):
        for attr in dict.keys():
            #attr=key.split('.')[1]
            objAttr=mc.listAttr(obj)
            if attr in objAttr:
                self.deleteAnimation(obj,attr)
                '''
                animNodePreTL = mc.listConnections('%s.%s'%(obj,attr), t = "animCurveTL")
                if animNodePreTL:
                    try:
                        mc.delete(animNodePreTL)[0]
                    except:
                        pass
                animNodePreTA = mc.listConnections('%s.%s'%(obj,attr), t = "animCurveTA")
                print 'animNodePreTA:'
                print animNodePreTA
                if animNodePreTA:
                    try:
                        mc.delete(animNodePreTA)[0]
                    except:
                        pass

                animNodePreTU = mc.listConnections('%s.%s'%(obj,attr), t = "animCurveTU")
                print 'animNodePreTU'
                print animNodePreTU
                if animNodePreTU:
                    try:
                        mc.delete(animNodePreTU)[0]
                    except:
                        pass
                '''


                keyTime=[]
                keyValue=[]
                tanLock=[]
                inTan=[]
                outTan=[]
                inAngle=[]
                outAngle=[]
                inWeight=[]
                outWeight=[]
                wt=dict[attr]['wt']
                preI=dict[attr]['preI']
                postI=dict[attr]['postI']
                keyInfo=dict[attr]['keyInfo']
                for onekey in keyInfo:
                    keyTime.append(float(onekey['time']))
                    #keyTime.append(onekey['key'])
                    keyValue.append(onekey['value'])
                    tanLock.append(onekey['tanLock'])
                    inTan.append(onekey['inTanType'])
                    outTan.append(onekey['outTanType'])
                    inAngle.append(onekey['inAngle'])
                    outAngle.append(onekey['outAngle'])
                    inWeight.append(onekey['inWeight'])
                    outWeight.append(onekey['outWeight'])
                for i in range(len(keyTime)):
                    try:
                        if drvKey:
                            mc.setKeyframe('%s.%s'%(obj,attr), float = keyTime[i], v = keyValue[i])
                        else:
                            mc.setKeyframe('%s.%s'%(obj,attr), time = keyTime[i], v = keyValue[i])
                    except:
                        print 'error in %s.%s setkey'%(obj,attr)

                try:
                    animNode = mc.listConnections('%s.%s'%(obj,attr), t = "animCurve")[0]
                    #move this to the top of import
                    mc.setAttr(animNode + ".weightedTangents", wt)
                    mc.setAttr(animNode + ".preInfinity", preI)
                    mc.setAttr(animNode + ".postInfinity", postI)
                except:
                    print obj+'no animationNode'

                if wt==True:
                    print inAngle
                    print outAngle
                    for j in range(len(keyTime)):
                        try:
                            #in/out tangent type
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, itt = inTan[j], time = (keyTime[j], keyTime[j]))
                            print inTan[j]

                            mc.keyTangent('%s.%s'%(obj,attr), e = True, ott = outTan[j], time = (keyTime[j], keyTime[j]))
                            print outTan[j]

                            mc.keyTangent('%s.%s'%(obj,attr), e = True, lock = 0, time = (keyTime[j], keyTime[j]))
                            print '-----1'
                            #in/out angle
                            print inAngle[j]
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, ia = inAngle[j], time = (keyTime[j], keyTime[j]))

                            print '-----2'
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, oa = outAngle[j], time = (keyTime[j], keyTime[j]))
                            print '-----3'
                            #in/out angle weight
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, iw = inWeight[j], time = (keyTime[j], keyTime[j]))
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, ow = outWeight[j], time = (keyTime[j], keyTime[j]))
                            print '-----4'
                            #apply the lock, make sure the same as txt file
                            mc.keyTangent('%s.%s'%(obj,attr), e = True, lock = tanLock[j], time = (keyTime[j], keyTime[j]))
                            print '-----5'

                        except:
                            print 'error in set %s.%s keyTangent '%(obj,attr)


    def deleteAnimation(self,obj,attr=[],delDrvKey=False):
        if not attr:
            if delDrvKey:
                animNode=mc.listConnections(obj,d=0,t='animCurve')
                if animNode:
                    mc.delete(animNode)
            else:
                animNode=[]
                animNode.append(mc.listConnections(obj,d=0,t='animCurveTL'))
                animNode.append(mc.listConnections(obj,d=0,t='animCurveTA'))
                animNode.append(mc.listConnections(obj,d=0,t='animCurveTU'))
                if animNode:
                    mc.delete(animNode)

        else:
            if delDrvKey:
                animNode=mc.listConnections('%s.%s'%(obj,attr),d=0,t='animCurve')
            else:
                animNode=(mc.listConnections('%s.%s'%(obj,attr),d=0,t='animCurveTL'))
                if animNode:
                    mc.delete(animNode)
                animNode=(mc.listConnections('%s.%s'%(obj,attr),d=0,t='animCurveTA'))
                if animNode:
                    mc.delete(animNode)
                animNode=(mc.listConnections('%s.%s'%(obj,attr),d=0,t='animCurveTU'))
                if animNode:
                    mc.delete(animNode)


    def getMirrorDict(self,dict,mirrorAttr=[]):
        mirrorDict=dict
        if mirrorAttr:
            for key in dict.keys():
                #attrs=key.split('.')[1]
                if key in mirrorAttr:
                    for i in range(len(dict[key]['keyInfo'])):
                        mirrorDict[key]['keyInfo'][i]['value']=dict[key]['keyInfo'][i]['value']*-1
        return mirrorDict



    def putDictInDB(self,obj,dict):
        reload(fileModule)
        filePath=fileModule.fileModule().saveDialog()
        #nodes=dict.keys()
        #obj=nodes[0].split('_')[0]
        sqlCmmd='create table if not exists ' + obj +  '(nodename varchar(20),attrname varchar(20),wt int,preI int,postI int,time int,value DOUBLE,itt varchar(10),ott varchar(10),tl int,ia DOUBLE,iw DOUBLE,oa DOUBLE,ow DOUBLE)'
        #sqlCmmd='create table if not exists ' + obj +  '(id int,nodename varchar(20),attrname varchar(20),wt int,preI int,postI int)'
        import sqlite3
        con = sqlite3.connect(filePath)
        cu=con.cursor()
        cu.execute("drop table if exists "+ obj)
        cu.execute(sqlCmmd)
        nodes=dict.keys()
        for node in nodes:
            i=0
            while i<= len(dict[node]['keyInfo'])-1:
                #sqlCmmd='insert into ' + obj + ' values (1,2,3,4,5,6)'

                sqlCmmd='insert into ' + obj + ' values ("'+str(node)+'","'+str(dict[node]['name'])+'","'+str(int(dict[node]['wt']))+'","'+str(dict[node]['preI'])+'","'+str(dict[node]['postI'])+'","'+str(dict[node]['keyInfo'][i]['time'])+'","'+str(dict[node]['keyInfo'][i]['value'])+'","'+str(dict[node]['keyInfo'][i]['inTanType'])+'","'+str(dict[node]['keyInfo'][i]['outTanType'])+'","'+str(int(dict[node]['keyInfo'][i]['tanLock']))+'","'+str(dict[node]['keyInfo'][i]['inAngle'])+'","'+str(dict[node]['keyInfo'][i]['inWeight'])+'","'+str(dict[node]['keyInfo'][i]['outAngle'])+'","'+str(dict[node]['keyInfo'][i]['outWeight'])+'")'
                #sqlCmmd='insert into ' + obj + ' values ('+str(i)+',1,2,'+str(dict[node]['wt'])+','+str(dict[node]['preI'])+','+str(dict[node]['postI'])+')'

                print sqlCmmd
                cu.execute(sqlCmmd)
                i=i+1
        con.commit()


    def getAnimCurveDB(self,objs,tStart = 0, tEnd = 0):
        if objs !=[]:
            reload(fileModule)
            filePath=fileModule.fileModule().saveDialog()
            con = sqlite3.connect(filePath)
            cu=con.cursor()
            for obj in objs:
                characterName=commonModule.commonModule().divNamespace(obj,0)
                characterName=characterName[0:-1]
                if characterName=='':
                    characterName='defalut'
                print characterName
                sqlCreatCmmd='create table if not exists ' + characterName +  '(objname varchar(20),nodename varchar(20),attrname varchar(20),wt int,preI int,postI int,time int,value DOUBLE,itt varchar(10),ott varchar(10),tl int,ia DOUBLE,iw DOUBLE,oa DOUBLE,ow DOUBLE)'
                #cu.execute("drop table if exists "+ characterName)
                cu.execute(sqlCreatCmmd)
                channels = mc.listConnections(obj, t = "animCurve", c = True)
                if channels != None:

                    strSqlB=''

                    for i in range(len(channels)/2):
                        i=i*2
                        attrname=channels[i].split('.')[-1]
                        weightedTangents = mc.getAttr(channels[i+1] + ".weightedTangents")
                        preInfinity = mc.getAttr(channels[i+1] + ".preInfinity")
                        postInfinity = mc.getAttr(channels[i+1] + ".postInfinity")
                        if tStart==0 and tEnd == 0:
                            keys = mc.keyframe(channels[i+1], q = True,keyframeCount=1)
                        else:
                            keys = mc.keyframe(channels[i+1], q = True, t = (tStart, tEnd),keyframeCount=1)
                        j=0
                        strSqlB='"'+obj+'","' + channels[i+1] + '","' +attrname+'","'+str(int(weightedTangents))+'","'+str(preInfinity)+'","'+str(postInfinity)
                        print 'strSqlB:'+strSqlB
                        if keys!=None or keys!=[]:
                            try:
                                while(j<=keys-1):
                                    strSqlD=''
                                    print 'node:'+ channels[i+1]
                                    print j
                                    timeChange=mc.keyframe(channels[i+1],q=1,timeChange=1)[j]
                                    valueChange=mc.keyframe(channels[i+1],q=1,valueChange=1)[j]
                                    inTanType = mc.keyTangent(channels[i+1], q = 1, itt = 1)[j]
                                    outTanType = mc.keyTangent(channels[i+1], q = 1, ott = 1)[j]
                                    tanLock = mc.keyTangent(channels[i+1], q = 1, lock = 1)[j]
                                    inAngle=mc.keyTangent(channels[i+1],q=1,inAngle=1)[j]
                                    inWeight=mc.keyTangent(channels[i+1],q=1,inWeight=1)[j]
                                    outAngle=mc.keyTangent(channels[i+1],q=1,outAngle=1)[j]
                                    outWeight=mc.keyTangent(channels[i+1],q=1,outWeight=1)[j]
                                    j=j+1
                                    strSqlD=strSqlB+'","'+str(timeChange)+'","'+str(valueChange)+'","'+inTanType+'","'+outTanType+'","'+str(int(tanLock))+'","'+str(inAngle)
                                    strSqlD=strSqlD+'","'+str(inWeight)+'","'+str(outAngle)+'","'+str(outWeight)+'"'
                                    sqlCmmd='insert into ' + characterName + ' values('+strSqlD+')'
                                    print sqlCmmd
                                    cu.execute(sqlCmmd)
                            except:
                                pass
            con.commit()
            con.close()

    def setAnimCurveDB(self,obj,dbpath=''):
        con = sqlite3.connect('D:/project/test_Project/data/test.db')
        cu=con.cursor()
        cu.execute('SELECT * FROM defalut where objname="'+obj+'"')
        arrs= cu.fetchall()
        con.close()
        mc.setKeyframe(arrs[0][0]+'.'+arrs[0][2],time=arrs[0][6],value=arrs[0][7])
        print 'here'
        mc.setAttr(arrs[0][1]+".weightedTangents",arrs[0][3])
        mc.setAttr(arrs[0][1]+".preInfinity",arrs[0][4])
        mc.setAttr(arrs[0][1]+".postInfinity",arrs[0][5])
        i=0
        while i<=len(arrs)-1:
            name=arrs[i][0]
            node=arrs[i][1]
            att=arrs[i][2]
            #wt=arrs[i][3]
            #preI=arrs[i][4]
            #postI=arrs[i][5]
            time=arrs[i][6]
            value=arrs[i][7]
            itt=arrs[i][8]
            ott=arrs[i][9]
            tl=arrs[i][10]
            ia=arrs[i][11]
            iw=arrs[i][12]
            oa=arrs[i][13]
            ow=arrs[i][14]
            mc.setKeyframe(name+'.'+att,time=time,value=value)
            mc.keyTangent(node,itt=itt,ott=ott,lock=tl,inAngle=ia,inWeight=iw,outAngle=oa,outWeight=ow)
            i=i+1

