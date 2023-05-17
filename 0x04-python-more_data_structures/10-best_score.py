#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = sorted(a_dictionary.values())[-1]
        for k, v in a_dictionary.items():
            if v == val:
                return k
