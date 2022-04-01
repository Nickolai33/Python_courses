my_str = input("Введите текст: ")
x = 0
my_list = my_str.split()
for i in my_list:
    if i.isdigit():
        x += 1
        print(i, end=' ')
