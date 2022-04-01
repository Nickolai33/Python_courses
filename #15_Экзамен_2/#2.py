# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
import random

list = [random.randint(0, 5) for i in range(10)]
print(f'Дан список: {list}.')
list_2 = []
for i in list:
    list.count(i)
    if list.count(i) >= 2:
        c = [i, i]
        list_2.append(c)
        list.remove(i)
        list.remove(i)
print(f'Равные пары: {list_2}.')
print(f'Количество пар: {len(list_2)}.')
