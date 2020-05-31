def merge_sort(x):
    n = len(x)
    if n == 0 or n == 1:
        return x
    middle = n // 2
    new_arr = []
    first = merge_sort(x[0:middle])
    second = merge_sort(x[middle:n])
    while len(first) > 0 or len(second) > 0:
        if len(first) == 0:
            new_arr.append(second[0])
            del second[0]
        elif len(second) == 0:
            new_arr.append(first[0])
            del first[0]
        elif first[0] <= second[0]:
            new_arr.append(first[0])
            del first[0]
        else:
            new_arr.append(second[0])
            del second[0]
    return new_arr