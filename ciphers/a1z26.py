LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'

def a1z26(string):
    encoded = []
    for i in string:
        if i in LETTERS:
            encoded.append(LETTERS.index(i) + 1)
        elif i in letters:
            encoded.append(letters.index(i) + 1)
    encoded = ' '.join(list(map(lambda l : str(l), encoded)))
    return encoded