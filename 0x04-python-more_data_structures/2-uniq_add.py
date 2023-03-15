#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set()
    for element in my_list:
        if isinstance(element, int) and element not in unique_set:
            unique_set.add(element)
    return sum(unique_set)
