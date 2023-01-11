#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()

d = {}
for i in list(s):
    count = len(list(filter(lambda x: x == i ,list(s))))
    
    d[i] = count
    
my_keys = sorted(d.items(), key=lambda x: (-x[1],x[0]))[:3]

for i in my_keys:
    print(i[0], i[1])

