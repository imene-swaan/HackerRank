# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = []
m = []
for i in range(n):
    s = input()
    if s in l:
        m.append(s)
    l.append(s)

print(len(l)-len(m))
        
    
    
