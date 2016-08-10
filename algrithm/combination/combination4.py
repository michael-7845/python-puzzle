#coding=utf-8
'''
Created on 2016-7-26

@author: kemin.yu
'''
import copy

#3. 给定两个整数n和k，返回1..n中的k个数的所有可能的组合
#=>
#4. 给定tuple，返回tuple中的k个元素的所有可能的组合
def combination(t, k):
    result = []
    solution = []
    cand = t
    getCombination(cand, k, 0, result, solution)
    return result
    
def getCombination(cand, k, level, result, solution):
    if(len(solution) == k):
        result.append(copy.deepcopy(solution))
#        print solution
        return
    for i in range(level, len(cand)):
        solution.append(cand[i])
        getCombination(cand, k, i+1, result, solution)
        solution.pop(-1)
    
def demo():
    print combination(range(1,4+1), 2)

if __name__ == '__main__':
    demo()
    