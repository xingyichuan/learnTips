# from collections.abc import Iterable
# from collections.abc import Iterator

# def f(x):
#     return x*x

# # r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# # #print(list(r))
# # print(next(r))
# # print(isinstance([1, 2, 3, 4, 5, 6, 7, 8, 9], Iterator))


# L = []
# for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     L.append(f(n))
# print(L)

# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# from functools import reduce

# def add(x, y):
#     return x + y

# print(reduce(add, [1, 3, 5, 7, 9]))

# def fn(x, y):
#     return x * 10 + y

# print(reduce(fn, [1, 3, 5, 7, 9]))

# def char2num(s):
#      digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#      return digits[s]


# print(list(map(char2num,'12345')))

# print(reduce(fn, map(char2num, '12345')))


# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))

from functools import reduce



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': -1}



def str2float(s):
     a = 0
     def calfloat(x, y):
          nonlocal a
          if y == -1:
               a = 1
               return x 

          if a == 0:
               return x * 10 + y
          else:
               a= a * 10
               return x + y/a

     return reduce(calfloat, map(char2num,s))  


def char2num(s):
     return DIGITS[s]


# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }


# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0.0)


# print(list(map(char2num,'123.456')))
print(str2float('123.456'))