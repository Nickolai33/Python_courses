a = input('Введите 7-значное число: ')
c = str(a)
b = int(a)
count1 = 0
count2 = 0
sum = 0
if len(a) == 7:
    a = int(a)
    while a > 0:
        if a % 2 == 0:
            count1 += 1
        else:
            count2 += 1
        a //= 10
else:
    print('Вы ввели не 7-значное число!')
print(f'Чётных цифр:  {count1}')
print(f'Нечётных цифр:  {count2}')
if count1 > count2:
    for i in c:
        sum += int(i)
    print(f'Сумма цифр введённого числа равна: {sum}')
elif count1 < count2:
    print(f'Произведение 1, 3 и 6 цифры равно: {int(c[0]) * int(c[2]) * int(c[5])}')