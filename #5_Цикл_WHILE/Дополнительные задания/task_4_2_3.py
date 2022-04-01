kron = input('Eto zakaz dlya vedmaka...')
if kron.isdigit():
    kron = int(kron)
    kron25 = 0
    kron10 = 0
    kron5 = 0
    kron1 = 0
    while kron > 0:
        if (kron - 25) >= 0:
            kron25 += 1
            kron -= 25
        elif kron - 10 >= 0:
            kron10 += 1
            kron -= 10
        elif kron - 5 >= 0:
            kron5 += 1
            kron -= 5
        elif kron - 1 >= 0:
            kron1 += 1
            kron -= 1
    print(kron)
    print(kron25 + kron1 + kron5 + kron10)
else:
    print('никак вы бл"34дь не научитесь')