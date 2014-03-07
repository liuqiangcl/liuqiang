#-*- UTF:coding-*-
'''
Created on 2014-2-25

@author: Hunk
'''
x="There are %d types of people." % 10
print x
binary="binary"
do_not="don't"
y="Those who know %s and those who %s." %(binary,do_not)
print x
print y

print "I said: %r." %(x)
print "I said: %s." %(x)
print "I also said:'%r'." %y
print "I also said:'%s'." %y
hilarious= False
joke_evaluation = "Isn't that joke so funny?! %r" 
print joke_evaluation % hilarious
print joke_evaluation % False

w="This is the left sidu of ..."
e="a string with a right side."
print w+e