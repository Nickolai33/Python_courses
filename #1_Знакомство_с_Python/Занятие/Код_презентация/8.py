from math import sin, cos, pi

a = float(input('a = '))

y = 2 * sin(3 * pi - 2 * a) ** 2 * cos(5 * pi + 2 * a) ** 2
print('y =', y)

z = 1 / 4 - 1 / 4 * sin(5 / 2 * pi - 8 * a)
print('z =', z)

