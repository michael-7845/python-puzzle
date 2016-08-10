#coding=utf-8
'''
Created on 2016-7-31

@author: kemin.yu
'''

# 开放定址
# 一旦发生冲突，就去寻找下一个空的散列地址，只要散列地址足够大，空的散列地址就总能找到
# fi(key) = (f(key) + di) % m
# di = 0, 1, 2, ..., m-1
# di = 1, 2, 4, ...
# di = random int
def hash_conflict(k, t, m=12, delta = 0):
    index = (k+delta) % m
    if t[index] is not None:
        delta += 1
        if delta < m:
            return hash_conflict(k, t, m, delta)
        else:
            return -1
    return index

def get(k, t, m=12, delta = 0):
    index = (k+delta) % m
    if t[index] != k:
        print k, "conflicting!"
        delta += 1
        if delta < m:
            return get(k, t, m, delta)
        else:
            return -1
    return index
    
def demo():
    a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    a_len = len(a)
    t = [None] * a_len
    for key in a:
        index = hash_conflict(key, t, a_len)
        t[index] = key
    print a
    print t
    
    for key in a:
        print get(key, t, a_len)
        
    
if __name__ == '__main__':
    demo()
    