#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    df = dict()
    df[k] = [x[k] for x in arr]
    indices = sorted(range(len(df[k])), key=lambda index: df[k][index])
    
    for i in range(m):
        df[i] = [x[i] for x in arr]
        df[i] = [df[i][index] for index in indices]
        
    for i in range(n):
            print(*[df[j][i] for j in range(m)])
