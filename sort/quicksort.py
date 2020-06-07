from insertion_sort import *

def quicksort(x):
    #Extended Quicksort with Insertion sort when length is lower of equal than 7
    n = len(x)
    if n == 0:
        return []
    if n == 1:
        return x
    if n <= 16:
        return insertion_sort(x)
    lower = []
    higheq = []
    eq = []
    pivot = insertion_sort([x[0], x[len(x) // 2], x[-1]])[1]
    for i in x:
        if i > pivot:
            higheq.append(i)
        elif i < pivot:
            lower.append(i)
        else:
            eq.append(i)
    newarr = []
    newarr.extend(quicksort(lower))
    newarr.extend(eq)
    newarr.extend(quicksort(higheq))
    return newarr
