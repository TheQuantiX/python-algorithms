import random

def is_sorted(x):
    for i in range(len(x) - 1):
        if x[i] > x[i + 1]:
            return False
    return True

def bogo_sort(x):
    x_new = list(x)
    while not is_sorted(x_new):
        random.shuffle(x_new)
    return x_new