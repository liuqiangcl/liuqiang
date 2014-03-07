#-*-coding:utf-8-*-
'''
Created on 2014-3-4

@author: Hunk
'''
# 
# from sys import argv
# script, input_file = argv
input_file=raw_input("打开文件:")
def print_all(f): #读取文件中内容
    print f.read()
      
      
def rewind(f): #重新定位文件
    f.seek(0)#重新定位在文件的第0位及开始位置 
  
def print_a_line(line_count, f):#统计文件杭州
    print line_count, f.readline()
 
  
current_file = open(input_file) #打开输入文件
print "First let's print the whole file:\n"
  
  
print_all(current_file)#读取文件内容
print "Now let's rewind, kind of like a tape."
  
  
rewind(current_file) 
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)#打印行号读取每行内容
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)




#验证readline是否按行读取文件内容
# file=open("test").readlines()
# print file
# print len(file)
# A=(1,2,3)
# B=len(A)
# print B


# print "???"
# def print_a_line(file):#统计文件杭州
#     for i in range(0,3):
#         print file.readline()
# file=open("test")
# print_a_line(file)
# 
# # file=open("test")
# # for i in range(0,len(file.readlines())):
# #     print file.readline()

