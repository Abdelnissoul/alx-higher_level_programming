#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for tmp in sorted(a_dictionary.keys()):
        print("{}: {}".format(tmp, a_dictionary[tmp]))
