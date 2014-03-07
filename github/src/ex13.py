#-*- coding:utf-8-*-
'''
Created on 2014-2-27

@author: Hunk
'''
# from sys import argv
# script, first, second, third = argv
# print "The script is called:", script
# print "Your first variable is:", first
# print "Your second variable is:", second
# print "Your third variable is:", third
#¸ñÊ½×ª»»
import sys
sys.argv=("ex13.py","first","second", "third") 
print "The script is called:", sys.argv[0]
print "Your first variable is:", sys.argv[1]
print "Your second variable is:", sys.argv[2]
print "Your third variable is:", sys.argv[3]

