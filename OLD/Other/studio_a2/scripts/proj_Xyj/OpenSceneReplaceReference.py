#-*- coding: utf-8 -*-
'''
Created on 2013-10-23
@contact:    power_zzj@163.com
@deffield    updated: Updated
@author: zhaozhongjie
'''
import os,sys
sys.path.append(r'//file-cluster/GDC/Resource/Support/Maya/Python')
import xlrd                             #    读取excel文件内容的包
import maya.cmds as cmds

class MyClass():
    '''
    classdocs
    '''
    print 'xxxxxxxxxxxxxxxxxxxxxxx'
    __FILE =__file__
    __EXCEL = 'OpenSceneReplaceReference.xls'                                       #    如果在excel文件和py文件在同一目录下，excel对应的名称。
    __EXCEL_FULL = os.path.join(os.path.split(__FILE)[0] , __EXCEL)           #    excel文件的绝对路径。
    #__EXCEL_FULL = r'd:\abc.xls'                                                                #    你也可以手动指定excel文件的绝对路径。
    
    __LIST = []                     #    任务清单

    def __init__(self):
        '''
            使用xlrd查询excel文件，生成任务清单
        '''
        data = self.open_excel()                       #     读excel文件
        table = data.sheets()[0]
        nrows = table.nrows                                          #    行数
        ncols = table.ncols                                            #    列数
        
        if nrows<3:
            print "数据错误"
            return
        
        for i in range( 2 , nrows):
            content =  table.row_values( i )                   #    某一行数据 
            self.__LIST.append( content)                        #    生成任务清单
        
        self.MyReplaceReference()                              #    执行任务清单
        

#     函数：---读excel文件----------------------------------------------------------------------
    def open_excel(self , file = __EXCEL_FULL):                                         
        try:
            data = xlrd.open_workbook( file )
            return data
        except Exception , e :
            print str(e)
            
#     函数：---执行任务清单----------------------------------------------------------------------
    def MyReplaceReference(self ):      
        fileName = cmds.file(q=1,sn=1)                       
        for a in self.__LIST:
            sure_key = a[0].split(';')                     #    1.    必须有的关键字
            choice_key = a[1].split(';')                 #    2.    选择性的关键字
            unless_key = a[2].split(';')                  #    3.    排除掉的关键字
            old_name = a[3]                   #    旧的参考名称
            new_name = a[4]                  #    替换参考名称
            new_reference = a[5]            #    替换参考的路径
            
            Condition1 = 1                               #    1.    判断是否包含关键字
            for x in sure_key:
                if x not in fileName:
                    Condition1 = 0
                    break
            
            Condition2 = 0                               #    2.    判断是否找到多选的关键字
            if choice_key ==['']:
                Condition2 = 1
            else:
                for x in choice_key:
                    if x in fileName:
                        Condition2 = 1
                        break     
            
            Condition3 = 0                                #    3.    判断是否找到排除的关键字
            if unless_key ==['']:
                Condition3 = 0
            else:            
                for x in unless_key:
                    if x in fileName:
                        Condition3 = 1
                        break

#===================================================================================================
#     如果满足 1 , 2 , 3 条条件，则开始替换参考：
#===================================================================================================
            if Condition1 ==1 and Condition2 ==1 and Condition3 == 0:       
                references = cmds.file(q=1,r=1)
                
                for r in references:
                    if old_name in r:
                        self.MyReplaceReferenceAndFixNameSapce( r, new_name , new_reference)
            
#     函数：---替换参考并修正NameSpace----------------------------------------------------------------------                        
    def MyReplaceReferenceAndFixNameSapce(self , r , new_name , new_reference ):      
#    1.    替换参考
        rfn = cmds.file( r , q=1 , rfn = 1)                                     #    求rfn节点的名字
        if os.path.exists(new_reference):                                     #    这个文件前期还没出完，所以要判断一下。也有可能这个目标文件根本不存在
            cmds.file(new_reference , loadReference = rfn )       
            
#    2.    修正namespace            
        cmds.namespace(setNamespace =":")
        for i in range(100):
            ns = new_name+"_" + str(i)
            if cmds.namespace(exists=ns):    continue
            else:
                newR = cmds.referenceQuery(rfn,filename = 1)
                cmds.file(newR , edit=1 , namespace = ns )
                
                cmds.lockNode( rfn , lock =0, )                                                       #    解锁
                newRFN = new_name + "_" + str(i) + "RN"                                    #    新rfn名字
                if cmds.objExists(newRFN) :   newRFN+= "1"                                 #    判断如果存在这个名字，自动在后面加“1”   
                if cmds.objExists(newRFN) :   newRFN+= "1"                                 #    重复上面的操作，确保万无一失
                cmds.rename( rfn , newRFN)                                                           #   重命名
                cmds.lockNode(newRFN,lock=1, )                                                  #   上锁
                
                break
        cmds.namespace(setNamespace =":")




        
if __name__ == '__main__':    
    MyClass()
    pass

