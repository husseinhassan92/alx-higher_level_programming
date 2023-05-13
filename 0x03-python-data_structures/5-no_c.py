#!/usr/bin/python3
def no_c(my_string):
    string = [chr for chr in my_string if chr not in ('c', 'C')]
    return ("".join(string))
