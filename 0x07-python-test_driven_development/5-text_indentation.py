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
    count = 0
    for items in text:
        if items in (identification):
            if text[count + 1] == " ":
                text = text[:count + 1] + text[count + 2:]
        else:
            count += 1
    count = 0
    for items in text:
        if items in identification:
            if items == '.':
                text = text.replace('.', '.\n\n')
                break
            count = 3
        else:
            count += 1
    count = 0
    for items in text:
        if items in identification:
            if items == '?':
                text = text.replace('?', '?\n\n')
                break
            count = 3
        else:
            count += 1
    count = 0
    for items in text:
        if items in identification:
            if items == ':':
                text = text.replace(':', ':\n\n')
                break
            count = 3
        else:
            count += 1
    print(text, end="")
    if text is "\n":
        print("\n")
