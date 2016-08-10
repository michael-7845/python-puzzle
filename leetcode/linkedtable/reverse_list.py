#!/usr/bin/python
#coding:utf-8
'''
Created on 2016��8��4��

@author: kemin.yu
'''
from macpath import curdir

"""
reverse a list

For example, given {1,2,3,4}, reorder it to {4,3,2,1}. You must do this in-place without altering the nodes' values.
"""

from queue import Queue
from node import Node

def answer(a):
    pre = a.last = a.element()
    cur = a.element().next
    pre.next = None
    
    if pre == None or cur == None:
        return a
    
    while cur != None:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp  
    a.first = pre   
    return a  

def demo():
    a = Queue()
    a.add(Node(1)); a.add(Node(2)); a.add(Node(3)); a.add(Node(4)); a.add(Node(5))
    print a
    print answer(a)

if __name__ == '__main__':
    demo()
    