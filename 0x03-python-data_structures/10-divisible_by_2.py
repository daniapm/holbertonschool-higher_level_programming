#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None:
        return None
    nueva = my_list.copy()
    for count in nueva:
        if count % 2 == 0:
            nueva[count] = True
        else:
            nueva[count] = False
    return nueva
