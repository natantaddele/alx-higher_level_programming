#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print(key, ":", a_dictionary[key])
