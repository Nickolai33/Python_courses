import random

N = 10
a = [0] * N


def func(mn, mx):
    for i in range(N):
        a[i] = random.randint(mn, mx)


mn = int(input('Начало диапазона: '))
mx = int(input('Конец диапазона: '))
func(mn, mx)
print(a)

