#-*-coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
the_count =[1,2,3,4,5]
fruits=["apples","oranges","pears","apricots"]
change =[1,"pennies",2,"dimes",3,"quarters"]
 
#this first kind of for-loop goes through a list
for number in the_count:
    print"This is count %d" % number
#��list����ѭ��
#same as above
for fruit in fruits:
    print "A fruit of type : %s" % fruit
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" %i
 
#we can also build lists , first start with an empty one
element=[] # ����һ���յ�list
#then use the range function to do 0 to 5 counts
for i in range(0,6): #
    print "Adding %d to the list." % i
    element.append(i) #����Ԫ��
#now we can print them out too 
for i in element:
    print "Element was:%d " %i
 
help(range)
# range([start,] stop[, step]) -> list of integers    
#start��ʼֵ������ֵ��step����

#���κ���
element=range(0,6)
print element


#element.count(value)#ͳ��value�Ĵ���
#element.index(value, ) #��ȡԪ�ص�����
#element.insert(index, object)#��ָ����λ�ò���Ԫ��
#element.pop()#ɾ��ָ��λ��Ԫ��
#element.remove(value)#ɾ����һ��ָ��Ԫ��
#element.reverse()��ת
#element.extend(iterable#�ϲ��б�)
#element.sort()����