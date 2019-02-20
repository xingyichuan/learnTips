from collections.abc import Iterable
from collections.abc import Iterator

def f(x):
    return x*x

# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# #print(list(r))
# print(next(r))
# print(isinstance([1, 2, 3, 4, 5, 6, 7, 8, 9], Iterator))


L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce

def add(x, y):
    return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
     return digits[s]


print(list(map(char2num,'12345')))

print(reduce(fn, map(char2num, '12345')))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))