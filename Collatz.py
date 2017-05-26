import math

num = int(input("Enter a number: "))
a = 0
while a == 0:
    n = num % 2
    if n == 0:
        num = num / 2
        print(num)
    elif num == 1:
        print("Yay! It's one!")
        a += 1
    else:
        num = num * 3 + 1
        print(num)
