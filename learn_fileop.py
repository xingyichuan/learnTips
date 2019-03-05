import os
# print(os.name)
# print(os.uname_result)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# print(os.path.join('/Users/michael', 'testdir'))
# os.mkdir('hello')
# os.removedirs('hello')
# print(os.path.split('/Users/michael/testdir/file.txt'))
# print(os.path.splitext('/path/to/file.txt'))


# os.rename('test.txt', 'test.py')
# os.remove('test.py')

print([x for x in os.listdir('.') if os.path.isdir(x)])

print([x for x in os.listdir('project') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))