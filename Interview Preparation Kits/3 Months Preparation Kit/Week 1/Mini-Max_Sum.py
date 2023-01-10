#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    mx = sum(list(filter(lambda x: x != min(arr), arr)))
    mn = sum(list(filter(lambda x: x != max(arr), arr)))
    
    if mx == 0:
        mx = sum([arr[i] for i in range(len(arr)-1)])
        mn = sum([arr[i] for i in range(len(arr)-1)])
        
    print(mn, mx)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
