#-*-coding:utf-8-*-
'''
Created on 2014-3-3

@author: Hunk
'''
# from sys import argv
# acript,filename=argv
#����Eclipse �޷�ʹ�������в���argv����ת��Ϊraw_input
filename=raw_input("�������ļ�����\n")
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target =open(filename,"w")#(�ļ����ƣ�ģʽ��д)
print "Truncating the file. goodbye!"
#target.truncate(4)# truncate(n):  ���ļ����������ַ���ʼ�ضϣ��ض��ļ�Ϊn���ַ�����n��ʾ�ӵ�ǰλ����ضϣ��ض�֮��n����������ַ���ɾ����
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



