def season(num):
    if num == 12 or 1 <= num <= 2:
        print("Зима")

    elif 3 <= num <= 5:
        print("Весна")

    elif 6 <= num <= 8:
        print("Лето")

    elif 9 <= num <= 11:
        print("Осень")

    else:
        print("Неверно введён номер месяца!")


n = int(input("Введите номер месяца (1-12): "))

season(n)


# print(season(int(input("Введите номер месяца (1-12): ")))) #Выдаст дополнительно None, т.к. нет return


# season(num=int(input("Введите номер месяца (1-12): ")))