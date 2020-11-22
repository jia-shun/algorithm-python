def quick_sort(array):
    """快速排序, s是列表"""
    if len(array) < 2:
        return
    p = array[0]
    L = []
    E = []
    R = []

    while len(array) > 0:
        if array[-1] < p:
            L.append(array.pop())
        elif array[-1] == p:
            E.append(array.pop())
        else:
            R.append(array.pop())

    quick_sort(L)
    quick_sort(R)
    array.extend(L)
    array.extend(E)
    array.extend(R)


if __name__ == '__main__':
    array = [1, 7, 9, 3, 5]
    quick_sort(array)
    print(array)
