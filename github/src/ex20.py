#-*-coding:utf-8-*-
'''
Created on 2014-3-4

@author: Hunk
'''
# 
# from sys import argv
# script, input_file = argv
input_file=raw_input("���ļ�:")
def print_all(f): #��ȡ�ļ�������
    print f.read()
      
      
def rewind(f): #���¶�λ�ļ�
    f.seek(0)#���¶�λ���ļ��ĵ�0λ����ʼλ�� 
  
def print_a_line(line_count, f):#ͳ���ļ�����
    print line_count, f.readline()
 
  
current_file = open(input_file) #�������ļ�
print "First let's print the whole file:\n"
  
  
print_all(current_file)#��ȡ�ļ�����
print "Now let's rewind, kind of like a tape."
  
  
rewind(current_file) 
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)#��ӡ�кŶ�ȡÿ������
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)




#��֤readline�Ƿ��ж�ȡ�ļ�����
# file=open("test").readlines()
# print file
# print len(file)
# A=(1,2,3)
# B=len(A)
# print B


# print "???"
# def print_a_line(file):#ͳ���ļ�����
#     for i in range(0,3):
#         print file.readline()
# file=open("test")
# print_a_line(file)
# 
# # file=open("test")
# # for i in range(0,len(file.readlines())):
# #     print file.readline()

