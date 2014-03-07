#-*-coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
print (True and True) #True
print (False and True) #False
print (1 == 1 and 2 == 1)  #False 
print ("test" == "test") #True
(1 == 1 or 2 != 1) #True
(True and 1 == 1) #True
print (False and 0 != 0)  #True
print (True or 1 == 1) #True
print ("test" == "testing") #False
print(1 != 0 and 2 == 1) #False
print("test" != "testing") #True
print("test" == 1)#False
print(not (True and False) )#True
print(not (1 == 1 and 0 != 1))#True
print(not (10 == 1 or 1000 == 1000))#False
print (not (1 != 10 or 3 == 4)) #False
print (not ("testing" == "testing" and "Zed" == "Cool Guy"))
print(1 == 1 and not ("testing" == 1 or 1 == 0))
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))


'''
    <> 不等于
    != 不等于
    >大于
    <小于
    <=x小于等于
    =>大于等于
    ==等于
'''