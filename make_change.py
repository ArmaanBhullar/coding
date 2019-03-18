#!/bin/python3
import math
import os
import random
import re
import sys
import numpy as np
#import functools
# Complete the getWays function below.
#@functools.lru_cache(maxsize=500)

def give_stupid_list(n, m, val):
    #returns an empty array with values val
    return [[val]*m for x in range(n)]

def getWays(n, ind):
    if ind==len(val):
        return 0
    min_el = min(val[ind:])
    if n<min_el:
        return 0
    if n==min_el:
        return 1
    if has_seen[n][ind]:
        return way_counts[n][ind]
    else:
#        print(n, ind)
        ans = getWays((n-min_el), ind)+getWays(n, ind+1)
        has_seen[n][ind] = True
        way_counts[n][ind] = ans
    return way_counts[n][ind]

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    import sys
    sys.setrecursionlimit(15000)
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])
    global has_seen
    global way_counts
    c = list(map(int, input().rstrip().split()))
#    n=10
#    m=4
#    c=[2,5,3,6]
    global val
    val=sorted(c)
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    has_seen = give_stupid_list(n+1, m+1, False)
    way_counts = give_stupid_list(n+1, m+1, 0)
    ways = getWays(n, 0)
    print(ways)
    #fptr.close()
