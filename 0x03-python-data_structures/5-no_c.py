#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for a in range(len(my_string)):
        if (my_string[a] != 'c' and my_string[a] != 'C'):
            new += my_string[a]
    return new
