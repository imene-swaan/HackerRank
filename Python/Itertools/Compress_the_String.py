# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

l = []

for k,v in groupby(s):
    l.append((len(list(v)), int(k)))
    
    
print(*l)
