s = 'hello everybody'
s_2 = 'Hello Everybody'
s_3 = 'Hello everybody'
# Делаем строку заголовком
print(s.title())

# Начинаем строку с заглавной буквы
print(s.capitalize())

# Переводим строку в верхний регистр
print(s.upper())

# Переводим строку в нижний регистр
print(s.lower())

# Инверсия регистра
print(s_2.swapcase())

# Проверяем, являются ли строки заголовками
print(s.istitle())
print(s_2.istitle())
print(s_3.istitle())


