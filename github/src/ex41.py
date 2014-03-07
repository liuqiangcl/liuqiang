#-*-coding:utf-8-*-
'''
Created on 2014-3-7

@author: Hunk
'''
class TheThing(object):
    def __init__(self):
        """定义变量number赋值0"""
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        
        self.number += more  #number=number+more
        return self.number
# two different things
#申请两个实例，调用函数some_function
a = TheThing()
b = TheThing()
a.some_function()
b.some_function()

print a.add_me_up(20)
print b.add_me_up(30)
# print a.number
# print b.number
# Study this. This is how you pass a variable
# from one class to another. You will need this.
class TheMultiplier(object):
    def __init__(self, base):
        """定义变量self.base赋值base"""
        self.base = base
    def do_it(self, m):
        #返回m和base的积
        return m * self.base


x = TheMultiplier(a.number)
print x.do_it(b.number)
"""
__dict__()#显示的是a这个实例的属性
"""