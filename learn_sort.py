print(sorted([36, 5, -12, 9, -21]))

list1 = [36, 5, -12, 9, -21]

print(sorted(list1, key=abs))


print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))