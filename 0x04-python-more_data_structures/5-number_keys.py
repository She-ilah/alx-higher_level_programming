#!/usr/bin/python3
def number_keys(a_dictionary):
    res = 0
    list_keys = list(a_dictionary.keys())

    for i in list_keys:
        res += 1

    return (res)
