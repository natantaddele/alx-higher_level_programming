#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_set_1 = set()
    unique_set_2 = set()
    for element in set_1:
        if element not in set_2:
            unique_set_1.add(element)
    for element in set_2:
        if element not in set_1:
            unique_set_2.add(element)
    return unique_set_1.union(unique_set_2)
