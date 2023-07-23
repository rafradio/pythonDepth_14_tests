""" 

    возвращает восемь королев 
    >>> ['a4', 'b7', 'c5', 'd2', 'e6', 'f1', 'g3', 'h8'] in list(calc(0, [], [], [], []))
    True

"""
def decor(func):
    def wrap(i, a, b, c, d):
        titles = 'abcdefgh'
        for c in func(i, a, b, c, d):
            yield [titles[i] + str(c[i]+1)  for i in range(8)]
    return wrap



@decor
def calc(i, a, b, c, d):
    def inner(i, a, b, c, d):
        if i < 8:
            for j in range(8):
                if j not in a and i not in b and j-i not in c and j+i not in d:
                    yield from inner(i+1, a+[j], b+[i], c+[j-i], d+[j+i])

        else: 
            yield a
    return inner(i, a, b, c, d)

# for m in calc(0, [], [], [], []):
#     print(m)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

