#coding=utf-8
'''
Created on 2016-7-31

@author: kemin.yu
'''
from random import *

# teacher: [studens]
mentor = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}

a = mentor['b'] + mentor['c']
b = mentor['a'] + mentor['c']
c = mentor['a'] + mentor['b']

all = mentor['a'] + mentor['b'] + mentor['c']

def _remove(a, b):
    return list(set(a)-set(b))

def group(): # not finished
    ga = sample(a, 3)
    print ga
    print a, b, c
    
    gb = sample(_remove(b,ga), 3)
    print gb
    print a, b, c
    
    gc = _remove(_remove(c, ga), gb)
    print gc
    print a, b, c
    
    rest = _remove(_remove(_remove(all, ga), gb), gc)
    print rest
    
def group2():
    import copy
    groups = copy.deepcopy(mentor)
    print groups
    while not _all_ok(groups):
        _shuffle(groups)
        print "groups:", groups
        print "mentor:", mentor
    
def _shuffle(groups):
    all = groups['a'] + groups['b'] + groups['c']
    print all
    shuffle(all)
    groups['a'] = all[0:3]
    groups['b'] = all[3:6]
    groups['c'] = all[6:9]  

def _ok(teacher, group):
    for student in group:
        if student in mentor[teacher]:
            return False
    return True

def _all_ok(groups):
    for (t, g) in groups.items():
        if not _ok(t, g):
            return False
    return True      

if __name__ == '__main__':
    group2()
    