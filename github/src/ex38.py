#-*-coding:utf-8-*-
'''
Created on 2014-3-6

@author: Hunk
'''
# create a mapping of state to abbreviation
"""create dict"""
states = {
          'Oregon': 'OR',
          'Florida': 'FL',
          'California': 'CA',
          'New York': 'NY',
          'Michigan': 'MI'
          }
# create a basic set of states and some cities in them
cities = {
          'CA': 'San Francisco',
          'MI': 'Detroit',
          'FL': 'Jacksonville'
          }
# add some more cities
"""字典中增加新的元素"""
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
#验证字典中具有哪些元素
print cities
 
# print out some cities
print '-' * 10
""""通过索引获取字典元素"""
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']
 
# print some states
 
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']#MI
print "Florida's abbreviation is: ", states['Florida']#FL
# do it by using the state then cities dict
 
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]#Detroit/把states对应的索引值做为参数引用
print "Florida has: ", cities[states['Florida']]#acksonville
 
 
# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)
print states.items() #转换成为列表
  
# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)
 
 
# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])
print '-' * 10
 
 
# safely get a abbreviation by state that might not be there
print "???"
state = states.get('Texas', None)
if not state:
    print "Sorry, no Texas."
 
# 
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city