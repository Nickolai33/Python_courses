my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["d"]
except IndexError:
    print("Такого индекса не существует!")
except KeyError:
    print("Этого ключа нет в словаре!")
except:
    print("Произошла другая ошибка!")


