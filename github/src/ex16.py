#-*-coding:utf-8-*-
'''
Created on 2014-3-3

@author: Hunk
'''
# from sys import argv
# acript,filename=argv
#由于Eclipse 无法使用命令行参数argv所以转换为raw_input
filename=raw_input("请输入文件名：\n")
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target =open(filename,"w")#(文件名称，模式：写)
print "Truncating the file. goodbye!"
#target.truncate(4)# truncate(n):  从文件的首行首字符开始截断，截断文件为n个字符；无n表示从当前位置起截断；截断之后n后面的所有字符被删除。
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1:")
line2 = raw_input("line 2:")
line3 = raw_input("line 3:")
print "I'm going to wirte these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally,we close it."
target.close()



