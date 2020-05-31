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