#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        
        t1 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")

        t2 = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
