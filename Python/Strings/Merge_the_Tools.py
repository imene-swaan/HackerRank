def merge_the_tools(string, k):
    # your code goes here
    a = int(len(string)/k)
    for i in range(a):
        ind = i*k
        t = list(string[ind:ind+k])
        u = []
        for j in t:
            if j in u:
                continue
            
            u.append(j)
        print(''.join(u))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
