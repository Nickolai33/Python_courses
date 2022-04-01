print("Дано натуральное число n (n <= 9)")
n = int(input("Введите число: "))
if n <= 9:
    n_str = (str(n) + " ") * 3
    n_tab = (n_str + "\n") * n
    print(n_tab)
else:
    print("Вы ввели число, не соответствующее условиям")


