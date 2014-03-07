#-*-coding:utf-8-*-
'''
Created on 2014-3-5

@author: Hunk
'''
def break_words(stuff):
    """this function will break up words for us."""
    words=stuff.split(' ')#通过字符串对象的split方法切割字符串对象为列表
    return words
''' 
"""验证split的作用"""
a="a,b,c,d,e,f"
print a.split(",")
'''
def sort_words(words):
    """ sorts the words"""
    return sorted(words)#排序
'''
"""对字符串进行排序形成list"""
print sorted("khd")
'''
def print_first_word(words):
    """Prints the first word after popping it off."""
    words=words.pop(0) #删除指定位置元素
    print words#打印删除的元素

def print_last_word(words):
    """Prints the last word after popping it off."""
    words = words.pop(-1)
    print words#打印删除的元素
"""pop 默认从最后开始删除，pop(n) ,n代表删除的位置"""


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)#对字符串进行分割
    print_first_word(words)#删除第一个元素
    print_last_word(words)#删除最后一个元素

#先排序进行删除元素
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
print "*" * 30
sentence = "All good things come to those who wait."
print break_words(sentence)
words=sort_words(sentence)
#以函数为参数进行调用
print_first_word(break_words(sentence))
print_last_word(break_words(sentence))
#1  
print sort_sentence(sentence)#首先对字符串切割成为list，然再次进行排序
  
#2  
print_first_and_last(sentence)

#3 
print_first_and_last_sorted(sentence)

'''定义函数时放在'"""' 之间的东西 被称作 documentation comments (文档注解)'''
help(sort_sentence)
