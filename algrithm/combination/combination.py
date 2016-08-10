#coding=utf-8
'''
Created on 2016-7-25

@author: kemin.yu
'''

#1. 给定候选数字的一个集合C和一个目标数字T， 找出C中的所有的唯一的组合，使得候选数字的加和等于T
#可以从C中无限次的选择相同的重复的数字
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
        getCombination(candidates, target, summary, i, solution, result)
        solution.pop(-1)
        summary -= candidates[i]

def demo():
    combinationSum([1, 3, 2], 6)

if __name__ == '__main__':
    demo()
    