def caesar(string, x):
    new_str = ''
    for i in string:
        if i not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_str += i
        elif i in 'abcdefghijklmnopqrstuvwxyz':
            num = 'abcdefghijklmnopqrstuvwxyz'.index(i)
            num += x
            num %= 26
            new_str += 'abcdefghijklmnopqrstuvwxyz'[num]
        else:
            num = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(i)
            num += x
            num %= 26
            new_str += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[num]
    return new_str