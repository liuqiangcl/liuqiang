#-*-coding:utf-8-*-
'''
Created on 2014-3-7

@author: Hunk
'''
class TheThing(object):
    def __init__(self):
        """�������number��ֵ0"""
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        
        self.number += more  #number=number+more
        return self.number
# two different things
#��������ʵ�������ú���some_function
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
        """�������self.base��ֵbase"""
        self.base = base
    def do_it(self, m):
        #����m��base�Ļ�
        return m * self.base


x = TheMultiplier(a.number)
print x.do_it(b.number)
"""
__dict__()#��ʾ����a���ʵ��������
"""