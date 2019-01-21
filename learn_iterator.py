from collections.abc import Iterable
print(isinstance((x for x in range(10)), Iterable))


from collections.abc import Iterator
print(isinstance((x for x in range(10)), Iterator))

print(isinstance(iter('abc'), Iterator))


# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break