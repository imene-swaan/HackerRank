# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = (int(x) for x in input().split())
arr = input().split()
likes = set(input().split())
dislikes = set(input().split())
happiness = 0

for num in arr:
    happiness += 1 if num in likes else 0
    happiness -= 1 if num in dislikes else 0
    
print(happiness)
