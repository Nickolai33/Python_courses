#5. Получить на ввод количество рублей и копеек и вывести в правильной форме,
# например, 3 рубля, 1 рубль 25 копеек, 3 копейки

r = input('Введите рубли: ')
k = input('Введите копейки: ')
if r[-1] == str(1):
    print(f'{r} рубль')
elif r[-1] == str(2) or r[-1] == str(3) or r[-1] == str(4):
    print(f'{r} рубля')
elif r[-1] == str(5) or r[-1] == str(6) or r[-1] == str(7) or r[-1] == str(8) or r[-1] == str(9) or r[-1] == str(0):
    print(f'{r} рублей')

if k[-1] == str(1):
    print(f'{k} копейка')
elif k[-1] == str(2) or k[-1] == str(3) or k[-1] == str(4):
    print(f'{k} копейки')
elif k[-1] == str(5) or k[-1] == str(6) or k[-1] == str(7) or k[-1] == str(8) or k[-1] == str(9) or k[-1] == str(0):
    print(f'{k} копеек')
