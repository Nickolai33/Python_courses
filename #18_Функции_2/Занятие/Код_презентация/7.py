def mul(a):
    def helper(b):
        return a * b

    return helper


three_mul = mul(3)

print(three_mul(5))

# print(mul(3)(2))
