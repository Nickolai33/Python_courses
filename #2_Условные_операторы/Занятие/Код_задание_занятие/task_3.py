# Написать примитивный калькулятор. Пользователь должен ввести число,
# потом операцию (+-/*) и потом ещё одно число, после этого
# пользователь получает ответ. Числа могут быть дробными

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
s = input("Введите операцию которую вы хотите сделать: ")

if s == "+":
    print(a+b)
elif s =="-":
    print(a-b)
elif s == "*":
    print(a*b)
elif s == "/":
    print(a/b)
elif s == "%":
    print(a%b)
elif s == "^":
    print(a**b)