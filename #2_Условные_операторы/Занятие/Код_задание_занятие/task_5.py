# Напишите программу, которая выполняет сравнение
# двух переменных , если условие верно то выполняется
# вложенный блок части if.

x = int(input())
y = int(input())

two_values = (x < y)

if two_values:
    print(x, "меньше", y)