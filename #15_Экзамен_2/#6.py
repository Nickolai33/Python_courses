# 6. Даны два списка чисел.
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.
import random

list = [random.randint(0, 5) for i in range(10)]
print(f'Дан список №1: {list}.')
list_2 = [random.randint(0, 5) for i in range(10)]
print(f'Дан список №2: {list_2}.')
list_3 = []
for i in list:
    if i in list_2:
        list_3.append(i)
print(f'Пересечения: {list_3}.')
print(f'Количество пересечений в обоих списках равно: {len(list_3)}.')
