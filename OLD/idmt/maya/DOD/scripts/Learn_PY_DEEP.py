#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
【功能】
 演示Python中命令行参数的获取和解析：
【整理】Python中如何获得并处理命令行参数
http://www.crifan.com/python_capture_and_parse_command_line_parameter

【作者】 Crifan Li
【版本】 2012-11-15

"""

#sys模块中包含了相关的，获得命令参数的功能
import sys;

#optparse是一个用于解析命令行输出参数的模块
import optparse;
#不过，该模块自动Python 2.7往后就废弃了，而推荐使用argparse：
#Deprecated since version 2.7: The optparse module is deprecated and will not be developed further; development will continue with the argparse module.


import argparse;

def cmdParaDemo():
    # 1. 演示sys.argv所获得的命令行中的输入的所有的内容
    print "The whole string you input can get from sys.argv=",sys.argv;
    argvLen = len(sys.argv);
    print "total fileds in sys.argv=",argvLen;
    
    for i,eachArg in enumerate(sys.argv):
        print "[%d]=%s"%(i, eachArg);
    
    # 2. 演示optparse的用法
    oldParser = optparse.OptionParser();
    oldParser.add_option("-u","--username",action="store", type="string",dest="username_optparse",help="Your user name");
    oldParser.add_option("-a","--age",action="store", type="int",dest="age_optparse",help="Your age");
    
    (options, args) = oldParser.parse_args();
    #此处用于导出所获得的变量
    #如果没有导出变量，则后面代码中，如果用到此处定义的参数所对应的变量时，就会报错，说找不到相关的变量
    #NameError: global name 'username_optparse' is not defined
    for i in dir(options):
        exec(i + " = options." + i);
    
    print "optparse: Your input username_optparse=%s, type(username_optparse)=%s, age_optparse=%d, type(age_optparse)=%s"%(username_optparse, type(username_optparse), age_optparse, type(age_optparse));
    
    # 3. 演示argparse的用法
    newParser = argparse.ArgumentParser();
    newParser.add_argument("-u", "--username", dest="username_argparse", help="Your user name");
    newParser.add_argument("-a", "--age", type=int, dest="age_argparse", help="Your age");
    args = newParser.parse_args();

    #后面，如果想要使用变量，则可以：
    #args.username_argparse
    #args.age_argparse
    #的方式引用
    
    print "args=",args; #args= Namespace(age_argparse=1000, username_argparse='crifanLi')
    print "type(args)=",type(args); #type(args)= <class 'argparse.Namespace'>
    
    argsDict = args.__dict__;
    print "parsed argsDict=",argsDict; #parsed argsDict= {'age_argparse': 1000, 'username_argparse': 'crifanLi'}
    
    # for eachArg in argsDict.keys():
        # exec(eachArg + " = " + argsDict[eachArg]); # -> TypeError: cannot concatenate 'str' and 'int' objects
    
    # for eachArg in argsDict.keys():
        # if(type(argsDict[eachArg]) != "<type 'string'>"):
            # exec(eachArg + " = " + str(argsDict[eachArg])); # -> NameError: name 'crifanLi' is not defined
        # else:
            # exec(eachArg + " = " + argsDict[eachArg]);

    #此处用于导出所获得的变量
    #（1）如果没有导出变量，则后面代码中:
    #如果用到此处定义的参数所对应的变量时，就会报错，说找不到相关的变量
    #NameError: global name 'username_optparse' is not defined
    #（2）而导出之后，后面就可以直接通过参数名：
    #username_argparse
    #age_argparse
    #的方式引用参数了。
    for eachArg in argsDict.keys():
        exec(eachArg + " = args." + eachArg);
    
    print "argparse: Your input username_argparse=%s, type(username_argparse)=%s, age_argparse=%d, type(age_argparse)=%s"%(username_argparse, type(username_argparse), age_argparse, type(age_argparse));

###############################################################################
if __name__=="__main__":
    cmdParaDemo();