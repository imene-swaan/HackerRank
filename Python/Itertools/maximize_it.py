# Enter your code here. Read input from STDIN. Print output to STDOUT

k, m = [int(i) for i in input().split()]

N = []
for i in range(k):
    N.append([int(i)**2 for i in input().split()][1:])


from itertools import product

s = []
for i in product(*N):
    s.append(sum(list(i))%m)

    
print(max(s))
