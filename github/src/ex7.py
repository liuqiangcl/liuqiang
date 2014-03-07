# -*- coding: UTF-8 -*-
'''
Created on 2014-2-26

@author: Hunk
'''
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "and everywhere that Mary want."
print "."*10  #what'd that do? 打印10 “.”
'''
SyntaxError: Non-ASCII character '\xb4' in file
 D:\workspace\github\src\ex7.py on line 10,
 but no encoding declared; 
 see http://www.python.org/peps/pep-0263.html for details
 编码格式错误，导致编译中文出错
'''
end1="C"
end2="h"
end3="e"
end4="e"
end5="s"
end6="e"
end7="B"
end8="u"
end9="r"
end10="g"
end11="e"
end12="r"
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12