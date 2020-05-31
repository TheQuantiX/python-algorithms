def bubble_sort(x):
    n = len(x)
    for i in range(n):
        dontNeedToSwap = True
        for j in range(n - i - 1):
            if x[j] > x[j + 1]:
                temp = x[j]
                x[j] = x[j + 1]
                x[j + 1] = temp
                dontNeedToSwap = False
        if dontNeedToSwap:
            break
    return x
