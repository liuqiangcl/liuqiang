#-*-coding:utf-8-*-
'''
Created on 2014-3-3

@author: Hunk
'''
from_file=raw_input("请输入拷贝的文件名称：") #定义拷贝文件
to_file=raw_input("请输入拷贝到的文件名称：")#定义拷贝到的文件
# from sys import argv
from os.path import exists#导入函数exists
#script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)#说明由什么地方拷贝到什么地方
# we could do these two on one line too, how?
in_file = open(from_file)#打开文件
indata = in_file.read()#读取文件中内容
print "The input file is %d bytes long" % len(indata)#获取文件内容的长度
print "Does the output file exist? %r" % exists(to_file)#判断拷贝到的文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort." #敲击回车继续，Ctrl+C中断
raw_input()
out_file = open(to_file,'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()#关闭文件
in_file.close()
