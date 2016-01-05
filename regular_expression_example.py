# -*- coding: cp936 -*-
import re


text = "Hi, I am Shirley Hilton. I am his wife.\nzhs"

m = re.findall(r"hi", text)
if m:
    print m
else:
    print 'not match'
    
m2 = re.findall(r"\bhi",text)
if m2:
    print m2
else:
    print 'not match'
    
m3 = re.findall(r"\bhi\b",text)
if m3:
    print m3
else:
    print 'not match'
    
m4 = re.findall(r"[Hh]i",text)
if m4:
    print "m4:"+str(m4) 
else:
    print 'not match'

#“.”在正则表达式中表示除换行符以外的任意字符
m5 = re.findall(r"i.",text)
if m5:
    print "m5:   "+str(m5) 
else:
    print 'not match'

#“\S”，它表示的是不是空白符的任意字符

#“*”表示数量：它表示前面的字符可以重复任意多次（包括0次）
#懒惰匹配
m6 = re.findall(r"I.*?e",text)
if m6:
    print "m6:   "+str(m6) 
else:
    print 'not match'
#贪婪匹配
m7 = re.findall(r"I.*e",text)
if m7:
    print "m7:   "+str(m7) 
else:
    print 'not match'


#从下面一段文本中，匹配出所有s开头，e结尾的单词。
text2 = "site sea sue sweet see case sse ssee loses"
m8 = re.findall(r"\bs\S*?e\b",text2)
if m8:
    print "m8:   "+str(m8) 
else:
    print 'not match'




    
