# help(abs)

# print(abs(-20))

# abs(1, 2)

# print(int('123'))

# a= abs
# print (a(-1))

# from abstest import my_abs 
# print (my_abs(-9))  

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny

# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)

# r = move(100, 100, 60, math.pi / 6)
# print(r)

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 2))