a = input('Введите слово с верхним и нижним регистром: ')
count_up = 0
count_down = 0
sum1 = []
sum2 = []
for i in range(len(a) - 1):
    b = a[i] + a[i +1]
    if b.isdigit():
        continue
    elif b.isupper():
        count_up += 1
    elif b.islower():
        count_down += 1
for i in list(a):
    if i == 'а' or i == 'у' or i == 'о' or i == 'ы' or i == 'э' \
            or i == 'ю' or i == 'я' or i == 'ё' or i == 'и' or i == 'е':
        sum1 += i
    else:
        sum2 += i
print(f'В введённом слове пар верхнего регистра - {count_up}, нижнего - {count_down}.')
print(f'В слове {len(a)} букв(ы). Из них гласных - {sum1}, согласных - {sum2}.')