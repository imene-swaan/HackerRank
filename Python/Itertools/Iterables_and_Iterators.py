# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
letters = input().split()
K = int(input())

from itertools import combinations

a_idx = set(idx for idx in range(N) if letters[idx] == 'a')
total, witha = 0, 0

for combination in combinations(range(N), K):
    total += 1
    if a_idx.intersection(combination):
        witha += 1

print(round(witha/total, 3))
