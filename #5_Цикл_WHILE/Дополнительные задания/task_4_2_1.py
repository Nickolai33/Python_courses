words = 0
while True:
    word = input('Enter word: ')
    words += 1
    if word == 'достаточно' or word == 'хватит' or word == 'стоп':
        words -= 1
        break
print(words)