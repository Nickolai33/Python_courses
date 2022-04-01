# 1. создать список случайных чисел (-20, 50) на 30 элементов
#     написать алгоритмы сортировки: по возрастанию, по убыванию
#     по количеству делителей числа ( 15 - 1, 3, 5; 30 - 1, 2, 3, 5, 6, 15) -> [15, 30, ...]
import random

list = [random.randint(-20, 50) for i in range(30)]
list_1 = list.copy()
print(f'Список №1: {list}.')
print(f'Количество чисел: {len(list)}.')
list.sort()
print(f'Сортировка по возрастанию: {list}.')
list.sort(reverse=True)
print(f'Сортировка по убыванию: {list}.')
list_3 = []
for i in list:
    delitel = 0
    if i > 0:
        for j in range(1, i + 1):
            if i % j == 0:
                delitel += 1
        print(f'Число из списка: {i}, кол-во делителей: {delitel}.')
        list_3.append((i, delitel))
print(f'Список чисел с делителями: {list_3}')

def keyFunc(item):                #тут я вообще не мог допетрить как отсортировать
   return item[1]                 #думал и пробовал много времени
list_3.sort(key=keyFunc)          #и в итоге просто списал эти три строчки с инета

print(f'Сортированный список по количеству делетелей: {list_3}')

# 2. создать еще один список чисел (рандомное количество элементов)
#     найти вывести: пересечения двух списков, уникальные элементы одного и второго

list_2 = [random.randint(-20, 50) for i in range(30)]
print(f'Список №1: {list_1}.')
print(f'Список №2: {list_2}.')
a = []
for h in list_1:
    if h in list_2:
        a.append(h)
print(f'Числа, которые есть в обоих списках: {a}.')
b = []
for g in list_1:
    if g not in list_2:
        b.append(g)
print(f'Уникальные элементы одного и второго списка: {b}.')