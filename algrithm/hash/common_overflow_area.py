#coding=utf-8
'''
Created on 2016-8-1

@author: kemin.yu
'''

# 公共溢出区法
# 凡是冲突的都放到公共溢出区
def hash(k, t, coa, m=12):
    index = k % m
    if t[index] is None:
        t[index] = k
    else:
        coa.append(k)

def get(k, t, coa, m=12):
    index = k % m
    pos = -1
    if t[index] != k:
        index = -1
        pos = coa.index(k)
    return index, pos
    
def demo():
    a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    a_len = len(a)
    t = [None] * a_len
    coa = []
    for key in a:
        hash(key, t, coa, a_len)
    print a
    print t
    print coa
    
    for key in a:
        print key, get(key, t, coa, a_len)
        
if __name__ == '__main__':
    demo()
    