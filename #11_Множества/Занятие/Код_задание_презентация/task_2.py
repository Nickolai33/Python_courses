# 1. Создаем словарь
dct = {1: 'value_1', 2: 'value_2', 3: 'value_3'}
print(dct)
# 2. Добавляем в словарь новый элемент с ключом 'str_key' и значением 12345
dct['str_key'] = 12345
print(dct)

# 3. Добавляем в словарь новый элемент с ключом ('it', 'is', 'tuple') и значением [11, 22, 'list_value', 33, {1, 2, 3}]
dct[('it', 'is', 'tuple')] = [11, 22, 'list_value', 33, {1, 2, 3}]
print(dct)

# 4. Получаем элемент словаря по ключу 'str_key'
# Способ 1: Напрямую - в случае отсутствия ключа формируется исключение
item_by_key_v1 = dct['str_key']
print(item_by_key_v1)
# Способ 2: Через функцию get() - в случае отсутствия ключа возвращается дефолтное значение 'No item'
item_by_key_v2 = dct.get('str_key', 'No item')
print(item_by_key_v2)

# 5. Удаляем элемент с ключом '2' из словаря
item_deleted = dct.pop(2, 'No item')
print(item_deleted)

# 6. Получаем ключи словаря

keys = dct.keys()
print(keys)
