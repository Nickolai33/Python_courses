n = int(input("Введите число: "))
for i in range(1, n + 1):
    if i >= 6 and i <= 11:
        continue
    elif i >= 15 and i <= 25:
        continue
    elif i >= 32 and i <=39:
        continue
    print(i)
    