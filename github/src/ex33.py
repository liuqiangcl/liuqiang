#-*- coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
# i = 0
# numbers=[]
# #创建列表
# while i<6:
#     print "At the top i is %d " % i
#     numbers.append(i)
#     i+=1
#     print "Numbers now:",numbers
#     print "At the bottom i is %d" % i
# #对列表循环
# print "The numbers:"
# for num in numbers:
#     print num
#     
#     
def create_list(num):
    i=0
    numbers=[]
    while i<num:
            #print "At the top i is %d " % i
            numbers.append(i)
            i+=1
    print "Numbers now:",numbers
for i in range(0,10):
    create_list(i)