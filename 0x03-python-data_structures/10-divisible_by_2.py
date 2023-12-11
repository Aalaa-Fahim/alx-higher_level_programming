#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    list_div = []
    for i in my_list:
        if i % 2 == 0:
            list_div.append(True)
        else:
            list_div.append(False)
    return (list_div)
