def card_number(number):
    number = str(number)
    return "*" * len(number[:-4]) + number[-4:]


def is_palindrome(word):
    if word.lower() == word[::-1].lower():
        return True
    else:
        return False
