import random

N = 5
M = 5

A = [[0] * M for i in range(N)]

for i in range(N):
    for j in range(M):
        A[i][j] = random.randint(10, 90)

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()

maxRow = 0
idRow = 0
i = 0
for row in A:
    if sum(row) > maxRow:
        maxRow = sum(row)
        idRow = i
    i += 1
print(idRow, '-', maxRow)
