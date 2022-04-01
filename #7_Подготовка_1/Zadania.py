# 1
# ch_1 = 3
# ch_2 = 'abc'
# ch_3 = ch_1
# ch_1 = ch_2
# ch_2 = ch_3
# print(ch_1, ch_2)

# 2
# ch = input('Введите натуральное число: ')
# s = 0
# for i in ch:
#     s += int(i)
# print(s)

# 3
# a = [1, -1, 2, 3, 5, -8, 13, 21, -34, 56, 89]
# for a in a:
#     if a < 0 and a % 2 == 0:
#         print(a)

# 1
# ch_1 = int(input('Введите первое число: '))
# ch_2 = int(input('Введите второе число: '))
# print("Сумма чисел -", ch_1 + ch_2)

# 2
# print("В неделе", 7 * 24 * 60 * 60, "секунд")

# 3
# print("2 в степени 18 -", 2 ** 18)

# 4
# print("остаток от деления 829 на 72 -", 829 % 72)

# 5
# ch_1 = float(input('Введите первое дробное число: '))
# ch_2 = float(input('Введите второе дробное число: '))
# print("Произведение чисел -", ch_2 * ch_1)
# print("сумма чисел", round(ch_2 + ch_1, 2))

# 6
# ch_1 = int(input('Введите первое число: '))
# ch_2 = int(input('Введите второе число: '))
# ch_3 = int(input('Введите третье число: '))
# ch_4 = int(input('Введите четвертое число: '))
# print("Среднее значение этих чисел -", (ch_4 + ch_2 + ch_3 + ch_1) / 4)

# 7
# rub = int(input("Введите количество рублей: "))
# val = input("Введите валюту, в которую хотите перевести рубли: ")
# evro = 0.338
# doll = 0.399
# ros_rub = 29.26
# if val == "доллар":
#     print(rub * doll, "- доллары")
# elif val == "евро":
#     print(evro * rub, "- евро")
# elif val == "российский рубль":
#     print(round(rub * ros_rub, 2), "- российские рубли")

# 8
# tickets = int(input('Какое количество билетиво вам нужно? '))
# popcorn = int(input('Сколько баночек попкорна вы хотите взять? '))
# price = tickets * 8 + popcorn * 11
# print("С вас", price, "рублей")

# 9
# min = int(input('Минимальный тариф: '))
# max = int(input('Максимальный тариф: '))
# days = int(input('Количество дней: '))
# econom = max * days - min * days
# print("Вы сэкономите", econom, "рублей")

# 10
# kredit = int(input("На какую сумму вы хотите взять кредит? "))
# percent = int(input("Под какой ежемесячный процент? "))
# price = kredit * ((percent * 0.01 * (1 + percent * 0.01) ** 12) / ((1 + percent * 0.01) ** 12 - 1))
# print("Вы должны заплатить -", price * 12, "рублей")

# 11
# ch_1 = int(input('Введите первое число: '))
# ch_2 = int(input('Введите второе число: '))
# ch_3 = int(input('Введите третье число: '))
# if ch_1 > ch_2 and ch_1 > ch_3:
#     print(ch_1)
# elif ch_2 > ch_3 and ch_2 > ch_1:
#     print(ch_2)
# else:
#     print(ch_3)

# 12
# ch_1 = int(input('Введите первое число: '))
# ch_2 = int(input('Введите второе число: '))
# ch_3 = int(input('Введите третье число: '))
# if ch_1 < ch_2 and ch_1 < ch_3:
#     print(ch_1)
# elif ch_2 < ch_3 and ch_2 < ch_1:
#     print(ch_2)
# else:
#     print(ch_3)

# 11/12
# ch_1 = int(input('Введите первое число: '))
# ch_2 = int(input('Введите второе число: '))
# ch_3 = int(input('Введите третье число: '))
# ch_4 = int(input('Введите первое число: '))
# ch_5 = int(input('Введите второе число: '))
# bm = input("Ищем чсило больше или меньше (б, м)?: ")
# if bm == "б":
#     if ch_1 > ch_2 and ch_1 > ch_3 and ch_1 > ch_4 and ch_1 > ch_5:
#         print(ch_1)
#     elif ch_2 > ch_3 and ch_2 > ch_1 and ch_2 > ch_4 and ch_2 > ch_5:
#         print(ch_2)
#     elif ch_3 > ch_2 and ch_3 > ch_1 and ch_3 > ch_4 and ch_3 > ch_5:
#         print(ch_3)
#     elif ch_4 > ch_3 and ch_4 > ch_1 and ch_4 > ch_2 and ch_4 > ch_5:
#         print(ch_4)
#     else:
#         print(ch_5)
# elif bm == 'м':
#     if ch_1 < ch_2 and ch_1 < ch_3 and ch_1 < ch_4 and ch_1 < ch_5:
#         print(ch_1)
#     elif ch_2 < ch_3 and ch_2 < ch_1 and ch_2 < ch_4 and ch_2 < ch_5:
#         print(ch_2)
#     elif ch_3 < ch_2 and ch_3 < ch_1 and ch_3 < ch_4 and ch_3 < ch_5:
#         print(ch_3)
#     elif ch_4 < ch_3 and ch_4 < ch_1 and ch_4 < ch_2 and ch_4 < ch_5:
#         print(ch_4)
#     else:
#         print(ch_5)

# 13
# sek = int(input('Введите количество секунд: '))
# days = sek // (60 * 60 * 24)
# hours = (sek % (60 * 60 * 24)) // (60 * 60)
# minutes = (sek % (60 * 60)) // 60
# seconds = sek % 60
# print(days, ":", hours, ":", minutes, ":", seconds, sep='')

# 14
# n = input('Введите значение n: ')
# per_1 = n + n
# per_2 = n + n + n
# print(int(n) + int(per_2) + int(per_1))

# 16
# str_1 = input("Введите строку: ")
# str_2 = input("Введите вторую строку: ")
# newlist = [str_1, str_2]
# print(newlist)

# 17
# I = ['q', 'w', 'e', 'r', 't', 'y']
# print(''.join(I))

# 18
# I1 = [17, 2, 4, 12]
# I2 = [10, 5, 4, 7]
# for i in range(0, len(I1)):
#     I3 = I1[i] * I2[i]
#     print(I3, end=', ')
# 19
# I = [3, 6, 12, 5, 2, 4, 17]
# a = min(I)
# I.remove(a)
# b = min(I)
# print(b)

# I = [1, 2, 3, 4, 5]
# a = I[1]*I[2]*I[3]*I[4]
# b = I[0]*I[2]*I[3]*I[4]
# c = I[1]*I[0]*I[3]*I[4]
# d = I[1]*I[2]*I[0]*I[4]
# e = I[1]*I[2]*I[3]*I[0]
# print([a, b, c, d, e])

# # 21
# I1 = ['a', 'b', 'c']
# I2 = ['d', 'e']
# for i in range(0, len(I1)):
#     for j in range(0, len(I2)):
#         I3 = I1[i] + I2[j]
#         print(I3)

