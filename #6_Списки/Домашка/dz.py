list = [15, 48, 'hello', 6, 19, 'world']
l = 0
h = 0
d = 0

for i in list:
    if type(i) is int:
        if i % 2 == 0:
            i = str(i)
            for k in i:
                k = int(k)
                l += k
            print(i, "Сумма цифр: ", l, "\n")
        else:
            index = list.index(i)
            list[index] = 1
    elif type(i) is str:
        for r in i:
            if r in "aeoiu":
                h += 1
            else:
                d += 1
        print(i, "\nКоличество глассных: ", h)
        print("Количество согласных: ", d, "\n")
        h = 0
        d = 0
print(list)
