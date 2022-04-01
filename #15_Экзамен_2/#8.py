# 8. В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
with open('D:\PycharmProjects\WINOS\#14_Экзамен\8.txt') as file:
    count = 0
    sum = 0
    for line in file:
        count += 1
        a = len(line)
        for i in range(a):
            if line[i].isdigit():
                num = int(line[i])
                sum += num
                if num < 3:
                    print(f'Ученик, чья оценка меньше 3 баллов - {line}')
    b = sum / count
    print(f'Средний балл по классу - {b}.')