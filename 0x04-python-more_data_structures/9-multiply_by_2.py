#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {k: val * 2 for k, val in a_dictionary.items()}
    return (new_dictionary)
