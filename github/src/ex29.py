#-*-coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
# people =20
# cats = 30
# dogs = 15
people=int(raw_input("people is :"))
cats=int(raw_input("cats is:"))
dogs =int(raw_input("dogs is:" ))

if people < cats:
    print "Too many cats! The world is doomed!"
if people >cats:
    print "Not many cats! The world is saved!"
if people <dogs:
    print "The world is drooled on!"
if people >dogs:
    print "The world is dry!"
dogs +=5 #等价dogs=dogs+5

if people>=dogs:
    print "People are greater than or equal to dogs"
if people <=dogs:
    print "People are less than or equal to dogs."
if people == dogs:
    print "People are dogs."


print "*" * 30
#采用if进行判断
#缩进为语法要求
#不缩进，语法报错提示"IndentationError: expected an indented block"
# if True and True:
#     print True
