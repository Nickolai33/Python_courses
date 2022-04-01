# Практическое 1

a = input('Введите строку: ')
b = input('Введите символ: ')
c = ''
for i in a:
    if i != b:
        c += i
        print(c)
print('Результат: ', c)


