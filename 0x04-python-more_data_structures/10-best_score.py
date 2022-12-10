#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    bestScore = list(a_dictionary.values())[0]
    bestKey = list(a_dictionary.keys())[0]
    for i, j in a_dictionary.items():
        if j > bestScore:
            bestScore = j
            bestKey = i

    return (bestKey)
