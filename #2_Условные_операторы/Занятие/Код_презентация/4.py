a = int(input())
b = int(input())
c = bool(input())

if a > 0 and b < 0:
    print("and")
elif a > 0 or b < 0:
    print("or")

if not c == False:
    print("not")

