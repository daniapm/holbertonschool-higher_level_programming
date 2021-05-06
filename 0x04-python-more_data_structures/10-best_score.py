#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    val_ordenados = (sorted(a_dictionary.items(), key=lambda dict: dict[1]))
    return (val_ordenados[-1][0])
