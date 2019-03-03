import types

class Animal(object):
    def run(self):
        print('Animal is running')


a= Animal()
print (type(a))

print(type('abc')==type(123))

def fn():
    pass

# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(lambda x: x)==types.LambdaType)
# print(type((x for x in range(10)))==types.GeneratorType)

# print(isinstance(a,Animal))
# print(isinstance('a', str))

# print(dir('ABC'))
# print('ABC'.__len__())

class MyDog(object):
     def __len__(self):
         return 100

print(MyDog().__len__())
print(len(MyDog()))


class MyObject(object):
     def __init__(self):
         self.x = 9
     def power(self):
         return self.x * self.x

obj = MyObject()
print(dir(obj))

print(hasattr(obj, 'x'))

setattr(obj, 'y', 19)
print(dir(obj))

# getattr(obj, 'z')

getattr(obj, 'z', 404)
fn = getattr(obj, 'power')


print(fn )
print(fn())