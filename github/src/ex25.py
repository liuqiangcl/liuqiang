#-*-coding:utf-8-*-
'''
Created on 2014-3-5

@author: Hunk
'''
def break_words(stuff):
    """this function will break up words for us."""
    words=stuff.split(' ')#ͨ���ַ��������split�����и��ַ�������Ϊ�б�
    return words
''' 
"""��֤split������"""
a="a,b,c,d,e,f"
print a.split(",")
'''
def sort_words(words):
    """ sorts the words"""
    return sorted(words)#����
'''
"""���ַ������������γ�list"""
print sorted("khd")
'''
def print_first_word(words):
    """Prints the first word after popping it off."""
    words=words.pop(0) #ɾ��ָ��λ��Ԫ��
    print words#��ӡɾ����Ԫ��

def print_last_word(words):
    """Prints the last word after popping it off."""
    words = words.pop(-1)
    print words#��ӡɾ����Ԫ��
"""pop Ĭ�ϴ����ʼɾ����pop(n) ,n����ɾ����λ��"""


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)#���ַ������зָ�
    print_first_word(words)#ɾ����һ��Ԫ��
    print_last_word(words)#ɾ�����һ��Ԫ��

#���������ɾ��Ԫ��
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
    
    
print "*" * 30
sentence = "All good things come to those who wait."
print break_words(sentence)
words=sort_words(sentence)
#�Ժ���Ϊ�������е���
print_first_word(break_words(sentence))
print_last_word(break_words(sentence))
#1  
print sort_sentence(sentence)#���ȶ��ַ����и��Ϊlist��Ȼ�ٴν�������
  
#2  
print_first_and_last(sentence)

#3 
print_first_and_last_sorted(sentence)

'''���庯��ʱ����'"""' ֮��Ķ��� ������ documentation comments (�ĵ�ע��)'''
help(sort_sentence)
