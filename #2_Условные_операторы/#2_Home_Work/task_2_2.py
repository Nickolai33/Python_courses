#2. Запросить у пользователя возраст. Если возраст меньше 0 - вывести Wrong input,
# если меньше 18 - вывести CocaCola, иначе - вывести Beer

a = int(input('Введите Ваш возраст: '))
if a <= 0:
    print('Wrong input')
elif 0 < a < 18:
    print('CocaCola')
else:
    print('Beer!!!')