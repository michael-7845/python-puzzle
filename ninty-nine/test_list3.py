#coding=utf-8
'''
Created on 2016-7-29

@author: kemin.yu
'''

import unittest
from list3 import *

class List3TestCase(unittest.TestCase):
    def testP21(self):
        self.assertListEqual(p21(["a", "b", "c", "d"], 2, "alfa"), ["a", "alfa", "b", "c", "d"])
        self.assertListEqual(p21(["a", "b", "c", "d"], 1, "alfa"), ["alfa", "a", "b", "c", "d"])
        self.assertListEqual(p21(["a", "b", "c", "d"], 5, "alfa"), ["a", "b", "c", "d", "alfa"])
    
    def testP22(self):
        self.assertListEqual(p22(4, 9), [4, 5, 6, 7, 8, 9])
    
    def testP23(self):
        func = p23
        r = func(6, 1, 49)
#        print r
        for item in r:
            self.assertIn(item, range(1, 49))
        self.assertEqual(len(r), 6)
        
    def testP24(self):
        func = p24d
        l = ["a", "b", "c", "d", "e", "f", "g", "h"]
        r = func(l, 3)
#        print r
        for item in r:
            self.assertIn(item, l)
        self.assertEqual(len(r), 3)
        self.assertEqual(len(set(r)), 3)
        
    def testP25(self):
        func = p25b
        l = ["a", "b", "c", "d", "e", "f"]
        r = func(l)
#        print r
        for item in r:
            self.assertIn(item, l)
        self.assertEqual(len(r), 6)
        self.assertEqual(len(set(r)), 6)
        
    def testP26(self):
        l = ["a", "b", "c", "d", "e", "f"]
        r = p26(l, 3)
        self.assertEqual(len(r), 20)
    
    def testP27(self):
        l = ["aldo", "beat", "carla", "david", "evi", "flip", "gary", "hugo", "ida"]
        r = p27(l, 2, 3, 4)
        self.assertEqual(len(r), 1260)
        r = p27(l, 2, 2, 5)
        self.assertEqual(len(r), 756)
        
    def testP28(self):
        l = [("a", "b", "c"), ("d", "e"), ("f", "g", "h"), ("d", "e"), ("i", "j", "k"), ("m", "n"), ("o",)]
        self.assertListEqual(p28(l),
                    [('o',), ('d', 'e'), ('d', 'e'), ('m', 'n'), ('a', 'b', 'c'), ('f', 'g', 'h'), ('i', 'j', 'k')])

def test():
    s = unittest.makeSuite(List3TestCase, "test")
    runner = unittest.TextTestRunner()
    runner.run(s)
    
def demo():
    c = List3TestCase("testP21")
    print c.__dict__
    print unittest.TestCase.__dict__

if __name__ == '__main__':
    test()
#    demo()
    