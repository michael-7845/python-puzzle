#coding=utf-8
'''
Created on 2016-7-26

@author: kemin.yu
'''
import copy

#1. 给定整数n，返回1..n中的数的所有可能的排列
def permutation(n):
    cand = range(1, n+1)
    result = []
    getPermutation(cand, 0, result)
    return result

def getPermutation(cand, level, result):
    if level == len(cand):
        result.append(copy.deepcopy(cand))
        print cand
        return
    for i in range(level, len(cand)):
        cand[i], cand[level] = cand[level], cand[i]
        getPermutation(cand, level+1, result)
        cand[i], cand[level] = cand[level], cand[i]
        
def demo():
    print permutation(3)

if __name__ == '__main__':
    demo()
    