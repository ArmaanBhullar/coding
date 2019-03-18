"""In this challenge, you will be given an array B and must determine an arrayA s.t.
For all i, 1<=A[i]<=B[i] .The task is to select A such that the sum of the
absolute difference of consecutive pairs of A is maximized."""
import math
import os
import random
import re
import sys

def where_el_val(ls, val):
    for el, ind in enumerate(ls):
        if el==val:
            return ind
    return None

def return_sub(ls1, ls2):
    return [x-y for x, y in zip(ls1, ls2)]

# Complete the cost function below.
def cost(B):
#    global total_cost
#    print("total_cost={}\nB={}".format(total_cost, B))
    N=len(B)
    if N<=1:
        return 0
    if N==2:
        return max(B)-1
    if (min(B)==1) and (max(B)==1):
        return 0
    if B[0]==1:
        x = B[1]
        y = B[2]
        s1 = 2*x-2
        s2 = y-1
        if s1<=s2:
            return cost([1]+B[2:])
        else:
#            total_cost = total_cost + 2*x-2
            return cost([1]+B[3:]) + 2*x-2
    if B[-1]==1:
        x = B[-2]
        y = B[-1]
        s1 = 2*y-1
        s2 = x-1
        if s1<=s2:
            return cost(B[:-2]+[1])
        else:
#            total_cost = total_cost + 2*y-2
            return cost(B[:-3]+[1]) + 2*y - 2
    min_el = min(B)
    min_ind = where_el_val(B, min_el)
    if min_el>1:
        new_arr = [min_el-1]*N
#        total_cost = total_cost+(min_el-1)*(N-1)
        return (min_el-1)*(N-1) + cost(return_sub(B, new_arr))
    else:
        return cost(B[:min_ind+1]) + cost(B[min_ind:])

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        B = list(map(int, input().rstrip().split()))
        global total_cost
        total_cost=0
        result = cost(B)
        print(result, "\n")
#        fptr.write(str(result) + '\n')

#    fptr.close()
