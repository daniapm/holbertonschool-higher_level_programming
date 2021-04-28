#!/usr/bin/python3
import sys

parametros = len(sys.argv) - 1
if len(sys.argv) - 1 == 0:
    print("0 arguments.")
elif len(sys.argv) - 1 == 1:
    print("1 argument:")
    print("1: {}".format(sys.argv[1]))
else:
    print("{} arguments:".format(parametros))
    for count in range(1, parametros + 1):
        print("{}: {}".format(count, sys.argv[count]))
