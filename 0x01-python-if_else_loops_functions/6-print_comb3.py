#!/usr/bin/python3
for number1 in range(0, 10):
    for number2 in range(0, 10):
        if number1 == number2:
            continue
        if number1 == 8 and number2 == 9:
            print("89")
        elif number1 < number2:
            print("{:d}{:d}, ".format(number1, number2), end="")
