a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a < b:
    for i in range(a, b + 1):
        k = 0
        for q in range(2, i):
            if i % q == 0:
                k += 1
        if k == 0:
            print(i)
            
