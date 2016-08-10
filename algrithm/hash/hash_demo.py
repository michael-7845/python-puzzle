#coding=utf-8
'''
Created on 2016-7-31

@author: kemin.yu
'''

num = 6
factor = 2
#table = [None] * num*factor
size = 100
table = [None] * size

def _print_table():
    print "====== table ======"
    line1 = line2 = ""
    for i in range(size):
        line1 += " %4s ," % i
        if table[i] is None:
            line2 += " %4s ," % ""
        else:
            line2 += " %4s ," % table[i]
        if (i+1) % 20 == 0:
            print line1
            print line2
            print "--------------------"
            line1 = line2 = ""

def _getDict(n):
    import random
    result = {}
    for i in range(n):
        k = random.randint(0, n*factor-1)
        result[k] = str(i)
    return result
    
# hash(k, v)
# t: table
# k: int
# v: str

# 直接定址法 
def hash1(k, v, t):
    t[k] = v
    
def demo1():
    d = _getDict(num)
    for k, v in d.items():
        hash1(k, v, table)
    print sorted(d.items())
    _print_table()
    
def hash1b(k, v, t):
    def linear(a, b):
        return a*k+b
    t[linear(2, 3)] = v
    
def demo1b():
    d = _getDict(num)
    for k, v in d.items():
        hash1b(k, v, table)
    print sorted(d.items())
    _print_table()

#数字分析法
# 平方取中
def hash2(k, v, t):
    index = k * k / 100 % 100
    t[index] = v
    
def demo2():
    d = {1123: "zero", 2356: "mike", 3921: "john"}
    for k, v in d.items():
        hash2(k, v, table)
    print sorted(d.items())
    _print_table()
    
# 折叠法
def hash2b(k, v, t):
    rest = k;
    sum = 0
    while rest > 100:
        sum += rest % 100
        rest = rest / 100
    sum += rest
    sum %= 100
    t[sum] = v
    
def demo2b():
    d = {11234578: "zero", 23212356: "mike", 39215672: "john"}
    for k, v in d.items():
        hash2b(k, v, table)
    print sorted(d.items())
    _print_table()
    
# 除留余数法
def hash2c(k, v, t):
    t[k%100] = v
    
def demo2c():
    d = {11234578: "zero", 23212356: "mike", 39215672: "john"}
    for k, v in d.items():
        hash2c(k, v, table)
    print sorted(d.items())
    _print_table()
    
# 随机数法
def hash2d(k, v, t):
    import random
    t[random.randint(0, 99)] = v
    
def demo2d():
    d = _getDict(num)
    for k, v in d.items():
        hash2d(k, v, table)
    print sorted(d.items())
    _print_table()

def demo():
    d = _getDict(10)
    print d, len(d)
    print table
    _print_table()

if __name__ == '__main__':
    demo2d()
    
