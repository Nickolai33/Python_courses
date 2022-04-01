import random

n = 0
a = int(input('Введите количество чисел: '))
b = input('Введите искомую цифру: ')
for i in range(a):
    c = random.randint(0, 1000)
    c1 = str(c)
    if b in c1:
        n += 1
    print(c1)
print(f'Искомая цифра встречается {n} раз.')