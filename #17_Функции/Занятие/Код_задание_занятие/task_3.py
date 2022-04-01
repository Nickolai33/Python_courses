import math


def square(a):
    p = 4 * a
    s = a ** 2
    d = math.sqrt(2) * a

    return p, s, d


print(square(int(input('Введите сторону квадрата: '))))
