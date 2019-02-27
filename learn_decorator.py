# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# @log
# def now():
#     print('2015-3-25')

# now=log(now)

# f=now

# print(f())


# import functools

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator




# @log('execute')
# def now():
#     print('2015-3-25')


# now=log("execute")(now)

# f=now

# print(f.__name__)


import  time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call %s():' % fn.__name__)
        temp = fn(*args, **kw)
        print('begin call %s():' % fn.__name__)
        return temp
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    print(x+y)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    print(x * y * z)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')