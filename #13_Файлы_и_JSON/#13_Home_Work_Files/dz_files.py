# Есть массив состоящий из слов и чисел.
# Нужно записать в файл сначала слова в порядке их длины, а после слов цифры в порядке возрастания.
a = ['python', 35, 'keyboard', 365, 2, 'home', 'git', 117, 'Queen']
b = []
c = []
for i in a:
    if i == str(i):
        i = str(i)
        b.append(i)
    elif i == int(i):
        i = int(i)
        c.append(i)
print(b)
print(c)
b.sort(key=len)
c.sort()
print(b)
print(c)
x = str(b)
y = str(c)
f_name = input('Имя файла: ')
f = open(f_name, 'w')
for i in b:
    f.write(i + ' ')
for i in c:
    i = str(i)
    f.write(i + ' ')
f.close()
f = open('dz.txt', 'r')
print(f.readlines())
f.close()
# f = open(f_name, )
# f.write(x + ' ' + y)
# f.close()
# f = open('dz.txt', 'r')
# print(f.read())
# f.close()
