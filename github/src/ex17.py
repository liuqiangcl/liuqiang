#-*-coding:utf-8-*-
'''
Created on 2014-3-3

@author: Hunk
'''
from_file=raw_input("�����뿽�����ļ����ƣ�") #���忽���ļ�
to_file=raw_input("�����뿽�������ļ����ƣ�")#���忽�������ļ�
# from sys import argv
from os.path import exists#���뺯��exists
#script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)#˵����ʲô�ط�������ʲô�ط�
# we could do these two on one line too, how?
in_file = open(from_file)#���ļ�
indata = in_file.read()#��ȡ�ļ�������
print "The input file is %d bytes long" % len(indata)#��ȡ�ļ����ݵĳ���
print "Does the output file exist? %r" % exists(to_file)#�жϿ��������ļ��Ƿ����
print "Ready, hit RETURN to continue, CTRL-C to abort." #�û��س�������Ctrl+C�ж�
raw_input()
out_file = open(to_file,'w')
out_file.write(indata)
print "Alright, all done."
out_file.close()#�ر��ļ�
in_file.close()
