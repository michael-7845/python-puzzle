#!/usr/bin/python
#coding:utf-8
'''
Created on 2016年8月3日

@author: kemin.yu
'''

class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
    def __str__(self):
        return "(value:%s, next:%s)" % (self.value, self.next)
        
def demo():
    node = Node(2)
    print node
    
if __name__ == '__main__':
    demo()
    