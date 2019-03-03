class Student(object):
    name = 'Student'
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

print(s.name)

s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问