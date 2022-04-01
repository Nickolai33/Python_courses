def mixed_function(a, b=2, c=3):
    return a + b + c


mixed_function(b=4, c=5)

print(mixed_function(1, b=4, c=5))  # 10

print(mixed_function(1))  # 6
