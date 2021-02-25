import maya.cmds as cmds
import os as os
def edo_imSelectDrivenKeyData():
    filename=cmds.fileDialog2(ds=1,fm=1)[0]
    edo_imDirvenKeyData(filename)

def edo_exSelectDrivenKeyData():
    path=cmds.fileDialog2(ds=1,fm=2)
    if path==None:
        return False
    path=path[0]
    sels=cmds.ls(sl=1)
    for sel in sels:
        #sel=sels[0]
        edo_exDirvenKeyData(sel,path)


def edo_imDirvenKeyData(filename='d:/setDrivenKeyData'):
    if not os.path.exists(filename):
        return False
    fobj=open(filename,'r')
    t=fobj.readline()
    while not t=='//theEnd':
        t=fobj.readline()
        if t=='//theEnd':
            print 'over!'
            break;
        tmp=t.split(':')
        driver=tmp[0]
        driverKey=tmp[1]
        drivens=tmp[2][:-1].split(',')
        if not cmds.objExists(driverKey):
            if 'Rt_' in driverKey:
                if cmds.objExists(driverKey.replace('Rt_','Lf_')):
                    cmds.duplicate(driverKey.replace('Rt_','Lf_'),n=driverKey)
            if 'Lf_' in driverKey:
                if cmds.objExists(driverKey.replace('Lf_','Rt_')):
                    cmds.duplicate(driverKey.replace('Lf_','Rt_'),n=driverKey)
        if cmds.objExists(driver) and  cmds.objExists(driverKey):
            try:
                cmds.connectAttr(driver,driverKey+'.input')
            except:
                print 'pase connection'
            for driven in drivens:
                #driven=drivens[0]
                driven=driven.replace('\r','').replace('\n','')
                if cmds.objExists(driven):
                    try:
                        cmds.connectAttr(driverKey+'.output',driven)
                    except:
                        print 'pass connection'
    fobj.close()

#edo_exDirvenKeyData('Lf_leg_drv_jnt_FRAME',path='d:/setDrivenKeyData')
def edo_exDirvenKeyData(driver,path='d:/setDrivenKeyData'):
	#driver='Lf_leg_drv_jnt_FRAME'
	kattrs=cmds.listAttr(driver,k=1)
	if kattrs==None:
	   print 'have no keyable attribute!'
	   return False
	if not os.path.isdir(path):
		os.mkdir(path)
	filename=path+'/'+driver+'.drk'
	fobj=open(filename,'w')
	fobj.writelines('//this file is  '+driver+'  setDrivenKey data!\n')
	for attr in kattrs:
		#attr=kattrs[7]
		print attr
		outputs=cmds.listConnections(driver+'.'+attr,s=0,d=1,p=1)
		if outputs==None:
			continue
		for output in outputs:
			#output=outputs[0]
			print output
			wtl=driver+'.'+attr+':'
			nodename=output.split('.')[0]
			ac=cmds.ls(nodename,type='animCurve')
			if ac==None or ac==[]:
				continue
			ac=ac[0]
			wtl+=ac+':'
			acoutputs=cmds.listConnections(ac+'.output',s=0,d=1,p=1)
			if acoutputs==None:
				continue
			acoutput=edo_convertListToStr(acoutputs)
			wtl+=acoutput
			fobj.writelines(wtl+'\n')
	fobj.writelines('//theEnd')   
	fobj.close()

def edo_convertListToStr(list):
    s=''
    for l in list:
        s+=l+','
    s=s[:-1]
    return s