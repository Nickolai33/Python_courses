class TheExample:
    a = 2
    b = 3

    def __init__(self, t, r):
        self.t = t
        self.r = r

    def func(self):
        self.c = 5
        print(self.c)

    def func1(self):
        return self.a + self.b

    def func2(self):
        return self.t**self.r


example = TheExample(4,2)

print(example.a)
print(example.func1())
print(example.func2())
example.func()

