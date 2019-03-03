#add description from dev

class Animal(object):
    def run(self):
        print('Animal is running...')

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass


# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

# class Cat(Animal):

#     def run(self):
#         print('Cat is running...')


# dog = Dog()
# dog.run()

# cat = Cat()
# cat.run()


# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型

# isinstance(a, list)

# print(isinstance(c, Animal))


def run_twice(a):
    a.run()
    a.run()

run_twice(Animal())
run_twice(Dog())


class Tortoise(Animal):
    pass
    # def run(self):
    #     print('Tortoise is running slowly...')

run_twice(Tortoise())