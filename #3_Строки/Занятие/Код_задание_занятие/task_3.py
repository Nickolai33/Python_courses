# На вход подается непустая строка S. В строке хотя бы два символа.
# В первой строке распечатайте каждый 3-й символ, начиная с нулевого (подряд, не разделяя символы пробелами).
# Во второй строке распечатайте первый и последний символы (подряд, не разделяя символы пробелами).
# В третей строке распечатайте S в верхнем регистре.
# В четвертой строке распечатайте S в обратном порядке.
# В пятой строке напечатайте True, если все символы в строке S — цифры и False в противном случае.

s = input()

print(s[::3])                                       # 1
print(s[:1] + s[-1:])                               # 2
print(s.upper())                                    # 3
print(s[::-1])                                      # 4
print(s.isdigit())                                  # 5


#s = 'Come crawling faster, obey your master!'




