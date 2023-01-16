if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        com, *args = input().split()
        args = [ int(a) for a in args]
        if com == "insert":
            L.insert(args[0], args[1])
        elif com == "print":
            print(L)
        elif com == "remove":
            L.remove(args[0])
        elif com == "append":
            L.append(args[0])
        elif com == "sort":
            L.sort()
        elif com == "pop":
            L.pop()
        elif com == "reverse":
            L.reverse()
        else:
            continue
