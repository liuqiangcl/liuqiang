#-*- coding:utf-8-*-
'''
Created on 2014-2-26

@author: Hunk
'''
a="I am 6'2\" tall."
print a
b='I am 6\'2" tall.'
print b
tabby_cat ="\t I'm tabbed in."
persian_cat="I'm split\non a line."
backslash_cat ="I'm \\a \\ cat."
fat_cat="""
I'll do a list:
\t * Cat food 
\t * Fishies
\t * Catnip \n \t * Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "\a"
print "\b"
print "\f"
#print "%r" %"\\"
print '\\'
'''
while True:
    for i in ["/","-","|","\\","|"]:
        print "%r\r" % i,
'''
'''
for i in ['/','-','|','\\','|']:
    print "%s\r" % i,
    '''