import random
N = 4
M = 4

A = [[0] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(10, 90)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

item = int(input("Введите число: "))
print()

for i in range(N):
    if item in A[i]:
        print("Строка (index):", i)
print()

for j in range(M):
    for i in range(N):
        if A[i][j] == item:
            print("Колонка (index):", j)
print()
