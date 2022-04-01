a = input('Введите текст: ')
b = list(a)
sum1 = []
sum2 = []
for i in b:
    if i == 'а' or i == 'у' or i == 'о' or i == 'ы' or i == 'э' \
            or i == 'ю' or i == 'я' or i == 'ё' or i == 'и' or i == 'е':
        sum1 += i
    else:
        sum2 += i
print(f'Количество гласных: {len(sum1)}')
print(f'Количество согласных: {len(sum2)}')
if len(sum1) == len(sum2):
    print(f'Все гласные буквы: {sum1}')