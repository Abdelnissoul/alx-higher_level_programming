#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_one = [replace if x == search else x for x in my_list]
    return new_one
