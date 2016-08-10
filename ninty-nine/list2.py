#coding=utf-8
'''
Created on 2016-7-29

@author: kemin.yu
'''
import nose
from nose.tools import *

#P11 (*) Modified run-length encoding
def p11(l):
    length = len(l)
    i = j = 0
    result = []
    
    while i < length:
        j = i + 1
        c = l[i]
        while j < length and l[j] == c:
            j += 1
        if j - i == 1:
            result.append(c)
        else:
            result.append((c, j-i))
        i = j
    return result

def test_p11():
    eq_(p11([]), [])
    l = p11(["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"])
    eq_(l[0], ("a", 4))
    eq_(l[1], "b")
    eq_(l[2], ("c", 2))
    eq_(l[3], ("a", 2))
    eq_(l[4], "d")
    eq_(l[5], ("e", 4))

#P12 (**) Decode a run-length encoded list
def p12(l):
    result = []
    for item in l:
        if isinstance(item, tuple):
            result.extend((item[0],) * item[1])
        else:
            result.append(item)
    return result

def test_p12():
    eq_(p12([]), [])
    orig = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
    mid = p11(orig)
    target = p12(mid)
    eq_(target, orig)

#P13 (**) Run-length encoding of a list (direct solution)
def p13(l): # also, p10() is an answer as well
    length = len(l)
    if length == 0:
        return l
    
    result = []
    result.append([1, l[0]])
    for item in l[1:]:
        if item == result[-1][1]:
            result[-1][0] += 1
        else:
            result.append([1, item])
    return result
    
def test_p13():
    eq_(p13(['a', 'b', 'c']), [[1, 'a'], [1, 'b'], [1, 'c']])
    eq_(p13(['a', 'a', 'a', 'b', 'c']), [[3, 'a'], [1, 'b'], [1, 'c']])
    eq_(p13(['a', 'b', 'b', 'c']), [[1, 'a'], [2, 'b'], [1, 'c']])
    eq_(p13(['a', 'b', 'c', 'c']), [[1, 'a'], [1, 'b'], [2, 'c']])
    eq_(p13(['a', 'a', 'b', 'c', 'c']), [[2, 'a'], [1, 'b'], [2, 'c']])
    
#P14 (*) Duplicate the elements of a list
def p14(l):
    result = []
    for item in l:
        result.append(item)
        result.append(item)
        # or 
        #result.extend([item] * 2)
    return result

def test_p14():
    r = p14([])
    eq_(len(r), 0)
    eq_(r, [])
    r = p14([1, 2, 3, 4])
    eq_(len(r), 8)
    eq_(r, [1, 1, 2, 2, 3, 3, 4, 4])

#P15 ** (**) Duplicate the elements of a list a given number of times**
def p15(l, times):
    result = []
    for item in l:
        result.extend([item] * times)
    return result

def test_p15():
    r = p15([], 3)
    eq_(len(r), 0)
    eq_(r, [])
    r = p15([1, 2, 3], 3)
    eq_(len(r), 9)
    eq_(r, [1, 1, 1, 2, 2, 2, 3, 3, 3])

def p15b(l, times):
    def flatten(l2):
        return [item for sub in l2 for item in sub]
    return flatten([[i] * times for i in l])

def test_p15b():
    r = p15b([], 3)
    eq_(len(r), 0)
    eq_(r, [])
    r = p15b([1, 2, 3], 3)
    eq_(len(r), 9)
    eq_(r, [1, 1, 1, 2, 2, 2, 3, 3, 3])
    
#P16 (**) Drop every N'th element from a list
def p16(l, interval):
    if interval == 0:
        return l
    
    i = 0
    result = []
    for item in l:
        i += 1
        if i % interval != 0:
            result.append(item)
    return result

