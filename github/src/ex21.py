#-*-coding:utf-8-*-
'''
Created on 2014-3-5

@author: Hunk
'''
# def add(a,b):
#     print "ADDING %d + %d" %(a,b)
#     return a+b
# def subtract(a,b):
#     print "SUBTRACTING %d -%d" %(a,b)
#     return a-b
# def multiply(a,b):
#     print "MULTIPLYING %d * %d" %(a,b)
#     return a*b
# def divide(a,b):
#     print "DIVIDING %d / %d" %(a,b)
#     return a/b
# 
# print "Let's do some math with just functions!"
# 
# age = add(24, 5)
# height = subtract(178, 4)
# weight = multiply(90, 2)
# iq = divide(100, 2)
# 
# 
# print "Age: %d, Height %d ,Weight :%d ,IQ: %d" % (age,height,weight,iq)
# 
# #��ʧ%��������ʾTypeError: 'str' object is not callable,type it in anyway 
# 
# 
# print "Here is a puzzle."
# what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 
# print "That becomes: ", what, "Can you do it by hand?"


#�ַ�����ʽ��ʱ���%�ŷ�ʽΪ%%
def remainder(a,b):
    print "remainder %d %% %d =" % (a,b)
    return a % b
print remainder(2,4)
