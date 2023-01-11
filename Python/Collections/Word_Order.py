from collections import Counter
n = int(input())
l = []
for _ in range(n):
    string = input()
    l.append(string)
s = set(l)
print(len(s))
d =  Counter(l)
for i in d.values():
    print(i, end = ' ')
