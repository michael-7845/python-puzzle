#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016-7-28

@author: kemin.yu
'''
import nose
from nose.tools import *
    
class NoSuchElementException(Exception):
    def __init__(self, arg):
        self.arg = arg

#P01 (*) Find the last element of a list
def p01(list):
    return list[-1]

def Test_p01():
    list = [0, 1, 2, 3]
    assert p01(list) == 3

#P02 (*) Find the last but one element of a list
def p02(list):
    if len(list) == 0:
        raise NoSuchElementException("list size is 0")
    if len(list) == 1:
        raise NoSuchElementException("list size is 1")
    return list[-2]

def test_p02():
    list = []
    assert_raises(NoSuchElementException, p02, list)
    
    list = [1]
    assert_raises(NoSuchElementException, p02, list)
    
    list = [1, 2, 3]
    eq_(p02(list), 2, "error")

#P03 (*) Find the Kth element of a list
def p03(list, kth):
    if len(list)==0 or kth<=0 or kth>len(list):
        raise NoSuchElementException("invalid kth: "+str(kth))
    return list[kth-1]

def test_p03():
    list = []
    assert_raises(NoSuchElementException, p03, list, 1)
    
    list = [1]
    assert_raises(NoSuchElementException, p03, list, 2)
    
    list = [1, 2, 3]
    assert_raises(NoSuchElementException, p03, list, 0)
    assert_raises(NoSuchElementException, p03, list, -1)
    eq_(p03(list, 2), 2, "error")

#P04 (*) Find the number of elements of a list
def p04(list):
    return len(list)

def test_p04():
    list = []
    eq_(p04(list), 0, "error")
    list = ['a']
    eq_(p04(list), 1, "error")
    list = [1, 2, 3]
    eq_(p04(list), 3, "error")

#P05 (*) Reverse a list
def p05(list):
    return list[::-1]

def test_p05():
    list = []
    eq_(p05(list), [], "error")
    list = ['a']
    eq_(p05(list), ['a'], "error")
    list = [1, 2, 3]
    eq_(p05(list), [3, 2, 1], "error")

#P06 (*) Find out whether a list is a palindrome
def p06(list):
    length = len(list)
    if length == 0:
        return True
    
    mid = length/2
    if(length%2 == 1):
        # odd
        small = big = mid
    else:
        # even
        small = mid - 1
        big = mid
    while small>=0 or big<length:
        if list[small] != list[big]:
            return False
        small -= 1
        big += 1
    return True 

def test_p06():
    list = []
    assert_true(p06(list), "error")   
    list = [1, 2, 3, 2, 1]
    assert_true(p06(list), "error")   
    list = [1, 2, 3, 2, 3]
    assert_false(p06(list), "error")   
    list = ['a', 'b', 'c', 'c', 'b', 'a']
    assert_true(p06(list), "error")   
    list = ['a', 'b', 'c', 'c', 'd', 'a']
    assert_false(p06(list), "error")   

#P07 (**) Flatten a nested list structure
def p07(l):
    result = []
    for item in l:
        if isinstance(item, (list, tuple)):
            for it in item:
                result.append(it)
        else:
            result.append(item)
    return result

def test_p07():
    list = []
    eq_(p07(list), [], "error")
    list = [1, 2, 3]
    eq_(p07(list), [1, 2, 3], "error")
    list = [1, [2, 3], 4, 5]
    eq_(p07(list), [1, 2, 3, 4, 5], "error")
    list = [1, [2, 3], 4, [5, 6, 7]]
    eq_(p07(list), [1, 2, 3, 4, 5, 6, 7], "error")
    list = [1, [2, 3], [4], [5, 6, 7]]
    eq_(p07(list), [1, 2, 3, 4, 5, 6, 7], "error")
    list = [1, (2, 3), 4, 5]
    eq_(p07(list), [1, 2, 3, 4, 5], "error")
    list = [1, (2, 3), 4, (5, 6, 7)]
    eq_(p07(list), [1, 2, 3, 4, 5, 6, 7], "error")
    list = [1, (2, 3), (4,), (5, 6, 7)]
    eq_(p07(list), [1, 2, 3, 4, 5, 6, 7], "error")
    list = [1, [2, 3], 4, [], 5]
    eq_(p07(list), [1, 2, 3, 4, 5], "error")
    list = [1, [2, 3], 4, (), 5]
    eq_(p07(list), [1, 2, 3, 4, 5], "error")

#P08 (**) Eliminate consecutive duplicates of list elements
def p08(l):
    length = len(l)
    if length == 0:
        return l
    
    i = j =0 
    result = []
    while i < length:
        for j in range(i+1, length):
            if l[i] != l[j]:
                result.append(l[i])
                break
        if j == length-1:
            result.append(l[j])
            break;
        i = j
    return result

def p08b(l):
    length = len(l)
    if length == 0:
        return l
    
    i = j =0 
    result = []
    while i < length:
        j = i + 1
        c = l[i]
        while j < length and l[j] == c:
            j += 1
        result.append(c)
        i = j
    return result

def p08c(l):
    length = len(l)
    if length == 0:
        return l
    
    result = []
    result.append(l[0])
    for item in l:
        if item != result[-1]:
            result.append(item)
    return result

def test_p08():
    eq_(p08([]), [])
    eq_(p08([1]), [1])
    eq_(p08([1, 2, 1, 2, 3]), [1, 2, 1, 2, 3])
    eq_(p08([1, 1, 1, 2, 3]), [1, 2, 3])
    eq_(p08([1, 2, 2, 2, 3]), [1, 2, 3])
    eq_(p08([1, 2, 3, 3, 3]), [1, 2, 3])
    eq_(p08([1, 1, 2, 3, 3]), [1, 2, 3])
    
def test_p08b():
    eq_(p08b([]), [])
    eq_(p08b([1]), [1])
    eq_(p08b([1, 2, 1, 2, 3]), [1, 2, 1, 2, 3])
    eq_(p08b([1, 1, 1, 2, 3]), [1, 2, 3])
    eq_(p08b([1, 2, 2, 2, 3]), [1, 2, 3])
    eq_(p08b([1, 2, 3, 3, 3]), [1, 2, 3])
    eq_(p08b([1, 1, 2, 3, 3]), [1, 2, 3])

def test_p08c():
    eq_(p08c([]), [])
    eq_(p08c([1]), [1])
    eq_(p08c([1, 2, 1, 2, 3]), [1, 2, 1, 2, 3])
    eq_(p08c([1, 1, 1, 2, 3]), [1, 2, 3])
    eq_(p08c([1, 2, 2, 2, 3]), [1, 2, 3])
    eq_(p08c([1, 2, 3, 3, 3]), [1, 2, 3])
    eq_(p08c([1, 1, 2, 3, 3]), [1, 2, 3])
    
#P09 (**) Pack consecutive duplicates of list elements into sublists
def p09(l): # understand the requirement by mistake
    length = len(l)
    if length == 0:
        return l
    
    i = j = 0 
    result = []
    while i < length:
        for j in range(i+1, length):
            if l[i] != l[j]:
                delta = j - i
                if delta > 1:
                    result.append([l[i]] * delta)
                else:
                    result.append(l[i])
                break
        if j == length-1:
            delta = j - i
            if l[i] == l[j] and j > i:
                result.append([l[i]] * (delta+1))
            else: 
                result.append(l[j])
            break;
        i = j
    return result

def p09b(l): # understand the requirement by mistake
    length = len(l)
    if length == 0:
        return l
    
    i = j =0 
    result = []
    while i < length:
        j = i + 1
        c = l[i]
        while j < length and l[j] == c:
            j += 1
        if j-i == 1:
            result.append(c)
        else:
            result.append([c] * (j-i))
        i = j
    return result

def p09c(l):
    length = len(l)
    if length == 0:
        return l
    
    result = []
    sub = []
    sub.append(l[0])
    for item in l[1:]:
        if item == sub[-1]:
            sub.append(item)
        else:
            result.append(sub)
            sub = [item]
    result.append(sub)
            
    return result

def test_p09():
    eq_(p09([]), [])
    eq_(p09([1]), [1])
    eq_(p09([1, 2, 1, 2, 3]), [1, 2, 1, 2, 3])
    eq_(p09([1, 1, 1, 2, 3]), [[1, 1, 1], 2, 3])
    eq_(p09([1, 2, 2, 2, 3]), [1, [2, 2, 2], 3])
    eq_(p09([1, 2, 3, 3, 3]), [1, 2, [3, 3, 3]])
    eq_(p09([1, 1, 2, 3, 3]), [[1, 1], 2, [3, 3]])

def test_p09b():   
    eq_(p09b([]), [])
    eq_(p09b([1]), [1])
    eq_(p09b([1, 2, 1, 2, 3]), [1, 2, 1, 2, 3])
    eq_(p09b([1, 1, 1, 2, 3]), [[1, 1, 1], 2, 3])
    eq_(p09b([1, 2, 2, 2, 3]), [1, [2, 2, 2], 3])
    eq_(p09b([1, 2, 3, 3, 3]), [1, 2, [3, 3, 3]])
    eq_(p09b([1, 1, 2, 3, 3]), [[1, 1], 2, [3, 3]])
    
def test_p09c():   
    eq_(p09c([]), [])
    eq_(p09c([1]), [[1]])
    eq_(p09c([1, 2, 1, 2, 3]), [[1], [2], [1], [2], [3]])
    eq_(p09c([1, 1, 1, 2, 3]), [[1, 1, 1], [2], [3]])
    eq_(p09c([1, 2, 2, 2, 3]), [[1], [2, 2, 2], [3]])
    eq_(p09c([1, 2, 3, 3, 3]), [[1], [2], [3, 3, 3]])
    eq_(p09c([1, 1, 2, 3, 3]), [[1, 1], [2], [3, 3]])

#P10 (*) Run-length encoding of a list
def p10(l):
    length = len(l)
    if length == 0:
        return l
    
    i = j =0 
    result = []
    while i < length:
        j = i + 1
        c = l[i]
        while j < length and l[j] == c:
            j += 1
        result.append((j-i, c))
        i = j
    return result

def test_p10():
    eq_(p10([]), [])
    l = p10(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"])
    eq_(l[0], (4, "a"))
    eq_(l[1], (1, "b"))
    eq_(l[2], (2, "c"))
    eq_(l[3], (2, "a"))
    eq_(l[4], (1, "d"))
    eq_(l[5], (4, "e"))

if __name__ == '__main__':
    nose.runmodule()
    
    