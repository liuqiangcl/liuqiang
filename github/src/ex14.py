#-*- coding:utf-8-*-
'''
Created on 2014-2-27

@author: Hunk
'''
# from sys import argv
# script, user_name = argv
# prompt = '> '
# print "Hi %s, I'm the %s script." % (user_name, script)
# print "I'd like to ask you a few questions."
# print "Do you like me %s?" % user_name
# likes = raw_input(prompt)
# print "Where do you live %s?" % user_name
# lives = raw_input(prompt)
# print "What kind of computer do you have?"
# computer = raw_input(prompt)
# print """
# Alright, so you said %r about liking me.
# You live in %r. Not sure where that is.
# And you have a %r computer. Nice.
# """ % (likes, lives, computer)
#±äÐÎÊéÐ´
from sys import argv
script=raw_input()
user_name=raw_input()
argv = (script,user_name) 
prompt = '> '
print "Hi %s, I'm the %s script." % (argv[0],argv[1])
print "I'd like to ask you a few questions."
print "Do you like me %s?" % argv[0]
likes = raw_input(prompt)
print "Where do you live %s?" % argv[0]
lives = raw_input(prompt)
print "What kind of computer do you have?"
computer = raw_input(prompt)
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
