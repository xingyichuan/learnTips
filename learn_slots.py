import types
class Student(object):
    __slots__ = ('name', 'age' ) 
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

def set_fool(self, s):
    self.fool = s

def set_age(self, age): # 定义一个函数作为实例方法
     self.age = age

bob = Student('Bob')
lisa = Student('Lisa')

from types import MethodType

# bob.set_age = MethodType(set_age, bob) # 给实例绑定一个方法
# bob.set_age(25) # 调用实例方法
# print(bob.age) # 测试结果

Student.set_age=set_age
guy =Student('guy')
guy.set_age(34)
# guy.size ='big'
print(guy.age)



# setattr 为类或实例设置属性
# setattr(Student, 'fool', 'fool1')
# print('Student:', Student.fool, 'Bob:', bob.fool, 'Lisa:', lisa.fool)

# method 1: setattr为类或实例绑定方法->失败
#setattr(Student, 'set_fool', set_fool)
#Student.set_fool('fool2') # 执行失败
#setattr(bob, 'set_fool', set_fool)
#bob.set_fool('fool2') # 执行失败

# method 2: 直接为类绑定方法，所有实例皆可使用
#Student.set_fool = set_fool
#Student.set_fool('fool3') # 执行失败
#bob.set_fool('fool3') # 执行成功
#lisa.set_fool('fool3') # 执行成功

# method 3: MethodTypes单独为一个实例绑定方法，其他实例不受影响
# bob.set_fool = types.MethodType(set_fool, bob)
# bob.set_fool('fool4') # 执行成功
#lisa.set_fool('fool4') # 执行失败

# print('Student:', Student.fool, 'Bob:', bob.fool, 'Lisa:', lisa.fool)

# print(set_fool)
# print(bob.set_fool)