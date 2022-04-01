#6. Ввести почтовый адрес. Проверить доменной имя. В случае если оно gmail.com, вывести на экран имя почтового ящика.
# Иначе вывести надпись “ DOMAIN NAME is not supported’
#см. подсказку для первого задания

mail = input('Введите почтовый адрес: ')
if 'gmail.com' in mail:
    print(mail)
else:
    print('DOMAIN NAME is not supported')