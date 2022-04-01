money = input('how much money?/? ')
if money.isdigit():
    money = int(money)
    expenses = 0
    while money > 0:
        expense = input('input price ')
        if expense.isdigit():
            expense = int(expense)
            if expense > money:
                print('not enough money ')
                break
            money -= expense
            expenses += 1
        else:
            print('wrong input')
    print('Num of purchases ', expenses)
    print('money left ', money)
else:
    print('kekw')