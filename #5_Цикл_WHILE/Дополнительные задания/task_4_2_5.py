sports = int(input('Input num of athletes '))
sher1, sher2, sher3, sher4 = '', '', '', ''
i1 = 1
i2 = 2
i3 = 3
i4 = 4
while i1 <= sports:
    if i1 <= sports:
        sher1 += str(i1) + ' '
        i1 += 4
    if i2 <= sports:
        sher2 += str(i2) + ' '
        i2 += 4
    if i3 <= sports:
        sher3 += str(i3) + ' '
        i3 += 4
    if i4 <= sports:
        sher4 += str(i4) + ' '
        i4 += 4


print(sher1)
print(sher2)
print(sher3)
print(sher4)