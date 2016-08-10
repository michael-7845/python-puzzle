#coding=utf-8
'''
Created on 2016-7-25

@author: kemin.yu
'''

# 15个人有3个leader，分成三组，每组5个人，但是每组必须有1个leader，打印出所有组合
# 12个人有3个leader，分成三组，每组4个人，但是每组必须有1个leader，打印出所有组合
# 9个人有3个leader，分成三组，每组3个人，但是每组必须有1个leader，打印出所有组合
leader = ['a', 'b', 'c']
members = range(1,12+1)
teamsize = 5

def _remove(seq1, seq2):
    result = list(set(seq1) - set(seq2))
    return result

def demo_remove():
    t1 = range(1, 7)
    t2 = (1, 2)
    _remove(t1, t2)
    
def team_member(members, num):
    from algrithm.combination import combination4
    team1 = combination4.combination(members, num)
    for t1 in team1:
        team23 = _remove(members, t1)
        t1.append(leader[0])
        team2 = combination4.combination(team23, num)
        for t2 in team2:
            t3 = _remove(team23, t2)
            t2.append(leader[1]); t3.append(leader[2])
            print t1, t2, t3

def demo():
    team_member(members, teamsize-1)

if __name__ == '__main__':
    demo()
    