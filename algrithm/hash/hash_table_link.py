#coding=utf-8
'''
Created on 2016-8-1

@author: kemin.yu
'''

# 链地址法
# 将所有关键字为同义词的记录存储在一个单链表（这里用list)来表示
def hash(k, t, m=12):
    index = k % m
    t[index].append(k)

def get(k, t, m=12):
    index = k % m
    pos = t[index].index(k)
    return index, pos
    
def demo():
    a = [12, 67, 56, 16, 25, 37, 22, 29, 15, 47, 48, 34]
    a_len = len(a)
    t = []
    for i in range(a_len):
        t.append([])
    for key in a:
        hash(key, t, a_len)
    print a
    print t
    
    for key in a:
        print get(key, t, a_len)
        
if __name__ == '__main__':
    demo()
    