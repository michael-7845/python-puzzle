#coding=utf-8
'''
Created on 2016-7-26

@author: kemin.yu
'''

#从字符串中分离"http://www.163.com/index.html"����www.163.com��
def q1():
    import re
    m = re.search("//(.*)/", "http://www.163.com/index.html")
    if m is not None:
        print m.group(1)

#输入任意一个字符串然后把它倒序显示出来
def q2():
    s = "this is the test string of mine"
    s_list = s.split()
    for s in s_list[::-1]:
        print s,

if __name__ == '__main__':
    q2()
    