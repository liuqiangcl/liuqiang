# -*- coding: UTF-8 -*-
'''
Created on 2014-3-5

@author: Hunk
'''
#1
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
#修改完成验证
#print break_words("a b c")
#2 
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
#修改完成验证
#print sort_words("hgaec") 
#3 
def print_first_word(words): #丢失最后的:号
    """Prints the first word after popping it off."""
    word = words.pop(0)  #删除list元素的函数多了一个o
    print word
#list_words=["a","b","c","d"]    
#print_first_word(list_words) #猜想结果为a，待验证。。。。。
#4
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)#丢失(半个括号
    print word
list_words=["a","b","c","d"]  
#print_last_word(list_words)
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
sentence = "All good things come to those who wait."
# sort_sentence(sentence) 
# a=sort_sentence(sentence)
# print a
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
  
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
  
 
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
 
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion\n
\t\t where there is none.
"""
 
 
print "--------------"
print poem
print "--------------"
 
five = 10 - 2 + 3 - 5
print "This should be five: %s" % five
 
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000 #除号的方向反了，变更为/
    crates = jars / 100
    return jelly_beans, jars, crates
 
 
start_point = 10000
beans,jars,crates = secret_formula(start_point)#变量上线不服，中间的横线非- ,不是==而是赋值=
 
print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)
 
start_point = start_point / 10
 
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)#丢失括号，参数的也错误丢失i正确为start_piont
 
sentence = "All god\tthings come to those who weight."
'''执行函数根据自己的编译器做了调整''' 
words = break_words(sentence)
sorted_words = sort_words(words)
print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words =sort_sentence(sentence)
print sorted_words #打印丢失t
print_first_and_last(sentence)#函数写错了
print_first_and_last_sorted(sentence) #函数和参数均错误了


