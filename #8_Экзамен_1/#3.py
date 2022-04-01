import random

a = int(input('Введите число №1 в диапазоне от 1 до 20: '))
b = int(input('Введите число №2 в диапазоне от 1 до 20: '))
count1 = 0
count2 = 0
count3 = 0
arr = []
for i in range(7):
    c = int(random.randint(1, 20))
    d = int(random.randint(1, 20))
    arr.append(c)
    arr.append(d)
    if a + b > c + d:
        count1 += 1
    elif a + b < c + d:
        count2 += 1
    elif a + b == c + d:
        count3 += 1
print(f'Числа "a + b" > "c + d" {count1} раз(а)')
print(f'Числа "a + b" < "c + d" {count2} раз(а)')
if count3 > 0:
    print(f'Случайные числа из 4 итерации: {arr[6]} и {arr[7]}')