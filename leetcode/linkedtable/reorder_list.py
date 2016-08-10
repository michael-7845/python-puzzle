#!/usr/bin/python
#coding:utf-8
'''
Created on 2016��8��4��

@author: kemin.yu
'''

"""
Given a singly linked list L: L0->L1-> ... ->Ln-1->Ln,
reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

For example, given {1,2,3,4}, reorder it to {1,4,2,3}. You must do this in-place without altering the nodes' values.
"""

from queue import Queue
from stack import Stack
from node import Node

def answer(a): #使用一个栈从两个方向获取数值
    c = Queue()
    
    b = Stack()
    cur = a.element()
    while cur != None:
        b.push(Node(cur.value))
        cur = cur.next
    
    c = Queue()
    a_pre = a.element()
    add_a_pre = False # queue length is odd
    while a.element().value != b.peek().value and \
          a_pre.value != b.peek().value:
        if a_pre.value == b.peek().value:
            add_a_pre = True
        a_pre = a.remove()
        c.add(Node(a_pre.value))
        c.add(Node(b.pop().value))
        
    if add_a_pre: # odd
        c.add(Node(a_pre.value))
    else: # even
        c.add(Node(a.remove().value))
        
    return c

def answer2(a): #使用快慢指针来均分链表， 然后把后面一半倒序
    slow = fast = a.first
    while fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            fast = fast.next
        if fast == a.last:
            break;
    
    mid = slow
    b = Queue()
    while slow:
        b.add(slow)
        slow = slow.next
    import reverse_list
    b2 = reverse_list.answer(b)
    
    r = Queue()
    _a = a.first
    _b = b.first
    while _a.value != mid.value:
        r.add(Node(_a.value))
        r.add(Node(_b.value))
        _a = _a.next
        _b = _b.next
    if _b:
        r.add(Node(_b.value))
      
    return r
    
def answer3(a): #使用快慢指针来均分链表， 然后把后面一半倒序, 拆分为2个队列，上看去更简洁
    slow = fast = a.first
    pre = None
    while fast:
        pre = slow
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            fast = fast.next
        if fast == a.last:
            break;
    pre.next = None
    a.last = pre
    
    b = Queue()
    while slow:
        b.add(slow)
        slow = slow.next
    import reverse_list
    b2 = reverse_list.answer(b)
    
    r = Queue()
    while a.element() and b.element() :
        r.add(Node(a.remove().value))
        r.add(Node(b.remove().value))
    if b.element():
        r.add(Node(b.remove().value))
      
    return r
    
def demo():
    a = Queue()
    a.add(Node(1)); a.add(Node(2)); a.add(Node(3)); a.add(Node(4)); a.add(Node(5)) #; a.add(Node(6))
    print a
    print answer3(a)

if __name__ == '__main__':
    demo()
    