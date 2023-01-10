# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())
pattern_and = re.compile('(?<=[ ])[&]{2}(?=[ ])')
pattern_or = re.compile('(?<=[ ])[|]{2}(?=[ ])')
for _ in range(n):
    line = input()
    
    line = re.sub(pattern_and, 'and', line)
    line = re.sub(pattern_or, 'or', line)
    
    print(line)
