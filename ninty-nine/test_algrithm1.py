#coding=utf-8
'''
Created on 2016-7-29

@author: Administrator
'''
import unittest

from algrithm1 import *

class Algrithm1TestCase(unittest.TestCase):
    
    def testP31(self):
        self.assertTrue(p31(7))
        self.assertFalse(p31(10))
        
    def testP32(self):
        self.assertListEqual(p32(315), [3, 3, 5, 7]);
        self.assertListEqual(p32(33), [3, 11]);
    
    def testP33(self):
        self.assertListEqual(p33(315), [[3, 2], [5, 1], [7, 1]]);
        self.assertListEqual(p33(33), [[3, 1], [11, 1]]);
    
    def testP34(self):
        self.assertListEqual(p34(2, 10), [2, 3, 5, 7]);
        self.assertListEqual(p34(7, 31), [7, 11, 13, 17, 19, 23, 29, 31]);
        
    def testP35(self):
        self.assertTupleEqual(p35(8), (3, 5));
        self.assertSetEqual(set(p35(28)), set((23, 5)));
        
    def testP36(self):
        self.assertListEqual(p36(9, 20), [[10, (3, 7)], [12, (5, 7)], [14, (3, 11)], [16, (3, 13)], [18, (5, 13)], [20, (3, 17)]])
        self.assertListEqual(p36b([992, 1382, 1856, 1928]), [[992, (73, 919)], [1382, (61, 1321)], 
                                                            [1856, (67, 1789)], [1928, (61, 1867)]])
        
    def testP37(self):
        self.assertEqual(p37(15, 27), 3)
        self.assertEqual(p37(20, 28), 4)
        
    def testP38(self):
        self.assertTrue(p38(35, 64))
        self.assertFalse(p38(21, 56))
        
    def testP39(self):
        self.assertEqual(p39(10), 4)
    
def demo():
    pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Algrithm1TestCase.testP31']
    unittest.main()