# Операция del - удаление элемента из словаря

# Исходный словарь
Salary = {'None': 120800.0,
          'Secretary': 101150.25,
          'Locksmith': 188200.00}

print(Salary)
# Удалить элемент по ключу 'Secretary'
del Salary['Secretary']
print(Salary)

# Попытка удалить несуществующий ключ
# del Salary[5] - так нельзя, генерируется исключение KeyError: 5
# del Salary['None'] - тоже запрещено


