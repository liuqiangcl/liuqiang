#-*-coding:utf-8-*-
'''
Created on 2014-3-4

@author: Hunk
'''
def cheese_and_crackers(cheese_count,boxes_of_crackers):#���庯��cheese_and_crackers,������������
    print"You hava %d cheeses!" % cheese_count #��ʽ������
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket .\n"
    
#���ú���cheese_and_crackers()

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) 
print ""  
#cheese_and_crackers("No","yes") ��ʽΪ���ͷ��ַ�����
#TypeError: %d format: a number is required, not str
print "OR, we can use variables from our script:"

amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers) #���ñ������в���

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)#��������ʽ�����в���

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)#����������������в���
cheese_and_crackers(1,0)

print "*" * 30

# def discipline(*num):
#     print "You can choose the %s %s" %(num)
# discipline("chinese","match")

