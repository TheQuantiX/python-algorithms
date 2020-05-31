LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = 'abcdefghijklmnopqrstuvwxyz'

def to_uppercase(sym):
    return LETTERS[letters.index(sym)]

def to_lowercase(sym):
    return letters[LETTERS.index(sym)]

def vigenere(string, key):
    i = 0
    str_res = ''
    for j in string:
        key_sym = key[i]
        i += 1
        i %= len(key)
        if j in LETTERS and key_sym in letters:
            key_sym = to_uppercase(key_sym)
        elif j in letters and key_sym in LETTERS:
            key_sym = to_uppercase(key_sym)
        if j in letters:
            str_res += letters[(letters.index(j) + letters.index(key_sym)) % 26]
        elif j in LETTERS:
            str_res += LETTERS[(LETTERS.index(j) + LETTERS.index(key_sym)) % 26]
    return str_res