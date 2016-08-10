#coding=utf-8
'''
Created on 2016-7-21

@author: kemin.yu
'''

#有两个序列a,b，大小都为n,序列元素的值任意整形数，无序； 
#要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小。 
#1. 将两序列合并为一个序列，并排序，为序列Source 
#2. 拿出最大元素Big，次大的元素Small 
#3. 在余下的序列S[:-2]进行平分，得到序列max，min 
#4. 将Small加到max序列，将Big加大min序列，重新计算新序列和，和大的为max，小的为min。 
def close_sum():
    list1 = [1, 3, 5, 7, 21]
    list2 = [2, 4, 6, 8, 12]
    
    list1.extend(list2)
    print list1
    list1.sort()
    print list1
    
    BIG = list1[-1]
    SMALL = list1[-2]
    
    min = list1[0:((len(list1)-2)/2)]
    max = list1[((len(list1)-2)/2):len(list1)-2]
    print min
    print max
    
    min.append(BIG)
    max.append(SMALL)
    print min
    print max
    print sum(min)
    print sum(max)
    
    min[3], max[3] = max[3], min[3]
    print min
    print max
    print sum(min)
    print sum(max)
    
    min[3], max[2] = max[2], min[3]
    print min
    print max
    print sum(min)
    print sum(max)

# 得到列表list的交集与差集 
def intersection_union_diff():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    
    inter = [val for val in list1 if val in list2]
    print inter
    
    union = list1 + [val for val in list2 if val not in list1]
    print union
    
    diff = [val for val in list1 if val not in list2]
    print diff

if __name__ == '__main__':
#    close_sum()
    intersection_union_diff()
    