n = int(input("Введите число: "))
for i in range(1, n + 1):
    divisor = 0
    for q in range (1, i + 1):
        if i % q == 0:
            divisor += 1
    print(i, "+" * divisor)
