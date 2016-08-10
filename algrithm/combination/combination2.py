#coding=utf-8
'''
Created on 2016-7-26

@author: kemin.yu
'''

#2. 给定候选数字的一个集合C和一个目标数字T， 找出C中的所有的唯一的组合，使得候选数字的加和等于T
#集合C中每个数字只能够选择1次

def combinationSum(candidates, target):
    candidates.sort()
    result = []
    solution = []
    getCombination(candidates, target, 0, 0, solution, result)
    
def getCombination(candidates, target, summary, level, solution, result):
    if summary > target:
        return
    if summary == target:
        result.append(solution)
        print solution
        return
    for i in range(level, len(candidates)):
        summary += candidates[i]
        solution.append(candidates[i])
        getCombination(candidates, target, summary, i+1, solution, result)
        solution.pop(-1)
        summary -= candidates[i]

def demo():
    combinationSum([1, 3, 2], 6)

if __name__ == '__main__':
    demo()
    