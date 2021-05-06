#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nueva = my_list.copy()
    if my_list:
        for count in nueva:
            if count % 2 == 0:
                nueva[count] = True
            else:
                nueva[count] = False
        return (nueva)
