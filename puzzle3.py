#!/usr/bin/env python3

MARGARIDA_UP = +1
DONALD_UP    = +2
GASTAO_UP    = +3

MARGARIDA_DOWN = -1
DONALD_DOWN    = -2
GASTAO_DOWN    = -3

BASE  = 0
LEFT  = 2
RIGHT = 1

KEYS = [
    (DONALD_UP, MARGARIDA_DOWN, DONALD_DOWN),
    (GASTAO_UP, DONALD_DOWN, MARGARIDA_DOWN),
    (DONALD_UP, DONALD_UP, MARGARIDA_DOWN),
    (MARGARIDA_DOWN, GASTAO_DOWN, DONALD_UP),
    (MARGARIDA_DOWN, MARGARIDA_DOWN, DONALD_UP),
    (GASTAO_DOWN, DONALD_DOWN, MARGARIDA_UP),
    (DONALD_UP, GASTAO_DOWN, GASTAO_UP),
    (GASTAO_UP, MARGARIDA_UP, MARGARIDA_DOWN),
    (MARGARIDA_DOWN, GASTAO_DOWN, MARGARIDA_UP),
]

KEY_NAMES = {
    1: "M",
    2: "D",
    3: "G",

    -1: "m",
    -2: "d",
    -3: "g"
}

def humanize(key):
    if isinstance(key, list):
        return " ".join([humanize(x) for x in key])
    elif key is None:
        return "None"
    else:
        return KEY_NAMES[key[0]] + KEY_NAMES[key[1]] + KEY_NAMES[key[2]]

def shift_rotate(keys, value):
    return keys if value == 0 else keys[value:] + keys[:value]

def check_constraints(state, i, constraints):
    for other, position in constraints[i]:
        if other >= i:
            continue
        if other >= len(state):
            continue
        if state[other] is None:
            continue
        if state[i][position] == -state[other][position]:
            continue
        return False
    return True

def _bruteforce(state, keys, used, i, constraints, solutions):
    if i == len(state):
        solutions.append([x for x in state])
        return

    for k, key in enumerate(keys):
        if used[k]:
            continue

        used[k] = True

        for rotate in range(3):
            state[i] = shift_rotate(key, rotate)

            if check_constraints(state, i, constraints):
                _bruteforce(state, keys, used, i+1, constraints, solutions)

        used[k] = False
    state[i] = None

def bruteforce(max_keys, constraints):
    state = [None for _ in range(max_keys)]
    used  = [False for _ in KEYS]
    solutions = []

    for i in range(max_keys):
        if not i in constraints:
            constraints[i] = []
    
    _bruteforce(state, KEYS, used, 0, constraints, solutions)
    return solutions
