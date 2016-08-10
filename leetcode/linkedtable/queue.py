#!/usr/bin/python
#coding:utf-8
'''
Created on 2016��8��3��

@author: kemin.yu
'''

from node import Node
from platform import node

class Queue(object):
    '''
    queue implementation in python
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.first = self.last = None
    
    def add(self, node):
        if self.first is None:
            self.first = node
            self.last = self.first
        else:
            self.last.next = node 
            self.last = node
    
    def remove(self):
        if self.first is not None:
            node = self.first
            self.first = node.next
            return node
        else:
            return None
    
    def element(self):
        if self.first is not None:
            return self.first
        else:
            return None
        
    def __str__(self):
        cur = self.first
        s = ""
        while cur is not None:
            s += "%s -> " % cur.value
            cur = cur.next
        return s
    
def demo():
    queue = Queue()
    queue.add(Node(2))
    queue.add(Node(4))
    queue.add(Node(6))
    while queue.element() is not None:
        print queue
        print queue.remove()
        
if __name__ == "__main__":
    demo()
    