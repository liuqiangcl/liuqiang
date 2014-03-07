#-*-coding:utf-8-*-
'''
Created on 2014-2-26

@author: Hunk
'''
formatter="%r %r %r %r"
print formatter % ("a","b","c","d")
print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter %(formatter,formatter,formatter,formatter)
print formatter % (
                   "I had this thing.",
                   "That you could type u right.",
                   "But it didn't sing.",
                   "So I said goodnight."
                   )