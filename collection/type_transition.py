#coding: utf-8
'''
Created on 2016-7-21

@author: Administrator
'''

# int(x [,base ])        
# long(x [,base ])       
# float(x )              
# complex(real [,imag ]) 
# str(x )                
# repr(x )               
# eval(str )             
# tuple(s )              
# list(s )               
# chr(x )                
# unichr(x )             
# ord(x )                
# hex(x )                
# oct(x )                

def number():
    print "number(): "
    n = 100
    s = "100"
    print int(s, 2)
    print int(s, 8)
    print int(s, 16)
    
    print long(n)
    
    print float(n)
    
    print complex(1, 2)
    
    s1 = hex(n)
    print s1, type(s1)
    print int(s1, 16)
    s2 = oct(n)
    print s2, type(s2)
    print int(s2, 8)
    
def string():
    print "string():"
    n = 123
    s = '456'
    
    s1 = str(n)
    print s1, type(s1)
    s2 = repr(n)
    print s2, type(s2)
    n1 = eval(s)
    print n1, type(n1)
    
def string_to_sequence():
    print "string_to_sequence():"
    s = "123"
    t = tuple(s)
    l = list(s)
    print t, type(t)
    print l, type(l)
    
def char():
    print "char():"
    c = "A"
    code = ord(c)
    c1 = chr(code)
    print code, c1
    
    u = u"A"
    u_code = ord(u)
    u1 = unichr(u_code)
    print u_code, u1

if __name__ == '__main__':
    number()
    string()
    string_to_sequence()
    char()
    
    