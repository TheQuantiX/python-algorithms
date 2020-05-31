import random

def insertion_sort(x):
    i = 1
    while i < len(x):
        j = i
        while j > 0 and x[j-1] > x[j]:
            temp = x[j]
            x[j] = x[j - 1]
            x[j - 1] = temp
            j = j - 1
        i = i + 1
    return x

def quicksort(x):
    #Extended Quicksort with Insertion sort when length is lower of equal than 7
    n = len(x)
    if n == 0:
        return []
    if n == 1:
        return x
    if n <= 7:
        return insertion_sort(x)
    lower = []
    higheq = []
    r = random.randint(0, len(x) - 1)
    pivot = x[r]
    for i in x:
        if i >= pivot:
            higheq.append(i)
        else:
            lower.append(i)
    newarr = []
    newarr.extend(quicksort(lower))
    newarr.extend(quicksort(higheq))
    return newarr