#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("99")
    else:
        print("{0:02d}, ".format(number), end="")
