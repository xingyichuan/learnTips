d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)


for k, v in d.items():
    print('key:{}, vaule:{}'.format(k,v))


from collections.abc import Iterable
print(isinstance('abc', Iterable))



for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)