def test_p16():
    r = p16([], 3)
    eq_(len(r), 0)
    eq_(r, [])
    
    r = p16(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 3)
    eq_(len(r), 8)
    eq_(r, ["a", "b", "d", "e", "g", "h", "j", "k"])
    
    r = p16(["a", "b"], 3)
    eq_(len(r), 2)
    eq_(r, ["a", "b"])
    
    r = p16(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 0)
    eq_(len(r), 11)
    eq_(r, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])

def p16b(l, interval):
    if interval == 0:
        return l
    return [ item for (index,item) in enumerate(l) if (index+1) % interval != 0 ]

def test_p16b():
    r = p16b([], 3)
    eq_(len(r), 0)
    eq_(r, [])
    
    r = p16b(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 3)
    eq_(len(r), 8)
    eq_(r, ["a", "b", "d", "e", "g", "h", "j", "k"])
    
    r = p16b(["a", "b"], 3)
    eq_(len(r), 2)
    eq_(r, ["a", "b"])
    
    r = p16b(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 0)
    eq_(len(r), 11)
    eq_(r, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    
#P17 (*) Split a list into two parts; the length of the first part is given
def p17(l, length):
    return (l[:length], l[length:])

def test_p17():
    r = p17([], 3)
    eq_(r[0], [])
    eq_(r[1], [])
    
    r = p17(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 3)
    eq_(r[0], ["a", "b", "c"])
    eq_(r[1], ["d", "e", "f", "g", "h", "i", "j", "k"])
    
    r = p17(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 0)
    eq_(r[0], [])
    eq_(r[1], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    
    r = p17(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 11)
    eq_(r[0], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    eq_(r[1], [])
    
    r = p17(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 12)
    eq_(r[0], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    eq_(r[1], [])

#P18 (**) Extract a slice from a list, counting from 1
def p18(l, start, end):
    return l[start-1:end]

def test_p18():
    r = p18([], 1, 3)
    eq_(r, [])
    
    r = p18(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 3, 7)
    eq_(r, ["c", "d", "e", "f", "g"])
    
    r = p18(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 1, 11)
    eq_(r, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])
    
    r = p18(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], 1, 12)
    eq_(r, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"])

#P19 (**) Rotate a list N places to the left
def p19(l, pos): # classic 3 reverse
    sub1 = l[:pos]; sub1.reverse()
    sub2 = l[pos:]; sub2.reverse()
    result = sub1 + sub2
    result.reverse()
    return result

def test_p19():
    eq_(p19(["a", "b", "c", "d", "e", "f", "g", "h"], 3), ["d", "e", "f", "g", "h", "a", "b", "c"])
    eq_(p19(["a", "b", "c", "d", "e", "f", "g", "h"], 0), ["a", "b", "c", "d", "e", "f", "g", "h",])
    eq_(p19(["a", "b", "c", "d", "e", "f", "g", "h"], -2), ["g", "h", "a", "b", "c", "d", "e", "f"])

def p19b(l, pos):
    left = l[:pos]
    right = l[pos:]
    return right+left

def test_p19b():
    eq_(p19b(["a", "b", "c", "d", "e", "f", "g", "h"], 3), ["d", "e", "f", "g", "h", "a", "b", "c"])
    eq_(p19b(["a", "b", "c", "d", "e", "f", "g", "h"], 0), ["a", "b", "c", "d", "e", "f", "g", "h",])
    eq_(p19b(["a", "b", "c", "d", "e", "f", "g", "h"], -2), ["g", "h", "a", "b", "c", "d", "e", "f"])

#P20 (*) Remove the K'th element from a list, counting from 1
def p20(l, kth):
    l.pop(kth-1)
    return l

def p20b(l, kth):
    return l[0:kth-1], l[kth:len(l)]

def test_p20():
    eq_(p20(["a", "b", "c", "d"], 2), ["a", "c", "d"])

def test_p20b():
    r = p20b(["a", "b", "c", "d"], 2)
    eq_(r[0], ["a", ])
    eq_(r[1], ["c", "d"])

if __name__ == '__main__':
    nose.runmodule()
    
    