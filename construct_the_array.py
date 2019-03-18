#!/bin/python3

import math
import os
import random
import re
import sys

def split_num(num):
    if num%2==0:
        return (int(num/2 + 1), int(num/2))
    else:
        return (int((num+1)/2), int((num+1)/2))

# Complete the countArray function below.


def countArray(n, maxim, start, end):
#    print('args: {},{},{},{}'.format(n, maxim, start, end))
    print("strating n is = ", n)
    if bool_ls[n][maxim][start][end]:
        return res_ls[n][maxim][start][end]
    elif (n==0) or (n==1):
        answer=0
    elif n==2:
        print('n is 2')
        if start == end:
            answer = 0
        else:
            answer = 1
    else:
        print('this should never be 2 : ', n)
        net_sum=0
        left_num, right_num = split_num(n)
        for l in range(1, maxim+1):
            net_sum=net_sum + countArray(left_num, maxim, start=start, end=l)*countArray(right_num, maxim, start=l, end=end)
        answer = net_sum

    bool_ls[n][maxim][start][end]=True
    res_ls[n][maxim][start][end]=answer
    return answer
    # Return the number of ways to fill in the array.

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])
    res_ls  = [[[[None]*(k+1)]*(k+1)]*(k+1)]*(n+1)
    bool_ls = [[[[False]*(k+1)]*(k+1)]*(k+1)]*(n+1)
    import pdb;pdb.set_trace()
    answer  = countArray(n, maxim=k, start=1, end=x)
#    print(bool_ls[3][2][2][2])
#    print(res_ls[3][2][2][2])
#    print(res_ls)

    print(answer)
#    fptr.write(str(answer) + '\n')

#    fptr.close()
