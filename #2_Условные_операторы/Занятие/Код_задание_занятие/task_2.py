# Вводятся три целых числа. Определить какое из них наибольшее.

a = int(input())
b = int(input())
c = int(input())


if a > b and a > c:
    print('Наибольшее: ', a)
else:
    if b > c:
        print('Наибольшее:', b)
    else:
        print('Наибольшее:', c)

