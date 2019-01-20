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


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append('END')
    return L

add_end()

print(add_end())

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3])
calc((1, 3, 5, 7))

def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]
print(calc1(*nums))