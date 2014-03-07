# -*- coding: UTF-8 -*-
'''
Created on 2014-3-6

@author: Hunk
'''
people=int(raw_input("people is :"))
cars=int(raw_input("cats is:"))
buses =int(raw_input("dogs is:" ))
if cars>people:
    print "We should take the cars."
    
elif cars <people:
    print "We should not take the cars."
    
else:
    print "We can,t decide."
    
if buses > cars:
    print "That's too many buses."
    
elif buses < cars:
    print "Maybe we could take the buses."

else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."

else:
    print "Fine, let's stay home then."
    
#if ... elif ...else if 如果为真执行if下的语句，不为真执行下一个elif判断，最后都不能执行，执行最后一个


if cars> people and cars >buses:
    print "cars biggest"
elif cars>people and cars<buses:
    print "buses biggest"


    
    
    
    