'''
Created on 2016-7-21

@author: kemin.yu
'''

def f(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return f(n-1)+f(n-2)

def demo1():
    for i in xrange(10):
        print f(i)

def f2(n):
    a, b = 0, 1;
#    while b<n:
#        print b
#        a, b = b, a+b
    

def demo2():
    print f2(10)

if __name__ == '__main__':
    demo2()
    