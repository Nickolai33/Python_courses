import random

M = int(input('Введите M: '))
N = int(input('Введите N: '))

A = [[0] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(1, 100)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

