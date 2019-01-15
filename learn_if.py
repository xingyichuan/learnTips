age = 20
if age >= 18:
    print('your age is', age)
    print('adult')


age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')


birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')
