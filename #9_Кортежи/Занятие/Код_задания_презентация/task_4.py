A = (13, 5, 43, 49, 67, 32, 12, 98, 6, 10, 34, 20, 55, 68, 14, 60, 14)
B = (53, 21, 4, 23, 76, 3, 43, 12, 54, 342, 21)
s_A = sum(A)
s_B = sum(B)
if s_A > s_B:
    print("Сумма больше в кортеже - A")
else:
    print("Сумма больше в кортеже - B")

print('min A', min(A), 'Номер - ', A.index(min(A)))
print('min B', min(B), 'Номер - ', B.index(min(B)))
