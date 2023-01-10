#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    neg = []
    pos = []
    zer = []
    for i in arr:
        if i < 0:
            neg.append(i)
        elif i > 0:
            pos.append(i)
        else:
            zer.append(i)
    
    print(float(len(pos)/len(arr)))
    print(float(len(neg)/len(arr)))
    print(float(len(zer)/len(arr)))
            
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
