# 7. Напишите программу, демонстрирующую работу try\except\finally.

dict = {'a': 0, 'b': 5, 'c': 7, 'power': 200, 'RB': 'Freedom'}

try:
    a = input('Введите ключ: ')
    value = dict[a]
except KeyError:
    print('Такой ключ в данном словаре не найден!')
finally:
    print('Конец кода.')
