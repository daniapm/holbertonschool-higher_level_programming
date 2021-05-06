#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is " ":
        sentence[0:] = None
    else:
        a = len(sentence)
        b = sentence[0]
        return a, b
