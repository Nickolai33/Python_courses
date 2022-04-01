number1 = input('input first number ')
if number1.isdigit() == 1:
    number2 = input('input second number ')
    if number2.isdigit() == 1:
        number1 = int(number1)
        number2 = int(number2)
        print(f'{number1} плюс {number2} равно {number2 + number1}')
    else:
        print('Incorrect input ')
else:
    print('Incorrect input ')
