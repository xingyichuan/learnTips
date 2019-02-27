print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f= lambda x:x+x
print(f)

def build(x, y):
    return lambda: x * x + y * y

print(build(3,4))
print(build(3,4)())

L = list(filter(lambda x: x%2==1, range(1, 20)))
print(L)