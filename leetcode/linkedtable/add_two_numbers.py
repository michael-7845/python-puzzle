#!/usr/bin/python
#coding:utf-8
'''
Created on 2016��8��3��

@author: kemin.yu
'''

"""
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

from queue import Queue
from node import Node

def answer(a, b):
    c = Queue()
    carry = 0
    while a.element() != None and b.element() != None:
        sum = a.remove().value + b.remove().value + carry
        c.add(Node(sum%10))
        carry = sum/10
    
    while a.element() != None:
        sum = a.remove().value + carry
        c.add(Node(sum%10))
        carry = sum/10
    
    while b.element() != None:
        sum = b.remove().value + carry
        c.add(Node(sum%10))
        carry = sum/10   
        
    if carry > 0:
        c.add(Node(carry))
    
    return c 

def demo():
    a = Queue()
    a.add(Node(2)); a.add(Node(4)); a.add(Node(5))
    print a
    
    b = Queue()
    b.add(Node(5)); b.add(Node(6)); b.add(Node(4))
    print b
    
    c = answer(a, b)
    print c

if __name__ == '__main__':
    demo()
    