import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))


test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')


print(re.split(r'\s+', 'a b   c'))
print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')

for i in range(3):
    print(m.group(i))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
for i in range(4):
    print(m.group(i))

print(re.match(r'^(\d+)(0*)$', '102300').groups())

print(re.match(r'^(\d+?)(0*)$', '102300').groups())

import re

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

re_telephone.match('010-12345').groups()
re_telephone.match('010-8086').groups()
