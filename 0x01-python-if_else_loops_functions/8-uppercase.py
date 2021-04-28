#!/usr/bin/python3
def uppercase(str):
    for upp in (str):
        upp = ord(upp)
        if upp >= 97 and upp <= 122:
            upp = (upp - 32)
        print("{}".format(chr(upp)), end="")
    print("")
