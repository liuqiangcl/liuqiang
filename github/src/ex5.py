#-*- coding:UTF_8 -*-
'''
Created on 2014-2-25

@author: Hunk
'''
my_name= "Zed A.Shaw"
my_age=35 #not a lie
my_height=74 #inches
my_weight=180 #lbs
my_eyes="Blue"
my_teeth="White"
my_hair="Brown"

print "Let's talk about %s." % my_name #%s,��ʾ��ʽһ������Ϊ�ַ�
print "He's %d inches tall." % my_height #%d,����
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
my_age, my_height, my_weight, my_age + my_height + my_weight)
print "*" * 30
#�ӷ���϶
name= "Zed A.Shaw"
age=35 #not a lie
height=74 #inches
weight=180 #lbs
eyes="Blue"
teeth="White"
hair="Brown"
print "Let's talk about %s." % name #%s,��ʾ��ʽһ������Ϊ�ַ�
print "He's %d inches tall." % height #%d,����
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)

print "*"* 30
# %r
print '%r'% '����' # �����ŵĵ����� 
print '%s'%'%s' # ��������

#��ʽ�ַ�������
#%d���͸�ʽ��
print "����:%d" %(2)
#%s�ַ�����ʽ��
print "�ַ���:%s"%("char")
print "�ַ�����ASCII��:%c" % "\xd4"
print "������:%f" %0.2
print "�޷�������:%u" % 122
print "�з�������(ʮ����):%d" % 22
'''
%c
�ַ�����ASCII��
%s
�ַ���
%d
�з�������(ʮ����)
%u
�޷�������(ʮ����)
%o
�޷�������(�˽���)
%x
�޷�������(ʮ������)
%X
�޷�������(ʮ�����ƴ�д�ַ�)
%e
��������(��ѧ������)
%E
��������(��ѧ����������E����e)
%f
��������(��С�������)
%g
��������(����ֵ�Ĵ�С����%e��%f)
%G
��������(������%g)
%p
ָ��(��ʮ�����ƴ�ӡֵ���ڴ��ַ)
%n
�洢����ַ��������Ž������б����һ��������
'''