# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())

tests = []

for _ in range(T):
    input()
    tests.append(list(map(int, input().split())))

def getMost(arr):
    left = arr[0]
    right = arr[-1]
    
    if right >= left:
        arr.pop()
        return right
    else:
        arr.pop(0)
        return left
    
def isStacked(blocks):
    picked = []
    picked.append(getMost(blocks))
    i = 0
    while len(blocks) != 0:
        picked.append(getMost(blocks))
        if picked[i] < picked[i+1]:
            return "No"
        i+=1
    return "Yes"
        
    
for test in tests:
    print(isStacked(test))
