d = dict(name='Bob', age=20, score=88)

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d['name'])

import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# print(json.load(fp))

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))


print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))