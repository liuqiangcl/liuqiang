#-*-coding:utf-8-*-
'''
Created on 2014-3-5

@author: Hunk
'''
print "Let's Practice everything."
print "You \'d need to know \' bout escapes with \\ that do \n newlines and \t tabs."

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------------------------------"
print poem 
print "-------------------------------------"

five = 10.2 -2 + 3 -6
print five
print "This should be five: %s" % five
print "This should be five: %d" % five 
print "This should be five: %f" % five 

def secret_formula(started):
    jelly_beans= started * 500
    jars=jelly_beans /1000
    crates =jars /100
    return jelly_beans,jars,crates


start_point = 10000


secret_formula(start_point)
print secret_formula#��ӡ�������Ǻ����Ĵ洢λ��


beans, jars, crates = secret_formula(start_point) #��beans, jars, crates ��������ȥ�洢����ֵ����ȡ����ֵ��Ҫ����
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)


start_point = start_point / 10


print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
