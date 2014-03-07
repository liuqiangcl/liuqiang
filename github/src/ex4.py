#-*- coding:UTF-8 -*-
'''
Created on 2014-2-24

@author: Hunk
'''
cars=100 #定义整型变量
space_in_a_car = 4.0 #定义单精度类型
drivers = 30 #定义整型变量
passengers = 90 #定义整型变量
cars_not_driven = cars - drivers  #计算cars和drivers之间的插入只
cars_driven = drivers #
print "cars_driven value is:",cars_driven
carpool_capacity = cars_driven * space_in_a_car
space_in_b_car=4
average_passengers_per_car = passengers / cars_driven
carpool_capacity_b = cars_driven * space_in_b_car
print carpool_capacity_b
#average_passengers_per_car = car_pool_capacity / passenger #car_pool_capacity没有定义
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."


