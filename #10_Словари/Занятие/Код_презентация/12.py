# Работа со словарями
# Обход словаря с помощью цикла for

# Исходный словарь
Months = { 1:'Jan', 2:'Feb', 3:'Mar',
           4:'Apr', 5:'May', 6:'Jun',
           7:'Jul', 8:'Aug', 9:'Sep',
           10:'Oct', 11:'Nov', 12:'Dec' }

# Цикл for обхода словаря
# в цикле mn - ключ, Months[mn] - значение
for mn in Months:
    print(mn, ': ', Months[mn])




