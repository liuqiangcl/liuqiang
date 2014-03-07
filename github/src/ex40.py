#-*-coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
class song():
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self): 
        """对变量进行循环"""
        for line in self.lyrics:
            print line
#新建两个实例            
happy_bday = song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = song(["They rally around the family",
"With pockets full of shells"])

#实例调用函数sing_me_a_song
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
