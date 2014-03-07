#-*-coding:utf-8-*-
'''
Created on 2014-3-4

@author: Hunk
'''
def cheese_and_crackers(cheese_count,boxes_of_crackers):#定义函数cheese_and_crackers,包含两个参数
    print"You hava %d cheeses!" % cheese_count #格式化整数
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket .\n"
    
#调用函数cheese_and_crackers()

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) 
print ""  
#cheese_and_crackers("No","yes") 格式为整型非字符类型
#TypeError: %d format: a number is required, not str
print "OR, we can use variables from our script:"

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) #采用变量进行参数

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)#以运算形式，进行参数

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#变量和数字运算进行参数
cheese_and_crackers(1,0)

print "*" * 30

# def discipline(*num):
#     print "You can choose the %s %s" %(num)
# discipline("chinese","match")

