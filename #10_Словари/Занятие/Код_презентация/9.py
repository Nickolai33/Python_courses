# Операция in - определение наличия ключа в словаре
# Исходный словарь
Salary = { 'Director': 120800.0,
           'Secretary': 101150.25,
           'Locksmith': 188200.00 }
print(Salary)

# Удалить элемент по ключу 'Secretary' с проверкой
key = 'Secretary'
if key in Salary:
    del Salary['Secretary']
    print(Salary)

# Попытка удалить несуществующий ключ
# если ключа нету, то исключение KeyError не генерируется
key2 = 5
if key2 in Salary:
    del Salary[key2]

    