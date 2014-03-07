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
#对list进行循环
#same as above
for fruit in fruits:
    print "A fruit of type : %s" % fruit
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" %i
 
#we can also build lists , first start with an empty one
element=[] # 定义一个空的list
#then use the range function to do 0 to 5 counts
for i in range(0,6): #
    print "Adding %d to the list." % i
    element.append(i) #增加元素
#now we can print them out too 
for i in element:
    print "Element was:%d " %i
 
help(range)
# range([start,] stop[, step]) -> list of integers    
#start起始值，结束值，step步长

#变形函数
element=range(0,6)
print element


#element.count(value)#统计value的次数
#element.index(value, ) #获取元素的索引
#element.insert(index, object)#在指定的位置插入元素
#element.pop()#删除指定位置元素
#element.remove(value)#删除第一个指定元素
#element.reverse()翻转
#element.extend(iterable#合并列表)
#element.sort()排序