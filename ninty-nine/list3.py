#coding=utf-8
'''
Created on 2016-7-29

@author: kemin.yu
'''

#P21 (*) Insert an element at a given position into a list
def p21(l, pos, element):
    l.insert(pos-1, element)
    return l

#P22 (*) Create a list containing all integers within a given range
def p22(start, end):
    return range(start, end+1)

#P23 (**) Extract a given number of randomly selected elements (potentially repeatable) from a list
def p23(n, start, end):
    import random
    candidate = range(start, end)
    result = []
    for i in range(n):
        result.append(random.choice(candidate))
    return result

#P24 (*) Lotto: Draw N different random numbers from the set 1..M
def p24(l, num):
    import random
    result = []
    for i in range(num):
        c = random.choice(l)
        while c in result:
            c = random.choice(l)
        result.append(c)
    return result

def p24b(l, num):
    import random
    return random.sample(l, num)

def p24c(l, num):
    import random, copy
    l2 = copy.deepcopy(l)
    result = []
    for i in range(num):
        c = random.choice(l2)
        result.append(c)
        l2.remove(c)
    return result

def p24d(l, num):
    import random, copy
    l2 = copy.deepcopy(l)
    result = []
    for _ in range(num):
        item = l2.pop(random.randint(0, len(l2)-1))
        result.append(item)
    return result

#P25 (*) Generate a random permutation of the elements of a list
def p25(l):
    import random
    random.shuffle(l)
    return l

def p25b(l):
    return p24c(l, len(l))

#P26 (**) Generate the combinations of K distinct objects chosen from the N elements of a list
def p26(l, num):
    result = []
    solution = []
    _combination(l, num, 0, result, solution)
    return result

def _combination(l, num, cur, result, solution):
    import copy
    if len(solution) == num:
        result.append(copy.deepcopy(solution))
        return
    for i in range(cur, len(l)):
        solution.append(l[i])
#        _combination(l, num, cur+1, result, solution) # permutation
        _combination(l, num, i+1, result, solution) # combination
        solution.pop(-1)
    
#P27 (**) Group the elements of a set into disjoint subsets
def p27(l, m, n, o):
    if m+n+o > len(l):
        return []
    
    import copy 
    result = []
    group1 = p26(l, m)
    for g1 in group1:
        rest23 = _remove(copy.deepcopy(l), g1)
#        print rest23, type(rest23)
        group2 = p26(rest23, n)
        for g2 in group2:
            rest3 = _remove(copy.deepcopy(rest23), g2)
            group3 = p26(rest3, o)
            for g3 in group3:
#                print g1, g2, g3
                result.append((g1, g2, g3))
    return result
    
def _remove(l, sub):
    for item in sub:
        l.remove(item)
    return l

#P28 (**) Sorting a list of lists according to length of sublists
def p28(l):
    return sorted(l, key=len)

def demo():
#    r = p26(["a", "b", "c", "d", "e", "f"], 3)
#    print len(r)
   r = p27(["a", "b", "c", "d", "e", "f", "g", "h", "i"], 2, 3, 4)
   print len(r)
   
   l = [("a", "b", "c"), ("d", "e"), ("f", "g", "h"), ("d", "e"), ("i", "j", "k"), ("m", "n"), ("o",)]
   print p28(l)

if __name__ == '__main__':
    demo()
    
    