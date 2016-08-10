#coding=utf-8
'''
Created on 2016-7-26

@author: kemin.yu
'''
import copy

#3. 给定两个整数n和k，返回1..n中的k个数（可以重复）的所有可能的组合
def combination(n, k):
    result = []
    solution = []
    cand = range(1, n+1)
    getCombination(cand, k, 0, result, solution)
    return result
    
def getCombination(cand, k, level, result, solution):
    if(len(solution) == k):
        result.append(copy.deepcopy(solution))
        print solution
        return
    for i in range(level, len(cand)):
        solution.append(cand[i])
        getCombination(cand, k, level+1, result, solution)
        solution.pop(-1)
    
def demo():
#    print combination(4, 2)
    print len(combination(6, 3))

if __name__ == '__main__':
    demo()
    