#!/usr/bin/python3
def no_c(my_string):
    str_new = ""
    for position in range(0, len(my_string)):
        if my_string[position] == 'c' or my_string[position] == 'C':
            continue
        str_new += my_string[position]
    return(str_new)
