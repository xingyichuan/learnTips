f=open(r'H:\project\project\learnTips\notfound.txt', 'r')
print(f.read())



# try:
#     f = open(r'H:\project\project\learnTips\notfound.txt', 'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()


# with open(r'H:\project\project\learnTips\notfound.txt', 'r') as f:
#     print(f.read())


for line in f.readlines():
    print(line.strip())


f.close()


# f = open('/Users/michael/test.jpg', 'rb')

# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

f1 = open(r'H:\project\project\learnTips\notfound.txt', 'w')
f1.write('Hello, world!')
f1.close()