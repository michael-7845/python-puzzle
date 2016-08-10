#!/usr/bin/python
#coding:utf-8
'''
Created on 2016��8��3��

@author: kemin.yu
'''

from node import Node

class Stack(object):
    '''
    stack implementation in python
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.top = None
        
    def pop(self):
        if self.top is not None:
            node = self.top
            self.top = node.next
            return node
        else:
            return None
    
    def push(self, node):
        if node is not None:
            node.next = self.top
            self.top = node
    
    def peek(self):
        if self.top is not None:
            return self.top
        else:
            return None
        
    def __str__(self):
        cur = self.top
        s = ""
        while cur is not None:
            s += "%s -> " % cur.value
            cur = cur.next
        return s
        
def demo():
    stack = Stack()
    stack.push(Node(2))
    stack.push(Node(4))
    stack.push(Node(6))
    while stack.peek() is not None:
        print stack
        print stack.pop()
        
if __name__ == "__main__":
    demo()
    