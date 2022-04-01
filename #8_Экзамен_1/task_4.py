import random
x = 0
my_str = ""
num_1 = input("Введите искомое число: ")
num_2 = int(input("Введите количество искомых чисел: "))
for i in range(num_2):
    n = random.randint(1, 1000)
    str_n = str(n)
    my_str = str_n + " "
    print(my_str)
    if num_1 in str_n:
        x += 1
print(f"Искомое число содержится {x} раз.")


