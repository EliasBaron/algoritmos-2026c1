def mergeSort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    l1 = mergeSort(l[:mid])
    l2 = mergeSort(l[mid:])

    return merge(l1, l2)


def merge(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    if l1[0] < l2[0]:
        return [l1[0]] + merge(l1[1:], l2)
    else:
        return [l2[0]] + merge(l1, l2[1:])


def contains(l1, l2):
    for e in l2:
        if not exists(e, l1):
            return False
    return True


def exists(e, ls):
    low = 0
    high = len(ls)
    while low < high:
        mid = (low + high) // 2
        if e == ls[mid]:
            return True
        elif e < ls[mid]:
            high = mid
        else:
            low = mid + 1
    return False


def solve():
    listA = [2, 4, 3, 1, 5, 6, 8, 3, 4, 2, 1, 4, 2]
    listB = [1, 2, 5]

    orderList = mergeSort(listA)
    print(orderList)
    print(contains(orderList, listB))


solve()
