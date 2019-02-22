# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum

# def calc_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax

# print(calc_sum(1,2,3))
# f= lazy_sum(1,2,3,4)
# print(f())


# f1 = lazy_sum(1, 3, 5, 7, 9)
# f2 = lazy_sum(1, 3, 5, 7, 9)

# print(f1==f2)

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#     return fs

# fx1, fx2, fx3 = count()

# print(fx1())
# print(fx2)
# print(fx3)

# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
#     return fs

# f1, f2, f3 = count()
# print(f1())

# f= [0]
# print(f[0])

def createCounter():
    f = 0
    print('闭包外--')
    def counter():
        print('闭包内--')
        nonlocal f
        f = f + 1
        return f
    return counter

counterA = createCounter()
print(counterA())
print(counterA())