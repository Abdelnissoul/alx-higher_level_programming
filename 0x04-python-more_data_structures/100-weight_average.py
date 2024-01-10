#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    number = 0
    weight = 0
    for add in my_list:
        number += add[0] * add[1]
        weight += add[1]
    return (number / weight)
