#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    while i < x:
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                j += 1
            i += 1
        except (TypeError, ValueError):
            break
    print("")
    return j
