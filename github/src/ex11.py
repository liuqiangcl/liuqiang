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
#��ʽ���ַ�����ʵ�ʲ���������
#TypeError: not all arguments converted during string formatting
#raw_input ʵ����������
print "*"*10
print "waht's your name ?",
name=raw_input()
print "How are you ?"
Greeting=raw_input()
print "I'm %r,How do you do  %r ,Thank you !" %(name,Greeting)

print "input ʵ������"

Greeting=input("�����ʺ���:\n")
print Greeting #input([prompt]) -> value
'''
Num = raw_input("6'2")# �������Ǵ�ӡ����ʾ��Ϣ
# import os   
# value=raw_input("������һ��ֵ:")
# abc=os.system(111)
# print abc

