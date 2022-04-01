# #1. Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.
import random

N = 5
M = 5
A = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
         A[i][j] = random.randint(1, 10)
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
max_sum = 0
stroka = 0
x = 0
for z in A:
    if sum(z) > max_sum:
        max_sum = sum(z)
        stroka = x
        x = x + 1
print(f'Сумма больше в строке - {stroka + 1}, сумма - {max_sum}.')



# #2. Ввод с клавиатуры.
# Если строка введённая с клавиатуры – это числа, то поделить первое на второе. Обработать ошибку деления на ноль.
# Если второе число 0, то программа запрашивает ввод чисел заново.
# Также если были введены буквы, то обработать исключение.
while True:
    print('Что бы выйти из программы введите "000"')
    a = input('Введите что-нибудь: ')
    b = input('Введите ещё что-нибудь: ')
    try:
        c = int(a) / int(b)
    except ZeroDivisionError:
        print('--->>> На ноль делить нельзя!')
        print()
    except ValueError:
        print('--->>> Введите числа!')
        print()
    else:
        print(c)
        print()
    if b == '000' or a == '000':
        print('--->>> Выход из программы')
        break