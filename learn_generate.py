#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

# g = (x * x for x in range(10))

# print(g)
# print(next(g))

# for i in range(9):
#     print(next(g))


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b

        # a, b = b, a + b
        t= (b,a+b)
        a= t[0]
        b= t[1]
        n = n + 1
    return 'done'


# print(fib(10))

# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o = odd()
# print(next(o))
# print(next(o))

# for n in fib(6):
#     print(n)

g = fib(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break