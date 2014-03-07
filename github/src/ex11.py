#-*- coding:utf-8-*-
'''
Created on 2014-2-27

@author: Hunk
'''
'''
print "How old are you ?",
age=raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh ?"
weight =raw_input()
print "So , you're %r old ,%r tall and %r heavy." %(age,height,weight)
#格式化字符串与实际参数不符合
#TypeError: not all arguments converted during string formatting
#raw_input 实现数据输入
print "*"*10
print "waht's your name ?",
name=raw_input()
print "How are you ?"
Greeting=raw_input()
print "I'm %r,How do you do  %r ,Thank you !" %(name,Greeting)

print "input 实现输入"

Greeting=input("输入问候语:\n")
print Greeting #input([prompt]) -> value
'''
Num = raw_input("6'2")# 括号中是打印的提示信息
# import os   
# value=raw_input("请输入一个值:")
# abc=os.system(111)
# print abc

