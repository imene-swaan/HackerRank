if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

list1=list(arr)
l = []
for i in list1:
    if i == max(list1):
        continue
    else:
        l.append(i)

print(max(l))
