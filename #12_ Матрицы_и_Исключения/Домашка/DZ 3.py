# Умножить bruce_willis на пятый элемент строки, введенный пользователем

bruce_willis = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
leeloo = int(input_data[4])
result = bruce_willis * leeloo
print(f"- Leeloo Dallas! Multi-pass № {result}!")

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение

