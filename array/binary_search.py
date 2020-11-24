def binary_search(array, key):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if array[mid] < key:
            start = mid + 1
        elif array[mid] > key:
            end = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    s = [1, 2, 3, 4, 5, 6]
    index = binary_search(s, 4)
    print(index)
