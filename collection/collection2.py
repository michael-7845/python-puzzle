#coding: utf-8
'''
Created on 2016-7-21

@author: kemin.yu
'''

# 1. 请写出一段Python代码实现删除一个list里面的重复元素
l = [1, 1, 2, 3, 4, 5, 2, 1, 3]

def one1():
    r = list(set(l))
    print r
    
def one2():
    d = {}
    for i in l:
        d[i] = 1
    print d.keys()

# 2. 删除list里面的某元素
def _deduplicate(n):
    while(n in l):
        l.remove(n)

def two1():
    _deduplicate(1)
    print l
    _deduplicate(2)
    print l
    _deduplicate(3)
    print l

if __name__ == '__main__':
    two1()
    