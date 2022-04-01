f = open('example.txt', 'r')
try:
    print(*f)  # работа с файлом
finally:
    f.close()
