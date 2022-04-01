# Практическое 3

mas = [1, 3, 4, 5, 6, 7, 8]
count = 0
count_2 = 0
for i in mas:
    if i % 2 == 0:
        count += 1
    else:
        count_2 += 1
print("Чётных: ", count, "Нечётных:", count_2)
sum = 0
pr = 1
if count > count_2:
    for i in mas:
        sum += i
    print("Сумма: ", sum)
else:
    pr = mas[0] * mas[2] * mas[5]
    print("Произведение: ", pr)

