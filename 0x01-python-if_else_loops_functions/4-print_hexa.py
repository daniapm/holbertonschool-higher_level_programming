#!/usr/bin/python3
for number in range(0, 98 + 1):
    hexa = hex(number)
    print("{:d} = {}".format(number, hexa), end="\n")
