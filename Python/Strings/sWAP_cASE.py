def swap_case(s):
    w = ''
    for i in s:
        if i == i.upper():
            i = i.lower()
        else:
            i = i.upper()
        w += i
    return w

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
