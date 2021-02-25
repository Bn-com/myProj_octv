__author__ = 'xuweijian'

class commonModule():
    def divNamespace(self,obj,arg=False):
        objName=''
        if arg==0:
            namearr=obj.split(':')[0:-1]
            if len(namearr)>0:
                for i in range(len(namearr)):
                    objName=objName+namearr[i]+":"
        elif arg==1:
            objName=obj.split(':')[-1]
        return objName