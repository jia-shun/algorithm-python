def quick_sort(s):
    """快速排序, s是列表"""
    if len(s) < 2:
        return
    p = s[0]
    L = []
    E = []
    R = []

    while len(s) > 0:
        if s[-1] < p:
            L.append(s.pop())
        elif s[-1] == p:
            E.append(s.pop())
        else:
            R.append(s.pop())

    quick_sort(L)
    quick_sort(R)
    s.extend(L)
    s.extend(E)
    s.extend(R)


if __name__ == '__main__':
    array = [1, 7, 9, 3, 5]
    quick_sort(array)
    print(array)
