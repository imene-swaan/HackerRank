# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
from itertools import groupby



N = int(input())

for _ in range(N):
    c = input()
    l = len(c)
    
    if (l != 16) and (l != 19):
        print('Invalid')
        continue
     
    else:
        path = re.compile('[456][0-9]{3}\-?[0-9]{4}\-?[0-9]{4}\-?[0-9]{4}')
        f = re.findall(path, c)
    
    if len(f) == 0:
        print('Invalid')
        continue
    else:
        c = re.sub('\-', '', f[0])
    
    groups = groupby(c)
    result = [sum(1 for _ in group) for label, group in groups]
    
    if max(result) > 3 :
        print('Invalid')
        continue
    
    print('Valid')
  
        
