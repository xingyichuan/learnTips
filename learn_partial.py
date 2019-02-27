print(int('12345', base=8))

def int2(x, base=2):
    return int(x, base)

print(int2('1000000'))

import functools
int2 = functools.partial(int, base=2)

print(int2('10000', base=8))

kw= {'base':2}
print(int('10001',**kw))


max2 = functools.partial(max, 10)

max2(5,6,7)

args = (10, 5, 6, 7)
max(*args)