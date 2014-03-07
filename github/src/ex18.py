#-*-coding:utf-8-*-
'''
Created on 2014-3-3

@author: Hunk
'''
#this one is like your scripts with argv
def print_two(*args): #*args 代表多个参数
#def funcation(): #定义函数  
    arg1,arg2=args
    print "arg1:%r,arg2:%r" %(arg1,arg2)
#ok,that *args is actually pointless,we can just do this
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r" %(arg1,arg2)
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
# this one takes no arguments
def print_none():
    print "I got nothin'."