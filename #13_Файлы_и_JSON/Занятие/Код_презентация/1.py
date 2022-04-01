# f = open(file_name, access_mode)
#
#
f = open('example.txt', 'r')  # открыть файл из рабочей директории в режиме чтения
# fp = open('C:/xyz.txt', 'r')  # открыть файл из любого каталога


print(*f)  # выводим содержимое файла
print(f)  # выводим объект

