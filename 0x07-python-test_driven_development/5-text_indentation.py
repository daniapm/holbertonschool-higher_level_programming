#!/usr/bin/python3
"""
module  prints a text with 2 new lines
"""


def text_indentation(text):
    """
    prints text with 2 new lines
    argc:
        text: text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        identification = ['.', '?', ':']
    idx = 0
    for items in text:
        if items in (identification):
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1
    idx = 0
    for items in text:
        if items in identification:
            if items == '.':
                text = text.replace('.', '.\n\n')
                break
            idx = 3
        else:
            idx += 1
    idx = 0
    for items in text:
        if items in identification:
            if items == '?':
                text = text.replace('?', '?\n\n')
                break
            idx = 3
        else:
            idx += 1
    idx = 0
    for items in text:
        if items in identification:
            if items == ':':
                text = text.replace(':', ':\n\n')
                break
            idx = 3
        else:
            idx += 1
    print(text, end="")
