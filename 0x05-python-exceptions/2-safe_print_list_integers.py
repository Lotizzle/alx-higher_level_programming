#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(0, x):
        try:
            if type(my_list[i]) == int:
                print("{}".format(my_list[i]), end="")
                num += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (num)
