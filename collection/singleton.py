#coding=utf-8
'''
Created on 2016-7-21

@author: kemin.yu
'''

def singleton(cls, *args, **kw):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton

@singleton
class MyClass(object):
    a = 1;
    def __init__(self, x=0):
        self.x = x
        
def demo():
    one = MyClass()  
    two = MyClass()  
     
    two.a = 3  
    print one.a  #3  
    print two.a  #3  
    print id(one)  #34722536
    print id(two)  #34722536
    print one == two  #True  
    print one is two  #True  
    one.x = 1  
    print one.x  #1  
    print two.x  #1 

#使用__metaclass__（元类）的高级python用法  
class Singleton2(type):  
    def __init__(cls, name, bases, dict):  
        super(Singleton2, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(self, *args, **kw):  
        if self._instance is None:  
            self._instance = super(Singleton2, self).__call__(*args, **kw)  
        return self._instance  
 
class MyClass2(object):  
    __metaclass__ = Singleton2  
    
def demo2:
    one = MyClass2()  
    two = MyClass2()  
     
    two.a = 3  
    print one.a  #3  
    print id(one)  #31495472  
    print id(two)  #31495472  
    print one == two  #True  
    print one is two  #True  

if __name__ == '__main__':
    demo2()
    