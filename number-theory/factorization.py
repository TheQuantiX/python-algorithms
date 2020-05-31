def factorize(x):
    n = x
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    for i in range(3, n, 2):
        while n % i == 0:
            res.append(i)
            n //= i
    if n != 1:
        res.append(n)
    return res