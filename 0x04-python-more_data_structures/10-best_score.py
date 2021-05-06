#!/usr/bin/python3
def best_score(a_dictionary):
    if (a_dictionary) is None:
        return None
    val_ordenados = (sorted(a_dictionary.items(), key=lambda dict: dict[1]))
    return (val_ordenados[-1][0])
