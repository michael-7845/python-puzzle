#coding=utf-8
'''
Created on 2016-7-29

@author: kemin.yu
'''

#P31 (**) Determine whether a given integer number is prime.
def p31(num):
    import math
    if num < 2:
        return False
    top = int(math.sqrt(num))
    for i in range(2, top+1):
        if num % i == 0:
            return False
    return True

#P32 (**) Determine the prime factors of a given positive integer.
def p32(num):
    if num < 2:
        return []
    result = []
    _prime_factors(num, result)
    return result

def _prime_factors(num, result):
    import math
    top = int(math.sqrt(num))
    factor = num
    for i in range(2, top+1):
        if num % i == 0:
            factor = i
            break;
    result.append(factor)
    if factor != num:
        _prime_factors(num/factor, result)

#P33 (**) Determine the prime factors of a given positive integer (2).
def p33(num):
    factors = p32(num)
    factors.sort()
    result = []
    sub = [factors[0], 1]
    for f in factors[1:]:
        if f == sub[0]:
            sub[1] += 1
        else:
            result.append(sub)
            sub = [f, 1]
    result.append(sub)
    return result

#P34 (*) A list of prime numbers
def p34(start, end):
    r = range(start, end+1)
    result = []
    for n in r:
        if p31(n):
            result.append(n)
    return result
    
#P35 (**) Goldbach's conjecture.
def p35(even):
    primes = sorted(p34(2, even+1))
    for p in primes:
        if (even-p) in primes:
            return p, even-p
    return 0, 0

#P36 (**) A list of Goldbach compositions.
def p36(start, end, interval=1):
    r = range(start, end+1)
    result = []
    for n in r:
        if n % 2 == 0:
            result.append([n, p35(n)])
    return result

def p36b(l):
    result = []
    for n in l:
        if n % 2 == 0:
            result.append([n, p35(n)])
    return result        

#P37 (**) Determine the greatest common divisor of two positive integer numbers.
def p37(a, b):
    return _gcd2(a, b)

def _gcd1(a, b): # greatest common divide
    if b == 0:
        return a
    else:
        return _gcd1(b, a%b)
    
def _gcd2(a, b): # greatest common divide
    c = a%b
    while c != 0:
        a = b
        b = c
        c = a%b
    return b

#P38 (*) Determine whether two positive integer numbers are coprime.
def p38(a, b):
    if p37(a, b) == 1:
        return True
    return False

#P39 (**) Calculate Euler's totient function phi(m).
def p39(m):
    result = []
    for i in range(1, m):
        if p38(i, m):
            result.append(i)
    print result
    return len(result)    

#P40 (**) Calculate Euler's totient function phi(m) (2).
# what does it mean?

if __name__ == '__main__':
    pass

