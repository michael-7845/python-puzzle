# coding: utf-8
'''
Created on 2016-7-21

@author: kemin.yu
'''

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass


def demo1():
    print Parent.x, Child1.x, Child2.x #1,1,1
    Child1.x = 2
    print Parent.x, Child1.x, Child2.x #1,2,1
    Parent.x = 3
    print Parent.x, Child1.x, Child2.x #3,2,3

def div1(x,y):
    print("%s/%s = %s" % (x, y, x/y))

def div2(x,y):
    print("%s//%s = %s" % (x, y, x//y))

def demo2():
    div1(5,2) # 2
    div1(5.,2) # 2.5
    div2(5,2) # 2
    div2(5.,2.) # 2.0

def demo3():
    list = ['a', 'b', 'c', 'd', 'e']
    print list[10:]

def demo4():
    def multipliers():
        return [lambda x : i * x for i in range(4)] #[(0*x), (1*x), (2*x), (3*x)]
    
    print [m(2) for m in multipliers()] # [0, 2, 4, 6]

def extendList(val, list=[]):
    list.append(val)
    return list

def demo5():
    list1 = extendList(10)
    list2 = extendList(123,[])
    list3 = extendList('a')
    
    print "list1 = %s" % list1 # [10, 'a']
    print "list2 = %s" % list2 # [123]
    print "list3 = %s" % list3 # [10, 'a']

if __name__ == '__main__':
    demo5()
    