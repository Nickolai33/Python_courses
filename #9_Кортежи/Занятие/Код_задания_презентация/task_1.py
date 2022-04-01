import random

a = [random.randint(0, 100) for i in range(10)]
b = tuple(a)
print(b)
print('max ', max(a), 'min ', min(a))


